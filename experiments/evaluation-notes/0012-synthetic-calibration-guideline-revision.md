# Synthetic Calibration Guideline Revision

## Objective

Record the first synthetic annotator calibration findings that were strong enough to justify guideline and answer-key revision before any broader real-item checkpoint.

This note is repo-safe. It refers only to synthetic item IDs and tracked synthetic fixtures. Local disagreement artifacts remain under ignored `data/interim/` and `data/processed/`.

## Context

The local-only synthetic calibration produced one primary-label disagreement and repeated disagreements on evidence sufficiency, confidence, subtype selection, and signal-tag selection.

The disagreement patterns were concentrated rather than random:

- `threads-synth-v1-0004` split `uncertain` versus `non_scam`
- `threads-synth-v1-0002` split on confidence, evidence sufficiency, and whether urgency signals from OCR were enough for the higher-severity interpretation
- `threads-synth-v1-0005` split on whether generic verification language justified a credential-request tag

Because these disagreements touched the finance boundary, screenshot/OCR sufficiency, and tag discipline, the result was strong enough to update the tracked guidance before any move to a broader real-item checkpoint.

## Inputs

- `data/samples/thread_item_sample_batch.csv`
- `data/samples/thread_item_calibration_answer_key.csv`
- local ignored `data/processed/calibration_agreement.md`
- local ignored `data/processed/calibration_disagreements.csv`

## Decisions

### 1. Readable finance discussion without a funnel stays `non_scam`

`threads-synth-v1-0004` was revised from:

- `scam_label`: `uncertain` -> `non_scam`
- `scam_type`: `investment_lure` -> `none`
- `signal_tags`: `vague_offer_strong_benefit` -> `none`
- `evidence_sufficiency`: `partial` -> `sufficient`
- `annotation_confidence`: `low` -> `medium`
- `missing_evidence`: `source_context_missing` -> `none`

Reason:

The item discusses savings and investing, but it does not show a conversion step, guaranteed benefit, private redirect, fake authority, payment ask, or a concrete lure. Topic alone is not a sufficient suspicious signal.

### 2. Decisive OCR can still support `sufficient` evidence

`threads-synth-v1-0002` was not relabeled.

Decision:

- keep the item as `scam`
- keep `evidence_sufficiency` as `sufficient`
- keep `annotation_confidence` anchored to the primary-label judgment rather than exact subtype overlap

Reason:

The captured OCR already contains the core redirect and urgency signals. Missing destination capture belongs in `missing_evidence`, not as an automatic downgrade of the label evidence.

### 3. Generic verification language does not automatically imply a credential request

`threads-synth-v1-0005` keeps the same primary label and subtype pattern, but the answer key removes the `credential_or_personal_data_request` signal tag.

Reason:

The item explicitly shows pseudo-official reward language, a fee request, and a private-channel step. Those are enough for the `scam` judgment. However, "verify your account" by itself does not prove that credentials or personal data were requested.

## Guidance Changes Applied

Tracked guidance was revised to make the above decisions durable:

- `docs/06-annotation-guideline-v1.md`
- `docs/24-annotator-training-and-calibration.md`
- `docs/31-annotation-quality-control-plan.md`

The main clarifications are:

- `uncertain` requires a visible suspicious signal, not just a finance topic
- missing destination or profile context does not automatically lower `evidence_sufficiency`
- confidence should track likely agreement on the primary label and core reason
- generic verification language does not automatically justify a credential-request tag

## Decision Implication

The synthetic calibration still does not authorize real-item expansion by itself.

What it does support:

- use the revised synthetic answer key for future blind calibration
- use the revised guidance for 1-2 real governed rehearsal items
- watch the same three boundary patterns during the first 10-15 real-item checkpoint

If the same patterns fail again on real governed items, revise the guideline again before completing the 50-item pilot.
