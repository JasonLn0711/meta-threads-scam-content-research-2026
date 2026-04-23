# Synthetic Sample Batch Manifest

## Identity

| Field | Value |
|---|---|
| Dataset ID | `threads_synthetic_sample_batch_v1_2026-04-23` |
| Primary file | `data/samples/thread_item_sample_batch.csv` |
| Source template | `templates/thread_item_sample_batch.json` |
| Records | 5 |
| Schema | `thread_item_schema_v1` |
| Label schema | `labeling_schema_v1` |
| Evidence status | Synthetic/redacted only |

## Purpose

This batch exists to test:

- CSV annotation compatibility
- JSON/JSONL conversion
- schema validation
- dataset audit logic
- calibration sheet preparation
- rule-baseline variants

It is not a real Threads dataset and must not be used for empirical claims.

## Record Mix

| Item ID | Case type | Intended lesson |
|---|---|---|
| `threads-synth-v1-0001` | obvious scam-like text lure | Guaranteed profit, unrealistic benefit, urgency, and private-channel redirect. |
| `threads-synth-v1-0002` | text plus image with redirect signal | OCR and visible contact/link evidence are decisive. |
| `threads-synth-v1-0003` | non-scam normal post | Benign comparator with ordinary personal content. |
| `threads-synth-v1-0004` | uncertain finance-related post | Finance context without enough scam-like evidence. |
| `threads-synth-v1-0005` | screenshot-heavy suspicious post | OCR and replies surface official-looking reward, verification, fee, and private contact. |

## Safety Notes

- No real Threads post text is included.
- No real screenshots are included.
- Placeholder image paths are non-evidence references only.
- Visible contact handles are synthetic and redacted.
- The only URL-like value uses `example.invalid` and should not be crawled.
- Generated dry-run outputs belong in `data/processed/`, which is ignored by git.

## Dry-Run Result

See:

- `docs/28-synthetic-pilot-dry-run-results.md`
- `experiments/dataset-audit/0002-synthetic-sample-audit-dry-run.md`
- `experiments/baselines/0002-synthetic-rule-baseline-dry-run.md`

