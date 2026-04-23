#!/usr/bin/env python3
"""Prepare blind annotation calibration files from labeled v1 records."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

from thread_dataset_utils import load_records, load_schema


BLIND_FIELDS = {
    "scam_label": "",
    "scam_type": "",
    "risk_level": "",
    "signal_tags": "",
    "evidence_sufficiency": "",
    "annotation_confidence": "",
    "annotation_notes": "",
    "annotator_id": "",
    "reviewer_id": "",
    "review_status": "new",
    "adjudication_status": "not_needed",
    "disagreement_flag": "false",
    "final_label": "",
    "final_risk_level": "",
    "baseline_split": "unassigned",
}

ANSWER_KEY_FIELDS = [
    "item_id",
    "scam_label",
    "scam_type",
    "risk_level",
    "signal_tags",
    "evidence_sufficiency",
    "annotation_confidence",
    "annotation_notes",
    "missing_evidence",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Labeled source records: .csv, .json, or .jsonl")
    parser.add_argument("--blind-output", type=Path, required=True, help="Output blind annotation CSV")
    parser.add_argument("--answer-key-output", type=Path, help="Optional answer key CSV")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("data-contracts/thread_item_schema_v1.json"),
        help="JSON schema path used for output column order",
    )
    parser.add_argument(
        "--annotator-copy",
        action="append",
        default=[],
        metavar="ANN_ID:PATH",
        help="Optional annotator-specific blind copy, e.g. ann_01:data/interim/calibration_ann_01.csv",
    )
    args = parser.parse_args()

    records = load_records(args.input)
    schema = load_schema(args.schema)
    fieldnames = list(schema.get("properties", {}).keys())

    blind_records = [make_blind_record(record, fieldnames) for record in records]
    write_csv(args.blind_output, blind_records, fieldnames)
    print(f"blind_records_written: {len(blind_records)}")
    print(f"blind_output: {args.blind_output}")

    if args.answer_key_output:
        answer_records = [make_answer_key_record(record) for record in records]
        write_csv(args.answer_key_output, answer_records, ANSWER_KEY_FIELDS)
        print(f"answer_key_records_written: {len(answer_records)}")
        print(f"answer_key_output: {args.answer_key_output}")

    for spec in args.annotator_copy:
        annotator_id, output_path = parse_annotator_copy(spec)
        annotator_records = [dict(record, annotator_id=annotator_id) for record in blind_records]
        write_csv(output_path, annotator_records, fieldnames)
        print(f"annotator_copy_written: {annotator_id} -> {output_path}")

    return 0


def make_blind_record(record: dict[str, Any], fieldnames: list[str]) -> dict[str, str]:
    blind = {field: flatten_csv_value(record.get(field, "")) for field in fieldnames}
    for field, value in BLIND_FIELDS.items():
        if field in blind:
            blind[field] = value
    return blind


def make_answer_key_record(record: dict[str, Any]) -> dict[str, str]:
    return {field: flatten_csv_value(record.get(field, "")) for field in ANSWER_KEY_FIELDS}


def parse_annotator_copy(spec: str) -> tuple[str, Path]:
    if ":" not in spec:
        raise ValueError("--annotator-copy must look like ANN_ID:path")
    annotator_id, path = spec.split(":", 1)
    annotator_id = annotator_id.strip()
    if not annotator_id:
        raise ValueError("annotator ID must not be empty")
    return annotator_id, Path(path)


def write_csv(path: Path, records: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)


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
