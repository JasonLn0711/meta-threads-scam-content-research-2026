# Recommended Path v1

## Immediate Report Milestone

By `2026-04-30`, produce [../reports/threads-scam-content-research-v0.md](../reports/threads-scam-content-research-v0.md) for CIB/165-facing review.

This report is the immediate research deliverable. It should turn the current scaffold into a readable v0 initial research report with problem definition, Threads-only scope, dataset v0 plan, annotation strategy, baseline comparison, evaluation framework, governance gates, budget-fit argument, and four-week execution path.

Use [27-report-v0-delivery-plan.md](27-report-v0-delivery-plan.md), [../reports/threads-scam-content-research-v0-executive-brief.md](../reports/threads-scam-content-research-v0-executive-brief.md), and [../reports/report-v0-review-checklist.md](../reports/report-v0-review-checklist.md) to make the report package reviewable before delivery.

The report supersedes a concept-only stakeholder scoping memo as the next artifact.

## What To Do Now

Build a phase-1 research MVP for Threads scam-like content triage.

Immediate next action: review the 55-record checkpoint report package in [../reports/threads-scam-content-checkpoint-0055-v0.1.md](../reports/threads-scam-content-checkpoint-0055-v0.1.md), [../reports/checkpoint-0055-decision-request.md](../reports/checkpoint-0055-decision-request.md), and [../reports/checkpoint-0055-review-checklist.md](../reports/checkpoint-0055-review-checklist.md), then record whether stakeholders choose C1, C2, or C3 before any item `0056` collection.

Decision 0058 selected a collection pause and checkpoint report v0.1 after checkpoint 0042. Decision 0059 then selected Option A for one bounded browser-session tranche. Decision 0060 closed that tranche after it reached 20 reviewed candidates and 10 selected items. Decision 0061 selected the 55-record checkpoint report package and blocks item `0056` until a new decision is recorded.

The next checkpoint decision should choose one of three paths:

- Pause additional browser-session candidate search and wait for CIB/stakeholder confirmed pointers if more final scam/high-risk rule families are needed.
- Pause collection and turn the 55-record pilot into an updated CIB/165-facing checkpoint report.
- Open another browser-session tranche only if stakeholders explicitly accept that its main value is false-positive and uncertainty calibration, not high-risk scam discovery.

Do not continue by habit. Run 0038 shows that approved browser-session search can produce strict-valid records, but it did not add final scam/high-risk items. Confirmed pointers remain the higher-yield path for rule-family learning.

The synthetic workflow dry run has been completed in [28-synthetic-pilot-dry-run-results.md](28-synthetic-pilot-dry-run-results.md). Treat it as tooling QA only; it does not replace stakeholder authorization or real pilot evidence.

The stakeholder outcome has been reported as approved. The launch packet is recorded under `governance/pilot-launch/` with status `go_with_limits`.

The same-day research status and first-principles rationale are summarized in [../notes/2026-04-23-research-day-notes.md](../notes/2026-04-23-research-day-notes.md).

Execute the pilot through [29-authorized-pilot-execution-plan.md](29-authorized-pilot-execution-plan.md), `governance/pilot-launch/threads_pilot_v1_2026-05_work_order.md`, and `templates/pilot_result_summary.md`.

Before any pilot labels are treated as baseline-ready, onboard annotators with [30-annotator-onboarding-quickstart.md](30-annotator-onboarding-quickstart.md) and run QA through [31-annotation-quality-control-plan.md](31-annotation-quality-control-plan.md).

Do not jump directly to a broad crawler expansion, 500-item dataset, embedding experiment, or model-training pass. The safe path to larger scale is documented in [32-500-item-expansion-plan.md](32-500-item-expansion-plan.md), but it depends on checkpoint review and an explicit continuation decision.

The MVP should include:

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
