"""
Initialize the Postgres database for Contra.

Connects to DATABASE_URL (loaded from .env), enables pgvector, and creates
the `papers` table. Safe to re-run: uses CREATE EXTENSION/TABLE IF NOT EXISTS.

Usage:
    uv run python scripts/init_db.py
"""

import argparse

import psycopg
from dotenv import load_dotenv

from db import resolve_url

load_dotenv()

# SPECTER2 produces 768-dim embeddings.
EMBEDDING_DIM = 768

SCHEMA = f"""
CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS papers (
    id SERIAL PRIMARY KEY,
    pmid TEXT UNIQUE NOT NULL,
    title TEXT,
    abstract TEXT,
    authors TEXT,
    year INTEGER,
    journal TEXT,
    doi TEXT,
    publication_types TEXT,
    mesh_terms TEXT,
    keywords TEXT,
    embedding vector({EMBEDDING_DIM})
);
"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--target", choices=["local", "railway"], default="local")
    args = p.parse_args()

    url = resolve_url(args.target)
    print(f"Target: {args.target}")
    print(f"Connecting to {url.rsplit('@', 1)[-1]}...")
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            version = cur.fetchone()[0]
            print(f"  {version}")

            cur.execute(SCHEMA)
            conn.commit()
            print("  Schema applied (vector extension + papers table).")

            cur.execute("SELECT extversion FROM pg_extension WHERE extname='vector';")
            row = cur.fetchone()
            print(f"  pgvector version: {row[0] if row else 'NOT INSTALLED'}")

            cur.execute("SELECT COUNT(*) FROM papers;")
            print(f"  papers row count: {cur.fetchone()[0]}")

    print("OK")


if __name__ == "__main__":
    main()
