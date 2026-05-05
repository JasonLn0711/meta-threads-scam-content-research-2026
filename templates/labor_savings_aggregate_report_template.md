# Labor-Savings Aggregate Report Template

Use this template after a bounded Reviewer Assist labor-savings slice is filled.

Do not include raw Threads evidence, raw OCR, URLs, handles, screenshots, browser/session artifacts, credentials, controlled-store locators, or stakeholder case IDs.

## Slice Identity

| Field | Value |
|---|---|
| `slice_id` |  |
| `comparison_type` | paired / comparable_slice / exploratory |
| `manual_baseline_count` |  |
| `assisted_review_count` |  |
| `source_lanes_compared` |  |
| `raw_evidence_excluded_from_git` | yes / no |

## Labor Summary

| Metric | Manual baseline | Assisted review | Difference |
|---|---:|---:|---:|
| Average review seconds |  |  |  |
| Median review seconds |  |  |  |
| P95 review seconds |  |  |  |
| Candidates reviewed per hour |  |  |  |
| Full-thread-read rate |  |  |  |
| Second-review rate |  |  |  |
| Disagreement rate |  |  |  |

## Assist Quality

| Metric | Value |
|---|---:|
| Summary usefulness mean |  |
| Summary rating 4-5 percent |  |
| Schema-prefill acceptance rate |  |
| Schema-prefill correction rate |  |
| Signal extraction correction rate |  |
| Priority ranking acceptance rate |  |
| Hard-negative warning acceptance rate |  |

## Discovery Method Effect

| Metric | Manual baseline | Assisted review | Difference |
|---|---:|---:|---:|
| Review-worthy yield |  |  |  |
| High-value candidates per reviewer hour |  |  |  |
| Insufficient-evidence rate |  |  |  |
| Hard-negative false-positive pressure |  |  |  |
| Duplicate or near-duplicate rate |  |  |  |

## Decision

Select one:

- `expand_assist_evaluation`;
- `revise_assist_design`;
- `keep_shadow_only`;
- `pause_assist_layer`;
- `request_new_governed_source_slice`.

## Rationale

- Main labor-saving evidence:
- Main correction-burden concern:
- Main hard-negative or false-positive concern:
- Main sample-bias limitation:
- Recommended next bounded slice:
