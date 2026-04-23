# Local Pilot Workspace

## Purpose

This document explains how to create the local working files for the first real Threads pilot after approval.

It is a preparation step only. It does not authorize collection, automate collection, or change the approved limits.

The local workspace exists so the collector, annotators, reviewer, adjudicator, and research engineer can work from the same schema without committing raw or sensitive evidence to git.

## Preconditions

Do not initialize or fill the local workspace until all of these are true:

- the controlled launch record is completed outside git
- exact source limits are recorded in the controlled location
- exact raw storage location is recorded outside git
- exact access list is recorded outside git
- exact retention or deletion rule is recorded outside git
- exact redaction limits are recorded outside git
- assigned collector, annotator, reviewer, adjudicator, and research engineer IDs exist
- everyone understands that raw evidence stays outside git

The non-sensitive launch plan is [37-approved-pilot-launch-plan.md](37-approved-pilot-launch-plan.md). The first checkpoint protocol is [38-first-pilot-checkpoint-protocol.md](38-first-pilot-checkpoint-protocol.md).

## Files Created

The initializer creates these empty working files under ignored `data/interim/`:

```text
data/interim/threads_pilot_v1_collection_log.csv
data/interim/threads_pilot_v1_annotations.csv
data/interim/threads_pilot_v1_annotation_pass_ann_01.csv
data/interim/threads_pilot_v1_annotation_pass_ann_02.csv
data/interim/threads_pilot_v1_checkpoint_review.md
data/interim/threads_pilot_v1_workspace_manifest.md
```

These are local-only files. After collection begins, they may contain sensitive or source-specific information. Do not commit them unless a later explicit decision says a specific file is fully redacted, approved, and safe to track.

## Dry Run

Preview the files without writing:

```bash
python scripts/init_pilot_workspace.py --dry-run
```

Use this before the controlled launch details are complete, during runbook rehearsal, or when checking a new machine.

## Initialize

After the controlled launch record is complete outside git:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

To use a different dataset or batch ID:

```bash
python scripts/init_pilot_workspace.py \
  --dataset-id threads_pilot_v1_2026-05 \
  --batch-id threads_pilot_v1_2026-05 \
  --ack-controlled-details
```

The script refuses to overwrite existing local files unless `--force` is supplied. Use `--force` only after confirming the existing local files contain no needed work.

## First Working Order

After initialization:

1. Fill only approved collection fields in `data/interim/threads_pilot_v1_collection_log.csv`.
2. Start `data/interim/threads_pilot_v1_annotations.csv` with schema-compliant item rows.
3. Keep raw screenshots, source packets, case exports, browser data, credentials, and unredacted identifiers outside git.
4. Fill `privacy_redaction_notes`, `screenshot_snapshot_status`, and `link_snapshot_status` whenever relevant.
5. Pause after the first 10-15 collected or annotated items.
6. Complete `data/interim/threads_pilot_v1_checkpoint_review.md` without raw Threads content.

## Local Checks

Before item 1:

```bash
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

Once annotation rows exist:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
```

For a checkpoint audit:

```bash
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  > data/processed/threads_pilot_v1_checkpoint_audit.md
```

After the full 50-item pilot has passed review and adjudication:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
python scripts/convert_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  data/processed/threads_pilot_v1.jsonl \
  --validate
python scripts/compare_rule_variants.py data/processed/threads_pilot_v1.jsonl \
  --output data/processed/threads_pilot_v1_rule_variant_comparison.md
```

All of these generated outputs are ignored by git by default.

## Do Not Commit

Do not commit:

- raw screenshots or media
- source URLs unless explicitly approved and safely normalized
- unredacted handles, phone numbers, payment details, emails, or referral codes
- stakeholder case packets
- browser exports, profiles, cookies, tokens, credentials, or HAR files
- local annotation CSVs after real evidence has been entered
- generated JSONL, audit, agreement, or baseline outputs that contain item-level real evidence

Commit only aggregate, non-sensitive findings, decision records, guide revisions, and schema changes.

## Failure Modes

Pause the pilot if any of these occur:

- the controlled launch record is incomplete or unclear
- local files contain fields not approved by the controlled record
- raw evidence appears in tracked git files
- the collector needs profile, account, landing-page, or redirect-chain context that was not approved
- screenshots, OCR, links, or handles cannot be redacted consistently
- more than 30 percent of checkpoint items are not ready for annotation because evidence is missing or unsafe

In a pause, update the controlled launch record or the relevant repo-safe runbook before collecting more items.
