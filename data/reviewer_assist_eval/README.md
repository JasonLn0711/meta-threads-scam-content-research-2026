# Reviewer Assist Evaluation Data

This directory stores metadata-only work orders for Reviewer Assist
labor-savings evaluation.

Its purpose is to help evaluate whether assisted review can improve the repo's
single highest priority:

```text
Design a governed automatic or assisted method for discovering review-worthy
Threads investment-scam candidates.
```

## Allowed Content

- Candidate alias IDs
- Batch IDs
- Routing lanes
- Sparse metadata features
- Structured behavior hints
- Manual-baseline aggregate metrics
- Assisted-review fields that are pending human fill
- Context-gate revision fields that are pending human fill
- Aggregate-only comparison scaffolds

## Forbidden Content

Do not store:

- raw Threads post text;
- raw reply text;
- raw OCR text;
- URLs or handles;
- screenshots;
- browser/session artifacts;
- credentials, cookies, tokens, or secrets;
- controlled-store locators;
- stakeholder case IDs;
- private personal data.

## Current Work Orders

| Work order | Purpose | Status |
|---|---|---|
| `batch_0010_work_order.yaml` | Decision `0146` execution workbench for comparing Batch `0009` manual baseline with a metadata-only assisted-review condition | assisted-review result received |
| `batch_0010_assisted_review_result.yaml` | Completed metadata-only assisted-review fill for the Decision `0146` workbench | completed human fill |
| `batch_0010_aggregate_result.yaml` | Machine-readable aggregate-only result for Decision `0147` | completed aggregate result |
| `batch_0011_work_order.yaml` | Decision `0148` expansion workbench using Batch `0008` balanced context-gating baseline | empirical result completed |
| `batch_0011_reviewer_rules.md` | Reviewer-facing rule sheet for the Batch `0011` expansion slice | safe for reviewer |
| `batch_0011_reviewer_fill_sheet_template.yaml` | Reviewer-facing fill template with manual-baseline fields removed | safe for reviewer |
| `batch_0011_assisted_review_result.yaml` | Completed empirical metadata-only assisted-review fill for the Decision `0148` workbench | completed empirical result |
| `batch_0011_aggregate_result.yaml` | Machine-readable aggregate result for Decision `0149` | completed aggregate result |
| `batch_0012_work_order.yaml` | Decision `0150` context-gate revision workbench for the Batch `0011` thread-required bottleneck | completed; packet/source reconciled |
| `batch_0012_reviewer_rules.md` | Reviewer-facing rule sheet for the Batch `0012` context-gate revision | safe for reviewer |
| `batch_0012_reviewer_fill_sheet_template.yaml` | Reviewer-facing fill template with prior-assisted outcomes removed | safe for reviewer |
| `batch_0012_reviewer_context_gate_packet.yaml` | Reviewer-facing Batch `0012` context-gate packet with revised assist outputs filled and human reviewer fields blank | reconciled packet artifact |
| `batch_0012_context_gate_result.yaml` | Completed empirical metadata-only context-gate fill for Batch `0012` | completed empirical result |
| `batch_0012_aggregate_result.yaml` | Machine-readable aggregate result for Decision `0152` and reconciliation status for Decision `0153` | completed aggregate result; packet/source warnings resolved |
| `batch_0013_work_order.yaml` | Decision `0154` bounded context-gate reuse workbench on existing Batch `0009` metadata aliases | reviewer packet ready |
| `batch_0013_reviewer_rules.md` | Reviewer-facing rule sheet for Batch `0013` bounded reuse | safe for reviewer |
| `batch_0013_reviewer_fill_sheet_template.yaml` | Reviewer-facing fill template with prior baseline outcomes removed | safe for reviewer |
| `batch_0013_reviewer_context_gate_packet.yaml` | Reviewer-facing Batch `0013` context-gate packet with revised assist outputs filled and human reviewer fields blank | ready for human context-gate review |

## Use

Use these files as controller-side work orders. If a reviewer-facing packet is
created from them, it must hide manual-baseline labels, confidence, and review
times so the assisted condition does not simply copy prior decisions.

The current result syntheses belong in:

```text
experiments/evaluation-notes/0107-reviewer-assist-labor-savings-evaluation-result.md
experiments/evaluation-notes/0108-reviewer-assist-expansion-batch-0008-result.md
experiments/evaluation-notes/0109-reviewer-assist-thread-required-lane-revision-result.md
experiments/evaluation-notes/0110-reviewer-assist-context-gate-bounded-reuse-result.md
```

Batch `0012` has a separate reviewer-facing packet and result:

```text
data/reviewer_assist_eval/batch_0012_reviewer_context_gate_packet.yaml
data/reviewer_assist_eval/batch_0012_context_gate_result.yaml
data/reviewer_assist_eval/batch_0013_reviewer_context_gate_packet.yaml
```

The packet remains a packet artifact. The completed empirical result belongs in
the result file and must preserve raw-evidence exclusion. Decision `0153`
reconciled the Batch `0012` packet/source alignment, so the current packet
generator and result validator report `0` packet-alignment warnings. Batch
`0013` is packet-ready only; it must not be treated as an empirical result until
human reviewer fields are filled.
