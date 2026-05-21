# Decision 0059: Select Option A Limited Browser Tranche After Checkpoint 0042

## Status

Accepted.

## Decision

Stakeholders select Option `A`: resume bounded intake after the 42-record checkpoint.

The next prospective tranche starts at item `0046` and may continue through item `0055`.

This decision authorizes a limited run design only. It does not authorize broad crawler expansion, unrestricted profile review, private-message access, landing-page or redirect-chain expansion, embedding/model training, production scoring, or legal fraud determination.

## Approved Limits

| Field | Value |
|---|---|
| Next tranche size | 10 items |
| Candidate review cap | 20 candidates |
| Selected item cap | 10 items |
| Prospective item range | `threads_pilot_v1_0046` through `threads_pilot_v1_0055` |
| Primary source path | approved browser-session capture |
| Supplemental source path | CIB/stakeholder confirmed pointer, if provided |
| Second review | required; use a fast, different-angle review before counting |
| Strict validation | required before any item counts |
| Raw evidence | controlled store only |
| Repo-visible evidence | redacted derived fields and aggregate/run notes only |

Items `0043` through `0045` already exist as post-checkpoint work. They remain outside the 42-record synthesis and are not used to consume this prospective item `0046-0055` authorization.

## Required Second Review

The second review must be faster than a full re-collection pass but must use a different angle from the first pass:

- first pass: capture and redacted evidence extraction;
- second pass: label/risk/evidence-family challenge review;
- required checks: scam versus anti-scam warning, reply/comment evidence, private-channel migration, contact/action gate, payment/deposit/wallet cues, testimonial/proof claims, urgency, impersonation, and insufficient-evidence fallback;
- false-negative policy: maintain high recall, but preserve `uncertain` or `insufficient_evidence` when the redacted evidence cannot support a final label.

## Required Validation

Each selected item must pass:

- one-item strict JSON validation;
- aggregate strict JSONL validation;
- dataset audit;
- rule-baseline smoke run when the record changes the aggregate;
- repo-safe redaction scan before commit.

No selected item counts until strict validation has 0 errors.

## Source Boundary

Approved browser-session capture is the primary source path. It may review at most 20 candidates and select at most 10 items.

CIB/stakeholder confirmed pointers may supplement the tranche. If a confirmed pointer is used, the item still requires controlled raw preservation, redacted manual entry, strict validation, and second review.

Query terms, browser search results, or visible candidate text are candidate-finding tools only. They do not become labels.

## Consequence

Open a bounded run record for the prospective item `0046-0055` tranche before executing collection.

If the candidate review cap is exhausted before 10 selected items, stop and write a method/result note instead of expanding the run.
