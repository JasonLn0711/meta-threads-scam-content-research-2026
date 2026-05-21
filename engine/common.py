"""Shared metadata-only helpers for the v2 research operating system."""

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CANDIDATE_SCHEMA = REPO_ROOT / "data-contracts" / "candidate_record_v2.schema.yaml"
DEFAULT_SPARSE_SCHEMA = REPO_ROOT / "meta-system" / "sparse_schema" / "sparse_features_v2.yaml"


class CandidateValidationError(ValueError):
    """Raised when a v2 candidate breaks schema or repo-safety rules."""


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def write_yaml(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(payload, handle, allow_unicode=True, sort_keys=False)


def candidate_paths(candidate_dir: Path) -> list[Path]:
    paths = sorted(candidate_dir.rglob("*.yaml")) + sorted(candidate_dir.rglob("*.yml"))
    return [path for path in paths if path.is_file()]


def load_schema(path: Path = DEFAULT_CANDIDATE_SCHEMA) -> dict[str, Any]:
    schema = load_yaml(path)
    if not isinstance(schema, dict):
        raise CandidateValidationError(f"{path} must contain a YAML object")
    return schema


def load_sparse_schema(path: Path = DEFAULT_SPARSE_SCHEMA) -> dict[str, Any]:
    schema = load_yaml(path)
    if not isinstance(schema, dict) or not isinstance(schema.get("features"), dict):
        raise CandidateValidationError(f"{path} must define a features mapping")
    return schema


def load_candidates(
    candidate_dir: Path,
    schema_path: Path = DEFAULT_CANDIDATE_SCHEMA,
    sparse_schema_path: Path = DEFAULT_SPARSE_SCHEMA,
    validate: bool = True,
) -> list[dict[str, Any]]:
    schema = load_schema(schema_path)
    sparse_schema = load_sparse_schema(sparse_schema_path)
    candidates: list[dict[str, Any]] = []
    for path in candidate_paths(candidate_dir):
        candidate = load_yaml(path)
        if not isinstance(candidate, dict):
            raise CandidateValidationError(f"{path}: candidate must be a YAML object")
        if validate:
            validate_candidate(candidate, schema, sparse_schema, source_path=path)
        candidates.append(candidate)
    return candidates


def validate_candidate(
    candidate: dict[str, Any],
    schema: dict[str, Any],
    sparse_schema: dict[str, Any],
    source_path: Path | None = None,
) -> None:
    prefix = f"{source_path}: " if source_path else ""
    _validate_forbidden_content(candidate, schema, prefix)

    for key in schema.get("required_top_level", []):
        if key not in candidate:
            raise CandidateValidationError(f"{prefix}missing required field {key!r}")

    if candidate.get("schema_version") != "candidate_record_v2":
        raise CandidateValidationError(f"{prefix}schema_version must be candidate_record_v2")
    _require_non_empty_string(candidate, "candidate_id", prefix)
    _require_non_empty_string(candidate, "batch_id", prefix)

    sparse_vector = _require_mapping(candidate, "sparse_vector", prefix)
    if sparse_vector.get("schema_version") != sparse_schema.get("schema_version"):
        raise CandidateValidationError(
            f"{prefix}sparse_vector.schema_version must be {sparse_schema.get('schema_version')}"
        )
    features = _require_mapping(sparse_vector, "features", prefix)
    allowed_features = set(sparse_schema.get("features", {}))
    unknown_features = sorted(set(features) - allowed_features)
    if unknown_features:
        raise CandidateValidationError(f"{prefix}unknown sparse feature(s): {', '.join(unknown_features)}")
    for feature_name, value in features.items():
        if value not in (0, 1, False, True):
            raise CandidateValidationError(f"{prefix}{feature_name!r} must be 0 or 1")

    embedding = _require_mapping(candidate, "embedding", prefix)
    _require_non_empty_string(embedding, "model", prefix)
    dim = embedding.get("dim")
    vector = embedding.get("vector")
    if not isinstance(dim, int) or isinstance(dim, bool) or dim < 0:
        raise CandidateValidationError(f"{prefix}embedding.dim must be a non-negative integer")
    if not isinstance(vector, list):
        raise CandidateValidationError(f"{prefix}embedding.vector must be a list")
    if len(vector) != dim:
        raise CandidateValidationError(f"{prefix}embedding.vector length must equal embedding.dim")
    for value in vector:
        if not isinstance(value, (int, float)) or isinstance(value, bool) or not math.isfinite(value):
            raise CandidateValidationError(f"{prefix}embedding.vector values must be finite numbers")

    review = _require_mapping(candidate, "review", prefix)
    allowed_decisions = set(schema.get("properties", {}).get("review", {}).get("allowed_decisions", []))
    if review.get("decision") not in allowed_decisions:
        raise CandidateValidationError(f"{prefix}review.decision has invalid value {review.get('decision')!r}")
    confidence = review.get("confidence")
    if not isinstance(confidence, (int, float)) or isinstance(confidence, bool) or not (0 <= confidence <= 1):
        raise CandidateValidationError(f"{prefix}review.confidence must be between 0 and 1")
    review_time = review.get("review_time_seconds")
    if not isinstance(review_time, (int, float)) or isinstance(review_time, bool) or review_time < 0:
        raise CandidateValidationError(f"{prefix}review.review_time_seconds must be a non-negative number")
    if not isinstance(review.get("second_review_required"), bool):
        raise CandidateValidationError(f"{prefix}review.second_review_required must be boolean")


def _require_mapping(parent: dict[str, Any], key: str, prefix: str) -> dict[str, Any]:
    value = parent.get(key)
    if not isinstance(value, dict):
        raise CandidateValidationError(f"{prefix}{key} must be a mapping")
    return value


def _require_non_empty_string(parent: dict[str, Any], key: str, prefix: str) -> None:
    value = parent.get(key)
    if not isinstance(value, str) or not value.strip():
        raise CandidateValidationError(f"{prefix}{key} must be a non-empty string")


def _validate_forbidden_content(value: Any, schema: dict[str, Any], prefix: str, path: str = "") -> None:
    forbidden_keys = {str(key).lower() for key in schema.get("forbidden_keys", [])}
    forbidden_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in schema.get("forbidden_string_patterns", [])]

    if isinstance(value, dict):
        for key, child in value.items():
            key_text = str(key)
            if key_text.lower() in forbidden_keys:
                location = f"{path}.{key_text}" if path else key_text
                raise CandidateValidationError(f"{prefix}forbidden raw/sensitive field {location!r}")
            child_path = f"{path}.{key_text}" if path else key_text
            _validate_forbidden_content(child, schema, prefix, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _validate_forbidden_content(child, schema, prefix, f"{path}[{index}]")
    elif isinstance(value, str):
        for pattern in forbidden_patterns:
            if pattern.search(value):
                raise CandidateValidationError(f"{prefix}forbidden raw/sensitive string at {path!r}")


def feature_weights(sparse_schema: dict[str, Any]) -> dict[str, float]:
    weights: dict[str, float] = {}
    for name, spec in sparse_schema.get("features", {}).items():
        weight = spec.get("weight", 1.0) if isinstance(spec, dict) else 1.0
        weights[str(name)] = float(weight)
    return weights


def active_sparse_features(candidate: dict[str, Any]) -> list[str]:
    features = candidate.get("sparse_vector", {}).get("features", {})
    if not isinstance(features, dict):
        return []
    return sorted(str(name) for name, value in features.items() if bool(value))


def sparse_feature_value(candidate: dict[str, Any], feature_name: str) -> int:
    value = candidate.get("sparse_vector", {}).get("features", {}).get(feature_name, 0)
    return 1 if bool(value) else 0


def candidate_id(candidate: dict[str, Any]) -> str:
    return str(candidate.get("candidate_id") or "")


def batch_id(candidate: dict[str, Any]) -> str:
    return str(candidate.get("batch_id") or "")


def review_decision(candidate: dict[str, Any]) -> str:
    return str(candidate.get("review", {}).get("decision") or "")


def review_time_seconds(candidate: dict[str, Any]) -> float:
    return max(float(candidate.get("review", {}).get("review_time_seconds") or 0.0), 1.0)


def second_review_required(candidate: dict[str, Any]) -> bool:
    return bool(candidate.get("review", {}).get("second_review_required"))


def embedding_vector(candidate: dict[str, Any]) -> list[float]:
    vector = candidate.get("embedding", {}).get("vector", [])
    if not isinstance(vector, list):
        return []
    return [float(value) for value in vector]
