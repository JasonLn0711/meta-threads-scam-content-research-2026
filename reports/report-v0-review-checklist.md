# Report v0 Review Checklist

## Purpose

Use this checklist before sharing the selected post-0076 stakeholder-facing report package.

The goal is not to make the report longer. The goal is to make sure the package is defensible, clear about limits, and ready to support post-0076 path selection.

Current package status: `revise_before_delivery`. The package consistency, manifest, validation-provenance, and decision-record edits have been applied locally; final external approval remains pending.

## Review Status Legend

| Status | Meaning |
|---|---|
| `pass` | Ready as written. |
| `revise` | Needs an edit before delivery. |
| `defer` | Valid issue, but not required for report v0. |
| `blocker` | Must be resolved before stakeholder delivery. |

Artifact package status values:

| Status | Meaning |
|---|---|
| `included_in_zip` | File belongs in the selected post-0076 reviewer ZIP. |
| `exists_in_full_repo_not_in_zip` | File exists in the full repo but is historical or supporting context outside the selected ZIP. |
| `not_required_for_post_0076_review` | File is not needed for the current selected reviewer package. |

## 1. Scope And Non-Promise Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report states Threads-only phase-1 scope | `pass` | AUTO-REPORT-REVIEW-01 | Report identity, executive summary, and scope sections keep Threads as the phase-1 surface. |
| Report says this is research, not production detection | `pass` | AUTO-REPORT-REVIEW-01 | Non-promise language appears in report identity, executive brief, and decision memo. |
| Report avoids legal fraud determinations | `pass` | AUTO-REPORT-REVIEW-01 | Report uses scam-like / risk-triage framing and explicitly avoids legal determination claims. |
| Report avoids claims of platform-scale coverage | `pass` | AUTO-REPORT-REVIEW-01 | Meta-wide, production, and cross-platform scope remain deferred. |
| Report avoids claims based on real annotated results before they exist | `pass` | AUTO-REPORT-REVIEW-01 | Report now distinguishes approved checkpoint 0055, local 0076 aggregate, and non-prevalence claims. |
| Deferred scope is explicit: video, deepfake detection, automation, cross-platform integration | `pass` | AUTO-REPORT-REVIEW-01 | Deferred scope and non-authorization language remain explicit. |

## 2. Governance And Privacy Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report says no automated collection without authorization | `pass` | AUTO-REPORT-REVIEW-01 | Post-0076 decision memo blocks new collection without a new decision record and controls. |
| Report points to data authorization and historical launch-gate artifacts | `pass` | AUTO-REPORT-REVIEW-01 | Delivery plan and artifact appendix keep authorization and launch-gate docs as historical or future-use context. |
| Report points to the stakeholder authorization packet and decision record | `pass` | AUTO-REPORT-REVIEW-01 | Delivery package includes stakeholder authorization and decision-record artifacts. |
| Report points to the real-pilot readiness review before collection | `pass` | AUTO-REPORT-REVIEW-01 | Delivery package and appendix include readiness review artifacts. |
| Report points to controlled launch, workspace, and preflight artifacts | `pass` | AUTO-REPORT-REVIEW-01 | Controlled launch, local workspace, and preflight artifacts remain listed. |
| Raw evidence is described as outside git | `pass` | AUTO-REPORT-REVIEW-01 | Report package repeats the no-raw-evidence-in-git boundary. |
| Screenshots, URLs, contact handles, and OCR privacy risks are acknowledged | `pass` | AUTO-REPORT-REVIEW-01 | Privacy surfaces are named as controlled evidence fields and governance risks. |
| Retention, access, and redaction decisions are listed as stakeholder decisions | `pass` | AUTO-REPORT-REVIEW-01 | Delivery plan keeps these as stakeholder/governance decisions. |
| Report makes the filled controlled launch record an outside-git requirement | `pass` | AUTO-REPORT-REVIEW-01 | Decision memo and report keep controlled raw preservation outside git. |
| No real personal data, screenshots, source URLs, credentials, tokens, or investigative details are included | `pass` | AUTO-REPORT-REVIEW-01 | Repo-visible package is aggregate and rule-family level only. |

