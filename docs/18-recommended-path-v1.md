# Recommended Path v1

## What To Do Now

Build a phase-1 research MVP for Threads scam-like content triage.

The MVP should include:

- Structured dataset schema.
- Annotation guideline.
- Scam-risk taxonomy.
- Manually reviewed sample of 100 to 150 items.
- Rule-based risk scorer.
- OCR augmentation for image and screenshot text.
- Comment/reply context comparison.
- Visible link and redirection signal extraction.
- Optional LLM-assisted explanation test on redacted, approved samples.
- Human-review-oriented evaluation.

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
- A decision memo for phase 2.

## Success After 4 Weeks

Success means:

- The team can annotate examples consistently enough to compare baselines.
- The first baseline produces understandable reasons.
- OCR, comments, or link signals show measurable value or are cut.
- The team knows whether LLM-assisted explanation is worth further testing.
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
