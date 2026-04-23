#!/usr/bin/env python3
"""Compare two independent annotation passes for Threads dataset v1."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

from thread_dataset_utils import load_records


SCALAR_FIELDS = [
    "scam_label",
    "risk_level",
    "evidence_sufficiency",
    "annotation_confidence",
]

SET_FIELDS = [
    "scam_type",
    "signal_tags",
    "missing_evidence",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("annotator_a", type=Path, help="First annotation file: .csv, .json, or .jsonl")
    parser.add_argument("annotator_b", type=Path, help="Second annotation file: .csv, .json, or .jsonl")
    parser.add_argument("--name-a", default="annotator_a", help="Display name for first file")
    parser.add_argument("--name-b", default="annotator_b", help="Display name for second file")
    parser.add_argument("--output", type=Path, help="Optional Markdown report path")
    parser.add_argument("--disagreements-csv", type=Path, help="Optional disagreement CSV path")
    args = parser.parse_args()

    records_a = index_by_item_id(load_records(args.annotator_a), args.name_a)
    records_b = index_by_item_id(load_records(args.annotator_b), args.name_b)
    shared_ids = sorted(set(records_a) & set(records_b))
    only_a = sorted(set(records_a) - set(records_b))
    only_b = sorted(set(records_b) - set(records_a))

    disagreements = collect_disagreements(records_a, records_b, shared_ids)
    report = render_report(records_a, records_b, shared_ids, only_a, only_b, disagreements, args.name_a, args.name_b)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"report_written: {args.output}")
    else:
        print(report)

    if args.disagreements_csv:
        write_disagreements_csv(args.disagreements_csv, disagreements)
        print(f"disagreements_written: {args.disagreements_csv}")

    return 0


def index_by_item_id(records: list[dict[str, Any]], name: str) -> dict[str, dict[str, Any]]:
    indexed: dict[str, dict[str, Any]] = {}
    for index, record in enumerate(records, 1):
        item_id = str(record.get("item_id") or "").strip()
        if not item_id:
            raise ValueError(f"{name}: row {index} has no item_id")
        if item_id in indexed:
            raise ValueError(f"{name}: duplicate item_id {item_id}")
        indexed[item_id] = record
    return indexed


def collect_disagreements(
    records_a: dict[str, dict[str, Any]],
    records_b: dict[str, dict[str, Any]],
    shared_ids: list[str],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for item_id in shared_ids:
        record_a = records_a[item_id]
        record_b = records_b[item_id]
        for field in SCALAR_FIELDS:
            value_a = str(record_a.get(field, ""))
            value_b = str(record_b.get(field, ""))
            if value_a != value_b:
                rows.append(disagreement_row(item_id, field, value_a, value_b))
        for field in SET_FIELDS:
            values_a = normalize_set(record_a.get(field))
            values_b = normalize_set(record_b.get(field))
            if values_a != values_b:
                rows.append(
                    disagreement_row(
                        item_id,
                        field,
                        "|".join(sorted(values_a)),
                        "|".join(sorted(values_b)),
                    )
                )
    return rows


def disagreement_row(item_id: str, field: str, value_a: str, value_b: str) -> dict[str, str]:
    return {
        "item_id": item_id,
        "field": field,
        "annotator_a_value": value_a,
        "annotator_b_value": value_b,
        "disagreement_type": classify_disagreement(field),
        "resolution_status": "pending",
        "final_value": "",
        "adjudicator_id": "",
        "adjudication_date": "",
        "adjudicator_notes": "",
        "guideline_change_needed": "",
    }


def classify_disagreement(field: str) -> str:
    if field == "scam_label":
        return "primary_label"
    if field == "risk_level":
        return "risk_level"
    if field == "evidence_sufficiency":
        return "evidence_sufficiency"
    if field == "annotation_confidence":
        return "confidence"
    if field == "scam_type":
        return "scam_type"
    if field == "signal_tags":
        return "signal_tags"
    if field == "missing_evidence":
        return "missing_evidence"
    return "other"


def render_report(
    records_a: dict[str, dict[str, Any]],
    records_b: dict[str, dict[str, Any]],
    shared_ids: list[str],
    only_a: list[str],
    only_b: list[str],
    disagreements: list[dict[str, str]],
    name_a: str,
    name_b: str,
) -> str:
    lines: list[str] = []
    lines.append("# Annotation Agreement Report")
    lines.append("")
    lines.append(f"- Annotator A: `{name_a}`")
    lines.append(f"- Annotator B: `{name_b}`")
    lines.append(f"- Shared items: {len(shared_ids)}")
    lines.append(f"- Only in {name_a}: {len(only_a)}")
    lines.append(f"- Only in {name_b}: {len(only_b)}")
    lines.append(f"- Disagreement rows: {len(disagreements)}")
    lines.append("")

    lines.append("## Scalar Agreement")
    lines.append("")
    lines.append("| Field | Agreement | Cohen kappa | Matches | Compared |")
    lines.append("|---|---:|---:|---:|---:|")
    for field in SCALAR_FIELDS:
        values_a = [str(records_a[item_id].get(field, "")) for item_id in shared_ids]
        values_b = [str(records_b[item_id].get(field, "")) for item_id in shared_ids]
        matches = sum(1 for value_a, value_b in zip(values_a, values_b) if value_a == value_b)
        compared = len(shared_ids)
        agreement = matches / compared if compared else 0.0
        kappa = cohen_kappa(values_a, values_b)
        lines.append(f"| `{field}` | {agreement:.3f} | {kappa:.3f} | {matches} | {compared} |")
    lines.append("")

    lines.append("## Set-Field Agreement")
    lines.append("")
    lines.append("| Field | Exact agreement | Mean Jaccard | Exact matches | Compared |")
    lines.append("|---|---:|---:|---:|---:|")
    for field in SET_FIELDS:
        exact_matches = 0
        jaccards: list[float] = []
        for item_id in shared_ids:
            set_a = normalize_set(records_a[item_id].get(field))
            set_b = normalize_set(records_b[item_id].get(field))
            if set_a == set_b:
                exact_matches += 1
            jaccards.append(jaccard(set_a, set_b))
        compared = len(shared_ids)
        exact_agreement = exact_matches / compared if compared else 0.0
        mean_jaccard = sum(jaccards) / len(jaccards) if jaccards else 0.0
        lines.append(f"| `{field}` | {exact_agreement:.3f} | {mean_jaccard:.3f} | {exact_matches} | {compared} |")
    lines.append("")

    lines.append("## Disagreement Counts")
    lines.append("")
    counts = count_by(disagreements, "disagreement_type")
    if counts:
        for key, count in counts.items():
            lines.append(f"- `{key}`: {count}")
    else:
        lines.append("- No disagreements.")
    lines.append("")

    lines.append("## Items Requiring Adjudication")
    lines.append("")
    item_counts = count_by(disagreements, "item_id")
    if item_counts:
        for item_id, count in item_counts.items():
            fields = sorted({row["field"] for row in disagreements if row["item_id"] == item_id})
            lines.append(f"- `{item_id}`: {count} disagreement(s): {', '.join(fields)}")
    else:
        lines.append("- None.")
    lines.append("")

    if only_a or only_b:
        lines.append("## File Coverage Mismatches")
        lines.append("")
        if only_a:
            lines.append(f"- Only in `{name_a}`: {', '.join(only_a)}")
        if only_b:
            lines.append(f"- Only in `{name_b}`: {', '.join(only_b)}")
        lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append("- Prioritize adjudication of `scam_label`, `risk_level`, and `evidence_sufficiency` disagreements.")
    lines.append("- Low subtype or signal-tag overlap usually means the guideline needs examples or tag merging.")
    lines.append("- Kappa is unstable on tiny calibration sets; use it as a warning light, not as a final quality score.")
    lines.append("- Do not expand to the full pilot if primary-label disagreement clusters around the same edge case.")
    lines.append("")
    return "\n".join(lines)


def normalize_set(value: Any) -> set[str]:
    if value is None or value == "":
        return set()
    if isinstance(value, str):
        values = value.split("|")
    elif isinstance(value, list):
        values = value
    else:
        values = [str(value)]
    cleaned = {str(item).strip() for item in values if str(item).strip()}
    if cleaned == {"none"}:
        return set()
    return cleaned


def jaccard(set_a: set[str], set_b: set[str]) -> float:
    if not set_a and not set_b:
        return 1.0
    union = set_a | set_b
    if not union:
        return 1.0
    return len(set_a & set_b) / len(union)


def cohen_kappa(values_a: list[str], values_b: list[str]) -> float:
    if not values_a or not values_b or len(values_a) != len(values_b):
        return 0.0
    total = len(values_a)
    observed = sum(1 for value_a, value_b in zip(values_a, values_b) if value_a == value_b) / total
    labels = set(values_a) | set(values_b)
    expected = 0.0
    for label in labels:
        p_a = sum(1 for value in values_a if value == label) / total
        p_b = sum(1 for value in values_b if value == label) / total
        expected += p_a * p_b
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return (observed - expected) / (1 - expected)


def count_by(rows: list[dict[str, str]], field: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for row in rows:
        value = row[field]
        counts[value] = counts.get(value, 0) + 1
    return dict(sorted(counts.items(), key=lambda pair: (-pair[1], pair[0])))


def write_disagreements_csv(path: Path, disagreements: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "item_id",
        "field",
        "annotator_a_value",
        "annotator_b_value",
        "disagreement_type",
        "resolution_status",
        "final_value",
        "adjudicator_id",
        "adjudication_date",
        "adjudicator_notes",
        "guideline_change_needed",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(disagreements)


if __name__ == "__main__":
    raise SystemExit(main())
