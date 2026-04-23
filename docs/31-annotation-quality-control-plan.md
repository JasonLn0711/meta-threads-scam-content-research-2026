# Annotation Quality Control Plan

## Purpose

This plan defines how the first annotation pilot will monitor label quality, field completeness, disagreement, and guideline drift.

The goal is not to make annotation slow or bureaucratic. The goal is to catch the first errors early enough that the 50-item pilot remains useful.

## Scope

Applies to:

- 5-item synthetic or redacted calibration
- 50-item authorized pilot
- first 100-200 item usable dataset after pilot review

Does not authorize:

- real Threads collection
- automated collection
- raw evidence in git
- legal fraud determinations
- production scoring

## QA Roles

| Role | QA responsibility |
|---|---|
| Project owner | Decides whether calibration and pilot quality are sufficient to proceed. |
| Lead annotator or reviewer | Checks label consistency and edge-case handling. |
| Adjudicator | Resolves disagreements and identifies guideline changes. |
| Research engineer | Runs validation, audit, agreement, and baseline scripts. |
| Governance reviewer | Checks redaction, approved fields, and raw-storage boundaries. |

## QA Stages

| Stage | Timing | Main question |
|---|---|---|
| Pre-annotation QA | Before annotators start | Are rows complete enough and safe enough to label? |
| Calibration QA | Before real pilot | Can annotators apply labels consistently on safe examples? |
| In-pass QA | During the first 10-15 real pilot items | Are field errors or label drift appearing early? |
| Second-review QA | After first-pass labels | Are high-risk, uncertain, low-confidence, and partial-evidence cases reviewed? |
| Adjudication QA | After disagreements | Are final labels evidence-based and guideline-consistent? |
| Post-pilot QA | After all 50 items | Is the dataset ready for baseline comparison or revision first? |

## Pre-Annotation QA

Before annotation begins, check:

- data authorization is complete for real evidence
- raw evidence is outside git
- collection batch ID is present
- required schema fields are present
- redaction notes exist where redaction occurred
- screenshot and link snapshot statuses are filled
- `has_image` agrees with `image_count`
- `has_external_link` agrees with `external_links`
- OCR text has been privacy-reviewed if present
- rows needing missing evidence are marked in `missing_evidence`

Use `templates/annotation_qa_checklist.md` for the batch-level check.

## Calibration QA

Minimum ready-to-proceed thresholds:

| Measure | Ready | Pause and revise |
|---|---:|---:|
| `scam_label` agreement | at least 0.80 | below 0.70 |
| `risk_level` agreement | at least 0.70 | below 0.60 |
| `evidence_sufficiency` agreement | at least 0.70 | below 0.60 |
| Mean `scam_type` Jaccard | at least 0.60 | below 0.50 |
| Mean `signal_tags` Jaccard | at least 0.50 | below 0.40 |

For five examples, thresholds are only practical warnings. Use disagreement themes as the main evidence.

Proceed only if annotators can explain:

- `scam` versus `uncertain`
- `uncertain` versus `insufficient_evidence`
- aggressive marketing versus scam-like persuasion
- legitimate finance discussion versus investment lure
- OCR-only and reply-only evidence handling

## In-Pass QA

After the first 10-15 pilot rows, pause for a quick check.

Look for:

- blank required annotation fields
- `signal_tags` left empty instead of `none`
- `uncertain` used as a catch-all
- `insufficient_evidence` used for merely ambiguous cases
- high-risk `scam` items not routed to second review
- notes that make legal claims
- notes that refer to outside knowledge not in the collected evidence
- repeated new signal tags not in the schema

If repeated problems appear, pause the pilot and revise instructions before completing all 50 items.

## Second-Review Routing

Second review is required for:

- all `scam` plus `high` risk items
- all `uncertain` labels
- all low-confidence labels
- all `partial`, `insufficient`, or `not_reviewable` evidence cases
- all cases where decisive evidence is in OCR only
- all cases where decisive evidence is in replies/comments only
- at least 20 percent of `non_scam` comparator items

Second review should focus on evidence quality and label boundary, not on rewriting every note.

## Adjudication QA

Use adjudication when annotators disagree on:

- primary label
- risk level
- evidence sufficiency
- key scam subtype
- key signal tags
- whether an item is reviewable

Adjudication output must include:

- final label
- final risk level
- evidence reviewed
- reason for decision
- whether guideline change is needed

Use `templates/adjudication_template.md`.

## Post-Pilot QA Thresholds

Investigate before expansion if:

| Finding | Warning threshold | Likely action |
|---|---:|---|
| `uncertain` labels | above 30 percent | Clarify label boundaries or source criteria. |
| `insufficient_evidence` labels | above 20 percent | Improve collection and evidence requirements. |
| primary-label disagreement | repeated same boundary | Add examples or revise definitions. |
| `other_high_risk_persuasion` | common | Split or clarify taxonomy. |
| five or more signal tags on most scam items | common | Simplify signal-tag guidance. |
| missing OCR on screenshot-heavy items | repeated | Clarify OCR capture or exclusion rules. |
| link/contact fields too specific | any privacy concern | Tighten redaction and storage rules. |

## Guideline Revision Rules

Do not revise the guideline after every single disagreement. Revise when:

- the same edge case appears at least twice
- two trained annotators use different labels for the same evidence pattern
- annotators invent the same new signal tag repeatedly
- a field is consistently misunderstood
- the current wording creates privacy or overclaiming risk

Use `templates/guideline_revision_log_template.md` to record proposed changes.

## Baseline Readiness QA

Before running baseline metrics, confirm:

- validation passes with zero errors
- `scam_label` is `scam` or `non_scam` for binary metric items
- `uncertain` and `insufficient_evidence` are excluded from binary precision/recall
- `annotation_confidence` is `high` or item is adjudicated for binary metrics
- `post_text` or `ocr_text` is nonempty
- `evidence_sufficiency` is `sufficient` or `partial`
- source and content-form skew are reported

Run baseline comparison only after audit findings are understood.

## QA Deliverables

At pilot exit, produce:

- completed annotation QA checklist
- calibration agreement summary
- disagreement/adjudication summary
- guideline revision log
- dataset audit summary
- rule baseline variant summary
- recommendation: expand, revise guideline, revise schema, narrow source, or pause

