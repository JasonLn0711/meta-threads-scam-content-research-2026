# Reply-Aware Recall Run Record 0016

This is the non-sensitive tracked run record for the next bounded evidence-expansion design before item `0024`.

Do not add raw Threads content, screenshots, full item URLs, raw handles, stakeholder case IDs, credentials, cookies, tokens, browser profiles, HAR files, full API responses, exact raw storage paths, access-list details, or sensitive investigative notes to this file. Exact sensitive values remain in the approved controlled location.

## Run Identity

| Field | Value |
|---|---|
| Run ID | `CRAWL-THREADS-PILOT-V1-0016` |
| Date opened | `2026-04-25` |
| Dataset ID | `threads_pilot_v1_2026-05` |
| Collection batch ID | `threads_pilot_v1_2026-05` |
| Prior checkpoint | `CHK-THREADS-PILOT-V1-0023` |
| Prior decision | `0032-close-run-0015-and-require-new-run-design` |
| Target local item range | `threads_pilot_v1_0024` through `threads_pilot_v1_0027` |
| Purpose | test reply/comment-aware, high-recall evidence discovery without letting one seed consume the full candidate budget |
| Current gate | `second_review_complete` |
| Run status | `local_records_built_second_reviewed_strict_valid` |

## Scope Rationale

Run 0015 proved the richer evidence path can build strict-valid, second-reviewed records, but it still produced no final `scam` or high-risk items. It also allowed one seed to consume all 20 candidate reviews.

Run 0016 changes the method:

- distribute candidate reviews across evidence families;
- inspect a narrow approved reply/comment window when available;
- treat anti-scam wording plus investment/profit funnel signals as a recall-priority pattern, not as automatic negation;
- prioritize false-negative reduction at triage;
- preserve human second review before final labels;
- keep raw/session/candidate material outside git.

## Approved Evidence Families

| Evidence family | Status | Repo-safe boundary |
|---|---|---|
| Top-level post text | approved | Redacted/minimized text only. |
| Narrow relevant replies/comments | approved_with_limits | At most 3 selected relevant replies/comments per candidate; no broad comment capture; no raw handles in git. |
| Reply/comment visible links | approved_with_limits | Domain/category or redacted reference only; no full raw URL in git. |
| Private-channel/contact signals | approved_with_limits | Category/redacted handle only; no raw handle or account ID in git. |
| Wallet/deposit/payment signals | approved | Risk-relevant excerpt/category only; no payment details or raw wallet address in git. |
| Screenshot/OCR evidence | approved_with_limits | Only if directly visible and needed; risk-relevant excerpt in git; raw screenshot controlled store only. |
| Redirect/landing evidence | approved_with_limits | Category/summary only in git; raw capture outside git. |

## Candidate Budget

| Limit | Value |
|---|---|
| Total candidate review cap | 20 candidates |
| Per evidence-family cap | 4 candidates |
| Selected item cap | 4 items |
| Target selected items | `0024` through `0027` only |
| Item `0028` allowed? | no |
| Parallel workers | 1 |
| Minimum delay between page/object fetches | 30 seconds |
| Burst behavior | none |

The per-family cap is mandatory. A family may produce fewer than 4 reviewable candidates, but it must not consume another family's budget unless a later decision explicitly changes the run.

## Risk-Probe Seed Matrix

Queries are only candidate-finding hints. Query terms cannot become labels, evidence, or proof.

| Seed ID | Risk domain | Visible signal family | Candidate cap | Selection target |
|---|---|---|---:|---|
| `RP-0016-01` | investment/finance | reply/comment private-channel or add-friend signal | 4 | at most 1 item |
| `RP-0016-02` | crypto/wallet | reply/comment wallet, deposit, or transfer signal | 4 | at most 1 item |
| `RP-0016-03` | easy-income/recruitment | reply/comment contact handle or messaging-app migration | 4 | at most 1 item |
| `RP-0016-04` | guaranteed outcome | guarantee plus link/contact/comment signal | 4 | at most 1 item |
| `RP-0016-05` | testimonial proof | earnings/proof screenshot plus link/contact/comment signal | 4 | at most 1 item |

Anti-scam wording is not a safe-control signal by itself. If a candidate says it hates, dislikes, rejects, or warns against scams while also offering an investment/profit path or showing links, contact handles, add-friend instructions, private-channel migration, wallet/deposit/payment language, or testimonial proof, route it to high-recall triage and second review.

## Reply/Comment Review Window

For each candidate, review only the approved narrow context:

- the top-level visible candidate content;
- at most 3 selected relevant replies/comments visible in the approved browser/session path;
- only replies/comments with risk-relevant links, handles, private-channel migration, add-friend instructions, wallet/deposit/payment language, suspicious domains, or explicit negation/control evidence;
- anti-scam wording plus investment/profit funnel signals must be preserved as a review note in redacted form;
- no broad comment scrolling, profile graph review, follower/following review, or unrelated replies.

