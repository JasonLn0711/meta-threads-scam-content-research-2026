# 0106 - Reviewer Assist Labor-Savings Evaluation Start

Date: 2026-05-05

## Start State

The repo has recorded two priority corrections:

- Decision 0143: current cases are partial fragments, not the full Threads investment-scam population;
- Decision 0144: the single highest priority is designing a governed automatic or assisted method for discovering review-worthy Threads investment-scam candidates.

Batch 0009 supports the active context-gating policy and provides the immediate routing baseline for reviewer capacity.

## Evaluation Opened

Decision 0145 opens the Reviewer Assist labor-savings evaluation package.

The evaluation is designed to test whether assisted review can support automatic or assisted discovery by:

- reducing review time;
- reducing manual schema filling;
- improving summary usefulness;
- clarifying signal-family extraction;
- preserving hard-negative boundaries;
- improving priority routing;
- keeping human final judgment intact.

## Inputs

- `decision-log/0145-open-reviewer-assist-labor-savings-evaluation-for-automatic-discovery.md`
- `reports/reviewer-assist-labor-savings-evaluation-plan.md`
- `experiments/batch_variants/0010-reviewer-assist-labor-savings-evaluation.md`
- `docs/63-context-gating-policy.md`
- `docs/62-reviewer-assist-layer-design.md`
- `templates/reviewer_assist_labor_savings_worksheet.md`
- `templates/schema_prefill_correction_log_template.csv`
- `templates/summary_usefulness_rubric.md`
- `templates/signal_family_extraction_qa_table.csv`
- `templates/hard_negative_hesitation_log_template.csv`
- `templates/priority_ranking_evaluation_table.csv`
- `templates/labor_savings_aggregate_report_template.md`
- `templates/reviewer_assist_governance_checklist.md`

## Boundary

This start note does not authorize new data collection, live Threads access, real LLM/API calls, model training, crawler expansion, item `0082`, production detection, legal fraud determinations, enforcement recommendations, public warnings, or raw evidence in git.

## Next Work

Use the Decision `0146` execution workbench:

```text
data/reviewer_assist_eval/batch_0010_work_order.yaml
experiments/evaluation-notes/0107-reviewer-assist-labor-savings-evaluation-result.md
```

Fill a bounded metadata-only assisted-review slice. The result must remain
aggregate-only and must decide whether to expand, revise, keep shadow-only,
pause, or request a new governed source slice only after assisted-review fields
are filled.
