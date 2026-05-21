"""Append-only logs for defensive self-play artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.evidence.storage import REPO_ROOT


SELFPLAY_DIR = REPO_ROOT / "data/selfplay"
SELFPLAY_VARIANTS_LOG = SELFPLAY_DIR / "variants.jsonl"
SELFPLAY_SIMULATIONS_LOG = SELFPLAY_DIR / "simulated_data.jsonl"
SELFPLAY_DETECTIONS_LOG = SELFPLAY_DIR / "detection_results.jsonl"
SELFPLAY_REWARDS_LOG = SELFPLAY_DIR / "rewards.jsonl"
SELFPLAY_STATE_PATH = SELFPLAY_DIR / "selfplay_state.json"


def append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def reset_selfplay_logs() -> None:
    if not SELFPLAY_DIR.exists():
        return
    for path in (
        SELFPLAY_VARIANTS_LOG,
        SELFPLAY_SIMULATIONS_LOG,
        SELFPLAY_DETECTIONS_LOG,
        SELFPLAY_REWARDS_LOG,
        SELFPLAY_STATE_PATH,
    ):
        path.unlink(missing_ok=True)