## 3. Terminology Consistency

| Check | Status | Owner | Notes |
|---|---|---|---|
| Primary labels are exactly `scam`, `non_scam`, `uncertain`, `insufficient_evidence` | `pass` | AUTO-REPORT-REVIEW-01 | Label set is preserved in report, executive brief, and checkpoint tables. |
| Risk levels are exactly `high`, `medium`, `low` | `pass` | AUTO-REPORT-REVIEW-01 | Risk-level language matches the checkpoint addendum. |
| Evidence sufficiency values match the labeling schema | `pass` | AUTO-REPORT-REVIEW-01 | Report preserves evidence sufficiency as a separate review concept. |
| Annotation confidence values match the labeling schema | `pass` | AUTO-REPORT-REVIEW-01 | Report retains confidence/adjudication as annotation fields rather than labels. |
| Field names match `data-contracts/thread_item_schema_v1.json` | `pass` | AUTO-REPORT-REVIEW-01 | Minimum evidence fields still use schema field names. |
| The report uses "scam-like" or "high-risk" when evidence is incomplete | `pass` | AUTO-REPORT-REVIEW-01 | Legal certainty is avoided; uncertainty remains first-class. |

## 4. Dataset And Annotation Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| `thread_item` is clearly defined as the unit of review | `pass` | AUTO-REPORT-REVIEW-01 | Problem definition defines the item unit and evidence surfaces. |
| Text, replies, OCR, links, handles, redirects, and screenshots are treated as evidence fields | `pass` | AUTO-REPORT-REVIEW-01 | Surfaces are included as inspectable evidence, not as automatic labels. |
| Controlled launch, workspace init, rehearsal, rehearsal review, 5-item calibration if needed, 10-15 checkpoint, 50-item pilot, and 100-200 item expansion are staged clearly | `pass` | AUTO-REPORT-REVIEW-01 | Legacy staged plan remains in report for historical pilot design; current next action is post-0076 decision. |
| Pilot composition is diagnostic and not presented as prevalence | `pass` | AUTO-REPORT-REVIEW-01 | Executive brief and report state diagnostic/non-prevalence framing. |
| Rehearsal review is described as the bridge from 1-2 records to the first 10-15 item checkpoint | `pass` | AUTO-REPORT-REVIEW-01 | Historical pilot-readiness bridge remains documented. |
| First 10-15 item checkpoint is described as the gate before completing 50 | `pass` | AUTO-REPORT-REVIEW-01 | Historical gate remains documented; current package has passed later checkpoints. |
| `uncertain` and `insufficient_evidence` boundaries are preserved | `pass` | AUTO-REPORT-REVIEW-01 | Binary metrics exclude these labels while preserving them for analysis. |
| Adjudication and second-review paths are described | `pass` | AUTO-REPORT-REVIEW-01 | Decision memo requires second review before future promotion. |

## 5. Baseline And Evaluation Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| Text-only baseline uses `post_text` | `pass` | AUTO-REPORT-REVIEW-01 | Baseline A uses post text. |
| Context baseline uses `reply_texts` | `pass` | AUTO-REPORT-REVIEW-01 | Baseline B includes reply/comment context. |
| OCR baseline uses `ocr_text` | `pass` | AUTO-REPORT-REVIEW-01 | OCR is included as bounded evidence. |
| Link/redirection baseline uses `external_links`, `visible_contact_handles`, and `visible_platform_redirects` | `pass` | AUTO-REPORT-REVIEW-01 | Link/redirection inputs are named explicitly. |
| Evaluation uses adjudicated or high-confidence labels where possible | `pass` | AUTO-REPORT-REVIEW-01 | Report preserves high-confidence/adjudicated slice framing. |
| `uncertain` and `insufficient_evidence` are not forced into binary metrics | `pass` | AUTO-REPORT-REVIEW-01 | Report excludes them from binary precision/recall interpretation. |
| Reviewer burden and explainability are evaluated, not only precision/recall | `pass` | AUTO-REPORT-REVIEW-01 | Current report highlights false-positive pressure as reviewer workload. |

