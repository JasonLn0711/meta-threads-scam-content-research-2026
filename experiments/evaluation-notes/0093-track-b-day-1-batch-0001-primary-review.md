# Track B Day 1 Batch 0001 Primary Review

## Purpose

Record the evaluation note for Track B batch `0001` primary review.

This note is repo-safe. It contains no raw Threads content, full item URLs, raw handles, raw contact IDs, screenshots, raw post text, raw reply text, raw OCR text, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details.

## Review Summary

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0001_checkpoint_seed_replay` |
| Source arm | `checkpoint-derived seed replay` |
| Review pass | primary review |
| Candidates surfaced | 6 |
| Candidates primary-reviewed | 6 |
| Final Track B labels | 0 |
| Accepted strict-valid records | 0 |
| Second review required | 6 |
| Report note | `reports/checkpoint-0081-track-b-day-1-batch-0001-primary-review.md` |
| Decision | `decision-log/0126-record-track-b-day-1-batch-0001-primary-review.md` |

## Primary Review Distribution

| Primary-review category | Count |
|---|---:|
| Initial scam/high | 4 |
| Initial non_scam/low hard-negative | 2 |
| Initial uncertain | 0 |
| Initial insufficient evidence | 0 |
| Duplicate | 0 |

## Reviewer Burden

| Metric | Value |
|---|---:|
| Total primary-review minutes | 16 |
| Average primary-review minutes | 2.7 |
| Human-reviewed cap used | 6 of 150 |

Review time is for repo-safe checkpoint replay review only. It is not a live raw-evidence inspection time.

## Stop-Rule Interpretation

Second-review rate is `100%`, above the normal concern threshold.

For this batch, the high rate is expected because:

- four replay candidates are high-risk signal-family examples; and
- two replay candidates are hard-negative comparator examples.

Required action:

```text
pause further checkpoint-derived seed replay surfacing until batch 0001 second review is complete
```

Other stop dimensions remain within bounds:

| Stop dimension | Status |
|---|---|
| Raw evidence leakage | pass |
| Duplicate pressure | pass |
| Insufficient-evidence pressure | pass |
| Hard-negative FP pressure | pass at primary review |
| Average review time | pass |
| Source cap pressure | pass |
| Candidate cap pressure | pass |

## Method Lesson

Checkpoint replay is useful for testing whether the Track B review worksheet can hold known signal-family patterns and hard negatives. It is not a live discovery-yield measure.

The next useful result is not another surfaced batch. The next useful result is second review for these six candidates, because that will test disagreement handling, hard-negative protection, and final Track B review outcome recording.

## Non-Authorizations

This note does not authorize:

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
