# Decision 0021: Record CIB-Approved Rehearsal Intake Readiness

## Date

2026-04-24

## Decision

Record the controlled rehearsal intake gate as `ready_for_controlled_item_entry`.

CIB approval is treated as complete for the current controlled pilot path. This replaces the earlier local wording that described the gate as `pause_for_authorization_review`.

The project still may not move into the first 10-15 item checkpoint until exactly one controlled rehearsal item is entered in redacted form, built into `manual_record_0001.json`, and strict-validated.

## Context

The repo-side preparation is complete enough to receive the first controlled rehearsal item:

- CIB approval for the current controlled pilot path is recorded in Decision 0018 and reaffirmed by the project owner
- local pilot workspace files exist under ignored `data/interim/`
- before-item-1 preflight has passed with zero errors
- local-only `manual_entry_0001.json` exists as an intake skeleton
- local-only item-selection worksheet exists and records that no specific item has been selected yet
- local checklist and aggregate review draft exist
- manual collection tooling is available through the local `.venv`

No raw Threads content, screenshots, source URLs, handles, credentials, run records, storage paths, or sensitive source details were copied into git.

The remaining blocker is not CIB approval. The blocker is operational: one selected controlled rehearsal item has not yet been entered into the local intake file. The builder correctly refuses the skeleton because `item_id` is blank.

## Options Considered

1. Move directly to the first 10-15 item checkpoint because CIB approval, workspace setup, and preflight are ready.
2. Fill a synthetic or placeholder item to exercise the real rehearsal decision path.
3. Mark the intake gate as CIB-approved and ready for controlled item entry, while keeping the first checkpoint blocked until one real rehearsal record is built and validated.

## Rationale

Option 3 preserves both facts:

- approval is not the blocker
- a real controlled item still has to prove the collection, redaction, validation, and review path

The first 10-15 item checkpoint is supposed to review real operational quality:

- whether approved fields are enough
- whether redaction works in practice
- whether collection burden is measurable
- whether boundary-watch issues appear
- whether the collector needs any context beyond the approved controlled path

None of those can be learned from an empty intake skeleton or a synthetic substitute. Advancing anyway would turn the checkpoint into process theater and make later baseline claims weaker.

## Consequences

- The current intake status is `ready_for_controlled_item_entry`.
- The next action is local and controlled: select exactly one CIB-approved rehearsal item and enter only approved redacted fields in `data/interim/manual_entry_0001.json`.
- `data/interim/manual_entry_0001.json` must remain local-only.
- The builder and strict validator must pass before the rehearsal can be reviewed.
- The local checklist and aggregate review draft must be updated after the controlled item is processed.
- The first 10-15 item checkpoint remains blocked until the rehearsal decision becomes `pass_ready_for_calibration_or_first_10_15` or `pass_with_limits`.

## Follow-Up

Before the first 10-15 item checkpoint:

1. Select exactly one CIB-approved controlled rehearsal item.
2. Update `data/interim/manual_entry_0001_selection_record.md` locally without copying raw evidence or sensitive details into git.
3. Fill `data/interim/manual_entry_0001.json` with only approved redacted fields.
4. Run:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

5. Review the local checklist.
6. Update the aggregate rehearsal review.
7. Record one of:

- `pass_ready_for_calibration_or_first_10_15`
- `pass_with_limits`
- a pause outcome
- `stop_source_for_pilot`

Review this decision after the first real controlled rehearsal item is built and validated.
