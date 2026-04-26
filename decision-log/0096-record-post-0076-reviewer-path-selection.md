# Decision 0096: Record Post-0076 Reviewer Path Selection

## Status

accepted

## Selected Path

`report_only_delivery`

## Delivery Status

`revise_before_delivery`

## Decision Owner

research owner / reviewer package maintainer

## Date

2026-04-26

## Scope

Refine and deliver the selected post-0076 report v0 package.

Checkpoint 0055 remains the canonical approved CIB/165-facing checkpoint package. Item 0076 remains a narrow local hard-negative addendum for false-positive calibration.

No new evidence collection is authorized by this decision.

## Required Changes Before Delivery

- Replace stale pilot-execution decision vocabulary in reviewer-facing materials with the post-0076 three-path decision vocabulary.
- Add a selected-package manifest so reviewers understand that the ZIP is not a full repo snapshot.
- Add repo-safe validation provenance for checkpoint 0055 and the local 0076 addendum.
- Make `REVIEWER_README.md`, the delivery handoff response table, and `templates/report_review_feedback.md` the canonical reviewer decision forms.
- Clarify that historical pilot-launch and authorization files remain full-repo context only.
- Clarify that strict validation means schema and validation checks passed, not evidence approval.
- Clarify that baseline metrics are smoke-test metrics on the current binary-evaluable slice, not production performance estimates.
- Rebuild the reviewer ZIP and rerun package leakage checks.

## Explicit Non-Authorizations

This decision does not authorize:

- item `0077`
- broad browser-session expansion
- crawler expansion
- confirmed-pointer intake without a new capped decision
- calibration browser tranche without a new capped decision
- embedding or model training
- production detection
- legal fraud determinations
- raw evidence in git

## Delivery Gate

Delivery may proceed only after required report/package edits are resolved and legal/privacy, domain, technical, and stakeholder sign-off status is recorded.

Any later evidence path must be recorded in a new decision log with caps, allowed source path, controlled storage requirements, redaction requirements, second-review requirements, strict-validation requirements, and stop conditions.
