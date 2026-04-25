# Post-Run 0039 Confirmed Pointer Intake Record 0040

This is the non-sensitive tracked intake record for the next confirmed-pointer tranche after run `0039`.

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, contact handles, stock names, stock codes, price values, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store or stakeholder system.

## Intake Identity

| Field | Value |
|---|---|
| Intake ID | `CONFIRMED-POINTER-THREADS-PILOT-V1-0040` |
| Date opened | `2026-04-26` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Related checkpoint | `threads_pilot_v1_0055` |
| Related request | `../../reports/post-run-0039-confirmed-pointer-request.md` |
| Prior decision | `0075-add-post-run-0039-confirmed-pointer-request` |
| Target local item range if pointers pass intake | starts at `threads_pilot_v1_0076`; maximum through `threads_pilot_v1_0080` before checkpoint |
| Purpose | obtain a small confirmed-pointer tranche after browser-session expansion failed to add new final scam/high-risk examples |
| Current gate | `pending_pointer_delivery` |
| Intake status | `opened_waiting_for_confirmed_pointers` |

## Why This Intake Exists

Run `0039` showed that increasing browser-session search volume did not solve the high-risk evidence gap.

The run produced strict-valid local candidate records, but second review found no new final scam/high-risk examples and identified duplicate/context-thin candidate pressure.

The next high-value source path is confirmed-pointer intake:

- one pointer at a time;
- controlled capture;
- raw evidence in the controlled store only;
- redacted local entry;
- strict validation;
- fast different-angle second review;
- rule-family update only when a reusable pattern is confirmed.

## Requested Pointer Type

| Requested type | Requirement |
|---|---|
| CIB/stakeholder/project-owner confirmed Threads scam pointer | Preferred |
| Reply/comment-driven scam-like example | Preferred |
| Private-channel migration or implicit DM funnel | Preferred |
| Contact/action gate example | Preferred |
| Wallet/deposit/payment cue example | Preferred |
| Testimonial, urgency, guarantee, or past-performance proof example | Preferred |
| Anti-scam warning hard negative | Optional only if explicitly requested |
| Broad browser-search candidate | Not requested in this intake |

## Intake Limits

| Limit | Value |
|---|---|
| Initial confirmed-pointer tranche | 3 to 5 pointers |
| Maximum pointers before checkpoint | 5 |
| Local item target | `0076-0080` maximum before checkpoint |
| Raw/source case IDs in git | no |
| Full URLs in git | no |
| Raw handles/account IDs in git | no |
| Screenshots in git | no |
| Required second review | yes, before any item counts |
| Required strict validation | yes, each record and aggregate |
| Browser-session candidate promotion | only through `docs/53-dedupe-first-full-thread-ready-gate.md` |

## Allowed Repo-Safe Fields

| Field family | Repo-safe allowed form |
|---|---|
| Post text | redacted/minimized excerpt only |
| Selected replies/comments | selected relevant redacted excerpts only |
| OCR text | risk-relevant redacted excerpt only |
| External links | domain/category or redacted reference only |
| Contact handles | platform/category plus `[redacted]` only |
| Redirect/landing evidence | category/summary only; no landing-page capture unless separately authorized |
| Screenshot reference | controlled-store reference category only; no image in git |
| Source URL | blank or redacted reference only |
| Stakeholder/source case ID | not in git |

## Required Controlled-Store Handling

Raw/source material must stay outside git. Controlled storage or stakeholder systems must hold:

- raw pointer source;
- full source URL or source case ID if needed;
- raw screenshots;
- raw reply/comment context;
- raw handles/account identifiers;
- raw HTML or browser-rendered text;
- raw OCR output;
- reviewer-sensitive notes.

## Intake Acceptance Criteria

A pointer can be converted into a local `manual_entry_####.json` only if all are true:

- source owner confirms the pointer is approved for this pilot;
- redaction owner confirms repo-safe fields are sufficient;
- raw/source material remains outside git;
- the item can be represented using the existing schema;
- the item is not only a query echo, interface text, unsupported rumor, or duplicate-only candidate;
- second-review owner is assigned;
- strict validation passes after build;
- any browser-discovered supplement passes the dedupe-first/full-thread-ready gate before promotion.

## Stop Conditions

Stop intake if:

- the pointer cannot be redacted safely;
- source ownership or approval is unclear;
- raw/source case IDs would need to enter git;
- broad unrelated personal data is required to understand the item;
- the item requires legal fraud determination rather than research triage;
- more than 5 pointers are needed before a checkpoint;
- stakeholders request browser-session search instead of confirmed pointers without a new decision;
- the work starts requiring private-message access, profile graph capture, landing pages, redirect chains, model training, or production detection.

## Execution Status

| Field | Value |
|---|---|
| Confirmed-pointer tranche approved? | pending |
| Pointer(s) received? | no |
| Redaction owner assigned? | pending |
| Second-review owner assigned? | pending |
| `manual_entry_0076.json` created? | no |
| Local records built? | no |
| Strict validation result | not run |
| Official checkpoint promoted? | no |

## Next Action

Wait for stakeholder/CIB/project-owner response to `reports/post-run-0039-confirmed-pointer-request.md`.

Do not create item `0076` until at least one confirmed pointer is delivered through the approved controlled channel and passes intake acceptance criteria.
