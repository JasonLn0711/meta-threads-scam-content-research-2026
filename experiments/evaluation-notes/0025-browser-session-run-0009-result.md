# Browser-Session Run 0009 Result

## Purpose

Record the repo-safe aggregate result of run 0009, which used the approved browser storage-state/session path to attempt exactly one item 0016 candidate.

This note contains no raw Threads content, item URLs, handles, screenshots, cookies, tokens, browser profiles, HAR files, raw visible text, raw storage paths, credential values, or sensitive investigative material.

## Result

| Check | Result |
|---|---|
| Approved browser storage-state path | used from controlled store |
| Probe seed used | `RP-0009-01` |
| Candidates reviewed | 5 |
| Selected items | 1 |
| `manual_entry_0016.json` created | yes, local-only ignored file |
| `manual_record_0016.json` built | yes, local-only ignored file |
| Strict validation | pass; 1 record, 0 errors, 0 warnings |
| 16-record JSONL validation | pass; 16 records, 0 errors, 0 warnings |
| Raw output in git | no |
| Session/cookie/token in git | no |
| Preliminary label / risk | `uncertain` / `medium` |
| Second-review final label / risk | `non_scam` / `low` |
| Second-review finding | query-keyword false positive; visible retained text negated guaranteed-profit framing |

## Finding

Run 0009 shows that the approved browser-session path can produce at least one extractable, redacted, strict-valid item after the public unauthenticated risk-probe path failed. Second review found that the first-pass `uncertain` / `medium` label was too aggressive because the retained text negated guaranteed-profit framing rather than promoting it. The final item 0016 label is `non_scam` / `low`.

This is useful as a false-positive pressure example: risk-probe candidate generation must exclude negated guarantee/risk-warning language before escalating an item.

## Decision

```text
open_limited_browser_session_extension_0010_with_negation_filter
```

## Required Before Item 17

- Before item 17, update candidate screening to exclude negated guaranteed-profit/risk-warning statements.
- Keep the same approved browser-session limits: one item at a time, at most 5 candidates per selected probe seed, no raw output in git.
- Do not expand to the full 50-item pilot from this result.
