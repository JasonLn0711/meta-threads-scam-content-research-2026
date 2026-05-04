# Context Gating Policy

Status: active v2 research policy

Date opened: 2026-05-04

## Purpose

This policy turns the Batch 0007 and Batch 0008 findings into a reviewer-routing
rule.

The goal is not scam detection. The goal is to allocate scarce reviewer time to
the lanes that maximize high-value candidate discovery per reviewer effort.

The policy is a decision-support layer for structured metadata. It is not a
production detector, legal fraud judgment, enforcement workflow, public-warning
workflow, model-training authorization, or data-collection authorization.

## First-Principle Rule

When reviewer capacity is constrained, route candidates by expected reviewer-hour
value before asking for deeper context.

The system should ask:

```text
Will reading more context likely produce high-value discovery, or will it mainly
increase review time, uncertainty, and second-review burden?
```

## Routing Lanes

### 1. Fast Lane - strong_source_priority

Activation:

```text
保證收益
AND (誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor)
AND NOT needs_thread
```

Review action:

```text
fast_priority_review
```

Batch 0008 evidence:

```text
reviewed_count: 4
yield_rate: 1.0
average_review_time_seconds: 33.25
high_value_candidates_per_hour: 108.270677
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
```

Policy:

Use this lane first when the reviewer-hour budget is tight. It has the strongest
reviewed evidence for high-value candidate discovery per reviewer hour.

Do not interpret this as legal fraud determination or automated scam labeling.

### 2. Boundary Lane - result_display_low_context_transition

Activation:

```text
成果展示
AND NOT 保證收益
AND NOT needs_thread
AND (誘導聯絡 OR 社群導流 OR reply_funnel OR review_stable_funnel_anchor)
```

Review action:

```text
cheap_boundary_triage
```

Batch 0008 evidence:

```text
reviewed_count: 4
yield_rate: 0.0
average_review_time_seconds: 42.5
second_review_rate: 0.5
uncertainty_rate: 1.0
```

Policy:

Review this lane only when the research question is boundary calibration,
decision-boundary learning, or a tiny diagnostic probe. Do not treat this lane as
a positive-yield source arm without new evidence.

### 3. Slow Context Lane - result_display_thread_required

Activation:

```text
成果展示
AND NOT 保證收益
AND needs_thread
AND NOT 情緒操控
```

Review action:

```text
slow_context_review_or_tiny_diagnostic_sample
```

Batch 0008 evidence:

```text
reviewed_count: 4
yield_rate: 0.0
average_review_time_seconds: 57.25
needs_thread_rate: 1.0
second_review_rate: 1.0
uncertainty_rate: 1.0
```

Policy:

Do not send this lane to routine review when reviewer capacity is constrained.
Use it only when the specific experiment requires context-gating diagnostics or
when a capped sample is needed to test whether the lane has changed.

### 4. Calibration Lane - result_display_clean_holdout

Activation:

```text
成果展示
AND NOT 保證收益
AND NOT (誘導聯絡 OR 社群導流 OR reply_funnel OR needs_thread OR 情緒操控)
```

Review action:

```text
hard_negative_calibration
```

Batch 0008 evidence:

```text
reviewed_count: 4
non_scam_count: 4
average_review_time_seconds: 34.5
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
```

Policy:

Preserve this lane as a hard-negative calibration pool. It protects the system
from over-generalizing `成果展示`.

## Reviewer-Hour Decision Rule

Use this priority order unless a later batch shows different reviewer-hour value:

```text
1. strong_source_priority
2. result_display_clean_holdout for hard-negative calibration
3. result_display_low_context_transition for cheap boundary triage
4. result_display_thread_required only for capped slow-context diagnostics
```

This priority order is about reviewer-hour allocation. It is not a final label
order.

## Stop And Continue Rules

Continue or expand a lane only if it improves at least one of:

- high-value candidates per reviewer hour;
- full-thread-reading reduction;
- second-review reduction;
- uncertainty reduction;
- hard-negative boundary clarity.

Pause or cap a lane when it shows:

- zero positive yield across repeated batches;
- high full-thread-reading burden;
- high second-review burden;
- high uncertainty without discovery value;
- sparse-cluster broadness without useful separation.

## What This Policy Changes

Before Batch 0008, result-display lanes were still plausible exploration targets.

After Batch 0008:

- `strong_source_priority` remains the fast reviewer-priority lane;
- `成果展示` alone is not a priority positive-yield source;
- low-context result-display remains boundary triage;
- thread-required result-display is too expensive for routine review;
- clean result-display holdouts are useful hard negatives.

## Evidence

- `experiments/batch_variants/0008-context-gate-reviewer-hour-value.md`
- `experiments/evaluation-notes/0104-v2-batch-0008-reviewer-hour-value-result.md`
- `metrics/batch_logs/batch_0008_run_log.yaml`
- `metrics/contrast_scores/latest.yaml`
- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/research_candidates/RC_0007.md`

## Non-Authorizations

This policy does not authorize:

- external data access;
- raw Threads content storage;
- PII storage;
- URL, handle, screenshot, browser-artifact, or controlled-store locator storage
  in git;
- sparse schema auto-promotion;
- model training;
- production detection;
- legal fraud determination;
- enforcement, takedown, or public warning actions.
