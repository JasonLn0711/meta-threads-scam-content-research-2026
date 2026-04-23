# Next 4 Weeks Plan

## Week 1: Scope, Taxonomy, Schema, And First Sample Design

Goals:

- Finalize taxonomy v1.
- Finalize dataset schema v1.
- Confirm data governance constraints.
- Draft annotation guideline v1.
- Define first sample inclusion and exclusion criteria.
- Collect or prepare the first small sample set if legally safe.

Deliverables:

- Updated `docs/04-taxonomy.md`.
- Updated `docs/06-annotation-guideline-v1.md`.
- Validated `data-contracts/thread_item_schema_v1.json`.
- First dataset manifest draft.
- Stakeholder open questions list.

## Week 2: Annotation And Text Baseline

Goals:

- Annotate first batch of 50 to 75 items.
- Track disagreement and unclear fields.
- Build or specify simple keyword/rule baseline.
- Run text-only baseline on the annotated batch.
- Record first false positives and false negatives.

Deliverables:

- Annotated batch v0.
- Text-only baseline experiment log.
- Guideline revision notes.
- Initial error analysis.

## Week 3: OCR, Comments, And Link Signals

Goals:

- Add OCR text for image and screenshot items.
- Add selected replies/comments for thread-context items.
- Extract visible link and redirection signals.
- Compare text-only versus text plus OCR.
- Compare post-only versus post plus comments.
- Compare with-link-signals versus without-link-signals.

Deliverables:

- Modality ablation experiment logs.
- OCR error notes.
- Comment-context value assessment.
- Link-signal false-positive review.

## Week 4: Evaluation, Decision Memo, And Narrowing

Goals:

- Evaluate precision, recall, F1, reviewer burden, explainability, evidence completeness, and ambiguity handling.
- Run a small LLM-assisted explanation comparison only if governance allows the sample content.
- Summarize which signals are high-ROI.
- Decide phase-2 direction or cut scope further.

Deliverables:

- Phase-1 evaluation memo.
- Updated risk register.
- Recommended path v2.
- Decision log entry on next phase.

## 4-Week Success Standard

At the end of 4 weeks, the project should know:

- Whether text-only rules are useful enough as a baseline.
- Whether OCR materially improves detection of image-heavy lures.
- Whether comments/replies are essential for redirection detection.
- Whether visible link signals improve triage without too many false positives.
- Whether LLM assistance is worth testing further.
- Whether the project should continue, narrow, or stop specific workstreams.
