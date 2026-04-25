# Targeted Exemplar Intake Record 0017

This is the non-sensitive tracked intake record for requesting targeted redacted high-risk exemplars or exemplar-like pointers before item `0028`.

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled location or stakeholder system.

## Intake Identity

| Field | Value |
|---|---|
| Intake ID | `EXEMPLAR-THREADS-PILOT-V1-0017` |
| Date opened | `2026-04-25` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Related checkpoint | `CHK-THREADS-PILOT-V1-0027` |
| Prior decision | `0034-select-api-or-targeted-exemplar-method-before-item-0028` |
| Target local item range if exemplars pass intake | starts at `threads_pilot_v1_0028` |
| Purpose | obtain targeted redacted high-risk examples or pointers without repeating broad browser/session search |
| Current gate | `intake_open_waiting_for_redacted_exemplars` |
| Intake status | `not_received` |

## Why This Intake Exists

The browser/session search-result path has produced useful calibration evidence, but no final `scam` or high-risk records through checkpoint `0027`.

Decision 0034 selected two higher-yield paths before item `0028`:

- complete API/session-aware readiness; or
- obtain targeted redacted stakeholder/CIB exemplars or pointers.

The API path remains blocked until `META_API_PROBE_URL` is supplied and checked, so this record opens the targeted exemplar path.

## Requested Exemplar Type

| Requested type | Requirement |
|---|---|
| High-risk scam-like Threads examples | Preferred |
| Report-worthy scam-like examples known to CIB/stakeholders | Preferred |
| Reply/comment-driven scam-like examples | Preferred |
| Anti-scam camouflage plus investment/profit funnel | Preferred |
| Link/contact/private-channel migration examples | Preferred |
| Wallet/deposit/payment or credential-risk examples | Preferred |
| Benign comparator examples | Not requested in this intake |

## Intake Limits

| Limit | Value |
|---|---|
| Initial exemplar cap | 1 to 3 exemplars |
| Local item target | item `0028` first; do not exceed item `0030` without a later decision |
| Raw/source case IDs in git | no |
| Full URLs in git | no |
| Raw handles/account IDs in git | no |
| Screenshots in git | no |
| Required second review | yes, before any item counts |
| Required strict validation | yes, each record and aggregate |

## Allowed Repo-Safe Fields

| Field family | Repo-safe allowed form |
|---|---|
| Post text | redacted/minimized excerpt only |
| Selected replies/comments | up to 3 selected relevant redacted excerpts |
| OCR text | risk-relevant redacted excerpt only |
| External links | domain/category or redacted reference only |
| Contact handles | platform/category plus `[redacted]` only |
| Redirect/landing evidence | category/summary only |
| Screenshot reference | controlled-store reference category only; no image in git |
| Source URL | blank or redacted reference only |
| Stakeholder/source case ID | not in git |

## Required Controlled-Store Handling

Raw/source material must stay outside git. Controlled storage or stakeholder systems must hold:

- raw exemplar source;
- full source URL or source case ID if needed;
- raw screenshots;
- raw reply/comment context;
- raw handles/account identifiers;
- full redirect or landing-page capture;
- reviewer-sensitive notes.

## Intake Acceptance Criteria

An exemplar can be converted into `manual_entry_0028.json` only if all are true:

- source owner confirms the exemplar is approved for this pilot;
- redaction owner confirms repo-safe fields are sufficient;
- raw/source material remains outside git;
- the item can be represented using the existing schema;
- the item is not only a query echo, interface text, or unsupported rumor;
- second-review owner is assigned;
- strict validation passes after build.

## Stop Conditions

Stop intake if:

- the exemplar cannot be redacted safely;
- source ownership or approval is unclear;
- raw/source case IDs would need to enter git;
- broad unrelated personal data is required to understand the item;
- the item requires legal fraud determination rather than research triage;
- more than 3 exemplars are needed before a method review.

## Execution Status

| Field | Value |
|---|---|
| Exemplar received? | no |
| Redaction owner assigned? | pending |
| Second-review owner assigned? | pending |
| `manual_entry_0028.json` created? | no |
| Local records built? | no |
| Strict validation result | not_applicable |

## Next Action

Request 1 to 3 targeted redacted exemplars or exemplar-like pointers from CIB/stakeholders using this intake boundary. Do not create item `0028` until at least one approved exemplar is received, redacted, built, strict-validated, and second-reviewed.
