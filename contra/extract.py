"""
LLM-based structured extraction from abstracts.

For each (query, abstract) pair, ask the model to extract a finding as JSON:
direction (supports/contradicts/inconclusive), claim, intervention, population,
sample_size, duration, confidence.
"""

import asyncio
import json
from typing import Any

from openai import AsyncOpenAI

MODEL = "gpt-4o-mini"

EXTRACTION_PROMPT = """\
You are analyzing a scientific paper to determine its stance on a research question.

Research question: "{query}"

Paper title: {title}

Paper abstract: {abstract}

Return a JSON object with these fields:
- "claim": one sentence stating the paper's main finding RELATIVE TO THE RESEARCH QUESTION
- "direction": one of "supports", "contradicts", "inconclusive"
    - "supports": the paper's findings would lead someone to answer YES to the research question
    - "contradicts": the paper's findings would lead someone to answer NO
    - "inconclusive": the paper does not directly address the question, or findings are mixed/null
- "stance_justification": a VERBATIM quote (or two) from the abstract that supports the chosen direction.
    Copy the exact sentence(s) — do not paraphrase, summarize, or reformat.
    Pick the sentence that most directly states the result driving the stance
    (e.g., the primary endpoint, the pooled effect size, the conclusion line).
- "intervention": what was tested (e.g., drug name, behavior, biomarker), or null if not applicable
- "population": who was studied (e.g., "early-stage Alzheimer's patients, age 65+"), or null
- "sample_size": integer, or null if not stated
- "duration": study duration as a string (e.g., "12 weeks"), or null
- "confidence": "high" if the abstract clearly addresses the question, "medium" if partial, "low" if tangential

Output valid JSON only.
"""


async def extract_one(client: AsyncOpenAI, query: str, paper) -> dict[str, Any]:
    prompt = EXTRACTION_PROMPT.format(
        query=query, title=paper.title, abstract=paper.abstract
    )
    resp = await client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"},
        temperature=0.0,
    )
    raw = resp.choices[0].message.content
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        data = {"direction": "inconclusive", "claim": "", "error": "json_parse_failed"}
    data["pmid"] = paper.pmid
    data["title"] = paper.title
    data["year"] = paper.year
    data["journal"] = paper.journal
    data["publication_types"] = paper.publication_types
    data["cited_by_count"] = paper.cited_by_count
    data["oa_pdf_url"] = paper.oa_pdf_url
    return data


async def extract_all(query: str, papers: list) -> list[dict[str, Any]]:
    """Run extraction over all papers in parallel."""
    async with AsyncOpenAI() as client:
        tasks = [extract_one(client, query, p) for p in papers]
        return await asyncio.gather(*tasks)
