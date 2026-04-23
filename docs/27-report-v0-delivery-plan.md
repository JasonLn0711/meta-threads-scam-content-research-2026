# Report v0 Delivery Plan

## Purpose

This plan turns the Threads scam-content research v0 report into a controlled stakeholder review package.

The immediate deliverable is a readable research report and pilot-decision packet by 2026-04-30. This plan does not authorize real Threads data collection, automation, scraping, model deployment, or production scoring.

## Delivery Package

Share these files as the v0 report package:

| Artifact | Purpose |
|---|---|
| `reports/threads-scam-content-research-v0-executive-brief.md` | Short stakeholder brief and decision request. |
| `reports/threads-scam-content-research-v0.md` | Full research report. |
| `reports/report-v0-review-checklist.md` | Pre-delivery and reviewer sign-off checklist. |
| `docs/25-stakeholder-pilot-kickoff.md` | Pilot approval memo. |
| `docs/26-pilot-go-no-go-checklist.md` | Gate before real collection. |
| `templates/data_authorization_request.md` | Record of allowed source, fields, storage, retention, and access. |
| `templates/report_review_feedback.md` | Structured feedback form for reviewers. |

## Review Sequence

| Step | Target date | Owner | Output |
|---|---:|---|---|
| Internal research review | 2026-04-24 | Research owner | Scope, methods, baseline, and budget comments. |
| Legal/privacy review | 2026-04-25 | Legal or data-governance reviewer | Data handling, storage, redaction, and wording comments. |
| Domain review | 2026-04-26 | Anti-fraud or investigator reviewer | Scam-type, evidence, and annotation-boundary comments. |
| Technical review | 2026-04-27 | Engineering/research reviewer | Schema, tooling, baseline, and evaluation comments. |
| Report revision | 2026-04-28 | Research owner | Updated report and executive brief. |
| Stakeholder readout prep | 2026-04-29 | Research owner and stakeholder owner | Final package and meeting agenda. |
| CIB/165-facing delivery | 2026-04-30 | Stakeholder owner | Decision: `go`, `go_with_limits`, `no_go`, or `revise_first`. |

Dates can move if reviewer availability requires it, but the review order should stay intact: scope, governance, domain, technical, then delivery.

## Reviewer Instructions

Reviewers should use `templates/report_review_feedback.md` and classify each comment as one of:

- `blocker`: must be fixed before delivery
- `required_revision`: should be fixed in v0 before delivery
- `clarification`: useful wording or explanation improvement
- `defer`: valid issue for after v0
- `question`: needs owner response

Reviewers should identify the affected artifact and section whenever possible.

## Feedback Handling Rules

| Feedback type | Action |
|---|---|
| Legal/privacy blocker | Stop delivery until resolved or explicitly scoped out. |
| Data authorization blocker | Keep report delivery, but mark pilot as `no_go` until authorization is recorded. |
| Scope expansion request | Defer unless it is needed to prevent misunderstanding. |
| Request for production detection | Reframe as deferred phase-2 or out-of-scope work. |
| Request for real results before pilot approval | Mark as impossible until authorized data exists. |
| Taxonomy ambiguity | Accept small wording fixes; defer large taxonomy changes to post-calibration unless blocking. |
| Baseline-method change | Accept if it improves clarity without adding infrastructure; otherwise defer. |

Every accepted material change should preserve these constraints:

- no automated collection authorization is implied
- no legal guilt determination is implied
- no raw evidence enters git
- uncertainty and evidence sufficiency remain first-class
- the first real data step remains the governed 50-item pilot

## Stakeholder Readout Agenda

1. Confirm the report is a research-plan and pilot-readiness package.
2. Explain why Threads is the phase-1 target.
3. Review what evidence fields the `thread_item` schema preserves.
4. Review the four primary annotation labels.
5. Review the 5-item calibration and 50-item pilot plan.
6. Review governance and privacy decisions that must be made before real collection.
7. Ask for a concrete pilot decision: `go`, `go_with_limits`, `no_go`, or `revise_first`.
8. Assign owners for authorization, raw storage, redaction, annotation, and adjudication.

## Decision Outcomes

| Decision | Meaning | Next action |
|---|---|---|
| `go` | Stakeholders approve the pilot as written. | Complete `templates/data_authorization_request.md`, then run `docs/26-pilot-go-no-go-checklist.md`. |
| `go_with_limits` | Stakeholders approve only a constrained pilot. | Record limits in the authorization request and revise the collection/redaction SOP if needed. |
| `no_go` | Stakeholders do not approve real data work. | Continue only synthetic calibration, docs, and tooling; do not collect real examples. |
| `revise_first` | Report or pilot design needs revision before decision. | Update the report package and rerun the review checklist. |

## Required Records After Delivery

After the stakeholder readout, update or create:

- a decision-log entry with the stakeholder outcome
- `templates/data_authorization_request.md` filled for the first approved source, if any
- `docs/26-pilot-go-no-go-checklist.md` with the initial gate status
- `notes/` meeting note with decisions, open questions, and owners
- `docs/16-open-questions-for-stakeholders.md` to remove answered questions and add new blockers

## Do Not Start Yet

Do not start any of the following until the stakeholder decision and authorization record allow it:

- real Threads collection
- screenshot storage
- source URL storage
- visible-link crawling
- automated collection
- bulk search
- profile or account review
- unredacted data transfer to external services
- model-assisted review on sensitive samples

