#!/usr/bin/env python3
"""Record a repo-level version bump in VERSION, CHANGELOG.md, and CSV."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
import re
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
VERSION_PATH = ROOT / "VERSION"
CHANGELOG_PATH = ROOT / "CHANGELOG.md"
CSV_PATH = ROOT / "versioning" / "version_log.csv"
VERSION_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
CSV_COLUMNS = [
    "timestamp_utc",
    "previous_version",
    "new_version",
    "bump_type",
    "categories",
    "summary",
    "details",
    "affected_paths",
    "decision_refs",
    "verification",
    "sources",
    "sensitive_data_check",
]
DEFAULT_SENSITIVE_CHECK = (
    "No raw Threads evidence, credentials, tokens, screenshots, source URLs, "
    "account handles, browser exports, or item-level controlled artifacts added."
)


@dataclass(frozen=True)
class VersionEntry:
    timestamp_utc: str
    previous_version: str
    new_version: str
    bump_type: str
    categories: list[str]
    summary: str
    details: list[str]
    affected_paths: list[str]
    decision_refs: list[str]
    verification: list[str]
    sources: list[str]
    sensitive_data_check: str


def parse_version(value: str) -> tuple[int, int, int]:
    match = VERSION_RE.match(value.strip())
    if not match:
        raise ValueError(f"invalid version '{value}'; expected vMAJOR.MINOR.PATCH")
    return tuple(int(part) for part in match.groups())


def format_version(parts: tuple[int, int, int]) -> str:
    return f"v{parts[0]}.{parts[1]}.{parts[2]}"


def bump_version(current: str, bump: str) -> str:
    major, minor, patch = parse_version(current)
    if bump == "major":
        return format_version((major + 1, 0, 0))
    if bump == "minor":
        return format_version((major, minor + 1, 0))
    if bump == "patch":
        return format_version((major, minor, patch + 1))
    raise ValueError(f"unsupported bump type: {bump}")


def read_current_version() -> str:
    if not VERSION_PATH.exists():
        raise FileNotFoundError("VERSION is missing; create it before bumping")
    value = VERSION_PATH.read_text(encoding="utf-8").strip()
    parse_version(value)
    return value


def require_values(values: list[str], fallback: str) -> list[str]:
    cleaned = [value.strip() for value in values if value and value.strip()]
    return cleaned if cleaned else [fallback]


def join_values(values: Iterable[str]) -> str:
    return ";".join(value.strip() for value in values if value and value.strip())


def build_markdown(entry: VersionEntry) -> str:
    date = entry.timestamp_utc[:10]
    lines = [
        f"## {entry.new_version} - {date}",
        "",
        f"- Type: {entry.bump_type}",
        f"- Previous version: {entry.previous_version}",
        f"- Categories: {join_values(entry.categories)}",
        f"- Summary: {entry.summary}",
        "",
        "### Detailed Changes",
        "",
    ]
    lines.extend(f"- {detail}" for detail in entry.details)
    lines.extend(["", "### Affected Paths", ""])
    lines.extend(f"- `{path}`" for path in entry.affected_paths)

    if entry.decision_refs:
        lines.extend(["", "### Decision References", ""])
        lines.extend(f"- `{ref}`" for ref in entry.decision_refs)

    lines.extend(["", "### Verification", ""])
    lines.extend(f"- `{item}`" for item in entry.verification)

    if entry.sources:
        lines.extend(["", "### Sources", ""])
        lines.extend(f"- {source}" for source in entry.sources)

    lines.extend(["", "### Sensitive Data Check", "", f"- {entry.sensitive_data_check}", ""])
    return "\n".join(lines)


def update_changelog(entry: VersionEntry) -> None:
    new_entry = build_markdown(entry)
    if not CHANGELOG_PATH.exists():
        CHANGELOG_PATH.write_text(
            "# Changelog\n\n"
            "This file tracks repository operating versions.\n\n"
            f"{new_entry}",
            encoding="utf-8",
        )
        return

    content = CHANGELOG_PATH.read_text(encoding="utf-8")
    lines = content.splitlines()
    insert_at = None
    for index, line in enumerate(lines):
        if line.startswith("## v"):
            insert_at = index
            break

    if insert_at is None:
        updated = content.rstrip() + "\n\n" + new_entry + "\n"
    else:
        before = "\n".join(lines[:insert_at]).rstrip()
        after = "\n".join(lines[insert_at:]).lstrip()
        updated = before + "\n\n" + new_entry + "\n" + after + "\n"

    CHANGELOG_PATH.write_text(updated, encoding="utf-8")


def append_csv(entry: VersionEntry) -> None:
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    file_exists = CSV_PATH.exists()
    with CSV_PATH.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_COLUMNS)
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "timestamp_utc": entry.timestamp_utc,
                "previous_version": entry.previous_version,
                "new_version": entry.new_version,
                "bump_type": entry.bump_type,
                "categories": join_values(entry.categories),
                "summary": entry.summary,
                "details": join_values(entry.details),
                "affected_paths": join_values(entry.affected_paths),
                "decision_refs": join_values(entry.decision_refs),
                "verification": join_values(entry.verification),
                "sources": join_values(entry.sources),
                "sensitive_data_check": entry.sensitive_data_check,
            }
        )


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    version_group = parser.add_mutually_exclusive_group(required=True)
    version_group.add_argument("--bump", choices=("major", "minor", "patch"))
    version_group.add_argument("--set-version", help="Explicit new version, e.g. v1.2.6")
    parser.add_argument("--summary", required=True, help="Repo-safe one-line summary")
    parser.add_argument("--category", action="append", default=[], help="Change category")
    parser.add_argument("--detail", action="append", default=[], help="Detailed change note")
    parser.add_argument("--path", action="append", default=[], help="Affected repo path")
    parser.add_argument("--decision-ref", action="append", default=[], help="Decision record path")
    parser.add_argument("--verification", action="append", default=[], help="Verification command or check")
    parser.add_argument("--source", action="append", default=[], help="Repo-safe source reference")
    parser.add_argument(
        "--sensitive-data-check",
        default=DEFAULT_SENSITIVE_CHECK,
        help="Repo-safe sensitive data check statement",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print the entry without writing files")
    return parser


def main() -> int:
    args = make_parser().parse_args()
    previous_version = read_current_version()
    summary = args.summary.strip()
    if not summary:
        raise SystemExit("summary must not be blank")

    if args.set_version:
        new_version = args.set_version.strip()
        parse_version(new_version)
        bump_type = "set"
    else:
        new_version = bump_version(previous_version, args.bump)
        bump_type = args.bump

    entry = VersionEntry(
        timestamp_utc=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        previous_version=previous_version,
        new_version=new_version,
        bump_type=bump_type,
        categories=require_values(args.category, "uncategorized"),
        summary=summary,
        details=require_values(args.detail, summary),
        affected_paths=require_values(args.path, "not specified"),
        decision_refs=[value.strip() for value in args.decision_ref if value.strip()],
        verification=require_values(args.verification, "not specified"),
        sources=[value.strip() for value in args.source if value.strip()],
        sensitive_data_check=args.sensitive_data_check.strip(),
    )

    markdown = build_markdown(entry)
    if args.dry_run:
        print(markdown)
        print(f"would_write_version: {entry.new_version}")
        print(f"would_update: {VERSION_PATH.relative_to(ROOT)}")
        print(f"would_update: {CHANGELOG_PATH.relative_to(ROOT)}")
        print(f"would_update: {CSV_PATH.relative_to(ROOT)}")
        return 0

    VERSION_PATH.write_text(entry.new_version + "\n", encoding="utf-8")
    update_changelog(entry)
    append_csv(entry)
    print(f"updated_version: {entry.new_version}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
