# Templates

Reusable templates for dataset collection, annotation, governance, and experiments.

## Current Templates

```text
500_item_expansion_work_order.md
baseline_error_review_table.csv
annotation_sheet_template.csv
annotation_disagreement_log_template.csv
annotation_qa_checklist.md
annotator_onboarding_checklist.md
adjudication_template.md
collection_log_template.csv
controlled_launch_details_template.md
data_authorization_request.md
dataset_manifest_template.md
experiment_log_template.md
guideline_revision_log_template.md
pilot_batch_work_order.md
pilot_checkpoint_review.md
pilot_decision_memo.md
pilot_result_summary.md
real_pilot_readiness_review.md
redaction_checklist.md
report_review_feedback.md
source_candidate_intake.md
source_sampling_frame_template.csv
stakeholder_authorization_decision_record.md
stakeholder_pilot_request_email.md
thread_item_sample.json
thread_item_sample_batch.json
```

Use the annotation, onboarding, QA, adjudication, disagreement, and guideline-revision templates for annotation workflow. Use the authorization, collection, redaction, work-order, result-summary, and manifest templates before or during the authorized pilot workflow. Use `report_review_feedback.md` for report-v0 stakeholder and reviewer comments.

Use `500_item_expansion_work_order.md` only after the staged expansion gates in `docs/32-500-item-expansion-plan.md` are satisfied.

Use `pilot_decision_memo.md` and `baseline_error_review_table.csv` after the 50-item pilot to decide whether to expand, revise, narrow, or pause.

Use `pilot_checkpoint_review.md` with `docs/38-first-pilot-checkpoint-protocol.md` after the first 10-15 real pilot items before completing all 50 items.

Use `source_candidate_intake.md` and `source_sampling_frame_template.csv` before any real source enters authorization or collection.

Use `stakeholder_authorization_decision_record.md` with `docs/36-stakeholder-authorization-packet.md` to record source, field, storage, access, retention, redaction, and sharing decisions.

Use `real_pilot_readiness_review.md` as the final owner-facing readiness record before any real 50-item pilot begins.

Use `controlled_launch_details_template.md` only in a controlled location outside git after filling it with exact source, storage, access, retention, or redaction details.

Do not put real Threads evidence, raw screenshots, credentials, browser exports, or stakeholder case material in templates.
