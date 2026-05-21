# 0013 - Reviewer Assist Context-Gate Bounded Reuse

Status: open for human fill under Decision `0154`

## Purpose

Use the reconciled Batch `0012` context gate in a smaller bounded slice to test
whether the gate can be reused without introducing packet/source drift, hard-
negative over-request, or fast-lane slowdown.

This is not a new collection run. It uses existing Batch `0009` metadata-safe
candidate aliases.

## First-Principle Question

```text
Can the reconciled context gate reduce reviewer-hour waste on a policy-weighted
metadata slice while preserving uncertainty, hard negatives, and fast lanes?
```

## Hypothesis

If the Batch `0012` context gate is reusable, the Batch `0013` human-filled
result should show:

- the thread-required target routed to `needs_thread_before_label`;
- the low-context boundary control routed to second review or uncertainty
  without a thread request by habit;
- clean result-display holdouts preserved as hard negatives;
- strong-source priority controls left metadata sufficient;
- raw-evidence leakage remains `0`;
- packet/source alignment remains `0` warnings at packet-generation time.

## Slice Design

| Role | Lane | Count | Source |
|---|---|---:|---|
| Target | `result_display_thread_required` | 1 | Batch `0009` D |
| Boundary control | `result_display_low_context_transition` | 1 | Batch `0009` C |
| Hard-negative control | `result_display_clean_holdout` | 2 | Batch `0009` B |
| Fast-lane control | `strong_source_priority` | 4 | Batch `0009` A |

## Baseline Snapshot

The selected Batch `0009` metadata records have a prior baseline total review
time of `303.0` seconds and average review time of `37.875` seconds. Those
prior labels and times are controller-side references only and must not be
shown in the reviewer-facing packet.

## Work Order

Controller-side work order:

```text
data/reviewer_assist_eval/batch_0013_work_order.yaml
```

Reviewer-facing rules and packet:

```text
data/reviewer_assist_eval/batch_0013_reviewer_rules.md
data/reviewer_assist_eval/batch_0013_reviewer_context_gate_packet.yaml
```

## Expected Result Note

After human fill, update:

```text
experiments/evaluation-notes/0110-reviewer-assist-context-gate-bounded-reuse-result.md
```

## Guardrails

- No new collection.
- No raw evidence in git.
- No browser/API automation.
- No real LLM/API calls.
- No model training.
- No final automated scam decisions.
- No legal, enforcement, public-warning, or production-detector claims.
- Do not treat Batch `0013`, Batch `0009`, or current fragments as
  representative of all Threads investment scams.
