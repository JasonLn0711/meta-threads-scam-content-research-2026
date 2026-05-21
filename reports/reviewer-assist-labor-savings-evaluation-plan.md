# Reviewer Assist Labor-Savings Evaluation Plan

## Purpose

Evaluate whether Reviewer Assist improves the repo's single highest priority:

```text
Design a governed automatic or assisted method for discovering review-worthy Threads investment-scam candidates.
```

This plan measures whether assisted review improves the discovery method by reducing human review burden while preserving candidate quality, hard-negative protection, uncertainty, evidence sufficiency, and human final judgment.

This is not a case-summary exercise. Current reviewed examples are partial fragments. They may be used as calibration and evaluation slices, but they must not be treated as representative of all Threads investment scams.

## Evaluation Question

```text
Does Reviewer Assist help the governed discovery method find, route, and review
review-worthy Threads investment-scam candidates with less human burden and
without increasing false-positive, hard-negative, or governance risk?
```

## Conditions Compared

| Condition | Description | Allowed Inputs | Outputs |
|---|---|---|---|
| Manual baseline | Reviewer works from existing repo-safe metadata and current review guidance | Structured metadata only | Human label, risk, burden fields, hesitation notes |
| Assisted review | Reviewer receives repo-safe summary, signal hints, schema-prefill draft, hard-negative warning, and priority explanation | Structured metadata only | Human label, accepted/corrected/rejected assist outputs, burden fields |

Both conditions must use comparable source lanes or candidate slices. If the slices differ, the report must state that the comparison is exploratory only.

## Source Boundary

Allowed:

- existing repo-safe metadata;
- existing reviewed slices;
- synthetic or metadata-only stubs;
- governed future slices opened by a later decision;
- aggregate metrics from prior Batch 0008 and Batch 0009 results.

Not allowed:

- raw Threads text;
- raw reply text;
- raw OCR text;
- raw URLs or handles;
- screenshots;
- browser/session artifacts;
- credentials;
- controlled-store locators;
- stakeholder case IDs;
- new external collection without a later governed decision.

## Assist Outputs To Evaluate

| Assist output | What it should do | What to measure |
|---|---|---|
| Candidate summary | Reduce default reading burden | Summary usefulness, full-thread-read rate, omission risk |
| Signal-family extraction | Surface visible candidate signals | Acceptance/correction/rejection rate |
| Schema prefill | Reduce manual field entry | Field acceptance and correction burden |
| Hard-negative warning | Protect ordinary/warning content | Hard-negative hesitation and false-positive pressure |
| Priority explanation | Route scarce reviewer time | Priority correctness, disagreement, over-prioritization |
| Missing-evidence note | Preserve uncertainty | Insufficient-evidence rate and second-review reason |

Assist outputs may suggest. They must not decide.

## Required Metrics

| Metric | Manual baseline | Assisted review | Decision use |
|---|---:|---:|---|
| reviewed candidates |  |  | Denominator |
| average review time |  |  | Mean labor burden |
| median review time |  |  | Typical labor burden |
| p95 review time |  |  | Long-tail risk |
| candidates reviewed per hour |  |  | Throughput |
| high-value candidates per reviewer hour |  |  | Discovery value |
| full-thread-read rate |  |  | Residual reading burden |
| summary usefulness mean | n/a |  | Summary value |
| schema-prefill acceptance rate | n/a |  | Field-assist quality |
| schema-prefill correction rate | n/a |  | Hidden correction burden |
| signal extraction correction rate | n/a |  | Signal-assist quality |
| priority ranking acceptance rate | n/a |  | Routing value |
| second-review rate |  |  | Ambiguity pressure |
| reviewer disagreement rate |  |  | Review stability |
| hard-negative false-positive pressure |  |  | Governance/trust risk |
| insufficient-evidence rate |  |  | Evidence-quality pressure |
| raw-evidence leakage incidents | 0 required | 0 required | Stop condition |

## Minimum Done Condition

The evaluation package is ready for result synthesis only when:

- every entry has a human final label or explicit `not_reviewable`;
- every assisted output is marked accepted, corrected, rejected, or not applicable;
- every correction has a repo-safe category;
- review time is recorded or explicitly marked unavailable;
- hard-negative and insufficient-evidence checks are complete;
- raw-evidence exclusion is confirmed;
- aggregate-only reporting tables can be filled.

## Execution Workbench

Decision `0146` opens the fillable execution workbench:

- `data/reviewer_assist_eval/batch_0010_work_order.yaml`
- `experiments/evaluation-notes/0107-reviewer-assist-labor-savings-evaluation-result.md`

Batch `0009` is the manual baseline. The assisted-review condition remains
filled in `data/reviewer_assist_eval/batch_0010_assisted_review_result.yaml`.
Decision `0147` records the aggregate-only result and selects
`expand_assist_evaluation`. The reviewer-facing packet must hide
manual-baseline labels, confidence, review times, and second-review decisions.

## Decision Rule

Use this rule after the aggregate report is filled:

| Result pattern | Decision |
|---|---|
| Review time drops, correction burden is low, hard-negative pressure stable | `expand_assist_evaluation` |
| Review time drops but correction or hesitation burden is high | `revise_assist_design` |
| Priority routing helps but assist text is unstable | `keep_shadow_only` |
| No labor gain or higher disagreement/hard-negative pressure | `pause_assist_layer` |
| Existing slices are too biased to answer the question | `request_new_governed_source_slice` |

## Guardrails

- Do not claim platform-wide coverage.
- Do not infer a complete taxonomy from current cases.
- Do not make final scam, legal, enforcement, or public-warning decisions.
- Do not use real LLM/API calls unless a later decision authorizes them.
- Do not turn the evaluation into a UI, dashboard, product, or production detector.
- Keep all outputs repo-safe and aggregate-only.
