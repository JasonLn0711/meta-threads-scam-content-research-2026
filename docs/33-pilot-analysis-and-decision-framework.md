# Pilot Analysis And Decision Framework

## Purpose

This framework defines how the project turns the first authorized 50-item pilot into a defensible research decision.

It should be used after collection, annotation, QA, audit, adjudication, and rule-baseline comparison are complete. It does not authorize collection and should not be used with synthetic-only results to justify real-world claims.

## Decision Question

After the 50-item pilot, answer:

> Is the Threads scam-content research workflow stable enough to expand, or should we revise, narrow, or pause before collecting more real data?

## Required Inputs

Do not make an expansion decision until all inputs exist:

| Input | Expected artifact |
|---|---|
| Governance confirmation | `templates/data_authorization_request.md`, `governance/pilot-authorization-register.md` |
| Work order | `templates/pilot_batch_work_order.md` |
| Annotation QA | `templates/annotation_qa_checklist.md` |
| Dataset audit | `data/processed/threads_pilot_v1_audit.md` copied only as non-sensitive aggregate findings |
| Agreement/adjudication summary | generated agreement report plus adjudication notes |
| Baseline comparison | `data/processed/threads_pilot_v1_rule_variant_comparison.md` copied only as aggregate findings |
| Error analysis | `experiments/evaluation-notes/0001-pilot-error-analysis-template.md` or filled equivalent |
| Pilot result summary | `templates/pilot_result_summary.md` |
| Decision memo | `templates/pilot_decision_memo.md` |

Local files under `data/interim/` and `data/processed/` are ignored by git. Commit only aggregate, non-sensitive summaries.

## Decision Options

| Decision | Use when | Next action |
|---|---|---|
| `expand_to_100_200` | Governance worked, labels are usable, evidence fields are mostly complete, and baselines are interpretable. | Build the first usable dataset batch. |
| `revise_guideline_first` | Label disagreement or uncertainty shows unclear annotation rules. | Update guideline, rerun calibration, then collect/annotate more. |
| `revise_schema_first` | Fields are missing, confusing, too sensitive, or too slow to fill. | Update schema/docs/templates before expansion. |
| `narrow_sources` | Source mix is too skewed, low-quality, or privacy-heavy. | Restrict to source types that produce reviewable evidence. |
| `pause` | Authorization, privacy, capacity, or evidence quality makes expansion unsafe or unhelpful. | Stop real data work until blocker is resolved. |

Do not choose `expand_to_500` directly after the 50-item pilot. The next expansion target is 100-200 items. Use `docs/32-500-item-expansion-plan.md` only after the intermediate batch proves stable.

## Scoring Rubric

Use this as a structured judgment aid, not as a mechanical formula.

| Dimension | Green | Yellow | Red |
|---|---|---|---|
| Governance | Approved limits followed; no incidents | Minor ambiguity resolved during pilot | Authorization unclear or violated |
| Privacy/redaction | No raw personal data in git; redaction consistent | Minor redaction fixes needed | Sensitive data handling concern |
| Schema completeness | Required fields complete; missing evidence intentional | Repeated optional-field gaps | Required fields missing or confusing |
| Label quality | Primary labels mostly stable; disagreements explainable | Repeated edge-case disagreement | Labels unreliable for comparison |
| Evidence sufficiency | Most items sufficient or partial | Many partial cases but reviewable | Too many `insufficient_evidence` or not-reviewable cases |
| Source/content skew | Skew understood and acceptable for diagnostic sample | Skew limits some claims | Skew makes results misleading |
| Baseline usefulness | Reasons are evidence-backed; variants teach something | Some signal value but noisy | Baseline dominated by false positives or missing evidence |
| Reviewer burden | Annotation/review time is manageable | Burden high but reducible | Burden blocks continuation |

Recommended decision:

- mostly green: `expand_to_100_200`
- green/yellow mix with clear fixes: `revise_guideline_first`, `revise_schema_first`, or `narrow_sources`
- any red governance/privacy issue: `pause`

## Quantitative Warning Thresholds

Investigate before expansion if:

| Measure | Warning threshold |
|---|---:|
| `uncertain` labels | above 30 percent |
| `insufficient_evidence` labels | above 20 percent |
| primary-label disagreement | repeated same boundary |
| high-risk items without second review | any |
| validation errors | any unresolved |
| missing required fields | any unresolved |
| raw evidence in git | any |
| false positives concentrated in one benign category | repeated pattern |
| decisive OCR/reply/link evidence unavailable | repeated pattern |

Thresholds are not automatic rejection. They trigger a documented analysis and fix before expansion.

## Required Analysis Sections

The decision memo must cover:

1. Governance and privacy outcome.
2. Dataset composition and source skew.
3. Annotation quality and disagreement themes.
4. Evidence completeness and missing evidence.
5. Baseline variant comparison.
6. False positive and false negative themes.
7. Reviewer burden.
8. Guideline/schema/source revisions needed.
9. Recommended decision.
10. Follow-up owners and dates.

## Claims Allowed After The Pilot

Allowed:

- "In this diagnostic pilot..."
- "Among the approved pilot items..."
- "The workflow found..."
- "OCR/replies/link fields changed baseline decisions in these pilot cases..."
- "The pilot suggests the guideline should be revised..."

Not allowed:

- platform prevalence claims
- legal fraud claims
- production performance claims
- claims about uncollected Threads content
- claims that the baseline can enforce, detect, or adjudicate fraud

## Decision Record

After completing `templates/pilot_decision_memo.md`, create a decision-log entry with:

- pilot dataset ID
- authorization reference
- decision
- main evidence
- required revisions
- next review point

If the decision is expansion, update `docs/18-recommended-path-v1.md` or create a v2 recommended path.

