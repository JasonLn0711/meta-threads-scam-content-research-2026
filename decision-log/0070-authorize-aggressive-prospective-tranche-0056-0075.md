# Decision 0070: Authorize Aggressive Prospective Tranche 0056-0075

## Status

Accepted.

## Decision

Authorize an aggressive but bounded prospective tranche after the approved checkpoint 0055 package.

The new prospective tranche is:

- item range: `threads_pilot_v1_0056` through `threads_pilot_v1_0075`;
- candidate review cap: 50 candidates maximum;
- selected-item cap: 20 items maximum;
- primary source path: CIB/stakeholder/project-owner confirmed pointers;
- supplemental source path: approved browser-session or API/session-aware candidate discovery only when needed to diversify evidence families;
- required second review: yes;
- required strict validation: yes;
- raw evidence location: controlled store only.

The new run record is:

- `governance/pilot-launch/threads_pilot_v1_2026-05_aggressive_prospective_tranche_run_record_0039.md`

## Context

Checkpoint 0055 is approved under C2 and the package is complete. The user requested an aggressive next authorized prospective tranche.

"Aggressive" is interpreted as larger and more proactive than run 0038 while still preserving governance limits. It does not mean unlimited crawling, unrestricted profile review, private-message access, landing-page expansion, redirect-chain capture, embedding/model training, production detection, or raw evidence in git.

Checkpoint 0055 showed that confirmed pointers were higher-yield for final scam/high-risk rule learning than browser-session search alone. Therefore, this tranche prioritizes confirmed pointers and uses browser/API-session-aware discovery only as a bounded supplemental path.

## Options Considered

| Option | Decision | Rationale |
|---|---|---|
| Unlimited aggressive crawler | Rejected | Violates governed pilot boundaries and increases privacy/source-skew risk. |
| Repeat run 0038 browser-session pattern only | Rejected as primary | The last browser-session tranche added no final scam/high-risk records. |
| Confirmed-pointer-first aggressive tranche with browser/API supplement | Accepted | More likely to add final scam/high-risk evidence families while keeping hard caps and validation gates. |
| Report-only maintenance | Defer | The approved package is complete; the user requested a new prospective tranche. |

## Consequence

Item `0056` is now authorized only within run `0039` and only after run-level preflight confirms the approved source path, controlled-store boundary, second-review rule, and strict-validation gate.

No selected item counts unless it has:

- controlled capture;
- raw evidence preserved only in the controlled store;
- redacted local entry;
- manual record build;
- one-item strict validation;
- aggregate strict validation;
- fast different-angle second review;
- repo-safe evaluation note.

The tranche must stop when 50 candidates are reviewed or 20 selected items are accepted, whichever comes first.

## Not Authorized

- Unlimited crawler expansion.
- Private-message access.
- Profile graph capture.
- Landing-page or redirect-chain capture.
- Raw screenshots, raw text, raw handles, raw URLs, credentials, cookies, tokens, browser profiles, storage state, or stakeholder case IDs in git.
- Embedding/model training.
- Production detection.
- Legal fraud determinations.
