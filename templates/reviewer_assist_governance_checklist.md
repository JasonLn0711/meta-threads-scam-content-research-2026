# Reviewer Assist Governance Checklist

Use this checklist before any Reviewer Assist labor-savings slice is treated as evaluable.

## Boundary Checks

| Check | Status | Note |
|---|---|---|
| No raw Threads text in tracked files | pass / fail |  |
| No raw reply text in tracked files | pass / fail |  |
| No raw OCR text in tracked files | pass / fail |  |
| No raw URLs or handles in tracked files | pass / fail |  |
| No screenshots or browser artifacts in tracked files | pass / fail |  |
| No credentials, tokens, or session values | pass / fail |  |
| No controlled-store locators in tracked files | pass / fail |  |
| No stakeholder case IDs in tracked files | pass / fail |  |

## Decision Checks

| Check | Status | Note |
|---|---|---|
| Human final decision preserved | pass / fail |  |
| Assist output does not decide scam label | pass / fail |  |
| Assist output does not imply legal fraud | pass / fail |  |
| Assist output does not imply enforcement action | pass / fail |  |
| Assist output does not imply public warning | pass / fail |  |
| Existing cases are not treated as representative | pass / fail |  |
| Automatic discovery-method purpose is explicit | pass / fail |  |

## Stop Conditions

Stop the evaluation if any check above fails or if reviewers cannot complete the slice without adding raw evidence to git.
