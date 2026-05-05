"""Generate safe synthetic data from self-play variants."""

from __future__ import annotations

import hashlib
import json
from typing import Any

from src.evidence.storage import utc_now
from src.selfplay.logging import SELFPLAY_SIMULATIONS_LOG, append_jsonl


def generate_simulated_data(variant: dict[str, Any], *, log: bool = False) -> dict[str, Any]:
    """Create one abstract, tagged synthetic sample from an adversarial variant."""
    text = _safe_simulation_text(variant)
    simulation_id = _simulation_id(str(variant.get("variant_id")), text)
    record = {
        "schema_version": "selfplay_simulated_data_v1",
        "simulation_id": simulation_id,
        "variant_id": variant.get("variant_id"),
        "origin_concept_id": variant.get("origin_concept_id"),
        "origin_concept_name": variant.get("origin_concept_name"),
        "origin_dominant_signal": variant.get("origin_dominant_signal"),
        "evasion_characteristic": variant.get("evasion_characteristic"),
        "difficulty": variant.get("difficulty", 0.0),
        "text": text,
        "candidate_type": "selfplay_simulated",
        "source": "defensive_selfplay",
        "tag": "abstract_safe_simulation",
        "simulated": True,
        "non_actionable": True,
        "actionable_content_included": False,
        "created_at": utc_now(),
        "raw_source_included": False,
    }
    if log:
        append_jsonl(SELFPLAY_SIMULATIONS_LOG, record)
    return record


def _safe_simulation_text(variant: dict[str, Any]) -> str:
    strategy = str(variant.get("variant_strategy", "surface-language mutation"))
    characteristic = str(variant.get("evasion_characteristic", "unknown_evasion"))
    example = str(variant.get("abstract_example", "Abstract sample only."))
    return (
        f"Abstract defensive simulation. Strategy: {strategy} "
        f"Evasion characteristic: {characteristic}. "
        f"{example} The sample intentionally omits platform names, contact details, payment details, "
        "promised outcomes, and step-by-step instructions."
    )


def _simulation_id(variant_id: str, text: str) -> str:
    material = json.dumps({"variant_id": variant_id, "text": text}, ensure_ascii=False, sort_keys=True)
    digest = hashlib.sha1(material.encode("utf-8")).hexdigest()[:12]
    return f"selfplay_simulation_{digest}"
