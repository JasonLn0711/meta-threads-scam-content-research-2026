# Authorized Pilot Execution Plan

## Purpose

This plan defines exactly what happens after stakeholders approve a real Threads pilot through `docs/36-stakeholder-authorization-packet.md` and `docs/26-pilot-go-no-go-checklist.md`.

It is not an authorization document. It is an execution plan that becomes usable only after the stakeholder authorization decision, data authorization request, source limits, raw-storage rules, redaction rules, and access list are approved.

## Current State

As of `2026-04-23`:

- synthetic workflow dry run is complete
- schema validation, audit, conversion, and rule-baseline scripts have been tested on synthetic records
- report-v0 review package exists
- pilot governance package exists
- approved pilot launch packet exists under `governance/pilot-launch/`
- launch status is `go_with_limits`
- no real Threads evidence has been collected

Default collection status remains paused until exact source, storage, access, retention, and redaction limits are written into the controlled launch record outside git.

## Activation Criteria

Begin this execution plan only when all of the following are true:

| Gate | Required artifact |
|---|---|
| Stakeholder authorization packet | Completed `docs/36-stakeholder-authorization-packet.md` |
| Stakeholder authorization decision | Completed `templates/stakeholder_authorization_decision_record.md` with `approved` or `approved_with_limits` |
| Source candidate intake | Completed `templates/source_candidate_intake.md` |
| Sampling frame | Completed `templates/source_sampling_frame_template.csv` |
| Source and field approval | Completed `templates/data_authorization_request.md` |
| Pilot go/no-go | Completed `docs/26-pilot-go-no-go-checklist.md` with `go` or `go_with_limits` |
| Batch work order | Completed `templates/pilot_batch_work_order.md` |
| Real-pilot readiness review | Completed `templates/real_pilot_readiness_review.md` with `go` or `go_with_limits` |
| Raw storage | Approved location outside git |
| Redaction | Redaction requirements understood by collector and reviewer |
| Access | Named people or roles allowed to see raw evidence |
| Retention | Deletion or retention rule recorded |

If any gate is incomplete, use only synthetic or fully redacted examples.

For the current approved pilot, the non-sensitive launch records are under `governance/pilot-launch/`. Exact sensitive source and storage/access details should remain outside git.

## Pilot Batch Identity

Recommended first real pilot identifiers:

```text
dataset_id: threads_pilot_v1_2026-05
collection_batch_id: threads_pilot_v1_2026-05
schema_version: thread_item_schema_v1
labeling_schema_version: labeling_schema_v1
annotation_guideline: docs/06-annotation-guideline-v1.md
```

Recommended local-only files:

```text
data/interim/threads_pilot_v1_collection_log.csv
data/interim/threads_pilot_v1_annotations.csv
data/interim/threads_pilot_v1_annotation_pass_ann_01.csv
data/interim/threads_pilot_v1_annotation_pass_ann_02.csv
data/processed/threads_pilot_v1.jsonl
data/processed/threads_pilot_v1_audit.md
data/processed/threads_pilot_v1_rule_variant_comparison.md
data/processed/threads_pilot_v1_agreement.md
data/processed/threads_pilot_v1_disagreements.csv
```

These files are ignored by git. Commit only aggregate, non-sensitive experiment notes and decision records.

Use [39-local-pilot-workspace.md](39-local-pilot-workspace.md) and `scripts/init_pilot_workspace.py` to create the empty `data/interim/` working files after controlled launch details are complete outside git.

## Roles

| Role | Minimum assignment |
|---|---|
| Project owner | Approves work order, checks governance gate, owns final pilot decision. |
| Data/governance reviewer | Confirms source, field, storage, retention, and sharing limits. |
| Collector | Records only approved fields and completes redaction checks. |
| Annotator 1 | Performs first-pass annotation. |
| Annotator 2 or reviewer | Reviews high-risk, uncertain, low-confidence, and sampled non-scam cases. |
| Adjudicator | Resolves disagreements and final labels. |
| Research engineer | Runs validation, audit, conversion, baseline comparison, and summary packaging. |

Use pseudonymous IDs such as `collector_01`, `ann_01`, `ann_02`, `rev_01`, and `adj_01`.

## Execution Sequence

### Step 1: Confirm Authorization

Before touching real evidence for a new pilot:

1. Complete `docs/36-stakeholder-authorization-packet.md`.
2. Complete `templates/stakeholder_authorization_decision_record.md`.
3. Complete `templates/data_authorization_request.md`.
4. Complete source intake with `templates/source_candidate_intake.md`.
5. Record the source in `governance/source-intake-register.md`.
6. Build the sampling frame with `templates/source_sampling_frame_template.csv`.
7. Record the approval summary in `governance/pilot-authorization-register.md`.
8. Complete `docs/26-pilot-go-no-go-checklist.md`.
9. Fill `templates/pilot_batch_work_order.md`.
10. Complete `templates/real_pilot_readiness_review.md` using `docs/35-real-pilot-readiness-review.md`.
11. Confirm raw evidence storage outside git.
12. Onboard annotators with `docs/30-annotator-onboarding-quickstart.md` and `templates/annotator_onboarding_checklist.md`.

Stop if the decision is `no_go`, `pending`, or unclear.

For the current approved pilot, use `governance/pilot-launch/threads_pilot_v1_2026-05_work_order.md` and first complete the controlled launch details outside git.

