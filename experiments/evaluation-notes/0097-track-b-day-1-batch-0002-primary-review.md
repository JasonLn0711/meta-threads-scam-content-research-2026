# Track B Day 1 Batch 0002 Primary Review

## Purpose

Record the evaluation note for Track B batch `0002` primary review.

This note is repo-safe. It contains no raw Threads content, full item URLs, raw handles, raw contact IDs, screenshots, raw post text, raw reply text, raw OCR text, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details.

## Review Summary

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0002_hard_negative_probe` |
| Source arm | `hard-negative probe arm` |
| Review pass | primary review |
| Candidates surfaced | 10 |
| Candidates primary-reviewed | 10 |
| Final Track B labels | 0 |
| Accepted strict-valid records | 0 |
| Second review required | 10 |
| Report note | `reports/checkpoint-0081-track-b-day-1-batch-0002-primary-review.md` |
| Decision | `decision-log/0130-record-track-b-day-1-batch-0002-primary-review.md` |

## Primary Review Distribution

| Primary-review category | Count |
|---|---:|
| Initial non_scam/low hard-negative | 10 |
| Initial scam/high | 0 |
| Initial uncertain | 0 |
| Initial insufficient evidence | 0 |
| Duplicate | 0 |

## Reviewer Burden

| Metric | Value |
|---|---:|
| Total primary-review minutes | 20 |
| Average primary-review minutes | 2.0 |
| Human-reviewed cap used | 16 of 150 |

Review time is for repo-safe hard-negative probe review only. It is not a live raw-evidence inspection time.

## Stop-Rule Interpretation

Second-review rate is `100%`, above the normal concern threshold.

For this batch, the high rate is expected because all ten candidates are hard-negative probe candidates and hard-negative flags require second review.

Required action:

```text
pause further hard-negative probe surfacing until batch 0002 second review is complete
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

The hard-negative probe arm is now measuring the method's ability to resist false positives. At primary review, the method preserves all ten hard-negative candidates as initial `non_scam` / `low`.

The next useful result is second review for these ten candidates, because that will test whether hard-negative protection survives independent review.

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
