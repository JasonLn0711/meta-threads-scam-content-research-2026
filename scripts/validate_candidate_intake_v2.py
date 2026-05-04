#!/usr/bin/env python3
"""Validate a metadata-only candidate intake worksheet."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from engine.common import load_yaml
from engine.exploration.intake import validate_candidate_intake


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Candidate intake YAML")
    parser.add_argument("--expected-count", type=int, default=None)
    args = parser.parse_args()

    intake = load_yaml(args.path)
    if not isinstance(intake, dict):
        print(f"error: {args.path} must contain a YAML object")
        return 1
    errors = validate_candidate_intake(intake, expected_count=args.expected_count)
    print(f"checked_intake_entries: {len(intake.get('intake_entries', []))}")
    print(f"errors: {len(errors)}")
    for error in errors:
        print(f"- {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
