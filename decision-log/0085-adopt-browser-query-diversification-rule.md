# Decision 0085: Adopt Browser Query Diversification Rule

## Status

Accepted.

## Decision

Adopt [../docs/54-browser-query-diversification-rule.md](../docs/54-browser-query-diversification-rule.md) as a required acquisition rule for future approved browser-session or API/session-aware candidate-discovery runs that use search queries.

## Context

Prior runs used search terms that were often too similar or topic-heavy. Run `0043` tested a more flexible matrix across risk domains, visible signal families, and wording styles. It reached the 60-candidate cap after 10 seeds, with 51 dedupe-pass candidates and 24 quality-review candidates, while creating no official items.

This showed that query diversification is useful for candidate discovery. It did not turn query terms into evidence.

## Rationale

The project needs two separate rules:

- acquisition rules for finding candidates;
- label rules for deciding what the evidence means.

Query diversification belongs in acquisition governance. It helps avoid narrow search bias and repeated low-yield runs, but it must not contaminate scam labels or baseline scoring.

## Consequences

- Future browser run records must define a query matrix before execution.
- The matrix must vary risk domain, visible signal family, and wording style.
- Query terms remain candidate-finding tools only.
- Reusing the same seed set requires an explicit reason.
- A browser candidate still needs dedupe-first/full-thread-ready promotion review before it can become an official selected item.
