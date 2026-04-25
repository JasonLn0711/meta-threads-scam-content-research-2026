# Option A Limited Browser Tranche Run Record 0038

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full HTML, exact raw storage paths, access-list details, stock names, stock codes, brand names, price values, contact handles, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled store.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `OPTION-A-THREADS-PILOT-V1-0046-0055-LIMITED-BROWSER-TRANCHE` |
| Date opened | `2026-04-25` |
| Related decision | `0059-select-option-a-limited-browser-tranche-after-checkpoint-0042` |
| Related checkpoint | `threads_pilot_v1_0042` |
| Prospective item range | `threads_pilot_v1_0046` through `threads_pilot_v1_0055` |
| Operator | `AUTO-OP-01` |
| Purpose | resume bounded intake after checkpoint 0042 under explicit stakeholder Option A limits |
| Primary source path | approved browser-session capture |
| Supplemental source path | CIB/stakeholder confirmed pointer, if provided |
| Raw output location | controlled store only |
| Repo-visible raw output | no |
| Run status | `open_not_executed` |

## Authorization And Scope

| Check | Result |
|---|---|
| Stakeholder selected Option A | yes |
| Next tranche size | 10 selected items maximum |
| Candidate review cap | 20 candidates maximum |
| Selected item cap | 10 items maximum |
| Primary source path approved | approved browser session capture |
| Supplemental confirmed pointers allowed | yes, if provided |
| Fast different-angle second review required | yes |
| Strict validation required | yes |
| Broad crawler expansion | no |
| Private-message access | no |
| Profile graph capture | no |
| Landing-page or redirect-chain capture | no |
| Embedding/model training | no |
| Raw output in git | no |

## Candidate And Selection Ledger

| Counter | Limit | Current |
|---|---:|---:|
| Candidates reviewed | 20 | 0 |
| Selected items | 10 | 0 |
| Strict-valid selected items | 10 | 0 |
| Second-reviewed selected items | 10 | 0 |

## Candidate Review Rules

- Use the approved browser session only within the bounded source path.
- Review no more than 20 candidates total for this run.
- Select no more than 10 items total for this run.
- Stop immediately when either cap is reached.
- Query terms and visible candidate text may help find candidates but must not become labels.
- Prefer candidates that add evidence-family diversity, reply/comment evidence, private-channel migration, contact/action gates, payment/deposit cues, testimonial proof, urgency, impersonation/contact hijack, or hard-negative boundary value.
- Do not continue into profile graph capture, private messages, landing pages, redirect chains, or unrelated account exploration unless a later decision authorizes that scope.

## Required Per-Item Workflow

Each selected item must complete:

1. controlled browser-session capture;
2. raw evidence preservation in the controlled store;
3. redacted manual entry;
4. manual record build;
5. one-item strict validation;
6. aggregate strict validation;
7. dataset audit;
8. fast different-angle second review;
9. repo-safe evaluation note and, if a new rule family is accepted, decision log;
10. run index update.

No item counts toward the selected-item cap until strict validation has 0 errors and second review has accepted the final label/risk/evidence family.

## Second Review Requirements

The second review must explicitly challenge:

- whether the item is scam, non-scam, uncertain, or insufficient evidence;
- whether the evidence supports high, medium, or low risk;
- whether reply/comment evidence changes the first-pass interpretation;
- whether anti-scam or victim-warning language is protective rather than conversion-oriented;
- whether contact/action gates, private-channel migration, or payment/deposit cues are present in the redacted evidence;
- whether the item should be downgraded to `uncertain` or `insufficient_evidence`.

The review should be fast, but it must use a different angle from the capture/extraction pass.

## Stop Conditions

Stop this run if:

- 20 candidates have been reviewed;
- 10 selected items have been accepted;
- strict validation produces unresolved errors;
- redaction boundary fails;
- raw evidence is about to enter git;
- the approved browser-session path becomes unavailable;
- the run starts needing profile graph, private messages, landing pages, redirect chains, or model/embedding work;
- a stakeholder changes the source or evidence boundary.

## Current Decision

Run 0038 is opened but not executed.

The next concrete execution step is to review the first approved browser-session candidate for item `0046`, unless a CIB/stakeholder confirmed pointer is provided first.
