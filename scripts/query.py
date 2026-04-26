"""
Run a query through vector, BM25, and hybrid retrieval and compare ranks.

Usage:
    uv run python scripts/query.py "does lithium slow cognitive decline in Alzheimer's?"
    uv run python scripts/query.py --top 10 --alpha 0.7 "amyloid beta plaques"
    uv run python scripts/query.py --rank-pmid 41980560 "lithium ..."  # show where a specific paper lands
"""

import argparse
import os

from dotenv import load_dotenv

from db import resolve_url
from retrieval import Retriever

load_dotenv()


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("query", type=str)
    p.add_argument("--top", type=int, default=10)
    p.add_argument("--alpha", type=float, default=0.7,
                   help="Vector weight in weighted hybrid (ignored for RRF)")
    p.add_argument("--method", type=str, default="rrf", choices=["rrf", "weighted"])
    p.add_argument("--pool", type=int, default=200)
    p.add_argument("--rank-pmid", type=str, default=None,
                   help="Print the rank of this PMID under each method")
    p.add_argument("--target", choices=["local", "railway"], default="local")
    return p.parse_args()


def show(label: str, results, rank_pmid=None):
    print(f"\n=== {label} ===")
    for i, (paper, score) in enumerate(results, 1):
        marker = " <-- TARGET" if rank_pmid and paper.pmid == rank_pmid else ""
        print(f"{i:2d}. [{score:.3f}] ({paper.year}) {paper.title[:100]}{marker}")


def find_rank(results_full, pmid):
    for i, (paper, _) in enumerate(results_full, 1):
        if paper.pmid == pmid:
            return i
    return None


def main():
    args = parse_args()
    url = resolve_url(args.target)
    print(f"Target: {args.target}")
    print("Loading retriever (model + corpus + BM25)...")
    r = Retriever(url)
    print(f"Corpus: {len(r.papers)} papers")

    n = len(r.papers)
    v_full = r.vector_search(args.query, k=n)
    b_full = r.bm25_search(args.query, k=n)
    h = r.hybrid_search(args.query, k=args.top, alpha=args.alpha,
                        pool=args.pool, method=args.method)

    show("Vector (top {})".format(args.top), v_full[: args.top], args.rank_pmid)
    show("BM25 (top {})".format(args.top), b_full[: args.top], args.rank_pmid)
    label = f"Hybrid {args.method}" + (f" alpha={args.alpha}" if args.method == "weighted" else "")
    show(f"{label} pool={args.pool} (top {args.top})", h, args.rank_pmid)

    if args.rank_pmid:
        print(f"\n--- Rank of PMID {args.rank_pmid} (out of {n}) ---")
        print(f"  Vector: {find_rank(v_full, args.rank_pmid)}")
        print(f"  BM25:   {find_rank(b_full, args.rank_pmid)}")
        h_full = r.hybrid_search(args.query, k=n, alpha=args.alpha,
                                 pool=n, method=args.method)
        print(f"  Hybrid: {find_rank(h_full, args.rank_pmid)}")


if __name__ == "__main__":
    main()
