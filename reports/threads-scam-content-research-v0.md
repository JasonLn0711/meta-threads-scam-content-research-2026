# Threads Scam Content Research Report v0

## Report Identity

| Field | Value |
|---|---|
| Working title | Threads scam-content research v0 |
| Target delivery date | 2026-04-30 |
| Prepared from | 2026-04-23 CIB/165 stakeholder direction and existing research scaffold |
| Primary repo | `meta-threads-scam-content-research-2026` |
| Related planning repo | `planning-everything-track` |
| Audience | CIB/165-facing review, anti-fraud research planning, professors, investigators, and engineers |
| Status | Report-delivery version aligned to the approved 55-record checkpoint package plus 0076 hard-negative addendum. No production promise. No legal determination claim. |

## Executive Summary

This v0 report recommends a Threads-only phase-1 research program for scam-like content triage. The immediate goal is not to build a production detector and not to decide legal guilt. The goal is to maintain a defensible evidence system that can answer a narrower practical question:

> Can Threads scam-like content be structured, annotated, and triaged using text, image OCR, comments/replies, visible redirection signals, and external-link evidence under a budget-constrained research program?

The repo has now moved beyond concept-only planning. It has an approved checkpoint package and a post-approval hard-negative addendum:

- Checkpoint 0055 is the current approved package for CIB/165-facing review.
- Item 0076 is a narrow post-0055 hard-negative addendum: `non_scam` / `low`.
- The local 76-record aggregate is strict-valid, but it does not replace the approved 55-record checkpoint package.
- Browser-session search has been useful for calibration and candidate-quality testing, but it has not justified unbounded collection.
- Confirmed-pointer intake remains the highest-yield path when new scam/high-risk rule-family learning is needed.

The recommended next path is report hardening and decision support, not more collection by default. This approach fits the practical NTD 1.8M research budget better than a full Meta-wide production system, video-heavy pipeline, deepfake detector, or automated enforcement architecture.

## Current Checkpoint State

The current approved package is checkpoint 0055, documented in:

- `reports/checkpoint-0055-approved-package-index.md`
- `reports/checkpoint-0055-executive-addendum.md`
- `reports/threads-scam-content-checkpoint-0055-v0.1.md`
- `governance/pilot-launch/checkpoint_0055_stakeholder_decision_record.md`
- `experiments/evaluation-notes/0068-checkpoint-0055-synthesis.md`

The post-approval addendum is:

- `reports/checkpoint-0076-hard-negative-addendum.md`
- `experiments/evaluation-notes/0080-checkpoint-0076-hard-negative-inclusion-synthesis.md`

Approved checkpoint 0055 summary:

| Metric | Value |
|---|---:|
| Strict-valid records | 55 |
| `scam` / high-risk records | 17 |
| `non_scam` records | 23 |
| `uncertain` records | 9 |
| `insufficient_evidence` records | 6 |
| Binary-evaluable items | 40 |
| Baseline precision | 0.708 |
| Baseline recall | 1.000 |
| Baseline F1 | 0.829 |
| Baseline false positives | 7 |
| Baseline false negatives | 0 |

These are smoke-test baseline metrics on the current binary-evaluable slice, not production performance estimates.

Local 0076 aggregate snapshot:

| Metric | Value |
|---|---:|
| Strict-valid records | 76 |
| `scam` records | 17 |
| `non_scam` records | 24 |
| `uncertain` records | 29 |
| `insufficient_evidence` records | 6 |
| `high` risk | 17 |
| `medium` risk | 13 |
| `low` risk | 46 |
| Baseline precision | 0.708 |
| Baseline recall | 1.000 |
| Baseline false positives | 7 |
| Baseline false negatives | 0 |

"Strict-valid" means schema and validation checks passed. It does not mean the 76-record local aggregate replaces the approved 55-record checkpoint package. Only checkpoint 0055 is currently approved for CIB/165-facing checkpoint use; item 0076 is a narrow local hard-negative addendum.

Interpretation:

- The approved 55-record package is the canonical CIB/165-facing checkpoint.
- Item 0076 strengthens the hard-negative boundary: anti-scam warning or scam-method vocabulary is not enough to label an item `scam`.
- False-positive pressure is a reviewer-workload issue, not a harmless metric.
- Confirmed-pointer intake remains the highest-yield approved path for high-risk rule learning.
- Broad crawler expansion is not the next default step.
- The next decision should explicitly choose report-only delivery, targeted confirmed-pointer intake, or a calibration-only browser tranche.

