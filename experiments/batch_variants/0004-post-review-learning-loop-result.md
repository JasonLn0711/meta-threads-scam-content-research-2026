# Batch 0004 Post-Review Learning Loop Result

## Purpose

Record the first Batch 0004 run where manual-assisted structured metadata entered the v2 Research Operating System as candidate records.

This is an actual result note. It does not infer raw evidence, legal fraud, enforcement action, or platform-scale detection capability.

## Inputs

- Intake worksheet: `data/candidate_intake/batch_0004_intake.yaml`
- Conversion report: `data/candidate_intake/batch_0004_conversion_report.yaml`
- Candidate records: `data/candidates/batch_0004/*.yaml`
- SVS output: `metrics/signal_scores/latest_ranking.yaml`
- Sparse clusters: `outputs/sparse_clusters/latest.yaml`
- Discrepancy report: `outputs/discrepancy_reports/latest.yaml`

## Conversion Result

```text
intake_count: 10
converted_count: 10
blocked_count: 0
written_count: 10
status: ready
```

The conversion gate wrote 10 metadata-only `candidate_record_v2` files under `data/candidates/batch_0004/`.

## Batch-Level Result

After Batch 0004 entered the ROS:

```text
candidate_count: 14
batch_0004_reviewed_count: 10
batch_0004_scam_count: 5
batch_0004_yield_rate: 0.5
batch_0004_information_density: 0.753623
batch_0004_review_time: 38.9
batch_0004_cognitive_load: 1.89
batch_0004_svs: 0.005125224
```

Compared with the synthetic Batch 0003 dry run:

```text
batch_0003_svs: 0.00112473
batch_0004_svs: 0.005125224
observed_change: 4.56x higher batch SVS
```

This is not a claim that Batch 0004 is universally better. It means this reviewed metadata batch produced more high-value candidate discovery per measured reviewer effort than the prior dry-run batch.

## Signal-Level Result

`保證收益` scaled upward after coverage increased:

```text
before_reviewed_count: 1
after_reviewed_count: 6
before_svs: 0.0068438
after_svs: 0.015351855
observed_change: 2.24x higher SVS
after_yield_rate: 1.0
after_review_time: 42.333333
```

`成果展示` weakened after coverage increased:

```text
before_reviewed_count: 1
after_reviewed_count: 9
before_svs: 0.0068438
after_svs: 0.00358105
observed_change: 0.52x of previous SVS
after_yield_rate: 0.444444
after_cognitive_load: 1.922222
```

Interpretation:

- `保證收益` looks like a stronger low-burden high-yield signal after a small reviewed expansion.
- `成果展示` looks more ambiguous and burden-sensitive when separated from guarantee language.
- `成果展示` should not be treated as a high-yield signal by itself without funnel, contact, or certainty structure.

## Cluster Result

Sparse clustering changed in a useful way:

- `sparse-cluster-0001` now contains 8 Batch 0004 candidates plus 2 synthetic candidates.
- Its core feature is `review_stable_funnel_anchor`.
- `sparse-cluster-0002` isolates two weaker `成果展示` candidates with `needs_thread` and `成果展示` as core features.

This suggests the sparse layer is separating:

- stronger funnel/value-anchor candidates;
- weaker or ambiguous result-display candidates that still require context.

## Discrepancy Result

```text
case_count: 0
missed_pattern: 0
over_generalization: 0
```

No new discrepancy-generated feature candidates were produced in this run.

Important limitation:

Batch 0004 candidate records have no embedding vectors, so embedding clustering skipped those 10 records. The absence of discrepancy cases should not be interpreted as proof that no missed pattern exists.

## Exploration Result

After Batch 0004, exploration tasks changed from low-coverage signal expansion to embedding-coverage gaps:

```text
task_count: 2
low_coverage_task_count: 0
embedding_outlier_task_count: 2
```

This means the system no longer sees `保證收益` or `成果展示` as the immediate low-coverage bottleneck. The next bottleneck is representation coverage for embedding-discovery comparison.

## Decision Implications

Do:

- keep `保證收益` as a high-priority sparse signal for the next small batch;
- split `成果展示` into stronger and weaker subconditions during future review;
- preserve `review_stable_funnel_anchor` as a useful bridge feature for now;
- treat missing embeddings as a discovery-layer coverage gap, not a decision gap.

Do not:

- promote a new sparse feature from this run;
- claim result-display alone is high yield;
- use embedding absence to downgrade or label candidates;
- expand collection volume before defining the next capped batch.

## Next Experiment

Run a capped contrast batch with two arms:

```text
A: 保證收益 + funnel/contact structure
B: 成果展示 without explicit 保證收益
```

Measure:

- SVS by arm;
- full-thread requirement rate;
- second-review rate;
- uncertain rate;
- cluster separation;
- whether `成果展示` needs a burden-aware subfeature.
