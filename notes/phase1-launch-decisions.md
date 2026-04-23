# Phase 1 Launch Decisions

This note records the current operational decisions for governed Phase 1 launch readiness. It is non-sensitive and should not contain raw evidence, exact controlled source details, raw storage paths, URLs, handles, screenshots, case IDs, credentials, or private investigative notes.

## Current Decision

The project is not moving to Phase 2.

Reason:

- Phase 1 has not yet produced checkpoint-reviewed evidence.
- As of `2026-04-24`, CIB approval is treated as complete for the current controlled pilot path; the current intake status is `ready_for_controlled_item_entry`.
- The controlled launch record is no longer the named blocker; the next blocker is safe controlled rehearsal, redaction review, a repo-safe rehearsal decision, and first 10-15 item checkpoint discipline.
- The workflow must prove safe manual collection, redaction, annotation, checkpoint review, and local baseline readiness before scale.
- No automation, scraping, live ingestion, production scoring, or new model layer is approved.

## Current Rehearsal Gate Status

Current intake status: `ready_for_controlled_item_entry`.

CIB approval is not the current blocker. The remaining blocker is operational: exactly one controlled rehearsal item still needs to be selected, entered in redacted form, built, and strict-validated before a rehearsal decision can be made.

As of `2026-04-24`, CIB and other units cannot provide redacted case examples, and manual controlled sampling is not available as the practical first path. The next acquisition path is therefore a one-item controlled low-speed crawler rehearsal under Decision 0022.

What is ready:

- CIB approval is recorded for the current controlled pilot path
- ignored local workspace files exist under `data/interim/`
- item-1 preflight has passed with zero errors
- local-only `manual_entry_0001.json` exists as an intake skeleton
- local-only selection worksheet exists and records that no item has been selected yet
- local checklist and aggregate review draft exist
- manual collection tooling can run through the ignored `.venv`
- controlled crawler acquisition plan and run-record template exist

What is not ready:

- no specific controlled rehearsal item has been selected or entered
- no controlled crawler run record has been filled for item 1
- no schema-valid real rehearsal record exists
- redaction burden has not been measured
- boundary-watch behavior has not been observed
- annotation readiness cannot be assessed

Therefore the project cannot start the first 10-15 item checkpoint yet. The next required action is to complete a controlled crawler run record, run a one-item low-speed crawler rehearsal under that record, fill the local intake with only approved redacted fields, build the local record, run strict validation, and update the aggregate rehearsal review with a new decision.

## Why 10-15 Items Come Before 50

The 10-15 item checkpoint is the first real gate because it is large enough to reveal operational problems and small enough to fix them cheaply.

It must answer:

- Can controlled manual collection produce reviewable records?
- Are redaction rules clear enough for screenshots, OCR, URLs, links, handles, replies, and stakeholder context?
- Are annotators applying labels consistently enough?
- Are too many items low-context or unreviewable?
- Is the source mix already skewed or privacy-heavy?
- Are collectors or annotators reaching for unapproved context?

The 50-item pilot is blocked unless the checkpoint decision is `continue_to_50` or `continue_with_limits`.

## Fragile Assumptions

These assumptions remain fragile until the first checkpoint:

- approved source categories will produce enough reviewable items
- redaction will not overwhelm collection
- visible links, handles, replies, screenshots, and OCR can be represented safely
- annotators can separate `uncertain` from `insufficient_evidence`
- the schema captures enough evidence without encouraging over-collection
- local-only files and generated outputs will remain outside git
- baseline outputs will be useful only after labels and evidence are stable

## What Must Be Learned Before Expansion

Before expanding beyond the first 10-15 items:

- whether governance and redaction rules work in practice
- whether the collector can avoid unapproved context
- whether annotation labels and notes are stable enough
- whether missing evidence is a collection problem or a source-quality problem
- whether the controlled source mix is too narrow, too ambiguous, or too privacy-heavy

Before expanding beyond 50:

- whether QA and adjudication produce usable final labels
- whether baseline comparisons teach anything beyond obvious keyword matching
- whether reviewer burden is manageable
- whether schema or guideline changes are required before more data
- whether a 100-200 item batch is justified by evidence, not momentum

## What Would Justify Expanding To 50

Expansion from 10-15 to 50 is justified only if:

- no raw evidence or sensitive controlled details entered git
- redaction quality is acceptable or limits can make it acceptable
- strict validation passes or field issues are fixable before more collection
- primary annotation disagreement is isolated and adjudicable
- `uncertain` and `insufficient_evidence` are not being used as catch-alls
- source/content mix remains useful for a diagnostic pilot
- no item requires unapproved profile, landing-page, redirect-chain, automation, or broad context

## What Would Justify Expanding To 100-200

Expansion beyond 50 is justified only after a decision memo shows:

- governance and privacy outcomes are green or controlled yellow
- labels, review routing, and adjudication are stable
- evidence fields are complete enough for baseline interpretation
- source skew and reviewer burden are understood
- guideline/schema/source revisions have been made or explicitly deferred
- the decision is `expand_to_100_200`, not a direct jump to 500

## What Would Justify Pause Or Narrowing

Pause or narrow the pilot if:

- controlled launch details are incomplete
- raw evidence, screenshots, handles, URLs, credentials, browser data, or sensitive notes enter git
- collectors need unapproved context to make records useful
- redaction cannot be performed consistently
- OCR or screenshots contain too much unrelated personal data
- the source mix produces too many low-context or unreviewable items
- annotation disagreement repeats on the same primary-label boundary
- baseline review would expose item-level sensitive evidence or produce misleading claims

The default next action is still outside git: use the controlled launch record, keep controlled-store artifacts out of git, validate the controlled rehearsal records, record the rehearsal outcome in the repo-safe review note, and stop at the first 10-15 item checkpoint before any 50-item continuation.
