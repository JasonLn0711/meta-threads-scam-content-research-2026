# Decision 0145: Open Reviewer Assist Labor-Savings Evaluation For Automatic Discovery

Date: 2026-05-05

Status: opened as evaluation design package

## Decision

Open the Reviewer Assist labor-savings evaluation as the next governed research package after the single-priority correction in Decision 0144.

The evaluation must support the repo's highest priority:

```text
Design a governed automatic or assisted method for discovering review-worthy Threads investment-scam candidates.
```

This package evaluates whether Reviewer Assist can make the discovery method more operationally useful by reducing review burden without weakening human final judgment, hard-negative protection, evidence sufficiency, or source-boundary discipline.

## What This Opens

This decision opens:

- an experiment plan for a metadata-only assisted-review comparison;
- worksheet and log templates for schema prefill, summary usefulness, signal extraction, hard-negative hesitation, priority ranking, and labor savings;
- an aggregate report template for deciding whether assisted discovery should expand, revise, or pause.

## What This Does Not Open

This decision does not authorize:

- new Threads or Meta data collection;
- item `0082`;
- broad crawler expansion;
- private-message access;
- account/profile graph capture;
- landing-page or redirect-chain capture outside a later decision;
- model training;
- real LLM/API calls;
- production detector claims;
- legal fraud determinations;
- enforcement recommendations;
- public warnings;
- raw evidence in git.

## Context

Decision 0143 records that current cases are partial fragments and cannot be treated as the complete Threads investment-scam population. Decision 0144 records that automatic or assisted discovery-method design is the single highest project priority.

Batch 0009 supports the active context-gating policy as a reviewer-capacity routing base. The next step is not to summarize current cases. The next step is to test whether assisted review can help the automatic or assisted discovery method surface, prioritize, and validate review-worthy candidates with less human burden.

## Required Comparison

The evaluation should compare a manual-review baseline against an assisted-review condition on comparable metadata-only slices.

The assisted condition may include:

- repo-safe candidate summary;
- signal-family extraction;
- schema prefill draft;
- hard-negative warning;
- priority explanation;
- missing-evidence note;
- second-review suggestion.

Every assisted output must preserve:

- human final label and risk decision;
- uncertainty;
- evidence references without raw evidence;
- hard-negative checks;
- reviewer override;
- aggregate-only reporting.

## Success Conditions

This evaluation supports the discovery method only if it shows:

- lower average, median, or p95 review time;
- higher reviewed candidates per hour or high-value candidates per reviewer hour;
- acceptable schema-prefill acceptance rate;
- controlled schema-prefill correction rate;
- useful summaries without hiding decisive context;
- no increase in hard-negative false-positive pressure;
- no unacceptable increase in second-review or disagreement rate;
- no raw-evidence leakage;
- no shift toward final automated scam decisions.

## Failure Conditions

Pause or revise the assisted-review design if:

- reviewer time is not reduced;
- prefill creates high correction burden;
- summaries omit decisive reply, OCR, or hard-negative context;
- priority ranking overfits current fragments;
- hard-negative false-positive pressure rises;
- second-review or disagreement rate increases without clear benefit;
- the evaluation starts treating existing cases as representative of all Threads investment scams;
- any scope, privacy, or raw-evidence boundary is violated.

## Artifacts

- `reports/reviewer-assist-labor-savings-evaluation-plan.md`
- `experiments/batch_variants/0010-reviewer-assist-labor-savings-evaluation.md`
- `experiments/evaluation-notes/0106-reviewer-assist-labor-savings-evaluation-start.md`
- `templates/reviewer_assist_labor_savings_worksheet.md`
- `templates/schema_prefill_correction_log_template.csv`
- `templates/summary_usefulness_rubric.md`
- `templates/signal_family_extraction_qa_table.csv`
- `templates/hard_negative_hesitation_log_template.csv`
- `templates/priority_ranking_evaluation_table.csv`
- `templates/labor_savings_aggregate_report_template.md`
- `templates/reviewer_assist_governance_checklist.md`

## Next Review Point

After filling a bounded assisted-review slice, produce an aggregate-only result note. The decision should be one of:

- `expand_assist_evaluation`;
- `revise_assist_design`;
- `keep_shadow_only`;
- `pause_assist_layer`;
- `request_new_governed_source_slice`.
