# Manual Rehearsal Intake Gate Check

## Objective

Verify that the manual collection assistant blocks an incomplete real-item rehearsal payload before any item-level record is built.

This is a repo-safe gate check. It does not include raw Threads content, screenshots, URLs, handles, source identifiers, or stakeholder case details.

## Context

The outside-git controlled launch record has been confirmed with final status `ready_for_first_10_15_items`.

The local-only workspace has been initialized under ignored `data/interim/`, and before-item-1 preflight has passed with `ERROR: 0`.

The next governed step is 1-2 manual rehearsal records. Before filling real approved fields, the placeholder intake should be unable to produce a real record.

## Command

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001_gate_test.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv
```

## Result

| Check | Result |
|---|---|
| Expected failure occurred? | yes |
| Exit behavior | blocked by governance error |
| Output record created? | no |
| Local collection log row created? | no |
| Raw evidence touched? | no |
| Repo preflight after check | `OK: 20`, `WARN: 1`, `ERROR: 0` |

Observed governance error:

```text
real manual items must use authorization_status='approved'
```

## Interpretation

The assistant correctly refuses to transform a `pending` real manual payload into a schema record.

This protects the pilot from a common failure mode: preparing a placeholder intake file, forgetting to complete controlled review, and accidentally generating item-level records as if the item were approved.

## Decision Implication

Current state:

```text
manual_rehearsal_gate_verified_waiting_for_approved_fields
```

Next action:

1. Collector fills `data/interim/manual_entry_0001.json` with approved, redacted fields only.
2. Collector changes `authorization_status` from `pending` to `approved` only after controlled review.
3. Build the local rehearsal record.
4. Run strict validation.
5. Review redaction and collection burden before any move to 10-15 items.

Do not proceed to the first 10-15 items until at least one rehearsal record passes governance, schema validation, and redaction review.
