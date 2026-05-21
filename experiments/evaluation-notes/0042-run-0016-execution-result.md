# Run 0016 Execution Result

This is the repo-safe execution result for `CRAWL-THREADS-PILOT-V1-0016`.

Do not add raw Threads content, screenshots, full URLs, handles, cookies, browser storage state, API responses, candidate HTML, raw comments, or sensitive investigative notes to this file. Raw/session/candidate artifacts remain in the approved controlled store.

## Summary

| Field | Result |
|---|---|
| Date | `2026-04-25` |
| Execution path | approved browser/session path |
| API path | not used; still blocked until `META_API_PROBE_URL` is approved and ready |
| Candidate cap | 20 total |
| Per-family candidate cap | 4 |
| Candidates reviewed | 20 |
| Selected item cap | 4 |
| Selected local items | 4 |
| New local item range | `threads_pilot_v1_0024` through `threads_pilot_v1_0027` |
| Raw output | controlled store only |
| Strict validation | pass; 27 checked, 0 errors, 0 warnings |
| Second review | pending |

## Budget Result

| Evidence family | Candidates reviewed | Selected items |
|---|---:|---:|
| reply/private-channel or add-friend | 4 | 1 |
| reply/wallet deposit transfer | 4 | 1 |
| reply/contact or messaging migration | 4 | 1 |
| guarantee plus link/contact/comment | 4 | 0 |
| testimonial plus link/contact/comment | 4 | 1 |

The run fixed the run 0015 budget problem: no single seed consumed the full candidate cap.

## Local Build Result

| Artifact | Result |
|---|---|
| `manual_entry_0024.json` through `manual_entry_0027.json` | created locally under `data/interim/` |
| `manual_record_0024.json` through `manual_record_0027.json` | built locally under `data/interim/` |
| `manual_records_checkpoint_0027.jsonl` | built locally under `data/interim/` |
| Schema/taxonomy validation | pass |

No raw content, raw reply text, source URL, raw handle, cookie, token, or session material was added to git.

## Aggregate Before Second Review

| Metric | Result |
|---|---|
| New labels | 4 `uncertain` |
| New risk levels | 4 `medium` |
| Visible signals | 4 `visible_external_link`; 4 `private_channel_redirect`; 4 `contact_handle_visible`; 1 `payment_deposit_or_fee_request`; 1 `vague_offer_strong_benefit` |
| Anti-scam camouflage candidates observed | 2 |

These counts do not mean the 4 new run 0016 records are accepted; they remain pending second review.

## Decision

Status: `continue_to_second_review`.

Do not open item `0028` until items `0024` through `0027` receive second review. The next review must pay special attention to anti-scam camouflage, reply/comment link or contact signals, and CIB's preference to avoid false negatives at the triage stage.
