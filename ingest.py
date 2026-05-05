#!/usr/bin/env python3
"""CLI wrapper for Evidence Layer v1 ingestion."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.evidence.ingestion import ingest_evidence


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--input", help="Synthetic or controlled text input to ingest.")
    input_group.add_argument("--input-file", type=Path, help="Local file to ingest.")
    parser.add_argument("--source", required=True, help="Non-sensitive source label, for example: threads.")
    parser.add_argument("--actor", default="local_cli", help="Audit actor label.")
    parser.add_argument("--binary", action="store_true", help="Read --input-file as binary bytes.")
    args = parser.parse_args()

    if args.input_file:
        raw_input = args.input_file.read_bytes() if args.binary else args.input_file.read_text(encoding="utf-8")
    else:
        raw_input = args.input

    result = ingest_evidence(raw_input, {"source": args.source, "input_mode": "cli"}, actor=args.actor)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
