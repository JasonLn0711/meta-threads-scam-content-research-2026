# Annotator Training And Calibration

## Purpose

This document defines how to prepare annotators before the 50-item pilot. It gives the project a measurable way to decide whether the annotation guideline is ready, whether reviewers need more examples, and whether the taxonomy is too broad.

Calibration is required before the first real pilot batch. It should use synthetic or redacted examples only unless data authorization is complete.

Participants:

- at least two annotators or one annotator plus one reviewer
- one annotation lead or adjudicator
- one governance reviewer if calibration uses any real redacted evidence
- the research engineer only for file preparation, comparison, and local report generation

Annotators must read the required materials before they see the blind calibration file. Do not use calibration to teach the guideline from scratch.

## Training Sequence

1. Read `docs/06-annotation-guideline-v1.md`.
2. Read `docs/30-annotator-onboarding-quickstart.md`.
3. Complete `templates/annotator_onboarding_checklist.md`.
4. Review `docs/04-taxonomy.md` and `data-contracts/labeling_schema_v1.json`.
5. Walk through the five synthetic examples in `templates/thread_item_sample_batch.json`.
6. Discuss the expected labels and evidence notes.
7. Run one blind calibration pass on five synthetic/redacted items.
8. Compare annotation passes with `scripts/compare_annotation_passes.py`.
9. Adjudicate disagreements.
10. Record guideline revision candidates in `templates/guideline_revision_log_template.md`.
11. Use `docs/31-annotation-quality-control-plan.md` to decide whether the pilot can proceed.

## Calibration Set

The minimum calibration set is five items:

- one obvious scam text lure
- one text plus image/OCR redirection case
- one ordinary non-scam post
- one ambiguous finance-related post
- one screenshot-heavy suspicious post

Select items that can create useful disagreement without requiring unapproved context. At least two of the five should stress likely boundary problems:

- `scam` versus `uncertain`
- `uncertain` versus `insufficient_evidence`
- aggressive but legitimate marketing versus scam-like persuasion
- OCR-only or reply-only evidence
- visible link or contact-handle handling
- source context absent by design

Do not choose five obvious examples. A calibration set that produces no discussion may fail to reveal dangerous label drift.

Use `data/samples/thread_item_sample_batch.csv` as a safe answer-key sample. For a blind exercise, use `scripts/prepare_calibration_files.py` to blank annotation fields before giving the file to annotators.

Annotation fields to remove or blank for blind calibration:

- `scam_label`
- `scam_type`
- `risk_level`
- `signal_tags`
- `evidence_sufficiency`
- `annotation_confidence`
- `annotation_notes`
- `review_status`
- `adjudication_status`
- `disagreement_flag`
- `final_label`
- `final_risk_level`

The blind file is not expected to validate until annotators fill those fields.

## Calibration Packet

Use `templates/annotator_calibration_packet_template.md` to prepare the local calibration packet. The packet should include:

- calibration ID and date
- assigned annotator IDs
- item IDs only, not raw source identifiers
- permitted evidence fields
- forbidden outside context
- expected time box
- disagreement review schedule
- the exact guideline and schema versions used

The packet may live outside git if it contains item-level real evidence. Commit only non-sensitive themes and guideline updates.

## Preparing Files

For a local calibration run:

```bash
python scripts/prepare_calibration_files.py data/samples/thread_item_sample_batch.csv \
  --blind-output data/interim/calibration_blind.csv \
  --answer-key-output data/processed/calibration_answer_key.csv \
  --annotator-copy ann_01:data/interim/calibration_ann_01.csv \
  --annotator-copy ann_02:data/interim/calibration_ann_02.csv
```

For a committed synthetic example of what blind calibration looks like, see:

- `data/samples/thread_item_calibration_blind.csv`
- `data/samples/thread_item_calibration_answer_key.csv`

## Agreement Targets

Do not treat these as hard scientific thresholds on a tiny calibration set. They are practical readiness gates.

