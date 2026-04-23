# Dataset Audit

Use this folder for first-batch dataset audits before baseline experiments. The audit should be lightweight and evidence-focused.

## Current Logs

| Audit | Purpose |
|---|---|
| `0001-pilot-audit-protocol.md` | Protocol for auditing the authorized 50-item pilot before baseline work. |
| `0002-synthetic-sample-audit-dry-run.md` | Synthetic-only dry run confirming validation, conversion, and audit behavior. |
| `0003-first-checkpoint-audit-protocol.md` | Safety and usefulness audit for the first 10-15 real pilot items. |

## Required Checks

### Class Balance

Count `scam_label` values:

- `scam`
- `non_scam`
- `uncertain`
- `insufficient_evidence`

For the 50-item pilot, investigate if `uncertain` is above about 30 percent or `insufficient_evidence` is above about 20 percent.

### Label Disagreement

Track disagreements by:

- primary label
- risk level
- scam subtype
- signal tags
- evidence sufficiency
- confidence

Use `templates/adjudication_template.md` for cases that need resolution.

### Missing Fields

Check required schema fields, especially:

- `collection_batch_id`
- `collection_timestamp`
- `authorization_status`
- `post_text`
- `reply_texts`
- `ocr_text`
- `scam_label`
- `signal_tags`
- `evidence_sufficiency`
- `screenshot_snapshot_status`
- `link_snapshot_status`

Empty text fields are allowed when evidence is absent, but the absence should be intentional and reflected in `missing_evidence`.

### Too Many Uncertain Labels

Review whether uncertain cases are caused by:

- missing source context
- missing OCR
- missing link snapshot
- unclear finance/recruitment rules
- weak screenshot-only evidence
- annotator hesitation about aggressive but legal marketing

If the same cause repeats, revise the annotation guideline before expanding the dataset.

### Duplicated Items

Check for:

- exact repeated post text
- near-duplicate post text
- repeated OCR claims
- repeated external links/domains
- repeated contact handles
- repeated screenshot assets

Mark clusters with `dedupe_key` and `near_duplicate_group_id`. Do not delete repeated items automatically; reuse may be an investigative signal.

### Source Skew

Count `source_type` and `collection_method`. A useful first batch should not be dominated entirely by one collection path unless that is the explicit stakeholder-provided dataset condition.

### Content-Form Skew

Count:

- text-only items
- text plus image items
- reply/context items
- OCR-heavy items
- screenshot-style items
- link/redirection items

If one content form dominates the pilot, baseline findings may not transfer to the rest of phase 1.

### Signal-Tag Drift

Look for:

- frequent use of `other_high_risk_persuasion`
- frequent `none` with non-scam labels only
- five or more signal tags on most scam cases
- repeated annotator notes inventing new tags

Signal-tag drift means the taxonomy needs a v1.1 cleanup.

## Audit Output

Each audit note should include:

- dataset ID and date
- item count
- label distribution
- source distribution
- content-form distribution
- missing-field summary
- top disagreement causes
- recommended schema or guideline changes
- decision: proceed to baseline, annotate more, or revise first
