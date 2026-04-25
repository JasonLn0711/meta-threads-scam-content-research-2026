# Run 0043 Diverse Body-Line Post-Href Result

## Summary

Run `0043` tested whether a more diverse browser-session query matrix plus body-line segmentation and post-href discovery could produce a better candidate surface than the prior article-only extraction path.

Result: successful method test, no official item creation.

## Scope

| Field | Value |
|---|---|
| Run | `0043` |
| Source | approved browser session |
| Method | body-line segmentation plus post-href discovery |
| Query posture | diverse risk-domain and visible-signal matrix |
| Candidate cap | 60 |
| Quality-review cap | 30 |
| Official item cap | 0 |
| Raw output | controlled store only |
| Manual entries created | 0 |
| Official checkpoint promotion | no |

## Aggregate Result

| Metric | Value |
|---|---:|
| Seeds checked | 10 |
| Candidates reviewed | 60 |
| Dedupe-pass candidates | 51 |
| Exact duplicates | 9 |
| Quality-review selected candidates | 24 |
| Post-href context attempts | 30 |
| Post-href context-ready attempts | 30 |
| Candidate body lines observed | 207 |
| Post-like hrefs observed | 52 |

Stop condition: `candidate_cap_reached`.

## Signal-Family Summary

| Signal family | Count |
|---|---:|
| investment or authority domain | 16 |
| private-channel migration | 12 |
| warning, recovery, or support domain | 8 |
| wallet, deposit, or verification | 7 |
| crypto domain | 6 |
| comment or reward gate | 1 |

The matrix reached its candidate cap after 10 of 24 seeds, which means the more diverse query design was productive enough that continuing the remaining seeds would not improve this capped method test.

## Interpretation

This run confirms that the next browser method should not return to article-only extraction. Body-line segmentation can expose reviewable candidates, and post-like href discovery can produce context-ready attempts.

However, this run does not promote any candidate into the official checkpoint. The output is useful for candidate-quality assessment and future method design only.

Query terms are candidate-finding tools only. They are not labels, final evidence, or scam determinations.

## Decision Implication

The browser path is now technically viable for candidate discovery, but it still needs a separate promotion decision before any candidate can become `manual_entry_0076` or an official checkpoint item.

Recommended next action:

1. run a repo-safe review of the 24 quality-review candidates in controlled store;
2. choose whether any candidate deserves a formal promotion review under the dedupe-first/full-thread-ready gate;
3. if yes, open a new promotion decision record before creating `manual_entry_0076`;
4. if no, keep confirmed-pointer intake as the preferred path for final scam/high-risk rule learning.
