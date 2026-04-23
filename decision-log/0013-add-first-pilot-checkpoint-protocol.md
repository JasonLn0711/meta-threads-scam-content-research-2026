# Decision 0013: Add First Pilot Checkpoint Protocol

## Date

2026-04-23

## Decision

Add a required first checkpoint after the first 10-15 real pilot items are collected or annotated.

The checkpoint must review collection safety, redaction, source mix, field completeness, early label distribution, second-review routing, and whether the pilot can safely continue to all 50 items.

## Context

The first real Threads pilot has been approved for `go_with_limits` launch preparation. The remaining pre-collection requirement is a controlled launch record with exact source, storage, access, retention, and redaction limits outside git.

Once collection begins, the riskiest mistake would be discovering privacy, redaction, source, or annotation problems only after all 50 pilot items have been collected. A 10-15 item checkpoint limits that risk.

## Options Considered

1. Proceed directly to all 50 items after controlled launch details are complete.
2. Check only after all 50 items are annotated.
3. Add a first 10-15 item checkpoint before completing the full pilot.

## Rationale

Option 3 gives the project the best balance of momentum and control. It is small enough to be practical, but early enough to catch:

- raw evidence storage mistakes
- screenshot, URL, handle, or OCR redaction failures
- missing required fields
- source skew
- label-boundary confusion
- overuse of `uncertain` or `insufficient_evidence`

## Consequences

- The pilot should pause after 10-15 items for checkpoint review.
- The checkpoint can decide `continue_to_50`, `continue_with_limits`, a specific pause, or `stop_pilot`.
- If collection or annotation problems repeat, the team must revise the launch record, collection SOP, annotation guide, or work order before continuing.
- No local raw data or generated pilot files should be committed.

## Follow-Up

Use:

- `docs/38-first-pilot-checkpoint-protocol.md`
- `templates/pilot_checkpoint_review.md`
- `experiments/dataset-audit/0003-first-checkpoint-audit-protocol.md`

Review this decision after the first checkpoint is completed.
