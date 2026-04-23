# Annotation Pilot Runbook

## Purpose

This runbook turns the dataset v1 package into a repeatable annotation pilot. It covers the 5-item dry run, the 50-item pilot, audit, adjudication, and first baseline handoff.

Do not use this runbook as authorization to collect data. Collection remains governed by `governance/data-governance.md`.

Before real examples are collected, follow `docs/23-collection-and-redaction-sop.md` and complete the readiness review in `docs/35-real-pilot-readiness-review.md`.

## Roles

| Role | Responsibility |
|---|---|
| Project owner | Confirms authorized source, storage location, and pilot scope. |
| Collector | Records only approved fields and redacts unnecessary personal data. |
| Annotator 1 | Performs first-pass labeling in the CSV template. |
| Reviewer | Reviews high-risk, uncertain, low-confidence, and sampled non-scam items. |
| Adjudicator | Resolves disagreements and records final label/risk. |
| Research engineer | Runs validation, audit, and baseline scripts on local-only files. |

Use pseudonymous IDs such as `ann_01`, `rev_01`, and `adj_01`.

## Required Files

| File | Purpose |
|---|---|
| `templates/annotation_sheet_template.csv` | Manual annotation sheet header. |
| `templates/annotator_onboarding_checklist.md` | Per-annotator readiness checklist. |
| `templates/annotation_qa_checklist.md` | Batch-level annotation QA checklist. |
| `templates/annotation_disagreement_log_template.csv` | Disagreement tracking sheet. |
| `templates/adjudication_template.md` | Disagreement resolution. |
| `templates/guideline_revision_log_template.md` | Guideline change candidates from calibration, adjudication, and audit. |
| `templates/dataset_manifest_template.md` | Dataset version record. |
| `templates/collection_log_template.csv` | Per-item collection and evidence-status log. |
| `templates/redaction_checklist.md` | Redaction QA before annotation or sharing. |
| `templates/pilot_batch_work_order.md` | Batch-level authorization, roles, fields, and stop conditions. |
| `templates/pilot_result_summary.md` | Post-pilot audit, annotation, baseline, and decision summary. |
| `templates/real_pilot_readiness_review.md` | Final owner-facing readiness record before real collection. |
| `data-contracts/thread_item_schema_v1.json` | Authoritative field schema. |
| `docs/06-annotation-guideline-v1.md` | Human annotation rules. |
| `docs/20-first-dataset-batch-plan.md` | Batch size and composition. |
| `docs/29-authorized-pilot-execution-plan.md` | Exact execution sequence after authorization. |
| `docs/35-real-pilot-readiness-review.md` | Integrated source, governance, annotation, QA, and baseline launch gate. |
| `experiments/dataset-audit/0001-pilot-audit-protocol.md` | Audit protocol. |
| `experiments/baselines/0001-rule-baseline-v1.md` | First baseline protocol. |
| `docs/24-annotator-training-and-calibration.md` | Annotator training and agreement workflow. |
| `docs/30-annotator-onboarding-quickstart.md` | Short annotator desk reference. |
| `docs/31-annotation-quality-control-plan.md` | QA stages, thresholds, review routing, and baseline-readiness checks. |

## 5-Item Dry Run

Use five synthetic or redacted items before any real pilot collection.

1. Copy `templates/annotation_sheet_template.csv` to a local-only file under `data/interim/`.
2. Fill five rows using synthetic/redacted examples.
3. Have Annotator 1 label all five.
4. Have the reviewer independently review at least two: one high-risk, one uncertain or ambiguous.
5. Run validation and audit.
6. Complete the relevant parts of `templates/annotation_qa_checklist.md`.
7. Fix the workflow before touching the 50-item pilot.

Commands:

```bash
python scripts/prepare_calibration_files.py data/samples/thread_item_sample_batch.csv \
  --blind-output data/interim/threads_dry_run_v1_blind.csv \
  --annotator-copy ann_01:data/interim/threads_dry_run_v1_annotations.csv
python scripts/validate_thread_dataset.py data/interim/threads_dry_run_v1_annotations.csv
python scripts/audit_thread_dataset.py data/interim/threads_dry_run_v1_annotations.csv > data/processed/threads_dry_run_v1_audit.md
python scripts/convert_thread_dataset.py data/interim/threads_dry_run_v1_annotations.csv data/processed/threads_dry_run_v1.jsonl --validate
```