## Candidate Reviewability Rule

A candidate may pass reviewability only if all are true:

- candidate content is independent item-level evidence, not a query echo or interface text;
- reply/comment evidence is narrow, selected, and risk-relevant;
- evidence can be reduced to approved redacted fields;
- raw screenshots, full OCR, full URLs, handles, raw replies, landing-page captures, redirect-chain details, profile details, credentials, browser/session material, and sensitive investigative notes stay outside git;
- evidence supports a research label without legal fraud determination;
- second review is completed before the item counts.

## Pre-Execution Requirements

| Check | Required result |
|---|---|
| Approved browser/session/API access path | browser/session ready or API/session-aware path ready |
| Controlled store | ready for raw page/session/reply/link/screenshot/OCR artifacts |
| Latest local aggregate | strict-valid checkpoint 0023 |
| Candidate caps | 20 total and 4 per family |
| Selected item cap | at most 4 selected items |
| Redaction rule | approved fields only; no raw identifiers in git |
| Second-review owner | assigned before selected items count |

## Preflight Result

| Check | Result |
|---|---|
| Browser storage-state shape | pass; cookie and origin arrays present |
| API dry-run readiness | blocked; `META_API_PROBE_URL` missing or empty |
| Latest local aggregate strict validation | pass; 23 checked, 0 errors, 0 warnings |
| Pilot preflight | pass; 21 OK, 0 WARN, 0 ERROR |
| Execution path allowed now | browser/session only |
| API execution allowed now | no |

## Execution Result

| Field | Result |
|---|---|
| Execution path used | approved browser/session path |
| API path used | no |
| Candidates reviewed | 20 |
| Per-family candidate cap | respected; 4 candidates in each of 5 families |
| Selected local items | 4 |
| Local item range created | `threads_pilot_v1_0024` through `threads_pilot_v1_0027` |
| Raw output location | controlled store only |
| Git-safe output | redacted local manual entries and local manual records only |
| Candidate cap reached? | yes |
| Selected item cap reached? | yes |
| Anti-scam camouflage candidates observed | 2 |

### Repo-Safe Aggregate

| Metric | Value |
|---|---|
| `manual_entry_0024.json` through `manual_entry_0027.json` created locally | yes |
| `manual_record_0024.json` through `manual_record_0027.json` built locally | yes |
| Checkpoint file | `data/interim/manual_records_checkpoint_0027.jsonl` |
| Strict validation | pass; 27 checked, 0 errors, 0 warnings |
| Run 0016 labels before second review | 4 `uncertain` |
| Run 0016 risk levels before second review | 4 `medium` |
| Run 0016 visible signal tags | 4 `visible_external_link`; 4 `private_channel_redirect`; 4 `contact_handle_visible`; 1 `payment_deposit_or_fee_request`; 1 `vague_offer_strong_benefit` |

Run 0016 corrected the run 0015 budget problem: every evidence family received exactly 4 reviewed candidates before selection. Query terms remain candidate-finding hints only and do not determine labels.

### Second-Review Result

| Metric | Value |
|---|---|
| Items second-reviewed | `threads_pilot_v1_0024` through `threads_pilot_v1_0027` |
| Final run 0016 labels | 2 `non_scam`; 2 `uncertain` |
| Final run 0016 risk levels | 2 `low`; 2 `medium` |
| False-positive pressure cases | 2 |
| Boundary/uncertainty cases | 2 |
| Strict validation after second review | pass; 27 checked, 0 errors, 0 warnings |

The second review kept high-recall private-channel/link/contact triage intact, but did not let those categories alone determine final labels. Security-warning or ordinary messaging-app discussion patterns were finalized as `non_scam` / `low`; crypto/account/deposit-management context and private-channel risk-property context remained `uncertain` / `medium`.

## Stop Conditions

Stop immediately if:

- login challenge, captcha, account warning, 403/429, or platform warning appears;
- any family reaches 4 reviewed candidates;
- total reviewed candidates reaches 20;
- selected items reach `0027`;
- item `0028` would be needed to make progress;
- candidate review requires broad comment capture, profile graph review, or unrelated replies;
- selected output cannot be reduced to approved redacted local JSON fields;
- raw evidence would need to enter git.

## Execution Status

| Field | Value |
|---|---|
| Run started? | yes |
| Candidate reviewed count | 20 |
| Selected item count | 4 |
| Local records built? | yes |
| Strict validation result | pass; 27 checked, 0 errors, 0 warnings |
| Second review complete? | yes |

## Next Action

Update the checkpoint interpretation from 23 to 27 strict-valid local records, then decide whether item `0028` requires a new run record, decision gate, or stop/pause decision.
