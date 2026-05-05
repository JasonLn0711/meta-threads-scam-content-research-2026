"""Append-only local logs for synthetic prediction artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.evidence.storage import REPO_ROOT


PREDICTIONS_DIR = REPO_ROOT / "data/predictions"
PREDICTED_VARIANTS_LOG = PREDICTIONS_DIR / "predicted_variants.jsonl"
SIMULATED_POSTS_LOG = PREDICTIONS_DIR / "simulated_posts.jsonl"
SIMULATION_SCORES_LOG = PREDICTIONS_DIR / "simulation_scores.jsonl"
VALIDATION_RESULTS_LOG = PREDICTIONS_DIR / "validation_results.jsonl"


def append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


def reset_prediction_logs() -> None:
    if not PREDICTIONS_DIR.exists():
        return
    for path in (
        PREDICTED_VARIANTS_LOG,
        SIMULATED_POSTS_LOG,
        SIMULATION_SCORES_LOG,
        VALIDATION_RESULTS_LOG,
    ):
        path.unlink(missing_ok=True)
