"""Generate ranked feature hypotheses from discrepancy groups.

This module proposes testable representation hypotheses only. It does not
modify sparse schemas, promote features, or use embeddings for decisions.
"""

from __future__ import annotations

from typing import Any

from engine.common import active_sparse_features, candidate_id


def auto_generate_feature_candidates(
    discrepancy_report: dict[str, Any],
    candidates: list[dict[str, Any]],
    min_group_size: int = 3,
) -> dict[str, Any]:
    candidate_by_id = {candidate_id(candidate): candidate for candidate in candidates}
    valid_groups = []
    skipped_cases = []

    for case in discrepancy_report.get("cases", []):
        case_id = str(case.get("case_id") or "")
        case_type = str(case.get("type") or "")
        candidate_ids = [str(item) for item in case.get("candidate_ids", [])]
        if case_type != "missed_pattern":
            skipped_cases.append(_skipped(case_id, candidate_ids, "not_missed_pattern"))
            continue
        if len(candidate_ids) < min_group_size:
            skipped_cases.append(_skipped(case_id, candidate_ids, "group_size_below_minimum"))
            continue
        loaded_candidates = [candidate_by_id[item_id] for item_id in candidate_ids if item_id in candidate_by_id]
        if len(loaded_candidates) < min_group_size:
            skipped_cases.append(_skipped(case_id, candidate_ids, "candidate_metadata_missing_or_group_too_small"))
            continue
        valid_groups.append({"case": case, "candidates": loaded_candidates})

    features = []
    for group in valid_groups:
        features.extend(_features_for_group(group["case"], group["candidates"]))

    ranked_features = sorted(
        features,
        key=lambda feature: (
            -int(feature["ranking"]["group_size"]),
            -float(feature["ranking"]["pattern_consistency"]),
            -float(feature["ranking"]["expected_clustering_impact"]),
            -float(feature["ranking"]["expected_discrepancy_reduction"]),
            str(feature["feature_id"]),
        ),
    )

    return {
        "schema_version": "auto_generated_feature_candidates_v1",
        "purpose": "rank testable sparse-representation hypotheses from valid missed-pattern discrepancy groups",
        "source_discrepancy_report": "outputs/discrepancy_reports/latest.yaml",
        "source_candidates": "data/candidates/*.yaml",
        "filters": {
            "case_type": "missed_pattern",
            "minimum_group_size": min_group_size,
            "raw_threads_evidence_allowed": False,
        },
        "summary": {
            "input_case_count": len(discrepancy_report.get("cases", [])),
            "valid_group_count": len(valid_groups),
            "skipped_case_count": len(skipped_cases),
            "feature_count": len(ranked_features),
        },
        "features": ranked_features,
        "skipped_cases": skipped_cases,
        "guardrails": {
            "sparse_schema_modified": False,
            "features_auto_promoted": False,
            "embedding_used_for_decision": False,
            "raw_threads_content_included": False,
            "pii_included": False,
        },
    }


def _features_for_group(case: dict[str, Any], candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    case_id = str(case.get("case_id") or "unknown_case")
    candidate_ids = [candidate_id(candidate) for candidate in candidates]
    group_size = len(candidates)
    proposals = []

    common_features = _common_sparse_features(candidates)
    if common_features:
        proposals.append(
            _proposal(
                feature_id=f"emergent_common_sparse_bridge_{case_id}",
                definition="Valid missed-pattern group shares existing sparse behavior units that may need a bridge feature.",
                activation_rule=" AND ".join(common_features),
                supporting_cases=candidate_ids,
                group_size=group_size,
                consistency=1.0,
                clustering_impact=0.75,
                discrepancy_reduction=0.8,
                expected_effect="should merge currently fragmented sparse clusters when shared behavior units are underweighted",
            )
        )

    reply_count = sum(1 for candidate in candidates if _feature(candidate, "reply_funnel"))
    contact_count = sum(1 for candidate in candidates if _feature(candidate, "誘導聯絡"))
    community_count = sum(1 for candidate in candidates if _feature(candidate, "社群導流"))
    value_count = sum(1 for candidate in candidates if _feature(candidate, "保證收益") or _feature(candidate, "成果展示"))
    needs_thread_count = sum(1 for candidate in candidates if _feature(candidate, "needs_thread"))
    second_review_count = sum(1 for candidate in candidates if candidate.get("review", {}).get("second_review_required"))
    high_time_count = sum(
        1 for candidate in candidates if float(candidate.get("review", {}).get("review_time_seconds") or 0) >= 150
    )

    behavior_patterns = [
        (
            "reply_contact_funnel_structure",
            reply_count + contact_count + community_count,
            "reply or contact/community funnel metadata is common in the missed-pattern group",
            "(reply_funnel OR 誘導聯絡 OR 社群導流)",
            "should improve sparse grouping of thread-mediated funnel structures",
        ),
        (
            "value_claim_anchor_structure",
            value_count,
            "guarantee or result-display metadata is common in the missed-pattern group",
            "(保證收益 OR 成果展示)",
            "should improve sparse grouping of value-claim anchors without relying on wording",
        ),
        (
            "thread_burden_structure",
            needs_thread_count + second_review_count + high_time_count,
            "reviewer burden metadata is common in the missed-pattern group",
            "(needs_thread OR second_review_required OR review_time_seconds >= 150)",
            "should separate high-burden ambiguity from low-burden high-value candidates",
        ),
    ]

    for pattern_name, support, definition, activation_rule, expected_effect in behavior_patterns:
        consistency = support / max(group_size, 1)
        if consistency < 0.67:
            continue
        proposals.append(
            _proposal(
                feature_id=f"emergent_{pattern_name}_{case_id}",
                definition=definition,
                activation_rule=activation_rule,
                supporting_cases=candidate_ids,
                group_size=group_size,
                consistency=consistency,
                clustering_impact=0.65,
                discrepancy_reduction=0.7,
                expected_effect=expected_effect,
            )
        )

    return proposals


def _common_sparse_features(candidates: list[dict[str, Any]]) -> list[str]:
    feature_sets = [set(active_sparse_features(candidate)) for candidate in candidates]
    if not feature_sets:
        return []
    return sorted(set.intersection(*feature_sets))


def _feature(candidate: dict[str, Any], name: str) -> bool:
    return bool(candidate.get("sparse_vector", {}).get("features", {}).get(name))


def _proposal(
    feature_id: str,
    definition: str,
    activation_rule: str,
    supporting_cases: list[str],
    group_size: int,
    consistency: float,
    clustering_impact: float,
    discrepancy_reduction: float,
    expected_effect: str,
) -> dict[str, Any]:
    return {
        "feature_id": feature_id,
        "type": "emergent",
        "definition": definition,
        "activation_rule": activation_rule,
        "supporting_cases": supporting_cases,
        "confidence": _confidence_label(consistency, group_size),
        "expected_effect": expected_effect,
        "ranking": {
            "group_size": group_size,
            "pattern_consistency": round(consistency, 6),
            "expected_clustering_impact": round(clustering_impact, 6),
            "expected_discrepancy_reduction": round(discrepancy_reduction, 6),
        },
    }


def _confidence_label(consistency: float, group_size: int) -> str:
    if group_size >= 5 and consistency >= 0.8:
        return "high"
    if group_size >= 3 and consistency >= 0.67:
        return "medium"
    return "low"


def _skipped(case_id: str, candidate_ids: list[str], reason: str) -> dict[str, Any]:
    return {
        "case_id": case_id,
        "candidate_ids": candidate_ids,
        "group_size": len(candidate_ids),
        "reason": reason,
    }
