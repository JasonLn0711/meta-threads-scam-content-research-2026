# Codex Workflow

## Operating Rule

Codex should treat this repo as a research operating system, not an app project. The correct default is to improve research clarity, data contracts, experiment design, and decision records before adding code.

## Start Here

Before making changes, read:

1. `README.md`
2. `docs/00-project-charter.md`
3. `docs/18-recommended-path-v1.md`
4. `governance/data-governance.md`
5. `docs/52-automated-versioning-and-change-log.md`
6. `AGENTS.md`
7. `docs/21-repo-relationships.md`

## Docs-First Updates

Before adding or changing code:

- Define the research question.
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

## Version Logging

When a repo-safe change should move the repository operating version, use:

```bash
python3 scripts/record_version_update.py --bump patch \
  --summary "Repo-safe summary" \
  --category governance \
  --path docs/example.md \
  --verification "git diff --check"
```

Use [52-automated-versioning-and-change-log.md](52-automated-versioning-and-change-log.md) to choose `major`, `minor`, or `patch`. Do not put raw evidence, handles, controlled URLs, credentials, screenshots, browser exports, or controlled item-level details in the version log.

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

Avoid:

- Scrapers
- Automated Threads collection
- Heavy ML training
- Web dashboards
- Production services
- Large dependency stacks

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