## 6. Budget-Fit Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report explains why the plan fits an NTD 1.8M research budget | `pass` | AUTO-REPORT-REVIEW-01 | Budget-fit section keeps phase 1 focused on evidence, labels, and baselines. |
| Report identifies high-ROI work for phase 1 | `pass` | AUTO-REPORT-REVIEW-01 | Taxonomy, annotation, controlled evidence, and explainable baselines are named. |
| Report identifies low-ROI or out-of-scope work | `pass` | AUTO-REPORT-REVIEW-01 | Heavy video, deepfake, production deployment, and large model work remain deferred. |
| The four-week path is plausible for a small team | `pass` | AUTO-REPORT-REVIEW-01 | Four-week path remains bounded; current package now asks for a post-0076 decision before new work. |
| No hidden dashboard, production platform, or large-model-training commitment is implied | `pass` | AUTO-REPORT-REVIEW-01 | Non-promise and deferred-scope sections block these interpretations. |

## 7. Stakeholder Decision Readiness

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report asks for a concrete pilot or post-checkpoint decision | `pass` | AUTO-REPORT-REVIEW-01 | Executive brief and decision memo now ask for a bounded post-0076 choice. |
| Report asks for a concrete post-0076 path: `report_only_delivery`, `targeted_confirmed_pointer_tranche`, or `calibration_only_browser_tranche` | `pass` | AUTO-REPORT-REVIEW-01 | Options are listed in the executive brief, delivery plan, and post-0076 memo. |
| Source authorization questions are clear | `pass` | AUTO-REPORT-REVIEW-01 | New evidence paths require approved source and a new decision record. |
| Field-retention questions are clear | `pass` | AUTO-REPORT-REVIEW-01 | Future collection gate requires controlled preservation and redaction decisions. |
| Screenshot and link-policy questions are clear | `pass` | AUTO-REPORT-REVIEW-01 | Memo blocks raw screenshots/URLs/handles in git. |
| Access and retention questions are clear | `pass` | AUTO-REPORT-REVIEW-01 | Memo requires controlled-store preservation before promotion. |
| Controlled launch details outside git are clear | `pass` | AUTO-REPORT-REVIEW-01 | Raw evidence and controlled details remain outside git. |
| First checkpoint decisions and stop conditions are clear | `pass` | AUTO-REPORT-REVIEW-01 | Historical checkpoint path and new post-0076 stop conditions are both explicit. |
| Historical pilot-decision vocabulary is separated from current path selection | `pass` | AUTO-REPORT-REVIEW-01 | Current reviewer-facing decision vocabulary is limited to `report_only_delivery`, `targeted_confirmed_pointer_tranche`, and `calibration_only_browser_tranche`. |

## 8. Artifact Link Check

