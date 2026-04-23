# Dataset Audit 0001: Pilot Batch Protocol

## Purpose

Run this audit before any baseline experiment on the 50-item pilot. The audit decides whether the dataset is ready for baseline comparison or needs annotation/schema cleanup first.

## Inputs

- `data/interim/threads_pilot_v1_annotations.csv` or equivalent local-only annotation file
- `data-contracts/thread_item_schema_v1.json`
- `docs/06-annotation-guideline-v1.md`

## Commands

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv > data/processed/threads_pilot_v1_audit.md
```

`data/interim/` and `data/processed/` are ignored by git. Copy only non-sensitive aggregate findings into an experiment note.

## Readiness Criteria

The pilot is ready for baseline work when:

- schema validation has zero errors
- no required field is missing because of collection confusion
- `uncertain` is not above about 30 percent
- `insufficient_evidence` is not above about 20 percent
- high-risk and uncertain items have second-review routing
- duplicate clusters are marked instead of silently removed
- source and content-form skew are understood

## Escalate Before Baseline If

- annotators disagree on the same label boundary repeatedly
- `other_high_risk_persuasion` becomes common
- external links or handles are stored too specifically for privacy comfort
- screenshot-heavy items lack OCR or screenshot status
- many items depend on context that phase 1 is not approved to collect

## Output Note

After the audit, write a short note with:

- dataset ID
- item count
- label distribution
- content-form distribution
- top missing fields
- top disagreement causes
- decision: proceed to baseline, annotate more, or revise guidance first
