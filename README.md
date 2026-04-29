---
title: Contra
emoji: 🧠
colorFrom: indigo
colorTo: pink
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
license: mit
short_description: Find where Alzheimer's research disagrees.
---

# Contra

**An AI tool that finds where scientific studies disagree, focused on Alzheimer's research.**

Ask a research question (e.g. *"Does lithium slow cognitive decline in Alzheimer's?"*).
Contra retrieves the most relevant clinical studies, classifies each as
*supporting*, *contradicting*, or *inconclusive*, and produces a synthesis
explaining where the evidence conflicts and why.

🔗 **Live demo:** https://huggingface.co/spaces/jonroby/contra

---

## Why this exists

The Alzheimer's literature is full of conflicting findings — anti-amyloid
antibodies, lithium, hormone replacement, statins, the herpes-simplex
hypothesis, the Mediterranean diet. A standard literature search returns
"papers that mention X." Contra answers a more useful question: **"where
do the papers on X disagree, and which evidence is stronger on each side?"**

---

## What papers are included

Contra does **not** search all of PubMed. The corpus is deliberately narrowed
to papers that make testable clinical claims about humans, so that
"supports / contradicts" labels are meaningful.

Starting from 227,857 PubMed records matching the Alzheimer's MeSH search
(1975–2026), three filters are applied in cascade (`scripts/filter_corpus.py`):

**1. Excluded publication types** — these are not primary research:
- Case Reports
- Comment
- Editorial
- Letter
- News
- Biography
- Historical Article

**2. Excluded study subjects** — animal-only research is dropped:
- Papers tagged with MeSH `Animals` or `Mice` but **not** `Humans`
- (Mixed human + animal studies are kept.)

**3. Required publication types** — at least one tag from the clinical-evidence
tiers must be present:

*Top tier (strongest evidence):*
- Meta-Analysis
- Systematic Review
- Randomized Controlled Trial
- Clinical Trial
- Multicenter Study

*Mid tier (still high-quality clinical evidence):*
- Observational Study
- Comparative Study
- Validation Study
- Evaluation Study

**Result:** 21,148 papers (9.3% of the original 227k). A paper outside these
tiers — e.g. a basic-science review, a preclinical mouse study, a conference
abstract, or a non-English paper without a PubMed-indexed translation — will
**not** appear in any Contra result, regardless of how relevant its content is.

This is a deliberate trade-off: precision over recall. A literature search tool
that includes everything dilutes the disagreement signal with editorials and
animal studies. A tool that only includes RCTs misses real-world observational
evidence. The mid-tier inclusion is the compromise.

---

## Architecture

```
PubMed (NCBI E-utilities) ──▶ 227k abstracts (1975–2026)
                                      │
                                      ▼
                              filter: clinical evidence tiers only
                                      │
                                      ▼
                              21,148 high-evidence papers
                                      │
                                      ▼  SPECTER v1 (768-dim)
                                      ▼
                          ┌───────────────────────┐
                          │  Postgres + pgvector  │ ◀── OpenAlex enrichment
                          │  ivfflat index        │     (citations, refs,
                          │  + BM25 in memory     │      OA links — 97.7%)
                          └──────────┬────────────┘
                                     │
                          user query ▼
                          ┌───────────────────────┐
                          │ Hybrid retrieval (RRF)│  top 20 papers
                          └──────────┬────────────┘
                                     ▼
                          ┌───────────────────────┐
                          │ LLM extraction        │  parallel, 20 calls
                          │ (gpt-4o-mini, JSON)   │  → claim, direction,
                          └──────────┬────────────┘    population, n, etc.
                                     ▼
                          ┌───────────────────────┐
                          │ Group + synthesize    │  supports / contradicts
                          │ (gpt-4o-mini)         │  / inconclusive + summary
                          └──────────┬────────────┘
                                     ▼
                          ┌───────────────────────┐
                          │ Gradio (HF Spaces)    │
                          └───────────────────────┘
```

