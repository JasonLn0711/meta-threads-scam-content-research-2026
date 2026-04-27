# Decision 0126: Record Track B Day 1 Batch 0001 Primary Review

## Status

accepted

## Date

2026-04-28

## Decision

Record the Track B primary review pass for batch `0001`.

This decision records repo-safe primary review of six checkpoint-derived seed replay candidates. It does not record final Track B labels because all six candidates require second review before final Track B adjudication.

## Batch

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0001_checkpoint_seed_replay` |
| Source arm | `checkpoint-derived seed replay` |
| Candidates surfaced | 6 |
| Candidates primary-reviewed | 6 |
| Accepted strict-valid records | 0 |
| Final Track B labels recorded | no |
| Second review required | yes: 6 of 6 |
| Related run | `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` |
| Report note | `reports/checkpoint-0081-track-b-day-1-batch-0001-primary-review.md` |
| Evaluation note | `experiments/evaluation-notes/0093-track-b-day-1-batch-0001-primary-review.md` |

## Primary Review Boundary

Primary review used existing checkpoint `0081` repo-safe summaries and signal-family references only.

No raw Threads URLs, handles, screenshots, raw post text, raw reply text, raw OCR text, contact IDs, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details were reviewed or added to git.

The prior checkpoint outcome is contextual input, not an automatic Track B final label.

## Primary Review Outcome

| Track B primary outcome | Count |
|---|---:|
| Initial `scam` / `high` pending second review | 4 |
| Initial `non_scam` / `low` hard-negative pending second review | 2 |
| Final Track B labels | 0 |
| Accepted strict-valid records | 0 |

## Stop-Rule Status

The batch triggers a stop-rule signal because second-review rate is 100%.

This is expected for a seed replay batch containing high-risk and hard-negative examples. The required action is to pause additional checkpoint-derived seed replay surfacing until second review records final Track B outcomes for batch `0001`.

| Stop dimension | Status |
|---|---|
| Raw evidence leakage | pass: none |
| Source cap pressure | pass: 6 of 30 checkpoint replay cap used |
| Total cap pressure | pass: 6 of 300 surfaced cap used |
| Human-review cap pressure | pass: 6 of 150 reviewed cap used |
| Duplicate pressure | pass: 0 duplicates by item-id replay dedupe |
| Insufficient-evidence pressure | pass: 0 primary-review insufficient evidence |
| Hard-negative FP pressure | pass: 0 primary-review hard-negative false-positive pressure |
| Second-review rate | stop signal: 6 of 6 require second review |
| Pause required | yes: pause further checkpoint seed replay surfacing until second review |

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

## Next Action

Run second review for batch `0001` before surfacing more checkpoint-derived seed replay candidates.
