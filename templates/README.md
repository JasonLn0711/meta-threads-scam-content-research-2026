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
discovery_source_arm_work_order.md
public_surface_patrol_work_order.md
experiment_log_template.md
guideline_revision_log_template.md
hard_negative_hesitation_log_template.csv
labor_savings_aggregate_report_template.md
manual_collection_prebuild_handoff.md
manual_collection_rehearsal_checklist.md
pilot_batch_work_order.md
pilot_checkpoint_review.md
pilot_decision_memo.md
pilot_result_summary.md
priority_ranking_evaluation_table.csv
real_pilot_readiness_review.md
redaction_checklist.md
report_review_feedback.md
reviewer_assist_governance_checklist.md
reviewer_assist_labor_savings_worksheet.md
reviewer_triage_packet.md
schema_prefill_correction_log_template.csv
signal_family_extraction_qa_table.csv
source_candidate_intake.md
source_sampling_frame_template.csv
stakeholder_authorization_decision_record.md
stakeholder_pilot_request_email.md
summary_usefulness_rubric.md
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

Use `public_surface_patrol_work_order.md` only after Decision `0156` and
`docs/74-public-surface-human-reproducible-patrol-v0.md` are in scope. It is a
planning and run-gate template for a public no-login, low-frequency,
human-reproducible browser fallback proposal; it does not authorize live
collection or Playwright execution by itself.

Use the Reviewer Assist evaluation templates opened by Decision `0145` only for metadata-only labor-savings evaluation in service of the governed automatic or assisted discovery method:

- `reviewer_assist_labor_savings_worksheet.md`
- `schema_prefill_correction_log_template.csv`
- `summary_usefulness_rubric.md`
- `signal_family_extraction_qa_table.csv`
- `hard_negative_hesitation_log_template.csv`
- `priority_ranking_evaluation_table.csv`
- `labor_savings_aggregate_report_template.md`
- `reviewer_assist_governance_checklist.md`

These templates measure whether assisted review improves discovery yield per reviewer hour without increasing correction burden, disagreement, hard-negative false-positive pressure, or governance risk. They do not authorize new collection, real LLM/API calls, model training, production detection, legal determinations, enforcement, or raw evidence in git.

Use `browser_candidate_promotion_review.md` with `docs/53-dedupe-first-full-thread-ready-gate.md` before any future browser-session candidate is promoted into an official selected item after run `0039`.

Use `source_candidate_intake.md` and `source_sampling_frame_template.csv` before any real source enters authorization or collection.

Use `stakeholder_authorization_decision_record.md` with `docs/36-stakeholder-authorization-packet.md` to record source, field, storage, access, retention, redaction, and sharing decisions.

Use `real_pilot_readiness_review.md` as the final owner-facing readiness record before any real 50-item pilot begins.

Use `controlled_launch_details_template.md` only in a controlled location outside git after filling it with exact source, storage, access, retention, redaction, screenshot, OCR, URL/link, handle/contact, role-ID, permitted-field, forbidden-field, uncertainty, and signoff details.

Use `discovery_source_arm_work_order.md` before any Discovery Method v1 source
arm is executed. It is the current template for official Threads API viability
checks and any future controlled browser fallback proposal. It does not
authorize personal-account crawling, one-second browser fetching, raw evidence
in git, final automated labels, production detection, enforcement, or public
warnings.

Do not put real Threads evidence, raw screenshots, credentials, browser exports, or stakeholder case material in templates.