| Artifact | Status | Notes |
|---|---|---|
| `PACKAGE_MANIFEST.md` | `included_in_zip` | Selected package manifest and reading order. |
| `REVIEWER_README.md` | `included_in_zip` | Canonical reviewer entrypoint and response table. |
| `reports/threads-scam-content-research-v0.md` | `included_in_zip` | Exists and aligned to 0055 + 0076 state. |
| `reports/threads-scam-content-research-v0-executive-brief.md` | `included_in_zip` | Exists and asks for bounded post-0076 decision. |
| `reports/post-0076-report-v0-delivery-handoff-note.md` | `included_in_zip` | Exists as the reviewer-facing handoff message. |
| `reports/post-0076-next-decision-memo.md` | `included_in_zip` | Exists and is part of the selected package. |
| `reports/post-0076-validation-provenance.md` | `included_in_zip` | Repo-safe validation, audit, and baseline provenance. |
| `reports/report-v0-review-checklist.md` | `included_in_zip` | This checklist; status remains revise-before-delivery until required edits land. |
| `docs/18-recommended-path-v1.md` | `included_in_zip` | Current post-0076 path plus historical design reference. |
| `docs/27-report-v0-delivery-plan.md` | `included_in_zip` | Selected package delivery plan. |
| `data-contracts/thread_item_schema_v1.json` | `included_in_zip` | Repo-safe item schema contract. |
| `data-contracts/labeling_schema_v1.json` | `included_in_zip` | Repo-safe label schema contract. |
| `templates/report_review_feedback.md` | `included_in_zip` | Post-0076 reviewer feedback form. |
| `docs/25-stakeholder-pilot-kickoff.md` | `exists_in_full_repo_not_in_zip` | Historical pilot-launch artifact; not required for current selected package. |
| `docs/36-stakeholder-authorization-packet.md` | `exists_in_full_repo_not_in_zip` | Historical/future authorization artifact; not current decision form. |
| `docs/26-pilot-go-no-go-checklist.md` | `exists_in_full_repo_not_in_zip` | Historical launch gate; current package does not authorize launch. |
| `docs/35-real-pilot-readiness-review.md` | `exists_in_full_repo_not_in_zip` | Historical readiness artifact; not current decision form. |
| `docs/37-approved-pilot-launch-plan.md` | `exists_in_full_repo_not_in_zip` | Historical controlled-launch entrypoint; not current authorization. |
| `docs/38-first-pilot-checkpoint-protocol.md` | `exists_in_full_repo_not_in_zip` | Historical checkpoint protocol. |
| `docs/39-local-pilot-workspace.md` | `exists_in_full_repo_not_in_zip` | Historical workspace artifact. |
| `docs/40-pilot-preflight-verification.md` | `exists_in_full_repo_not_in_zip` | Historical preflight artifact. |
| `templates/data_authorization_request.md` | `exists_in_full_repo_not_in_zip` | Future-use authorization template, only after a new evidence decision. |
| `templates/stakeholder_authorization_decision_record.md` | `exists_in_full_repo_not_in_zip` | Future-use decision template, not current response table. |
| `templates/real_pilot_readiness_review.md` | `exists_in_full_repo_not_in_zip` | Future-use launch template. |
| `templates/controlled_launch_details_template.md` | `not_required_for_post_0076_review` | Filled sensitive version stays outside git if ever used. |
| `templates/manual_collection_rehearsal_checklist.md` | `not_required_for_post_0076_review` | Historical collection rehearsal artifact. |
| `templates/controlled_rehearsal_review.md` | `not_required_for_post_0076_review` | Historical collection rehearsal artifact. |
| `templates/annotator_calibration_packet_template.md` | `not_required_for_post_0076_review` | Historical calibration artifact. |
| `templates/pilot_checkpoint_review.md` | `not_required_for_post_0076_review` | Historical checkpoint worksheet. |
| `experiments/evaluation-notes/0014-controlled-rehearsal-review-protocol.md` | `not_required_for_post_0076_review` | Historical rehearsal protocol; not part of selected package. |

## Final Sign-Off

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Research owner | AUTO-REPORT-REVIEW-01 | `revise_before_delivery` | 2026-04-26 | Reviewer-required package consistency edits have been applied; final external approval remains pending. |
| Legal/privacy reviewer | external reviewer | `pending` |  | Needed before external delivery if policy wording changes. |
| Domain reviewer | external reviewer | `pending` |  | Needed if stakeholder wants more rule-family interpretation. |
| Technical reviewer | external reviewer | `pending` |  | Needed if baseline or schema interpretation changes. |
| Stakeholder owner | external stakeholder | `pending` |  | Needed to select post-0076 path. |

## Blocker Log

| Blocker | Owner | Required fix | Due date | Resolved? |
|---|---|---|---|---|
| External confirmation of revised selected package is still pending. | stakeholder owner | Review the rebuilt post-0076 package and confirm the selected path before delivery or any new evidence decision. | before delivery | no |
