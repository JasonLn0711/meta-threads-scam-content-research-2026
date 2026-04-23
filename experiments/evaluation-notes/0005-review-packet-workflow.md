# Evaluation Note 0005: Review Packet Workflow

## Hypothesis

Reviewer packets can make the rule baseline easier to tune by placing predictions, reason codes, matched signals, and evidence fields into one local-only Markdown artifact per item.

## Dataset Slice

Initial smoke test:

- `data/samples/rule_baseline_eval_sample.json`
- synthetic-only records
- baseline variant: `all`

Future pilot input:

- `data/interim/threads_pilot_v1_annotations.csv`
- optional `predictions.json` from `scripts/run_rule_baseline.py`
- local-only packet output directory

## Method

```bash
python scripts/build_review_packets.py data/samples/rule_baseline_eval_sample.json \
  --run-name synthetic-review-packets-smoke
```

With an existing prediction run:

```bash
python scripts/build_review_packets.py data/interim/threads_pilot_v1_annotations.csv \
  --predictions-json experiments/baselines/outputs/pilot-all/predictions.json \
  --run-name pilot-v1-review-packets
```

## Outputs

- `index.md`
- `review_packet_index.csv`
- `packet_manifest.json`
- `packets/*.md`

## Decision Use

The packets support:

- false-positive review
- false-negative review
- ambiguity review
- high-risk reason-code checks
- medium-risk threshold checks
- reviewer notes for guideline and config revision

## Review Questions

- Did the matched signal actually appear in the cited evidence field?
- Is the reason code understandable to a reviewer?
- Did a weak signal over-trigger a medium or high decision?
- Did a decisive private redirect, OCR lure, or reply funnel get missed?
- Should the next config pass raise or lower a threshold?
- Does the annotation guideline need a new example?

## Commit Boundary

Commit only this experiment note and aggregate, non-sensitive summaries.

Do not commit real packet outputs if they contain raw post text, replies, OCR text, source links, personal handles, screenshots, or private investigative details.
