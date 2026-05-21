"""Adversarial adaptation heuristics for synthetic candidate metadata."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from src.evidence.storage import REPO_ROOT, utc_now
from src.intelligence.yaml_store import write_yaml


ADVERSARIAL_PATTERNS_PATH = REPO_ROOT / "data/adversarial_patterns.yaml"


def detect_adversarial_patterns(
    candidates: list[dict[str, Any]],
    *,
    output_path: Path = ADVERSARIAL_PATTERNS_PATH,
) -> dict[str, Any]:
    """Detect simple, explainable adversarial adaptation signals."""
    findings: list[dict[str, Any]] = []
    findings.extend(_low_feature_high_scam(candidates))
    findings.extend(_feature_drop_anomalies(candidates))
    findings.extend(_concept_mismatches(candidates))
    findings = sorted(findings, key=lambda row: (-float(row["severity"]), row["type"], row["candidate_id"]))
    payload = {
        "schema_version": "adversarial_patterns_v1",
        "generated_at": utc_now(),
        "findings": findings,
        "summary": {
            "finding_count": len(findings),
            "types": _type_counts(findings),
            "exploration_priority": min(1.0, round(len(findings) / max(1, len(candidates)), 6)),
        },
        "raw_content_included": False,
    }
    write_yaml(output_path, payload)
    return payload


def _low_feature_high_scam(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    findings = []
    for candidate in candidates:
        if not _is_high_scam(candidate):
            continue
        strength = _feature_strength(candidate)
        if strength <= 0.35:
            findings.append(
                {
                    "type": "low_feature_high_scam",
                    "candidate_id": candidate.get("candidate_id", ""),
                    "concept_id": _concept_id(candidate),
                    "feature_strength": strength,
                    "severity": round(1.0 - strength, 6),
                    "reason": "High-value review outcome with weak explicit feature surface.",
                }
            )
    return findings


def _feature_drop_anomalies(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        concept_id = _concept_id(candidate)
        if concept_id:
            grouped[concept_id].append(candidate)

    findings = []
    for concept_id, rows in grouped.items():
        ordered = sorted(rows, key=lambda item: (item.get("round", 0), item.get("created_at", ""), item.get("candidate_id", "")))
        if len(ordered) < 2:
            continue
        first = _average_strength(ordered[: max(1, len(ordered) // 2)])
        second = _average_strength(ordered[max(1, len(ordered) // 2) :])
        scam_count = sum(1 for candidate in ordered if _is_high_scam(candidate))
        if scam_count > 0 and first - second >= 0.25:
            findings.append(
                {
                    "type": "feature_drop_anomaly",
                    "candidate_id": "concept_level",
                    "concept_id": concept_id,
                    "feature_strength_before": first,
                    "feature_strength_after": second,
                    "severity": round(first - second, 6),
                    "reason": "Explicit feature surface declined while scam outcomes remained present.",
                }
            )
    return findings


def _concept_mismatches(candidates: list[dict[str, Any]]) -> list[dict[str, Any]]:
    findings = []
    for candidate in candidates:
        features = _features(candidate)
        expected = str(features.get("expected_signal") or candidate.get("expected_signal") or "")
        dominant = str(features.get("concept_dominant_signal") or "")
        is_novel = bool(features.get("is_novel_concept"))
        high_scam = _is_high_scam(candidate)
        if high_scam and is_novel:
            findings.append(
                {
                    "type": "concept_mismatch",
                    "candidate_id": candidate.get("candidate_id", ""),
                    "concept_id": _concept_id(candidate) or "novel_concept_pool",
                    "severity": 0.85,
                    "reason": "High-value outcome was routed to the novelty pool.",
                }
            )
        elif high_scam and expected and dominant and expected != dominant:
            findings.append(
                {
                    "type": "concept_mismatch",
                    "candidate_id": candidate.get("candidate_id", ""),
                    "concept_id": _concept_id(candidate),
                    "expected_signal": expected,
                    "dominant_signal": dominant,
                    "severity": 0.65,
                    "reason": "Query signal and matched concept signal diverged on a high-value candidate.",
                }
            )
    return findings


def _is_high_scam(candidate: dict[str, Any]) -> bool:
    decision = candidate.get("review_decision") or candidate.get("decision")
    return decision == "scam" or bool(candidate.get("high_value"))


def _feature_strength(candidate: dict[str, Any]) -> float:
    features = _features(candidate)
    explicit_signals = [
        "guaranteed_return",
        "off_platform_contact",
        "impersonation",
        "urgency",
    ]
    signal_score = sum(1 for key in explicit_signals if features.get(key)) / len(explicit_signals)
    concept_confidence = float(features.get("concept_confidence", 0.0) or 0.0)
    mismatch_penalty = 0.2 if features.get("is_novel_concept") else 0.0
    return round(max(0.0, min(1.0, (0.55 * signal_score) + (0.45 * concept_confidence) - mismatch_penalty)), 6)


def _average_strength(candidates: list[dict[str, Any]]) -> float:
    if not candidates:
        return 0.0
    return round(sum(_feature_strength(candidate) for candidate in candidates) / len(candidates), 6)


def _concept_id(candidate: dict[str, Any]) -> str:
    return str(_features(candidate).get("concept_id") or candidate.get("concept_id") or "")


def _features(candidate: dict[str, Any]) -> dict[str, Any]:
    features = candidate.get("features", {})
    return features if isinstance(features, dict) else {}


def _type_counts(findings: list[dict[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = defaultdict(int)
    for finding in findings:
        counts[str(finding["type"])] += 1
    return dict(sorted(counts.items()))
