# Decision 0090: Authorize Run 0045 Source-Linkage Follow-Up

## Status

Accepted.

## Decision

Authorize run `0045` as a narrow source-linkage and full-thread/reply-status follow-up for run `0043` promotion candidates.

This decision does not authorize automatic creation of `manual_entry_0076`. It authorizes a controlled attempt to determine whether any first-pass candidate can be tied to item-level source context.

## Scope

| Field | Value |
|---|---|
| Run | `0045` |
| Source candidates | run `0043` promotion packet |
| Candidate attempt cap | 5 |
| Source path | approved browser session plus controlled-store packet |
| Goal | source-linkage/full-thread/reply-status check |
| Raw output | controlled store only |
| Manual entry creation | no |
| Official item promotion | no |

## Required Gates

The run may mark a candidate as `source_linkage_ready` only if:

- candidate text is tied to a specific post-href context;
- candidate text is observable in the re-opened controlled browser context;
- evidence attribution is item-level rather than search-page-only;
- reply/comment status is captured or explicitly recorded as unavailable/unstructured;
- no raw evidence is copied into git.

## Consequence

Run `0045` can produce a repo-safe aggregate result and a controlled-store packet. A separate second-review/build decision remains required before `manual_entry_0076`.
