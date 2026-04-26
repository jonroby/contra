"""
End-to-end pipeline: query -> hybrid retrieval -> LLM extraction -> synthesis.

Usage:
    uv run python scripts/analyze.py "does lithium slow cognitive decline in Alzheimer's?"
    uv run python scripts/analyze.py --target railway --top 20 "..."
"""

import argparse
import asyncio
import json
import time

from dotenv import load_dotenv

from db import resolve_url
from extract import extract_all
from retrieval import Retriever
from synthesize import synthesize

load_dotenv()


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("query", type=str)
    p.add_argument("--top", type=int, default=20, help="How many papers to extract from")
    p.add_argument("--target", choices=["local", "railway"], default="local")
    p.add_argument("--json-out", type=str, default=None,
                   help="Optionally write full result as JSON to this path")
    return p.parse_args()


def main():
    args = parse_args()
    url = resolve_url(args.target)

    print(f"[1/4] Loading retriever (target={args.target})...")
    t0 = time.time()
    r = Retriever(url)
    print(f"      {len(r.papers)} papers indexed in {time.time()-t0:.1f}s")

    print(f"[2/4] Hybrid search for: {args.query!r}")
    t0 = time.time()
    hits = r.hybrid_search(args.query, k=args.top, method="rrf", pool=200)
    print(f"      retrieved {len(hits)} papers in {time.time()-t0:.2f}s")

    print(f"[3/4] LLM extraction (gpt-4o-mini, parallel)...")
    t0 = time.time()
    papers = [p for p, _ in hits]
    findings = asyncio.run(extract_all(args.query, papers))
    print(f"      extracted {len(findings)} findings in {time.time()-t0:.1f}s")

    supports = [f for f in findings if f.get("direction") == "supports"]
    contradicts = [f for f in findings if f.get("direction") == "contradicts"]
    inconclusive = [f for f in findings if f.get("direction") == "inconclusive"]

    print(f"[4/4] Synthesis...")
    t0 = time.time()
    summary = synthesize(args.query, findings)
    print(f"      done in {time.time()-t0:.1f}s")

    print("\n" + "=" * 70)
    print(f"QUERY: {args.query}")
    print("=" * 70)
    print(f"\nSUMMARY:\n{summary}\n")
    print(f"COUNTS: supports={len(supports)}, contradicts={len(contradicts)}, "
          f"inconclusive={len(inconclusive)}")

    for label, group in [("SUPPORTS", supports), ("CONTRADICTS", contradicts)]:
        print(f"\n--- {label} ({len(group)}) ---")
        for f in group:
            print(f"  [{f.get('year')}] {f.get('title','')[:90]}")
            print(f"    claim: {f.get('claim','')[:140]}")
            print(f"    pmid: {f.get('pmid')}, conf: {f.get('confidence')}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump({
                "query": args.query,
                "summary": summary,
                "supports": supports,
                "contradicts": contradicts,
                "inconclusive": inconclusive,
            }, fh, indent=2, ensure_ascii=False)
        print(f"\nWrote full result to {args.json_out}")


if __name__ == "__main__":
    main()
