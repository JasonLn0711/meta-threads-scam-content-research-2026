# First Dataset Batch Plan

## Goal

Create the first Threads scam-content dataset version for pilot annotation and baseline experiments. This is a research bootstrap dataset, not a production collection pipeline and not a prevalence estimate.

The first batch should answer:

- Can annotators use the v1 guideline consistently?
- Are the schema fields practical to fill?
- Which signals appear in text, replies, OCR, links, and redirection evidence?
- Is there enough clean evidence to run a first text/OCR/link baseline?

## Recommended Batch Sizes

Start with a 50-item pilot. This is large enough to expose label confusion, missing fields, and source skew, but small enough to revise quickly.

After revising the guide and schema from the pilot, build a first usable batch of 100 to 200 items. If annotation capacity is limited, target 100 to 150.

## Pilot Composition

| Bucket | Target count | Purpose |
|---|---:|---|
| Likely scam or high-risk scam-like | 15 | Test positive signal coverage. |
| Likely non-scam comparator | 15 | Calibrate false positives and hard negatives. |
| Uncertain or ambiguous | 10 | Stress-test edge cases and mixed evidence. |
| Insufficient-evidence or low-context | 10 | Test evidence sufficiency and collection quality. |

Include a mix of:

- text-only posts
- text plus image posts
- replies/comments with redirection
- OCR-heavy images or screenshot-style posts
- visible links, contact handles, or off-platform redirect signals

## First Usable Batch Composition

| Bucket | Target count |
|---|---:|
| Likely scam | 40-60 |
| Non-scam comparators | 40-60 |
| Uncertain | 20-40 |
| Insufficient evidence | 10-20 |

Do not try to match natural prevalence in v1. The first dataset is a diagnostic sample for annotation, evidence quality, and baseline feasibility.

## Collection Strategy

Use mixed collection only:

- stakeholder-provided cases where sharing, retention, and redaction are authorized
- manual public examples where collection is permitted and documented
- synthetic or redacted examples only for dry-run templates and pipeline tests

Do not use crawlers, scrapers, browser automation, bulk export, or landing-page crawling unless approval is recorded in `governance/data-governance.md`.

Use `docs/23-collection-and-redaction-sop.md` and `templates/collection_log_template.csv` for the actual collection workflow.

## Evidence Preservation

Every item should record:

- `item_id`
- `collection_batch_id`
- `collection_timestamp`
- `collection_method`
- `source_type`
- `authorization_status`
- `screenshot_snapshot_status`
- `link_snapshot_status`
- `privacy_redaction_notes`
- `metadata_notes`

Store source URLs only when approved. Prefer redacted or normalized references when the full URL includes personal data, tracking identifiers, or sensitive investigative context.

Raw screenshots and stakeholder evidence stay out of git. Store them only in approved local or institutional locations.

## De-Duplication

Check duplicates before annotation using:

- exact post text
- near-duplicate post text
- OCR text reuse
- repeated external link or domain
- repeated visible contact handle
- repeated screenshot reference
- similar reply pattern

Do not automatically delete duplicate clusters. Reuse can be a campaign signal. Mark duplicates with `dedupe_key` and `near_duplicate_group_id`, then decide whether to keep one representative or preserve the cluster for analysis.

## Annotation Rounds

Round 1:

- One annotator labels all 50 pilot items.
- Annotator fills `scam_label`, `scam_type`, `risk_level`, `signal_tags`, `evidence_sufficiency`, `annotation_confidence`, `missing_evidence`, and notes.

Round 2:

- Second reviewer checks all `scam` high-risk items, all `uncertain` items, all low-confidence items, and a sample of `non_scam` items.
- Mark `review_status` as `needs_second_review` when there is disagreement or weak evidence.

Adjudication:

- Resolve disagreements with `templates/adjudication_template.md`.
- Fill `final_label` and `final_risk_level` only after adjudication.
- Use repeated disagreements to revise the guideline.

After the pilot:

- Count label distribution.
- Count uncertain and insufficient-evidence rates.
- Review source and content-form skew.
- Review top disagreement causes.
- Update `docs/06-annotation-guideline-v1.md` if needed before expanding to 100-200 items.

## Enough Data For First Baseline

The first baseline can begin when there are at least:

- 60 reviewable items total
- 25 `scam` and 25 `non_scam` items with high confidence or adjudication
- nonempty `post_text` or `ocr_text` for most baseline items
- at least 10 items where OCR or reply context changes interpretation

If the dataset does not meet these thresholds, keep collecting and annotating before modeling.

## Enough Data To Revise The Guideline

Revise the annotation guide after the first 50 items if:

- `uncertain` exceeds about 30 percent of labels
- `insufficient_evidence` exceeds about 20 percent
- annotators repeatedly disagree on finance, recruitment, giveaway, health, or celebrity cases
- annotators invent new signal tags more than a few times
- evidence notes show inconsistent interpretation of screenshot-only or reply-only cases

## Warning Signs The Taxonomy Is Too Broad

- Most scam items receive five or more subtypes.
- Annotators cannot distinguish `investment_lure`, `guaranteed_profit_claim`, and `suspicious_crypto_trading_lure`.
- `other_high_risk_persuasion` becomes common.
- Risk level is driven by annotator intuition rather than signal tags.
- Many cases need platform/account/landing-page context that phase 1 is not approved to collect.

If these appear, narrow the taxonomy for v1.1 rather than adding more fields.

## Human Owner Next Actions

- Confirm whether stakeholder-provided examples are authorized for annotation.
- Decide where local raw evidence will be stored outside git.
- Assign at least two pseudonymous annotator IDs.
- Complete `templates/data_authorization_request.md` for any real source.
- Run a 5-item dry annotation using the templates before collecting the full 50-item pilot.
