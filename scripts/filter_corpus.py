"""
Filter the full PubMed corpus to high-evidence-tier clinical papers and
merge OpenAlex enrichment fields.

Reads:
    data/abstracts.json              (~227k PubMed records)
    data/openalex/enrichment.json    (~222k OpenAlex enrichments)

Writes:
    data/abstracts_filtered.json     (~21k merged records)

Filter cascade (Option A in NOTES.md):
    1. Exclude editorial-style publication types (case reports, letters, etc.)
    2. Exclude animal-only studies (MeSH "Animals"/"Mice" without "Humans")
    3. Keep only clinical evidence tiers (RCTs, meta-analyses, systematic
       reviews, observational studies, etc.)

OpenAlex fields are merged where available (~98% of survivors). Papers without
OpenAlex data are kept with NULL enrichment fields.

Usage:
    uv run python scripts/filter_corpus.py
"""

import json
from pathlib import Path

ABSTRACTS_PATH = Path("data/abstracts.json")
ENRICHMENT_PATH = Path("data/openalex/enrichment.json")
OUTPUT_PATH = Path("data/abstracts_filtered.json")

# PubMed publication-type tiers (Oxford EBM pyramid, mapped to our task)
TOP_TIER = {
    "Meta-Analysis",
    "Systematic Review",
    "Randomized Controlled Trial",
    "Clinical Trial",
    "Multicenter Study",
}
MID_TIER = {
    "Observational Study",
    "Comparative Study",
    "Validation Study",
    "Evaluation Study",
}
KEEP_TIERS = TOP_TIER | MID_TIER

# Drop these outright — not research claims
EXCLUDE_TYPES = {
    "Case Reports",
    "Comment",
    "Editorial",
    "Letter",
    "News",
    "Biography",
    "Historical Article",
}


def is_animal_only(mesh_terms: list[str]) -> bool:
    """True if MeSH tags indicate non-human study (Animals/Mice without Humans)."""
    s = set(mesh_terms or [])
    has_humans = any(m == "Humans" or m.startswith("Humans/") for m in s)
    has_animals = any(
        m in ("Animals", "Mice") or m.startswith(("Animals/", "Mice/"))
        for m in s
    )
    return has_animals and not has_humans


def passes_filter(paper: dict) -> bool:
    pub_types = set(paper.get("publication_types") or [])
    if pub_types & EXCLUDE_TYPES:
        return False
    if is_animal_only(paper.get("mesh_terms") or []):
        return False
    if not (pub_types & KEEP_TIERS):
        return False
    return True


def strip_openalex_url(url: str) -> str:
    """https://openalex.org/W12345 -> W12345"""
    if not url:
        return ""
    return url.rsplit("/", 1)[-1]


def merge_enrichment(paper: dict, enrichment: dict | None) -> dict:
    """Add OpenAlex fields to a paper record. NULLs if no enrichment."""
    if not enrichment:
        paper["openalex_id"] = None
        paper["cited_by_count"] = None
        paper["referenced_works"] = None
        paper["concepts"] = None
        paper["oa_status"] = None
        paper["oa_pdf_url"] = None
        return paper

    paper["openalex_id"] = enrichment.get("openalex_id") or None
    paper["cited_by_count"] = enrichment.get("cited_by_count")
    # strip URL prefixes from referenced_works -> just IDs
    refs = enrichment.get("referenced_works") or []
    paper["referenced_works"] = [strip_openalex_url(r) for r in refs] if refs else []
    paper["concepts"] = enrichment.get("concepts") or []
    # is_oa is redundant with oa_pdf_url; we keep status + url only
    paper["oa_status"] = (enrichment.get("oa_status") if enrichment.get("is_oa") is not None else None)
    paper["oa_pdf_url"] = enrichment.get("oa_pdf_url")
    return paper


def main():
    print(f"Loading {ABSTRACTS_PATH}...")
    with open(ABSTRACTS_PATH, encoding="utf-8") as f:
        papers = json.load(f)
    print(f"  {len(papers):,} papers loaded")

    print(f"Loading {ENRICHMENT_PATH}...")
    with open(ENRICHMENT_PATH, encoding="utf-8") as f:
        enrichment = json.load(f)
    print(f"  {len(enrichment):,} enrichment records loaded")

    print("\nFiltering...")
    filtered = [p for p in papers if passes_filter(p)]
    print(f"  passed Option A filter: {len(filtered):,} / {len(papers):,} "
          f"({100*len(filtered)/len(papers):.1f}%)")

    print("\nMerging OpenAlex enrichment...")
    with_enrich = 0
    without_enrich = 0
    merged = []
    for p in filtered:
        enr = enrichment.get(p["pmid"])
        if enr:
            with_enrich += 1
        else:
            without_enrich += 1
        merged.append(merge_enrichment(p, enr))

    print(f"  with enrichment:    {with_enrich:,} ({100*with_enrich/len(merged):.1f}%)")
    print(f"  without enrichment: {without_enrich:,} ({100*without_enrich/len(merged):.1f}%)")

    print(f"\nWriting {OUTPUT_PATH}...")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False)

    size_mb = OUTPUT_PATH.stat().st_size / 1_000_000
    print(f"Done: {len(merged):,} merged records -> {OUTPUT_PATH} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
