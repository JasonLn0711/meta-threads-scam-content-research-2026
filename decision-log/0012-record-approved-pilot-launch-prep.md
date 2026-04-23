# Decision 0012: Record Approved Pilot Launch Preparation

## Date

2026-04-23

## Decision

Record the stakeholder outcome as approved and move the Threads pilot into controlled launch preparation.

The operational launch decision is `go_with_limits`.

## Context

The project owner reported:

> The outcome is approved, so the project should proceed to go, pilot work order, and real-pilot readiness review.

The project owner then confirmed approval of the repo's requirement that exact source, storage, access, retention, and redaction limits be written into the launch record.

The project still must preserve its governance boundaries. Approval is therefore recorded as a bounded pilot launch, not as unlimited collection or production deployment.

## Rationale

The repo has already completed:

- dataset and labeling schema
- annotation guideline
- synthetic dry run
- stakeholder authorization packet
- source intake and sampling-frame package
- go/no-go checklist
- work-order template
- real-pilot readiness review

The correct next step is to create non-sensitive launch records that let the team begin the 50-item pilot after exact raw storage and access details are confirmed outside git.

## Consequences

- The 50-item pilot may proceed under `go_with_limits`.
- Collection is manual-only or stakeholder-provided only.
- No scraping, crawling, browser automation, bulk export, landing-page crawling, redirect expansion, profile review, or production scoring is approved.
- Raw evidence, screenshots, full sensitive URLs, handles, credentials, browser exports, and stakeholder case material must not be committed.
- The first review checkpoint is after 10-15 collected or annotated rows.
- The 500-item expansion remains out of scope until pilot results and intermediate expansion gates justify it.

## Follow-Up

Before the first real item is collected:

1. Complete the controlled launch record with exact source, storage, access, retention, and redaction limits.
2. Confirm exact raw evidence storage outside git in a controlled location.
3. Confirm exact access list outside git.
4. Assign collector, annotator, reviewer, adjudicator, and research engineer IDs.
5. Create local-only working files under ignored `data/interim/`.
6. Begin with the first 10-15 item checkpoint before completing the full 50-item pilot.
