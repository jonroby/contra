"""
End-to-end pipeline CLI: query -> hybrid retrieval -> LLM extraction -> synthesis.

Thin wrapper around `contra.pipeline.run_query`. Same logic powers the Gradio
web UI; this module just adds CLI argument parsing and human-readable output.

Usage:
    uv run python cli/analyze.py "does lithium slow cognitive decline in Alzheimer's?"
    uv run python cli/analyze.py --target railway --top 20 "..."
"""

import argparse
import json

from dotenv import load_dotenv

from contra.pipeline import run_query

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
    print(f"Running pipeline (target={args.target}, top={args.top})...")
    result = run_query(args.query, target=args.target, top_k=args.top)
    timings = result.metadata.get("timings", {})

    print("\n" + "=" * 70)
    print(f"QUERY: {result.query}")
    print("=" * 70)
    print(f"\nSUMMARY:\n{result.summary}\n")
    print(
        f"COUNTS: supports={len(result.supports)}, "
        f"contradicts={len(result.contradicts)}, "
        f"inconclusive={len(result.inconclusive)}"
    )
    print(f"TIMINGS: {timings}")

    for label, group in [("SUPPORTS", result.supports),
                         ("CONTRADICTS", result.contradicts)]:
        print(f"\n--- {label} ({len(group)}) ---")
        for f in group:
            print(f"  [{f.get('year')}] {f.get('title','')[:90]}")
            print(f"    claim: {f.get('claim','')[:140]}")
            print(f"    pmid: {f.get('pmid')}, conf: {f.get('confidence')}")

    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(result.as_dict(), fh, indent=2, ensure_ascii=False)
        print(f"\nWrote full result to {args.json_out}")


if __name__ == "__main__":
    main()
