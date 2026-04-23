# AGENTS.md

This repository is a documentation-first research operating system for Threads-related scam or scam-like content research within the Meta ecosystem.

## Mission

Support a serious, budget-aware research program for studying scam-like content on Meta Threads. The repo should help researchers, investigators, reviewers, professors, and engineers define the problem, structure evidence, annotate examples, run narrow experiments, and decide what is worth building next.

The project is a research scaffold, not a production detector.

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

## Working Style

- Prefer Markdown, CSV, JSONL, and small Python utilities only when experiments justify code.
- Keep the repo documentation-first, research-second, code-third.
- Define data contracts before relying on new fields.
- Update taxonomy and annotation guidance before changing labels.
- Every experiment must state hypothesis, data slice, method, cost, results, failure modes, and decision implications.
- Every model or rule output must preserve explainable reasons and evidence references.
- Legal, platform, and privacy constraints are research constraints, not afterthoughts.

## Future Agent Workflow

Start with:

1. `README.md`
2. `docs/00-project-charter.md`
3. `docs/18-recommended-path-v1.md`
4. `governance/data-governance.md`
5. `docs/19-codex-workflow.md`
6. `docs/20-repo-series-naming.md`
7. `docs/21-repo-relationships.md`

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