## CIB/165 Stakeholder Context

The CIB/165 context is treated as a stakeholder signal, not as a dataset. The current understanding is that Threads is an urgent reporting surface for scam-like content and therefore deserves a focused research plan.

This report does not claim:

- That CIB/165 has provided a legally usable training dataset.
- That any specific Threads item is confirmed criminal fraud.
- That automated collection from Threads has been authorized.
- That a detector can replace human investigation or platform enforcement.

The correct first-principles framing is:

1. Reports create operational pressure, but reports are not labels.
2. Scam-like content often uses partial evidence, persuasion, redirection, and ambiguity.
3. Research must preserve evidence and uncertainty before it can support technical modeling.
4. A phase-1 system should help reviewers prioritize and understand cases, not make final accusations.

## Why Threads Is The Phase-1 Target

Threads is the right phase-1 target for four reasons.

| Reason | Implication |
|---|---|
| Stakeholder report pressure appears concentrated on Threads | Start where operational attention is highest. |
| Threads content is often text and comment heavy | Early evidence can be reviewed without expensive video systems. |
| Scam-like behavior may use replies, redirection, and screenshots | A post-only dataset would miss important context. |
| A Threads-first scope is narrow enough to manage | It prevents a small research budget from becoming a platform-wide promise. |

The earlier broader Meta scam-ad framing remains useful as umbrella strategy, but phase 1 should execute in this Threads-focused repo.

## Problem Definition

In this project, "Threads scam content" means Threads-related public or stakeholder-provided content that appears to contain scam-like, fraud-like, or high-risk persuasion patterns. The project does not require legal confirmation at annotation time.

The unit of review is a `thread_item`, which may include:

- Original post text.
- Relevant replies or comments.
- Attached image references.
- OCR text extracted from image or screenshot content.
- Visible links, handles, QR codes if transcribed, or redirection instructions.
- Observed risk signals and evidence notes.
- Human annotation label and uncertainty state.

The target decision is not "fraud or not fraud." The target decision is:

> Should this item be routed, deprioritized, or marked uncertain for human review based on preserved evidence?

## Phase-1 Scope

Phase 1 includes evidence surfaces that are inspectable, explainable, and realistic under the budget.

| Surface | Include now? | Reason |
|---|---|---|
| Text posts | Yes | Primary lure language is often visible and cheap to annotate. |
| Text plus image posts | Yes | Scam-like posts may place claims or testimonials in images. |
| Replies/comments | Yes | Redirection and persuasion often happen outside the original post. |
| OCR from images | Yes, bounded | Adds evidence from screenshots, posters, and embedded claims. |
| Visible redirection signals | Yes | Requests to move to LINE, Telegram, WhatsApp, private DM, or external pages are high-value signals. |
| External links | Yes, visible-only first | URLs and domains can be recorded without crawling destination pages. |
| Screenshot-heavy posts | Yes, if redacted and ethically handled | Evidence value can be high, but privacy risk must be controlled. |

## Deferred Scope

The following should not be phase-1 mainline work.

| Topic | Defer reason |
|---|---|
| Long video | High compute, high annotation cost, low fit for first dataset slice. |
| Heavy short-video pipeline | Useful later, but early research should not depend on video transcription and multimodal inference. |
| Deepfake detection | Important future risk, but too large and specialized for this first report. |
| Full Meta cross-platform integration | Would dilute the Threads question and inflate governance burden. |
| Automated production detection | Requires platform integration, monitoring, QA, appeals, and legal/policy controls beyond research scope. |
| Automated collection/scraping | Not authorized unless written approval, API access, and governance controls are recorded. |

## Historical Phase-1 Dataset Design

This section records the original governed pilot design. It is not the current post-0076 authorization state. The current decision is limited to `report_only_delivery`, `targeted_confirmed_pointer_tranche`, or `calibration_only_browser_tranche`.

The first useful dataset should be small enough to inspect manually and broad enough to expose label ambiguity.

Recommended staged size:

- 5 synthetic or redacted calibration items.
- 1-2 manual rehearsal records after controlled launch details are complete outside git.
- 1 aggregate rehearsal review before the first 10-15 item checkpoint.
- 10-15 real pilot items for the first checkpoint.
- 50 manually reviewed pilot items after the checkpoint supports continuation.
- 100-200 first usable items only after pilot review and any guideline/schema revisions.
- Each item should preserve enough context for annotation.
- No raw personal data or unnecessary screenshots should be committed to git.

