"""Generate metadata-only feature candidates from discrepancy reports."""

from __future__ import annotations

from copy import deepcopy
from typing import Any


def generate_feature_candidates(discrepancy_report: dict[str, Any]) -> list[dict[str, Any]]:
    cases = discrepancy_report.get("cases", [])
    candidates: list[dict[str, Any]] = []

    missed_cases = [case for case in cases if case.get("type") == "missed_pattern"]
    if missed_cases:
        candidates.append(
            {
                "feature_id": "emergent_embedding_close_sparse_gap",
                "type": "emergent",
                "definition": "Embedding-close candidate pairs are not explained by current sparse features.",
                "activation_rule": "Pending human definition; do not activate until accepted and rewritten as an explainable binary sparse rule.",
                "supporting_cases": [case["case_id"] for case in missed_cases],
                "confidence": _confidence(len(missed_cases)),
                "status": "proposed",
                "promotion_allowed_without_human_review": False,
            }
        )

    broad_cases = [case for case in cases if case.get("type") == "over_generalization"]
    if broad_cases:
        candidates.append(
            {
                "feature_id": "emergent_sparse_cluster_split_signal",
                "type": "emergent",
                "definition": "Sparse-similar candidate pairs are far apart in discovery-only embedding space.",
                "activation_rule": "Pending human review; use only to decide whether an existing sparse feature needs narrowing or a split feature.",
                "supporting_cases": [case["case_id"] for case in broad_cases],
                "confidence": _confidence(len(broad_cases)),
                "status": "proposed",
                "promotion_allowed_without_human_review": False,
            }
        )

    return candidates


def build_review_queue(feature_candidates: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": "feature_review_queue_v1",
        "human_review_required": True,
        "allowed_decisions": ["pending", "accepted", "rejected"],
        "items": [
            {
                "feature_id": candidate["feature_id"],
                "decision": "pending",
                "review_note": "Human reviewer must accept or reject before sparse schema promotion.",
            }
            for candidate in feature_candidates
        ],
    }


def promote_accepted_features(
    sparse_schema: dict[str, Any],
    feature_candidates: list[dict[str, Any]],
    review_queue: dict[str, Any],
    default_weight: float = 1.0,
) -> dict[str, Any]:
    """Return a copy of sparse_schema with accepted feature candidates added.

    This function does not infer acceptance. It only honors explicit human queue
    decisions with `decision: accepted`.
    """

    promoted = deepcopy(sparse_schema)
    promoted.setdefault("features", {})
    by_id = {candidate["feature_id"]: candidate for candidate in feature_candidates}

    for item in review_queue.get("items", []):
        if item.get("decision") != "accepted":
            continue
        feature_id = str(item.get("feature_id") or "")
        candidate = by_id.get(feature_id)
        if not candidate or feature_id in promoted["features"]:
            continue
        weight = float(candidate.get("weight", default_weight))
        promoted["features"][feature_id] = {
            "type": "human_accepted_emergent",
            "weight": weight,
            "definition": candidate.get("definition", ""),
            "activation_rule": candidate.get("activation_rule", ""),
            "derived_from_feature_candidate": feature_id,
        }

    return promoted


def _confidence(case_count: int) -> float:
    return round(min(0.75, 0.35 + (case_count * 0.1)), 3)
