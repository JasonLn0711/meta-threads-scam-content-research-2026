# Experiment 0001: Rule Baseline v1

## Hypothesis

A transparent rule baseline using `post_text`, `reply_texts`, `ocr_text`, `external_links`, `visible_contact_handles`, and `visible_platform_redirects` can create a useful first high-risk review queue before heavier models are justified.

## Dataset Slice

Use the first baseline-ready v1 slice:

- `scam_label` is `scam` or `non_scam`
- prefer `final_label` when `review_status` is `adjudicated`
- `annotation_confidence` is `high`, or `review_status` is `adjudicated`
- `post_text` or `ocr_text` is nonempty
- `evidence_sufficiency` is `sufficient` or `partial`
- `baseline_split` is not `excluded`

Keep `uncertain` and `insufficient_evidence` records in the audit, but exclude them from binary precision/recall.

## Method

Run four variants:

| Variant | Fields |
|---|---|
| `text_only` | `post_text` |
| `text_reply` | `post_text`, `reply_texts` |
| `text_ocr` | `post_text`, `ocr_text` |
| `all` | `post_text`, `reply_texts`, `ocr_text`, `external_links`, `visible_contact_handles`, `visible_platform_redirects` |

Use:

```bash
python scripts/validate_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
python scripts/audit_thread_dataset.py data/interim/threads_pilot_v1_annotations.csv
python scripts/rule_baseline_v1.py data/interim/threads_pilot_v1_annotations.csv --variant text_only --output data/processed/rule_v1_text_only.csv
python scripts/rule_baseline_v1.py data/interim/threads_pilot_v1_annotations.csv --variant text_reply --output data/processed/rule_v1_text_reply.csv
python scripts/rule_baseline_v1.py data/interim/threads_pilot_v1_annotations.csv --variant text_ocr --output data/processed/rule_v1_text_ocr.csv
python scripts/rule_baseline_v1.py data/interim/threads_pilot_v1_annotations.csv --variant all --output data/processed/rule_v1_all.csv
```

Do not crawl links. The link/redirection baseline uses only visible fields already recorded in the dataset.

## Metrics

Report:

- precision, recall, and F1 for `scam` versus `non_scam`
- high-risk queue yield
- false positives among legitimate finance, marketing, recruitment, health, and giveaway items
- false negatives where OCR or replies carried the decisive signal
- number of items excluded from binary metrics because they are `uncertain` or `insufficient_evidence`
- annotation and evidence-quality issues found by `audit_thread_dataset.py`

## Cost

Expected compute cost is near zero. Human cost is annotation and error analysis time.

## Failure Modes

- Keyword rules overflag legitimate finance or recruitment language.
- OCR text adds noisy false positives.
- Reply context is unrelated or too expensive to review.
- Link presence alone overflags legitimate creators.
- `uncertain` labels are too broad to interpret rule errors.

## Decision Rule

Continue with rule plus OCR/reply/link comparison if:

- the `all` variant improves recall or high-risk yield over `text_only`
- false positives remain explainable
- reviewers find the matched signal tags useful

Revise the annotation guide or schema first if:

- audit shows too many missing fields
- `uncertain` exceeds the pilot threshold
- disagreement clusters around the same edge cases

Move to a simple text classifier only after the rule baseline has been run on at least 100 usable records.
