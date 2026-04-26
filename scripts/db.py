"""Shared DB target resolution: --target local|railway -> DATABASE_URL."""

import os


def resolve_url(target: str) -> str:
    """Return DATABASE_URL for the given target ("local" or "railway")."""
    env_name = "DATABASE_URL" if target == "local" else "RAILWAY_DATABASE_URL"
    url = os.getenv(env_name)
    if not url:
        raise SystemExit(f"{env_name} not set in .env")
    return url
