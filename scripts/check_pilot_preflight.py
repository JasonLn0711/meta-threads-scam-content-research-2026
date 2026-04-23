#!/usr/bin/env python3
"""Run repo-safe preflight checks before the Threads pilot starts.

This script does not collect data and does not inspect controlled launch
records stored outside git. It checks only local repo mechanics: required
artifacts, JSON/CSV structure, git-ignore protection, tracked-file hygiene,
and optional local workspace readiness.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
import subprocess
from typing import Iterable

from thread_dataset_utils import load_json


REQUIRED_PACKAGE_FILES = (
    "README.md",
    ".gitignore",
    "data-contracts/thread_item_schema_v1.json",
    "data-contracts/labeling_schema_v1.json",
    "docs/06-annotation-guideline-v1.md",
    "docs/07-dataset-schema.md",
    "docs/08-baseline-strategy.md",
    "docs/20-first-dataset-batch-plan.md",
    "docs/23-collection-and-redaction-sop.md",
    "docs/29-authorized-pilot-execution-plan.md",
    "docs/31-annotation-quality-control-plan.md",
    "docs/35-real-pilot-readiness-review.md",
    "docs/37-approved-pilot-launch-plan.md",
    "docs/38-first-pilot-checkpoint-protocol.md",
    "docs/39-local-pilot-workspace.md",
    "docs/40-pilot-preflight-verification.md",
    "governance/data-governance.md",
    "governance/pilot-authorization-register.md",
    "governance/source-intake-register.md",
    "governance/pilot-launch/threads_pilot_v1_2026-05_source_intake.md",
    "governance/pilot-launch/threads_pilot_v1_2026-05_sampling_frame.csv",
    "governance/pilot-launch/threads_pilot_v1_2026-05_authorization_decision.md",
    "governance/pilot-launch/threads_pilot_v1_2026-05_data_authorization.md",
    "governance/pilot-launch/threads_pilot_v1_2026-05_go_no_go.md",
    "governance/pilot-launch/threads_pilot_v1_2026-05_work_order.md",
    "governance/pilot-launch/threads_pilot_v1_2026-05_readiness_review.md",
    "templates/annotation_sheet_template.csv",
    "templates/collection_log_template.csv",
    "templates/controlled_launch_details_template.md",
    "templates/pilot_checkpoint_review.md",
    "templates/real_pilot_readiness_review.md",
    "templates/redaction_checklist.md",
    "scripts/init_pilot_workspace.py",
    "scripts/check_pilot_preflight.py",
    "scripts/validate_thread_dataset.py",
    "scripts/audit_thread_dataset.py",
    "scripts/convert_thread_dataset.py",
    "scripts/compare_rule_variants.py",
)

JSON_FILES = (
    "data-contracts/thread_item_schema_v1.json",
    "data-contracts/labeling_schema_v1.json",
    "templates/thread_item_sample.json",
    "templates/thread_item_sample_batch.json",
)

LOCAL_WORKSPACE_FILES = (
    "data/interim/threads_pilot_v1_collection_log.csv",
    "data/interim/threads_pilot_v1_annotations.csv",
    "data/interim/threads_pilot_v1_annotation_pass_ann_01.csv",
    "data/interim/threads_pilot_v1_annotation_pass_ann_02.csv",
    "data/interim/threads_pilot_v1_checkpoint_review.md",
    "data/interim/threads_pilot_v1_workspace_manifest.md",
)

REQUIRED_GITIGNORE_PATTERNS = (
    "data/raw/*",
    "data/interim/*",
    "data/processed/*",
    "data/private/",
    "data/sensitive/",
    "data/screenshots/",
    "data/browser-exports/",
    "data/browser-profiles/",
    "evidence/raw/",
    "evidence/private/",
    "!data/raw/README.md",
    "!data/interim/README.md",
    "!data/processed/README.md",
)

REQUIRED_COLLECTION_COLUMNS = (
    "collection_batch_id",
    "item_id",
    "candidate_bucket",
    "collector_id",
    "collection_timestamp",
    "source_type",
    "collection_method",
    "authorization_status",
    "screenshot_snapshot_status",
    "link_snapshot_status",
    "raw_storage_location",
    "redaction_required",
    "redaction_completed",
    "ready_for_annotation",
    "exclusion_reason",
)

FORBIDDEN_TRACKED_PREFIXES = (
    "data/raw/",
    "data/interim/",
    "data/processed/",
    "data/private/",
    "data/sensitive/",
    "data/screenshots/",
    "data/browser-exports/",
    "data/browser-profiles/",
    "evidence/raw/",
    "evidence/private/",
)

ALLOWED_TRACKED_DATA_READMES = {
    "data/raw/README.md",
    "data/interim/README.md",
    "data/processed/README.md",
}

RISKY_TRACKED_SUFFIXES = (
    ".har",
    ".sqlite",
    ".sqlite3",
    ".db",
    ".cookies",
    ".cookie",
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".mp4",
    ".mov",
    ".webm",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
)

LOCAL_RAW_DIRS = (
    "data/raw",
    "data/screenshots",
    "data/browser-exports",
    "data/browser-profiles",
    "evidence/raw",
    "evidence/private",
)


@dataclass(frozen=True)
class Finding:
    status: str
    area: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run repo-safe pilot preflight checks. This does not collect Threads data "
            "or inspect controlled records outside git."
        )
    )
    parser.add_argument(
        "--before-item-1",
        action="store_true",
        help="Require controlled-details acknowledgement and initialized local workspace files.",
    )
    parser.add_argument(
        "--ack-controlled-details",
        action="store_true",
        help=(
            "Acknowledge that exact source, storage, access, retention, and redaction "
            "limits are recorded in the controlled non-git location."
        ),
    )
    parser.add_argument(
        "--markdown-output",
        type=Path,
        help="Optional path for a Markdown preflight report, preferably under ignored data/processed/.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return a failing exit code when warnings are present.",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def add(findings: list[Finding], status: str, area: str, message: str) -> None:
    findings.append(Finding(status=status, area=area, message=message))


def read_csv_header(path: Path) -> list[str]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        return next(reader, [])


def run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def git_ls_files(root: Path) -> list[str]:
    result = run_git(root, ["ls-files", "-z"])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "git ls-files failed")
    return [part for part in result.stdout.split("\0") if part]


def check_required_files(root: Path, findings: list[Finding]) -> None:
    missing = [path for path in REQUIRED_PACKAGE_FILES if not (root / path).exists()]
    if missing:
        for path in missing:
            add(findings, "ERROR", "package", f"missing required artifact: {path}")
    else:
        add(findings, "OK", "package", f"all {len(REQUIRED_PACKAGE_FILES)} required repo artifacts exist")


def check_json_files(root: Path, findings: list[Finding]) -> None:
    for relative in JSON_FILES:
        path = root / relative
        try:
            load_json(path)
        except Exception as exc:  # noqa: BLE001 - report parser failure cleanly
            add(findings, "ERROR", "json", f"{relative} failed to parse: {exc}")
        else:
            add(findings, "OK", "json", f"{relative} parses")


def check_annotation_template(root: Path, findings: list[Finding]) -> None:
    schema_path = root / "data-contracts/thread_item_schema_v1.json"
    template_path = root / "templates/annotation_sheet_template.csv"
    try:
        schema = load_json(schema_path)
        schema_columns = list(schema.get("properties", {}).keys())
        required_columns = set(schema.get("required", []))
        header = read_csv_header(template_path)
    except Exception as exc:  # noqa: BLE001
        add(findings, "ERROR", "csv-schema", f"could not compare annotation template to schema: {exc}")
        return

    missing = [column for column in schema_columns if column not in header]
    extra = [column for column in header if column not in schema_columns]
    missing_required = sorted(required_columns - set(header))

    if missing_required:
        add(findings, "ERROR", "csv-schema", f"annotation template missing required schema columns: {', '.join(missing_required)}")
    if missing:
        add(findings, "ERROR", "csv-schema", f"annotation template missing schema columns: {', '.join(missing)}")
    if extra:
        add(findings, "ERROR", "csv-schema", f"annotation template has non-schema columns: {', '.join(extra)}")
    if header != schema_columns and not (missing or extra):
        add(findings, "WARN", "csv-schema", "annotation template columns match schema but order differs")
    if not (missing_required or missing or extra):
        add(findings, "OK", "csv-schema", f"annotation template covers all {len(schema_columns)} schema fields")


def check_collection_template(root: Path, findings: list[Finding]) -> None:
    template_path = root / "templates/collection_log_template.csv"
    try:
        header = read_csv_header(template_path)
    except Exception as exc:  # noqa: BLE001
        add(findings, "ERROR", "collection-template", f"could not read collection log template: {exc}")
        return

    missing = [column for column in REQUIRED_COLLECTION_COLUMNS if column not in header]
    if missing:
        add(findings, "ERROR", "collection-template", f"collection log template missing required columns: {', '.join(missing)}")
    else:
        add(findings, "OK", "collection-template", f"collection log template includes {len(REQUIRED_COLLECTION_COLUMNS)} required operational columns")


def check_gitignore(root: Path, findings: list[Finding]) -> None:
    gitignore_path = root / ".gitignore"
    try:
        lines = set(gitignore_path.read_text(encoding="utf-8").splitlines())
    except FileNotFoundError:
        add(findings, "ERROR", "gitignore", ".gitignore is missing")
        return

    missing_patterns = [pattern for pattern in REQUIRED_GITIGNORE_PATTERNS if pattern not in lines]
    if missing_patterns:
        add(findings, "ERROR", "gitignore", f"missing protective patterns: {', '.join(missing_patterns)}")
    else:
        add(findings, "OK", "gitignore", "protective data/evidence ignore patterns are present")

    for probe in ("data/raw/probe.csv", "data/interim/probe.csv", "data/processed/probe.csv"):
        result = run_git(root, ["check-ignore", "--quiet", probe])
        if result.returncode == 0:
            add(findings, "OK", "gitignore", f"{probe} is ignored")
        else:
            add(findings, "ERROR", "gitignore", f"{probe} is not ignored by git")


def check_tracked_file_hygiene(root: Path, findings: list[Finding]) -> None:
    try:
        tracked = git_ls_files(root)
    except RuntimeError as exc:
        add(findings, "WARN", "git", f"could not inspect tracked files: {exc}")
        return

    forbidden = []
    for path in tracked:
        if path in ALLOWED_TRACKED_DATA_READMES:
            continue
        if any(path.startswith(prefix) for prefix in FORBIDDEN_TRACKED_PREFIXES):
            forbidden.append(path)

    if forbidden:
        for path in forbidden:
            add(findings, "ERROR", "tracked-files", f"tracked file appears in a local/raw evidence area: {path}")
    else:
        add(findings, "OK", "tracked-files", "no tracked files found in raw/interim/processed/private evidence areas")

    risky = [
        path
        for path in tracked
        if Path(path).suffix.lower() in RISKY_TRACKED_SUFFIXES and not path.startswith("data/samples/")
    ]
    if risky:
        add(findings, "WARN", "tracked-files", f"{len(risky)} tracked file(s) have media/archive/browser-data-like extensions; review manually")
    else:
        add(findings, "OK", "tracked-files", "no tracked media/archive/browser-data-like files detected outside samples")


def count_local_files(path: Path) -> int:
    if not path.exists():
        return 0
    if path.is_file():
        return 1
    count = 0
    for child in path.rglob("*"):
        if child.is_file() and child.name != "README.md":
            count += 1
    return count


def check_local_raw_dirs(root: Path, findings: list[Finding], before_item_1: bool) -> None:
    for relative in LOCAL_RAW_DIRS:
        count = count_local_files(root / relative)
        if count:
            status = "ERROR" if before_item_1 else "WARN"
            add(
                findings,
                status,
                "local-raw",
                f"{relative} contains {count} local non-README file(s); raw evidence should remain outside git-controlled folders",
            )
    if not any(count_local_files(root / relative) for relative in LOCAL_RAW_DIRS):
        add(findings, "OK", "local-raw", "no local non-README files found in repo raw/screenshot/browser/evidence folders")


def check_local_workspace(root: Path, findings: list[Finding], required: bool) -> None:
    missing = [relative for relative in LOCAL_WORKSPACE_FILES if not (root / relative).exists()]
    if missing:
        status = "ERROR" if required else "WARN"
        add(
            findings,
            status,
            "local-workspace",
            f"local workspace files missing: {', '.join(missing)}",
        )
        if required:
            add(findings, "ERROR", "local-workspace", "run scripts/init_pilot_workspace.py after controlled details are complete")
        return

    add(findings, "OK", "local-workspace", "all expected local workspace files exist")

    template_pairs = (
        ("templates/collection_log_template.csv", "data/interim/threads_pilot_v1_collection_log.csv"),
        ("templates/annotation_sheet_template.csv", "data/interim/threads_pilot_v1_annotations.csv"),
        ("templates/annotation_sheet_template.csv", "data/interim/threads_pilot_v1_annotation_pass_ann_01.csv"),
        ("templates/annotation_sheet_template.csv", "data/interim/threads_pilot_v1_annotation_pass_ann_02.csv"),
    )
    for template, local_file in template_pairs:
        try:
            template_header = read_csv_header(root / template)
            local_header = read_csv_header(root / local_file)
        except Exception as exc:  # noqa: BLE001
            add(findings, "ERROR", "local-workspace", f"could not compare {local_file} header: {exc}")
            continue
        if template_header != local_header:
            add(findings, "ERROR", "local-workspace", f"{local_file} header differs from {template}")
        else:
            add(findings, "OK", "local-workspace", f"{local_file} header matches template")


def check_worktree(root: Path, findings: list[Finding]) -> None:
    result = run_git(root, ["status", "--short", "--untracked-files=all"])
    if result.returncode != 0:
        add(findings, "WARN", "git", f"could not inspect git status: {result.stderr.strip()}")
        return
    if result.stdout.strip():
        add(findings, "WARN", "git", "worktree has uncommitted or untracked changes")
    else:
        add(findings, "OK", "git", "worktree is clean")


def check_controlled_ack(findings: list[Finding], before_item_1: bool, acknowledged: bool) -> None:
    if acknowledged:
        add(findings, "OK", "controlled-details", "operator acknowledged controlled launch details are complete outside git")
        return
    message = (
        "controlled launch details cannot be verified from this repo; exact source, storage, "
        "access, retention, and redaction limits must be complete outside git"
    )
    if before_item_1:
        add(findings, "ERROR", "controlled-details", f"{message}; rerun with --ack-controlled-details after confirmation")
    else:
        add(findings, "WARN", "controlled-details", message)


def summarize(findings: Iterable[Finding]) -> dict[str, int]:
    counts = {"OK": 0, "WARN": 0, "ERROR": 0}
    for finding in findings:
        counts[finding.status] = counts.get(finding.status, 0) + 1
    return counts


def render_text(findings: list[Finding]) -> str:
    counts = summarize(findings)
    lines = [
        "Threads pilot preflight check",
        "",
        f"OK: {counts['OK']}  WARN: {counts['WARN']}  ERROR: {counts['ERROR']}",
        "",
    ]
    for finding in findings:
        lines.append(f"[{finding.status}] {finding.area}: {finding.message}")
    return "\n".join(lines)


def render_markdown(findings: list[Finding]) -> str:
    counts = summarize(findings)
    rows = "\n".join(
        f"| `{finding.status}` | {finding.area} | {finding.message.replace('|', '/')} |"
        for finding in findings
    )
    return f"""# Threads Pilot Preflight Report

