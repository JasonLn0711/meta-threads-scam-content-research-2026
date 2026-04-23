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
| Report states Threads-only phase-1 scope |  |  |  |
| Report says this is research, not production detection |  |  |  |
| Report avoids legal fraud determinations |  |  |  |
| Report avoids claims of platform-scale coverage |  |  |  |
| Report avoids claims based on real annotated results before they exist |  |  |  |
| Deferred scope is explicit: video, deepfake detection, automation, cross-platform integration |  |  |  |

## 2. Governance And Privacy Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report says no automated collection without authorization |  |  |  |
| Report points to data authorization and go/no-go artifacts |  |  |  |
| Raw evidence is described as outside git |  |  |  |
| Screenshots, URLs, contact handles, and OCR privacy risks are acknowledged |  |  |  |
| Retention, access, and redaction decisions are listed as stakeholder decisions |  |  |  |
| No real personal data, screenshots, source URLs, credentials, tokens, or investigative details are included |  |  |  |

## 3. Terminology Consistency

| Check | Status | Owner | Notes |
|---|---|---|---|
| Primary labels are exactly `scam`, `non_scam`, `uncertain`, `insufficient_evidence` |  |  |  |
| Risk levels are exactly `high`, `medium`, `low` |  |  |  |
| Evidence sufficiency values match the labeling schema |  |  |  |
| Annotation confidence values match the labeling schema |  |  |  |
| Field names match `data-contracts/thread_item_schema_v1.json` |  |  |  |
| The report uses "scam-like" or "high-risk" when evidence is incomplete |  |  |  |

## 4. Dataset And Annotation Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| `thread_item` is clearly defined as the unit of review |  |  |  |
| Text, replies, OCR, links, handles, redirects, and screenshots are treated as evidence fields |  |  |  |
| 5-item calibration, 50-item pilot, and 100-200 item expansion are staged clearly |  |  |  |
| Pilot composition is diagnostic and not presented as prevalence |  |  |  |
| `uncertain` and `insufficient_evidence` boundaries are preserved |  |  |  |
| Adjudication and second-review paths are described |  |  |  |

## 5. Baseline And Evaluation Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| Text-only baseline uses `post_text` |  |  |  |
| Context baseline uses `reply_texts` |  |  |  |
| OCR baseline uses `ocr_text` |  |  |  |
| Link/redirection baseline uses `external_links`, `visible_contact_handles`, and `visible_platform_redirects` |  |  |  |
| Evaluation uses adjudicated or high-confidence labels where possible |  |  |  |
| `uncertain` and `insufficient_evidence` are not forced into binary metrics |  |  |  |
| Reviewer burden and explainability are evaluated, not only precision/recall |  |  |  |

## 6. Budget-Fit Review

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report explains why the plan fits an NTD 1.8M research budget |  |  |  |
| Report identifies high-ROI work for phase 1 |  |  |  |
| Report identifies low-ROI or out-of-scope work |  |  |  |
| The four-week path is plausible for a small team |  |  |  |
| No hidden dashboard, production platform, or large-model-training commitment is implied |  |  |  |

## 7. Stakeholder Decision Readiness

| Check | Status | Owner | Notes |
|---|---|---|---|
| Report asks for a concrete pilot decision |  |  |  |
| Source authorization questions are clear |  |  |  |
| Field-retention questions are clear |  |  |  |
| Screenshot and link-policy questions are clear |  |  |  |
| Access and retention questions are clear |  |  |  |
| Report explains what happens after `go`, `go_with_limits`, or `no_go` |  |  |  |

## 8. Artifact Link Check

| Artifact | Status | Notes |
|---|---|---|
| `reports/threads-scam-content-research-v0.md` |  |  |
| `reports/threads-scam-content-research-v0-executive-brief.md` |  |  |
| `docs/25-stakeholder-pilot-kickoff.md` |  |  |
| `docs/26-pilot-go-no-go-checklist.md` |  |  |
| `docs/27-report-v0-delivery-plan.md` |  |  |
| `templates/data_authorization_request.md` |  |  |
| `templates/report_review_feedback.md` |  |  |

## Final Sign-Off

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Research owner |  | `approve` / `revise` / `block` |  |  |
| Legal/privacy reviewer |  | `approve` / `revise` / `block` |  |  |
| Domain reviewer |  | `approve` / `revise` / `block` |  |  |
| Technical reviewer |  | `approve` / `revise` / `block` |  |  |
| Stakeholder owner |  | `approve` / `revise` / `block` |  |  |

## Blocker Log

| Blocker | Owner | Required fix | Due date | Resolved? |
|---|---|---|---|---|
|  |  |  |  |  |

