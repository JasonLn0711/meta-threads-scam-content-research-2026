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
| Status | Initial research report. No production promise. No annotated-result claim. |

## Executive Summary

This v0 report recommends a Threads-only phase-1 research program for scam-like content triage. The immediate goal is not to build a production detector and not to decide legal guilt. The goal is to build a defensible research scaffold that can answer a narrower practical question:

> Can Threads scam-like content be structured, annotated, and triaged using text, image OCR, comments/replies, visible redirection signals, and external-link evidence under a budget-constrained research program?

The recommended first path is a small, evidence-centric study:

- Run a 5-item synthetic or redacted annotator calibration before real collection.
- Build a 50-item first pilot batch after authorization and calibration pass.
- Expand to a 100-200 item first usable dataset only after pilot review.
- Balance examples across `scam`, `non_scam`, `uncertain`, and `insufficient_evidence`.
- Capture post text, reply/comment text, attached image paths or placeholders, OCR text, visible links, redirection language, and explainable risk signals.
- Compare a text-only rule baseline against a richer rule baseline using OCR, comments/replies, and link/redirection signals.
- Evaluate usefulness for human review, not only model metrics.

This approach fits the practical NTD 1.8M research budget better than a full Meta-wide production system, video-heavy pipeline, deepfake detector, or automated enforcement architecture.

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

## Dataset v0 Plan

The first useful dataset should be small enough to inspect manually and broad enough to expose label ambiguity.

Recommended staged size:

- 5 synthetic or redacted calibration items.
- 50 manually reviewed pilot items after authorization.
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

- 50 annotated pilot items for workflow and error analysis.
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
- Narrowing decision for phase 2.

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

An NTD 1.8M research budget can support a focused dataset, annotation workflow, simple baselines, OCR augmentation, limited LLM-assisted review tests, and a serious evaluation memo.

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
2. 5-item calibration and 50-item pilot.
3. Text-only and text+OCR+comments/link-signal rule baselines.
4. Evidence completeness scoring.
5. Error analysis and reviewer workflow memo.

Medium-ROI but risky work:

1. LLM-assisted explanation testing on redacted samples.
2. Lightweight destination-link categorization if links are lawfully captured.
3. Inter-annotator agreement study if enough reviewer time exists.

Low-ROI or over-ambitious for phase 1:

1. Heavy video.
2. Deepfake detection.
3. Cross-platform platform integration.
4. Automated collection.
5. Custom large model training.

## Four-Week Execution Path After v0

| Week | Target output |
|---|---|
| Week 1 | Finalize taxonomy, schema, data-governance gate, annotation guide, and stakeholder authorization request. Run synthetic/redacted calibration prep. |
| Week 2 | Run annotator calibration, adjudicate disagreement, collect the authorized 50-item pilot if approved, and build text-only rule baseline. |
| Week 3 | Add OCR, reply/comment, and link/redirection signals. Compare rule baseline variants and optional redacted LLM explanation. |
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

## Approval Gates

Before real data work:

- Complete `docs/36-stakeholder-authorization-packet.md`.
- Complete `templates/stakeholder_authorization_decision_record.md`.
- Complete `templates/data_authorization_request.md`.
- Record data authority in `governance/pilot-authorization-register.md`.
- Pass `docs/26-pilot-go-no-go-checklist.md`.
- Complete `templates/real_pilot_readiness_review.md`.
- Decide what evidence can be stored in git, local storage, or private controlled folders.
- Finalize redaction procedure.
- Run annotator calibration and finalize adjudication process.
- Confirm whether external links can be visited, archived, or only recorded as visible strings.

Before any model-assisted workflow:

- Use only approved and redacted samples.
- Preserve reason codes and evidence references.
- Do not send sensitive investigative data to third-party systems without authorization.
- Keep human review in the loop.

## Non-Promise Statement

This v0 report is an initial research report. It does not promise production detection, automated enforcement, legal fraud determination, platform integration, deepfake detection, or broad Meta coverage. Its deliverable is a structured, defensible path for studying Threads scam-like content and deciding what a budget-fit phase-1 research MVP should include.

## Recommended v0 Deliverables By 2026-04-30

By the deadline, the repo should contain:

- This readable v0 report.
- Decision log for the April 30 report deadline.
- CIB/165 direction note.
- Link from `README.md`.
- Updated recommended path with the April 30 milestone.
- Stakeholder pilot kickoff memo and go/no-go checklist.
- Planning repo agenda blocks and Google Calendar events.

## Appendix: Active Repo Artifacts

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
| `docs/26-pilot-go-no-go-checklist.md` | Required gate before real collection and annotation. |
| `docs/35-real-pilot-readiness-review.md` | Integrated final readiness review before real collection. |
| `data-contracts/thread_item_schema_v1.json` | Machine-readable item schema. |
| `data-contracts/labeling_schema_v1.json` | Machine-readable label schema. |
| `templates/annotation_sheet_template.csv` | Spreadsheet starter for manual review. |
| `templates/data_authorization_request.md` | Source, field, retention, and redaction approval record. |
| `templates/stakeholder_authorization_decision_record.md` | Stakeholder decision record for pilot approval or limits. |
| `templates/real_pilot_readiness_review.md` | Fillable readiness decision record. |
| `templates/collection_log_template.csv` | Per-item collection readiness and evidence-status log. |
| `templates/redaction_checklist.md` | Redaction QA before annotation or sharing. |
| `scripts/validate_thread_dataset.py` | Local schema and consistency validation. |
| `scripts/audit_thread_dataset.py` | Dataset audit for balance, missing fields, duplicates, and skew. |
| `scripts/compare_annotation_passes.py` | Inter-annotator agreement and disagreement export. |
| `scripts/rule_baseline_v1.py` | First transparent rule baseline. |
| `scripts/compare_rule_variants.py` | Text/reply/OCR/all variant comparison. |
