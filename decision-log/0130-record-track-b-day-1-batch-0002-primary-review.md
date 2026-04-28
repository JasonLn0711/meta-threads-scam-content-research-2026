# Decision 0130: Record Track B Day 1 Batch 0002 Primary Review

## Status

accepted

## Date

2026-04-28

## Decision

Record primary review for Track B batch `0002` under the `hard-negative probe arm`.

This decision records repo-safe primary review of ten hard-negative probe candidates. It does not record final Track B labels because all ten candidates require second review before final Track B adjudication.

## Batch

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0002_hard_negative_probe` |
| Source arm | `hard-negative probe arm` |
| Candidates surfaced | 10 |
| Candidates primary-reviewed | 10 |
| Accepted strict-valid records | 0 |
| Final Track B labels recorded | no |
| Second review required | yes: 10 of 10 |
| Related run | `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` |
| Report note | `reports/checkpoint-0081-track-b-day-1-batch-0002-primary-review.md` |
| Evaluation note | `experiments/evaluation-notes/0097-track-b-day-1-batch-0002-primary-review.md` |

## Primary Review Boundary

Primary review used repo-safe hard-negative candidate aliases and contrast categories only.

No raw Threads URLs, handles, screenshots, raw post text, raw reply text, raw OCR text, contact IDs, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details were reviewed or added to git.

The hard-negative contrast type is contextual input, not an automatic final Track B label.

## Primary Review Outcome

| Track B primary outcome | Count |
|---|---:|
| Initial `non_scam` / `low` hard-negative pending second review | 10 |
| Initial `scam` / `high` | 0 |
| Initial `uncertain` | 0 |
| Initial `insufficient_evidence` | 0 |
| Final Track B labels | 0 |
| Accepted strict-valid records | 0 |

## Stop-Rule Status

The batch triggers a stop-rule signal because second-review rate is 100%.

This is expected for a hard-negative probe batch because hard-negative flags require second review. The required action is to pause additional hard-negative probe surfacing until second review records final Track B outcomes for batch `0002`.

| Stop dimension | Status |
|---|---|
| Raw evidence leakage | pass: none |
| Source cap pressure | pass: 10 of 50 hard-negative probe cap used |
| Total cap pressure | pass: 16 of 300 surfaced cap used |
| Human-review cap pressure | pass: 16 of 150 reviewed cap used |
| Duplicate pressure | pass: 0 duplicates by candidate-alias dedupe |
| Insufficient-evidence pressure | pass: 0 primary-review insufficient evidence |
| Hard-negative FP pressure | pass: 0 primary-review hard-negative false-positive pressure |
| Second-review rate | stop signal: 10 of 10 require second review |
| Pause required | yes: pause further hard-negative probe surfacing until second review |

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

Run second review for batch `0002` before surfacing more hard-negative probe candidates.
