"""
Embed abstracts with SPECTER and load into Postgres.

Two input modes:

    --input data/abstracts_filtered.json    # single merged file (Option A flow)
    --year 2026                              # one year-shard from data/progress/
    (default)                                # all year-shards from data/progress/

The merged file produced by filter_corpus.py also contains OpenAlex
enrichment fields, which are populated when present.

SPECTER expects "title [SEP] abstract" as input. The model is 768-dim,
matching the schema vector(768) column.

Usage:
    uv run python scripts/embed_and_load.py --input data/abstracts_filtered.json
    uv run python scripts/embed_and_load.py                   # all year-shards
    uv run python scripts/embed_and_load.py --year 2026       # one year
    uv run python scripts/embed_and_load.py --batch-size 16   # tune for memory
"""

import argparse
import json
from pathlib import Path

import psycopg
from dotenv import load_dotenv
from pgvector.psycopg import register_vector
from psycopg.types.json import Jsonb
from sentence_transformers import SentenceTransformer

from db import resolve_url

load_dotenv()

PROGRESS_DIR = Path("data/progress")
MODEL_NAME = "allenai/specter"
DEFAULT_BATCH_SIZE = 32


def parse_args():
    p = argparse.ArgumentParser(description="Embed abstracts and load into Postgres")
    p.add_argument("--input", type=Path, default=None,
                   help="Single JSON file to load (e.g., data/abstracts_filtered.json). "
                        "Mutually exclusive with --year/year-shards mode.")
    p.add_argument("--year", type=int, default=None,
                   help="Only process this year's shard (default: all shards)")
    p.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE)
    p.add_argument("--limit", type=int, default=None,
                   help="Cap papers loaded per shard (testing)")
    p.add_argument("--target", choices=["local", "railway"], default="local")
    return p.parse_args()


def load_shard(path: Path) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def shard_paths(year: int | None) -> list[Path]:
    if year is not None:
        path = PROGRESS_DIR / f"{year}.json"
        if not path.exists():
            raise SystemExit(f"No shard at {path}")
        return [path]
    return sorted(PROGRESS_DIR.glob("*.json"))


def embed_papers(model: SentenceTransformer, papers: list[dict],
                 batch_size: int) -> list[list[float]]:
    # SPECTER input format: title and abstract joined by [SEP]
    texts = [f"{p['title']} [SEP] {p['abstract']}" for p in papers]
    embeddings = model.encode(
        texts,
        batch_size=batch_size,
        show_progress_bar=True,
        convert_to_numpy=True,
    )
    return embeddings


def upsert_papers(conn, papers: list[dict], embeddings) -> int:
    rows = [
        (
            p["pmid"],
            p["title"],
            p["abstract"],
            "; ".join(p.get("authors") or []),
            p.get("year"),
            p.get("journal", ""),
            p.get("doi", ""),
            "; ".join(p.get("publication_types") or []),
            "; ".join(p.get("mesh_terms") or []),
            "; ".join(p.get("keywords") or []),
            emb,
            # OpenAlex enrichment (None when filter_corpus.py didn't find a match)
            p.get("openalex_id"),
            p.get("cited_by_count"),
            Jsonb(p["referenced_works"]) if p.get("referenced_works") is not None else None,
            Jsonb(p["concepts"]) if p.get("concepts") is not None else None,
            p.get("oa_status"),
            p.get("oa_pdf_url"),
        )
        for p, emb in zip(papers, embeddings)
    ]
    with conn.cursor() as cur:
        cur.executemany(
            """
            INSERT INTO papers
              (pmid, title, abstract, authors, year, journal, doi,
               publication_types, mesh_terms, keywords, embedding,
               openalex_id, cited_by_count, referenced_works, concepts,
               oa_status, oa_pdf_url)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s)
            ON CONFLICT (pmid) DO NOTHING
            """,
            rows,
        )
        return cur.rowcount


def main():
    args = parse_args()
    if args.input and args.year:
        raise SystemExit("--input and --year are mutually exclusive")

    url = resolve_url(args.target)
    print(f"Target: {args.target}")

    if args.input:
        if not args.input.exists():
            raise SystemExit(f"No file at {args.input}")
        paths = [args.input]
    else:
        paths = shard_paths(args.year)
    print(f"Found {len(paths)} input file(s): {[p.name for p in paths]}")

    print(f"Loading model: {MODEL_NAME} (first run will download ~440MB)")
    model = SentenceTransformer(MODEL_NAME)

    with psycopg.connect(url) as conn:
        register_vector(conn)
        for path in paths:
            papers = load_shard(path)
            if args.limit:
                papers = papers[: args.limit]
            if not papers:
                print(f"  {path.name}: empty, skip")
                continue
            print(f"  {path.name}: embedding {len(papers)} papers...")
            embeddings = embed_papers(model, papers, args.batch_size)
            inserted = upsert_papers(conn, papers, embeddings)
            conn.commit()
            print(f"  {path.name}: inserted {inserted} new rows "
                  f"({len(papers) - inserted} already present)")

        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM papers;")
            total = cur.fetchone()[0]
    print(f"\nDone. papers table now has {total} rows.")


if __name__ == "__main__":
    main()
