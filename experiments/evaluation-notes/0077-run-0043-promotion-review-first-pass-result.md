# Run 0043 Promotion Review First-Pass Result

## Summary

The first-pass promotion review for the 24 run `0043` quality-review candidates is complete.

Result: no candidate is promotable into `manual_entry_0076` yet.

## Scope

| Field | Value |
|---|---|
| Source run | `0043` |
| Review candidates | 24 |
| Review type | browser-candidate promotion first pass |
| Raw output | controlled store only |
| Manual entries created | 0 |
| Official items promoted | 0 |

## Aggregate Gate Result

| Gate outcome | Count |
|---|---:|
| Candidates reviewed | 24 |
| Promotable candidates | 0 |
| Candidates allowed for `manual_entry_0076` | 0 |
| Paused for source-linkage/full-thread capture | 24 |
| Source-context gate failures | 24 |
| Reply-context gate failures | 24 |
| Evidence-attribution gate failures | 24 |

## Signal Coverage

| Signal family | Count |
|---|---:|
| private-channel migration | 9 |
| investment or authority domain | 8 |
| wallet, deposit, or verification | 7 |
| warning, recovery, or support domain | 7 |
| crypto domain | 6 |

## Interpretation

Run `0043` found useful candidate surface signals, but the method did not tie each candidate line to an item-level source URL and reply context.

The candidates were retained as search body lines with page-level post-href context. Under the dedupe-first/full-thread-ready gate, that is not enough for official promotion.

This result does not mean the candidates are non-scam. It means the current evidence package is not promotion-ready.

## Decision Implication

Do not create `manual_entry_0076` from the first-pass run `0043` packet.

The next useful action is a narrow source-linkage/full-thread capture attempt for a small subset of the 24 candidates. Only candidates that gain item-level source context, reply-context status, evidence attribution, second review, and strict validation can be reconsidered for `manual_entry_0076`.
