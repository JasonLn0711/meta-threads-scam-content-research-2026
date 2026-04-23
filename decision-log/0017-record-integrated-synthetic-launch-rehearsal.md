# Decision 0017: Record Integrated Synthetic Launch Rehearsal

## Date

2026-04-23

## Decision

Record the integrated Phase 1 synthetic launch rehearsal as completed, while preserving the blocker that no real Threads pilot item may be collected until the controlled launch record is complete outside git.

The rehearsal confirms only that the local tooling path can execute on synthetic fixtures. It does not authorize real collection, scraping, live ingestion, production scoring, Phase 2 work, or expansion beyond the first real checkpoint.

## Context

Phase 1 now has governance posture, schema, annotation guidance, local workspace tooling, manual collection assistant checks, calibration utilities, audit tooling, rule-baseline tooling, review packets, and synthesis tooling.

The next risk was operational: the repo could contain the right pieces but still fail to run as a governed launch bridge. A synthetic-only integrated rehearsal exercised that bridge without touching live Threads content or storing real evidence.

The rehearsal is documented in `experiments/evaluation-notes/0008-phase1-synthetic-launch-rehearsal.md`.

## Options Considered

1. Treat the synthetic rehearsal as enough to start the 50-item pilot.
2. Treat the synthetic rehearsal as a tooling check only and keep the controlled-launch and first-checkpoint gates.
3. Skip a decision record and leave the result only in evaluation notes.

## Rationale

Option 2 is the only option consistent with the project boundaries.

The rehearsal showed that the scripts can produce and inspect local artifacts using synthetic inputs, but it did not answer the real Phase 1 questions:

- whether exact source, storage, access, retention, redaction, screenshot, OCR, URL/link, and handle/contact rules are complete
- whether real collection burden is manageable
- whether real redaction quality is acceptable
- whether real annotator disagreement is stable enough
- whether OCR, reply/comment context, and visible link/handle signals are useful without unapproved context
- whether the first 10-15 real items justify continuing to 50

## Consequences

- The repo can proceed to the next human-controlled launch step, not to real collection by default.
- The controlled launch record remains outside git if it contains sensitive source, storage, access, or investigative details.
- The immediate next commands after controlled launch completion are still:

```bash
python scripts/init_pilot_workspace.py --ack-controlled-details
python scripts/check_pilot_preflight.py --before-item-1 --ack-controlled-details
```

- The first real governed checkpoint remains mandatory after 10-15 items.
- The 50-item pilot remains conditional on the checkpoint decision.
- Phase 2, automation, scraping, live ingestion, and production scoring remain out of scope.

## Follow-Up

Human owner:

- Complete the controlled launch record outside git.
- Confirm raw storage, access, retention, and redaction rules.
- Confirm collector, annotator, reviewer, adjudicator, and research engineer IDs.

Codex after the human-controlled launch record is complete:

- Initialize the local pilot workspace.
- Run item-1 preflight.
- Support the 1-2 item manual collection rehearsal without committing local evidence.

Review this decision after the first 10-15 item checkpoint.
