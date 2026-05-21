# Decision 0092: Promote Run 0045 Hard Negative As Manual Entry 0076

## Status

Accepted.

## Decision

Promote one run `0045` source-linkage-ready candidate into `manual_entry_0076` as a redacted `non_scam` / `low` hard-negative calibration item.

This is not a scam/high-risk expansion. It is a negative case showing that scam-method vocabulary, private-channel vocabulary, and investment-group vocabulary can appear in victim-prevention warning context.

## Context

Run `0043` produced 24 quality-review candidates. The first-pass promotion review found no promotable candidate because source-context, reply-context, and evidence-attribution gates failed.

Run `0045` re-opened a small subset and found 2 source-linkage-ready candidates. Second review determined that the strongest candidate is warning / victim-prevention content, not a conversion offer.

## Review Result

| Field | Value |
|---|---|
| Source run | `0045` |
| Candidate role | hard-negative / calibration |
| Final label | `non_scam` |
| Final risk | `low` |
| Evidence sufficiency | `sufficient` |
| Confidence | `high` |
| Manual entry | `manual_entry_0076` |
| Manual record | `manual_record_0076` |

## Rationale

The candidate describes scam-group mechanics as a warning to readers. The private-channel and investment-group vocabulary appears as cautionary context, not as an author-controlled funnel or replacement investment path.

This improves the dataset because CIB policy prioritizes low false negatives, but the rule system still needs hard negatives to avoid treating every mention of scam methods as scam content.

## Consequences

- Build `manual_entry_0076.json` using redacted fields only.
- Build and strict-validate `manual_record_0076.json`.
- Do not add raw Threads URL, raw handle, raw text, screenshots, browser artifacts, or exact controlled-store paths to git.
- Keep checkpoint 0055 unchanged until a separate checkpoint synthesis decision is made.
