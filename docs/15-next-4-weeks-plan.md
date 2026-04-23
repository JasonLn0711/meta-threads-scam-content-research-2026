# Next 4 Weeks Plan

## Current Status As Of 2026-04-23

Completed:

- Threads-first repo scaffold.
- Dataset schema and labeling schema v1.
- Annotation guideline, dataset schema docs, and first batch plan.
- Collection/redaction SOP, pilot runbook, annotator calibration, stakeholder kickoff, and go/no-go checklist.
- Report-v0 package with executive brief, review checklist, delivery plan, and feedback template.
- Synthetic sample and calibration CSVs.
- Validation, audit, conversion, annotation-agreement, calibration, and rule-baseline scripts.
- Synthetic validation, audit, conversion, and baseline dry run.
- Authorized pilot execution plan, work-order template, result-summary template, and authorization register.
- Annotator onboarding quickstart, annotation QA plan, QA checklist, onboarding checklist, and guideline revision log template.
- Staged 500-item expansion plan, with unlimited immediate collection rejected or paused.
- Pilot analysis and decision framework with decision memo and error review table.
- Source intake and sampling-frame package.
- Integrated real-pilot readiness review package.
- Stakeholder authorization packet and decision-record template.
- Approved pilot launch packet with `go_with_limits` records.
- First 10-15 item checkpoint protocol and review template.
- Local-only pilot workspace initializer and runbook.
- Repo-safe item-1 preflight verifier and runbook.
- Consolidated research day note: `notes/2026-04-23-research-day-notes.md`.

Not completed:

- controlled launch record with exact source, storage, access, retention, and redaction limits outside git
- initialized local-only pilot workspace under ignored `data/interim/`
- passing item-1 preflight after controlled launch acknowledgement
- real 50-item pilot collection
- first 10-15 item checkpoint result
- human annotation on real examples
- real baseline evaluation
- pilot decision memo from real results
- 500-item expansion
- LLM-assisted review test

The next work is controlled launch execution: complete the non-git launch record, initialize the local workspace, pass item-1 preflight, then collect only the first 10-15 items for checkpoint review. It is not more abstract planning, broad collection, or automation.

## Week 1: Scope, Taxonomy, Schema, And First Sample Design

Goals:

- Finalize taxonomy v1.
- Finalize dataset schema v1.
- Confirm data governance constraints.
- Draft annotation guideline v1.
- Define first sample inclusion and exclusion criteria.
- Prepare synthetic dry-run samples and collect no real evidence until approved.

Deliverables:

- Updated `docs/04-taxonomy.md`.
- Updated `docs/06-annotation-guideline-v1.md`.
- Validated `data-contracts/thread_item_schema_v1.json`.
- First dataset manifest draft.
- Stakeholder open questions list.
- Annotation pilot runbook and dry-run workflow.
- Collection/redaction SOP and authorization request template.
- Annotator training and calibration protocol.
- Synthetic dry-run result note.

## Week 2: Annotation And Text Baseline

Goals:

- Complete controlled launch details for exact source, storage, access, retention, and redaction limits.
- Initialize local-only pilot files under ignored `data/interim/`.
- Pass the item-1 preflight.
- Run 5-item calibration.
- Collect and review the first 10-15 real pilot items before completing the 50-item batch.
- Annotate the authorized 50-item pilot batch only if the checkpoint gate passes.
- Track disagreement and unclear fields.
- Build or specify simple keyword/rule baseline.
- Run text-only baseline on the authorized annotated batch.
- Record first false positives and false negatives.

Deliverables:

- Annotated batch v0.
- Text-only baseline experiment log.
- Guideline revision notes.
- Initial error analysis.
- Dataset audit and rule-variant comparison report.
- Annotation agreement report.

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
