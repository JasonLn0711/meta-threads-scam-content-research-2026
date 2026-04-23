#!/usr/bin/env python3
"""Build one schema-valid Threads item from manually supplied local fields.

This script does not collect data from Threads, fetch URLs, crawl pages, or run
browser automation. It only structures a local JSON payload supplied by the
collector.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from src.data_collection.collection_log import append_collection_log, write_action_log
from src.data_collection.collector import build_manual_collection_record, load_manual_collection_config
from thread_dataset_utils import load_schema, validate_records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path, help="Local manually prepared JSON payload")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/manual_collection_assistant.yaml"),
        help="Manual collection assistant config",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("data-contracts/thread_item_schema_v1.json"),
        help="Thread item schema path",
    )
    parser.add_argument("--output", type=Path, help="Write the generated record as JSON")
    parser.add_argument("--append-jsonl", type=Path, help="Append the generated record to JSONL")
    parser.add_argument("--collection-log", type=Path, help="Append a local collection log CSV row")
    parser.add_argument(
        "--ack-controlled-details",
        action="store_true",
        help="Acknowledge controlled launch details are complete outside git for real manual items",
    )
    parser.add_argument(
        "--allow-governance-warnings",
        action="store_true",
        help="Continue when governance warnings are present. Errors still fail.",
    )
    parser.add_argument("--print-record", action="store_true", help="Print generated record JSON to stdout")
    args = parser.parse_args()

    payload = load_payload(args.input_json)
    config = load_manual_collection_config(args.config)
    action_log_config = config.get("action_log", {})
    action_log_path = action_log_config.get("path")
    include_target_url = bool(action_log_config.get("include_target_url", False))
    item_id = str(payload.get("item_id") or "")

    try:
        record, governance, log_row = build_manual_collection_record(
            payload,
            config,
            ack_controlled_details=args.ack_controlled_details,
        )
        schema_errors, schema_warnings = validate_records([record], load_schema(args.schema))
    except Exception as exc:  # pragma: no cover - CLI safety wrapper
        maybe_log_action(
            action_log_path,
            config,
            success=False,
            item_id=item_id,
            target_url=str(payload.get("source_url_if_stored") or ""),
            message=str(exc),
            include_target_url=include_target_url,
        )
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    for warning in governance.warnings:
        print(f"GOVERNANCE WARNING: {warning}", file=sys.stderr)
    for error in governance.errors:
        print(f"GOVERNANCE ERROR: {error}", file=sys.stderr)
    for warning in schema_warnings:
        print(f"SCHEMA WARNING: {warning}", file=sys.stderr)
    for error in schema_errors:
        print(f"SCHEMA ERROR: {error}", file=sys.stderr)

    if governance.errors or schema_errors:
        maybe_log_action(
            action_log_path,
            config,
            success=False,
            item_id=record.get("item_id", item_id),
            target_url=str(payload.get("source_url_if_stored") or ""),
            message="governance or schema errors",
            include_target_url=include_target_url,
        )
        return 2
    if governance.warnings and not args.allow_governance_warnings:
        maybe_log_action(
            action_log_path,
            config,
            success=False,
            item_id=record.get("item_id", item_id),
            target_url=str(payload.get("source_url_if_stored") or ""),
            message="governance warnings require --allow-governance-warnings",
            include_target_url=include_target_url,
        )
        print("ERROR: governance warnings present; rerun with --allow-governance-warnings after review", file=sys.stderr)
        return 3

    if args.output:
        write_json(args.output, record)
    if args.append_jsonl:
        append_jsonl(args.append_jsonl, record)
    if args.collection_log:
        append_collection_log(args.collection_log, log_row)
    if args.print_record:
        print(json.dumps(record, indent=2, sort_keys=True))

    maybe_log_action(
        action_log_path,
        config,
        success=True,
        item_id=record.get("item_id", item_id),
        target_url=str(payload.get("source_url_if_stored") or ""),
        message="manual record built",
        include_target_url=include_target_url,
    )

    print(f"item_id: {record['item_id']}")
    print("governance_errors: 0")
    print(f"governance_warnings: {len(governance.warnings)}")
    print("schema_errors: 0")
    print(f"schema_warnings: {len(schema_warnings)}")
    if args.output:
        print(f"output: {args.output}")
    if args.append_jsonl:
        print(f"jsonl: {args.append_jsonl}")
    if args.collection_log:
        print(f"collection_log: {args.collection_log}")
    return 0


def load_payload(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain one JSON object")
    return data


def write_json(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")


def maybe_log_action(
    action_log_path: str | None,
    config: dict[str, Any],
    *,
    success: bool,
    item_id: str,
    target_url: str,
    message: str,
    include_target_url: bool,
) -> None:
    if not config.get("action_log", {}).get("enabled", True) or not action_log_path:
        return
    write_action_log(
        action_log_path,
        mode=str(config.get("collection_mode", "manual_only")),
        action_type="build_manual_record",
        success=success,
        item_id=item_id,
        target_url=target_url,
        message=message,
        include_target_url=include_target_url,
    )


if __name__ == "__main__":
    raise SystemExit(main())
