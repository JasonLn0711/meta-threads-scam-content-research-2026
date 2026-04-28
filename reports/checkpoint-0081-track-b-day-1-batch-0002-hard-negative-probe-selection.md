# Checkpoint 0081 Track B Day 1 Batch 0002 Hard-Negative Probe Selection

## Purpose

Record source-arm selection for Track B batch `0002`.

This note contains no raw Threads content, full item URLs, raw handles, raw contact IDs, screenshots, raw post text, raw reply text, raw OCR text, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details.

## Selection Status

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0002_hard_negative_probe` |
| Date bucket | `2026-04-28` |
| Track | `track_b_capped_live_method_test` |
| Source arm | `hard-negative probe arm` |
| Selection status | `candidate_surfacing_recorded` |
| Planned surfaced candidates | up to 10 |
| Candidates surfaced | 10 |
| Candidates reviewed | 0 |
| Accepted strict-valid records | 0 |
| Related decision | `decision-log/0128-select-track-b-day-1-batch-0002-hard-negative-probe.md` |
| Run record | `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` |
| Evaluation note | `experiments/evaluation-notes/0095-track-b-day-1-batch-0002-hard-negative-probe-selection.md` |
| Raw evidence in git | no |

## Current Surfacing Update

Candidate surfacing is now recorded in:

```text
reports/checkpoint-0081-track-b-day-1-batch-0002-hard-negative-probe-candidates.md
```

Candidate surfacing outcome:

```text
surfaced: 10
reviewed: 0
accepted strict-valid records: 0
primary review status: pending
```

## Why This Source Arm Is Next

Batch `0001` showed that the review workflow can carry checkpoint-derived high-risk and hard-negative replay examples through primary review, second review, and final review outcome recording.

Batch `0002` should now test the most important protection before larger live discovery arms: whether the method can avoid false-positive pressure against legitimate or non-scam investment-adjacent content.

## Hard-Negative Probe Targets

Batch `0002` should prefer hard-negative contrast types that are likely to be over-flagged by a naive investment-scam signal method:

| Hard-negative type | Why it matters |
|---|---|
| Genuine anti-scam warning | Protects warning content from being mistaken for scam content. |
| Ordinary investment discussion | Protects finance vocabulary that lacks a funnel. |
| Financial education | Protects educational content from teacher/advisor overreach. |
| General market commentary | Protects market analysis without individualized conversion. |
| Personal investment journaling | Protects ordinary self-reporting without recruitment. |
| Legitimate finance creator content | Protects creator content when no funnel is visible. |
| Public contact information without funnel behavior | Separates public contact presence from private-channel migration. |
| Educational chart or screenshot content | Protects images that are explanatory rather than profit-proof lures. |
| News discussion | Protects current-event discussion from investment-domain overflagging. |
| Market-risk warning content | Protects cautionary content from scam-like vocabulary matching. |

## Source-Arm Counter Plan

| Source arm | Surfaced cap | Surfaced before batch | Planned batch size | Surfaced after this selection | Remaining surfaced cap |
|---|---:|---:|---:|---:|---:|
| Checkpoint-derived seed replay | 30 | 6 | 0 | 6 | 24 |
| Reviewer-supplied candidates | 30 | 0 | 0 | 0 | 30 |
| Approved browser-session risk-probe matrix | 110 | 0 | 0 | 0 | 110 |
| Reply/comment funnel cue candidates | 60 | 0 | 0 | 0 | 60 |
| OCR/image-cue candidates | 20 | 0 | 0 | 0 | 20 |
| Hard-negative probe arm | 50 | 0 | up to 10 | 10 | 40 |
| Total | 300 | 6 | up to 10 planned | 16 | 284 |

The later candidate-surfacing record consumes 10 surfaced slots from the hard-negative probe arm cap.

## Candidate Surfacing Rules For Batch 0002

Each surfaced candidate must record:

- candidate unit;
- source arm;
- hard-negative contrast type;
- signal families that might create false-positive pressure;
- evidence completeness score;
- dedupe status;
- primary review time;
- hard-negative flag;
- second-review trigger;
- repo-safe notes only.

Each surfaced candidate must avoid:

- raw Threads URLs;
- handles;
- screenshots;
- raw post text;
- raw reply text;
- raw OCR text;
- contact IDs;
- credentials;
- browser/session artifacts;
- exact controlled-store paths;
- stakeholder case IDs;
- private recipient details.

## Daily Stop-Rule Baseline

| Field | Value |
|---|---|
| `date_bucket` | `2026-04-28` |
| `surfaced_today` | 6 before batch `0002`; this selection surfaces 0 |
| `reviewed_today` | 6 before batch `0002`; this selection reviews 0 |
| `duplicates_today` | 0 from completed batch `0001`; batch `0002` pending |
| `insufficient_evidence_today` | 0 from completed batch `0001`; batch `0002` pending |
| `hard_negative_fp_pressure_today` | 0 from completed batch `0001`; batch `0002` pending |
| `average_review_time_today` | 4.7 combined minutes from batch `0001`; batch `0002` pending |
| `second_review_rate_today` | batch `0001` second review complete; batch `0002` pending |
| `reviewer_disagreement_today` | 0 from completed batch `0001`; batch `0002` pending |
| `raw_evidence_leak` | no |
| `stop_rule_triggered` | no new stop signal from this selection |
| `pause_required` | no; candidate surfacing may proceed only within selected hard-negative probe boundary |
| `owner_role_alias` | `track_b_daily_stop_check_owner` |

## Non-Authorizations

This source-arm selection note does not authorize:

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
