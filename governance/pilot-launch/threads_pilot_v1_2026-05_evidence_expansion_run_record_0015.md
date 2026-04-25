# Evidence-Expansion Run Record 0015

This is the non-sensitive tracked run record for the first post-gate evidence-expansion attempt after stakeholders approved all proposed evidence families.

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled location.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0015` |
| Date opened | `2026-04-25` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Prior gate | `EVIDENCE-SCOPE-THREADS-PILOT-V1-0014` |
| Prior decision | `0031-record-stakeholder-evidence-expansion-approval` |
| Target local item range | starts at `threads_pilot_v1_0018`; at most 10 selected items |
| Purpose | attempt a bounded evidence-expansion tranche using approved expanded evidence families |
| Current gate | `browser_session_execution_ready_api_path_blocked` |
| Run status | `preflight_complete_not_started` |

## Stakeholder Scope Approval

| Evidence family | Status | Repo-safe boundary |
|---|---|---|
| Redacted stakeholder exemplars | approved | Redacted fields only in git; raw/source case IDs outside git. |
| Risk-relevant OCR excerpt | approved | Risk-relevant excerpt only; no full screenshot text dump in git. |
| Screenshot raw storage | approved_with_limits | Controlled store only; no screenshot in git. |
| Narrow adjacent reply context | approved | Fixed narrow context only; no broad comment capture; no handles in git. |
| Visible-link domain/category | approved | Domain/category or redacted reference only; no full raw URL in git. |
| Redirect or landing-page evidence | approved_with_limits | Category/summary only in git; raw capture outside git. |
| Profile/account context review | approved_with_limits | Only if needed for the scoped item-level question; aggregate/redacted summary only in git. |

## Pre-Execution Requirements

| Check | Required result |
|---|---|
| Approved browser/session/API access path | browser/session path ready; API path blocked |
| Controlled store | ready for browser/session raw screenshot/OCR/reply/link/redirect/profile evidence |
| Latest local aggregate | strict-valid; 17 checked, 0 errors, 0 warnings |
| Candidate cap | at most 20 candidates |
| Selected item cap | at most 10 items |
| Second-review owner | assigned before item counts |
| Redaction rule | approved fields only; no raw identifiers in git |

## Preflight Result

| Check | Result |
|---|---|
| Browser storage-state shape | pass |
| API dry-run readiness | blocked; `META_API_PROBE_URL` missing or empty |
| Latest local aggregate strict validation | pass |
| Pilot preflight | pass; 21 OK, 0 WARN, 0 ERROR |
| Execution path allowed now | browser/session only |
| API execution allowed now | no |

## Run Limits

| Limit | Value |
|---|---|
| Target selected item count | at most 10 |
| Candidate review cap | 20 candidates total |
| Parallel workers | 1 |
| Minimum delay between page/object fetches | 30 seconds |
| Burst behavior | none |
| Item 0028 allowed? | no |

## Candidate Reviewability Rule

A candidate may pass reviewability only if all are true:

- candidate content is independent item-level evidence, not a query echo or interface text;
- evidence can be reduced to approved redacted fields;
- raw screenshots, full OCR, full URLs, handles, raw replies, landing-page captures, redirect-chain details, profile details, credentials, browser/session material, and sensitive investigative notes stay outside git;
- evidence supports a research label without legal fraud determination;
- second review is completed before the item counts.

## Stop Conditions

Stop immediately if:

- login challenge, captcha, account warning, 403/429, or platform warning appears;
- more than 20 candidates must be reviewed;
- candidate review requires broad profile graph review or broad comments beyond this run scope;
- selected output cannot be reduced to approved redacted local JSON fields;
- raw evidence would need to enter git;
- item 0028 would be needed to make progress.

## Execution Status

| Field | Value |
|---|---|
| Run started? | no |
| Candidate reviewed count | 0 |
| Selected item count | 0 |
| Local records built? | no |
| Strict validation result | not_applicable |
| Second review complete? | no |

## Next Action

Execute only through the approved browser/session path unless the API path is later completed and rechecked. Keep the run bounded to at most 20 candidates reviewed and at most 10 selected items, from item 0018 through item 0027. Do not open item 0028 in this run.
