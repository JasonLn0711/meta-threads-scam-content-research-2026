# Post-Run 0039 Confirmed Pointer Request

## Purpose

Use this request after run `0039` closed without adding new final scam/high-risk examples.

The goal is to request a small number of CIB/stakeholder/project-owner confirmed pointers so the project can continue high-value rule-family learning without repeating broad browser-session candidate search.

This request contains no raw Threads URLs, handles, screenshots, raw post text, raw reply text, contact IDs, stock names, stock codes, price values, credentials, browser/session artifacts, stakeholder case IDs, or sensitive investigative notes.

## Why This Is Needed

Run `0039` tested whether a larger approved browser-session supplement could find new final scam/high-risk examples.

It did not. The result was:

- 50 candidates reviewed;
- 20 local candidate entries created;
- 11 adjudicated `uncertain`;
- 9 duplicate or near-duplicate exclusions;
- 0 new final scam/high-risk examples;
- no new official checkpoint promoted.

The bottleneck is not candidate volume. The bottleneck is item-level evidence quality: source context, reply/comment context, and dedupe quality.

## Requested Source

Please provide one small confirmed-pointer tranche.

| Field | Request |
|---|---|
| Preferred source | CIB/stakeholder/project-owner confirmed pointer |
| Preferred tranche size | 3-5 pointers |
| Maximum tranche size before checkpoint | 5 pointers |
| Item handling | one pointer at a time |
| Raw evidence storage | controlled store only |
| Repo-visible content | redacted fields and aggregate conclusions only |
| Required review | strict validation and fast different-angle second review |

## What To Provide

Provide the exact pointer details only through the approved controlled channel, not in public repo files.

Minimum useful pointer context:

- source pointer sufficient for controlled capture;
- confirmation that the pointer is approved for research intake;
- whether post/reply/comment context is important;
- any known evidence-family reason, if shareable in redacted form;
- any boundary notes, such as do-not-capture fields or retention limits.

## What Not To Provide In Git

Do not place these in git, issues, public docs, or non-controlled notes:

- raw post URLs;
- raw handles or account IDs;
- screenshots with unnecessary personal information;
- raw post or reply text;
- private contact IDs;
- case IDs;
- credentials, cookies, storage state, tokens, or browser exports;
- sensitive investigative notes.

## Intake Method

Each pointer should follow:

1. record the full pointer only in the controlled store;
2. capture the item through the approved browser/session-aware or API/session-aware path;
3. preserve raw evidence in the controlled store;
4. create a redacted local `manual_entry_####.json`;
5. build a schema-valid `manual_record_####.json`;
6. strict-validate one-item and aggregate outputs;
7. complete fast different-angle second review;
8. add a repo-safe evaluation note;
9. update the rule library only if a reusable evidence family is confirmed;
10. update the run index and checkpoint decision state.

## Decision Needed

Please return:

| Field | Response |
|---|---|
| Confirmed-pointer tranche approved? | yes / no |
| Pointer source owner |  |
| Pointer count |  |
| Allowed capture path | browser-session / API-session-aware / other approved path |
| Reply/comment capture allowed? | yes / no / case-by-case |
| Screenshot capture allowed? | yes / no / case-by-case |
| OCR allowed? | yes / no / case-by-case |
| Required redaction notes |  |
| Stop condition |  |
| Decision owner |  |
| Date |  |

## Default Recommendation

Approve a 3-5 pointer tranche and process one pointer at a time.

Do not open another broad browser-session tranche unless the dedupe-first/full-thread-ready gate is explicitly tested on a small bounded run.
