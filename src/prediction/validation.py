"""Validation hooks for predicted variants against later observations."""

from __future__ import annotations

import math
from typing import Any

from src.embedding.encoder import encode
from src.evidence.storage import utc_now
from src.prediction.logging import VALIDATION_RESULTS_LOG, append_jsonl


def track_prediction_validation(
    predicted_variants: list[dict[str, Any]],
    observed_candidates: list[dict[str, Any]],
    *,
    current_round: int | None = None,
    log: bool = False,
) -> dict[str, Any]:
    """Track whether predicted variants are later observed in candidate metadata."""
    results = [_validate_variant(variant, observed_candidates, current_round=current_round) for variant in predicted_variants]
    payload = {
        "schema_version": "prediction_validation_v1",
        "generated_at": utc_now(),
        "results": results,
        "summary": {
            "variant_count": len(results),
            "observed_count": sum(1 for result in results if result["observed"]),
            "validation_mode": "synthetic_metadata_only",
        },
        "raw_content_included": False,
    }
    if log:
        append_jsonl(VALIDATION_RESULTS_LOG, payload)
    return payload


def _validate_variant(
    variant: dict[str, Any],
    candidates: list[dict[str, Any]],
    *,
    current_round: int | None,
) -> dict[str, Any]:
    variant_text = str(variant.get("example_text") or variant.get("search_query") or "")
    best = {"candidate_id": None, "similarity": 0.0, "round": None}
    for candidate in candidates:
        text = _candidate_text(candidate)
        if not text:
            continue
        similarity = _cosine(encode(variant_text), encode(text))
        if similarity > float(best["similarity"]):
            best = {
                "candidate_id": candidate.get("candidate_id"),
                "similarity": round(similarity, 6),
                "round": candidate.get("round"),
            }
    observed = float(best["similarity"]) >= 0.72
    observed_round = best["round"] if observed else None
    origin_round = variant.get("origin_round")
    if observed and current_round is not None and origin_round is not None:
        lag = max(0, int(current_round) - int(origin_round))
    else:
        lag = None
    return {
        "variant_id": variant.get("variant_id"),
        "origin_concept_id": variant.get("origin_concept_id"),
        "observed": observed,
        "best_candidate_id": best["candidate_id"] if observed else None,
        "best_similarity": best["similarity"],
        "first_observed_round": observed_round,
        "time_lag_rounds": lag,
        "validation_note": "synthetic observation only; real validation requires governed evidence",
    }


def _candidate_text(candidate: dict[str, Any]) -> str:
    for key in ("text", "raw_text", "example_text"):
        if candidate.get(key):
            return str(candidate[key])
    features = candidate.get("features", {}) if isinstance(candidate.get("features"), dict) else {}
    return " ".join(
        str(value)
        for value in (
            features.get("expected_signal"),
            features.get("concept_name"),
            features.get("concept_dominant_signal"),
        )
        if value
    )


def _cosine(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return 0.0
    return max(0.0, min(1.0, numerator / (left_norm * right_norm)))
