"""
Local terminal eval — hits the local FastAPI server (`uv run uvicorn app:app
--port 8000`) for each golden question and prints a clean per-question
report to stdout. No Braintrust, no LLM judge.

Every full run is persisted to `evals/runs/{timestamp}-{git_sha}.json` so
that `cli/eval_history.py` can show metric drift over time. Partial runs
(via --questions) are not persisted to keep the history honest.

Run:
    # in one terminal
    uv run uvicorn app:app --port 8000

    # in another
    uv run python cli/eval.py
    uv run python cli/eval.py --questions 1,19
    uv run python cli/eval.py --show-justifications
"""

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import httpx

GOLDEN_PATH = Path(__file__).parent.parent / "evals" / "golden.json"
RUNS_DIR = Path(__file__).parent.parent / "evals" / "runs"
API_URL = "http://localhost:8000"
QUERY_TIMEOUT_S = 180.0


def _bucket(output: dict, name: str) -> list[dict]:
    return output.get(name) or []


def _surfaced_pmids(output: dict) -> set[str]:
    pmids: set[str] = set()
    for name in ("supports", "contradicts", "inconclusive"):
        for f in _bucket(output, name):
            if pmid := f.get("pmid"):
                pmids.add(str(pmid))
    return pmids


def _stance_map(output: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    for direction in ("supports", "contradicts", "inconclusive"):
        for f in _bucket(output, direction):
            if pmid := f.get("pmid"):
                out[str(pmid)] = direction
    return out


def _justification_map(output: dict) -> dict[str, str]:
    out: dict[str, str] = {}
    for direction in ("supports", "contradicts", "inconclusive"):
        for f in _bucket(output, direction):
            pmid = f.get("pmid")
            quote = f.get("stance_justification")
            if pmid and quote:
                out[str(pmid)] = quote
    return out


def _truncate(items: list, max_n: int) -> str:
    if len(items) <= max_n:
        return ", ".join(items)
    return ", ".join(items[:max_n]) + f", ... +{len(items) - max_n} more"


def _query_api(client: httpx.Client, question: str) -> dict:
    resp = client.post("/api/query", json={"question": question})
    resp.raise_for_status()
    return resp.json()


def _evaluate_one(
    client: httpx.Client,
    question: str,
    expected: dict,
    show_missed: int,
    show_extra: int,
    show_justifications: bool,
) -> dict:
    output = _query_api(client, question)
    surfaced = _surfaced_pmids(output)
    relevant = {str(p) for p in expected.get("relevant_pmids", [])}

    overlap = surfaced & relevant
    missed = relevant - surfaced
    extra = surfaced - relevant

    precision = len(overlap) / len(surfaced) if surfaced else 0.0
    recall = len(overlap) / len(relevant) if relevant else 0.0

    predicted_stances = _stance_map(output)
    golden_stances = {str(k): v for k, v in expected.get("stances", {}).items()}
    stance_overlap = [p for p in golden_stances if p in predicted_stances]
    stance_correct = sum(
        1 for p in stance_overlap if predicted_stances[p] == golden_stances[p]
    )
    stance_acc = stance_correct / len(stance_overlap) if stance_overlap else None

    just_pairs = []
    if show_justifications:
        golden_justifications = expected.get("stance_justifications", {})
        system_justifications = _justification_map(output)
        for pmid in sorted(stance_overlap):
            if pmid in golden_justifications and pmid in system_justifications:
                just_pairs.append({
                    "pmid": pmid,
                    "golden_stance": golden_stances[pmid],
                    "system_stance": predicted_stances[pmid],
                    "golden_quote": golden_justifications[pmid],
                    "system_quote": system_justifications[pmid],
                })

    return {
        "question": question,
        "n_surfaced": len(surfaced),
        "n_relevant": len(relevant),
        "n_overlap": len(overlap),
        "precision": precision,
        "recall": recall,
        "stance_correct": stance_correct,
        "stance_overlap": len(stance_overlap),
        "stance_acc": stance_acc,
        "missed_str": _truncate(sorted(missed), show_missed),
        "extra_str": _truncate(sorted(extra), show_extra),
        "just_pairs": just_pairs,
    }


def _print_one(idx: int, row: dict, show_justifications: bool) -> None:
    title = row["question"]
    if len(title) > 76:
        title = title[:73] + "..."
    print(f"Q{idx:02d}  {title}")
    print(
        f"     surfaced: {row['n_surfaced']:<3} "
        f"relevant: {row['n_relevant']:<3} "
        f"overlap:  {row['n_overlap']}"
    )
    stance_str = (
        f"stance_acc: {row['stance_acc']:.2f} "
        f"({row['stance_correct']}/{row['stance_overlap']})"
        if row["stance_acc"] is not None
        else "stance_acc: n/a (no overlap)"
    )
    print(
        f"     precision: {row['precision']:.2f}  "
        f"recall: {row['recall']:.2f}   "
        f"{stance_str}"
    )
    if row["missed_str"]:
        print(f"     missed:    [{row['missed_str']}]")
    if row["extra_str"]:
        print(f"     extra:     [{row['extra_str']}]")

    if show_justifications and row["just_pairs"]:
        print()
        for pair in row["just_pairs"]:
            agree = "✓" if pair["golden_stance"] == pair["system_stance"] else "✗"
            print(
                f"     PMID {pair['pmid']} "
                f"(golden: {pair['golden_stance']}, "
                f"system: {pair['system_stance']}) {agree}"
            )
            print(f"       golden:  \"{pair['golden_quote'][:120]}...\"")
            print(f"       system:  \"{pair['system_quote'][:120]}...\"")
    print()


def _compute_totals(rows: list[dict]) -> dict:
    n = len(rows)
    if not n:
        return {}

    total_surfaced = sum(r["n_surfaced"] for r in rows)
    total_relevant = sum(r["n_relevant"] for r in rows)
    total_overlap = sum(r["n_overlap"] for r in rows)
    total_stance_correct = sum(r["stance_correct"] for r in rows)
    total_stance_overlap = sum(r["stance_overlap"] for r in rows)

    stance_rows = [r for r in rows if r["stance_acc"] is not None]

    return {
        "n_questions": n,
        "n_surfaced": total_surfaced,
        "n_relevant": total_relevant,
        "n_overlap": total_overlap,
        "n_stance_correct": total_stance_correct,
        "n_stance_overlap": total_stance_overlap,
        "macro_precision": sum(r["precision"] for r in rows) / n,
        "macro_recall": sum(r["recall"] for r in rows) / n,
        "macro_stance_acc": (
            sum(r["stance_acc"] for r in stance_rows) / len(stance_rows)
            if stance_rows
            else None
        ),
        "micro_precision": total_overlap / total_surfaced if total_surfaced else 0.0,
        "micro_recall": total_overlap / total_relevant if total_relevant else 0.0,
        "micro_stance_acc": (
            total_stance_correct / total_stance_overlap
            if total_stance_overlap
            else None
        ),
    }


def _print_totals(totals: dict) -> None:
    print("─" * 78)
    print(
        f"TOTAL  surfaced: {totals['n_surfaced']}  "
        f"relevant: {totals['n_relevant']}  "
        f"overlap: {totals['n_overlap']}"
    )
    print(
        f"       macro  precision: {totals['macro_precision']:.2f}  "
        f"recall: {totals['macro_recall']:.2f}  "
        f"stance_acc: {totals['macro_stance_acc']:.2f}"
    )
    print(
        f"       micro  precision: {totals['micro_precision']:.2f}  "
        f"recall: {totals['micro_recall']:.2f}  "
        f"stance_acc: {totals['micro_stance_acc']:.2f} "
        f"({totals['n_stance_correct']}/{totals['n_stance_overlap']})"
    )


def _git_sha() -> str:
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=Path(__file__).parent.parent,
            stderr=subprocess.DEVNULL,
        )
        return sha.decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "nogit"


