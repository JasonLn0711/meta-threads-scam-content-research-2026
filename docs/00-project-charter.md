# Project Charter

## Objective

Build a documentation-first research program for Threads-related scam or scam-like content. The project should identify practical signals, create defensible annotation and data contracts, compare early baselines, and narrow toward a phase-1 research MVP that fits an approximate NTD 1.8 million budget.

The central question is:

> What is the most realistic, evidence-driven, budget-fit way to study and prototype scam-content triage on Threads, starting from text, images, comments, OCR, and visible redirection signals?

## Scope

Phase 1 focuses on Threads-related content:

- Text posts
- Text plus image posts
- Replies and comments
- OCR text extracted from images or screenshots
- Visible redirection signals in posts or comments
- External links when present
- Human-review-oriented risk scoring and explanation

## Non-Goals

Phase 1 does not attempt to:

- Build a production detector.
- Make legal determinations of fraud.
- Cover all Meta platforms.
- Automate bulk Threads collection without approval.
- Prioritize long video analysis.
- Build a deepfake detection pipeline.
- Build a dashboard, data platform, or heavy ML system.

## Assumptions

- Early data collection may be semi-manual.
- Stakeholder-provided examples may become available, but legal sharing constraints are unresolved.
- Threads reports contain enough text, comment, link, and image-text signals to justify a first study.
- A small but well-labeled sample is more valuable than a larger weakly governed dataset.
- Human review remains central; automated outputs should support triage, not replace judgment.

## Constraints

- Approximate practical budget: NTD 1.8 million.
- No automated Meta data collection without documented authorization.
- Evidence must preserve uncertainty and avoid unnecessary personal data.
- Research outputs must be explainable to public-sector stakeholders.
- Early baselines should be cheap, inspectable, and auditable.

## Budget Realism

The budget can support:

- Research planning and documentation.
- Data schema and annotation design.
- A small manually reviewed dataset.
- Lightweight OCR and link-signal extraction.
- Simple keyword, rule, and possibly LLM-assisted baselines.
- Error analysis and decision memos.

The budget likely cannot support:

- Production-grade cross-platform detection.
- Continuous data ingestion from Meta.
- Large-scale human labeling.
- Heavy video understanding.
- Deepfake detection as a primary workstream.
- Platform-scale monitoring or enforcement tooling.

## Phase-1 Success

Phase 1 succeeds if it produces:

- A stable definition of Threads scam-like content for research purposes.
- A usable taxonomy and annotation guide.
- A dataset schema that preserves evidence and uncertainty.
- A 50-item pilot and a 100-200 item first usable batch after pilot review.
- A baseline comparison showing which signals add value.
- A clear recommendation on continuing, narrowing, or stopping specific workstreams.
