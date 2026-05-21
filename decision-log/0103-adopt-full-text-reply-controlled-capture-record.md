# Decision 0103: Adopt Full Text And Reply Controlled Capture Record

## Status

Accepted.

## Date

2026-04-27

## Decision

For confirmed Threads pointers, adopt a required controlled-store full-text/reply capture record before item promotion.

The required artifact is:

```text
RAW/controlled-pilot/item_####_full_thread/<timestamp>/extracted_full_text_review.json
```

This artifact preserves the complete visible top-level post text and complete visible reply/comment text available to the approved browser-rendered/session-aware capture view, or explicitly records why replies/comments were unavailable, hidden, absent-at-capture, partial, or not attempted.

## Rationale

Some scam features appear only in replies/comments, not in the top-level post. Examples include:

- private-message requests;
- LINE, Telegram, WhatsApp, Messenger, IG, FB, or other messaging migration;
- add-friend, contact, assistant, or private-group cues;
- recommendations, stock tips, reporting stock picks, or individualized advice;
- reassurance, guarantee, no-fee, altruistic, or financial-freedom trust softening;
- testimonial proof, profit proof, luxury-result proof, or screenshot proof;
- coordinated replies, double-act endorsement, fake social proof, or contact hijack.

Without a structured full-text/reply artifact, a repo-safe manual record can lose the evidence needed to explain the label and rule family.

## Required Boundaries

- Raw visible post text and raw reply/comment text remain in the controlled store only.
- Tracked repo files must use redacted summaries, feature families, counts, hashes, and capture-status fields.
- `complete_visible` means complete under the approved capture view at capture time; it is not a claim that no hidden, deleted, private, or platform-restricted replies exist.
- Manual entry build is blocked when reply/comment context is likely decisive and reply capture is `not_attempted` or unexplained `partial_visible`.
- This decision does not authorize broad crawler expansion, search-query discovery, private-message access, landing-page capture, redirect-chain capture, profile graph capture, embedding/model training, production detection, or legal fraud determinations.

## Files Updated

- `docs/55-full-text-reply-controlled-capture-record.md`
- `docs/52-confirmed-scam-pointer-intake-method.md`
- `templates/controlled_crawler_run_record.md`
- `governance/pilot-launch/threads_pilot_v1_2026-05_items_0077_0079_full_thread_capture_work_order_0049.md`

## Consequence

Future confirmed-pointer captures should preserve full visible text and reply/comment status in controlled storage first, then reduce the case into redacted repo-safe fields for annotation, validation, rule updates, and checkpoint synthesis.
