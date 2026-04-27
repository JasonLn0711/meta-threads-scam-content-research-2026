# Decision 0123: Record Track B Day 0 Start

## Status

accepted

## Date

2026-04-27

## Decision

Record Track B Day 0 operational start under decision `0122`.

This decision records gate confirmation and local-only workspace readiness. It does not authorize any activity outside the locked Track B boundary.

## Scope

Track B is a capped live investment-scam candidate-discovery method test.

Day 0 records:

- formal signoff was complete;
- the Track B run record is open;
- the local-only workspace directory exists under ignored `data/interim/track_b/`;
- validation and raw-evidence exclusion targets are ready;
- no candidates were surfaced, reviewed, accepted, or validated during Day 0.

## Related Artifacts

| Artifact | Purpose |
|---|---|
| `decision-log/0122-record-track-b-start-authorization-after-formal-signoff.md` | Start authorization after formal signoff. |
| `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` | Repo-safe Track B run record. |
| `experiments/evaluation-notes/0090-track-b-day-0-start-record.md` | Day 0 evaluation/start note. |
| `reports/checkpoint-0081-track-b-day-0-start-record.md` | Report-facing Day 0 start record. |

## Locked Caps

| Cap | Value |
|---|---:|
| Surfaced candidates | 300 |
| Human-reviewed candidates | 150 |
| Accepted strict-valid records | 75 |
| Intake window | 14 calendar days |

| Source arm | Surfaced candidate cap |
|---|---:|
| Checkpoint-derived seed replay | 30 |
| Reviewer-supplied candidates | 30 |
| Approved browser-session risk-probe matrix | 110 |
| Reply/comment funnel cue candidates | 60 |
| OCR/image-cue candidates | 20 |
| Hard-negative probe arm | 50 |

No overflow queue is allowed.

## Day 0 Result

| Metric | Value |
|---|---:|
| Candidates surfaced | 0 |
| Candidates human-reviewed | 0 |
| Accepted strict-valid records | 0 |
| Stop-rule triggers | 0 |

## Next Action

Proceed to Day 1 source-arm intake only under the run record and locked caps.

Every candidate must remain repo-safe in git-facing outputs and must be checked through dedupe, evidence completeness, reviewer-time measurement, second-review triggers, hard-negative protection, and daily stop-rule checks.

## Non-Authorizations

This decision does not authorize:

- item `0082`;
- open-ended collection;
- broad crawler/browser expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture;
- model or embedding training;
- production detector claims;
- legal fraud determinations;
- automated enforcement;
- public release;
- raw evidence in git;
- any activity outside the locked Track B caps.
