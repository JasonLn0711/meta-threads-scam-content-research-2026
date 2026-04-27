# Checkpoint 0081 Package QA

## Purpose

Record the repo-safe QA result for the selected checkpoint 0081 reviewer package copied to Downloads.

This note contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, exact controlled-store paths, or stakeholder case IDs.

## Package

| Field | Value |
|---|---|
| Package directory | `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package` |
| ZIP path | `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package.zip` |
| Package version/date | 2026-04-27 recipient adoption dispatch rebuild |
| Package file count | 43 files |
| ZIP SHA-256 | external handoff checksum generated after ZIP rebuild in `/Users/iKev/Downloads/checkpoint-0081-cib-approved-package.zip.sha256` |
| Package status | recipient adoption dispatch log opened; ready for allowed checkpoint use |
| Superseded package handling | old post-0076 package moved out of Downloads top level into `_superseded-review-packages/2026-04-27-post-0076-superseded-by-checkpoint-0081/` |

## Included Entry Points

| File | Purpose |
|---|---|
| `REVIEWER_README.md` | Reviewer reading order and response table. |
| `PACKAGE_MANIFEST.md` | Exact selected package contents and exclusions. |
| `reports/checkpoint-0081-executive-addendum.md` | Short reviewer entry point. |
| `reports/checkpoint-0081-cib-technical-report.pdf` | Compiled PDF technical report with tables and figures. |
| `reports/checkpoint-0081-cib-technical-report.tex` | LaTeX technical report source with tables and figures. |
| `reports/checkpoint-0081-approved-package-index.md` | Canonical approved package index. |
| `reports/checkpoint-0081-final-handoff-note.md` | Final handoff note and recipient-specific sharing gate. |
| `reports/checkpoint-0081-recipient-adoption-tracker.md` | Repo-safe recipient acceptance and conditions tracker. |
| `reports/checkpoint-0081-recipient-adoption-request.md` | Repo-safe message/form for recipient acceptance. |
| `reports/checkpoint-0081-recipient-adoption-dispatch-log.md` | Repo-safe dispatch outbox and receipt tracker. |
| `reports/checkpoint-0081-package-qa.md` | Package QA, checksum, validation, and leakage-scan summary. |
| `reports/checkpoint-0081-reviewer-delivery-tracker.md` | Reviewer response tracker and minor-edit resolution log. |
| `reports/checkpoint-0081-technical-governance-recheck.md` | Technical/governance re-check result. |
| `experiments/evaluation-notes/0089-checkpoint-0081-cib-approved-synthesis.md` | Detailed 78-record synthesis. |
| `decision-log/0105-approve-cib-78-record-checkpoint-synthesis.md` | CIB approval decision record. |
| `decision-log/0106-deliver-checkpoint-0081-review-package.md` | Delivery decision and non-authorizations. |
| `decision-log/0107-record-checkpoint-0081-approve-with-minor-edits.md` | Reviewer response and minor-edit resolution decision. |
| `decision-log/0108-record-checkpoint-0081-technical-governance-recheck.md` | Technical/governance re-check decision. |
| `decision-log/0109-record-checkpoint-0081-final-handoff.md` | Final handoff decision and sharing gate. |

## Validation

| Check | Result |
|---|---|
| 78-record strict validation | pass: 0 errors, 0 warnings |
| Baseline smoke run | `checkpoint-0081-cib-approved-smoke-v1` |
| Baseline precision | 0.829 |
| Baseline recall | 0.944 |
| Baseline F1 | 0.883 |
| Baseline false positives | 7 |
| Baseline false negatives | 2 |
| Baseline triage support caveat | baseline uses `final_risk_level` when present; one duplicate/insufficient-evidence trace explains support `high 36`, `medium 10`, `low 32` versus aggregate risk `high 36`, `medium 11`, `low 31` |
| Technical/governance re-check | pass |
| Final handoff note | present |
| Recipient adoption tracker | present |
| Recipient adoption request | present |
| Recipient adoption dispatch log | present |
| `.DS_Store` in package directory | none found |
| ZIP created | yes |
| LaTeX static structure check | pass: document, table, figure, tabular, tabularx, longtable, and tikzpicture environments balanced |
| PDF compilation | pass with `tectonic`; only minor line-breaking warning remains |

## Leakage Scan

The package was scanned for raw Threads URLs, raw handles, post-code-like strings, cookie/token/session terms, raw capture markers, contact-handle markers, and local project paths.

The scan did not find actual raw Threads URLs, raw handles, credential values, browser/session artifacts, or local controlled-store paths. Hits were limited to governance boundary language, schema identifiers, and controlled-store policy wording.

## Boundary

This package is a selected reviewer package, not a full repo snapshot. Older checkpoint 0055 and post-0076 files remain in the repo as historical context, but the package entry point is checkpoint 0081.

The package does not authorize item `0082`, broad browser/crawler expansion, confirmed-pointer intake, embedding/model training, production detection, legal fraud determinations, or raw evidence in git.

## Superseded Package Handling

The old post-0076 package is no longer the canonical reviewer entry point. To avoid reviewer confusion, it was moved out of the Downloads top level into a dated superseded archive with a `README_SUPERSEDED.md` notice.

Current reviewer-facing package:

```text
/Users/iKev/Downloads/checkpoint-0081-cib-approved-package.zip
```
