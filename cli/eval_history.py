"""
Read all eval runs persisted by `cli/eval_local.py` and print a chronological
table of headline metrics, with deltas vs the previous run.

Run:
    uv run python cli/eval_history.py
    uv run python cli/eval_history.py --include-partial
    uv run python cli/eval_history.py --last 10
"""

import argparse
import json
from pathlib import Path

RUNS_DIR = Path(__file__).parent.parent / "evals" / "runs"


def _load_runs(include_partial: bool) -> list[dict]:
    if not RUNS_DIR.exists():
        return []
    runs = []
    for path in sorted(RUNS_DIR.glob("*.json")):
        with open(path) as f:
            data = json.load(f)
        if data.get("partial") and not include_partial:
            continue
        data["_path"] = path
        runs.append(data)
    return runs


def _arrow(curr: float | None, prev: float | None) -> str:
    if curr is None or prev is None:
        return "  "
    diff = curr - prev
    if abs(diff) < 0.005:
        return "·"
    return "↑" if diff > 0 else "↓"


def _fmt(value: float | None) -> str:
    return f"{value:.2f}" if value is not None else " n/a"


def _print_table(runs: list[dict]) -> None:
    if not runs:
        print("No runs found in evals/runs/. Run cli/eval_local.py first.")
        return

    header = (
        f"{'when (UTC)':<17}  "
        f"{'sha':<14}  "
        f"{'questions':>9}  "
        f"{'precision':>11}  "
        f"{'recall':>10}  "
        f"{'stance_acc':>13}"
    )
    print(header)
    print("─" * len(header))

    prev = None
    for run in runs:
        totals = run.get("totals") or {}
        ts = run["timestamp_utc"]
        when = f"{ts[:4]}-{ts[4:6]}-{ts[6:8]} {ts[9:11]}:{ts[11:13]}"
        sha = run.get("git_sha", "nogit")
        n_q = totals.get("n_questions", 0)
        macro_p = totals.get("macro_precision")
        macro_r = totals.get("macro_recall")
        macro_s = totals.get("macro_stance_acc")

        if prev:
            prev_t = prev.get("totals") or {}
            ap = _arrow(macro_p, prev_t.get("macro_precision"))
            ar = _arrow(macro_r, prev_t.get("macro_recall"))
            as_ = _arrow(macro_s, prev_t.get("macro_stance_acc"))
        else:
            ap = ar = as_ = " "

        partial_tag = " *" if run.get("partial") else "  "
        print(
            f"{when}{partial_tag} "
            f"{sha:<14}  "
            f"{n_q:>9}  "
            f"{_fmt(macro_p):>9} {ap}  "
            f"{_fmt(macro_r):>8} {ar}  "
            f"{_fmt(macro_s):>11} {as_}"
        )
        prev = run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--include-partial",
        action="store_true",
        help="Include partial runs (those with --questions filter) in the history.",
    )
    parser.add_argument(
        "--last",
        type=int,
        help="Only show the last N runs.",
    )
    args = parser.parse_args()

    runs = _load_runs(include_partial=args.include_partial)
    if args.last:
        runs = runs[-args.last:]
    _print_table(runs)
    if any(r.get("partial") for r in runs):
        print("\n* partial run (--questions filter)")


if __name__ == "__main__":
    main()