Dry-run success means:

- zero schema errors
- annotators understand the label set
- at least one disagreement can be adjudicated cleanly
- no one needs to store raw screenshots or personal data in git

## Annotator Calibration

Before the 50-item pilot, have two annotators independently label the same five synthetic or redacted calibration items.

Prepare the local files:

```bash
python scripts/prepare_calibration_files.py data/samples/thread_item_sample_batch.csv \
  --blind-output data/interim/calibration_blind.csv \
  --answer-key-output data/processed/calibration_answer_key.csv \
  --annotator-copy ann_01:data/interim/calibration_ann_01.csv \
  --annotator-copy ann_02:data/interim/calibration_ann_02.csv
```

Compare the passes:

```bash
python scripts/compare_annotation_passes.py \
  data/interim/calibration_ann_01.csv \
  data/interim/calibration_ann_02.csv \
  --name-a ann_01 \
  --name-b ann_02 \
  --output data/processed/calibration_agreement.md \
  --disagreements-csv data/processed/calibration_disagreements.csv
```

Use `docs/24-annotator-training-and-calibration.md` to decide whether to proceed, recalibrate, or revise the guideline.

## 50-Item Pilot

Use `docs/29-authorized-pilot-execution-plan.md` after the authorization gate and real-pilot readiness review pass.

For the approved pilot launch, run the first 10-15 item checkpoint in `docs/38-first-pilot-checkpoint-protocol.md` before completing all 50 items.

Use the composition in `docs/20-first-dataset-batch-plan.md`:

- 15 likely scam or high-risk scam-like items
- 15 likely non-scam comparator items
- 10 uncertain or ambiguous items
- 10 insufficient-evidence or low-context items

Recommended local file names:

```text
data/interim/threads_pilot_v1_annotations.csv
data/processed/threads_pilot_v1.jsonl
data/processed/threads_pilot_v1_audit.md
data/processed/threads_pilot_v1_rule_variant_comparison.md
```

## Annotation Workflow

1. Collector fills identity, provenance, and content fields.
2. Annotator 1 fills `scam_label`, `scam_type`, `risk_level`, `signal_tags`, `evidence_sufficiency`, `annotation_confidence`, `missing_evidence`, and `annotation_notes`.
3. Run in-pass QA after the first 10-15 rows using `docs/31-annotation-quality-control-plan.md`.
4. Reviewer checks all `scam` high-risk items, all `uncertain` items, all low-confidence items, partial/insufficient evidence items, OCR-only decisive cases, reply-only decisive cases, and a sample of `non_scam` items.
5. Adjudicator resolves disagreements with `templates/adjudication_template.md`.
6. Research engineer validates, audits, converts, and runs baseline comparison.

## Validation And Conversion

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
python scripts/convert_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv data/processed/threads_pilot_v1.jsonl --validate
python scripts/audit_thread_dataset.py data/processed/threads_pilot_v1.jsonl > data/processed/threads_pilot_v1_audit.md
```

If validation has errors, fix the annotation file before running baselines.

## Baseline Handoff

Run all rule variants:

```bash
python scripts/compare_rule_variants.py data/processed/threads_pilot_v1.jsonl > data/processed/threads_pilot_v1_rule_variant_comparison.md
```

Then inspect:

- whether `text_ocr` improves recall over `text_only`
- whether `text_reply` catches reply-only lures
- whether `all` overflags legitimate links or contact info
- whether high-risk predictions have evidence-backed reasons

## Pilot Stop Conditions

Pause before expanding to 100-200 items if:

- `uncertain` exceeds about 30 percent
- `insufficient_evidence` exceeds about 20 percent
- schema validation errors are common
- annotators repeatedly disagree on the same edge case
- external links or contact handles are stored too specifically
- raw screenshots or personal data are creeping into tracked files

## Pilot Exit Deliverables

At the end of the 50-item pilot, produce:

- dataset manifest
- aggregate audit summary
- disagreement/adjudication summary
- annotation agreement summary
- rule baseline variant comparison
- completed `templates/pilot_result_summary.md`
- recommendation: expand, revise guideline, revise schema, or narrow scope
