"""
Braintrust evals for Contra.

Two independent evals over the same golden set (`evals/golden.json`):

  1. retrieval — precision/recall over the union of papers Contra surfaces
     in its final result (supports + contradicts + inconclusive), versus the
     human-labeled `relevant_pmids`. Stance is ignored.

  2. stance — for each (question, pmid) we labeled in `stances`, did Contra
     classify it into the right bucket? Only papers Contra actually surfaced
     are scored (you can't grade a stance on a paper that wasn't retrieved).

Run:
    uv run python cli/eval.py            # both
    uv run python cli/eval.py retrieval
    uv run python cli/eval.py stance
"""

import json
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from braintrust import Eval

from contra.db import resolve_url
from contra.pipeline import run_query
from contra.retrieval import Retriever

GOLDEN_PATH = Path(__file__).parent.parent / "evals" / "golden.json"
PROJECT = "contra"
TARGET = "railway"

_RETRIEVER: Retriever | None = None


def _retriever() -> Retriever:
    global _RETRIEVER
    if _RETRIEVER is None:
        _RETRIEVER = Retriever(resolve_url(TARGET))
    return _RETRIEVER


def _load_golden() -> list[dict]:
    with open(GOLDEN_PATH) as f:
        return json.load(f)


def _surfaced_pmids(result) -> set[str]:
    pmids: set[str] = set()
    for bucket in (result.supports, result.contradicts, result.inconclusive):
        for f in bucket:
            if pmid := f.get("pmid"):
                pmids.add(str(pmid))
    return pmids


def _stance_map(result) -> dict[str, str]:
    out: dict[str, str] = {}
    for direction, bucket in [
        ("supports", result.supports),
        ("contradicts", result.contradicts),
        ("inconclusive", result.inconclusive),
    ]:
        for f in bucket:
            if pmid := f.get("pmid"):
                out[str(pmid)] = direction
    return out


def task(question: str):
    return run_query(question, target=TARGET, retriever=_retriever())


def precision_scorer(output, expected) -> float:
    surfaced = _surfaced_pmids(output)
    relevant = {str(p) for p in expected["relevant_pmids"]}
    if not surfaced:
        return 0.0
    return len(surfaced & relevant) / len(surfaced)


def recall_scorer(output, expected) -> float:
    surfaced = _surfaced_pmids(output)
    relevant = {str(p) for p in expected["relevant_pmids"]}
    if not relevant:
        return 0.0
    return len(surfaced & relevant) / len(relevant)


def stance_accuracy_scorer(output, expected) -> float:
    """Of labeled pmids that Contra surfaced, fraction with correct stance."""
    predicted = _stance_map(output)
    labeled = {str(k): v for k, v in expected["stances"].items()}
    overlap = [pmid for pmid in labeled if pmid in predicted]
    if not overlap:
        return 0.0
    correct = sum(1 for pmid in overlap if predicted[pmid] == labeled[pmid])
    return correct / len(overlap)


def _data():
    for row in _load_golden():
        yield {
            "input": row["question"],
            "expected": {
                "relevant_pmids": row.get("relevant_pmids", []),
                "stances": row.get("stances", {}),
            },
        }


def run_retrieval_eval():
    Eval(
        PROJECT,
        experiment_name="retrieval",
        data=lambda: list(_data()),
        task=task,
        scores=[precision_scorer, recall_scorer],
    )


def run_stance_eval():
    Eval(
        PROJECT,
        experiment_name="stance",
        data=lambda: list(_data()),
        task=task,
        scores=[stance_accuracy_scorer],
    )


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("retrieval", "all"):
        run_retrieval_eval()
    if which in ("stance", "all"):
        run_stance_eval()
