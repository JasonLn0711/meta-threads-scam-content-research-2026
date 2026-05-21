"""Reward calculation for defensive self-play."""

from __future__ import annotations

from typing import Any

from src.evidence.storage import utc_now
from src.selfplay.logging import SELFPLAY_REWARDS_LOG, append_jsonl


def compute_rewards(
    A_output: dict[str, Any],
    B_output: dict[str, Any],
    *,
    log: bool = False,
) -> dict[str, Any]:
    """Compute adversary and detector rewards from one self-play exchange."""
    confidence = _clamp(float(B_output.get("confidence", 0.0) or 0.0))
    origin_concept_id = A_output.get("origin_concept_id")
    matched = bool(origin_concept_id and B_output.get("matched_concept") == origin_concept_id)
    partial_detection = bool(B_output.get("is_scam_like") and B_output.get("novelty"))
    accuracy_component = 1.0 if matched else 0.58 if partial_detection else 0.0
    adversary_reward = 1.0 - confidence
    detector_reward = (0.72 * accuracy_component) + (0.28 * confidence)
    result = {
        "schema_version": "selfplay_reward_v1",
        "variant_id": A_output.get("variant_id"),
        "simulation_id": B_output.get("simulation_id"),
        "origin_concept_id": origin_concept_id,
        "matched_concept": B_output.get("matched_concept"),
        "detection_confidence": round(confidence, 6),
        "accuracy_component": round(accuracy_component, 6),
        "adversary_reward": round(_clamp(adversary_reward), 6),
        "detector_reward": round(_clamp(detector_reward), 6),
        "created_at": utc_now(),
        "simulated": True,
        "raw_source_included": False,
    }
    if log:
        append_jsonl(SELFPLAY_REWARDS_LOG, result)
    return result


def _clamp(value: float) -> float:
    return max(0.0, min(1.0, float(value)))
