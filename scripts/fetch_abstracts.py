"""
Fetch Alzheimer's abstracts from PubMed via E-utilities.
Uses year-slicing to bypass the 9,999 retmax ceiling.

Usage:
    uv run python scripts/fetch_abstracts.py                        # full run, all years
    uv run python scripts/fetch_abstracts.py --api-key YOUR_KEY     # faster (10 req/s vs 3)
    uv run python scripts/fetch_abstracts.py --start-year 2020      # only 2020-present
    uv run python scripts/fetch_abstracts.py --max-per-year 500     # quick test run

Output: data/abstracts.json

Fields per record:
    pmid, title, abstract, authors, year, journal,
    doi, publication_types, mesh_terms, keywords
"""

import os
import requests
import xml.etree.ElementTree as ET
import json
import time
import argparse
from typing import Optional

from dotenv import load_dotenv

load_dotenv()


# ── CONFIG ──────────────────────────────────────────────────────────────────
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SEARCH_TERM = 'alzheimer[MeSH Terms] OR alzheimer[Title/Abstract]'
BATCH_SIZE = 200        # records per efetch call
# MEDLINE began systematically including author abstracts ~1975; pre-1975 records are
# mostly citation-only. Alzheimer's also wasn't widely researched until the 1980s
# (ADRDA founded 1980, first major NIH funding push mid-80s), so starting at 1975
# loses almost nothing meaningful and skips ~25 years of near-empty searches.
DEFAULT_START = 1975
DEFAULT_END = 2026
OUTPUT_FILE = "data/abstracts.json"
# Per-year shard files written here as each year finishes, so a crash or Ctrl-C
# doesn't lose hours of work. On rerun, years with an existing shard are skipped.
# Final step merges all shards into OUTPUT_FILE.
PROGRESS_DIR = "data/progress"


def parse_args():
    p = argparse.ArgumentParser(description="Download Alzheimer's abstracts from PubMed")
    p.add_argument("--api-key", type=str, default=os.getenv("NCBI_API_KEY"),
                   help="NCBI API key (free at ncbi.nlm.nih.gov/account). "
                        "Defaults to NCBI_API_KEY env var (loaded from .env).")
    p.add_argument("--start-year", type=int, default=DEFAULT_START)
    p.add_argument("--end-year", type=int, default=DEFAULT_END)
    p.add_argument("--max-per-year", type=int, default=None,
                   help="Cap PMIDs per year (useful for testing)")
    p.add_argument("--output", type=str, default=OUTPUT_FILE)
    return p.parse_args()


def rate_limit(api_key: Optional[str]):
    """NCBI allows 3 req/s without key, 10 with key."""
    time.sleep(0.11 if api_key else 0.34)


def esearch_range(term: str, mindate: str, maxdate: str,
                  api_key: Optional[str], retmax: int = 9999) -> tuple[list[str], int]:
    """Return (PMIDs, total_count) for a date range. Dates as YYYY/MM/DD."""
    params = {
        "db": "pubmed",
        "term": term,
        "mindate": mindate,
        "maxdate": maxdate,
        "datetype": "pdat",
        "retmax": retmax,
        "retmode": "json",
        "usehistory": "n",
    }
    if api_key:
        params["api_key"] = api_key

    rate_limit(api_key)
    resp = requests.get(f"{BASE_URL}/esearch.fcgi", params=params, timeout=30)
    resp.raise_for_status()
    data = resp.json()

    count = int(data["esearchresult"]["count"])
    ids = data["esearchresult"]["idlist"]
    return ids, count


def esearch_year(term: str, year: int, api_key: Optional[str]) -> list[str]:
    """Get all PMIDs for a year, recursively splitting date ranges if >9999 results."""

    def collect(mindate: str, maxdate: str, depth: int = 0) -> list[str]:
        ids, count = esearch_range(term, mindate, maxdate, api_key)
        if count <= 9999:
            return ids
        if depth > 6:
            print(f"    WARNING: {mindate}..{maxdate} has {count} results, can't split further")
            return ids
        # split range in half by parsing dates
        from datetime import date
        y1, m1, d1 = map(int, mindate.split("/"))
        y2, m2, d2 = map(int, maxdate.split("/"))
        start = date(y1, m1, d1).toordinal()
        end = date(y2, m2, d2).toordinal()
        if end - start < 1:
            return ids
        mid = (start + end) // 2
        mid_d = date.fromordinal(mid)
        next_d = date.fromordinal(mid + 1)
        left = collect(mindate, mid_d.strftime("%Y/%m/%d"), depth + 1)
        right = collect(next_d.strftime("%Y/%m/%d"), maxdate, depth + 1)
        return left + right

    return collect(f"{year}/01/01", f"{year}/12/31")


def efetch_batch(pmids: list[str], api_key: Optional[str], retries: int = 3) -> str:
    """Fetch PubMed XML for a batch of PMIDs. Returns raw XML string."""
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "rettype": "xml",
        "retmode": "xml",
    }
    if api_key:
        params["api_key"] = api_key

    for attempt in range(retries):
        try:
            rate_limit(api_key)
            resp = requests.get(f"{BASE_URL}/efetch.fcgi", params=params, timeout=60)
            resp.raise_for_status()
            return resp.text
        except (requests.RequestException, requests.Timeout) as e:
            wait = 2 ** (attempt + 1)
            print(f"    Retry {attempt + 1}/{retries} after error: {e}. Waiting {wait}s...")
            time.sleep(wait)

    raise RuntimeError(f"Failed to fetch batch after {retries} retries")


