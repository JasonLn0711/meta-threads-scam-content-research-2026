# Confirmed Scam Pointer Intake Method

## Purpose

Use this method when the project owner, CIB, or another approved stakeholder supplies a confirmed Threads scam pointer for the research database and rule library.

The goal is to preserve raw evidence in the controlled store, convert only redacted fields into local records, update the rule library when the case reveals a reusable pattern, and keep the repo documentation-first.

As of the 42-record checkpoint, this is the highest-yield approved method for adding high-risk scam-like rule families. It should remain bounded: one pointer at a time, controlled capture, redacted record, second review, strict validation, and checkpoint synthesis. It does not authorize broad crawler expansion or prevalence claims.

## Method

1. Record the full source pointer only in the controlled store.
2. Use the approved browser/session or API/session-aware path to capture the item.
3. Preserve raw browser-rendered text, visible text blocks, HTML, screenshot, hrefs, and capture hashes in the controlled store.
4. Create a controlled-store `extracted_full_text_review.json` that records full visible top-level post text and full visible reply/comment text, or explicitly records why reply/comment text was unavailable, hidden, absent-at-capture, or only partially captured. Use [55-full-text-reply-controlled-capture-record.md](55-full-text-reply-controlled-capture-record.md).
5. Create a local redacted `manual_entry_####.json`.
6. Build `manual_record_####.json`.
7. Append a checkpoint JSONL.
8. Strict-validate the item and aggregate.
9. Complete second review before counting the item.
10. Add or update taxonomy, annotation guidance, reason codes, and baseline rules only when the case shows a reusable evidence family.
11. Add a repo-safe run/evaluation note with hashes, counts, reply/comment capture status, and limitations.
12. Update `governance/pilot-launch/run_index.md` or the next checkpoint synthesis when the item crosses a checkpoint boundary.

## Boundaries

- Do not commit raw post text, raw replies, screenshots, full item URLs, raw handles, HTML, cookies, storage state, credentials, source case IDs, or private investigative notes.
- Do not infer prevalence from confirmed pointers.
- Do not treat one confirmed scam method as the definition of all scam content.
- Do not access private messages.
- Do not perform broad profile graph review unless a later run record explicitly authorizes it.

## Full Text And Reply Gate

Because confirmed scam features may appear in the top-level post, the poster's replies, other users' comments, or coordinated reply accounts, every confirmed pointer now needs a full-text/reply capture status before promotion.

Required statuses:

| Capture surface | Required status |
|---|---|
| Full visible top-level post text | captured in controlled store, or capture failure documented |
| Full visible replies/comments | `complete_visible`, `partial_visible`, `unavailable_or_none_visible`, or `not_attempted` |
| Reply/comment limitation | documented in the item run record and evaluation note |
| Repo-safe reduction | only redacted summaries, feature families, counts, hashes, and status fields in git |

`complete_visible` means complete for the approved browser-rendered/session-aware view at capture time. It is not a claim that no hidden, deleted, private, or platform-restricted replies exist.

Manual entry build should be blocked when reply/comment context is likely decisive and the run has `not_attempted` or unexplained `partial_visible` status.

## Rule Library Principle

Every confirmed pointer should answer two questions:

- What reusable evidence family did this case teach us?
- What should not be overgeneralized from this case?

If the answer is only "this specific account is bad," do not add a broad rule. If the answer is a repeatable funnel pattern, add a narrowly named signal tag and require convergence or second review.
