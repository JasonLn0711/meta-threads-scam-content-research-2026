# Decision 0082: Close Run 0042 And Select Body-Line/Post-Href Method

## Status

Accepted.

## Decision

Close run `0042` and select body-line segmentation plus post-href discovery as the next browser candidate extraction method.

This does not create item `0076`, manual records, or official checkpoint items.

## Context

Run `0041` used an article-based extractor and produced no candidates. Run `0042` diagnosed the rendered search-page structure under the approved browser session.

The diagnostic found 0 `article` elements, but it found candidate body lines and post-like hrefs.

## Consequence

The next browser candidate run must revise extraction to body-line segmentation and post-href discovery.

Do not repeat the run `0041` article-only extraction path with higher caps.

The current official checkpoint remains `threads_pilot_v1_0055`.
