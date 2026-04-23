# Baseline Experiment 0002: Synthetic Rule Baseline Dry Run

## Hypothesis

The rule baseline should demonstrate the expected value of additional low-cost evidence fields on a synthetic calibration set:

- `text_only` should catch only visible post-text lures.
- `text_reply` should improve cases where replies contain private-channel or fee evidence.
- `text_ocr` should improve cases where screenshot/image text contains the decisive lure.
- `all` should combine post text, replies, OCR, links, handles, and redirects without using crawling or automation.

## Dataset Slice

| Field | Value |
|---|---|
| Dataset | `data/samples/thread_item_sample_batch.csv` |
| Records | 5 |
| Binary metric records | 4 |
| Excluded from binary metrics | 1 `uncertain` case |
| Evidence type | Synthetic/redacted only |

## Method

```bash
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant text_only \
  --output data/processed/synthetic-dry-run/rule_baseline_text_only_predictions.csv
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant text_reply \
  --output data/processed/synthetic-dry-run/rule_baseline_text_reply_predictions.csv
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant text_ocr \
  --output data/processed/synthetic-dry-run/rule_baseline_text_ocr_predictions.csv
python scripts/rule_baseline_v1.py data/samples/thread_item_sample_batch.csv \
  --variant all \
  --output data/processed/synthetic-dry-run/rule_baseline_all_predictions.csv
python scripts/compare_rule_variants.py \
  data/processed/synthetic-dry-run/thread_item_sample_batch.jsonl \
  --output data/processed/synthetic-dry-run/rule_variant_comparison.md
```

Generated prediction files are local-only under `data/processed/synthetic-dry-run/`.

## Result

| Variant | Binary items | TP | FP | FN | Precision | Recall | F1 | High-risk predictions |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `text_only` | 4 | 1 | 0 | 2 | 1.000 | 0.333 | 0.500 | 1 |
| `text_reply` | 4 | 2 | 0 | 1 | 1.000 | 0.667 | 0.800 | 2 |
| `text_ocr` | 4 | 3 | 0 | 0 | 1.000 | 1.000 | 1.000 | 3 |
| `all` | 4 | 3 | 0 | 0 | 1.000 | 1.000 | 1.000 | 3 |

This is a synthetic QA result only. The perfect `text_ocr` and `all` scores are not expected to transfer to real data.

## Changed Decisions Versus Text Only

| Variant | Changed cases |
|---|---|
| `text_reply` | `threads-synth-v1-0005`: low to high |
| `text_ocr` | `threads-synth-v1-0002`: medium to high; `threads-synth-v1-0005`: low to high |
| `all` | `threads-synth-v1-0002`: medium to high; `threads-synth-v1-0005`: low to high |

## Baseline Calibration Notes

The dry run led to a small update in `scripts/rule_baseline_v1.py`:

- guaranteed-profit plus unrealistic-benefit evidence now maps to `high`
- redirect plus proof/authority plus urgency now maps to `high`
- generic "before and after" wording was removed as a standalone testimonial/earnings signal

The third change matters because a benign garden comparator contained generic "before and after" text. A useful baseline should not turn that ordinary phrase into a scam-like earnings signal without money, proof, results, or redirection context.

## Interpretation

The synthetic results support the planned experiment design:

- reply context can materially change risk level
- OCR can materially change risk level for screenshot-style posts
- visible link/contact/redirect fields are useful as reasons, but must not imply link crawling
- `uncertain` should stay outside binary precision/recall

The main thing to test on real pilot data is whether these same signals increase recall without overflagging legitimate finance, marketing, creator, recruitment, giveaway, or health content.

## Cost

Compute cost was near zero. Human cost was inspection, one small rule calibration, and experiment logging.

## Failure Modes To Watch In The Real Pilot

- OCR may create false positives from unrelated screenshot text.
- Reply context may be noisy or unrelated to the original item.
- Legitimate creators may use links, handles, and urgency language.
- Finance discussion can resemble investment-lure wording without being scam-like.
- Synthetic examples may overrepresent clear-cut cases.

## Decision

Keep the rule baseline as the first baseline family for the authorized 50-item pilot.

Next run:

1. Validate and audit the authorized 50-item pilot.
2. Run the same four variants.
3. Use only high-confidence or adjudicated `scam`/`non_scam` records for binary metrics.
4. Report `uncertain` and `insufficient_evidence` separately.
5. Do error analysis before adding classifiers or LLM-assisted review.

