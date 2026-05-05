# Codex Workflow

## Operating Rule

Codex should treat this repo as a research operating system, not an app project. The correct default is to improve the first-principle discovery method: scalable, stable, and reviewable discovery of Threads investment-scam candidates.

Before making a substantial change, state how it advances candidate discovery, signal-family learning, evidence completeness, hard-negative protection, reviewer workflow, discovery-yield measurement, or a capped method-test decision.

## Start Here

Before making changes, read:

1. `README.md`
2. `docs/00-project-charter.md`
3. `docs/61-labor-efficient-investment-scam-candidate-discovery-north-star.md`
4. `docs/62-reviewer-assist-layer-design.md`
5. `docs/63-context-gating-policy.md`
6. `docs/65-evidence-layer-v1.md`
7. `docs/66-closed-loop-discovery-v1.md`
8. `docs/18-recommended-path-v1.md`
9. `docs/56-first-principle-investment-scam-discovery-method.md`
10. `docs/57-investment-scam-discovery-signal-family-matrix.md`
11. `governance/data-governance.md`
12. `AGENTS.md`
13. `docs/21-repo-relationships.md`

## Docs-First Updates

Before adding or changing code:

- Define the research question.
- Define how the change advances the investment-scam discovery-method goal.
- Define the dataset fields.
- Define the annotation label impact.
- Define the experiment log.
- Confirm the change fits budget and scope.

## Decision Logging

Create a decision record when changing:

- Scope
- Data collection method
- Annotation labels
- Dataset schema
- Baseline family
- Model strategy
- Budget assumption
- Production boundary
- Relationship to the umbrella repo or planning repo
- The first-principle discovery-method goal

## Branch Naming

Recommended branches:

- `docs/taxonomy-v1`
- `docs/data-strategy`
- `experiment/text-rule-baseline`
- `experiment/ocr-ablation`
- `experiment/comment-context`
- `governance/data-access`

## Dataset Contracts

Do not rely on a new field until it is added to:

- `docs/07-dataset-schema.md`
- `data-contracts/thread_item_schema_v1.json`
- `templates/annotation_sheet_template.csv` when spreadsheet annotation is affected

## Cross-Repo Routing

- Put weekly priority, status, and next actions in `../planning-everything-track`.
- Put broad Meta scam-risk strategy and cross-platform scope decisions in `../meta-scam-ad-research-2026`.
- Put Threads-specific schema, annotation, experiment, and evaluation details in this repo.
- Link across repos when useful; do not duplicate live research artifacts.

## Experiment Trace

Every experiment must leave a written trace:

- Hypothesis
- Dataset slice
- Method
- Cost
- Result
- Error analysis
- Decision implication

Use `docs/17-experiment-log-template.md` or `templates/experiment_log_template.md`.

## Code Restraint

Allowed early code:

- Schema validation
- CSV/JSONL conversion
- Simple rule baseline
- Metric calculation
- OCR normalization for approved local files
- Evidence integrity hashing, audit-chain checks, and metadata-only candidate stubs
- Synthetic closed-loop simulations for query-arm value and reviewer-hour metrics

Avoid:

- Scrapers
- Automated Threads collection
- Heavy ML training
- Web dashboards
- Production services
- Large dependency stacks
- Raw locators, handles, screenshots, URLs, or sensitive evidence in git-facing candidate records

## Safety Language

Use:

- "scam-like"
- "high-risk"
- "triage"
- "signals"
- "review support"
- "uncertain"
- "insufficient evidence"

Avoid:

- "confirmed fraud"
- "criminal"
- "automatic enforcement"
- "platform-wide detection"
- "production-ready"
