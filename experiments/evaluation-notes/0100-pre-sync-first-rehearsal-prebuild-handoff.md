# First Rehearsal Prebuild Handoff

Historical note: this was a local pre-sync handoff note originally drafted before the repository was fast-forwarded to the current `origin/main` state on `2026-05-04`. It is retained as a repo-safe audit note, but the active evaluation-note sequence has since advanced beyond the first controlled rehearsal build.

## Objective

Prepare the collector-facing prebuild handoff for the first 1-2 controlled rehearsal records before the first 10-15 item checkpoint.

This note is repo-safe. It does not contain raw Threads content, screenshots, source URLs, handles, case IDs, credentials, raw storage paths, access lists, or sensitive investigative details.

## Why This Step Exists

The previous readiness check identified the remaining blocker: `data/interim/manual_entry_0001.json` still needs approved, redacted, non-placeholder values from one selected item. Controlled crawler rehearsal run 0001 also confirmed that no extractable item was available from the first static seed path. The next practical research risk is not schema validation. It is the handoff from collector or operator judgment to a local JSON payload once a selected item exists.

That handoff needs its own lightweight checklist because a generated schema-valid record can still be operationally wrong if the input:

- carries placeholder text
- stores raw identifiers
- uses unapproved source or context fields
- copies full URLs or handles
- includes OCR or screenshot text beyond the approved evidence slice
- forces the collector to rely on profile, account, landing-page, redirect-chain, or automation context

The new prebuild handoff makes those risks explicit before the builder runs.

## Artifact Added

| File | Purpose |
|---|---|
| `templates/manual_collection_prebuild_handoff.md` | Local-only collector/operator and governance-reviewer handoff before building `manual_record_0001.json`. |

Completed copies should stay local-only if they contain item-level evidence or operational source details.

## Workflow Position

Use this sequence for the first rehearsal item:

1. Collector or approved operator selects one item under the controlled launch and run-record limits.
2. Collector fills `data/interim/manual_entry_0001.json` with approved, redacted, non-placeholder values.
3. Collector and governance reviewer complete `templates/manual_collection_prebuild_handoff.md` locally.
4. Research engineer runs the manual record builder.
5. Research engineer runs strict validation on the generated local record.
6. Collector and reviewer complete `templates/manual_collection_rehearsal_checklist.md` locally.

The prebuild handoff is before record generation. The rehearsal checklist is after record generation.

## Current Decision

Current decision: `prebuild_handoff_ready_waiting_for_selected_item`

Reason:

- outside-git controlled launch confirmation has been received
- local-only pilot workspace exists under ignored `data/interim/`
- before-item-1 preflight has passed with `ERROR: 0`
- placeholder and pending-authorization gates are verified
- controlled crawler rehearsal run 0001 did not produce an extractable selected item
- the redacted-field readiness check identified the required intake values once a selected item exists
- the prebuild handoff template now gives the collector/operator and reviewer a concrete local checklist before the builder runs
- no real Threads evidence has been collected, generated, or committed as part of this step

## Next Action

After an approved path produces one selected item, the collector should update `data/interim/manual_entry_0001.json` locally and complete a local copy of `templates/manual_collection_prebuild_handoff.md`.

Only after the handoff decision is `ready_to_build_rehearsal_record`, run:

```bash
.venv/bin/python scripts/build_manual_collection_record.py data/interim/manual_entry_0001.json \
  --ack-controlled-details \
  --output data/interim/manual_record_0001.json \
  --collection-log data/interim/threads_pilot_v1_collection_log.csv

.venv/bin/python scripts/validate_thread_dataset.py data/interim/manual_record_0001.json --strict
```

If the handoff pauses, record the blocker locally and do not move to the first 10-15 item checkpoint.

## Commit Boundary

Commit only this aggregate note, the blank template, and index or doc references.

Do not commit:

- completed handoff copies with item-level evidence
- local-only files under `data/interim/`
- raw evidence or screenshots
- source URLs, handles, case IDs, or stakeholder case material
- generated real records or collection logs
