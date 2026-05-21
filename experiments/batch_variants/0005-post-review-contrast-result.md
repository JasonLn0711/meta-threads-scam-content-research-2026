# Batch 0005 Post-Review Contrast Result

## Purpose

Record the Batch 0005 contrast run after human-reviewed structured metadata was
added to the v2 Research Operating System.

This is an actual result note. It does not infer raw evidence, legal fraud,
enforcement action, or platform-scale detection capability.

## Inputs

- Experiment plan: `experiments/batch_variants/0005-guarantee-vs-result-display-contrast.md`
- Reviewer packet: `data/candidate_intake/batch_0005_reviewer_packet.md`
- Intake worksheet: `data/candidate_intake/batch_0005_intake.yaml`
- Conversion report: `data/candidate_intake/batch_0005_conversion_report.yaml`
- Candidate records: `data/candidates/batch_0005/*.yaml`
- Batch run log: `metrics/batch_logs/batch_0005_run_log.yaml`
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

The conversion gate wrote 10 metadata-only `candidate_record_v2` files under
`data/candidates/batch_0005/`.

## Batch-Level Result

After Batch 0005 entered the ROS:

```text
candidate_count: 24
batch_0005_reviewed_count: 10
batch_0005_scam_count: 4
batch_0005_non_scam_count: 2
batch_0005_uncertain_count: 4
batch_0005_yield_rate: 0.4
batch_0005_information_density: 0.462319
batch_0005_review_time: 41.4
batch_0005_cognitive_load: 1.68
batch_0005_svs: 0.002658839
```

Compared with Batch 0004:

```text
batch_0004_svs: 0.005125224
batch_0005_svs: 0.002658839
observed_change: 0.52x of Batch 0004 SVS
```

This decrease is not a failure by itself. Batch 0005 intentionally included a
contrast arm with ambiguous and hard-negative result-display examples.

## Arm Result

Arm A: `保證收益 + funnel/contact structure`

```text
reviewed_count: 5
scam_count: 4
uncertain_count: 1
yield_rate: 0.8
review_time: 38.4
cognitive_load: 1.4
needs_thread_rate: 0.2
second_review_rate: 0.2
svs: 0.010157867
```

Arm B: `成果展示 without explicit 保證收益`

```text
reviewed_count: 5
scam_count: 0
non_scam_count: 2
uncertain_count: 3
yield_rate: 0.0
review_time: 44.4
cognitive_load: 1.96
needs_thread_rate: 0.8
second_review_rate: 0.6
svs: 0.0
```

Interpretation:

- Arm A produced higher research yield with lower review burden.
- Arm B produced mostly uncertainty and higher thread/context burden.
- `成果展示` is not a negative class. It is a context-dependent mixed signal.

## Signal-Level Result

`保證收益` remains the top-ranked sparse signal after coverage increased:

```text
before_reviewed_count: 6
after_reviewed_count: 11
before_svs: 0.015351855
after_svs: 0.012867571
observed_change: 0.84x of previous SVS
after_yield_rate: 0.909091
```

`成果展示` weakened further:

```text
before_reviewed_count: 9
after_reviewed_count: 15
before_svs: 0.00358105
after_svs: 0.002215116
observed_change: 0.62x of previous SVS
after_yield_rate: 0.333333
```

## Cluster And Discrepancy Result

Sparse clustering now has two clusters. The large cluster is broad and mixed,
which means the current sparse representation still needs contrast-aware
interpretation. The smaller cluster isolates the A05 burden case with a synthetic
candidate through `needs_thread + 情緒操控`.

Discrepancy output:

```text
case_count: 2
missed_pattern: 0
over_generalization: 2
```

Both discrepancy cases are driven by synthetic embedded candidates. Batch 0005
candidate records have no embedding vectors, so embedding output remains a
discovery-coverage gap, not decision evidence.

## Decision Implications

Do:

- prioritize `保證收益 + funnel/contact structure` for the next high-value source
  arm;
- keep `成果展示` as a contrast and context-dependent signal;
- measure `needs_thread` and second-review rate as burden penalties;
- consider a future burden-aware `成果展示` subfeature only through human-reviewed
  feature promotion.
- use `metrics/contrast_scores/latest.yaml` to route high-value source-arm
  candidates separately from context-cost candidates.

Do not:

- treat `成果展示` as automatically safe or automatically high-risk;
- treat lower Batch 0005 SVS as a failed experiment;
- use embedding output for labels or sparse-schema updates;
- auto-promote any feature from this run.

## Next Experiment

Use the contrast-aware scoring loop:

```text
strong source arm: 保證收益 + executable transition
contrast arm: 成果展示 + context-required / no explicit guarantee
```

The first scoring result is recorded in
`experiments/evaluation-notes/0101-v2-contrast-aware-routing-result.md`.

Next, measure whether this routing lowers reviewer burden by sending B-arm
candidates to slower context review while keeping A-arm candidates high priority.

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store
  locators
- no external systems accessed by this artifact
- no embedding-based decisions
- no automatic feature promotion
- no legal fraud, enforcement, takedown, or public warning claim