Recommended 50-item pilot balance:

| Label bucket | Target count | Purpose |
|---|---:|---|
| likely `scam` or high-risk scam-like | 15 | Test positive signal coverage. |
| likely `non_scam` comparator | 15 | Calibrate false positives and hard negatives. |
| likely `uncertain` | 10 | Stress-test ambiguity handling. |
| likely `insufficient_evidence` | 10 | Test evidence status and collection quality. |

The first 10-15 item checkpoint should approximate this mix without forcing unapproved evidence:

| Checkpoint bucket | Suggested count | Purpose |
|---|---:|---|
| likely scam or high-risk scam-like | 3 to 5 | Test whether strong signals are captured safely. |
| likely non-scam comparator | 3 to 5 | Catch early false-positive pressure. |
| uncertain or ambiguous | 2 to 3 | Stress-test label boundaries. |
| insufficient-evidence or low-context | 1 to 3 | Check whether source quality or collection rules are blocking review. |

The checkpoint should include some variation across text-only, text plus image, reply/comment context, OCR-heavy or screenshot-style content, and visible link/handle/redirect signals when those forms are approved.

Recommended first usable batch balance:

| Label bucket | Target count | Purpose |
|---|---:|---|
| `scam` | 40 to 60 | Likely scam-like or high-risk lures. |
| `non_scam` | 40 to 60 | Legitimate marketing, ordinary discussion, benign finance, news, satire, or unrelated content. |
| `uncertain` | 20 to 40 | Ambiguous cases where signals exist but evidence is not enough. |
| `insufficient_evidence` | 10 to 20 | Items with missing context, unreadable images, broken links, or screenshot-only claims that cannot be assessed. |

Candidate source types:

- Manually collected public examples, only where lawful and within platform terms.
- Stakeholder-provided examples, only after authority and handling rules are documented.
- Synthetic or redacted calibration examples for annotator training.
- Negative controls from ordinary Threads content if collection and privacy handling are approved.

Do not begin automated collection until governance approval is recorded in `governance/data-governance.md`.

Some fields may exist only in the controlled local or interim evidence store. Tracked repo artifacts must use redacted, normalized, hashed, counted, or presence-only representations where raw text, URLs, handles, screenshots, contact IDs, or sensitive notes would otherwise appear.

In reviewer-facing tracked reports, `post_text`, `reply_texts`, and `ocr_text` are represented through summaries, labels, reason codes, or redacted excerpts only. `external_links` is represented through a domain category, presence flag, or redacted reference only. `visible_contact_handles` is represented through platform or contact-type signal only.

## Minimum Evidence Fields

Each reviewed item should capture:

- `item_id`
- `schema_version`
- `source_platform`
- `source_type`
- `collection_batch_id`
- `collection_timestamp`
- `collection_method`
- `authorization_status`
- `post_text`
- `reply_texts`
- `image_paths`
- `image_count`
- `has_image`
- `has_reply`
- `has_external_link`
- `ocr_text`
- `external_links`
- `visible_contact_handles`
- `visible_platform_redirects`
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
- `screenshot_snapshot_status`
- `link_snapshot_status`
- `privacy_redaction_notes`

The active machine-readable draft is `data-contracts/thread_item_schema_v1.json`.

## Annotation Plan

The annotation plan should use four primary labels.

| Label | Meaning |
|---|---|
| `scam` | Evidence is strong enough to mark the item as scam-like or high-risk for review. |
| `non_scam` | Evidence does not support scam-like risk under this project taxonomy. |
| `uncertain` | Some signals exist, but context, intent, or evidence strength is unresolved. |
| `insufficient_evidence` | The reviewer cannot assess because required evidence is missing, unreadable, inaccessible, or out of scope. |

Annotators should separately record:

- Scam subtype, if known.
- Signal tags.
- Explainable reasons.
- Evidence type.
- Uncertainty state.
- Missing evidence.
- Notes for adjudication.

Ambiguous finance posts should not be labeled `scam` only because they discuss money, trading, crypto, AI investment, or profit. They should require evidence such as guaranteed-profit language, impersonation, suspicious testimonial framing, high-pressure urgency, redirection to private channels, or unverifiable endorsement claims.

## Initial Scam-Type Taxonomy

The first taxonomy should include:

