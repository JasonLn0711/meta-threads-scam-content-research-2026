# Full Text And Reply Controlled Capture Record

## Purpose

Confirmed Threads scam pointers can hide decisive features in either the top-level post or the reply/comment area. A post may look like ordinary investment sharing while the replies contain private-message requests, LINE or other messaging-app migration, add-friend links, fake endorsement, recommendations, stock tips, reassurance, guarantees, or other funnel cues.

For confirmed-pointer intake, the project should preserve complete visible text in the controlled store before reducing the case into repo-safe redacted fields.

## Core Principle

`complete` means complete for the approved browser-rendered/session-aware capture view at the time of capture. It does not mean the platform has no hidden, deleted, private, rate-limited, or algorithmically withheld replies.

Every confirmed pointer should therefore distinguish:

- complete visible capture under the approved session;
- partial capture because loading, scrolling, platform UI, or time caps prevented full review;
- unavailable or no visible replies/comments at capture time;
- not attempted, which blocks promotion unless separately justified.

## Controlled-Store Artifact

For each confirmed pointer, create a controlled-store artifact next to the raw capture:

```text
RAW/controlled-pilot/item_####_full_thread/<timestamp>/extracted_full_text_review.json
```

This file may contain raw visible post and reply/comment text because it lives outside git. It should not be copied into tracked repo files.

Minimum fields:

```json
{
  "item_id": "threads_pilot_v1_####",
  "capture_timestamp_utc": "YYYY-MM-DDTHH:MM:SSZ",
  "source_status": "CIB/stakeholder/project-owner confirmed pointer",
  "capture_scope": "approved_browser_rendered_session_visible_thread",
  "top_level_post_text": "raw controlled-store text",
  "visible_reply_texts": [
    {
      "order": 1,
      "text": "raw controlled-store reply/comment text",
      "author_role_if_visible": "poster|other|unknown",
      "risk_relevant": true,
      "risk_feature_family": [
        "private_channel_redirect"
      ]
    }
  ],
  "reply_capture_status": "complete_visible|partial_visible|unavailable_or_none_visible|not_attempted",
  "reply_capture_status_note": "short explanation",
  "visible_reply_count": 0,
  "scroll_count": 0,
  "load_more_attempted": "yes|no|not_available",
  "image_text_observed_from_screenshot": [],
  "ocr_status": "not_applicable|captured|manual_visual_summary|unavailable",
  "controlled_artifacts": {
    "raw_capture_json": "raw_capture.json",
    "page_html": "page.html",
    "screenshot": "controlled-store screenshot reference"
  },
  "repo_boundary": "Do not copy raw URLs, handles, raw text, screenshots, HTML, or exact controlled-store paths into git."
}
```

## Repo-Safe Mapping

Tracked repo files should contain only redacted derived fields:

| Controlled-store field | Repo-safe representation |
|---|---|
| Full top-level post text | Redacted summary in `post_text` or short privacy-reviewed excerpt |
| Full reply/comment text | Redacted selected `reply_texts` summaries, not raw full replies |
| Raw handles/contact IDs | Category or redacted value only |
| Raw URLs | Blank, domain category, or redacted reference only |
| Screenshot/image | `image_count`, `screenshot_style`, `screenshot_snapshot_status`, and controlled-store reference only |
| OCR/raw image text | Risk-relevant redacted OCR summary only |
| Reply completeness | `metadata_notes`, `missing_evidence`, and run-record status table |

If replies/comments are unavailable, hidden, not loaded, or absent at capture time, do not write `has_reply=true`. Instead, record the limitation in `metadata_notes` and use `missing_evidence=["reply_context_missing"]` when reply context would materially improve review.

## Required Feature Checks

During second review, inspect both top-level post text and visible replies/comments for:

- private-message requests;
- LINE, Telegram, WhatsApp, Messenger, IG, FB, or other messaging migration;
- add-friend, contact, assistant, or group-join cues;
- external links, disguised links, or link-like text;
- recommendations, stock tips, named-stock guidance, or report-stock-pick behavior;
- reassurance, guarantee, risk-free, no-fee, altruistic, or financial-freedom trust softening;
- testimonial proof, profit proof, luxury-result proof, or screenshot proof;
- coordinated replies, reply impersonation, double-act endorsement, or fake social proof;
- payment, deposit, wallet, account-management, credential, or personal-data requests.

Query terms, topic words, and isolated finance vocabulary remain candidate-finding signals only. Labels must come from the whole collected evidence unit plus approved confirmation context.

## Promotion Gate

A confirmed pointer should not be promoted into `manual_entry_####.json` unless one of these is true:

1. `extracted_full_text_review.json` exists in the controlled store and records top-level text plus reply/comment status.
2. The run record explicitly states why full visible replies/comments were unavailable, hidden, deleted, platform-restricted, or not relevant.
3. A reviewer accepts the limitation and records what feature families can still be learned from the available evidence.

If the reply/comment layer could change the label or rule family but was not captured or not reviewable, keep the item in a pending or partial state until the limitation is resolved or accepted by decision record.
