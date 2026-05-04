# Batch 0006 Post-Review Routing Result

## Purpose

Record the Batch 0006 contrast-aware routing validation after human-reviewed
structured metadata was completed and converted into v2 candidate records.

This is an actual experiment result note, not a tutorial and not a detector
evaluation. It records whether reviewer routing improved discovery value per
unit reviewer effort.

## Inputs

- Experiment plan: `experiments/batch_variants/0006-contrast-aware-routing-validation.md`
- Reviewer packet: `data/candidate_intake/batch_0006_reviewer_packet.md`
- Intake worksheet: `data/candidate_intake/batch_0006_intake.yaml`
- Conversion report: `data/candidate_intake/batch_0006_conversion_report.yaml`
- Candidate records: `data/candidates/batch_0006/*.yaml`
- Batch run log: `metrics/batch_logs/batch_0006_run_log.yaml`
- SVS output: `metrics/signal_scores/latest_ranking.yaml`
- Contrast-aware routing output: `metrics/contrast_scores/latest.yaml`
- Sparse clusters: `outputs/sparse_clusters/latest.yaml`
- Discrepancy report: `outputs/discrepancy_reports/latest.yaml`

## Conversion Result

```text
intake_count: 12
converted_count: 12
blocked_count: 0
written_count: 12
status: ready
```

The conversion gate wrote 12 metadata-only `candidate_record_v2` files under
`data/candidates/batch_0006/`.

## Batch-Level Result

After Batch 0006 entered the ROS:

```text
candidate_count_after_run: 36
batch_0006_reviewed_count: 12
batch_0006_scam_count: 5
batch_0006_non_scam_count: 2
batch_0006_uncertain_count: 5
batch_0006_yield_rate: 0.416667
batch_0006_information_density: 0.425121
batch_0006_review_time: 41.75
batch_0006_cognitive_load: 1.7125
batch_0006_svs: 0.002477502
```

Compared with Batch 0005:

```text
batch_0005_svs: 0.002658839
batch_0006_svs: 0.002477502
observed_change: 0.93x of Batch 0005 SVS
```

This slight decrease is not a failure. Batch 0006 was designed to validate
routing lanes, not to maximize aggregate batch SVS.

## Lane Result

Lane A: `strong_source_priority`

```text
reviewed_count: 4
scam_count: 4
yield_rate: 1.0
review_time: 32.5
cognitive_load: 1.1875
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
svs: 0.020606701
```

Lane B: `result_display_context_review`

```text
reviewed_count: 4
scam_count: 0
uncertain_count: 4
yield_rate: 0.0
review_time: 49.75
cognitive_load: 2.2875
needs_thread_rate: 1.0
second_review_rate: 1.0
uncertainty_rate: 1.0
svs: 0.0
```

Lane C: `result_display_contrast_holdout`

```text
reviewed_count: 2
scam_count: 0
non_scam_count: 2
yield_rate: 0.0
review_time: 37.0
cognitive_load: 1.0
needs_thread_rate: 0.0
second_review_rate: 0.0
uncertainty_rate: 0.0
svs: 0.0
```

Lane D: `guarantee_context_review`

```text
reviewed_count: 2
scam_count: 1
uncertain_count: 1
yield_rate: 0.5
review_time: 49.0
cognitive_load: 2.325
needs_thread_rate: 1.0
second_review_rate: 1.0
uncertainty_rate: 0.5
svs: 0.001383443
```

Interpretation:

- Lane A is a validated fast lane in this metadata-only dry run.
- Lane B is a validated context-cost lane, not a direct high-yield source arm.
- Lane C remains useful as hard-negative or boundary calibration.
- Lane D should not be merged with Lane A because its context burden changes
  reviewer effort.

## Global Contrast Result

After Batch 0006, the global contrast-aware score shows:

```text
strong_source_priority:
  reviewed_count: 14
  scam_count: 14
  yield_rate: 1.0
  review_time: 37.428571
  cognitive_load: 1.246429
  svs: 0.017651939
  needs_thread_rate: 0.0
  second_review_rate: 0.0
  uncertainty_rate: 0.0

result_display_context_review:
  reviewed_count: 13
  scam_count: 0
  yield_rate: 0.0
  review_time: 46.692308
  cognitive_load: 2.3
  svs: 0.0
  needs_thread_rate: 1.0
  second_review_rate: 0.846154
  uncertainty_rate: 0.846154
```

The useful distinction is not `保證收益` versus `成果展示` alone. The useful
distinction is:

```text
fast lane: guarantee/certainty anchor + executable transition + low context burden
slow lane: broad result display + context burden + high uncertainty
```

## Signal-Level Result

Top sparse signals after Batch 0006:

```text
保證收益:
  reviewed_count: 17
  yield_rate: 0.882353
  svs: 0.011325292

review_stable_funnel_anchor:
  reviewed_count: 18
  yield_rate: 0.833333
  svs: 0.010401546

成果展示:
  reviewed_count: 22
  yield_rate: 0.272727
  svs: 0.001597597

needs_thread:
  reviewed_count: 19
  yield_rate: 0.105263
  svs: 0.00030193
```

This supports keeping `保證收益` and `review_stable_funnel_anchor` as high-value
sparse signals while treating `needs_thread` as a cost signal.

## Cluster And Discrepancy Result

Sparse clustering remains too broad:

```text
sparse_cluster_count: 1
candidate_count: 36
```

The broad sparse cluster is the main failure mode. It means lane-level routing is
currently more useful than raw sparse clustering for reviewer-effort allocation.

Embedding output remains discovery-only:

```text
embedded_candidate_count: 3
Batch 0006 embedding decisions: none
```

Discrepancy output after Batch 0006:

```text
case_count: 2
missed_pattern: 0
over_generalization: 2
```

The two discrepancy cases are still synthetic embedding coverage artifacts. No
sparse-schema update should be made from them without human feature review.

## Decision Implications

Do:

- keep `strong_source_priority` as the high-priority review lane;
- route `result_display_context_review` to slower context review;
- keep `result_display_contrast_holdout` as hard-negative calibration;
- keep `guarantee_context_review` separate from the fast lane;
- measure review-time and second-review burden before increasing batch size.

Do not:

- treat `成果展示` as automatically safe;
- treat `保證收益` without context as automatically low-burden;
- scale collection volume before the broad sparse-cluster failure mode is
  addressed;
- use embedding output for decisions or schema changes;
- auto-promote any feature from this run.

## Next Experiment

Run one more capped routing batch only if it tests the current bottleneck:

```text
Question:
Can result-display context cases be split into lower-cost and higher-cost
sub-lanes without adding raw content or reviewer overload?

Candidate next feature hypothesis:
context_required_result_display

Expected effect:
reduce over-generalization inside the broad sparse cluster and make slow-lane
review more predictable.
```

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no external systems accessed by this artifact
- no embedding-based decisions
- no automatic feature promotion
- no legal fraud, enforcement, takedown, or public warning claim
