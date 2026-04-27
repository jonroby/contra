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

Ask a research question about Alzheimer's. Contra retrieves relevant clinical
studies, classifies each as supporting or contradicting your question, and
summarizes where the evidence conflicts.

Built on a hybrid retrieval system (pgvector + BM25 + RRF) over 21,148
high-evidence-tier PubMed abstracts, with OpenAlex enrichment for citation
metadata. LLM-powered extraction (gpt-4o-mini) classifies each retrieved
study and produces a synthesis summary.

