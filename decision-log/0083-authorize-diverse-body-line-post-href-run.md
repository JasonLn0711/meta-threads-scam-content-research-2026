# Decision 0083: Authorize Diverse Body-Line Post-Href Run

## Status

Accepted.

## Decision

Authorize run `0043` to test a more diverse query matrix using body-line segmentation plus post-href discovery.

The run settings are:

- up to 24 diverse search seeds;
- up to 60 reviewed candidates;
- up to 30 quality-review candidates;
- source: approved browser session;
- no manual entry creation;
- no official checkpoint promotion;
- raw output controlled-store only.

## Context

Run `0042` found that Threads search pages exposed body lines and post-like hrefs, but not `article` elements. The project owner also noted that prior queries were too similar.

The next method should test more diverse query families and the extraction surface selected by run `0042`.

## Consequence

Run `0043` can execute as a candidate-quality method test.

Query terms remain candidate-finding tools only and must not become labels.