- Investment lure.
- Guaranteed profit claim.
- Fake endorsement.
- Redirect-to-private-channel.
- Impersonation or pseudo-official language.
- High-pressure urgency.
- Suspicious testimonial or fabricated success story.
- Recruitment or side-hustle lure.
- Suspicious crypto or trading lure.
- Giveaway or reward lure.
- Medical or health miracle claim.
- Other high-risk persuasion, if visible in Threads examples and not captured above.

Taxonomy changes should update `docs/04-taxonomy.md` and the annotation guide before they are used in a dataset release.

## Baseline Plan

The first baseline comparison should be simple and explainable.

### Baseline A: Text-Only Rule Baseline

Inputs:

- `post_text`
- optionally normalized visible text from the post field only

Method:

- Keyword and phrase rules.
- Pattern rules for guaranteed returns, urgency, impersonation language, and suspicious contact instructions.
- Reason-code output.

Expected value:

- Gives a transparent floor.
- Finds obvious lures.
- Exposes wording variation quickly.

Expected weakness:

- Misses image-only claims.
- Misses comment-only redirection.
- Can overflag legitimate marketing.

### Baseline B: Text + OCR + Comments + Link-Signal Rule Baseline

Inputs:

- `post_text`
- `reply_texts`
- `ocr_text`
- `external_links`
- visible redirection signals

Method:

- Same rule family as Baseline A.
- Additional rules for private-channel redirection, URL/domain patterns, OCR claim language, and comment-context escalation.
- Output includes evidence source: post, reply, OCR, or link field.

Expected value:

- Tests whether additional evidence surfaces improve recall and reviewer usefulness.
- Produces a stronger human-review packet.

Expected weakness:

- OCR noise may create false positives.
- Comments increase annotation burden.
- Link signals can overflag legitimate campaigns.

### Optional Baseline C: LLM-Assisted Explanation Review

This should be used only on approved, redacted samples.

Purpose:

- Generate reviewer-facing explanations.
- Compare explanation quality against rule reason codes.
- Test ambiguity handling.

Not allowed in v0:

- Autonomous enforcement.
- Unredacted sensitive data submission.
- Claims that the LLM determines truth.

## First Experiment

Recommended first experiment:

> Compare a text-only rule baseline against text + OCR, text + replies, and text + OCR + replies + link/redirection variants on the first validated pilot dataset slice.

Hypothesis:

> OCR, comments/replies, and visible link/redirection signals improve human-review triage usefulness more than post text alone, but they may increase false positives and reviewer burden.

Data needed:

- 10-15 checkpoint items to confirm governance, redaction, collection burden, annotation consistency, and evidence sufficiency before scale.
- 50 annotated pilot items for workflow and error analysis only after checkpoint continuation.
- At least 25 `scam` and 25 `non_scam` high-confidence or adjudicated items before reporting binary precision/recall as meaningful.
- At least 10 items where OCR or reply context changes interpretation before making a strong modality claim.
- Items with visible external link, handle, or private-channel redirection language before making a link-signal claim.

Outputs:

- Per-item risk tier.
- Reason codes.
- Evidence-source fields.
- Confusion matrix against human labels.
- Reviewer burden estimate.
- Error analysis.
- Decision on whether to continue, revise, narrow, or pause before any larger batch.

## Evaluation Framework

Do not evaluate only with model metrics. The project should measure both predictive and operational value.

| Metric | Why it matters |
|---|---|
| Precision | High-risk route should not overload reviewers with weak accusations. |
| Recall | Obvious scam-like lures should not be missed. |
| F1 | Gives a compact view when comparing baselines. |
| Reviewer burden | Measures how many items or fields must be reviewed per useful flag. |
| Triage usefulness | Human reviewers should understand why an item was routed. |
| Explainability quality | Reason codes should be grounded in evidence fields. |
| Evidence completeness | The system should expose missing context instead of guessing. |
| Robustness to wording variation | Scam-like content shifts phrasing. |
| Ambiguity handling | Uncertain and insufficient-evidence cases should be preserved. |
| Human-review workflow usefulness | The output should support review decisions, not just scores. |

## Budget-Fit Argument Under NTD 1.8M

An NTD 1.8M research budget can support a focused dataset, annotation workflow, simple baselines, OCR augmentation, and a serious evaluation memo.

It is not realistic for:

- Production-scale ingestion.
- Full Meta platform coverage.
- Comprehensive video analysis.
- Deepfake detection as a mainline deliverable.
- Large custom model training.
- End-to-end enforcement integration.
- A full dashboard, alerting, case-management, and audit system.

High-ROI work:

