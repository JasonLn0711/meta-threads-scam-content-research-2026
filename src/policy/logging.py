"""Append-only logs for adaptive policy decisions and feedback."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from src.evidence.storage import REPO_ROOT


POLICY_DIR = REPO_ROOT / "data/policy"
POLICY_DECISION_LOG = POLICY_DIR / "context_action_log.jsonl"
POLICY_FEEDBACK_LOG = POLICY_DIR / "feedback_log.jsonl"
POLICY_EVALUATION_LOG = POLICY_DIR / "evaluation_reports.jsonl"
POLICY_STATE_PATH = POLICY_DIR / "policy_state.json"


def append_jsonl(path: Path, entry: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False, sort_keys=True) + "\n")


def read_jsonl(path: Path, *, limit: int | None = None) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows[-limit:] if limit else rows


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def reset_policy_logs() -> None:
    if not POLICY_DIR.exists():
        return
    for path in (
        POLICY_DECISION_LOG,
        POLICY_FEEDBACK_LOG,
        POLICY_EVALUATION_LOG,
        POLICY_STATE_PATH,
    ):
        path.unlink(missing_ok=True)
