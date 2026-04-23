# Dataset Audit 0002: Synthetic Sample Dry Run

## Hypothesis

The synthetic sample batch should validate cleanly, convert cleanly, and produce audit warnings about representativeness rather than schema problems.

## Dataset Slice

| Field | Value |
|---|---|
| Dataset | `data/samples/thread_item_sample_batch.csv` |
| Records | 5 |
| Source | Synthetic, redacted, non-evidence examples |
| Schema | `thread_item_schema_v1` |
| Use | Workflow QA only |

## Method

```bash
python scripts/validate_thread_dataset.py data/samples/thread_item_sample_batch.csv --strict
python scripts/validate_thread_dataset.py templates/thread_item_sample_batch.json --strict
python scripts/convert_thread_dataset.py data/samples/thread_item_sample_batch.csv \
  data/processed/synthetic-dry-run/thread_item_sample_batch.jsonl \
  --validate
python scripts/audit_thread_dataset.py data/samples/thread_item_sample_batch.csv
```

## Result

| Check | Result |
|---|---|
| CSV strict validation | 5 checked, 0 errors, 0 warnings |
| JSON strict validation | 5 checked, 0 errors, 0 warnings |
| CSV to JSONL conversion | 5 records written |
| Required fields missing | none |
| Possible duplicates | none found |

Label distribution:

| Label | Count |
|---|---:|
| `scam` | 3 |
| `non_scam` | 1 |
| `uncertain` | 1 |
| `insufficient_evidence` | 0 |

Evidence and confidence:

| Field | Count |
|---|---:|
| `sufficient` evidence | 4 |
| `partial` evidence | 1 |
| `high` confidence | 4 |
| `low` confidence | 1 |
| reply-context items | 3 |
| screenshot/OCR items | 2 |

Audit flags:

- `source_type` is 5/5 `researcher_synthetic`
- `collection_method` is 5/5 `synthetic`

## Interpretation

The audit behavior is correct:

- It passes a schema-valid synthetic batch.
- It reports the intended label and evidence distribution.
- It flags source and collection-method skew instead of mistaking the dry-run set for a real pilot.

This means the audit script is ready for the 50-item pilot after authorization, but the synthetic sample must not be used for empirical claims.

## Cost

Near-zero compute cost. Human cost was inspection and result write-up.

## Failure Modes Observed

No schema or conversion failures were observed.

The main limitation is expected: a five-item synthetic set cannot test real source skew, annotator disagreement, real screenshot quality, link redaction burden, or live ambiguity.

## Decision

Use this workflow for the first real pilot audit after the data authorization gate passes.

Do not relax the source-skew warning. It should remain noisy for synthetic-only and single-source batches because that warning is useful during the real pilot.