def parse_article(article: ET.Element) -> Optional[dict]:
    """Extract fields from a single <PubmedArticle> element."""

    # -- PMID --
    pmid_el = article.find(".//PMID")
    if pmid_el is None:
        return None
    pmid = pmid_el.text

    medline = article.find(".//MedlineCitation")
    art = article.find(".//Article")
    if art is None:
        return None

    # -- Title --
    title_el = art.find(".//ArticleTitle")
    title = "".join(title_el.itertext()).strip() if title_el is not None else ""

    # -- Abstract (handles structured abstracts with labels) --
    abstract_parts = []
    for at in art.findall(".//Abstract/AbstractText"):
        label = at.get("Label", "")
        text = "".join(at.itertext()).strip()
        if text:
            if label:
                abstract_parts.append(f"{label}: {text}")
            else:
                abstract_parts.append(text)
    abstract = " ".join(abstract_parts)

    if not abstract:
        return None  # skip records without abstracts

    # -- Authors --
    authors = []
    for author in art.findall(".//AuthorList/Author"):
        last = author.findtext("LastName", "")
        fore = author.findtext("ForeName", "")
        if last:
            authors.append(f"{last} {fore}".strip())

    # -- Year --
    year = None
    for date_path in [".//ArticleDate", ".//Journal/JournalIssue/PubDate"]:
        y_el = art.find(f"{date_path}/Year")
        if y_el is not None and y_el.text:
            try:
                year = int(y_el.text)
                break
            except ValueError:
                pass
    if year is None:
        md = art.findtext(".//Journal/JournalIssue/PubDate/MedlineDate", "")
        if md and md[:4].isdigit():
            year = int(md[:4])

    # -- Journal --
    journal = art.findtext(".//Journal/Title", "")

    # -- DOI --
    doi = ""
    for eid in article.findall(".//PubmedData/ArticleIdList/ArticleId"):
        if eid.get("IdType") == "doi":
            doi = eid.text or ""
            break

    # -- Publication Types --
    pub_types = []
    for pt in art.findall(".//PublicationTypeList/PublicationType"):
        if pt.text:
            pub_types.append(pt.text)

    # -- MeSH Terms (with qualifiers) --
    mesh_terms = []
    if medline is not None:
        for mh in medline.findall(".//MeshHeadingList/MeshHeading"):
            desc = mh.findtext("DescriptorName", "")
            if desc:
                quals = [q.text for q in mh.findall("QualifierName") if q.text]
                if quals:
                    mesh_terms.append(f"{desc}/{'/'.join(quals)}")
                else:
                    mesh_terms.append(desc)

    # -- Keywords --
    keywords = []
    if medline is not None:
        for kw in medline.findall(".//KeywordList/Keyword"):
            if kw.text:
                keywords.append(kw.text)

    return {
        "pmid": pmid,
        "title": title,
        "abstract": abstract,
        "authors": authors,
        "year": year,
        "journal": journal,
        "doi": doi,
        "publication_types": pub_types,
        "mesh_terms": mesh_terms,
        "keywords": keywords,
    }


def parse_xml(xml_str: str) -> list[dict]:
    """Parse efetch XML into list of article dicts."""
    records = []
    try:
        root = ET.fromstring(xml_str)
    except ET.ParseError as e:
        print(f"    XML parse error: {e}")
        return records

    for article in root.findall(".//PubmedArticle"):
        rec = parse_article(article)
        if rec:
            records.append(rec)
    return records


def fetch_year(year: int, api_key: Optional[str], max_per_year: Optional[int]) -> list[dict]:
    """Fetch all abstracts for a year, with internal date-range splitting."""
    pmids = esearch_year(SEARCH_TERM, year, api_key)
    # dedup PMIDs (date-range splits can overlap at boundaries in rare cases)
    pmids = list(dict.fromkeys(pmids))
    if max_per_year and len(pmids) > max_per_year:
        pmids = pmids[:max_per_year]
    if not pmids:
        return []

    print(f"  {year}: {len(pmids)} PMIDs", end="", flush=True)
    records = []
    for i in range(0, len(pmids), BATCH_SIZE):
        batch = pmids[i:i + BATCH_SIZE]
        try:
            xml = efetch_batch(batch, api_key)
            records.extend(parse_xml(xml))
        except Exception as e:
            print(f" [batch error: {e}]", end="")
        print(".", end="", flush=True)
    print(f" -> {len(records)} abstracts")
    return records


def main():
    args = parse_args()
    years = range(args.start_year, args.end_year + 1)

    os.makedirs(PROGRESS_DIR, exist_ok=True)

    print(f"Fetching Alzheimer's abstracts from PubMed ({args.start_year}-{args.end_year})")
    if args.api_key:
        print("Using API key (10 req/s)")
    else:
        print("No API key (3 req/s). Pass --api-key for ~3x speed.")
    print(f"Progress dir: {PROGRESS_DIR} (existing year files will be skipped)")
    print()

    for year in years:
        shard_path = os.path.join(PROGRESS_DIR, f"{year}.json")
        if os.path.exists(shard_path):
            print(f"  {year}: already fetched, skipping")
            continue
        try:
            records = fetch_year(year, args.api_key, args.max_per_year)
        except Exception as e:
            print(f"  {year}: failed ({e}), will retry on next run")
            continue

        # atomic write: tmp then rename
        tmp = shard_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False)
        os.replace(tmp, shard_path)

    # -- Merge all shards --
    all_records = {}
    for fname in sorted(os.listdir(PROGRESS_DIR)):
        if not fname.endswith(".json"):
            continue
        with open(os.path.join(PROGRESS_DIR, fname), encoding="utf-8") as f:
            for rec in json.load(f):
                all_records[rec["pmid"]] = rec

    output = list(all_records.values())
    output.sort(key=lambda r: (r["year"] or 0, r["pmid"]))

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nDone: {len(output)} unique records -> {args.output}")


if __name__ == "__main__":
    main()