1. Taxonomy and annotation guideline.
2. Controlled launch details, local workspace, 1-2 item rehearsal, rehearsal review, 5-item calibration if needed, 10-15 item checkpoint, and conditional 50-item pilot.
3. Text-only and text+OCR+comments/link-signal rule baselines.
4. Evidence completeness scoring.
5. Error analysis and reviewer workflow memo.

Medium-ROI but risky work:

1. Lightweight destination-link categorization if links are lawfully captured and if separate approval permits it.
2. Inter-annotator disagreement study if enough reviewer time exists.
3. Later model-assisted explanation testing only after Phase 1 produces governed real evidence and a separate decision record authorizes it.

Low-ROI or over-ambitious for phase 1:

1. Heavy video.
2. Deepfake detection.
3. Cross-platform platform integration.
4. Automated collection.
5. Custom large model training.

## Historical Four-Week Plan, Superseded By Post-0076 Decision Gate

This plan is retained for context. It does not authorize new collection after checkpoint 0055 and item 0076.

| Week | Target output |
|---|---|
| Week 1 | Finalize taxonomy, schema, data-governance gate, annotation guide, and stakeholder authorization request. Run synthetic/redacted calibration prep. |
| Week 2 | Complete controlled launch details, initialize local workspace, pass item-1 preflight, rehearse 1-2 records, record the rehearsal review, run annotator calibration if needed, and collect only the first 10-15 items for checkpoint review. |
| Week 3 | If the checkpoint and conditional 50-item pilot permit it, add OCR, reply/comment, and link/redirection signals and compare rule baseline variants. |
| Week 4 | Evaluate, write error analysis, summarize evidence, and decide whether to continue, narrow, or defer additional modalities. |

## Required Stakeholder Questions

For CIB/165 and investigative stakeholders:

- What counts as "report-worthy" Threads content?
- Are we studying illegal scam, suspicious fraud-like content, high-risk lures, or user-report pressure?
- What evidence standard matters operationally?
- Can CIB/165 provide redacted examples, report categories, or case summaries?
- Which scam families are currently highest priority?

For legal and policy stakeholders:

- What collection method is permitted?
- Can public examples be stored as text, screenshots, hashes, or redacted evidence snapshots?
- Which personal data must be removed before annotation?
- Are external-link checks allowed, and under what rules?
- What can be shared with professors, students, or engineering collaborators?

For domain reviewers:

- Which signals are strong enough for review routing?
- Which signals are weak or misleading?
- How should ambiguous financial education, legitimate marketing, celebrity references, politics, satire, and medical claims be handled?
- How much reviewer burden is acceptable?

## Historical Approval Gates

These gates remain useful if a later decision reopens evidence work. They do not authorize another pilot, browser tranche, confirmed-pointer tranche, crawler expansion, embedding experiment, or model-training pass under the current post-0076 report-only path.

Before real data work:

- Complete `docs/36-stakeholder-authorization-packet.md`.
- Complete `templates/stakeholder_authorization_decision_record.md`.
- Complete `templates/data_authorization_request.md`.
- Record data authority in `governance/pilot-authorization-register.md`.
- Pass `docs/26-pilot-go-no-go-checklist.md`.
- Complete `templates/real_pilot_readiness_review.md`.
- Complete the controlled launch record outside git with exact source, storage, access, retention, redaction, screenshot, OCR, URL/link, handle/contact, role-ID, permitted-field, forbidden-field, uncertainty, and signoff details.
- Initialize local-only workspace files and pass item-1 preflight.
- Rehearse 1-2 manual records.
- Record the rehearsal outcome with `templates/controlled_rehearsal_review.md`.
- Run 5-item annotator calibration and finalize adjudication process.
- Run the first 10-15 item checkpoint before completing the 50-item pilot.
- Confirm whether external links can be stored only as visible strings or redacted/normalized references. Do not crawl or expand links without separate approval.

Model-assisted workflow is not part of the current launch. Before any later model-assisted workflow:

- Use only approved and redacted samples.
- Preserve reason codes and evidence references.
- Do not send sensitive investigative data to third-party systems without authorization.
- Keep human review in the loop.

## Non-Promise Statement

This v0 report is an initial research report. It does not promise production detection, automated enforcement, legal fraud determination, platform integration, deepfake detection, or broad Meta coverage. Its deliverable is a structured, defensible path for studying Threads scam-like content and deciding what a budget-fit phase-1 research MVP should include.

## Historical v0 Deliverables By 2026-04-30

