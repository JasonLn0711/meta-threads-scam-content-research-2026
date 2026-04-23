# Redaction Checklist

## Item

- `collection_batch_id`:
- `item_id`:
- Reviewer:
- Date:

## Source And Storage

- Raw evidence stored outside git:
- Raw storage location:
- Authorization status:
- Retention rule known:
- Access limited to approved people:

## Personal Or Sensitive Data Check

Mark each as removed, retained with approval, not present, or not applicable.

| Element | Status | Notes |
|---|---|---|
| Ordinary user handles |  |  |
| Profile photos or faces |  |  |
| Personal names |  |  |
| Phone numbers |  |  |
| Email addresses |  |  |
| Messaging handles |  |  |
| Bank/account/payment details |  |  |
| Credential/login information |  |  |
| Unrelated comments or replies |  |  |
| Tracking parameters in URLs |  |  |
| Browser/session data |  |  |
| Stakeholder investigative notes |  |  |

## Dataset Field Redaction

| Field | Redaction action |
|---|---|
| `post_text` |  |
| `reply_texts` |  |
| `image_paths` |  |
| `ocr_text` |  |
| `external_links` |  |
| `visible_contact_handles` |  |
| `source_url_if_stored` |  |
| `metadata_notes` |  |
| `privacy_redaction_notes` |  |

## Snapshot Status

- `screenshot_snapshot_status`:
- `link_snapshot_status`:

## Final Check

- No raw screenshots committed to git:
- No unnecessary personal data in annotation file:
- Contact handles are redacted or approved:
- Source URLs are blank, redacted, normalized, or approved:
- OCR text was reviewed for unrelated personal data:
- `privacy_redaction_notes` filled:
- Ready for annotation:

## Notes

Use short evidence-handling notes only. Do not add accusations or legal conclusions.
