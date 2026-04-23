# 2026-04-23 CIB/165 Report v0 Direction

## What Changed Today

The immediate deliverable changed from a concept-level stakeholder scoping memo to a real initial research report.

The report target is:

- Title: Threads scam-content research report v0.
- Deadline: 2026-04-30.
- Audience: CIB/165-facing review and internal research alignment.
- Scope: Threads only.
- Posture: research plan with concrete dataset, annotation, baseline, evaluation, governance, and budget sections.

## Strategic Judgment

Threads should remain the first execution surface because current stakeholder context suggests high report pressure there, and because the first evidence surfaces are practical:

- Text posts.
- Text plus image posts.
- Replies/comments.
- OCR from attached images and screenshots.
- Visible redirection signals.
- External links when present.

This is still not a production detector. The report should help decide what a lawful, review-supporting phase-1 MVP can realistically do under the NTD 1.8M research budget.

## Important Boundary

The CIB/165 context should be described as stakeholder background. It should not be treated as verified dataset evidence unless samples, authority, and data-handling rules are later provided.

Do not overclaim:

- No legal fraud determination.
- No automated enforcement.
- No broad Meta coverage.
- No automated Threads collection unless approved.
- No deepfake or video-heavy mainline in phase 1.

## Action Items

- [x] Create `reports/threads-scam-content-research-v0.md`.
- [x] Add a report index at `reports/README.md`.
- [x] Record a decision log for the April 30 report deadline.
- [x] Link the report from `README.md`.
- [x] Mention the April 30 milestone in `docs/18-recommended-path-v1.md`.
- [x] Create report-v0 executive brief, review checklist, delivery plan, and reviewer feedback template.
- [x] Add pilot readiness gate, authorization workflow, and stakeholder kickoff materials.
- [x] Run the synthetic sample through validation, audit, conversion, and rule-baseline variants.
- [x] Update the planning repo W18 agenda and project file.
- [ ] Create Google Calendar focus blocks and a deadline marker.

## Implementation Note

The report package and planning agenda were implemented on `2026-04-23`.

Google Calendar creation was attempted through the connector, but create/read calls returned unsupported-tool errors. Because live calendar creation could not be verified, the planning repo now contains an importable `.ics` fallback:

```text
../planning-everything-track/data/projects/2026-04-meta-scam-ad-research/2026-04-27-30-cib-165-threads-report-v0-calendar-blocks.ics
```

## Same-Day Implementation Summary

By later on `2026-04-23`, the Threads repo had advanced beyond the initial report direction:

- Dataset and annotation v1 package exists.
- Pilot governance, collection/redaction, calibration, and go/no-go docs exist.
- Report v0 package exists with executive brief and review checklist.
- Local scripts exist for validation, audit, conversion, annotation agreement, calibration-sheet preparation, and rule-baseline comparison.
- Synthetic sample and calibration CSVs exist for dry-run use only.
- Synthetic sample manifest and dry-run experiment logs were added.
- `scripts/rule_baseline_v1.py` was calibrated after the synthetic run.
- Authorized pilot execution plan, work-order template, result-summary template, and authorization register were added.
- Annotator onboarding quickstart, annotation QA plan, QA checklist, onboarding checklist, and guideline revision log template were added.
- A direct request for 500 real items without limitations was rejected or paused and replaced with a staged 500-item expansion plan.
- Pilot analysis and decision framework, decision memo, and baseline error review table were added.
- Source intake and sampling-frame docs, templates, and register were added.
- Integrated real-pilot readiness review docs and template were added.

The repo is now pilot-ready in the narrow sense that the workflow can be exercised locally. It is not data-ready until stakeholders approve the source, fields, raw-evidence storage, screenshot/link handling, access, retention, and redaction rules.

## Synthetic Dry-Run Result

The synthetic dry run used `data/samples/thread_item_sample_batch.csv` and produced:

- CSV strict validation: 5 records, 0 errors, 0 warnings.
- JSON strict validation: 5 records, 0 errors, 0 warnings.
- CSV-to-JSONL conversion: 5 records written locally under ignored `data/processed/`.
- Dataset audit: 3 `scam`, 1 `non_scam`, 1 `uncertain`, no missing required fields, no exact duplicates.
- Expected audit warning: 5/5 records are `researcher_synthetic`.

Rule-baseline synthetic QA:

| Variant | Precision | Recall | F1 | Note |
|---|---:|---:|---:|---|
| `text_only` | 1.000 | 0.333 | 0.500 | Catches only visible post-text lure. |
| `text_reply` | 1.000 | 0.667 | 0.800 | Reply context recovers one fee/redirection case. |
| `text_ocr` | 1.000 | 1.000 | 1.000 | OCR recovers synthetic screenshot-style cases. |
| `all` | 1.000 | 1.000 | 1.000 | Combines text, replies, OCR, links, handles, and redirects. |

These are workflow QA numbers only, not real Threads performance claims.

## Current Blocker

The next real research step is stakeholder approval:

1. Review `reports/threads-scam-content-research-v0-executive-brief.md`.
2. Complete `reports/report-v0-review-checklist.md`.
3. Collect comments using `templates/report_review_feedback.md`.
4. Record pilot authorization using `templates/data_authorization_request.md`.
5. Run `docs/26-pilot-go-no-go-checklist.md`.
6. If approved, complete `templates/pilot_batch_work_order.md` and execute `docs/29-authorized-pilot-execution-plan.md`.
7. Before annotation, onboard annotators with `docs/30-annotator-onboarding-quickstart.md` and run QA with `docs/31-annotation-quality-control-plan.md`.
8. Use `docs/32-500-item-expansion-plan.md` only after the 50-item pilot and 100-200 item first usable batch justify expansion.
9. After the 50-item pilot, use `docs/33-pilot-analysis-and-decision-framework.md` and `templates/pilot_decision_memo.md` to decide whether to expand, revise, narrow, or pause.
10. Before any real source is authorized, complete `templates/source_candidate_intake.md` and `templates/source_sampling_frame_template.csv`.
11. Before any real collection starts, complete `templates/real_pilot_readiness_review.md` using `docs/35-real-pilot-readiness-review.md`.

Until that gate passes, use only synthetic or fully redacted examples.

## First-Principles Reasoning

The April 30 artifact must be a report, not another concept memo, because:

1. Threads report pressure needs to be translated into a research question before data work begins.
2. The project has no authorized real dataset yet, so the report must distinguish stakeholder context from evidence.
3. NTD 1.8M can support a governed dataset slice and baseline study, but not full Meta production detection.
4. Human-review triage is the correct phase-1 output because it preserves uncertainty and avoids legal overclaiming.
5. The report creates the approval and narrowing path needed before collection, annotation, or baseline claims.