This list records the original April 30 package target. The current deliverable is the selected post-0076 reviewer package and path-selection decision.

By the deadline, the repo should contain:

- This readable v0 report.
- Decision log for the April 30 report deadline.
- CIB/165 direction note.
- Link from `README.md`.
- Updated recommended path with the April 30 milestone.
- Stakeholder pilot kickoff memo and historical launch-gate checklist.
- Planning repo agenda blocks and Google Calendar events.

## Appendix: Historical And Active Repo Artifacts

| Artifact | Purpose |
|---|---|
| `docs/04-taxonomy.md` | Scam type, risk signal, evidence, and uncertainty vocabulary. |
| `docs/05-data-strategy.md` | Data-source, sampling, privacy, and versioning plan. |
| `docs/06-annotation-guideline-v1.md` | First label and annotation rules. |
| `docs/07-dataset-schema.md` | Human-readable dataset schema. |
| `docs/08-baseline-strategy.md` | Baseline families and tradeoffs. |
| `docs/09-phase-1-experiment-plan.md` | Experiment families and decision implications. |
| `docs/10-evaluation-framework.md` | Model and human-review evaluation criteria. |
| `docs/11-budget-fit-analysis.md` | NTD 1.8M realism and cut lines. |
| `docs/18-recommended-path-v1.md` | Phase-1 MVP recommendation. |
| `docs/22-annotation-pilot-runbook.md` | Dry-run, calibration, annotation, audit, and baseline workflow. |
| `docs/23-collection-and-redaction-sop.md` | Manual collection, redaction, OCR, link, and snapshot handling. |
| `docs/24-annotator-training-and-calibration.md` | Training and agreement workflow before the pilot. |
| `docs/25-stakeholder-pilot-kickoff.md` | Stakeholder-facing approval memo for real pilot data. |
| `docs/36-stakeholder-authorization-packet.md` | Approval packet for source, field, storage, access, retention, and redaction decisions. |
| `docs/26-pilot-go-no-go-checklist.md` | Historical required gate before real collection and annotation. |
| `docs/35-real-pilot-readiness-review.md` | Integrated final readiness review before real collection. |
| `docs/37-approved-pilot-launch-plan.md` | Repo-safe controlled launch entrypoint after approval. |
| `docs/38-first-pilot-checkpoint-protocol.md` | First 10-15 item checkpoint gate before completing 50. |
| `docs/39-local-pilot-workspace.md` | Local-only workspace initialization instructions. |
| `docs/40-pilot-preflight-verification.md` | Repo-safe preflight before item 1. |
| `data-contracts/thread_item_schema_v1.json` | Machine-readable item schema. |
| `data-contracts/labeling_schema_v1.json` | Machine-readable label schema. |
| `templates/annotation_sheet_template.csv` | Spreadsheet starter for manual review. |
| `templates/data_authorization_request.md` | Source, field, retention, and redaction approval record. |
| `templates/stakeholder_authorization_decision_record.md` | Stakeholder decision record for pilot approval or limits. |
| `templates/real_pilot_readiness_review.md` | Fillable readiness decision record. |
| `templates/controlled_launch_details_template.md` | Outside-git controlled detail structure for exact launch limits. |
| `templates/manual_collection_rehearsal_checklist.md` | 1-2 item rehearsal checklist before real volume. |
| `templates/controlled_rehearsal_review.md` | Aggregate-only bridge from the first 1-2 rehearsal items to the first 10-15 item checkpoint. |
| `templates/annotator_calibration_packet_template.md` | 5-item calibration packet template. |
| `templates/pilot_checkpoint_review.md` | First 10-15 item checkpoint worksheet. |
| `experiments/evaluation-notes/0014-controlled-rehearsal-review-protocol.md` | Repo-safe review protocol for the first 1-2 controlled real rehearsal items. |
| `templates/collection_log_template.csv` | Per-item collection readiness and evidence-status log. |
| `templates/redaction_checklist.md` | Redaction QA before annotation or sharing. |
| `scripts/validate_thread_dataset.py` | Local schema and consistency validation. |
| `scripts/audit_thread_dataset.py` | Dataset audit for balance, missing fields, duplicates, and skew. |
| `scripts/compare_annotation_passes.py` | Inter-annotator agreement and disagreement export. |
| `scripts/rule_baseline_v1.py` | First transparent rule baseline. |
| `scripts/compare_rule_variants.py` | Text/reply/OCR/all variant comparison. |
