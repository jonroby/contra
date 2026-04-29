# Stage 1: build the React frontend
FROM node:20-alpine AS frontend-builder
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install
COPY frontend/ ./
RUN npm run build

# Stage 2: Python backend serving the API + the built frontend
FROM python:3.12-slim
WORKDIR /app

# System deps for psycopg and sentence-transformers
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install uv (project uses uv for dependency management)
RUN pip install --no-cache-dir uv

# Copy everything hatchling needs to build the local `contra` package
# (pyproject declares package=true, so uv sync builds it editable).
# README.md is required because pyproject sets readme = "README.md".
COPY pyproject.toml uv.lock* README.md ./
COPY contra/ ./contra/

# Now sync dependencies (this also builds the local contra package)
RUN uv sync --frozen --no-dev || uv sync --no-dev

# Copy the rest of the application code
COPY app.py ./

# Copy the built frontend from stage 1
COPY --from=frontend-builder /app/frontend/dist ./frontend/dist

# HuggingFace Spaces sets PORT, default to 7860 for HF compatibility
ENV PORT=7860
EXPOSE 7860

CMD ["sh", "-c", "uv run uvicorn app:app --host 0.0.0.0 --port ${PORT}"]
