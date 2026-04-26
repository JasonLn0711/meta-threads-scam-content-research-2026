# Threads Scam Content Research v0 Executive Brief

## Brief Identity

| Field | Value |
|---|---|
| Report package | Threads scam-content research v0 |
| Target delivery date | 2026-04-30 |
| Audience | CIB/165-facing review, anti-fraud research planning, investigators, professors, and engineers |
| Status | Review brief aligned to checkpoint 0055 plus 0076 hard-negative addendum. No production promise. No legal determination claim. |
| Primary report | `reports/threads-scam-content-research-v0.md` |

## Bottom Line

The next useful research step is report-delivery hardening and a bounded stakeholder decision, not a production detector and not broad collection by habit.

The current evidence-system state is:

- checkpoint 0055 is the canonical approved package for CIB/165-facing review;
- item 0076 is a narrow hard-negative addendum: `non_scam` / `low`;
- local 76-record aggregate validation passed, but it does not replace the approved 55-record package;
- browser-session search has value for calibration and candidate-quality testing, but it has not justified unbounded expansion;
- confirmed-pointer intake remains the strongest path if stakeholders need more scam/high-risk rule-family learning.

This keeps the project useful under budget while avoiding unsupported claims about legal fraud, automated enforcement, platform-scale detection, or collection authority.

## Why Threads First

Threads is the recommended first surface because stakeholder discussion suggests high scam-content report pressure there, and the first evidence surfaces are realistic to inspect:

- post text
- selected replies and comments
- text in images or screenshots through OCR
- visible links and domains
- visible contact handles
- redirection language to private channels or external platforms

This is narrower and more defensible than a Meta-wide scam-ad system. It also avoids making long video, deepfake detection, account graph analysis, or production automation prerequisites for the first research result.

## What The v0 Package Provides

The repo now supports a first research pilot through:

- a `thread_item` dataset schema
- a human annotation guideline
- a label vocabulary for `scam`, `non_scam`, `uncertain`, and `insufficient_evidence`
- governance, collection, and redaction templates
- pilot runbooks and go/no-go checks
- controlled launch, local workspace, preflight, rehearsal, rehearsal-review, and first-checkpoint operating docs
- synthetic calibration samples
- local validation, audit, agreement, conversion, and rule-baseline scripts
- an initial report tying scope, evidence, budget, governance, annotation, and baseline experiments together

The package is intentionally documentation-first and tooling-light.

## Decision Requested

Stakeholders should decide which bounded path is needed next.

| Option | Meaning | When to choose |
|---|---|---|
| `report_only_delivery` | Share and refine the checkpoint report package without new collection. | Choose this if 0055 plus 0076 is enough for current review. |
| `targeted_confirmed_pointer_tranche` | Add a small number of approved stakeholder/CIB pointers through controlled capture, redaction, second review, and strict validation. | Choose this if new scam/high-risk rule-family learning is needed. |
| `calibration_only_browser_tranche` | Use approved browser-session work only for hard negatives, uncertainty, or false-positive calibration. | Choose this if reviewer burden and rule boundaries need stress testing. |

Any future collection still requires a new decision record, capped scope, controlled preservation, redacted fields, second review, strict validation, and repo-safe reporting.

## What This Work Will Not Do

The v0 package does not authorize:

- uncontrolled automated Threads collection or scraping outside the approved controlled launch record
- uncontrolled account or profile crawling
- uncontrolled landing-page crawling or redirect expansion
- production scoring
- enforcement actions
- legal fraud determinations
- unredacted sensitive data in git
- broad Meta cross-platform integration
- heavy video or deepfake detection as phase-1 mainline work

## Current Package Design

The approved checkpoint package is diagnostic, not a prevalence estimate. It should be read as an evidence-system review package:

| Component | Purpose |
|---|---|
| Checkpoint 0055 | Canonical approved 55-record package. |
| 0076 hard-negative addendum | Tests anti-scam warning and scam-method vocabulary false-positive pressure. |
| Confirmed-pointer method | Highest-yield path for new final scam/high-risk rule-family learning. |
| Browser-session candidate methods | Useful only when capped, dedupe-first, full-thread-ready, and explicitly approved. |

The first baseline-ready slice should use high-confidence or adjudicated items with nonempty evidence fields, clear `scam` or `non_scam` labels, and sufficient evidence. `uncertain` and `insufficient_evidence` items should be retained for ambiguity and evidence-quality analysis, but excluded from binary precision/recall.

## Key Risks To Watch

| Risk | Mitigation |
|---|---|
| Annotators over-label aggressive marketing or finance content as scam | Require observable evidence and use `uncertain` when mixed signals remain unresolved. |
| `uncertain` becomes a catch-all | Separate mixed evidence from missing evidence; use `insufficient_evidence` when review cannot proceed. |
| Screenshots or links introduce privacy risk | Redact before annotation where required and keep raw evidence outside git. |
| The dataset skews toward only obvious lures | Include non-scam comparators and ambiguous cases from the start. |
| The report is read as a production promise | Repeat that phase 1 is research, triage, and evidence design only. |

## Next Seven Days

By 2026-04-30:

1. Complete report-v0 review using `reports/report-v0-review-checklist.md`.
2. Collect reviewer comments with `templates/report_review_feedback.md`.
3. Resolve scope, legal/privacy, and evidence-language comments before delivery.
4. Confirm whether the next path is report-only delivery, targeted confirmed-pointer intake, or calibration-only browser review.
5. If new evidence is approved, complete the controlled decision and storage records before collection.
6. Keep embedding/model training and broad crawler expansion deferred until a later explicit decision.
