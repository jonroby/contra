"""
LLM synthesis: turn grouped findings into a 2-3 sentence state-of-evidence summary.
"""

from openai import OpenAI

MODEL = "gpt-4o-mini"

SYNTHESIS_PROMPT = """\
Research question: "{query}"

The following findings were extracted from {n_papers} scientific papers.

SUPPORTING ({n_supports}):
{supports_block}

CONTRADICTING ({n_contradicts}):
{contradicts_block}

INCONCLUSIVE ({n_inconclusive}):
{inconclusive_block}

Write a 2-3 sentence summary of the current state of evidence. If supports and
contradicts both exist, highlight that there is genuine disagreement and
identify likely reasons (different populations, dosages, study designs, sample
sizes). Be specific and grounded in the findings above. Do not invent details.
"""


def _block(items: list[dict], cap: int = 8) -> str:
    if not items:
        return "(none)"
    lines = []
    for it in items[:cap]:
        claim = it.get("claim") or "(no claim)"
        pop = it.get("population") or "?"
        n = it.get("sample_size")
        n_str = f"n={n}" if n else "n=?"
        lines.append(f"- {claim} [{pop}, {n_str}, {it.get('year')}]")
    if len(items) > cap:
        lines.append(f"- ... and {len(items) - cap} more")
    return "\n".join(lines)


def synthesize(query: str, findings: list[dict]) -> str:
    supports = [f for f in findings if f.get("direction") == "supports"]
    contradicts = [f for f in findings if f.get("direction") == "contradicts"]
    inconclusive = [f for f in findings if f.get("direction") == "inconclusive"]

    prompt = SYNTHESIS_PROMPT.format(
        query=query,
        n_papers=len(findings),
        n_supports=len(supports),
        n_contradicts=len(contradicts),
        n_inconclusive=len(inconclusive),
        supports_block=_block(supports),
        contradicts_block=_block(contradicts),
        inconclusive_block=_block(inconclusive),
    )

    client = OpenAI()
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return resp.choices[0].message.content.strip()
