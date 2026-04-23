#!/usr/bin/env python3
"""Convert Threads dataset v1 records between CSV, JSON, and JSONL."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any

from thread_dataset_utils import load_records, load_schema, validate_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Input dataset: .csv, .json, or .jsonl")
    parser.add_argument("output", type=Path, help="Output dataset path")
    parser.add_argument(
        "--format",
        choices=["csv", "json", "jsonl"],
        help="Output format. Defaults to output file extension.",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("data-contracts/thread_item_schema_v1.json"),
        help="JSON schema path used for field order and optional validation",
    )
    parser.add_argument("--validate", action="store_true", help="Validate before writing output")
    args = parser.parse_args()

    records = load_records(args.input)
    schema = load_schema(args.schema)

    if args.validate:
        errors, warnings = validate_records(records, schema)
        for warning in warnings:
            print(f"WARNING: {warning}")
        for error in errors:
            print(f"ERROR: {error}")
        if errors:
            print(f"conversion_aborted: {len(errors)} validation error(s)")
            return 1

    output_format = args.format or infer_format(args.output)
    fieldnames = list(schema.get("properties", {}).keys())
    args.output.parent.mkdir(parents=True, exist_ok=True)

    if output_format == "csv":
        write_csv(args.output, records, fieldnames)
    elif output_format == "json":
        args.output.write_text(json.dumps(records, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    elif output_format == "jsonl":
        write_jsonl(args.output, records)
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

    print(f"records_written: {len(records)}")
    print(f"output: {args.output}")
    print(f"format: {output_format}")
    return 0


def infer_format(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".csv":
        return "csv"
    if suffix == ".json":
        return "json"
    if suffix == ".jsonl":
        return "jsonl"
    raise ValueError("Cannot infer output format; use --format csv|json|jsonl")


def write_csv(path: Path, records: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({field: flatten_csv_value(record.get(field, "")) for field in fieldnames})


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    lines = [json.dumps(record, ensure_ascii=False, sort_keys=False) for record in records]
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def flatten_csv_value(value: Any) -> str:
    if isinstance(value, list):
        return "|".join(str(item) for item in value)
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return ""
    return str(value)


if __name__ == "__main__":
    raise SystemExit(main())
