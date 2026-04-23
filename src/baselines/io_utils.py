"""Input/output helpers for local baseline runs."""

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


def load_records(path: str | Path) -> list[dict[str, Any]]:
    input_path = Path(path)
    suffix = input_path.suffix.lower()
    if suffix == ".csv":
        return load_csv_records(input_path)
    if suffix == ".json":
        data = json.loads(input_path.read_text(encoding="utf-8"))
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return [data]
        raise ValueError(f"{input_path} must contain a JSON object or array")
    if suffix == ".jsonl":
        return load_jsonl_records(input_path)
    raise ValueError(f"Unsupported input format for {input_path}; use .csv, .json, or .jsonl")


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


def write_json(path: str | Path, data: Any) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_summary(path: str | Path, lines: list[str]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
