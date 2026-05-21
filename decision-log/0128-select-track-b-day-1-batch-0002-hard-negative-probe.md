# Decision 0128: Select Track B Day 1 Batch 0002 Hard-Negative Probe

## Status

accepted

## Date

2026-04-28

## Decision

Select the `hard-negative probe arm` as Track B batch `0002`.

This decision records source-arm selection and batch planning only. It does not surface candidates, collect new evidence, create item `0082`, run browser/session work, build local Track B records, or validate new records.

## Rationale

Batch `0001` verified the checkpoint-derived seed replay workflow and closed its second-review pause condition. The next safest method-test step is not more checkpoint replay by habit. The next step should pressure-test false-positive protection before moving into larger live discovery arms such as the approved browser-session risk-probe matrix.

The hard-negative probe arm directly tests whether the signal-family method can avoid over-flagging:

- genuine anti-scam warning;
- ordinary investment discussion;
- financial education;
- general market commentary;
- personal investment journaling;
- legitimate finance creator content;
- public contact information without funnel behavior;
- educational chart or screenshot content;
- news discussion;
- market-risk warning content.

## Batch Plan

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0002_hard_negative_probe` |
| Selected source arm | `hard-negative probe arm` |
| Source-arm surfaced cap | 50 |
| Planned batch size | up to 10 surfaced candidates |
| Candidates surfaced by this decision | 0 |
| Candidates reviewed by this decision | 0 |
| Accepted strict-valid records by this decision | 0 |
| Related run | `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` |
| Report note | `reports/checkpoint-0081-track-b-day-1-batch-0002-hard-negative-probe-selection.md` |
| Evaluation note | `experiments/evaluation-notes/0095-track-b-day-1-batch-0002-hard-negative-probe-selection.md` |

## Required Candidate Boundary

Candidate surfacing for batch `0002` must use repo-safe candidate notes only.

Each surfaced candidate must preserve the hard-negative contrast being tested and must avoid raw Threads URLs, handles, screenshots, raw post text, raw reply text, raw OCR text, contact IDs, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details in git-facing output.

## Stop-Rule Baseline

The hard-negative probe arm is specifically monitored for hard-negative false-positive pressure.

| Stop dimension | Batch `0002` baseline |
|---|---|
| Raw evidence leakage | must remain 0 |
| Hard-negative false-positive pressure | measured from first reviewed candidate |
| Duplicate pressure | measured from surfaced candidates |
| Insufficient-evidence pressure | measured from primary review |
| Reviewer burden | measured from primary review |
| Source-arm cap pressure | hard-negative probe arm cap is 50; planned batch size up to 10 |

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
- candidate surfacing outside the locked Track B source arms and caps.

## Next Action

Surface batch `0002` hard-negative probe candidates only under this selected source arm and the locked Track B boundary.
