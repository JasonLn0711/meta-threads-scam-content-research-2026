# Post-0076 Reviewer Re-Check Request

## Purpose

Use this message when sending the rebuilt post-0076 reviewer package back to reviewers after the `revise_before_delivery` fixes.

This is a delivery/re-check request only. It does not authorize item `0077`, new evidence collection, browser/crawler expansion, confirmed-pointer intake, embedding/model training, production detection, legal fraud determination, or raw evidence in git.

## Suggested Message

Subject: Re-check request: revised Threads scam-content research v0 post-0076 package

Hi [Name],

The post-0076 report v0 package has been revised after reviewer feedback.

Please review the rebuilt package and confirm whether it can move from `revise_before_delivery` to delivery approval under `report_only_delivery`.

Package details:

| Field | Value |
|---|---|
| Package | post-0076 report v0 reviewer package |
| ZIP path | `/Users/iKev/Downloads/post-0076-report-v0-package.zip` |
| File count | 28 files |
| ZIP SHA-256 | `bc465816b937210a1bb3429cbda523e13b7f567a38304aa4ac138412d3d4f85c` |
| Package-build commit | `9ee1d89` |
| Remote main before this re-check request note | `2ca15434f03caef815c81313bc869d3347ae4e8a` |

What changed since the first review:

- Added a selected-package manifest so the ZIP is clearly not a full repo snapshot.
- Added reviewer README and canonical response table.
- Added validation provenance for checkpoint 0055 and local item 0076.
- Replaced stale pilot-execution decision vocabulary with the post-0076 three-path decision vocabulary.
- Clarified that `strict-valid` means schema/validation pass, not evidence approval.
- Clarified that baseline metrics are smoke-test metrics, not production performance.
- Marked historical launch and authorization materials as full-repo context only.
- Rebuilt the ZIP and recorded leakage/validation QA in `reports/post-0076-revised-package-qa.md`.

Please return:

| Field | Response |
|---|---|
| Selected path | `report_only_delivery` / `targeted_confirmed_pointer_tranche` / `calibration_only_browser_tranche` |
| Delivery status | `approve_with_minor_edits` / `revise_before_delivery` / `block_delivery` |
| Required changes before delivery |  |
| Required conditions before any future new evidence |  |
| External sign-offs still required | legal/privacy / domain / technical / stakeholder |
| Decision owner |  |
| Date |  |
| Notes |  |

Recommended response if no further blocker remains:

```text
Selected path: report_only_delivery
Delivery status: approve_with_minor_edits
New evidence collection: not authorized
Broad browser/crawler expansion: not authorized
Embedding/model training: not authorized
Production detector claim: not authorized
Legal fraud determination claim: not authorized
```

Best,

[Your name]
