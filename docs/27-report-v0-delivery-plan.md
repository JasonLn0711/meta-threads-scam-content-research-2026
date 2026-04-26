# Report v0 Delivery Plan

## Purpose

This plan turns the Threads scam-content research v0 report into a controlled post-0076 stakeholder review package.

The immediate deliverable is a selected reviewer package for path selection by 2026-04-30. This plan does not authorize item `0077`, real Threads data collection, automation, scraping, model deployment, production scoring, or legal fraud determinations.

Current package status: `revise_before_delivery`.
Current selected path under review: `report_only_delivery`.

## Delivery Package

Share the selected post-0076 reviewer package, not a full repo snapshot. `PACKAGE_MANIFEST.md` and `REVIEWER_README.md` are the package entrypoints.

| Artifact | Purpose |
|---|---|
| `PACKAGE_MANIFEST.md` | Selected package manifest, reading order, and full-repo reference boundary. |
| `REVIEWER_README.md` | Canonical reviewer entrypoint and response table. |
| `reports/threads-scam-content-research-v0-executive-brief.md` | Short stakeholder brief and decision request. |
| `reports/threads-scam-content-research-v0.md` | Full research report. |
| `reports/post-0076-next-decision-memo.md` | Bounded decision memo after checkpoint 0055 and 0076. |
| `reports/post-0076-validation-provenance.md` | Repo-safe validation and baseline provenance. |
| `reports/report-v0-review-checklist.md` | Pre-delivery and reviewer sign-off checklist. |
| `reports/checkpoint-0055-approved-package-index.md` | Canonical approved checkpoint package index. |
| `reports/checkpoint-0076-hard-negative-addendum.md` | Narrow local hard-negative addendum. |
| `governance/pilot-launch/run_index.md` | Repo-safe run and item index. |
| `decision-log/0096-record-post-0076-reviewer-path-selection.md` | Current reviewer path-selection decision record. |
| `templates/report_review_feedback.md` | Structured feedback form for reviewers. |
| `data-contracts/thread_item_schema_v1.json` | Repo-safe item schema contract. |
| `data-contracts/labeling_schema_v1.json` | Repo-safe label schema contract. |

Historical pilot-launch documents and authorization templates remain available in the full repo for context, but they are not the current reviewer decision form and do not authorize new evidence collection.

## Review Sequence

| Step | Target date | Owner | Output |
|---|---:|---|---|
| Internal research review | 2026-04-24 | Research owner | Scope, methods, baseline, and budget comments. |
| Legal/privacy review | 2026-04-25 | Legal or data-governance reviewer | Data handling, storage, redaction, and wording comments. |
| Domain review | 2026-04-26 | Anti-fraud or investigator reviewer | Scam-type, evidence, and annotation-boundary comments. |
| Technical review | 2026-04-27 | Engineering/research reviewer | Schema, tooling, baseline, and evaluation comments. |
| Report revision | 2026-04-28 | Research owner | Updated report and executive brief. |
| Stakeholder readout prep | 2026-04-29 | Research owner and stakeholder owner | Final package and meeting agenda. |
| CIB/165-facing delivery | 2026-04-30 | Stakeholder owner | Decision: `report_only_delivery`, `targeted_confirmed_pointer_tranche`, or `calibration_only_browser_tranche`. |

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
| Data authorization blocker | Keep report delivery if safe, but do not open new evidence collection until a new capped decision and authorization record exist. |
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
- any later evidence step must first receive a new capped decision, controlled storage plan, redaction plan, second review, and strict-validation requirement

## Stakeholder Readout Agenda

1. Confirm the report is a selected post-0076 reviewer package, not a full repo snapshot.
2. Explain why Threads is the phase-1 target.
3. Review what evidence fields the `thread_item` schema preserves.
4. Review the four primary annotation labels.
5. Review why historical pilot-launch materials are context only.
6. Review governance and privacy decisions that would be required before any later new evidence.
7. Ask for a concrete post-0076 path: `report_only_delivery`, `targeted_confirmed_pointer_tranche`, or `calibration_only_browser_tranche`.
8. If a new evidence path is chosen, require a new decision record with caps, source rules, storage rules, second review, and validation before collection.

## Decision Outcomes

| Decision | Meaning | Next action |
|---|---|---|
| `report_only_delivery` | Stakeholders want the checkpoint package delivered or refined without new evidence. | Harden the report, executive brief, checklist, and handoff notes. Do not open a new collection run. |
| `targeted_confirmed_pointer_tranche` | Stakeholders need new scam/high-risk rule-family learning from approved pointers. | Record a new decision with caps and source rules, then use controlled capture, redaction, second review, build, and strict validation. |
| `calibration_only_browser_tranche` | Stakeholders need hard negatives, uncertainty, or false-positive calibration. | Record a new decision with caps and stop conditions; do not count the tranche as official scam expansion. |

## Required Records After Delivery

After the stakeholder readout, update or create only the records required by the selected post-0076 path:

- a decision-log entry with the post-0076 outcome
- revised package status and checklist if delivery remains report-only
- a new capped collection decision only if stakeholders explicitly choose a new evidence path
- authorization, controlled-storage, redaction, second-review, and strict-validation records only after a new evidence path is approved
- `notes/` meeting note with decisions, open questions, and owners
- `docs/16-open-questions-for-stakeholders.md` to remove answered questions and add new blockers

## Do Not Start Yet

Do not start any of the following until the stakeholder decision and authorization record allow it:

- item `0077`
- real Threads collection
- screenshot storage
- source URL storage
- visible-link crawling
- automated collection
- bulk search
- profile or account review
- unredacted data transfer to external services
- model-assisted review on sensitive samples

Historical pilot vocabulary and runbooks remain in the full repo for governance history. They are not the current post-0076 authorization state.
