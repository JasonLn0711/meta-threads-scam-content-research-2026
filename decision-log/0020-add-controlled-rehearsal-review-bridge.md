# Decision 0020: Add Controlled Rehearsal Review Bridge

## Date

2026-04-23

## Decision

Add a required repo-safe review step after the first 1-2 controlled rehearsal items and before the first 10-15 item checkpoint.

The review must convert the rehearsal from a local operational activity into one explicit decision:

- `pass_ready_for_calibration_or_first_10_15`
- `pass_with_limits`
- a pause outcome
- `stop_source_for_pilot`

## Context

The repo already had:

- a controlled rehearsal work order
- a manual rehearsal checklist
- a boundary watchlist from synthetic calibration
- a first 10-15 item checkpoint protocol

What was missing was the bridge between them. Without that bridge, the workflow could drift from:

```text
rehearsal happened
```

to:

```text
start the first 10-15 items
```

without a durable, aggregate, non-sensitive decision record. That would make it too easy to skip burden review, redaction lessons, or repeated boundary failures discovered during the first real rehearsal items.

## Options Considered

1. Treat the manual rehearsal checklist as enough and move directly to the first 10-15 item checkpoint.
2. Wait and fold rehearsal findings into the first checkpoint only.
3. Add a short repo-safe rehearsal review bridge before the checkpoint.

## Rationale

Option 3 gives the cleanest operational spine.

It preserves a narrow decision gate that is:

- earlier than the first 10-15 item checkpoint
- aggregate-only and safe to commit
- specific enough to catch redaction burden, schema friction, and label-boundary failures
- compatible with manual, stakeholder-provided, API-authorized, and automation-assisted paths

## Consequences

- The first 1-2 rehearsal items now require a repo-safe review artifact before the first 10-15 item checkpoint begins.
- Core launch docs should route the team through:

```text
controlled launch details
-> local workspace
-> item-1 preflight
-> 1-2 item rehearsal
-> controlled rehearsal review
-> calibration if needed
-> first 10-15 item checkpoint
```

- Rehearsal outcomes now use explicit decision values instead of informal "looks okay" progression.
- If the rehearsal fails on redaction, schema, authorization, or repeated boundary confusion, the correct action is to pause before the first 10-15 item checkpoint.

## Follow-Up

Use:

- `templates/controlled_rehearsal_review.md`
- `experiments/evaluation-notes/0014-controlled-rehearsal-review-protocol.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_controlled_rehearsal_work_order.md`

Review this decision after the first real controlled rehearsal review is completed.
