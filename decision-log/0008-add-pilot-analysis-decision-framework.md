# Decision 0008: Add Pilot Analysis Decision Framework

## Identity

- Date: 2026-04-23
- Status: accepted
- Owner: Jason

## Decision

Add a post-pilot analysis and decision framework before any expansion beyond the first authorized 50-item pilot.

The project must decide whether to expand, revise, narrow, or pause using a full evidence bundle: governance outcome, annotation QA, dataset audit, agreement/adjudication, baseline comparison, error analysis, reviewer burden, and evidence completeness.

## Context

The project already has collection, authorization, annotation, QA, dry-run, and expansion-planning docs. The remaining gap was how to convert pilot outputs into a defensible decision.

Without a decision framework, the project could overreact to a single metric, such as baseline F1, and miss governance, label-quality, privacy, evidence, or reviewer-burden problems.

## Options Considered

| Option | Pros | Cons | Decision |
|---|---|---|---|
| Decide expansion informally after pilot | Fast | Easy to overclaim or miss blockers | Rejected |
| Use baseline metrics only | Simple | Ignores governance, annotation quality, evidence gaps, and reviewer burden | Rejected |
| Require structured pilot decision memo | Slower but defensible | Adds one more summary artifact | Accepted |

## Rationale

The first real pilot is a research gate, not a production benchmark. A structured decision memo keeps the project honest about:

- whether data handling worked
- whether labels are reliable enough
- whether evidence fields are complete enough
- whether baselines are interpretable
- whether OCR, replies, links, and redirects actually add value
- whether the next useful action is expansion or revision

## Consequences

Use:

- `docs/33-pilot-analysis-and-decision-framework.md`
- `templates/pilot_decision_memo.md`
- `templates/baseline_error_review_table.csv`
- `experiments/evaluation-notes/0003-pilot-decision-analysis-protocol.md`

Do not expand to 100-200 or 500 items until the pilot decision memo is complete and a decision-log entry records the outcome.

## Next Review

Review after the first authorized 50-item pilot completes.

