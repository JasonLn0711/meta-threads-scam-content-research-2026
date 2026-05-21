# Decision 0129: Record Track B Day 1 Batch 0002 Hard-Negative Probe Candidates

## Status

accepted

## Date

2026-04-28

## Decision

Record candidate surfacing for Track B batch `0002` under the `hard-negative probe arm`.

This decision surfaces ten repo-safe hard-negative probe candidates for later primary review. It does not review, label, adjudicate, validate, or accept any Track B record.

## Batch

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0002_hard_negative_probe` |
| Source arm | `hard-negative probe arm` |
| Planned batch size | up to 10 surfaced candidates |
| Candidates surfaced | 10 |
| Candidates reviewed | 0 |
| Final Track B review outcomes recorded | no |
| Accepted strict-valid records | 0 |
| Related run | `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` |
| Report note | `reports/checkpoint-0081-track-b-day-1-batch-0002-hard-negative-probe-candidates.md` |
| Evaluation note | `experiments/evaluation-notes/0096-track-b-day-1-batch-0002-hard-negative-probe-candidates.md` |

## Candidate Scope

The ten candidates are repo-safe hard-negative probe aliases. They are designed to test false-positive pressure against investment-adjacent but non-scam or potentially benign surfaces.

No raw Threads URLs, handles, screenshots, raw post text, raw reply text, raw OCR text, contact IDs, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details were added to git.

## Candidate Distribution

| Hard-negative contrast type | Count |
|---|---:|
| Genuine anti-scam warning | 1 |
| Ordinary investment discussion | 1 |
| Financial education | 1 |
| General market commentary | 1 |
| Personal investment journaling | 1 |
| Legitimate finance creator content | 1 |
| Public contact information without funnel behavior | 1 |
| Educational chart or screenshot content | 1 |
| News discussion | 1 |
| Market-risk warning content | 1 |

## Stop-Rule Status

No stop rule is triggered by this candidate surfacing step.

| Stop dimension | Status |
|---|---|
| Raw evidence leakage | pass: none |
| Source cap pressure | pass: 10 of 50 hard-negative probe cap used |
| Total cap pressure | pass: 16 of 300 surfaced cap used |
| Human-review cap pressure | pass: 6 of 150 reviewed cap used |
| Duplicate pressure | pass at candidate-alias surfacing; primary review still required |
| Insufficient-evidence pressure | not measured until primary review |
| Hard-negative FP pressure | not measured until primary review |
| Reviewer burden | not measured until primary review |
| Pause required | no |

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

Run primary review for batch `0002` and measure hard-negative false-positive pressure, evidence completeness, reviewer burden, and second-review triggers.
