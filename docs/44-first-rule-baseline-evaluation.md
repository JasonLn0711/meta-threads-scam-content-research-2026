# First Rule Baseline Evaluation

## Purpose

This evaluation guide defines how to judge the first modular rule baseline.

The goal is not to prove production performance. The goal is to learn whether transparent low-cost signals can create a useful human-review queue and which evidence fields are worth keeping.

## Binary Metrics

For records with gold `scam` or `non_scam` labels, report:

- accuracy
- precision
- recall
- F1
- true positives
- true negatives
- false positives
- false negatives

Records labeled `uncertain`, `insufficient_evidence`, or blank are excluded from binary precision/recall and counted separately.

## Triage Metrics

For records with gold risk levels, report:

- exact high/medium/low agreement
- confusion matrix
- per-class support

High-risk precision matters first because false positives can waste reviewer time and can unfairly burden legitimate finance, recruitment, health, creator, or promotional content.

## Error Analysis

Review these slices first:

| Slice | Why |
|---|---|
| False positives | Shows where legitimate content is harmed by broad rules. |
| False negatives | Shows which scam-like patterns the baseline misses. |
| Medium-risk ambiguous cases | Shows where the baseline is appropriately cautious or too noisy. |
| OCR-driven changes | Tests whether image text adds value or noise. |
| Reply-driven changes | Tests whether comments/replies expose funneling. |
| Link/contact-driven changes | Tests whether redirection improves precision without overflagging creators. |
| Subtype-specific misses | Shows whether one scam family needs new rules or better data. |

## Run Commands

Synthetic smoke run:

```bash
python scripts/run_rule_baseline.py data/samples/rule_baseline_eval_sample.json \
  --variant all \
  --run-name synthetic-eval-smoke
```

Calibration workbench:

```bash
python scripts/run_rule_calibration.py data/samples/rule_baseline_eval_sample.json \
  --run-name synthetic-calibration-smoke
```

Compare variants after a labeled pilot:

```bash
python scripts/run_rule_baseline.py data/interim/threads_pilot_v1_annotations.csv \
  --variant text_only \
  --run-name pilot-text-only
python scripts/run_rule_baseline.py data/interim/threads_pilot_v1_annotations.csv \
  --variant text_reply \
  --run-name pilot-text-reply
python scripts/run_rule_baseline.py data/interim/threads_pilot_v1_annotations.csv \
  --variant text_ocr \
  --run-name pilot-text-ocr
python scripts/run_rule_baseline.py data/interim/threads_pilot_v1_annotations.csv \
  --variant all \
  --run-name pilot-all
```

Generated outputs are local-only by default under:

```text
experiments/baselines/outputs/
```

## Interpretation

Continue with the baseline if:

- high-risk cases have clear, evidence-backed reasons
- OCR, replies, or redirect fields improve triage
- false positives are understandable and tunable
- reviewers can use the output in a worksheet or packet

Revise before expanding if:

- weak single signals dominate medium-risk output
- legitimate finance/recruitment/health content is overflagged
- OCR or reply evidence is too noisy
- uncertainty labels are too broad for useful evaluation

Do not add heavier classifiers until rule errors have been reviewed.

See `docs/45-rule-baseline-calibration-workflow.md` for the threshold-profile and reviewer-worksheet workflow.

See `docs/47-review-packet-workflow.md` for the local-only item packet workflow used to inspect baseline reasons, matched evidence fields, false positives, false negatives, and ambiguous cases.
