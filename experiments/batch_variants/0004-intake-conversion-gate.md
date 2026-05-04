# Batch 0004 Intake Conversion Gate

## Purpose

Create a hard boundary between exploration suggestions and candidate records.

Batch 0004 currently contains metadata-only stubs and a manual-assisted intake worksheet. The next system step is not to invent candidate labels or sparse vectors. The next step is to verify whether each intake entry has enough completed, structured, human-reviewed metadata to become a `candidate_record_v2` file.

## First-Principle Fit

This gate supports the v2 research operating system goal:

```text
maximize high-value candidate discovery per unit reviewer effort
```

It does this by making reviewer effort measurable without letting incomplete intake data contaminate SVS, sparse clusters, or discrepancy reports.

## Inputs

- `data/candidate_intake/batch_0004_intake.yaml`
- `data-contracts/candidate_record_v2.schema.yaml`
- `meta-system/sparse_schema/sparse_features_v2.yaml`

## Output

- `data/candidate_intake/batch_0004_conversion_report.yaml`

Candidate records are written only when:

- `fill_status` is `completed`
- every sparse feature observation is completed as `0` or `1`
- review decision, confidence, review time, and second-review flag are complete
- all completion gates are true
- the resulting candidate validates against `candidate_record_v2`
- the operator explicitly runs the converter with `--write-candidates`

## Initial Pre-Review Batch 0004 Result

Actual state after the first conversion-gate run, before the worksheet was filled:

```text
intake_count: 10
converted_count: 0
blocked_count: 10
written_count: 0
status: blocked
```

This was the expected result because Batch 0004 entries were still pending manual review at that point.

## Blocked Reasons

The initial blockers were structural, not analytical:

- intake entries are not marked `completed`
- sparse observations are still pending or expected-from-stub
- review fields are still pending
- completion gates are still pending

This means the system is correctly refusing to turn exploration hypotheses into evidence records.

## Measurement Plan

After manual-assisted review fills the worksheet, rerun:

```bash
./.venv/bin/python scripts/convert_candidate_intake_v2.py
```

If the report shows zero blocked entries, then write candidate records:

```bash
./.venv/bin/python scripts/convert_candidate_intake_v2.py --write-candidates
```

Then run:

```bash
./.venv/bin/python scripts/validate_candidate_v2.py data/candidates
./.venv/bin/python scripts/run_v2_ros.py
./.venv/bin/python scripts/generate_feature_candidates_v1.py
./.venv/bin/python scripts/generate_exploration_tasks.py
```

Compare before and after:

- `metrics/signal_scores/latest_ranking.yaml`
- `outputs/sparse_clusters/latest.yaml`
- `outputs/discrepancy_reports/latest.yaml`
- `exploration/tasks/latest.yaml`

## Learning Question

Does completing Batch 0004 change the system state?

The first real post-review learning signal is one of:

- low-coverage high-SVS signals become more stable
- sparse cluster membership changes
- discrepancy cases reappear and generate new feature hypotheses
- review time or second-review pressure changes for `成果展示` or `保證收益`

## Guardrails

- no raw Threads content
- no PII
- no URLs, handles, screenshots, browser artifacts, credentials, or controlled-store locators
- no candidate records before human review
- no embedding-based decisions
- no sparse feature promotion from this gate
