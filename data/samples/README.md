# Samples

This folder is for safe synthetic or fully redacted examples that demonstrate the dataset format.

Do not place real Threads screenshots, personal identifiers, live URLs, or stakeholder evidence here.

Current sample sources:

- `templates/thread_item_sample.json`
- `templates/thread_item_sample_batch.json`
- `data/samples/thread_item_sample_batch.csv`
- `data/samples/thread_item_sample_batch_manifest.md`
- `data/samples/thread_item_calibration_blind.csv`
- `data/samples/thread_item_calibration_answer_key.csv`
- `data/samples/rule_baseline_dev_sample.json`
- `data/samples/rule_baseline_eval_sample.json`
- `data/samples/manual_collection_assistant_input_synthetic.json`

The CSV samples are generated from the synthetic JSON batch and exist only to test spreadsheet and calibration workflows.

The rule-baseline JSON samples are synthetic starter examples for testing the modular rule detector. They include investment lure, OCR redirect, benign, ambiguous finance, screenshot-heavy testimonial/reward, and reply-funnel cases. They are not real Threads evidence and should not be used as performance evidence.

The manual collection assistant input is a synthetic local-entry payload for testing record-building and governance checks. It is not a collected Threads item.

The first synthetic dry run is documented in:

- `docs/28-synthetic-pilot-dry-run-results.md`
- `experiments/dataset-audit/0002-synthetic-sample-audit-dry-run.md`
- `experiments/baselines/0002-synthetic-rule-baseline-dry-run.md`

Generated dry-run outputs belong under `data/processed/`, which is ignored by git.