def _save_run(rows: list[dict], totals: dict, partial: bool) -> Path:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    sha = _git_sha()
    suffix = "-partial" if partial else ""
    path = RUNS_DIR / f"{timestamp}-{sha}{suffix}.json"
    RUNS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "timestamp_utc": timestamp,
        "git_sha": sha,
        "api_url": API_URL,
        "partial": partial,
        "totals": totals,
        "rows": rows,
    }
    with open(path, "w") as f:
        json.dump(payload, f, indent=2)
    return path


def _check_api(client: httpx.Client) -> None:
    try:
        resp = client.get("/api/health", timeout=5.0)
        resp.raise_for_status()
    except (httpx.ConnectError, httpx.HTTPStatusError, httpx.ReadTimeout) as exc:
        sys.exit(
            f"ERROR: {API_URL}/api/health unreachable ({exc}).\n"
            f"Start the local server with: uv run uvicorn app:app --port 8000"
        )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--questions",
        help="Comma-separated 1-indexed question numbers (e.g. '1,19'). Default: all.",
    )
    parser.add_argument(
        "--show-missed",
        type=int,
        default=8,
        help="Max golden pmids to print for the 'missed' line (default: 8).",
    )
    parser.add_argument(
        "--show-extra",
        type=int,
        default=8,
        help="Max surfaced pmids to print for the 'extra' line (default: 8).",
    )
    parser.add_argument(
        "--show-justifications",
        action="store_true",
        help="Print golden vs system stance_justification quotes for overlapping pmids.",
    )
    parser.add_argument(
        "--no-save",
        action="store_true",
        help="Skip persisting this run to evals/runs/. Default is to always save.",
    )
    args = parser.parse_args()

    with open(GOLDEN_PATH) as f:
        golden = json.load(f)

    if args.questions:
        wanted = {int(x) for x in args.questions.split(",")}
        selected = [(i + 1, q) for i, q in enumerate(golden) if i + 1 in wanted]
    else:
        selected = list(enumerate(golden, start=1))

    print(f"Running {len(selected)} question(s) against {API_URL}...\n")

    with httpx.Client(base_url=API_URL, timeout=QUERY_TIMEOUT_S) as client:
        _check_api(client)

        rows = []
        for idx, q in selected:
            try:
                row = _evaluate_one(
                    client=client,
                    question=q["question"],
                    expected={
                        "relevant_pmids": q.get("relevant_pmids", []),
                        "stances": q.get("stances", {}),
                        "stance_justifications": q.get("stance_justifications", {}),
                    },
                    show_missed=args.show_missed,
                    show_extra=args.show_extra,
                    show_justifications=args.show_justifications,
                )
            except Exception as exc:
                print(f"Q{idx:02d}  ERROR: {exc}\n", file=sys.stderr)
                continue
            rows.append(row)
            _print_one(idx, row, args.show_justifications)

    if rows:
        totals = _compute_totals(rows)
        _print_totals(totals)

        if not args.no_save:
            partial = bool(args.questions)
            path = _save_run(rows, totals, partial=partial)
            tag = " (partial)" if partial else ""
            print(f"\nSaved run{tag} to {path.relative_to(Path.cwd())}")


if __name__ == "__main__":
    main()
