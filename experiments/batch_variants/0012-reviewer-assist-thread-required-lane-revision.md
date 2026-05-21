# 0012 - Reviewer Assist Thread-Required Lane Revision

Status: open for human fill under Decision `0150`

## Purpose

Test a revised Reviewer Assist context gate for the
`result_display_thread_required` lane.

Batch `0011` reduced review time overall, but the thread-required lane stayed
slow and uncertain. Batch `0012` therefore shifts the evaluation question from
"can the assistant help label this metadata-only item?" to "can the assistant
quickly identify when a metadata-only item should not be labeled yet?"

## First-Principle Question

```text
Can Reviewer Assist reduce wasted review time on thread-dependent candidates by
routing them to the correct context-first next action, without over-requesting
thread context for fast-lane or hard-negative controls?
```

## Baseline From Batch 0011

Thread-required lane:

```text
count: 4
assisted_total_review_time_seconds: 207.0
assisted_average_review_time_seconds: 51.75
uncertain_count: 4
second_review_required_count: 4
insufficient_evidence_count: 4
```

Controls:

```text
strong_source_priority_assisted_average_review_time_seconds: 23.0
result_display_low_context_transition_assisted_average_review_time_seconds: 33.75
result_display_clean_holdout_assisted_average_review_time_seconds: 24.0
```

## Slice Design

| Role | Lane | Count | Purpose |
|---|---|---:|---|
| Target | `result_display_thread_required` | 4 | Test early context dependency routing |
| Boundary control | `result_display_low_context_transition` | 4 | Ensure low-context boundary cases are not over-routed |
| Hard-negative control | `result_display_clean_holdout` | 2 | Preserve hard-negative calibration |
| Fast-lane control | `strong_source_priority` | 2 | Ensure context gate does not slow strong fast-lane cases |

## Revised Assist Outputs

For each candidate, prepare:

- `context_dependency_gate`;
- `context_reason_codes`;
- `minimal_context_needed`;
- `safe_next_action`;
- `metadata_label_guardrail`;
- `priority_explanation`;
- `missing_evidence_note`;
- `second_review_suggestion`.

These are assist outputs for human review. They do not make final scam, legal
fraud, enforcement, or public-warning determinations.

## Success Metrics

Measure:

- context-gate review time;
- accepted/corrected/rejected rate for the context gate;
- rate of correct `needs_thread_before_label` routing for thread-required
  targets;
- over-request rate on low-context, clean-holdout, and fast-lane controls;
- under-request risk;
- second-review rate;
- insufficient-evidence rate;
- hard-negative protection;
- raw-evidence leakage incidents.

## Work Order

Fill:

```text
data/reviewer_assist_eval/batch_0012_work_order.yaml
```

Use the reviewer-facing rules and fill template:

```text
data/reviewer_assist_eval/batch_0012_reviewer_rules.md
data/reviewer_assist_eval/batch_0012_reviewer_fill_sheet_template.yaml
```

## Expected Result Note

After human fill, update:

```text
experiments/evaluation-notes/0109-reviewer-assist-thread-required-lane-revision-result.md
```

## Guardrails

- No new collection.
- No raw evidence in git.
- No real LLM/API calls.
- No model training.
- No final automated scam decisions.
- No legal, enforcement, public-warning, or production-detector claims.
- Do not treat Batch `0012` as representative of all Threads investment scams.
