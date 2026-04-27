"""End-to-end query pipeline: retrieve → extract → group → synthesize.

This is the single source of truth for "given a research question, produce
a contradiction-aware answer." Both `cli/analyze.py` and the Gradio web app
call `run_query()`.
"""

import asyncio
import time
from dataclasses import dataclass, field
from typing import Any

from contra.db import resolve_url
from contra.extract import extract_all
from contra.retrieval import Retriever
from contra.synthesize import synthesize


@dataclass
class PipelineResult:
    query: str
    summary: str
    supports: list[dict[str, Any]] = field(default_factory=list)
    contradicts: list[dict[str, Any]] = field(default_factory=list)
    inconclusive: list[dict[str, Any]] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def as_dict(self) -> dict[str, Any]:
        return {
            "query": self.query,
            "summary": self.summary,
            "supports": self.supports,
            "contradicts": self.contradicts,
            "inconclusive": self.inconclusive,
            "metadata": self.metadata,
        }


def _group(findings: list[dict]) -> tuple[list, list, list]:
    sup = [f for f in findings if f.get("direction") == "supports"]
    con = [f for f in findings if f.get("direction") == "contradicts"]
    inc = [f for f in findings if f.get("direction") == "inconclusive"]
    return sup, con, inc


def run_query(
    query: str,
    target: str = "railway",
    top_k: int = 20,
    retriever: Retriever | None = None,
) -> PipelineResult:
    """Run the full pipeline for one query.

    `retriever` can be passed in to avoid the ~5s cold start when calling
    repeatedly (e.g., the Gradio app loads it once at startup).
    """
    timings: dict[str, float] = {}

    if retriever is None:
        t0 = time.time()
        retriever = Retriever(resolve_url(target))
        timings["retriever_init_s"] = round(time.time() - t0, 2)

    t0 = time.time()
    hits = retriever.hybrid_search(query, k=top_k, method="rrf", pool=200)
    timings["retrieval_s"] = round(time.time() - t0, 2)

    t0 = time.time()
    papers = [p for p, _ in hits]
    findings = asyncio.run(extract_all(query, papers))
    timings["extraction_s"] = round(time.time() - t0, 2)

    sup, con, inc = _group(findings)

    t0 = time.time()
    summary = synthesize(query, findings)
    timings["synthesis_s"] = round(time.time() - t0, 2)

    return PipelineResult(
        query=query,
        summary=summary,
        supports=sup,
        contradicts=con,
        inconclusive=inc,
        metadata={
            "target": target,
            "top_k": top_k,
            "n_retrieved": len(hits),
            "n_findings": len(findings),
            "timings": timings,
        },
    )
