# Approved Placeholder Gate Check

## Objective

Verify that changing a manual rehearsal intake from `pending` to `approved` is not enough to generate a real record while unresolved placeholders remain.

This is a repo-safe gate check. It does not include raw Threads content, screenshots, URLs, handles, source identifiers, or stakeholder case details.

## Context

The user supplied:

```json
"authorization_status": "approved"
```

The local-only `data/interim/manual_entry_0001.json` was updated accordingly, but the intake still contained `FILL_*` placeholder values. A real record should not be generated from that state.

## Safety Patch

Added a real-item governance guard in:

```text
src/data_collection/governance_checks.py
```

The guard blocks real manual records that contain unresolved placeholder markers such as:

- `FILL_`
- `REPLACE_`
- `PENDING_`

Synthetic records are not affected by this real-item placeholder guard.

## Command

```bash
python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001_placeholder_gate.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv
```

## Result

| Check | Result |
|---|---|
| Expected failure occurred? | yes |
| Exit behavior | blocked by governance errors |
| Output record created? | no |
| Raw evidence touched? | no |
| Synthetic smoke test still passes? | yes |
| Before-item-1 preflight after check | `OK: 20`, `WARN: 1`, `ERROR: 0` |

Observed governance errors:

```text
real manual item contains unresolved placeholder in post_text
real manual item contains unresolved placeholder in metadata_notes
real manual item contains unresolved placeholder in privacy_redaction_notes
```

Synthetic smoke result:

```text
governance_errors: 0
governance_warnings: 0
schema_errors: 0
schema_warnings: 0
```

## Interpretation

The rehearsal gate now requires both:

1. controlled approval status, and
2. replacement of placeholder fields with approved, redacted manual evidence fields.

This prevents an accidental false start where a collector marks an intake as approved but leaves placeholder text in the record.

## Decision Implication

Current state:

```text
approved_placeholder_gate_verified_waiting_for_redacted_fields
```

Next action:

1. Collector replaces all `FILL_*` values in `data/interim/manual_entry_0001.json`.
2. Collector confirms fields are approved and redacted under the controlled launch record.
3. Build the rehearsal record again.
4. Run strict validation.
5. Complete local redaction and collection-log review before moving to the first 10-15 items.
