"""
Retrieval layer: vector search (pgvector), BM25 search, and hybrid merge.

The corpus is loaded from Postgres once at startup. BM25 is built in memory.
Vector search hits the DB per query.
"""

import os
from dataclasses import dataclass
from typing import Optional

import numpy as np
import psycopg
from pgvector.psycopg import register_vector
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

MODEL_NAME = "allenai/specter"


@dataclass
class Paper:
    pmid: str
    title: str
    abstract: str
    year: Optional[int]
    journal: Optional[str] = None
    publication_types: Optional[list[str]] = None
    cited_by_count: Optional[int] = None
    oa_pdf_url: Optional[str] = None


def tokenize(text: str) -> list[str]:
    return text.lower().split()


class Retriever:
    """Loads corpus from Postgres, builds BM25, and exposes search methods."""

    def __init__(self, db_url: str, model_name: str = MODEL_NAME):
        self.db_url = db_url
        self.model = SentenceTransformer(model_name)

        # Load corpus into memory for BM25
        self.papers: list[Paper] = []
        self.pmid_to_idx: dict[str, int] = {}
        with psycopg.connect(db_url) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT pmid, title, abstract, year, journal, "
                    "publication_types, cited_by_count, oa_pdf_url FROM papers;"
                )
                for i, row in enumerate(cur.fetchall()):
                    pmid, title, abstract, year, journal, pub_types, cited, oa_url = row
                    types_list = (
                        [t.strip() for t in pub_types.split(";") if t.strip()]
                        if pub_types
                        else None
                    )
                    self.papers.append(
                        Paper(
                            pmid=pmid,
                            title=title or "",
                            abstract=abstract or "",
                            year=year,
                            journal=journal,
                            publication_types=types_list,
                            cited_by_count=cited,
                            oa_pdf_url=oa_url,
                        )
                    )
                    self.pmid_to_idx[pmid] = i

        tokenized = [tokenize(f"{p.title} {p.abstract}") for p in self.papers]
        self.bm25 = BM25Okapi(tokenized)

    def vector_search(self, query: str, k: int = 50) -> list[tuple[Paper, float]]:
        q_emb = self.model.encode(query, convert_to_numpy=True)
        with psycopg.connect(self.db_url) as conn:
            register_vector(conn)
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT pmid, 1 - (embedding <=> %s) AS similarity
                    FROM papers
                    ORDER BY embedding <=> %s
                    LIMIT %s
                    """,
                    (q_emb, q_emb, k),
                )
                rows = cur.fetchall()
        return [(self.papers[self.pmid_to_idx[pmid]], float(sim)) for pmid, sim in rows]

    def bm25_search(self, query: str, k: int = 50) -> list[tuple[Paper, float]]:
        scores = self.bm25.get_scores(tokenize(query))
        top_idx = np.argsort(scores)[::-1][:k]
        return [(self.papers[i], float(scores[i])) for i in top_idx]

    def hybrid_search(
        self, query: str, k: int = 30, alpha: float = 0.7, pool: int = 200,
        method: str = "rrf", rrf_k: int = 60,
    ) -> list[tuple[Paper, float]]:
        """
        method="rrf": Reciprocal Rank Fusion (rank-based, robust). Ignores alpha.
        method="weighted": min-max normalized weighted sum. alpha = vector weight.
        """
        v = self.vector_search(query, k=pool)
        b = self.bm25_search(query, k=pool)

        if method == "rrf":
            combined: dict[str, float] = {}
            for rank, (p, _) in enumerate(v, 1):
                combined[p.pmid] = combined.get(p.pmid, 0.0) + 1.0 / (rrf_k + rank)
            for rank, (p, _) in enumerate(b, 1):
                combined[p.pmid] = combined.get(p.pmid, 0.0) + 1.0 / (rrf_k + rank)
        else:
            v_norm = _minmax({p.pmid: s for p, s in v})
            b_norm = _minmax({p.pmid: s for p, s in b})
            combined = {}
            for pmid, s in v_norm.items():
                combined[pmid] = combined.get(pmid, 0.0) + alpha * s
            for pmid, s in b_norm.items():
                combined[pmid] = combined.get(pmid, 0.0) + (1 - alpha) * s

        ranked = sorted(combined.items(), key=lambda x: x[1], reverse=True)[:k]
        return [(self.papers[self.pmid_to_idx[pmid]], score) for pmid, score in ranked]


def _minmax(scores: dict[str, float]) -> dict[str, float]:
    if not scores:
        return {}
    vals = list(scores.values())
    lo, hi = min(vals), max(vals)
    if hi - lo < 1e-12:
        return {k: 1.0 for k in scores}
    return {k: (v - lo) / (hi - lo) for k, v in scores.items()}
