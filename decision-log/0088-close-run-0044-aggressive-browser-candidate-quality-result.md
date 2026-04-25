# Decision 0088: Close Run 0044 Aggressive Browser Candidate Quality Result

## Status

Accepted.

## Decision

Close run `0044` as a successful controlled-store-only candidate-quality test.

No manual entries, manual records, or official checkpoint items were created.

## Result

Run `0044` produced:

- 26 seeds checked;
- 200 candidates reviewed;
- 190 candidates passing dedupe;
- 10 exact duplicates;
- 180 local selected candidates;
- 131 post-href context attempts;
- 131 context-ready attempts;
- 0 manual entries;
- 0 official checkpoint items.

## Rationale

The run achieved the user-approved aggressive candidate-quality goal and preserved the boundary between candidate discovery and official labeling.

Negative and non-scam candidates are valid controlled local traces for calibration, but they are not automatically official dataset records.

## Consequences

- Run `0044` is closed for execution.
- Raw candidate evidence remains in the controlled store.
- Repo-visible conclusions remain aggregate and repo-safe.
- Any future official item from this candidate bank requires a separate promotion decision, per-candidate gate review, second review, and strict validation.
