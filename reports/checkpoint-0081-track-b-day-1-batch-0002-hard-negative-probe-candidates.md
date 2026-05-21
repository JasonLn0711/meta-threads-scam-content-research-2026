# Checkpoint 0081 Track B Day 1 Batch 0002 Hard-Negative Probe Candidates

## Purpose

Record repo-safe candidate surfacing for Track B batch `0002` under the `hard-negative probe arm`.

This note contains no raw Threads content, full item URLs, raw handles, raw contact IDs, screenshots, raw post text, raw reply text, raw OCR text, credentials, browser/session artifacts, exact controlled-store paths, stakeholder case IDs, or private recipient details.

## Batch Status

| Field | Value |
|---|---|
| Batch ID | `track_b_day_1_batch_0002_hard_negative_probe` |
| Date bucket | `2026-04-28` |
| Track | `track_b_capped_live_method_test` |
| Source arm | `hard-negative probe arm` |
| Candidate status | `second_review_complete` |
| Candidates surfaced | 10 |
| Candidates reviewed | 10 |
| Final Track B review outcomes | 10 |
| Accepted strict-valid records | 0 |
| Related decision | `decision-log/0129-record-track-b-day-1-batch-0002-hard-negative-probe-candidates.md` |
| Run record | `governance/pilot-launch/threads_pilot_v1_2026-05_track_b_capped_method_test_run_record_0054.md` |
| Evaluation note | `experiments/evaluation-notes/0096-track-b-day-1-batch-0002-hard-negative-probe-candidates.md` |
| Raw evidence in git | no |

## Current Review Update

Primary review is now recorded in:

```text
reports/checkpoint-0081-track-b-day-1-batch-0002-primary-review.md
```

Second review is now recorded in:

```text
reports/checkpoint-0081-track-b-day-1-batch-0002-second-review.md
```

Final review outcome:

```text
reviewed: 10
final non_scam/low hard negatives: 10
hard-negative false-positive pressure: 0
reviewer disagreements: 0
accepted strict-valid records: 0
pause required: no active pause from batch 0002
```

## Candidate Ledger

These are repo-safe candidate aliases for hard-negative pressure testing. They are not final Track B labels, legal determinations, enforcement recommendations, or accepted strict-valid records.

| Candidate ID | Candidate unit | Hard-negative contrast type | Potential false-positive signal families | Expected review focus | Dedupe status | Track B review status |
|---|---|---|---|---|---|---|
| `track_b_hn_probe_0001` | thread | genuine anti-scam warning | anti-scam language; investment domain seed | distinguish warning language from conversion behavior | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0002` | post | ordinary investment discussion | investment domain seed | check whether finance vocabulary alone is over-flagged | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0003` | post | financial education | teacher/advisor framing; investment domain seed | separate education from individualized funnel behavior | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0004` | post | general market commentary | investment domain seed; market-analysis framing | protect non-directed market commentary | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0005` | post | personal investment journaling | investment domain seed; personal-result framing | distinguish journaling from recruitment or proof lure | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0006` | account-context | legitimate finance creator content | profile-context pattern; investment domain seed | ensure bounded profile context does not become graph suspicion | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0007` | post | public contact information without funnel behavior | external contact category; investment domain seed | separate public contact presence from private-channel migration | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0008` | post | educational chart or screenshot content | OCR-derived financial claim; educational chart context | separate explanatory images from profit-proof lures | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0009` | post | news discussion | investment domain seed; news/current-event context | protect finance-related news discussion | unique by candidate alias | second review complete; final `non_scam` / `low` |
| `track_b_hn_probe_0010` | post | market-risk warning content | risk-warning language; investment domain seed | distinguish cautionary content from reassurance camouflage | unique by candidate alias | second review complete; final `non_scam` / `low` |

## Source-Arm Counter Update

| Source arm | Surfaced cap | Surfaced before batch | Surfaced in batch | Surfaced after batch | Remaining surfaced cap |
|---|---:|---:|---:|---:|---:|
| Checkpoint-derived seed replay | 30 | 6 | 0 | 6 | 24 |
| Reviewer-supplied candidates | 30 | 0 | 0 | 0 | 30 |
| Approved browser-session risk-probe matrix | 110 | 0 | 0 | 0 | 110 |
| Reply/comment funnel cue candidates | 60 | 0 | 0 | 0 | 60 |
| OCR/image-cue candidates | 20 | 0 | 0 | 0 | 20 |
| Hard-negative probe arm | 50 | 0 | 10 | 10 | 40 |
| Total | 300 | 6 | 10 | 16 | 284 |

Additional caps:

| Cap | Used after batch | Limit | Remaining |
|---|---:|---:|---:|
| Human-reviewed candidates | 16 | 150 | 134 |
| Accepted strict-valid records | 0 | 75 | 75 |

## Daily Stop-Rule Check

| Field | Value |
|---|---|
| `date_bucket` | `2026-04-28` |
| `surfaced_today` | 16 |
| `reviewed_today` | 16 |
| `duplicates_today` | 0 |
| `insufficient_evidence_today` | 0 |
| `hard_negative_fp_pressure_today` | 0 |
| `average_review_time_today` | 4.3 combined minutes across completed batch `0001` and batch `0002` |
| `second_review_rate_today` | 100%; resolved for batch `0002` |
| `reviewer_disagreement_today` | 0 |
| `raw_evidence_leak` | no |
| `stop_rule_triggered` | closed: decision `0130` pause condition resolved by second review |
| `pause_required` | no active pause from batch `0002`; continue only by next source-arm/batch control |
| `owner_role_alias` | `track_b_daily_stop_check_owner` |

## Interpretation

Batch `0002` is the first Track B batch focused entirely on hard-negative pressure. It is designed to test whether the signal-family method can avoid treating investment-adjacent but non-scam or potentially benign content as scam candidates merely because it contains finance, warning, education, chart, contact, or market-risk language.

Second review is complete. All ten candidate aliases are final Track B `non_scam` / `low` hard-negative outcomes for this method-test ledger, with 0 hard-negative false-positive pressure and 0 reviewer disagreements.

Do not continue hard-negative probe surfacing by habit. The next useful result should come from a deliberately selected next Track B source arm or controlled batch.

## Non-Authorizations

This candidate-surfacing note does not authorize:

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
