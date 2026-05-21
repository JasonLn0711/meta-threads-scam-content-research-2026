# Run 0015 Execution Result

This is the repo-safe execution result for `CRAWL-THREADS-PILOT-V1-0015`.

Do not add raw Threads content, screenshots, full URLs, handles, cookies, browser storage state, API responses, candidate HTML, or sensitive investigative notes to this file. Raw/session/candidate artifacts remain in the approved controlled store.

## Summary

| Field | Result |
|---|---|
| Date | `2026-04-25` |
| Execution path | approved browser/session path |
| API path | not used; still blocked until `META_API_PROBE_URL` is approved and ready |
| Candidate cap | 20 total |
| Candidates reviewed | 20 |
| Selected item cap | 10 total |
| Selected local items | 6 |
| New local item range | `threads_pilot_v1_0018` through `threads_pilot_v1_0023` |
| Raw output | controlled store only |
| Strict validation | pass; 23 checked, 0 errors, 0 warnings |
| Second review | pending |

The first risk-probe seed exhausted the 20-candidate cap, so later seeds were not sampled in this execution. The seed was used only to locate candidates; it was not used as a label.

## Local Build Result

| Artifact | Result |
|---|---|
| `manual_entry_0018.json` through `manual_entry_0023.json` | created locally under `data/interim/` |
| `manual_record_0018.json` through `manual_record_0023.json` | built locally under `data/interim/` |
| `manual_records_checkpoint_0023.jsonl` | built locally under `data/interim/` |
| Schema/taxonomy normalization | completed using existing allowed enum values |

No raw content or session material was added to git.

## Aggregate Before Second Review

| Metric | Result |
|---|---|
| New labels | 6 `uncertain` |
| New risk levels | 1 `low`, 5 `medium` |
| Visible signals | 6 `visible_external_link`; 3 `contact_handle_visible`; 3 `private_channel_redirect`; 2 `guaranteed_or_risk_free_claim`; 2 `unrealistic_profit_or_benefit` |

The checkpoint aggregate now contains 23 strict-valid records: 22 non-excluded records and 1 excluded trace record. These counts do not mean the 6 new run 0015 records are accepted; they remain pending second review.

## Decision

Status: `continue_to_second_review`.

Do not open more expansion candidates until items `0018` through `0023` receive second review. After second review, update the aggregate accepted/evaluable counts and decide whether the remaining run 0015 capacity should be used.
