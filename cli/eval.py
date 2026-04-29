"""
Braintrust eval for Contra.

One Eval over the golden set (`evals/golden.json`) with four scorers:

  1. precision / recall — over the union of papers Contra surfaces
     (supports + contradicts + inconclusive), versus the human-labeled
     `relevant_pmids`. Stance is ignored.

  2. stance accuracy — for each (question, pmid) we labeled in `stances`,
     did Contra classify it into the right bucket? Only papers Contra
     actually surfaced are scored.

  3. stance justification — for a stratified random sample of (question, pmid)
     pairs where the golden set has a `stance_justifications` quote, an LLM
     judge (Claude Haiku 4.5) compares it to the system's `stance_justification`.
     Returns 1.0 if the two quotes support the same finding, 0.5 if partially
     overlapping, 0.0 if different. Sample is 12 per stance bucket = 36 calls
     per run, seeded for run-to-run comparability.

The pipeline runs once per question; all four scorers read the same
PipelineResult.

Run:
    uv run python cli/eval.py
"""

import json
import os
import random
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic
from braintrust import Eval

from contra.db import resolve_url
from contra.pipeline import run_query
from contra.retrieval import Retriever

GOLDEN_PATH = Path(__file__).parent.parent / "evals" / "golden.json"
PROJECT = "contra"
TARGET = "railway"
JUDGE_MODEL = "claude-haiku-4-5-20251001"

# Stratified random sample of (question, pmid) pairs to judge for stance
# justification. 12 per stance bucket × 3 buckets = 36 judge calls per run
# (vs ~200 if full). Seed fixed so two runs are comparable; bump to invalidate.
STANCE_JUSTIFICATION_SAMPLE_PER_STANCE = 12
STANCE_JUSTIFICATION_SAMPLE_SEED = 0

_RETRIEVER: Retriever | None = None
_ANTHROPIC: Anthropic | None = None


def _retriever() -> Retriever:
    global _RETRIEVER
    if _RETRIEVER is None:
        _RETRIEVER = Retriever(resolve_url(TARGET))
    return _RETRIEVER


def _anthropic() -> Anthropic:
    global _ANTHROPIC
    if _ANTHROPIC is None:
        _ANTHROPIC = Anthropic()
    return _ANTHROPIC


def _load_golden() -> list[dict]:
    with open(GOLDEN_PATH) as f:
        return json.load(f)


def _stance_justification_sample() -> set[tuple[str, str]]:
    """Stratified random sample of (question, pmid) pairs for the stance-justification judge.

    Stratifies by golden stance so all three buckets are represented evenly,
    not in proportion to their (skewed) frequency in the golden set.
    """
    by_stance: dict[str, list[tuple[str, str]]] = {
        "supports": [],
        "contradicts": [],
        "inconclusive": [],
    }
    for row in _load_golden():
        question = row["question"]
        stances = row.get("stances", {})
        justifications = row.get("stance_justifications", {})
        for pmid, stance in stances.items():
            if pmid in justifications and stance in by_stance:
                by_stance[stance].append((question, str(pmid)))

    rng = random.Random(STANCE_JUSTIFICATION_SAMPLE_SEED)
    sampled: set[tuple[str, str]] = set()
    for stance, pairs in by_stance.items():
        k = min(STANCE_JUSTIFICATION_SAMPLE_PER_STANCE, len(pairs))
        sampled.update(rng.sample(pairs, k))
    return sampled


_STANCE_JUSTIFICATION_SAMPLE = _stance_justification_sample()


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


def _stance_justification_map(result) -> dict[str, str]:
    out: dict[str, str] = {}
    for bucket in (result.supports, result.contradicts, result.inconclusive):
        for f in bucket:
            pmid = f.get("pmid")
            quote = f.get("stance_justification")
            if pmid and quote:
                out[str(pmid)] = quote
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


STANCE_JUSTIFICATION_JUDGE_PROMPT = """\
You are evaluating whether two short quotes from a scientific abstract \
support the same finding about a research question.

Research question: {question}

Golden quote (from human reviewer): "{golden}"

System quote (from automated extraction): "{system}"

The system also classified this paper's stance as: {system_stance}

Decide whether the system's quote points at the same evidence the human \
reviewer pointed at. Both quotes should support the same conclusion about \
the research question — not just be on the same general topic.

Respond with exactly one of these labels on the first line:
- equivalent: the two quotes support the same specific finding (same numbers, \
same outcome, or paraphrased conclusion of the same result)
- partial: the quotes are about the same study and point in the same \
direction but emphasize different facets (e.g., one cites the effect size, \
the other cites the conclusion sentence)
- different: the system's quote does not support the same finding as the \
golden quote, or the system quote does not actually support the system's \
own stance label

Then on the next line, give a one-sentence reason.\
"""


def _judge_pair(question: str, golden: str, system: str, system_stance: str) -> float:
    prompt = STANCE_JUSTIFICATION_JUDGE_PROMPT.format(
        question=question,
        golden=golden,
        system=system,
        system_stance=system_stance,
    )
    resp = _anthropic().messages.create(
        model=JUDGE_MODEL,
        max_tokens=200,
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip().lower()
    first_line = text.splitlines()[0] if text else ""
    if first_line.startswith("equivalent"):
        return 1.0
    if first_line.startswith("partial"):
        return 0.5
    return 0.0


def stance_justification_scorer(input, output, expected) -> float:
    """Mean LLM-judge score over the stratified (question, pmid) sample.

    Only scored on pmids in `_STANCE_JUSTIFICATION_SAMPLE` that the system
    actually surfaced with a stance_justification. Pmids in the sample but
    missing from the system output (not retrieved, or extracted without a
    quote) are silently skipped — that's a coverage problem caught by recall,
    not by stance justification.
    """
    golden_quotes = {str(k): v for k, v in expected.get("stance_justifications", {}).items()}
    system_quotes = _stance_justification_map(output)
    system_stances = _stance_map(output)
    pmids = [
        p
        for p in golden_quotes
        if p in system_quotes and (input, p) in _STANCE_JUSTIFICATION_SAMPLE
    ]
    if not pmids:
        return 0.0
    scores = [
        _judge_pair(
            question=input,
            golden=golden_quotes[p],
            system=system_quotes[p],
            system_stance=system_stances.get(p, "unknown"),
        )
        for p in pmids
    ]
    return sum(scores) / len(scores)


def _data():
    for row in _load_golden():
        yield {
            "input": row["question"],
            "expected": {
                "relevant_pmids": row.get("relevant_pmids", []),
                "stances": row.get("stances", {}),
                "stance_justifications": row.get("stance_justifications", {}),
            },
        }


def run_eval():
    Eval(
        PROJECT,
        experiment_name="contra",
        data=lambda: list(_data()),
        task=task,
        scores=[
            precision_scorer,
            recall_scorer,
            stance_accuracy_scorer,
            stance_justification_scorer,
        ],
    )


if __name__ == "__main__":
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY not set — stance_justification_scorer will fail.", file=sys.stderr)
    run_eval()
