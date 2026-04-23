# Rule Baseline Implementation Plan

## Purpose

This document defines the first modular rule-based baseline for Threads scam-content research.

The baseline is a triage-oriented research tool. It is not a legal adjudicator, not a production moderation system, not a platform enforcement workflow, and not evidence that an actor committed fraud.

## Supported Tasks

| Task | Output | Purpose |
|---|---|---|
| Binary prediction | `scam_like`, `not_scam_like` | Provides a simple baseline comparison layer. |
| Risk triage | `high`, `medium`, `low` | Prioritizes human review without overclaiming certainty. |
| Explainable output | reason codes, explanations, score breakdown | Lets reviewers inspect why a case was flagged. |
| Subtype hint | optional subtype string or null | Suggests a likely review category only when evidence is sufficient. |

## Inputs Used

The first baseline reads local structured records that follow `data-contracts/thread_item_schema_v1.json`.

Used fields:

- `post_text`
- `reply_texts`
- `ocr_text`
- `external_links`
- `visible_contact_handles`
- `visible_platform_redirects`
- `screenshot_style`
- labels such as `scam_label`, `risk_level`, `final_label`, and `final_risk_level` when evaluation is possible

The baseline does not fetch posts, crawl links, inspect profiles, or collect Threads data.

## Phase-1 Exclusions

Out of scope:

- automated Threads or Meta data collection
- link crawling or landing-page capture
- production deployment
- deepfake detection
- heavy video analysis
- account graph or actor attribution
- legal or enforcement decisions

## Ambiguity Handling

The baseline is intentionally conservative:

- A single weak signal should not create `high` risk.
- `high` risk requires both score and multi-category evidence.
- `medium` risk means review-worthy, not proven scam-like.
- `uncertain` and `insufficient_evidence` gold labels are reported separately from binary precision/recall.
- Missing context should be preserved in reviewer notes and error analysis rather than hidden inside a score.

## Implementation Shape

The package is split by responsibility:

```text
src/baselines/
  taxonomy.py          stable signal and reason-code definitions
  signal_extractor.py  field-specific signal extraction
  risk_scoring.py      config-driven weighted scoring
  explainability.py    reviewer-facing reasons
  io_utils.py          local CSV/JSON/JSONL helpers
  rule_based.py        public prediction API

src/evaluation/
  metrics.py           binary metrics
  triage_metrics.py    high/medium/low triage metrics
  error_analysis.py    review queues for mistakes
```

The current single-script baseline remains available as `scripts/rule_baseline_v1.py`, but it is now a compatibility wrapper around the modular package.

## Run Commands

Run the modular baseline:

```bash
python scripts/run_rule_baseline.py data/samples/rule_baseline_dev_sample.json \
  --variant all \
  --run-name synthetic-dev-smoke
```

Run the legacy CSV-compatible wrapper:

```bash
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv --variant all
```

Generated outputs belong under `experiments/baselines/outputs/`, which is ignored by git.

## First Human Tuning Loop

After 30-50 real annotated items:

1. Review false positives before raising recall.
2. Check whether single weak signals are over-triggering `medium`.
3. Check whether OCR and reply-only signals are useful or noisy.
4. Tune `configs/baseline_rule_config.yaml`, not Python code, when changing weights or thresholds.
5. Record the tuning decision in an experiment log.
