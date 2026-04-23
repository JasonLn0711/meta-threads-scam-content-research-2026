# Review Packet Workflow

## Purpose

This workflow turns structured records and rule-baseline predictions into local-only Markdown packets for human review.

The goal is to make baseline review defensible and efficient:

- reviewers see the exact evidence fields used by the baseline
- reason codes and matched signals stay visible
- false positives, false negatives, and ambiguous cases are easy to sort
- reviewer notes can feed threshold tuning, guideline revision, and schema cleanup

This is a research triage workflow. It is not a moderation queue, enforcement system, legal finding, or production detector.

## When To Use It

Use review packets after one of these runs:

- synthetic smoke tests
- first 30-50 annotated pilot items
- threshold calibration comparisons
- post-guideline-revision spot checks

Do not use this workflow to collect Threads data, crawl links, inspect private profiles, or store raw screenshots in git.

## Command

Synthetic tooling check:

```bash
python scripts/build_review_packets.py data/samples/rule_baseline_eval_sample.json \
  --run-name synthetic-review-packets-smoke
```

Use an existing prediction run:

```bash
python scripts/build_review_packets.py data/interim/threads_pilot_v1_annotations.csv \
  --predictions-json experiments/baselines/outputs/pilot-all/predictions.json \
  --run-name pilot-v1-review-packets
```

Generate predictions on the fly:

```bash
python scripts/build_review_packets.py data/interim/threads_pilot_v1_annotations.csv \
  --variant all \
  --run-name pilot-v1-review-packets
```

Generated outputs are local-only by default:

```text
experiments/evaluation-notes/outputs/<run-name>/
```

## Outputs

| File | Use |
|---|---|
| `index.md` | Reviewer-friendly table sorted by review priority. |
| `review_packet_index.csv` | Spreadsheet-style queue for assigning or filtering review work. |
| `packet_manifest.json` | Machine-readable run manifest and priority counts. |
| `packets/<item_id>.md` | One packet per item with evidence, prediction, reasons, matched signals, and reviewer form. |

## Review Priority

Packets are sorted into these buckets:

| Priority | Meaning |
|---|---|
| `01_false_positive_review` | Gold label is non-scam but baseline predicted scam-like. |
| `02_false_negative_review` | Gold label is scam but baseline did not predict scam-like. |
| `03_ambiguity_review` | Gold label is uncertain or insufficient evidence. |
| `04_high_risk_reason_check` | Baseline predicted high risk and reasons should be inspected. |
| `05_medium_risk_threshold_check` | Baseline predicted medium risk and threshold behavior should be reviewed. |
| `06_spot_check` | Lower-priority sanity review. |

## Packet Contents

Each packet includes:

- safety boundary
- source and annotation fields
- binary and triage predictions
- subtype hint when available
- total score and reason codes
- short explanations
- post text, reply text, OCR text, links, handles, redirects, and screenshot style
- matched signal table
- score breakdown JSON
- reviewer decision form

The packet intentionally shows evidence fields plainly rather than hiding them behind aggregate metrics.

## Human Review Procedure

Review in this order:

1. False positives.
2. False negatives.
3. Ambiguous or insufficient-evidence items.
4. High-risk reason checks.
5. Medium-risk threshold checks.
6. Spot checks.

For each item, record:

- final label
- final risk
- whether the reviewer agrees with the baseline
- evidence that drove the decision
- missing evidence that would change the decision
- guideline, schema, or threshold feedback

## How Findings Feed The Project

Use review notes to decide:

- whether a reason code is too broad
- whether a threshold is too low or too high
- whether OCR, reply, or redirect fields are adding value
- whether annotation guidance needs examples for a confusing pattern
- whether data contracts need a new field or clearer field semantics

Do not tune thresholds from synthetic data alone. Use synthetic packets only to validate tooling.

## Commit Boundary

Safe to commit:

- this workflow doc
- aggregate experiment notes
- empty output guard files
- synthetic-only examples

Do not commit:

- real packet outputs with raw item text
- screenshots
- personal handles
- source URLs from live cases
- credentials, cookies, browser exports, or private investigation notes
