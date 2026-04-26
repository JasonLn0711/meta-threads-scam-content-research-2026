# Report v0 Review Checklist

## Purpose

Use this checklist before sharing `reports/threads-scam-content-research-v0.md` as the April 30 stakeholder-facing report package.

The goal is not to make the report longer. The goal is to make sure the report is defensible, clear about limits, and ready to support a pilot decision.

## Review Status Legend

| Status | Meaning |
|---|---|
| `pass` | Ready as written. |
| `revise` | Needs an edit before delivery. |
| `defer` | Valid issue, but not required for report v0. |
| `blocker` | Must be resolved before stakeholder delivery. |

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
| Report points to data authorization and go/no-go artifacts | `pass` | AUTO-REPORT-REVIEW-01 | Delivery plan and artifact appendix include authorization and go/no-go docs. |
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
| Report explains what happens after `go`, `go_with_limits`, or `no_go` | `defer` | AUTO-REPORT-REVIEW-01 | Legacy decision outcomes remain in delivery plan; current next decision uses post-0076 options instead. |

## 8. Artifact Link Check

| Artifact | Status | Notes |
|---|---|---|
| `reports/threads-scam-content-research-v0.md` | `pass` | Exists and aligned to 0055 + 0076 state. |
| `reports/threads-scam-content-research-v0-executive-brief.md` | `pass` | Exists and asks for bounded post-0076 decision. |
| `reports/post-0076-report-v0-delivery-handoff-note.md` | `pass` | Exists as the reviewer-facing handoff message. |
| `reports/post-0076-next-decision-memo.md` | `pass` | Exists and is now part of the package. |
| `docs/25-stakeholder-pilot-kickoff.md` | `pass` | Exists as historical/launch artifact. |
| `docs/36-stakeholder-authorization-packet.md` | `pass` | Exists as authorization artifact. |
| `docs/26-pilot-go-no-go-checklist.md` | `pass` | Exists as launch gate artifact. |
| `docs/35-real-pilot-readiness-review.md` | `pass` | Exists as readiness artifact. |
| `docs/37-approved-pilot-launch-plan.md` | `pass` | Exists as controlled launch entrypoint. |
| `docs/38-first-pilot-checkpoint-protocol.md` | `pass` | Exists as checkpoint protocol artifact. |
| `docs/39-local-pilot-workspace.md` | `pass` | Exists as workspace artifact. |
| `docs/40-pilot-preflight-verification.md` | `pass` | Exists as preflight artifact. |
| `docs/27-report-v0-delivery-plan.md` | `pass` | Exists and includes post-0076 memo. |
| `templates/data_authorization_request.md` | `pass` | Exists. |
| `templates/stakeholder_authorization_decision_record.md` | `pass` | Exists. |
| `templates/real_pilot_readiness_review.md` | `pass` | Exists. |
| `templates/controlled_launch_details_template.md` | `pass` | Exists. |
| `templates/manual_collection_rehearsal_checklist.md` | `pass` | Exists. |
| `templates/controlled_rehearsal_review.md` | `pass` | Exists. |
| `templates/annotator_calibration_packet_template.md` | `pass` | Exists. |
| `templates/pilot_checkpoint_review.md` | `pass` | Exists. |
| `experiments/evaluation-notes/0014-controlled-rehearsal-review-protocol.md` | `pass` | Exists. |
| `templates/report_review_feedback.md` | `pass` | Exists. |

## Final Sign-Off

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Research owner | AUTO-REPORT-REVIEW-01 | `approve` | 2026-04-26 | Repo self-review passes for report-package consistency. |
| Legal/privacy reviewer | external reviewer | `pending` |  | Needed before external delivery if policy wording changes. |
| Domain reviewer | external reviewer | `pending` |  | Needed if stakeholder wants more rule-family interpretation. |
| Technical reviewer | external reviewer | `pending` |  | Needed if baseline or schema interpretation changes. |
| Stakeholder owner | external stakeholder | `pending` |  | Needed to select post-0076 path. |

## Blocker Log

| Blocker | Owner | Required fix | Due date | Resolved? |
|---|---|---|---|---|
| No internal repo blocker found in this self-review. External sign-off is still pending. | stakeholder owner | Choose post-0076 path before new evidence collection. | before next tranche | no |
