"""Signal ranking entrypoint for the sparse engine."""

from __future__ import annotations

from typing import Any

from engine.sparse.svs import build_latest_ranking


def rank_signals(candidates: list[dict[str, Any]], sparse_schema: dict[str, Any]) -> dict[str, Any]:
    return build_latest_ranking(candidates, sparse_schema)
