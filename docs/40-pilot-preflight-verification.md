# Pilot Preflight Verification

## Purpose

Use this preflight before item 1 of the real Threads pilot.

The preflight is a mechanical safety check. It does not approve sources, inspect raw evidence, collect Threads data, or verify the controlled launch record stored outside git. It checks whether the repo and local workspace are structurally ready for the approved pilot workflow.

## What It Checks

`scripts/check_pilot_preflight.py` checks:

- required schema, annotation, governance, launch, and script artifacts exist
- JSON contracts and sample files parse
- `templates/annotation_sheet_template.csv` matches `thread_item_schema_v1`
- `templates/collection_log_template.csv` has required collection/redaction columns
- `.gitignore` protects raw, interim, processed, private, screenshot, browser-export, and evidence folders
- no tracked files appear in raw/interim/processed/private evidence areas
- no local raw files are sitting in repo-controlled raw/screenshot/browser/evidence folders
- optional local workspace files exist and match template headers
- the operator acknowledged controlled launch details when running the item-1 check
- git worktree status is visible before launch

It deliberately does not check the contents of controlled records outside git. That remains a human governance requirement.

## Repo-Only Check

Run this anytime:

```bash
python scripts/check_pilot_preflight.py
```

This check may warn that controlled launch details have not been acknowledged and local workspace files are missing. That is acceptable before the pilot workspace is initialized.

## Before Item 1 Check

After the controlled launch record is complete outside git and the local workspace has been initialized:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

Use this before recording the first real item in `data/interim/threads_pilot_v1_collection_log.csv`.

## Optional Markdown Report

To save a local-only preflight report:

```bash
python scripts/check_pilot_preflight.py \
  --before-item-1 \
  --ack-controlled-details \
  --markdown-output data/processed/threads_pilot_v1_preflight.md
```

`data/processed/` is ignored by git. Do not commit the generated report if it includes local state that could reveal sensitive operational details.

## Interpreting Results

| Status | Meaning | Action |
|---|---|---|
| `OK` | Check passed. | Continue. |
| `WARN` | Review needed, but the script is not blocking by default. | Explain or fix before item 1. |
| `ERROR` | Blocking issue. | Fix before pilot collection starts. |

Use `--strict` if warnings should cause a failing exit code:

```bash
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details --strict
```

## Important Limits

The preflight cannot prove:

- the exact controlled source is lawful or permitted
- the raw storage path is correct
- the access list is complete
- the retention rule is enforceable
- screenshots or OCR text are already redacted
- annotators have actually read the guideline

Those remain project-owner and governance-reviewer responsibilities.

## When To Pause

Pause before item 1 if the preflight reports:

- any `ERROR`
- local raw files in repo-controlled raw/screenshot/browser/evidence folders
- tracked files under `data/raw/`, `data/interim/`, `data/processed/`, or private evidence areas
- missing local workspace files during the `--before-item-1` run
- annotation template/schema mismatch
- missing `.gitignore` protections
- no controlled-details acknowledgement during the `--before-item-1` run

After fixing the issue, rerun the preflight and keep only non-sensitive aggregate notes in git.
