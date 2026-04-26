"""
Enrich abstracts with OpenAlex metadata: citation counts, references,
fields of study (concepts), and open-access PDF links.

Reads PMIDs from data/abstracts.json, batches them into per-50 OpenAlex
queries, and writes one shard JSON per batch. A final merge step combines
all shards into data/openalex/enrichment.json keyed by PMID.

Resumable: existing shard files are skipped on rerun.

Usage:
    uv run python scripts/fetch_openalex.py
    uv run python scripts/fetch_openalex.py --limit 500    # quick test
"""

import argparse
import json
import os
import time
from pathlib import Path

import requests

# ── CONFIG ──────────────────────────────────────────────────────────────────
INPUT_FILE = Path("data/abstracts.json")
PROGRESS_DIR = Path("data/openalex/progress")
OUTPUT_FILE = Path("data/openalex/enrichment.json")

API_URL = "https://api.openalex.org/works"
BATCH_SIZE = 50  # OpenAlex caps filter OR-list at 50 IDs

# Polite-pool: include a contact email in the User-Agent or `mailto` param.
# Gets you into a faster, more reliable rate-limit pool.
CONTACT_EMAIL = "jonathan.roby1@gmail.com"
USER_AGENT = f"contra-research ({CONTACT_EMAIL})"

# Fields we actually need — keeps response payloads small.
SELECT_FIELDS = ",".join([
    "ids",
    "cited_by_count",
    "referenced_works",
    "concepts",
    "open_access",
])

# OpenAlex polite pool allows ~10 req/s. Stay well under to be safe.
SLEEP_BETWEEN_CALLS = 0.15
MAX_RETRIES = 4


def parse_args():
    p = argparse.ArgumentParser(description="Enrich PubMed papers with OpenAlex data")
    p.add_argument("--input", type=Path, default=INPUT_FILE)
    p.add_argument("--limit", type=int, default=None,
                   help="Cap total PMIDs (testing)")
    p.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    return p.parse_args()


def load_pmids(path: Path, limit: int | None) -> list[str]:
    with open(path, encoding="utf-8") as f:
        records = json.load(f)
    pmids = [r["pmid"] for r in records if r.get("pmid")]
    # dedup, preserve order
    pmids = list(dict.fromkeys(pmids))
    if limit:
        pmids = pmids[:limit]
    return pmids


def fetch_batch(pmids: list[str]) -> list[dict]:
    """One OpenAlex call for up to BATCH_SIZE PMIDs. Returns raw work dicts."""
    pmid_filter = "pmid:" + "|".join(pmids)
    params = {
        "filter": pmid_filter,
        "select": SELECT_FIELDS,
        "per-page": len(pmids),
        "mailto": CONTACT_EMAIL,
    }
    headers = {"User-Agent": USER_AGENT}

    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(API_URL, params=params, headers=headers, timeout=30)
            if resp.status_code == 429:
                wait = 2 ** (attempt + 2)  # 4, 8, 16, 32
                print(f"    429 rate-limited, sleeping {wait}s")
                time.sleep(wait)
                continue
            resp.raise_for_status()
            return resp.json().get("results", [])
        except (requests.RequestException, requests.Timeout) as e:
            wait = 2 ** (attempt + 1)
            print(f"    Retry {attempt + 1}/{MAX_RETRIES} after error: {e}. Sleeping {wait}s.")
            time.sleep(wait)

    raise RuntimeError(f"Failed after {MAX_RETRIES} retries")


def extract_pmid(work: dict) -> str | None:
    """OpenAlex returns pmid as a URL like https://pubmed.ncbi.nlm.nih.gov/12345."""
    pmid_url = work.get("ids", {}).get("pmid", "")
    if not pmid_url:
        return None
    return pmid_url.rsplit("/", 1)[-1]


def normalize_work(work: dict) -> dict:
    """Strip down an OpenAlex work to just the fields we need."""
    oa = work.get("open_access") or {}
    concepts = work.get("concepts") or []
    return {
        "openalex_id": work.get("ids", {}).get("openalex", "").rsplit("/", 1)[-1],
        "doi": work.get("ids", {}).get("doi"),
        "cited_by_count": work.get("cited_by_count", 0),
        "referenced_works": work.get("referenced_works") or [],
        "concepts": [
            {"name": c.get("display_name"), "score": c.get("score"), "level": c.get("level")}
            for c in concepts if c.get("score", 0) >= 0.3  # filter low-confidence
        ],
        "is_oa": oa.get("is_oa", False),
        "oa_status": oa.get("oa_status"),
        "oa_pdf_url": oa.get("oa_url"),
    }


def main():
    args = parse_args()
    PROGRESS_DIR.mkdir(parents=True, exist_ok=True)

    pmids = load_pmids(args.input, args.limit)
    total = len(pmids)
    batches = [pmids[i:i + args.batch_size] for i in range(0, total, args.batch_size)]
    print(f"PMIDs: {total} -> {len(batches)} batches of {args.batch_size}")
    print(f"Progress dir: {PROGRESS_DIR} (existing batch files will be skipped)")
    print()

    fetched = 0
    skipped = 0
    for i, batch in enumerate(batches):
        shard_path = PROGRESS_DIR / f"batch_{i:05d}.json"
        if shard_path.exists():
            skipped += 1
            continue

        try:
            works = fetch_batch(batch)
        except Exception as e:
            print(f"  batch {i:05d}: failed ({e}), will retry on next run")
            continue

        # build pmid -> normalized record
        out = {}
        for work in works:
            pmid = extract_pmid(work)
            if pmid:
                out[pmid] = normalize_work(work)

        tmp = shard_path.with_suffix(".json.tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False)
        os.replace(tmp, shard_path)

        fetched += 1
        if fetched % 20 == 0:
            print(f"  batch {i:05d}: {fetched} fetched, {skipped} skipped, "
                  f"{len(out)}/{len(batch)} hits in this batch")

        time.sleep(SLEEP_BETWEEN_CALLS)

    print(f"\nFetch phase done: {fetched} new, {skipped} pre-existing")

    # ── Merge ───────────────────────────────────────────────────────────────
    print("\nMerging shards...")
    merged = {}
    for shard in sorted(PROGRESS_DIR.glob("batch_*.json")):
        with open(shard, encoding="utf-8") as f:
            merged.update(json.load(f))

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    hits = len(merged)
    print(f"Done: {hits}/{total} PMIDs enriched ({100*hits/total:.1f}% coverage)")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
