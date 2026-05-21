# Rule Baseline Calibration Workflow

## Purpose

The next research step after implementing the modular rule baseline is calibration.

Calibration means comparing evidence variants and conservative threshold profiles to decide which rule settings produce the most useful reviewer queue. It does not mean optimizing against synthetic examples, proving real-world performance, or expanding data collection.

## Workbench Command

Run on synthetic samples for tool checks:

```bash
python scripts/run_rule_calibration.py data/samples/rule_baseline_eval_sample.json \
  --run-name synthetic-calibration-smoke
```

Run after the first authorized annotation slice exists:

```bash
python scripts/run_rule_calibration.py data/interim/threads_pilot_v1_annotations.csv \
  --run-name pilot-rule-calibration-v1
```

Generated outputs are local-only under:

```text
experiments/baselines/outputs/<run-name>/
```

## Outputs

| File | Use |
|---|---|
| `calibration_summary.json` | Metric matrix for each profile and evidence variant. |
| `changed_decisions.json` | Risk-level changes versus `baseline/text_only`. |
| `baseline_all_error_analysis.json` | False-positive, false-negative, and ambiguity review queues. |
| `matrix_predictions.json` | Full prediction matrix for audit/debugging. |
| `reviewer_worksheet.csv` | Human review worksheet for threshold and reason-code review. |
| `calibration_report.md` | Compact Markdown report for experiment logging. |

## Calibration Profiles

The profiles live in:

```text
configs/rule_calibration_variants.yaml
```

Current profiles:

- `baseline`: recommended conservative defaults
- `precision_first`: stricter high-risk threshold and category requirement
- `recall_probe`: lower medium-risk threshold for missed-case inspection
- `redirect_strict`: lower redirect/contact weights to test overflagging
- `ocr_sensitive`: increases OCR and screenshot evidence to test image-text lift

These are transparent probes, not separate models.

## Review Order

For the first real 30-50 annotated items:

1. Inspect `reviewer_worksheet.csv`.
2. Review false negatives first for the CIB-authorized pilot, especially missed reply/comment, link, private-channel, wallet/deposit, and add-friend signals.
3. Review false positives second and keep explainable false positives in the triage queue when that improves recall.
4. Inspect medium-risk uncertain cases.
5. Compare `text_only` to `text_reply`, `text_ocr`, and `all`.
6. Compare `baseline` to `precision_first`.
7. Tune `configs/baseline_rule_config.yaml` only after documenting the decision.

## Decision Rules

Prefer the baseline profile if:

- high-risk reasons are specific and reviewable
- false negatives are minimized for approved high-risk evidence families
- false positives are explainable, reviewable, and not used as final accusations
- OCR and reply signals improve recall without obvious noise

Prefer `precision_first` settings if:

- legitimate finance, recruitment, health, or creator content is overflagged
- medium/high output is dominated by weak link or urgency signals
- reviewers distrust the high-risk queue

Use `recall_probe` to investigate missed cases and to stress-test the CIB preference for lower false negatives. Do not treat recall-probe output as a final label without human review.

## Non-Claims

Synthetic calibration results are tooling checks. They do not estimate Threads prevalence, production accuracy, or law-enforcement value.
