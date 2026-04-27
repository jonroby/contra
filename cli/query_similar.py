"""
Smoke test: embed a query and run cosine similarity search against papers.

Usage:
    uv run python cli/query_similar.py "does lithium slow cognitive decline in Alzheimer's?"
    uv run python cli/query_similar.py --top 5 "amyloid beta plaque formation"
    uv run python cli/query_similar.py --target railway "..."
"""

import argparse

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector
from sentence_transformers import SentenceTransformer

from contra.db import resolve_url

load_dotenv()

MODEL_NAME = "allenai/specter"


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("query", type=str)
    p.add_argument("--top", type=int, default=10)
    p.add_argument("--target", choices=["local", "railway"], default="local")
    return p.parse_args()


def main():
    args = parse_args()
    url = resolve_url(args.target)

    print(f"Loading model {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    q_emb = model.encode(args.query, convert_to_numpy=True)

    with psycopg.connect(url) as conn:
        register_vector(conn)
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT pmid, title, year,
                       1 - (embedding <=> %s) AS similarity
                FROM papers
                ORDER BY embedding <=> %s
                LIMIT %s
                """,
                (q_emb, q_emb, args.top),
            )
            rows = cur.fetchall()

    print(f"\nQuery: {args.query!r}\n")
    for i, (pmid, title, year, sim) in enumerate(rows, 1):
        print(f"{i:2d}. [{sim:.3f}] ({year}) {title[:120]}")
        print(f"    PMID: {pmid}")


if __name__ == "__main__":
    main()
