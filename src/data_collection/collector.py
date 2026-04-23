"""Orchestration helpers for manual-only collection record building."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .collection_log import collection_log_row
from .governance_checks import (
    GovernanceResult,
    check_record_governance,
    load_manual_collection_config as load_config_file,
)
from .manual_record_builder import build_thread_item_record


def build_manual_collection_record(
    payload: dict[str, Any],
    config: dict[str, Any],
    *,
    ack_controlled_details: bool = False,
) -> tuple[dict[str, Any], GovernanceResult, dict[str, str]]:
    record = build_thread_item_record(payload, config)
    governance = check_record_governance(record, config, ack_controlled_details=ack_controlled_details)
    log_row = collection_log_row(record, payload)
    return record, governance, log_row


def load_manual_collection_config(path: str | Path) -> dict[str, Any]:
    return load_config_file(path)
