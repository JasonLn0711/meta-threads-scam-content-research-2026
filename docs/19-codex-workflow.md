# Codex Workflow

## Operating Rule

Codex should treat this repo as a research operating system, not an app project. The correct default is to improve the first-principle discovery method: scalable, stable, and reviewable discovery of Threads investment-scam candidates.

Before making a substantial change, state how it advances candidate discovery, signal-family learning, evidence completeness, hard-negative protection, reviewer workflow, discovery-yield measurement, or a capped method-test decision.

## Start Here

Before making changes, read:

1. `README.md`
2. `docs/00-project-charter.md`
3. `docs/61-labor-efficient-investment-scam-candidate-discovery-north-star.md`
4. `docs/73-authorized-threads-discovery-method-v1.md`
5. `docs/62-reviewer-assist-layer-design.md`
6. `docs/63-context-gating-policy.md`
7. `docs/65-evidence-layer-v1.md`
8. `docs/66-closed-loop-discovery-v1.md`
9. `docs/67-advanced-discovery-v2.md`
10. `docs/68-concept-reasoning-layer-v1.md`
11. `docs/69-dynamic-intelligence-layer-v1.md`
12. `docs/70-predictive-simulation-layer-v1.md`
13. `docs/71-defensive-self-play-layer-v1.md`
14. `docs/72-adaptive-policy-deployment-loop-v1.md`
15. `docs/18-recommended-path-v1.md`
16. `docs/51-meta-content-library-api-access.md`
17. `docs/52-automated-versioning-and-change-log.md`
18. `docs/53-first-principle-meta-research-tools-application-strategy.md`
19. `docs/56-first-principle-investment-scam-discovery-method.md`
20. `docs/57-investment-scam-discovery-signal-family-matrix.md`
21. `governance/data-governance.md`
22. `AGENTS.md`
23. `docs/21-repo-relationships.md`

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

Recent access and versioning decisions live in:

- `0157-record-breeze-guard-26-as-deferred-candidate.md`
- `0158-require-meta-content-library-api-route.md`
- `0159-add-automated-versioning-and-change-log.md`
- `0160-record-first-principle-meta-research-tools-application-strategy.md`

For CIB/165 Threads research, default to Meta Content Library / API application
prep and official access checks before falling back to any browser source-arm
design. Use the regular Threads API only as a bounded supplementary route with
explicit endpoint, permission, field, date-range, query-count, and retention
limits.

## Version Logging

Before finishing a governed repo change, decide whether to bump the repo
operating version under `docs/52-automated-versioning-and-change-log.md`.

Use:

```bash
python3 scripts/record_version_update.py --bump patch \
  --summary "Short repo-safe summary" \
  --category governance \
  --path docs/example.md \
  --detail "Repo-safe detail." \
  --verification "git diff --check"
```

This updates `VERSION`, prepends `CHANGELOG.md`, and appends
`versioning/version_log.csv`. Do not include raw Threads evidence, source URLs,
handles, screenshots, credentials, browser artifacts, or controlled run details
in version entries.

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
- Synthetic prompt-shaped query generation, local embeddings, local clustering, and contextual bandit simulations
- Synthetic cluster-to-concept reasoning and conservative novelty routing
- Synthetic concept graph, temporal tracking, evolution, and adversarial-adaptation heuristics
- Synthetic predictive simulation, subtle concept mutation, risk scoring, and validation hooks

Avoid:

- Scrapers
- Automated Threads collection
- Personal-account browser crawling as a standing method
- One-second automated browser fetching as a default control
- Real LLM/API calls without a new decision and governance boundary
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
