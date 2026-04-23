# Controlled Rehearsal Review Protocol

## Objective

Turn the first 1-2 controlled real rehearsal items into a repo-safe decision record before the first 10-15 item checkpoint begins.

This protocol exists because the rehearsal checklist is item-level and operational, while the checkpoint protocol is batch-level and comes later. The team needs one short aggregate review in between so the first real rehearsal becomes a decision, not just an activity.

This note is repo-safe. It must not contain raw Threads content, screenshots, source URLs, handles, case IDs, credentials, run-record details, raw storage paths, or sensitive investigative material.

## Research Question

Can the approved manual, stakeholder-provided, API-authorized, or automation-assisted path produce redacted, schema-valid local records without:

- governance failure
- redaction failure
- repeated finance or OCR boundary confusion
- pseudo-official tag overreach
- demand for unapproved context

## Hypothesis

The first 1-2 controlled rehearsal items should be enough to reveal whether the launch path is ready for:

- `pass_ready_for_calibration_or_first_10_15`
- `pass_with_limits`

If the rehearsal instead produces repeated boundary confusion, redaction issues, or unapproved-context pressure, the correct outcome is a pause rather than a quiet move into the first 10-15 item checkpoint.

## Data Slice

Maximum slice:

- 1-2 approved real rehearsal items only
- approved fields only
- controlled launch record already completed outside git
- raw evidence outside git only

Do not treat this review as a mini-checkpoint, prevalence sample, or baseline dataset.

## Required Inputs

- `governance/pilot-launch/threads_pilot_v1_2026-05_controlled_rehearsal_work_order.md`
- `templates/manual_collection_rehearsal_checklist.md`
- `templates/controlled_rehearsal_review.md`
- `experiments/evaluation-notes/0013-controlled-rehearsal-boundary-watchlist.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_guideline_revision_log.md`
- `docs/40-pilot-preflight-verification.md`

## Method

1. Confirm the controlled launch record is complete outside git and the local workspace already exists.
2. Run or confirm `scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details` with `ERROR: 0`.
3. Build 1-2 local rehearsal records under the approved controlled path.
4. Run strict validation on each rehearsal record.
5. Review the local collection log and the completed manual rehearsal checklist.
6. Apply the boundary watchlist for finance-without-funnel, OCR sufficiency, pseudo-official wording, and confidence interpretation.
7. Fill `templates/controlled_rehearsal_review.md` with aggregate-only findings.
8. Record exactly one rehearsal decision before the first 10-15 item checkpoint begins.

## Suggested Local Commands

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

If a second rehearsal item is used, repeat the same flow for `manual_entry_0002.json`.

## Cost To Record

This review should explicitly record:

- collector time
- governance review time
- annotation lead review time
- research engineer time
- redaction burden
- number of unclear or missing fields

The first real rehearsal is partly a burden-measurement exercise. If the work is too expensive or confusing at 1-2 items, it will not get better by pretending the first 10-15 item checkpoint has already started.

## Decision Values

Choose exactly one:

- `pass_ready_for_calibration_or_first_10_15`
- `pass_with_limits`
- `pause_for_redaction_fix`
- `pause_for_schema_or_guideline_fix`
- `pause_for_authorization_review`
- `stop_source_for_pilot`

## Decision Rules

Use `pass_ready_for_calibration_or_first_10_15` when:

- strict validation passes
- raw evidence stayed outside git
- redaction works consistently
- no blocking governance issue appears
- no repeated boundary-watch failure appears
- no unapproved context is needed

Use `pass_with_limits` when:

- the rehearsal is basically usable
- one or more extra limits are needed before the first 10-15 item checkpoint
- those limits can be enforced immediately without changing the research question

Use `pause_for_redaction_fix` when:

- screenshots, URLs, handles, OCR, or related notes cannot be redacted consistently

Use `pause_for_schema_or_guideline_fix` when:

- approved evidence does not fit the schema cleanly
- the same label boundary fails repeatedly
- the team cannot explain how to write evidence-based notes without improvising

Use `pause_for_authorization_review` when:

- the collector or reviewer needs profile, landing-page, redirect, destination, or automation context that the controlled launch record did not approve

Use `stop_source_for_pilot` when:

- the approved source category is too unsafe, too low-context, or too burdensome to continue in the current pilot

## Decision Implications

If the decision is `pass_ready_for_calibration_or_first_10_15`:

- rerun the 5-item calibration only if annotators changed
- otherwise proceed to `docs/38-first-pilot-checkpoint-protocol.md`

If the decision is `pass_with_limits`:

- write the new limit into the relevant launch or SOP artifact before item 3
- then start the first 10-15 item checkpoint under that narrower scope

If the decision is any pause or stop:

- do not start the first 10-15 item checkpoint
- update the relevant guideline, SOP, schema, or authorization artifact first
- resume only after the project owner records the revised launch condition

## Commit Boundary

Commit only:

- this protocol
- the filled aggregate review note if it is fully non-sensitive
- related non-sensitive guideline or process updates

Do not commit:

- local rehearsal inputs or outputs
- collection logs with item-level details
- screenshots
- URLs or handles
- run-record identifiers or storage details
- item-level disagreement notes
