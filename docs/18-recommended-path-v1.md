# Recommended Path v1

## Immediate Report Milestone

By `2026-04-30`, produce [../reports/threads-scam-content-research-v0.md](../reports/threads-scam-content-research-v0.md) for CIB/165-facing review.

This report is the immediate research deliverable. It should turn the current scaffold into a readable v0 research checkpoint with problem definition, Threads-only scope, historical dataset design, annotation strategy, baseline comparison, evaluation framework, governance gates, budget-fit argument, and a post-0076 path decision.

Use [27-report-v0-delivery-plan.md](27-report-v0-delivery-plan.md), [../reports/threads-scam-content-research-v0-executive-brief.md](../reports/threads-scam-content-research-v0-executive-brief.md), [../reports/post-0076-next-decision-memo.md](../reports/post-0076-next-decision-memo.md), and [../reports/report-v0-review-checklist.md](../reports/report-v0-review-checklist.md) to make the report package reviewable before delivery.

The report supersedes a concept-only stakeholder scoping memo as the next artifact.

## Current Post-0076 Path

The repo is now in report-delivery and stakeholder-decision mode.

Immediate next action: revise and deliver the selected post-0076 reviewer package under `report_only_delivery`. Use the approved 55-record checkpoint package plus the narrow 0076 hard-negative addendum as the current CIB/165-facing evidence-system state.

Do not execute another pilot, browser tranche, confirmed-pointer tranche, crawler expansion, embedding/model experiment, or item `0077` until reviewers choose one of:

- `report_only_delivery`
- `targeted_confirmed_pointer_tranche`
- `calibration_only_browser_tranche`

Decision 0058 selected a collection pause and checkpoint report v0.1 after checkpoint 0042. Decision 0059 then selected Option A for one bounded browser-session tranche. Decision 0060 closed that tranche after it reached 20 reviewed candidates and 10 selected items. Decision 0061 selected the 55-record checkpoint report package and blocked item `0056` until a new decision was recorded. Decision 0062 selects C2: keep collection paused and review/refine the 55-record checkpoint report package. Decision 0066 records that all reviewer roles approved the checkpoint 0055 package. Decision 0067 adds the canonical approved-package index at [../reports/checkpoint-0055-approved-package-index.md](../reports/checkpoint-0055-approved-package-index.md). Decision 0072 closed run 0039 after aggressive browser-session search added no final scam/high-risk items. Decision 0073 adopts a dedupe-first/full-thread-ready gate before any future browser candidate promotion. Decision 0085 adopts query diversification as an acquisition rule for future search-based browser runs. Decision 0093 accepts local item `0076` for next-checkpoint inclusion as `non_scam` / `low` hard-negative calibration. Decision 0094 hardens report v0 around the post-0076 state and adds a bounded next-decision memo.

The current approved package should be used from:

- [../reports/checkpoint-0055-approved-package-index.md](../reports/checkpoint-0055-approved-package-index.md)
- [../reports/checkpoint-0055-executive-addendum.md](../reports/checkpoint-0055-executive-addendum.md)
- [../reports/threads-scam-content-checkpoint-0055-v0.1.md](../reports/threads-scam-content-checkpoint-0055-v0.1.md)
- [../reports/checkpoint-0076-hard-negative-addendum.md](../reports/checkpoint-0076-hard-negative-addendum.md)
- [../reports/post-0076-next-decision-memo.md](../reports/post-0076-next-decision-memo.md)

Do not continue collection by habit. Runs 0038 and 0039 show that approved browser-session search can produce strict-valid local candidate records, but it did not add final scam/high-risk items and can create duplicate/context-thin review load. Run 0045 and item 0076 show that browser-session work can still be useful for hard-negative calibration. Confirmed pointers remain the higher-yield path for rule-family learning if a later decision requests more scam/high-risk evidence. After run `0039`, do not promote additional browser-session candidates unless a new decision authorizes that work and the candidates pass the dedupe-first/full-thread-ready gate in [53-dedupe-first-full-thread-ready-gate.md](53-dedupe-first-full-thread-ready-gate.md). If a future browser run uses search queries, apply [54-browser-query-diversification-rule.md](54-browser-query-diversification-rule.md) before execution.

