# 0109 - Reviewer Assist Thread-Required Lane Revision Result Workbench

Date: 2026-05-05

Status: empirical context-gate result completed; packet/source alignment reconciled

## Purpose

This workbench is the result layer for Decision `0150`.

It tests whether a revised Reviewer Assist context gate can reduce wasted
review time on `result_display_thread_required` candidates by routing them to
the correct context-first next action before reviewers attempt a confident
metadata-only label.

## Evaluation Question

```text
Can Reviewer Assist identify thread dependency earlier, route the candidate to
the correct next action, and avoid over-requesting thread context for controls?
```

## Inputs

- Decision: `decision-log/0150-open-reviewer-assist-thread-required-lane-revision.md`
- Experiment plan: `experiments/batch_variants/0012-reviewer-assist-thread-required-lane-revision.md`
- Work order: `data/reviewer_assist_eval/batch_0012_work_order.yaml`
- Reviewer rules: `data/reviewer_assist_eval/batch_0012_reviewer_rules.md`
- Reviewer fill template: `data/reviewer_assist_eval/batch_0012_reviewer_fill_sheet_template.yaml`
- Reviewer context-gate packet: `data/reviewer_assist_eval/batch_0012_reviewer_context_gate_packet.yaml`
- Human-fill handoff: `reports/reviewer-assist-batch-0012-context-gate-handoff.md`
- Completed context-gate result: `data/reviewer_assist_eval/batch_0012_context_gate_result.yaml`
- Aggregate result: `data/reviewer_assist_eval/batch_0012_aggregate_result.yaml`
- Result decision: `decision-log/0152-record-reviewer-assist-batch-0012-context-gate-result.md`
- Prior result decision: `decision-log/0149-record-reviewer-assist-expansion-batch-0011-result.md`
- Prior aggregate result: `data/reviewer_assist_eval/batch_0011_aggregate_result.yaml`

## Baseline Snapshot

Batch `0011` thread-required lane:

| Metric | Value |
|---|---:|
| Count | 4 |
| Assisted total review seconds | 207.0 |
| Assisted average review seconds | 51.75 |
| Uncertain count | 4 |
| Second-review required count | 4 |
| Insufficient-evidence count | 4 |

Control baselines from Batch `0011`:

| Lane | Assisted avg seconds | Role in Batch 0012 |
|---|---:|---|
| `strong_source_priority` | 23.0 | fast-lane regression control |
| `result_display_low_context_transition` | 33.75 | boundary over-request control |
| `result_display_clean_holdout` | 24.0 | hard-negative over-request control |

## Slice Coverage

| Role | Lane | Count |
|---|---|---:|
| Target | `result_display_thread_required` | 4 |
| Boundary control | `result_display_low_context_transition` | 4 |
| Hard-negative control | `result_display_clean_holdout` | 2 |
| Fast-lane control | `strong_source_priority` | 2 |

## Prepared Context-Gate Packet

Decision `0151` prepared the reviewer-facing context-gate packet.

The packet fills only revised assist outputs:

- context dependency gate;
- context reason codes;
- minimal context needed;
- safe next action;
- metadata label guardrail;
- priority explanation;
- missing-evidence note;
- second-review suggestion.

It leaves all `reviewer_fields` blank and does not expose prior Batch `0011`
labels, timings, second-review decisions, or insufficient-evidence decisions.

The packet was later completed by human review. The completed result is now
recorded in `data/reviewer_assist_eval/batch_0012_context_gate_result.yaml`.

## Completed Aggregate Result

| Metric | Batch 0011 baseline | Batch 0012 revised gate | Difference |
|---|---:|---:|---:|
| Target lane reviewed candidates | 4 | 4 | 0 |
| Target lane average seconds | 51.75 | 29.5 | -22.25 |
| Target lane median seconds | pending | 29.5 | n/a |
| Target lane p95 seconds | pending | 30.85 | n/a |
| Correct thread-before-label routing rate | pending | 1.0 | n/a |
| Metadata-only overreach count | pending | 0 | n/a |
| Boundary-control over-request count | pending | 0 | n/a |
| Hard-negative over-request count | pending | 0 | n/a |
| Fast-lane slowdown count | pending | 0 | n/a |
| Second-review rate | 1.0 for target lane | 1.0 for target lane | 0 |
| Insufficient-evidence rate | 1.0 for target lane | 1.0 for target lane | 0 |
| Raw-evidence leakage incidents | 0 required | 0 | 0 |

Across all 12 entries:

| Metric | Value |
|---|---:|
| Total context-gate review seconds | 300.0 |
| Average context-gate review seconds | 25.0 |
| Median context-gate review seconds | 27.5 |
| P95 context-gate review seconds | 30.45 |

## Lane Interpretation

| Lane role | Count | Result |
|---|---:|---|
| `target_thread_required` | 4 | 4/4 routed to `needs_thread_before_label`; 0 metadata-only overreach |
| `boundary_control` | 4 | 4/4 routed to second review before label; 0 thread over-request |
| `hard_negative_control` | 2 | 2/2 hard negatives preserved; 0 thread over-request |
| `fast_lane_control` | 2 | 2/2 metadata sufficient; 0 fast-lane slowdown |

## Validation

Validation command:

```bash
.venv/bin/python scripts/validate_reviewer_assist_context_gate_result.py
```

Validation result:

| Check | Count |
|---|---:|
| Required-field / aggregate errors | 0 |
| Source-packet alignment warnings | 0 |
| Initial source-packet warnings before reconciliation | 12 |
| Raw-evidence leakage incidents | 0 |

The initial source-packet alignment warnings were non-fatal traceability
warnings. They came from expected-behavior alias differences and from the
completed result using fast-lane controls `STUB_0008_A_01` / `STUB_0008_A_02`,
while the generated source packet used `STUB_0008_A_03` / `STUB_0008_A_04`.

Decision `0153` reconciled the controller work order, reviewer fill template,
packet generator, and regenerated reviewer-facing packet. The validator now
checks both reviewer-visible metadata and revised assist outputs against the
packet, and the current result validates with `0` source-packet alignment
warnings.

## Decision Slot

Selected option:

```text
adopt_context_gate_revision
```

Available options were:

- `adopt_context_gate_revision`;
- `revise_context_gate_again`;
- `keep_thread_required_lane_capped`;
- `pause_thread_required_lane`;
- `request_governed_thread_context_capture_design`.

Current decision: `adopt_context_gate_revision`

## Stop Conditions

Stop and do not synthesize a favorable result if:

- raw Threads text, raw reply text, raw OCR text, URL, handle, screenshot,
  browser/session artifact, credential, stakeholder case ID, or controlled-store
  locator enters tracked git files;
- the revised gate turns into a final scam, legal fraud, enforcement, or
  public-warning decision;
- reviewer-facing materials expose the prior assisted labels or times;
- review time is not recorded and no unavailable reason is given;
- controls are broadly over-routed into thread-required review;
- thread-required targets are confidently labeled from metadata-only evidence
  despite unresolved context;
- the result starts treating Batch `0012` or current case fragments as
  representative of all Threads investment scams.
