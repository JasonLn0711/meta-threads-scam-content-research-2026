# Batch 0005 Guarantee vs Result-Display Contrast

## Purpose

Run the smallest useful contrast test after Batch 0004.

Batch 0004 showed that `保證收益` scaled upward after reviewed structured metadata entered the v2 Research Operating System, while broad `成果展示` weakened. Batch 0005 tests whether that difference is stable enough to guide the next exploration strategy.

This is not a collection authorization, production detector step, legal fraud judgment, or enforcement workflow.

## First-Principle Question

The question is not:

```text
Can the system find more scam-like items?
```

The question is:

```text
Which sparse signal family maximizes high-value candidate discovery per unit reviewer effort?
```

## Source Evidence

Current Batch 0004 result:

```text
保證收益:
  reviewed_count: 6
  yield_rate: 1.0
  review_time: 42.333333
  cognitive_load: 1.325
  svs: 0.015351855

成果展示:
  reviewed_count: 9
  yield_rate: 0.444444
  review_time: 46.111111
  cognitive_load: 1.922222
  svs: 0.00358105
```

Research candidate:

- `outputs/research_candidates/RC_0002.md`

## Reviewer Packet

Use `data/candidate_intake/batch_0005_reviewer_packet.md` as the operating guide
for manual-assisted metadata fill.

The packet defines the contrast arms, field dictionary, stop rules, entry-level
review cues, and done condition. It is intentionally metadata-only and does not
authorize collection, raw evidence storage, or automated decisions.

## Result Record

Post-review outcome is recorded in
`experiments/batch_variants/0005-post-review-contrast-result.md` and
`metrics/batch_logs/batch_0005_run_log.yaml`.

## Batch Design

Use two balanced arms:

```text
A: 保證收益 + funnel/contact structure
B: 成果展示 without explicit 保證收益
```

Target size:

```text
10 candidate stubs total
5 stubs in Arm A
5 stubs in Arm B
```

This cap is intentional. The goal is to resolve the next research direction, not to increase volume.

## Arm A: Guarantee + Funnel/Contact

Inclusion criteria:

- `保證收益` expected as the primary signal
- at least one funnel/contact cue expected:
  - `誘導聯絡`
  - `社群導流`
  - `reply_funnel`
- reviewer should test whether `review_stable_funnel_anchor` is supported

Measurement focus:

- whether SVS remains high
- whether review time stays low
- whether `needs_thread` remains low
- whether second review remains uncommon

Expected behavior:

```text
guarantee_funnel_anchor
```

## Arm B: Result Display Without Explicit Guarantee

Inclusion criteria:

- `成果展示` expected as the primary signal
- `保證收益` should be absent unless review proves otherwise
- split examples across:
  - result display with funnel/contact cue
  - result display without funnel/contact cue
  - result display with ambiguity requiring thread context

Measurement focus:

- whether `成果展示` stays weak as a standalone signal
- whether `needs_thread` explains the burden
- whether second-review and uncertain rates rise
- whether a burden-aware subfeature is needed

Expected behavior:

```text
result_display_without_guarantee
```

## Review Fields Required

Each reviewed intake entry must complete:

- all sparse feature observations as `0` or `1`
- review decision: `scam`, `non_scam`, or `uncertain`
- confidence
- review time in seconds
- second-review requirement
- completion gates confirming no raw evidence or PII entered the repo

## Success Conditions

Batch 0005 succeeds if it produces one of these decisions:

- Arm A keeps higher SVS and lower burden: prioritize `保證收益 + funnel/contact structure`.
- Arm B remains high-uncertainty or high-burden: treat broad `成果展示` as a mixed signal.
- Arm B becomes strong only under a narrow condition: create a feature candidate, but do not auto-promote it.
- Both arms weaken: pause expansion and treat Batch 0004 as small-sample signal inflation.

## Measurement Plan

After human review fills `data/candidate_intake/batch_0005_intake.yaml`, run:

```bash
./.venv/bin/python scripts/validate_candidate_intake_v2.py data/candidate_intake/batch_0005_intake.yaml --expected-count 10
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0005_intake.yaml --report-output data/candidate_intake/batch_0005_conversion_report.yaml
./.venv/bin/python scripts/convert_candidate_intake_v2.py data/candidate_intake/batch_0005_intake.yaml --report-output data/candidate_intake/batch_0005_conversion_report.yaml --write-candidates
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

Compare:

- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/sparse_clusters/latest.yaml`
- `outputs/discrepancy_reports/latest.yaml`
- `exploration/tasks/latest.yaml`

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store locators
- no external systems accessed by this artifact
- no embedding-based decisions
- no automatic feature promotion
- no legal fraud, enforcement, takedown, or public warning claim
