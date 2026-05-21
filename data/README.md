# Data Directory

This directory supports the first Threads scam-content research dataset package. It is for dataset layout, local staging, and safe sample documentation. It is not a place to commit raw evidence.

Do not commit raw Threads data, personal data, screenshots with unnecessary personal information, browser exports, credentials, tokens, cookies, or sensitive investigative material.

## Layout

```text
data/
  raw/          local-only approved source evidence
  interim/      local-only normalized working files
  processed/    local-only analysis-ready exports unless explicitly cleared
  reviewer_assist_eval/ metadata-only Reviewer Assist evaluation work orders and aggregate results
  samples/      safe synthetic or redacted examples only
  predictions/  ignored synthetic predictive simulation logs
  selfplay/     ignored defensive self-play simulation logs
  policy/       ignored adaptive policy decision, feedback, evaluation, and state logs
  concept_graph.yaml        ignored synthetic concept graph
  concept_time_series.yaml  ignored synthetic concept time series
  adversarial_patterns.yaml ignored synthetic adversarial findings
```

## Commit Rules

- `README.md` files and synthetic/redacted sample documentation are safe to commit.
- Raw screenshots, copied posts, browser exports, or stakeholder case files are not safe to commit.
- Any real dataset slice must have authorization recorded in `governance/data-governance.md`.
- Any dataset used in an experiment should record schema version, annotation guideline version, source type, collection method, sample size, privacy handling, known bias, and allowed uses.
- Reviewer Assist evaluation files may store structured metadata, routing lanes, human-fill fields, and aggregate results, but not raw evidence or reviewer-facing copies with hidden baseline labels exposed.

## First Dataset Version

The first real dataset should be staged as a local working slice, for example:

```text
threads_sample_v1_2026-05/
```

Use `data-contracts/thread_item_schema_v1.json` as the authoritative field contract and `templates/annotation_sheet_template.csv` for manual annotation.
