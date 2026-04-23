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

The CSV samples are generated from the synthetic JSON batch and exist only to test spreadsheet and calibration workflows.

The first synthetic dry run is documented in:

- `docs/28-synthetic-pilot-dry-run-results.md`
- `experiments/dataset-audit/0002-synthetic-sample-audit-dry-run.md`
- `experiments/baselines/0002-synthetic-rule-baseline-dry-run.md`

Generated dry-run outputs belong under `data/processed/`, which is ignored by git.
