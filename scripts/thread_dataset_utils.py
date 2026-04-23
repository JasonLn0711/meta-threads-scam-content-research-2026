"""Small helpers for Threads dataset v1 scripts.

These utilities intentionally avoid collection, crawling, or platform access.
They only read local CSV/JSON/JSONL files that already exist.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


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

NONE_EXCLUSIVE_FIELDS = {
    "visible_platform_redirects",
    "scam_type",
    "signal_tags",
    "missing_evidence",
}

TEXT_FIELDS_FOR_DEDUP = ("post_text", "ocr_text")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_records(path: Path) -> list[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return load_csv_records(path)
    if suffix == ".jsonl":
        return load_jsonl_records(path)
    if suffix == ".json":
        data = load_json(path)
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return [data]
        raise ValueError(f"{path} must contain a JSON object or array")
    raise ValueError(f"Unsupported dataset format for {path}; use .csv, .json, or .jsonl")


def load_csv_records(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return [coerce_csv_record(row) for row in reader]


def load_jsonl_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        data = json.loads(stripped)
        if not isinstance(data, dict):
            raise ValueError(f"{path}:{line_number} must be a JSON object")
        records.append(data)
    return records


def coerce_csv_record(row: dict[str, str | None]) -> dict[str, Any]:
    record: dict[str, Any] = {}
    for key, raw_value in row.items():
        value = "" if raw_value is None else raw_value.strip()
        if key in ARRAY_FIELDS:
            record[key] = split_array(value)
        elif key in BOOL_FIELDS:
            record[key] = parse_bool(value)
        elif key in INT_FIELDS:
            record[key] = int(value) if value else 0
        else:
            record[key] = value
    return record


def split_array(value: str) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in value.split("|") if part.strip()]


def parse_bool(value: str) -> bool:
    lowered = value.lower()
    if lowered in {"true", "1", "yes", "y"}:
        return True
    if lowered in {"false", "0", "no", "n", ""}:
        return False
    raise ValueError(f"Cannot parse boolean value: {value!r}")


def normalize_text(value: Any) -> str:
    if isinstance(value, list):
        value = " ".join(str(item) for item in value)
    return " ".join(str(value or "").lower().split())


def record_text(record: dict[str, Any], fields: tuple[str, ...]) -> str:
    parts: list[str] = []
    for field in fields:
        value = record.get(field)
        if isinstance(value, list):
            parts.extend(str(item) for item in value)
        elif value:
            parts.append(str(value))
    return "\n".join(parts)


def summarize_counts(records: list[dict[str, Any]], field: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for record in records:
        value = record.get(field)
        if isinstance(value, list):
            values = value or ["<empty>"]
        else:
            values = [value if value not in (None, "") else "<empty>"]
        for item in values:
            counts[str(item)] = counts.get(str(item), 0) + 1
    return dict(sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])))


def load_schema(path: Path) -> dict[str, Any]:
    schema = load_json(path)
    if not isinstance(schema, dict):
        raise ValueError(f"{path} must contain a JSON schema object")
    return schema


def validate_records(records: list[dict[str, Any]], schema: dict[str, Any]) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    required = schema.get("required", [])
    properties = schema.get("properties", {})

    for index, record in enumerate(records, 1):
        item_id = str(record.get("item_id") or f"<row {index}>")
        unknown_fields = sorted(set(record) - set(properties))
        for field in unknown_fields:
            if record.get(field) not in ("", None, []):
                errors.append(f"{item_id}: unknown field {field}")

        for field in required:
            if field not in record:
                errors.append(f"{item_id}: missing required field {field}")
                continue
            if record.get(field) is None:
                errors.append(f"{item_id}: required field {field} is null")

        for field, value in record.items():
            if field not in properties:
                continue
            prop = properties[field]
            validate_field(item_id, field, value, prop, errors)

        validate_consistency(item_id, record, errors, warnings)

    return errors, warnings


def validate_field(
    item_id: str,
    field: str,
    value: Any,
    prop: dict[str, Any],
    errors: list[str],
) -> None:
    expected = prop.get("type")
    if expected == "string":
        if not isinstance(value, str):
            errors.append(f"{item_id}: {field} must be a string")
        if prop.get("minLength") and isinstance(value, str) and len(value) < prop["minLength"]:
            errors.append(f"{item_id}: {field} must not be empty")
        if "const" in prop and value != prop["const"]:
            errors.append(f"{item_id}: {field} must equal {prop['const']!r}")
        if "enum" in prop and value not in prop["enum"]:
            errors.append(f"{item_id}: {field} has invalid value {value!r}")
    elif expected == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            errors.append(f"{item_id}: {field} must be an integer")
        elif "minimum" in prop and value < prop["minimum"]:
            errors.append(f"{item_id}: {field} must be >= {prop['minimum']}")
    elif expected == "boolean":
        if not isinstance(value, bool):
            errors.append(f"{item_id}: {field} must be a boolean")
    elif expected == "array":
        if not isinstance(value, list):
            errors.append(f"{item_id}: {field} must be an array")
            return
        min_items = prop.get("minItems")
        if min_items and len(value) < min_items:
            errors.append(f"{item_id}: {field} must have at least {min_items} item(s)")
        item_schema = prop.get("items", {})
        enum = item_schema.get("enum")
        for item in value:
            if item_schema.get("type") == "string" and not isinstance(item, str):
                errors.append(f"{item_id}: {field} item {item!r} must be a string")
            if enum and item not in enum:
                errors.append(f"{item_id}: {field} has invalid item {item!r}")


def validate_consistency(
    item_id: str,
    record: dict[str, Any],
    errors: list[str],
    warnings: list[str],
) -> None:
    for field in NONE_EXCLUSIVE_FIELDS:
        values = record.get(field, [])
        if isinstance(values, list) and "none" in values and len(values) > 1:
            errors.append(f"{item_id}: {field} cannot combine 'none' with other values")

    image_count = record.get("image_count")
    has_image = record.get("has_image")
    image_paths = record.get("image_paths", [])
    if isinstance(image_count, int) and isinstance(has_image, bool):
        if has_image and image_count == 0:
            errors.append(f"{item_id}: has_image is true but image_count is 0")
        if not has_image and image_count > 0:
            errors.append(f"{item_id}: has_image is false but image_count is > 0")
    if isinstance(image_count, int) and isinstance(image_paths, list) and len(image_paths) > image_count:
        warnings.append(f"{item_id}: image_paths has more entries than image_count")

    if isinstance(record.get("has_reply"), bool) and isinstance(record.get("reply_texts"), list):
        if record["has_reply"] and not record["reply_texts"]:
            warnings.append(f"{item_id}: has_reply is true but reply_texts is empty")
        if not record["has_reply"] and record["reply_texts"]:
            warnings.append(f"{item_id}: has_reply is false but reply_texts is not empty")

    if isinstance(record.get("has_external_link"), bool) and isinstance(record.get("external_links"), list):
        if record["has_external_link"] and not record["external_links"]:
            warnings.append(f"{item_id}: has_external_link is true but external_links is empty")
        if not record["has_external_link"] and record["external_links"]:
            warnings.append(f"{item_id}: has_external_link is false but external_links is not empty")

    if record.get("review_status") == "adjudicated":
        if not record.get("final_label"):
            warnings.append(f"{item_id}: adjudicated item has blank final_label")
        if not record.get("final_risk_level"):
            warnings.append(f"{item_id}: adjudicated item has blank final_risk_level")


def content_shape(record: dict[str, Any]) -> str:
    has_text = bool(str(record.get("post_text") or "").strip())
    has_image = bool(record.get("has_image"))
    has_reply = bool(record.get("has_reply"))
    has_ocr = bool(str(record.get("ocr_text") or "").strip())
    has_link = bool(record.get("has_external_link") or record.get("external_links"))
    has_redirect = bool([value for value in record.get("visible_platform_redirects", []) if value != "none"])

    if has_image and has_ocr and record.get("screenshot_style") in {"screenshot_style", "screenshot_heavy"}:
        return "screenshot_ocr"
    if has_text and has_image:
        return "text_image_post"
    if has_reply:
        return "reply_context"
    if has_link or has_redirect:
        return "link_or_redirect"
    if has_text:
        return "text_only"
    return "low_context"
