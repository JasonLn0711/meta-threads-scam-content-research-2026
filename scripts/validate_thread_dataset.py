#!/usr/bin/env python3
"""Validate Threads dataset v1 CSV/JSON/JSONL records."""

from __future__ import annotations

import argparse
from pathlib import Path

from thread_dataset_utils import load_records, load_schema, validate_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("data-contracts/thread_item_schema_v1.json"),
        help="JSON schema path",
    )
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    records = load_records(args.input)
    schema = load_schema(args.schema)
    errors, warnings = validate_records(records, schema)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    print(f"checked_records: {len(records)}")
    print(f"errors: {len(errors)}")
    print(f"warnings: {len(warnings)}")

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
