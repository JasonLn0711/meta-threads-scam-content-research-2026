# Decision 0060: Close Option A Run 0038 After Caps

## Status

Accepted.

## Decision

Close Option A run 0038 for further collection.

The run reviewed 20 candidates and selected 10 items, reaching both stakeholder-approved caps for this tranche.

## Context

Stakeholders approved Option A after checkpoint 0042:

- next tranche size: 10 items;
- maximum candidates reviewed: 20;
- maximum selected items: 10;
- primary source path: approved browser-session capture;
- supplemental source path: CIB/stakeholder confirmed pointers if provided;
- fast different-angle second review required;
- strict validation required.

Run 0038 completed within those limits and produced items `0046-0055`.

## Result

Second review produced:

- 0 final `scam` items;
- 1 final `non_scam` item;
- 4 final `uncertain` items;
- 5 final `insufficient_evidence` items.

The 55-record aggregate strict validation passed with 0 errors and 0 warnings.

The baseline smoke run over the 55-record aggregate produced precision `0.708`, recall `1.000`, F1 `0.829`, 7 false positives, and 0 false negatives.

## Rationale

The run proved that approved browser-session capture can produce strict-valid records, but it also showed that candidate search still yields many thin snippets and uncertainty examples.

Because both caps are exhausted, continuing the same run would violate the stakeholder-approved boundary.

## Consequence

Do not add more candidates or selected items to run 0038.

The next research decision should be one of:

- synthesize a 55-record checkpoint before any further browser-session tranche;
- request or wait for CIB/stakeholder confirmed pointers if more final scam/high-risk rule-family examples are needed;
- open a new bounded run only if a later decision records source path, candidate cap, selected-item cap, second-review rule, and strict-validation requirement.
