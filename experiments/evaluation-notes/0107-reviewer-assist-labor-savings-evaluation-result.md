# 0107 - Reviewer Assist Labor-Savings Evaluation Result Workbench

Date: 2026-05-05

Status: completed aggregate-only shadow result

## Purpose

This workbench is the execution layer for Decision `0145` and Decision `0146`.

It is designed to answer:

```text
Does Reviewer Assist help the governed discovery method find, route, and review
review-worthy Threads investment-scam candidates with less human burden and
without increasing false-positive, hard-negative, or governance risk?
```

This file records the aggregate-only result after the assisted-review fields
were filled in `data/reviewer_assist_eval/batch_0010_assisted_review_result.yaml`.

This is a metadata-only shadow evaluation. It supports expanding Reviewer Assist
evaluation, but it does not prove platform-wide coverage, authorize new
collection, authorize model training, or validate production scam detection.

## Inputs

- Decision: `decision-log/0145-open-reviewer-assist-labor-savings-evaluation-for-automatic-discovery.md`
- Execution workbench decision: `decision-log/0146-open-reviewer-assist-evaluation-execution-workbench.md`
- Evaluation plan: `reports/reviewer-assist-labor-savings-evaluation-plan.md`
- Experiment plan: `experiments/batch_variants/0010-reviewer-assist-labor-savings-evaluation.md`
- Work order: `data/reviewer_assist_eval/batch_0010_work_order.yaml`
- Assisted-review result: `data/reviewer_assist_eval/batch_0010_assisted_review_result.yaml`
- Manual baseline result: `experiments/evaluation-notes/0105-v2-batch-0009-context-gating-policy-check-result.md`
- Manual baseline run log: `metrics/batch_logs/batch_0009_run_log.yaml`

## Baseline Snapshot

Manual baseline from Batch `0009`:

| Metric | Value |
|---|---:|
| Reviewed candidates | 12 |
| Scam / high-value count | 8 |
| Non-scam count | 2 |
| Uncertain count | 2 |
| Yield rate | 0.666667 |
| Average review time seconds | 37.333333 |
| Candidates per reviewer hour | 96.428571 |
| High-value candidates per reviewer hour | 64.285714 |
| Needs-thread rate | 0.083333 |
| Second-review rate | 0.25 |
| Uncertainty rate | 0.166667 |

These baseline metrics are not platform-wide coverage claims. They are only the
manual baseline for a metadata-only evaluation slice.

## Assisted-Review Fill Status

```text
candidate_entries: 12
completed_assisted_review_entries: 12
raw_evidence_leakage_incidents: 0
manual_assisted_final_label_mismatch_rate: 0.0
```

The assisted condition preserved the same final label distribution as the
manual baseline:

```text
scam: 8
non_scam: 2
uncertain: 2
```

This is not an independent platform-validity finding. It is a same-slice
labor-savings and assist-quality result.

## Aggregate Result

| Metric | Manual baseline | Assisted review | Difference |
|---|---:|---:|---:|
| Reviewed candidates | 12 | 12 | 0 |
| Average review seconds | 37.333333 | 28.750000 | -8.583333 |
| Median review seconds | 35.500000 | 25.500000 | -10.000000 |
| P95 review seconds, nearest-rank | 58.000000 | 53.000000 | -5.000000 |
| Candidates reviewed per hour | 96.428571 | 125.217391 | +28.788820 |
| High-value candidates per reviewer hour | 64.285714 | 83.478261 | +19.192547 |
| Review-worthy yield | 0.666667 | 0.666667 | 0.000000 |
| Needs-thread proxy rate | 0.083333 | 0.083333 | 0.000000 |
| Second-review rate | 0.250000 | 0.250000 | 0.000000 |
| Manual-assisted final-label mismatch rate | n/a | 0.000000 | n/a |
| Hard-negative false-positive pressure | 0.000000 | 0.000000 | 0.000000 |
| Insufficient-evidence rate | not measured here | 0.166667 | n/a |
| Raw-evidence leakage incidents | 0 required | 0 | 0 |

Average review time dropped by `22.9911%` on this same-slice shadow evaluation.

## Assist Quality

| Metric | Assisted review |
|---|---:|
| Summary usefulness mean | 4.416667 |
| Summary rating 4-5 percent | 0.916667 |
| Summary omission risk, low / medium / high | 9 / 2 / 1 |
| Schema-prefill clean accepted rate | 0.750000 |
| Schema-prefill accepted-or-minor rate | 1.000000 |
| Schema-prefill correction rate | 0.250000 |
| Signal suggestion clean accepted rate | 0.833333 |
| Signal suggestion accepted-or-minor rate | 1.000000 |
| Signal suggestion correction rate | 0.166667 |
| Priority explanation clean accepted rate | 0.916667 |
| Priority explanation accepted-or-minor rate | 1.000000 |
| Priority explanation correction rate | 0.083333 |
| Hard-negative warning acceptance rate among applicable entries | 1.000000 |
| Hard-negative over-warning or missed-warning count | 0 |

## Interpretation

The result supports expanding Reviewer Assist evaluation because:

- average, median, and nearest-rank p95 review time all improved;
- high-value candidates per reviewer hour improved from `64.285714` to `83.478261`;
- final assisted labels matched manual baseline labels on this slice;
- second-review rate did not increase;
- hard-negative warnings were accepted for all applicable entries;
- raw-evidence leakage remained zero.

The result is still limited because:

- the slice is Batch `0009`, a policy-weighted metadata-only slice;
- it is not representative of all Threads investment scams;
- it does not test live discovery, new source arms, or raw-thread context;
- it does not authorize production, model training, external collection, or
  automated final decisions.

## Decision Slot

Select exactly one after the assisted-review fields are filled:

- `expand_assist_evaluation`;
- `revise_assist_design`;
- `keep_shadow_only`;
- `pause_assist_layer`;
- `request_new_governed_source_slice`.

Current decision: `expand_assist_evaluation`

Expansion should remain metadata-only or separately governed. The next slice
should include another comparable source-lane mix or a later approved governed
source slice so this result does not overfit Batch `0009`.

## Stop Conditions

Stop and do not synthesize a favorable result if:

- any raw Threads text, raw reply text, raw OCR text, URL, handle, screenshot,
  browser/session artifact, credential, stakeholder case ID, or controlled-store
  locator enters tracked git files;
- assisted output implies final scam, legal fraud, enforcement, or public-warning
  judgment;
- reviewer-facing materials expose the manual-baseline labels or times;
- review time is not recorded and no unavailable reason is given;
- summary or schema prefill creates unmeasured correction burden;
- hard-negative false-positive pressure increases without a clear revision path;
- the result starts treating Batch `0009` or current case fragments as
  representative of all Threads investment scams.

## Next Action

Open the next bounded Reviewer Assist evaluation slice. It should preserve:

- no raw evidence in git;
- human final judgment;
- hidden baseline fields in any reviewer-facing packet;
- hard-negative calibration;
- second-review override;
- aggregate-only reporting.
