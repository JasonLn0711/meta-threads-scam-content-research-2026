# Dataset Audit 0003: First Pilot Checkpoint

## Purpose

Audit the first 10-15 real pilot items before the team finishes the full 50-item batch.

This is not a baseline experiment. It is an early safety and usefulness check.

## Scope

Use this protocol only after:

- controlled launch details are complete outside git
- first 10-15 candidate items are collected or annotated
- raw evidence remains outside git
- collection uses only approved manual or stakeholder-provided paths

Do not commit local annotation files, raw evidence, screenshots, URLs, handles, or generated outputs unless they are explicitly approved and fully non-sensitive.

## Inputs

Local-only:

- `data/interim/threads_pilot_v1_collection_log.csv`
- `data/interim/threads_pilot_v1_annotations.csv`, if first-pass labels exist

Repo-safe:

- `governance/pilot-launch/threads_pilot_v1_2026-05_sampling_frame.csv`
- `docs/38-first-pilot-checkpoint-protocol.md`
- `templates/pilot_checkpoint_review.md`

## Commands

Run validation only if the annotation CSV has schema fields:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  > data/processed/threads_pilot_v1_checkpoint_audit.md
```

If only the collection log exists, perform a manual checkpoint review with `templates/pilot_checkpoint_review.md`.

## Required Checks

### Collection Safety

- raw evidence stayed outside git
- controlled source limits were followed
- no automation, crawling, bulk export, redirect expansion, landing-page capture, or profile review occurred
- screenshots and source URLs follow the controlled redaction limits
- contact handles are redacted or categorized
- OCR text was privacy-reviewed before entering annotation fields

### Composition

- first 10-15 items include at least two label-intent buckets
- comparator items are not postponed until the end
- uncertain and insufficient-evidence items are present but not dominating
- content forms include more than one surface where feasible

### Annotation Quality

If labels exist:

- no blank primary labels
- no blank evidence sufficiency values
- no blank annotation confidence values
- `uncertain` and `insufficient_evidence` are not interchangeable
- high-risk, uncertain, low-confidence, and partial-evidence items route to second review
- notes avoid legal conclusions and raw identifiers

## Escalation Conditions

Pause before continuing to 50 items if:

- any raw evidence entered git
- any unapproved source or method was used
- any item requires unapproved profile/account/landing-page context
- more than 30 percent of checkpoint items are not ready for annotation because evidence is missing or unsafe
- `uncertain` is above 40 percent and caused by unclear guidance
- `insufficient_evidence` is above 30 percent and caused by collection quality
- redaction cannot be applied consistently

## Output

Create a non-sensitive checkpoint summary using `templates/pilot_checkpoint_review.md`.

Do not run `scripts/summarize_pilot_results.py` to make an expansion decision at this stage. For fewer than 50 non-synthetic items, synthesis should return `first_checkpoint_review_required`.

Decision values:

- `continue_to_50`
- `continue_with_limits`
- `pause_for_redaction_fix`
- `pause_for_collection_fix`
- `pause_for_guideline_fix`
- `pause_for_authorization_review`
- `stop_pilot`

If the decision is a pause or stop, update the relevant launch, governance, annotation, or source document before continuing.
