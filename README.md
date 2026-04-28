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
│   ├── query.py                   # retrieval comparison (vector vs BM25 vs hybrid)
│   └── query_similar.py           # vector-only smoke test
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

## Status

- [x] Stage 1 — Data pipeline (227k abstracts)
- [x] Stage 2 — Embedding + Postgres (21,148 papers, both DBs in sync)
- [x] Stage 3 — Hybrid retrieval (RRF, pool=200)
- [x] Stage 4 — LLM extraction + synthesis
- [x] Stage 5 — Gradio web UI on HF Spaces
- [x] OpenAlex enrichment — 97.7% coverage
- [ ] **Next:** evals (`ranx` for retrieval, Ragas for generation) with hand-curated test set
- [ ] Composite evidence-quality scoring (study design × recency × citation velocity)
- [ ] React/Vite frontend (planned)
- [ ] "Do contradicting papers cite each other?" feature (data is already in DB)

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
