# AGENTS.md

This repository is a documentation-first research operating system for Threads-related scam or scam-like content research within the Meta ecosystem.

## Mission

Support a serious, budget-aware research program for studying scam-like content on Meta Threads. From this point forward, the repo has one non-negotiable top priority: design a governed automatic or assisted method for discovering review-worthy Threads investment-scam candidates. Scalability, stability, reviewability, labor efficiency, governance, evidence handling, hard-negative protection, and reviewer assistance are support requirements for that discovery-method goal.

The current collected cases are partial fragments, not a representative sample of all Threads investment scams. Agents must not treat existing cases as the full population, infer a complete taxonomy from them, or claim platform-wide coverage from them. Use existing cases as hypotheses, seeds, hard-negative controls, workflow examples, and evaluation slices.

The project purpose is governed automatic or assisted discovery design: finding review-worthy Threads investment-scam candidates beyond the current fragments, then testing whether source arms, signals, summaries, and priority rules generalize under bounded review. Other goals are subordinate to this purpose and must not contradict it.

The repo should help researchers, investigators, reviewers, professors, and engineers define the problem, structure evidence, annotate examples, run narrow experiments, measure discovery yield and reviewer burden together, reduce avoidable review labor, and decide what is worth building next.

The project is a research scaffold, not a production detector.

## First-Principle Direction

Every substantial change must serve the automatic or assisted investment-scam discovery method. It should support at least one of:

- investment-scam candidate discovery;
- labor-efficient review-worthy candidate discovery;
- signal-family learning;
- full-thread/reply-aware evidence capture;
- hard-negative protection;
- dedupe and source-linkage quality;
- reviewer workflow and second-review clarity;
- discovery-yield and reviewer-burden measurement;
- reviewer-assist, schema-prefill, summary-assisted review, priority-ranking, and labor-savings evaluation;
- Reviewer Assist Layer design when it reduces reading, summarization, signal extraction, schema filling, triage, or reporting burden without replacing human decisions;
- capped discovery experiment design;
- future expansion from investment scams to other scam families.

Package, governance, readiness, and shadow-pilot artifacts are support structures for this goal. They are not the final goal by themselves.

Do not frame labor reduction as a secondary convenience. Discovery yield and reviewer burden are coupled success conditions: a high-yield method that requires excessive manual reading, copying, summarizing, and schema filling is not operationally scalable, and a low-burden method that does not surface enough review-worthy candidates is not useful.

## Repo Series Naming

This repo follows the series pattern:

```text
meta-[scope]-[risk-domain]-[content-surface]-research-[year]
```

Examples:

- `meta-scam-ad-research-2026`
- `meta-threads-scam-content-research-2026`
- `meta-instagram-scam-content-research-2026`
- `meta-facebook-scam-page-research-2026`

Use `scam` instead of `fraud` unless a legal determination is actually in scope. Use `research` to avoid implying a production system. Use the year to preserve budgeting and project lineage.

## Hard Boundaries

1. Do not automate Threads or Meta data collection without explicit written authorization, approved API access, and legal or stakeholder approval recorded in `governance/data-governance.md`.
2. Do not commit raw personal data, credentials, browser exports, screenshots containing unnecessary personal information, or sensitive investigative material.
3. Do not claim that this project can solve full-platform scam detection or make legal determinations.
4. Do not convert this repo into a web app, dashboard, database product, or heavy ML platform unless a later decision log explicitly authorizes that scope.
5. Preserve uncertainty. Suspicion is not guilt, and weak evidence must stay labeled as weak evidence.
6. Do not use AI/system support to make final scam determinations, legal fraud determinations, enforcement recommendations, public warnings, automated takedowns, or production detector claims.

## Working Style

- Prefer Markdown, CSV, JSONL, and small Python utilities only when experiments justify code.
- Keep the repo documentation-first, research-second, code-third.
- Define data contracts before relying on new fields.
- Update taxonomy and annotation guidance before changing labels.
- Every experiment must state hypothesis, data slice, method, cost, results, failure modes, and decision implications.
- Every model or rule output must preserve explainable reasons and evidence references.
- Every reviewer-assist output must preserve human override, uncertainty, hard-negative checks, and repo-safe evidence references.
- Future experiments should measure average/median/p95 review time, candidates reviewed per hour, field auto-fill and correction rates, summary usefulness, full-thread-reading rate, second-review rate, reviewer disagreement rate, hard-negative false-positive pressure, insufficient-evidence rate, review-worthy yield per source arm, and high-risk yield per reviewer hour when relevant.
- Legal, platform, and privacy constraints are research constraints, not afterthoughts.

## Future Agent Workflow

Start with:

1. `README.md`
2. `docs/00-project-charter.md`
3. `docs/61-labor-efficient-investment-scam-candidate-discovery-north-star.md`
4. `docs/62-reviewer-assist-layer-design.md`
5. `docs/63-context-gating-policy.md`
6. `docs/65-evidence-layer-v1.md`
7. `docs/66-closed-loop-discovery-v1.md`
8. `docs/67-advanced-discovery-v2.md`
9. `docs/68-concept-reasoning-layer-v1.md`
10. `docs/69-dynamic-intelligence-layer-v1.md`
11. `docs/70-predictive-simulation-layer-v1.md`
12. `docs/71-defensive-self-play-layer-v1.md`
13. `docs/72-adaptive-policy-deployment-loop-v1.md`
14. `docs/18-recommended-path-v1.md`
15. `docs/56-first-principle-investment-scam-discovery-method.md`
16. `docs/57-investment-scam-discovery-signal-family-matrix.md`
17. `governance/data-governance.md`
18. `docs/19-codex-workflow.md`
19. `docs/20-repo-series-naming.md`
20. `docs/21-repo-relationships.md`

Before changing scope, update:

- `docs/02-scope-and-prioritization.md`
- `docs/11-budget-fit-analysis.md`
- `decision-log/`

Before changing annotation labels, update:

- `docs/04-taxonomy.md`
- `docs/06-annotation-guideline-v1.md`
- `data-contracts/thread_item_schema_v1.json`

Before adding experiments, create or update an experiment log under:

- `experiments/modality-studies/`
- `experiments/baselines/`
- `experiments/evaluation-notes/`

Keep `scripts/` and `src/` minimal until experiments justify code.
