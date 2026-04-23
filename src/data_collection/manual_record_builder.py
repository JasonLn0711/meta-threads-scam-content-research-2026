"""Build schema-v1 records from manually supplied, local-only fields."""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone
from typing import Any

from .metadata_extractor import extract_visible_metadata


ARRAY_FIELDS = {
    "reply_texts",
    "image_paths",
    "external_links",
    "visible_contact_handles",
    "visible_platform_redirects",
    "scam_type",
    "signal_tags",
    "missing_evidence",
}

BOOL_FIELDS = {"has_image", "has_reply", "has_external_link", "disagreement_flag"}
INT_FIELDS = {"image_count"}

SCHEMA_FIELDS = (
    "item_id",
    "schema_version",
    "source_platform",
    "source_type",
    "collection_batch_id",
    "collection_timestamp",
    "collection_method",
    "authorization_status",
    "post_text",
    "reply_texts",
    "image_paths",
    "image_count",
    "has_image",
    "has_reply",
    "has_external_link",
    "external_links",
    "visible_contact_handles",
    "visible_platform_redirects",
    "ocr_text",
    "language",
    "screenshot_style",
    "scam_label",
    "scam_type",
    "risk_level",
    "signal_tags",
    "evidence_sufficiency",
    "annotation_confidence",
    "annotation_notes",
    "annotator_id",
    "reviewer_id",
    "review_status",
    "adjudication_status",
    "disagreement_flag",
    "final_label",
    "final_risk_level",
    "source_url_if_stored",
    "screenshot_snapshot_status",
    "link_snapshot_status",
    "metadata_notes",
    "privacy_redaction_notes",
    "dedupe_key",
    "near_duplicate_group_id",
    "missing_evidence",
    "baseline_split",
)


def build_thread_item_record(payload: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    defaults = dict(config.get("defaults", {}))
    record: dict[str, Any] = {}

    for field in SCHEMA_FIELDS:
        if field in payload:
            record[field] = coerce_field(field, payload[field])
        elif field in defaults:
            record[field] = coerce_field(field, defaults[field])
        else:
            record[field] = default_for_field(field)

    if not record["item_id"]:
        raise ValueError("item_id is required")
    if not record["collection_timestamp"]:
        record["collection_timestamp"] = datetime.now(timezone.utc).isoformat(timespec="seconds")

    _derive_visible_metadata(record, config)
    _derive_booleans_and_statuses(record)
    _derive_missing_evidence(record)
    _derive_dedupe_key(record, config)
    return {field: record[field] for field in SCHEMA_FIELDS}


def _derive_visible_metadata(record: dict[str, Any], config: dict[str, Any]) -> None:
    builder = config.get("manual_record_builder", {})
    if not builder.get("auto_extract_visible_metadata", True):
        return
    privacy = config.get("privacy", {})
    extracted = extract_visible_metadata(
        post_text=str(record.get("post_text") or ""),
        reply_texts=list(record.get("reply_texts") or []),
        ocr_text=str(record.get("ocr_text") or ""),
        explicit_links=list(record.get("external_links") or []),
        explicit_handles=list(record.get("visible_contact_handles") or []),
        explicit_redirects=list(record.get("visible_platform_redirects") or []),
        external_link_storage=str(privacy.get("external_link_storage", "domain_only")),
    )
    record["external_links"] = extracted["external_links"]
    record["visible_contact_handles"] = extracted["visible_contact_handles"]
    record["visible_platform_redirects"] = extracted["visible_platform_redirects"]


def _derive_booleans_and_statuses(record: dict[str, Any]) -> None:
    record["image_count"] = max(int(record.get("image_count") or 0), len(record.get("image_paths") or []))
    record["has_image"] = bool(record["image_count"] or record.get("image_paths"))
    record["has_reply"] = bool(record.get("reply_texts"))
    record["has_external_link"] = bool(record.get("external_links"))

    if not record.get("screenshot_snapshot_status") or record["screenshot_snapshot_status"] == "not_applicable":
        if record["has_image"]:
            record["screenshot_snapshot_status"] = "captured_redacted" if record.get("image_paths") else "not_captured"
        else:
            record["screenshot_snapshot_status"] = "not_applicable"

    if not record.get("link_snapshot_status") or record["link_snapshot_status"] == "not_applicable":
        record["link_snapshot_status"] = "not_captured" if record["has_external_link"] else "not_applicable"


def _derive_missing_evidence(record: dict[str, Any]) -> None:
    if record.get("missing_evidence") and record["missing_evidence"] != ["none"]:
        return
    missing: list[str] = []
    if not str(record.get("post_text") or "").strip():
        missing.append("post_text_missing")
    if record.get("has_image") and not str(record.get("ocr_text") or "").strip():
        missing.append("ocr_missing_or_low_quality")
    if record.get("has_external_link") and record.get("link_snapshot_status") in {"not_captured", "unavailable"}:
        missing.append("link_snapshot_missing")
    record["missing_evidence"] = missing or ["none"]


def _derive_dedupe_key(record: dict[str, Any], config: dict[str, Any]) -> None:
    builder = config.get("manual_record_builder", {})
    if record.get("dedupe_key") or not builder.get("auto_generate_dedupe_key", True):
        return
    pieces = [
        str(record.get("post_text") or ""),
        " ".join(record.get("reply_texts") or []),
        str(record.get("ocr_text") or ""),
        " ".join(record.get("external_links") or []),
        " ".join(record.get("visible_contact_handles") or []),
    ]
    normalized = " ".join(" ".join(pieces).lower().split())
    record["dedupe_key"] = "sha256:" + hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:16]


def coerce_field(field: str, value: Any) -> Any:
    if field in ARRAY_FIELDS:
        return coerce_list(value)
    if field in BOOL_FIELDS:
        return coerce_bool(value)
    if field in INT_FIELDS:
        return int(value or 0)
    if value is None:
        return ""
    return str(value)


def coerce_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if isinstance(value, str):
        return [part.strip() for part in value.split("|") if part.strip()]
    return [str(value).strip()]


def coerce_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    lowered = str(value or "").strip().lower()
    if lowered in {"true", "1", "yes", "y"}:
        return True
    if lowered in {"false", "0", "no", "n", ""}:
        return False
    raise ValueError(f"cannot parse boolean value: {value!r}")


def default_for_field(field: str) -> Any:
    if field in ARRAY_FIELDS:
        return ["none"] if field in {"scam_type", "signal_tags", "missing_evidence"} else []
    if field in BOOL_FIELDS:
        return False
    if field in INT_FIELDS:
        return 0
    return ""
