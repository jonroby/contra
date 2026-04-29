"""
Contra — FastAPI backend serving the React frontend.

Stage 1: minimal shell. Health endpoint + static-file mount for the built
React app. Pipeline endpoints (`/api/query`) come in Stage 2.

Run locally:
    # build the frontend once
    cd frontend && npm install && npm run build && cd ..
    # run the backend
    uv run uvicorn app:app --host 0.0.0.0 --port 8000

For development with hot-reload, run the Vite dev server (`npm run dev`) on
port 5173 — it proxies /api to localhost:8000.

Deploy: HuggingFace Docker Space. The Dockerfile builds the frontend and
runs uvicorn.
"""

import os
import time
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

load_dotenv()

if os.getenv("BRAINTRUST_API_KEY"):
    import braintrust

    braintrust.init_logger(project="contra")
    braintrust.auto_instrument()

from contra.db import resolve_url
from contra.retrieval import Retriever

DEFAULT_TARGET = os.getenv("CONTRA_TARGET", "railway")

print(f"[startup] Loading Retriever (target={DEFAULT_TARGET})...")
_t0 = time.time()
RETRIEVER = Retriever(resolve_url(DEFAULT_TARGET))
print(
    f"[startup] Retriever ready: {len(RETRIEVER.papers):,} papers in "
    f"{time.time() - _t0:.1f}s"
)

app = FastAPI(title="Contra")


@app.get("/api/health")
def health() -> dict:
    return {"status": "ok", "papers": len(RETRIEVER.papers)}


# Mount the built React app last so /api/* routes take precedence.
FRONTEND_DIST = Path(__file__).parent / "frontend" / "dist"
if FRONTEND_DIST.exists():
    app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="frontend")
else:
    print(
        f"[startup] WARNING: {FRONTEND_DIST} not found. "
        "Run `cd frontend && npm run build` to build the React app."
    )