### Step 2: Prepare Local Files

Create local working copies under ignored folders:

```bash
python scripts/init_pilot_workspace.py --dry-run
python scripts/init_pilot_workspace.py --ack-controlled-details
```

This creates the collection log, primary annotation sheet, two annotator pass sheets, checkpoint worksheet, and local workspace manifest under ignored `data/interim/`.

Do not copy raw screenshots, source exports, credentials, browser profiles, or stakeholder case packets into git.

### Step 3: Collect 50 Candidate Items

Use the diagnostic composition:

| Bucket | Target |
|---|---:|
| likely scam or high-risk scam-like | 15 |
| likely non-scam comparator | 15 |
| uncertain or ambiguous | 10 |
| insufficient-evidence or low-context | 10 |

The collector should complete collection fields and evidence-status fields first. If an item cannot be redacted or documented safely, exclude it and record the reason in the collection log.

For the current approved pilot, do not collect all 50 items in one uninterrupted pass. Pause after the first 10-15 collected or annotated rows and run `docs/38-first-pilot-checkpoint-protocol.md`.

### Step 4: Redaction QA

Before annotation:

1. Run `templates/redaction_checklist.md` on every item with screenshots, OCR, source URLs, contact handles, or stakeholder case context.
2. Replace contact handles with redacted category values such as `telegram:[redacted]`.
3. Normalize or redact URLs according to the authorization request.
4. Confirm `privacy_redaction_notes` is filled where redaction occurred.
5. Confirm raw evidence is outside git.

### Step 5: Validate Before Annotation

Run validation as soon as the 50 rows have collection/content fields:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
```

Fix schema errors before annotators begin. Warnings should be reviewed and either fixed or explained in `metadata_notes` or `missing_evidence`.

### Step 6: Annotate

Annotator 1 fills:

- `scam_label`
- `scam_type`
- `risk_level`
- `signal_tags`
- `evidence_sufficiency`
- `annotation_confidence`
- `missing_evidence`
- `annotation_notes`
- `annotator_id`
- `review_status`

Do not force `uncertain` or `insufficient_evidence` into binary labels.

After the first 10-15 annotated rows, pause for in-pass QA using `docs/31-annotation-quality-control-plan.md` and `templates/annotation_qa_checklist.md`.

### Step 7: Second Review And Adjudication

Second review is required for:

- all high-risk `scam` labels
- all `uncertain` labels
- all low-confidence labels
- all cases with `partial`, `insufficient`, or `not_reviewable` evidence
- a sample of `non_scam` comparator items

Use:

- `templates/annotation_disagreement_log_template.csv`
- `templates/adjudication_template.md`

Fill `final_label` and `final_risk_level` only after adjudication.

### Step 8: Audit And Convert

After first annotation and required reviews:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv --strict
python scripts/convert_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv \
  data/processed/threads_pilot_v1.jsonl \
  --validate
python scripts/audit_thread_dataset.py data/processed/threads_pilot_v1.jsonl \
  > data/processed/threads_pilot_v1_audit.md
```

If strict validation fails, pause baseline work until the dataset is corrected.

### Step 9: Run Baseline Variants

```bash
python scripts/compare_rule_variants.py data/processed/threads_pilot_v1.jsonl \
  --output data/processed/threads_pilot_v1_rule_variant_comparison.md
```

Review:

- `text_only` versus `text_reply`
- `text_only` versus `text_ocr`
- `text_only` versus `all`
- false positives among benign finance, marketing, creator, recruitment, health, or giveaway cases
- false negatives where OCR, replies, or visible redirects carried decisive evidence

### Step 10: Package Results

Create a non-sensitive summary using `templates/pilot_result_summary.md`.

Then complete decision analysis using:

- `docs/33-pilot-analysis-and-decision-framework.md`
- `templates/baseline_error_review_table.csv`
- `templates/pilot_decision_memo.md`
- `experiments/evaluation-notes/0003-pilot-decision-analysis-protocol.md`

Commit only:

- aggregate audit findings
- aggregate baseline findings
- disagreement themes without raw personal data
- schema/guideline revision recommendations
- guideline revision log from `templates/guideline_revision_log_template.md`
- pilot decision memo
- decision log for expand, revise, narrow, or pause

Do not commit raw annotation CSVs unless they are confirmed synthetic or fully de-identified and approved.

## Stop Conditions

Pause immediately if:

- authorization is unclear
- raw screenshots or personal data enter tracked files
- source URLs include sensitive tracking or personal data with no redaction rule
- annotators need unapproved profile/account/landing-page context
- collection drifts toward automation
- `uncertain` exceeds 30 percent without a clear explanation
- `insufficient_evidence` exceeds 20 percent without a collection-quality fix
- reviewers repeatedly disagree on the same edge case

## Exit Decision

At pilot end, choose one:

| Decision | Meaning |
|---|---|
| `expand_to_100_200` | Pilot labels and evidence fields are stable enough to expand. |
| `revise_guideline_first` | Label boundaries or edge cases need cleanup. |
| `revise_schema_first` | Fields are missing, confusing, too sensitive, or too burdensome. |
| `narrow_sources` | Source skew or collection burden is too high. |
| `pause` | Authorization, privacy, or operational risk blocks continuation. |

Record the decision in `decision-log/` and update `docs/18-recommended-path-v1.md` or a v2 recommended path as needed.
