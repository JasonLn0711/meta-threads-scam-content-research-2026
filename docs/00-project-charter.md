# Project Charter

## Objective

Build a documentation-first research program for Threads-related scam or scam-like content. From this point forward, the project has one highest priority: design a governed automatic or assisted method for discovering review-worthy Threads investment-scam candidates.

Documentation, governance, annotation, validation, baseline work, Reviewer Assist, metrics, and reporting exist to support that discovery-method goal. They are not the final goal by themselves and must not contradict the automatic discovery-method design.

The central question is:

> What governed automatic or assisted candidate-discovery method can find enough review-worthy Threads investment-scam candidates while minimizing reviewer burden, preserving hard-negative boundaries, controlling false-positive pressure, and keeping evidence handling governance-safe?

Labor reduction is not a secondary convenience. It is an operational feasibility constraint and a core research success condition.

## Scope

Phase 1 focuses on Threads-related content:

- Governed automatic or assisted investment-scam candidate discovery as the first focused method objective
- Text posts
- Text plus image posts
- Replies and comments
- OCR text extracted from images or screenshots
- Visible redirection signals in posts or comments
- External links when present
- Human-review-oriented risk scoring and explanation
- Labor-efficient reviewer-assist support for reading, summarization, signal extraction, schema prefill, priority ranking, hard-negative checking, and repo-safe notes

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
- The first scalable method should work for investment scams before the repo expands to other scam families.
- Candidate discovery is not guilt determination; labels remain evidence-bound and review-centered.
- Discovery yield and reviewer burden must be evaluated together; neither can be optimized alone.

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
- Simple keyword and rule baselines.
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
- A scalable investment-scam candidate-discovery method that can be evaluated by yield and reviewer burden.
- Evidence that the method can find enough review-worthy candidates with acceptable average, median, and p95 review time.
- Metrics for candidates reviewed per hour, field auto-fill and correction rates, summary usefulness, full-thread-reading rate, second-review rate, disagreement rate, hard-negative false-positive pressure, insufficient-evidence rate, review-worthy yield per source arm, and high-risk yield per reviewer hour.
- A usable taxonomy and annotation guide.
- A dataset schema that preserves evidence and uncertainty.
- A 50-item pilot and a 100-200 item first usable batch after pilot review.
- A baseline comparison showing which signals add value.
- A clear recommendation on continuing, narrowing, or stopping specific workstreams.
