# Batch 0004 Low-Coverage High-SVS Signal Exploration

## Purpose

Run the next smallest learning experiment after Batch 0003.

The system has no active discrepancy cases after the previous learning loop, so the next bottleneck is not representation repair. The next bottleneck is low coverage for high-SVS signals.

## Selected Tasks

| Task | Signal | Why selected |
|---|---|---|
| `EXP_0001` | `成果展示` | `reviewed_count=1`, `yield_rate=1.0`, `svs=0.0068438` |
| `EXP_0002` | `保證收益` | `reviewed_count=1`, `yield_rate=1.0`, `svs=0.0068438` |

## Batch Shape

- Batch ID: `batch-0004-low-coverage-high-svs`
- Candidate stubs: 10 total
- Stub source: `data/candidate_stubs/latest.yaml`
- Selected stub output: `data/candidate_stubs/batch_0004.yaml`
- Collection mode: `safe / manual-assisted`
- External system access from this repo: none
- Raw Threads content in git: none
- PII in git: none

## Research Question

Do high-SVS, low-coverage signals remain useful after a small targeted expansion, or were their high scores just artifacts of tiny sample size?

## Hypotheses

1. `成果展示` will remain a high-value signal if result-display anchors continue to produce review-worthy candidates without large review-time increases.
2. `保證收益` will remain a high-value signal if guarantee/certainty anchors continue to produce review-worthy candidates without high cognitive load.
3. `review_stable_funnel_anchor` should remain useful as a cross-signal low-burden grouping feature if these stubs resolve cleanly without second review.

## Measurement Plan

After manually filling metadata-only candidate records for this batch, rerun:

```bash
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

Then compare:

- `成果展示` SVS before and after Batch 0004.
- `保證收益` SVS before and after Batch 0004.
- Batch-level SVS before and after Batch 0004.
- Whether any new `missed_pattern` discrepancy appears.
- Whether candidate review time increases enough to lower value per reviewer effort.
- Whether hard-negative or uncertain outcomes reveal over-specific signal enthusiasm.

## Done Condition

Batch 0004 is complete when:

- 10 metadata-only candidate records have been added or explicitly marked not fillable.
- No raw Threads content, PII, URLs, handles, screenshots, browser artifacts, credentials, or controlled-store paths are committed.
- Candidate validation passes.
- The v2 runner refreshes sparse clusters, embedding clusters, discrepancy report, and signal ranking.
- A short interpretation note states whether each target signal should continue, be revised, or be paused.

## Stop Rules

Stop immediately if:

- a candidate requires raw Threads content in git;
- a candidate requires PII, raw URL, handle, screenshot, browser export, credential, secret material, or controlled-store locator in git;
- reviewer burden exceeds the planned 10-stub batch;
- the batch drifts into crawler expansion, external access, production detection, legal fraud determination, or enforcement recommendation.

## Decision Implication

If both signals remain high-value and low-burden, run one more small mixed batch that includes hard-negative contrast.

If either signal collapses under review burden or uncertainty, revise the sparse representation before collecting more stubs.