The synthetic workflow dry run has been completed in [28-synthetic-pilot-dry-run-results.md](28-synthetic-pilot-dry-run-results.md). Treat it as tooling QA only; it does not replace stakeholder authorization or real pilot evidence.

The same-day research status and first-principles rationale are summarized in [../notes/2026-04-23-research-day-notes.md](../notes/2026-04-23-research-day-notes.md).

Historical pilot-launch materials remain available in [29-authorized-pilot-execution-plan.md](29-authorized-pilot-execution-plan.md), `governance/pilot-launch/threads_pilot_v1_2026-05_work_order.md`, and `templates/pilot_result_summary.md`. They are governance history and design references, not the current post-0076 authorization state.

Before any future evidence tranche is treated as baseline-ready, require a new capped decision, controlled evidence handling, redaction, second review, strict validation, and QA through [31-annotation-quality-control-plan.md](31-annotation-quality-control-plan.md).

Do not jump directly to a broad crawler expansion, 500-item dataset, embedding experiment, or model-training pass. The safe path to larger scale is documented in [32-500-item-expansion-plan.md](32-500-item-expansion-plan.md), but it depends on checkpoint review and an explicit continuation decision.

## Historical Phase-1 Design Reference

The original phase-1 MVP design remains useful as research architecture, but it does not authorize new post-0076 collection. If a later decision reopens evidence work, the design should include:

- Structured dataset schema.
- Annotation guideline.
- Scam-risk taxonomy.
- 5-item calibration, first 10-15 item checkpoint, conditional 50-item pilot, and 100-200 item first usable dataset only after pilot review.
- Rule-based risk scorer.
- OCR augmentation for image and screenshot text.
- Comment/reply context comparison.
- Visible link and redirection signal extraction.
- CIB-authorized API and automation run records where automated collection or processing is used.
- Human-review-oriented evaluation.

Do not add model-assisted explanation tests in the current launch. Revisit only after Phase 1 produces governed real evidence and a later decision record authorizes that scope.

## Why This Is The Best First Path

Threads is the current focus because stakeholder discussion suggests it receives a high volume of scam-content reports. Text, images, comments, OCR, and redirection signals are the best first evidence surfaces because they are reviewable, relatively cheap, and directly connected to likely scam lures.

This path creates learning quickly:

- Which signals matter.
- Which fields must be captured.
- Which labels are stable.
- Which baselines are useful.
- Which scope should be cut.

## What To Defer

Defer:

- Full Meta cross-platform integration.
- Automated collection.
- Long video.
- Heavy short-video analysis.
- Deepfake detection as a mainline workstream.
- Production deployment.
- Dashboard or platform engineering.
- Large custom model training.

## Phase-1 MVP Definition

The phase-1 MVP is not a detector. It is a research package that supports human review.

It should produce:

- A `thread_item_schema_v1` data contract.
- Annotation sheet template.
- Experiment log template.
- Annotated dataset slice.
- Baseline risk tiers.
- Explainable reasons for each flag.
- Error analysis.
- A decision memo on whether to expand, revise, narrow, pause, or later define a next-phase direction.

## Success After 4 Weeks

Success means:

- The team can annotate examples consistently enough to compare baselines.
- The first baseline produces understandable reasons.
- OCR, comments, or link signals show measurable value or are cut.
- Stakeholders agree that risk triage is the right operational framing.

## Evidence That Justifies Continuing

Continue if:

- High-risk tier precision is acceptable for human review.
- Recall improves when OCR or comment context is added.
- Explanations help reviewers move faster.
- Uncertain cases are routed better than with binary labels.
- Data access constraints are manageable.

## Evidence That Justifies Cutting Scope Further

Cut scope if:

- Reviewers cannot apply labels consistently.
- Comment context adds little value but high burden.
- OCR creates too much noise.
- Link signals overflag legitimate content.
- The evidence needed for useful triage is unavailable.
- Costs begin shifting toward production engineering before research questions are answered.