---

## Tech stack

- **Backend:** Python 3.12, Gradio (deployed on HuggingFace Spaces)
- **Database:** PostgreSQL 18 + pgvector (Railway)
- **Embeddings:** SPECTER v1 (`allenai/specter`), 768-dim
- **Vector index:** ivfflat, `lists=200`
- **Lexical search:** `rank_bm25` (in-memory at app startup)
- **Hybrid merge:** Reciprocal Rank Fusion (RRF), pool=200
- **LLM:** gpt-4o-mini (extraction + synthesis)
- **Enrichment:** OpenAlex API (citations, references, fields-of-study, OA links)
- **Evals:** Braintrust (two experiments: retrieval P/R, stance accuracy)

---

## Data pipeline (one-shot, see `scripts/`)

1. **Fetch** — PubMed E-utilities, year-sharded for resumability → 227,857 abstracts
2. **Enrich** — OpenAlex batch API → 222,728 records (97.7% coverage)
3. **Filter** — apply *Option A* clinical-evidence-tier cascade →
   - exclude editorials/letters/case reports
   - exclude animal-only studies (MeSH `Animals`/`Mice` without `Humans`)
   - keep only RCTs, meta-analyses, systematic reviews, observational studies, etc.
   - **→ 21,148 papers**
4. **Embed** — SPECTER on `"{title} [SEP] {abstract}"`, batch 32 → ~7 min on M-series
5. **Load** — Postgres COPY, build ivfflat index. Local mirrored to Railway via `pg_dump`.

---

## Repo layout

```
contra/
├── app.py                         # Gradio web UI (HF Spaces entrypoint)
├── README.md
├── NOTES.md                       # design decisions, rejected alternatives, math
│
├── contra/                        # importable application package
│   ├── retrieval.py               # hybrid search (vector + BM25 + RRF)
│   ├── extract.py                 # async per-paper LLM extraction
│   ├── synthesize.py              # cross-paper summary
│   ├── pipeline.py                # run_query(): full end-to-end
│   └── db.py                      # connection helpers (local | railway)
│
├── cli/                           # command-line tools (use `contra/`)
│   ├── analyze.py                 # full pipeline CLI
│   ├── eval.py                    # Braintrust evals (retrieval + stance)
│   ├── query.py                   # retrieval comparison (vector vs BM25 vs hybrid)
│   └── query_similar.py           # vector-only smoke test
│
├── evals/
│   └── golden.json                # hand-curated test set (5 questions)
│
├── scripts/                       # one-shot DB & data setup
│   ├── fetch_abstracts.py
│   ├── fetch_openalex.py
│   ├── filter_corpus.py
│   ├── embed_and_load.py
│   └── init_db.py
│
└── data/                          # gitignored — raw fetched data
```

---

## Roadmap

- Hand-curate golden eval set with real disagreements (current set is system-seeded)
- Composite evidence-quality scoring (study design × recency × citation velocity)
- React/Vite frontend
- "Do contradicting papers cite each other?" feature (data is already in DB)

---

## Local development

```bash
# 1. Install
uv sync

# 2. Configure .env
cp .env.example .env  # fill in DATABASE_URL, RAILWAY_DATABASE_URL, OPENAI_API_KEY

# 3. (One-time) build the database
uv run python scripts/init_db.py --target local
uv run python scripts/fetch_abstracts.py
uv run python scripts/fetch_openalex.py
uv run python scripts/filter_corpus.py
uv run python scripts/embed_and_load.py --input data/abstracts_filtered.json --target local

# 4. Run the CLI
uv run python cli/analyze.py "does lithium slow cognitive decline?"

# 5. Or run the web UI
CONTRA_TARGET=local uv run python app.py  # visits http://127.0.0.1:7860
```

---

See **[NOTES.md](./NOTES.md)** for architecture decisions, rejected alternatives,
filter math, and the rationale behind each non-obvious choice.
