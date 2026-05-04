"""Convert completed metadata-only intake entries into candidate records."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from engine.common import validate_candidate, write_yaml


REQUIRED_COMPLETION_GATES = [
    "raw_threads_content_excluded",
    "pii_excluded",
    "only_structured_metadata",
    "human_review_completed",
]


def build_intake_conversion_report(
    intake: dict[str, Any],
    candidate_schema: dict[str, Any],
    sparse_schema: dict[str, Any],
    *,
    write_candidates: bool = False,
    repo_root: Path | None = None,
) -> dict[str, Any]:
    """Build a conversion report and optionally write valid candidate records."""

    entries = intake.get("intake_entries", [])
    if not isinstance(entries, list):
        entries = []

    converted_records = []
    blocked_entries = []
    written_count = 0
    repo_root = repo_root or Path.cwd()

    for entry in entries:
        if not isinstance(entry, dict):
            blocked_entries.append(
                {
                    "intake_id": "unknown",
                    "candidate_stub_id": "",
                    "candidate_record_output_target": "",
                    "blockers": ["intake entry must be a mapping"],
                }
            )
            continue

        record, blockers = build_candidate_record_from_intake_entry(entry, intake, candidate_schema, sparse_schema)
        target = str(entry.get("candidate_record_output_target") or "")
        if blockers:
            blocked_entries.append(
                {
                    "intake_id": str(entry.get("intake_id") or ""),
                    "candidate_stub_id": str(entry.get("candidate_stub_id") or ""),
                    "candidate_record_output_target": target,
                    "blockers": blockers,
                }
            )
            continue

        validate_candidate(record, candidate_schema, sparse_schema)
        output_path = _safe_candidate_output_path(repo_root, target)
        if write_candidates:
            write_yaml(output_path, record)
            written_count += 1
        converted_records.append(
            {
                "intake_id": str(entry.get("intake_id") or ""),
                "candidate_stub_id": str(entry.get("candidate_stub_id") or ""),
                "candidate_id": record["candidate_id"],
                "candidate_record_output_target": target,
                "written": bool(write_candidates),
            }
        )

    blocked_count = len(blocked_entries)
    converted_count = len(converted_records)
    return {
        "schema_version": "candidate_intake_conversion_report_v1",
        "batch_id": str(intake.get("batch_id") or ""),
        "source_intake_schema_version": str(intake.get("schema_version") or ""),
        "conversion_mode": "write_candidates" if write_candidates else "report_only",
        "status": _report_status(len(entries), blocked_count),
        "summary": {
            "intake_count": len(entries),
            "converted_count": converted_count,
            "blocked_count": blocked_count,
            "written_count": written_count,
            "candidate_records_written": bool(write_candidates and written_count),
        },
        "converted_records": converted_records,
        "blocked_entries": blocked_entries,
        "required_completion_gates": REQUIRED_COMPLETION_GATES,
        "next_actions": _next_actions(blocked_count, converted_count),
        "guardrails": {
            "external_systems_accessed": False,
            "raw_threads_content_included": False,
            "pii_included": False,
            "candidate_records_fabricated": False,
            "requires_human_review_before_conversion": True,
            "candidate_records_written": bool(write_candidates and written_count),
        },
    }


def build_candidate_record_from_intake_entry(
    entry: dict[str, Any],
    intake: dict[str, Any],
    candidate_schema: dict[str, Any],
    sparse_schema: dict[str, Any],
) -> tuple[dict[str, Any], list[str]]:
    blockers: list[str] = []

    fill_status = entry.get("fill_status")
    if fill_status != "completed":
        blockers.append("fill_status must be completed")

    features, feature_blockers = _normalize_sparse_features(entry.get("sparse_feature_observations"), sparse_schema)
    blockers.extend(feature_blockers)

    review, review_blockers = _normalize_review(entry.get("review_metadata_to_fill"), candidate_schema)
    blockers.extend(review_blockers)

    gate_blockers = _validate_completion_gate(entry.get("completion_gate"))
    blockers.extend(gate_blockers)

    target = str(entry.get("candidate_record_output_target") or "")
    if not target:
        blockers.append("candidate_record_output_target is required")
    candidate_id = Path(target).stem if target else str(entry.get("intake_id") or "")
    if not candidate_id:
        blockers.append("candidate_id could not be derived from candidate_record_output_target")

    embedding, embedding_blockers = _normalize_embedding(entry.get("embedding"))
    blockers.extend(embedding_blockers)
    record = {
        "schema_version": "candidate_record_v2",
        "candidate_id": candidate_id,
        "batch_id": str(intake.get("batch_id") or ""),
        "sparse_vector": {
            "schema_version": sparse_schema.get("schema_version"),
            "features": features,
        },
        "embedding": embedding,
        "review": review,
        "source_stub": {
            "candidate_stub_id": str(entry.get("candidate_stub_id") or ""),
            "task_id": str(entry.get("task_id") or ""),
            "signal_hint": str(entry.get("signal_hint") or ""),
            "expected_behavior": str(entry.get("expected_behavior") or ""),
        },
        "structured_hints": _normalize_structured_hints(entry.get("structured_hints_to_fill")),
        "metadata_guardrails": {
            "raw_threads_content_excluded": True,
            "pii_excluded": True,
            "only_structured_metadata": True,
            "human_review_completed": True,
        },
    }

    if blockers:
        return record, blockers

    try:
        validate_candidate(record, candidate_schema, sparse_schema)
    except Exception as error:  # noqa: BLE001 - return validation message in report.
        blockers.append(str(error))
    return record, blockers


def _normalize_sparse_features(
    observations: Any,
    sparse_schema: dict[str, Any],
) -> tuple[dict[str, int], list[str]]:
    blockers: list[str] = []
    features: dict[str, int] = {}
    if not isinstance(observations, dict):
        return features, ["sparse_feature_observations must be a mapping"]

    allowed_features = list(sparse_schema.get("features", {}))
    for feature_name in allowed_features:
        if feature_name not in observations:
            blockers.append(f"sparse feature {feature_name!r} is missing")
            continue
        value, value_error = _normalize_binary(observations.get(feature_name))
        if value_error:
            blockers.append(f"sparse feature {feature_name!r} must be completed as 0 or 1")
            continue
        features[str(feature_name)] = value

    unknown_features = sorted(str(name) for name in set(observations) - set(allowed_features))
    if unknown_features:
        blockers.append(f"unknown sparse feature observations: {', '.join(unknown_features)}")
    return features, blockers


def _normalize_review(review_input: Any, candidate_schema: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    blockers: list[str] = []
    if not isinstance(review_input, dict):
        return {}, ["review_metadata_to_fill must be a mapping"]

    allowed_decisions = set(candidate_schema.get("properties", {}).get("review", {}).get("allowed_decisions", []))
    decision = review_input.get("decision")
    if decision not in allowed_decisions:
        blockers.append("review.decision must be scam, non_scam, or uncertain")

    confidence, confidence_error = _normalize_number(review_input.get("confidence"))
    if confidence_error or confidence is None or not 0 <= confidence <= 1:
        blockers.append("review.confidence must be a number between 0 and 1")

    review_time, review_time_error = _normalize_number(review_input.get("review_time_seconds"))
    if review_time_error or review_time is None or review_time < 0:
        blockers.append("review.review_time_seconds must be a non-negative number")

    second_review, second_review_error = _normalize_bool(review_input.get("second_review_required"))
    if second_review_error:
        blockers.append("review.second_review_required must be boolean")

    return (
        {
            "decision": decision,
            "confidence": confidence,
            "review_time_seconds": review_time,
            "second_review_required": second_review,
        },
        blockers,
    )


def _validate_completion_gate(gate: Any) -> list[str]:
    if not isinstance(gate, dict):
        return ["completion_gate must be a mapping"]
    blockers = []
    for gate_name in REQUIRED_COMPLETION_GATES:
        value, value_error = _normalize_bool(gate.get(gate_name))
        if value_error or value is not True:
            blockers.append(f"completion_gate.{gate_name} must be true")
    return blockers


def _normalize_structured_hints(hints: Any) -> dict[str, Any]:
    if not isinstance(hints, dict):
        return {
            "common_behaviors": [],
            "structural_patterns": [],
            "reviewer_signals": [],
            "hard_negative_contrast": "",
            "metadata_only_note": "metadata_only",
        }
    return {
        "common_behaviors": _normalize_string_list(hints.get("common_behaviors")),
        "structural_patterns": _normalize_string_list(hints.get("structural_patterns")),
        "reviewer_signals": _normalize_string_list(hints.get("reviewer_signals")),
        "hard_negative_contrast": str(hints.get("hard_negative_contrast") or ""),
        "metadata_only_note": str(hints.get("metadata_only_note") or "metadata_only"),
    }


def _normalize_string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [str(item) for item in value if str(item).strip()]


def _normalize_embedding(embedding: Any) -> tuple[dict[str, Any], list[str]]:
    if not isinstance(embedding, dict):
        return {"model": "none", "dim": 0, "vector": []}, []
    blockers = []
    vector = embedding.get("vector")
    if not isinstance(vector, list):
        vector = []
        blockers.append("embedding.vector must be a list when embedding is provided")
    dim_input = embedding.get("dim", len(vector))
    if isinstance(dim_input, bool):
        dim = len(vector)
        blockers.append("embedding.dim must be a non-negative integer when embedding is provided")
    else:
        try:
            dim = int(dim_input)
        except (TypeError, ValueError):
            dim = len(vector)
            blockers.append("embedding.dim must be a non-negative integer when embedding is provided")
    return {
        "model": str(embedding.get("model") or "none"),
        "dim": dim,
        "vector": vector,
    }, blockers


def _normalize_binary(value: Any) -> tuple[int, bool]:
    normalized, error = _normalize_bool(value)
    if error:
        if value in (0, 1):
            return int(value), False
        if isinstance(value, str) and value.strip() in {"0", "1"}:
            return int(value.strip()), False
        return 0, True
    return int(bool(normalized)), False


def _normalize_bool(value: Any) -> tuple[bool | None, bool]:
    if isinstance(value, bool):
        return value, False
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized in {"true", "yes"}:
            return True, False
        if normalized in {"false", "no"}:
            return False, False
    return None, True


def _normalize_number(value: Any) -> tuple[float | None, bool]:
    if isinstance(value, bool) or value is None:
        return None, True
    if isinstance(value, (int, float)):
        return float(value), False
    if isinstance(value, str):
        try:
            return float(value.strip()), False
        except ValueError:
            return None, True
    return None, True


def _safe_candidate_output_path(repo_root: Path, target: str) -> Path:
    if not target:
        raise ValueError("candidate_record_output_target is required")
    target_path = Path(target)
    if target_path.is_absolute():
        raise ValueError("candidate_record_output_target must be repo-relative")
    output_path = (repo_root / target_path).resolve()
    repo_root_resolved = repo_root.resolve()
    candidates_root = (repo_root_resolved / "data" / "candidates").resolve()
    if not _is_relative_to(output_path, candidates_root):
        raise ValueError("candidate_record_output_target must stay under data/candidates")
    return output_path


def _is_relative_to(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def _next_actions(blocked_count: int, converted_count: int) -> list[str]:
    if blocked_count:
        return [
            "Complete human review metadata in the intake worksheet.",
            "Set all completion gates to true only after raw content and PII are excluded.",
            "Re-run this conversion report before writing candidate records.",
        ]
    if converted_count:
        return [
            "Run candidate validation on data/candidates.",
            "Run the v2 ROS pipeline and compare SVS, sparse clusters, and discrepancy reports.",
        ]
    return ["No intake entries found; rebuild or inspect the candidate intake worksheet."]


def _report_status(entry_count: int, blocked_count: int) -> str:
    if entry_count == 0:
        return "empty"
    if blocked_count:
        return "blocked"
    return "ready"
