# Collection Field Normalization

## Purpose

This document defines how the manual collection assistant normalizes visible fields before a record reaches annotation.

The goal is privacy-minimized consistency, not maximum data retention.

## Principle

Store the least sensitive representation that still supports review.

Examples:

- domain-only external links instead of full tracking URLs
- redacted contact-handle categories instead of raw handles
- selected relevant replies instead of complete comment threads
- risk-relevant OCR excerpts instead of all screenshot text
- screenshot status instead of raw screenshots in git

## Normalized Fields

| Field | Normalization |
|---|---|
| `external_links` | Defaults to domain-only visible links. |
| `visible_contact_handles` | Defaults to redacted categories such as `telegram:[redacted]`. |
| `visible_platform_redirects` | Maps visible text to schema categories such as `telegram`, `line`, `whatsapp`, `external_site`, or `none`. |
| `has_external_link` | Derived from normalized `external_links`. |
| `has_reply` | Derived from non-empty `reply_texts`. |
| `has_image` | Derived from `image_count` or `image_paths`. |
| `screenshot_snapshot_status` | Defaults to `not_applicable`, `not_captured`, or `captured_redacted` depending on image evidence. |
| `link_snapshot_status` | Defaults to `not_applicable` or `not_captured`; no destination capture is performed. |
| `missing_evidence` | Adds missing post text, OCR, or link snapshot indicators when appropriate. |
| `dedupe_key` | Derived hash from redacted local fields when enabled. |

## What Is Not Normalized

The assistant does not decide whether an item is a scam.

By default, collection-stage records remain conservative:

- `scam_label: uncertain`
- `risk_level: low`
- `scam_type: [none]`
- `signal_tags: [none]`
- `review_status: new`

Annotators and reviewers should update labels later under the annotation guideline.

## Visible Link Handling

The assistant may parse links visible in manually supplied text, but it does not visit them.

Allowed:

```text
example.com
t.me
wa.me
```

Not allowed by default:

```text
https://example.com/path?tracking=value
full redirect chains
landing-page text
browser capture artifacts
```

If a full URL is necessary, it must be explicitly approved in the controlled launch record and the config must be revised with a governance decision.

## Contact Handle Handling

The assistant prefers category-level redaction:

```text
telegram:[redacted]
line:[redacted]
whatsapp:[redacted]
email:[redacted]
phone:[redacted]
other:[redacted]
```

Do not store raw ordinary handles, phone numbers, emails, referral codes, or payment details in repo-visible files.

## OCR Handling

OCR text must already be manually supplied from an approved local or stakeholder-provided image.

The assistant does not perform OCR. It only carries the supplied OCR text into the schema and flags likely missing OCR when an image exists but `ocr_text` is blank.

## Collection Log Mapping

The assistant can append a local collection-log row with:

- item ID
- source type
- collection method
- authorization status
- image count
- screenshot and link status
- whether text, replies, links, handles, and OCR were present
- whether redaction appears required or complete
- whether the item is ready for annotation

The collection log is a local working file and should remain under ignored `data/interim/` for real pilot work.

## Audit Boundary

Normalization supports auditability, but it does not replace human governance.

If the controlled launch record denies a field, do not enter that field into the assistant. If a collector is unsure whether a field is allowed, pause and ask the project owner or governance reviewer.
