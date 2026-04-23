#!/usr/bin/env python3
"""Produce a lightweight Markdown audit for a Threads dataset v1 file."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Any

from thread_dataset_utils import (
    content_shape,
    load_records,
    load_schema,
    normalize_text,
    summarize_counts,
    validate_records,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Dataset file: .csv, .json, or .jsonl")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("data-contracts/thread_item_schema_v1.json"),
        help="JSON schema path",
    )
    args = parser.parse_args()

    records = load_records(args.input)
    schema = load_schema(args.schema)
    errors, warnings = validate_records(records, schema)

    print(f"# Dataset Audit: {args.input}")
    print()
    print("## Summary")
    print()
    print(f"- Items: {len(records)}")
    print(f"- Schema errors: {len(errors)}")
    print(f"- Schema warnings: {len(warnings)}")
    print()

    print_count_section("Scam Labels", summarize_counts(records, "scam_label"))
    print_count_section("Risk Levels", summarize_counts(records, "risk_level"))
    print_count_section("Evidence Sufficiency", summarize_counts(records, "evidence_sufficiency"))
    print_count_section("Annotation Confidence", summarize_counts(records, "annotation_confidence"))
    print_count_section("Source Type", summarize_counts(records, "source_type"))
    print_count_section("Collection Method", summarize_counts(records, "collection_method"))
    print_count_section("Signal Tags", summarize_counts(records, "signal_tags"))

    shape_counts: dict[str, int] = {}
    for record in records:
        shape = content_shape(record)
        shape_counts[shape] = shape_counts.get(shape, 0) + 1
    print_count_section("Content Shapes", dict(sorted(shape_counts.items(), key=lambda pair: (-pair[1], pair[0]))))

    print_required_missing_section(records, schema)
    print_empty_evidence_section(records)
    print_duplicate_section(records)
    print_warning_section(records)

    if errors:
        print("## Schema Errors")
        print()
        for error in errors[:50]:
            print(f"- {error}")
        if len(errors) > 50:
            print(f"- ... {len(errors) - 50} more")
        print()

    if warnings:
        print("## Schema Warnings")
        print()
        for warning in warnings[:50]:
            print(f"- {warning}")
        if len(warnings) > 50:
            print(f"- ... {len(warnings) - 50} more")
        print()

    return 1 if errors else 0


def print_count_section(title: str, counts: dict[str, int]) -> None:
    print(f"## {title}")
    print()
    if not counts:
        print("- No values")
        print()
        return
    for value, count in counts.items():
        print(f"- `{value}`: {count}")
    print()


def print_required_missing_section(records: list[dict[str, Any]], schema: dict[str, Any]) -> None:
    required = schema.get("required", [])
    missing_counts: dict[str, int] = {}
    for field in required:
        count = 0
        for record in records:
            if field not in record or record.get(field) is None:
                count += 1
        if count:
            missing_counts[field] = count
    print_count_section("Required Fields Missing", missing_counts)


def print_empty_evidence_section(records: list[dict[str, Any]]) -> None:
    evidence_fields = [
        "post_text",
        "reply_texts",
        "image_paths",
        "external_links",
        "visible_contact_handles",
        "ocr_text",
    ]
    empty_counts: dict[str, int] = {}
    for field in evidence_fields:
        count = 0
        for record in records:
            value = record.get(field)
            if value in (None, "", []):
                count += 1
        if count:
            empty_counts[field] = count
    print_count_section("Evidence Fields Empty", empty_counts)


def print_duplicate_section(records: list[dict[str, Any]]) -> None:
    duplicate_sources: dict[str, dict[str, list[str]]] = {
        "post_text": defaultdict(list),
        "ocr_text": defaultdict(list),
        "external_links": defaultdict(list),
        "visible_contact_handles": defaultdict(list),
    }

    for record in records:
        item_id = str(record.get("item_id") or "<missing>")
        for field in ("post_text", "ocr_text"):
            normalized = normalize_text(record.get(field))
            if normalized:
                duplicate_sources[field][normalized].append(item_id)
        for field in ("external_links", "visible_contact_handles"):
            for value in record.get(field, []) or []:
                normalized = normalize_text(value)
                if normalized:
                    duplicate_sources[field][normalized].append(item_id)

    print("## Possible Duplicates")
    print()
    found = False
    for field, groups in duplicate_sources.items():
        for value, item_ids in groups.items():
            if len(item_ids) > 1:
                found = True
                preview = value[:90] + ("..." if len(value) > 90 else "")
                print(f"- `{field}` duplicate `{preview}`: {', '.join(item_ids)}")
    if not found:
        print("- No exact duplicates found in text, OCR, links, or handles.")
    print()


def print_warning_section(records: list[dict[str, Any]]) -> None:
    total = len(records) or 1
    label_counts = summarize_counts(records, "scam_label")
    uncertain_rate = label_counts.get("uncertain", 0) / total
    insufficient_rate = label_counts.get("insufficient_evidence", 0) / total

    print("## Audit Flags")
    print()
    flags: list[str] = []
    if uncertain_rate > 0.30:
        flags.append(f"`uncertain` is {uncertain_rate:.1%}, above the 30% pilot warning threshold.")
    if insufficient_rate > 0.20:
        flags.append(
            f"`insufficient_evidence` is {insufficient_rate:.1%}, above the 20% pilot warning threshold."
        )

    for field in ("source_type", "collection_method"):
        counts = summarize_counts(records, field)
        if counts:
            top_value, top_count = next(iter(counts.items()))
            if top_count / total > 0.70:
                flags.append(f"`{field}` is skewed toward `{top_value}` ({top_count}/{total}).")

    if not flags:
        print("- No threshold flags.")
    else:
        for flag in flags:
            print(f"- {flag}")
    print()


if __name__ == "__main__":
    raise SystemExit(main())
