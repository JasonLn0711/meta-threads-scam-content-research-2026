# Synthetic Pilot Dry-Run Results

## Purpose

This note records the first end-to-end dry run of the Threads dataset, audit, and baseline workflow using only synthetic records.

It is a tooling and workflow result. It is not an empirical result about Threads, CIB/165 reports, scam prevalence, or real-world detector performance.

## Dataset Slice

| Field | Value |
|---|---|
| Input file | `data/samples/thread_item_sample_batch.csv` |
| Records | 5 |
| Source type | `researcher_synthetic` |
| Collection method | `synthetic` |
| Evidence status | No real Threads evidence, no personal data, no live URLs, no raw screenshots |
| Purpose | Validate schema, audit logic, conversion, and baseline variants before real pilot data |

## Commands Run

```bash
python scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv --strict
python scripts/validate_thread_dataset.py templates/thread_item_sample_batch.json --strict
python scripts/convert_thread_dataset.py data/samples/thread_item_sample_batch.csv \
  data/processed/synthetic-dry-run/thread_item_sample_batch.jsonl \
  --validate
python scripts/audit_thread_dataset.py data/samples/thread_item_sample_batch.csv
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant text_only \
  --output data/processed/synthetic-dry-run/rule_baseline_text_only_predictions.csv
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant text_reply \
  --output data/processed/synthetic-dry-run/rule_baseline_text_reply_predictions.csv
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant text_ocr \
  --output data/processed/synthetic-dry-run/rule_baseline_text_ocr_predictions.csv
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant all \
  --output data/processed/synthetic-dry-run/rule_baseline_all_predictions.csv
python scripts/compare_rule_variants.py \
  data/processed/synthetic-dry-run/thread_item_sample_batch.jsonl \
  --output data/processed/synthetic-dry-run/rule_variant_comparison.md
```

Generated outputs are local-only under `data/processed/synthetic-dry-run/`, which is ignored by git.

## Validation Result

| Check | Result |
|---|---|
| CSV strict validation | 5 records checked, 0 errors, 0 warnings |
| JSON strict validation | 5 records checked, 0 errors, 0 warnings |
| CSV to JSONL conversion | 5 records written |

Interpretation: the sample batch is schema-compatible and can exercise both spreadsheet and JSONL workflows.

## Audit Result

| Category | Result |
|---|---|
| Items | 5 |
| `scam` | 3 |
| `non_scam` | 1 |
| `uncertain` | 1 |
| `insufficient_evidence` | 0 |
| `high` risk | 3 |
| `low` risk | 2 |
| `sufficient` evidence | 4 |
| `partial` evidence | 1 |
| `high` confidence | 4 |
| `low` confidence | 1 |
| Required fields missing | none |
| Possible duplicates | none found |

Audit flags:

- `source_type` is skewed toward `researcher_synthetic` because all five records are synthetic.
- `collection_method` is skewed toward `synthetic` for the same reason.

Interpretation: the audit script correctly distinguishes schema readiness from dataset representativeness. The sample is valid for workflow QA, but not for research conclusions.

## Baseline Variant Result

| Variant | Binary items | TP | FP | FN | Precision | Recall | F1 | High-risk predictions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `text_only` | 4 | 1 | 0 | 2 | 1.000 | 0.333 | 0.500 | 1 |
| `text_reply` | 4 | 2 | 0 | 1 | 1.000 | 0.667 | 0.800 | 2 |
| `text_ocr` | 4 | 3 | 0 | 0 | 1.000 | 1.000 | 1.000 | 3 |
| `all` | 4 | 3 | 0 | 0 | 1.000 | 1.000 | 1.000 | 3 |

Important limitation: this is a five-record synthetic QA set. These metrics prove command behavior and expected field use. They do not estimate real performance.

## Per-Case Lessons

| Item | Lesson |
|---|---|
| `threads-synth-v1-0001` | Text-only can catch obvious guaranteed-profit language after baseline tuning, but replies add stronger private-channel evidence. |
| `threads-synth-v1-0002` | OCR and visible-link/contact fields are decisive for screenshot-style redirection cases. |
| `threads-synth-v1-0003` | Benign comparator stayed `non_scam`; the baseline was tuned to avoid treating generic "before and after" wording as earnings-testimonial evidence. |
| `threads-synth-v1-0004` | Ambiguous finance content remains outside binary metrics; this is correct for calibration because weak investment context alone should not become `scam`. |
| `threads-synth-v1-0005` | Reply and OCR fields both surface decisive fee, verification, and pseudo-official reward language. |

## Baseline Adjustment Made

The dry run exposed three small rule-calibration issues in `scripts/rule_baseline_v1.py`, which were corrected before recording the final dry-run result:

- guaranteed-profit plus unrealistic-benefit evidence is now high risk
- redirect plus proof/authority plus urgency is now high risk
- generic "before and after" wording no longer triggers the earnings-testimonial signal by itself

These are conservative baseline changes. They do not add automation, crawling, or model assistance.

## What This Proves

The repo is ready to run a local, governed pilot workflow once real data authorization exists:

- schema validation works on CSV and JSON
- CSV-to-JSONL conversion works
- dataset audit identifies source skew and missing evidence fields
- rule baseline variants can compare post text, replies, OCR, links, handles, and redirects
- generated predictions can stay in ignored local folders
- aggregate findings can be copied into commit-safe experiment notes

## What This Does Not Prove

This dry run does not prove:

- real Threads scam prevalence
- baseline accuracy on live content
- annotator reliability on real evidence
- that stakeholder-provided examples may be used
- that screenshots, URLs, handles, or OCR text may be retained
- that automated collection is permitted

## Decision

Proceed to stakeholder report review and pilot authorization. Do not collect real examples until `docs/36-stakeholder-authorization-packet.md`, `templates/stakeholder_authorization_decision_record.md`, `templates/data_authorization_request.md`, `docs/26-pilot-go-no-go-checklist.md`, and `templates/real_pilot_readiness_review.md` are completed.

After authorization, repeat the same workflow on the 50-item pilot and record the result under `experiments/dataset-audit/` and `experiments/baselines/`.
