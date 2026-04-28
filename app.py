"""
Contra — Gradio web UI.

Single text input → contradiction-aware answer over PubMed Alzheimer's papers.
Loads the Retriever once at startup so each query just runs the LLM steps.

Run locally:
    uv run python app.py

Deploy: copy this file (and its dependencies) to a HuggingFace Space configured
as a Gradio SDK app. Set RAILWAY_DATABASE_URL and OPENAI_API_KEY as Space secrets.
"""

import os
import time

import gradio as gr
from dotenv import load_dotenv

load_dotenv()

if os.getenv("BRAINTRUST_API_KEY"):
    import braintrust

    braintrust.init_logger(project="contra")
    braintrust.auto_instrument()

from contra.db import resolve_url
from contra.pipeline import PipelineResult, run_query
from contra.retrieval import Retriever

# Default to railway (deployed); set CONTRA_TARGET=local for dev.
DEFAULT_TARGET = os.getenv("CONTRA_TARGET", "railway")

EXAMPLES = [
    "Does lithium slow cognitive decline in Alzheimer's?",
    "Do anti-amyloid antibodies improve clinical outcomes in Alzheimer's?",
    "Is the Mediterranean diet protective against Alzheimer's?",
    "Do statins reduce Alzheimer's risk?",
    "Is there a causal link between herpes simplex virus and Alzheimer's?",
]

# Load the retriever once. ~5s cold start; pays off after the first query.
print(f"[startup] Loading Retriever (target={DEFAULT_TARGET})...")
_t0 = time.time()
RETRIEVER = Retriever(resolve_url(DEFAULT_TARGET))
print(f"[startup] Retriever ready: {len(RETRIEVER.papers):,} papers in {time.time()-_t0:.1f}s")


def _format_findings(findings: list[dict]) -> str:
    """Render a list of findings as a Markdown block."""
    if not findings:
        return "_(none)_"
    lines = []
    for f in findings:
        year = f.get("year") or "?"
        title = (f.get("title") or "").strip()
        claim = (f.get("claim") or "").strip()
        pmid = f.get("pmid")
        n = f.get("sample_size")
        n_str = f"n={n}" if n else "n=?"
        pop = f.get("population") or "—"
        conf = f.get("confidence") or "?"
        link = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else None
        title_md = f"**[{title}]({link})**" if link else f"**{title}**"
        lines.append(
            f"- [{year}] {title_md}  \n"
            f"  _{claim}_  \n"
            f"  <sub>{pop} · {n_str} · confidence: {conf}</sub>"
        )
    return "\n".join(lines)


def handle_query(question: str) -> tuple[str, str, str, str, str]:
    """Gradio handler. Returns (summary_md, counts_md, supports_md, contradicts_md, inconclusive_md)."""
    question = (question or "").strip()
    if not question:
        return ("Please enter a research question.", "", "", "", "")

    try:
        result: PipelineResult = run_query(
            question, target=DEFAULT_TARGET, retriever=RETRIEVER
        )
    except Exception as e:
        return (f"**Error:** {e}", "", "", "", "")

    counts_md = (
        f"**Supports:** {len(result.supports)} · "
        f"**Contradicts:** {len(result.contradicts)} · "
        f"**Inconclusive:** {len(result.inconclusive)}  \n"
        f"<sub>retrieval {result.metadata['timings'].get('retrieval_s', '?')}s · "
        f"extraction {result.metadata['timings'].get('extraction_s', '?')}s · "
        f"synthesis {result.metadata['timings'].get('synthesis_s', '?')}s</sub>"
    )

    return (
        f"### Summary\n\n{result.summary}",
        counts_md,
        _format_findings(result.supports),
        _format_findings(result.contradicts),
        _format_findings(result.inconclusive),
    )


with gr.Blocks(title="Contra — Alzheimer's Contradiction Detector") as demo:
    gr.Markdown(
        "# Contra\n"
        "**Find where the Alzheimer's research disagrees.**  \n"
        "Ask a research question. Contra retrieves relevant clinical studies, "
        "classifies each as supporting or contradicting your question, and "
        "summarizes where the evidence conflicts."
    )

    with gr.Row():
        question = gr.Textbox(
            label="Research question",
            placeholder="e.g., Does lithium slow cognitive decline in Alzheimer's?",
            lines=2,
            scale=4,
        )
        submit = gr.Button("Search", variant="primary", scale=1)

    gr.Examples(examples=EXAMPLES, inputs=question)

    summary_out = gr.Markdown()
    counts_out = gr.Markdown()

    with gr.Tabs():
        with gr.Tab("Supporting studies"):
            supports_out = gr.Markdown()
        with gr.Tab("Contradicting studies"):
            contradicts_out = gr.Markdown()
        with gr.Tab("Inconclusive"):
            inconclusive_out = gr.Markdown()

    submit.click(
        fn=handle_query,
        inputs=question,
        outputs=[summary_out, counts_out, supports_out, contradicts_out, inconclusive_out],
    )
    question.submit(
        fn=handle_query,
        inputs=question,
        outputs=[summary_out, counts_out, supports_out, contradicts_out, inconclusive_out],
    )


if __name__ == "__main__":
    demo.launch()