| Measure | Ready to proceed | Pause and revise |
|---|---:|---:|
| `scam_label` agreement | at least 0.80 | below 0.70 |
| `risk_level` agreement | at least 0.70 | below 0.60 |
| `evidence_sufficiency` agreement | at least 0.70 | below 0.60 |
| Mean `scam_type` Jaccard | at least 0.60 | below 0.50 |
| Mean `signal_tags` Jaccard | at least 0.50 | below 0.40 |

Kappa can be reported, but it is unstable for five examples. Use disagreement patterns and adjudication notes as the main signal.

Minimum qualitative expectations before real pilot annotation:

- both annotators can explain every `scam`, `uncertain`, `non_scam`, and `insufficient_evidence` choice from collected evidence only
- primary-label disagreements are isolated and adjudicable
- annotators do not use `uncertain` as a substitute for missing evidence
- annotators do not use `insufficient_evidence` for merely ambiguous but reviewable evidence
- risk-level disagreements do not change which items need second review
- signal-tag disagreement does not hide the main risk reason

Dangerous label drift includes:

- repeated `scam` versus `non_scam` disagreement on the same evidence pattern
- one annotator labeling aggressive marketing as `scam` without concrete risk signals
- one annotator requiring unapproved source/profile/landing-page context before labeling
- OCR/reply-only evidence being treated as decisive by one annotator and ignored by another
- `insufficient_evidence` used when evidence is present but uncomfortable or ambiguous
- notes making legal fraud claims rather than research labels

Acceptable disagreement includes:

- subtype or signal-tag differences that do not change the primary label or review route
- confidence differences that can be resolved through adjudication notes
- one-off boundary disagreements that do not repeat across the five items

## Comparison Command

After two annotators complete independent files:

```bash
python scripts/compare_annotation_passes.py \
  data/interim/calibration_ann_01.csv \
  data/interim/calibration_ann_02.csv \
  --name-a ann_01 \
  --name-b ann_02 \
  --output data/processed/calibration_agreement.md \
  --disagreements-csv data/processed/calibration_disagreements.csv
```

Review the Markdown report and use `templates/annotation_disagreement_log_template.csv` or the generated disagreement CSV for adjudication.

## What To Discuss In Calibration

For each disagreement, ask:

- Was the evidence missing or merely ambiguous?
- Did annotators use `uncertain` differently?
- Did one annotator overuse `scam` for aggressive marketing?
- Did screenshot-only or OCR-only evidence drive the disagreement?
- Were `scam_type` values too overlapping?
- Were too many `signal_tags` selected?
- Would an example in the guideline prevent this disagreement?

## Common Calibration Failure Modes

| Failure | Likely cause | Fix |
|---|---|---|
| High `scam` vs `uncertain` disagreement | Evidence threshold unclear | Add examples to label definitions. |
| Low `risk_level` agreement | Triage priority is too subjective | Tie high risk to concrete signal combinations. |
| Low subtype overlap | Scam subtypes overlap too much | Merge or clarify subtype boundaries. |
| Low signal-tag overlap | Too many tags or vague tag definitions | Add tag examples or simplify tags. |
| Many `insufficient_evidence` labels | Collection fields are incomplete | Fix collection SOP or evidence requirements. |

## Pilot Readiness Decision

Proceed to the first 10-15 real item checkpoint only when:

- primary-label disagreements can be adjudicated without changing the entire taxonomy
- annotators can explain why `uncertain` differs from `insufficient_evidence`
- annotators agree on how to handle finance, recruitment, giveaway, celebrity, and screenshot-heavy cases
- redaction and evidence-sufficiency rules are not blocking annotation

Proceed to the rest of the 50-item pilot only after the first 10-15 item checkpoint also supports continuation.

Revise `docs/06-annotation-guideline-v1.md` before continuing when:

- the same primary-label boundary fails more than once
- annotators cannot explain `uncertain` versus `insufficient_evidence`
- the guideline does not say how to handle an observed evidence pattern
- disagreement themes imply a field or label is being interpreted differently

If calibration fails, do not collect or annotate more real examples until the guideline or workflow is corrected and the affected calibration cases are reviewed again.

Use `templates/annotation_qa_checklist.md` for batch-level QA before annotation, during the first 10-15 pilot items, and before baseline handoff.
