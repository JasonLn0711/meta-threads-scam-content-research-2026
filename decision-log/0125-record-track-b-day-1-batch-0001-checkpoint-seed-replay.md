# Decision 0125: Record Track B Day 1 Batch 0001 Checkpoint Seed Replay

## Status

accepted

## Date

2026-04-28

## Decision

Record the first Track B Day 1 surfaced candidate batch under the `checkpoint-derived seed replay` source arm.

This decision surfaces repo-safe checkpoint-derived candidate references only. It does not record Track B human review, second review, accepted strict-valid records, new Threads evidence collection, or item `0082`.

## Batch

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0001_checkpoint_seed_replay` |
| Date bucket | `2026-04-28` |
| Source arm | `checkpoint-derived seed replay` |
| Candidates surfaced in batch | 6 |
| Candidates human-reviewed in batch | 0 |
| Accepted strict-valid records in batch | 0 |
| Candidate status | `surfaced_pending_track_b_review` |
| Related run | `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` |
| Report note | `reports/checkpoint-0081-track-b-day-1-batch-0001-checkpoint-seed-replay.md` |
| Evaluation note | `experiments/evaluation-notes/0092-track-b-day-1-batch-0001-checkpoint-seed-replay.md` |

## Scope

The batch uses existing checkpoint `0081` repo-safe references to replay signal families into the Track B source-arm ledger.

This batch includes:

- four prior checkpoint high-risk signal-family examples;
- two prior checkpoint hard-negative comparator examples.

The prior checkpoint outcomes are context only. Track B review labels, risk values, reviewer time, second-review outcomes, and strict-valid record acceptance remain pending.

## Source-Arm Counter Update

| Source arm | Surfaced cap | Surfaced before batch | Surfaced in batch | Surfaced after batch | Remaining surfaced cap |
|---|---:|---:|---:|---:|---:|
| Checkpoint-derived seed replay | 30 | 0 | 6 | 6 | 24 |
| Total Track B surfaced candidates | 300 | 0 | 6 | 6 | 294 |

Human-reviewed candidates remain `0` of `150`.

Accepted strict-valid records remain `0` of `75`.

## Daily Stop-Rule Check

| Field | Value |
|---|---|
| `date_bucket` | `2026-04-28` |
| `surfaced_today` | 6 |
| `reviewed_today` | 0 |
| `duplicates_today` | 0 by checkpoint item-id replay dedupe |
| `insufficient_evidence_today` | n/a until Track B review |
| `hard_negative_fp_pressure_today` | n/a until Track B review |
| `average_review_time_today` | n/a |
| `second_review_rate_today` | n/a |
| `reviewer_disagreement_today` | n/a |
| `raw_evidence_leak` | no |
| `stop_rule_triggered` | no |
| `pause_required` | no |

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
