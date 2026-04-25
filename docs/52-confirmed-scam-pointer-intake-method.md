# Confirmed Scam Pointer Intake Method

## Purpose

Use this method when the project owner, CIB, or another approved stakeholder supplies a confirmed Threads scam pointer for the research database and rule library.

The goal is to preserve raw evidence in the controlled store, convert only redacted fields into local records, update the rule library when the case reveals a reusable pattern, and keep the repo documentation-first.

## Method

1. Record the full source pointer only in the controlled store.
2. Use the approved browser/session or API/session-aware path to capture the item.
3. Preserve raw browser-rendered text, visible text blocks, HTML, screenshot, hrefs, and capture hashes in the controlled store.
4. Create a local redacted `manual_entry_####.json`.
5. Build `manual_record_####.json`.
6. Append a checkpoint JSONL.
7. Strict-validate the item and aggregate.
8. Complete second review before counting the item.
9. Add or update taxonomy, annotation guidance, reason codes, and baseline rules only when the case shows a reusable evidence family.
10. Add a repo-safe run/evaluation note with hashes, counts, and limitations.

## Boundaries

- Do not commit raw post text, raw replies, screenshots, full item URLs, raw handles, HTML, cookies, storage state, credentials, source case IDs, or private investigative notes.
- Do not infer prevalence from confirmed pointers.
- Do not treat one confirmed scam method as the definition of all scam content.
- Do not access private messages.
- Do not perform broad profile graph review unless a later run record explicitly authorizes it.

## Rule Library Principle

Every confirmed pointer should answer two questions:

- What reusable evidence family did this case teach us?
- What should not be overgeneralized from this case?

If the answer is only "this specific account is bad," do not add a broad rule. If the answer is a repeatable funnel pattern, add a narrowly named signal tag and require convergence or second review.
