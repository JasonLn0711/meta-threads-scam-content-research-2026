# Templates

Reusable templates for dataset collection, annotation, governance, and experiments.

## Current Templates

```text
500_item_expansion_work_order.md
baseline_error_review_table.csv
browser_candidate_promotion_review.md
annotation_sheet_template.csv
annotation_disagreement_log_template.csv
annotation_qa_checklist.md
annotator_calibration_packet_template.md
annotator_onboarding_checklist.md
adjudication_template.md
collection_log_template.csv
controlled_launch_details_template.md
controlled_crawler_run_record.md
controlled_rehearsal_review.md
data_authorization_request.md
dataset_manifest_template.md
experiment_log_template.md
guideline_revision_log_template.md
manual_collection_prebuild_handoff.md
manual_collection_rehearsal_checklist.md
pilot_batch_work_order.md
pilot_checkpoint_review.md
pilot_decision_memo.md
pilot_result_summary.md
real_pilot_readiness_review.md
redaction_checklist.md
report_review_feedback.md
reviewer_triage_packet.md
source_candidate_intake.md
source_sampling_frame_template.csv
stakeholder_authorization_decision_record.md
stakeholder_pilot_request_email.md
thread_item_sample.json
thread_item_sample_batch.json
track_b_candidate_review_template.md
```

Use the annotation, onboarding, QA, adjudication, disagreement, and guideline-revision templates for annotation workflow. Use the authorization, collection, redaction, work-order, result-summary, and manifest templates before or during the authorized pilot workflow. Use `report_review_feedback.md` for report-v0 stakeholder and reviewer comments.

Use `annotator_calibration_packet_template.md` for blind calibration setup. Use `controlled_crawler_run_record.md` before any approved crawler rehearsal, `manual_collection_prebuild_handoff.md` before building each 1-2 item controlled rehearsal record, `manual_collection_rehearsal_checklist.md` after the generated record exists, and `controlled_rehearsal_review.md` for the aggregate pass, pause, or stop decision.

Use `500_item_expansion_work_order.md` only after the staged expansion gates in `docs/32-500-item-expansion-plan.md` are satisfied.

Use `pilot_checkpoint_review.md` with `docs/38-first-pilot-checkpoint-protocol.md` after the first 10-15 real pilot items before completing all 50 items. This is the gate to `continue_to_50`, `continue_with_limits`, pause, revise, or stop.

Use `pilot_decision_memo.md`, `pilot_result_summary.md`, and `baseline_error_review_table.csv` only after the checkpoint-approved 50-item pilot to decide whether to expand to 100-200, revise, narrow, or pause.

Use `reviewer_triage_packet.md` only as a controlled worksheet pattern for item-level baseline review. Generated real packets should stay local-only unless fully sanitized and approved.

Use `track_b_candidate_review_template.md` for repo-safe Track B candidate-review outcome and reviewer-burden measurement fields. It is for dual-success evaluation only: discovery effectiveness plus reviewer-labor efficiency. It must not include raw evidence and does not change Track B caps, authorize new source arms, or authorize model training.

Use `browser_candidate_promotion_review.md` with `docs/53-dedupe-first-full-thread-ready-gate.md` before any future browser-session candidate is promoted into an official selected item after run `0039`.

Use `source_candidate_intake.md` and `source_sampling_frame_template.csv` before any real source enters authorization or collection.

Use `stakeholder_authorization_decision_record.md` with `docs/36-stakeholder-authorization-packet.md` to record source, field, storage, access, retention, redaction, and sharing decisions.

Use `real_pilot_readiness_review.md` as the final owner-facing readiness record before any real 50-item pilot begins.

Use `controlled_launch_details_template.md` only in a controlled location outside git after filling it with exact source, storage, access, retention, redaction, screenshot, OCR, URL/link, handle/contact, role-ID, permitted-field, forbidden-field, uncertainty, and signoff details.

Do not put real Threads evidence, raw screenshots, credentials, browser exports, or stakeholder case material in templates.