## Summary

| Status | Count |
|---|---:|
| OK | {counts['OK']} |
| WARN | {counts['WARN']} |
| ERROR | {counts['ERROR']} |

## Findings

| Status | Area | Finding |
|---|---|---|
{rows}

## Interpretation

- `ERROR` findings must be fixed before pilot collection starts.
- `WARN` findings require owner review and should be explained before item 1.
- This report does not contain raw Threads evidence and does not verify controlled details stored outside git.
"""


def write_markdown_report(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()
    root = repo_root()
    findings: list[Finding] = []

    check_required_files(root, findings)
    check_json_files(root, findings)
    check_annotation_template(root, findings)
    check_collection_template(root, findings)
    check_gitignore(root, findings)
    check_tracked_file_hygiene(root, findings)
    check_local_raw_dirs(root, findings, before_item_1=args.before_item_1)
    check_local_workspace(root, findings, required=args.before_item_1)
    check_controlled_ack(findings, before_item_1=args.before_item_1, acknowledged=args.ack_controlled_details)
    check_worktree(root, findings)

    print(render_text(findings))

    if args.markdown_output:
        output_path = args.markdown_output
        if not output_path.is_absolute():
            output_path = root / output_path
        write_markdown_report(output_path, render_markdown(findings))
        print("")
        print(f"Wrote Markdown report: {output_path}")

    counts = summarize(findings)
    if counts["ERROR"]:
        return 1
    if args.strict and counts["WARN"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
