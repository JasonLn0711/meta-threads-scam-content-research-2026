# Data Governance

## Governing Principle

This project studies scam-like content on Threads through lawful, proportionate, and evidence-preserving research methods. Data access constraints are part of the research design.

## Collection Boundary

Do not automate collection from Threads or any Meta surface unless all of the following are true:

1. The collection method is legally approved.
2. Platform access conditions are documented.
3. Stakeholder or institutional authorization is recorded.
4. The approved scope is written in this file or in a linked decision record.
5. The fields collected are limited to what the experiment requires.

Semi-manual collection, stakeholder-provided samples, and documented public examples may be used for early planning if privacy and platform constraints are respected.

## Prohibited Repository Contents

Do not commit:

- Raw personal data
- Credentials, tokens, cookies, session files, or browser profiles
- Screenshots containing unnecessary personal information
- Sensitive investigative material
- Unredacted stakeholder case material
- Automated scraping outputs without recorded authorization

Use `data/README.md` to describe datasets without storing sensitive raw data in git.

## Evidence Handling

Each research item should preserve:

- What was observed
- Where it came from at a non-sensitive level
- Which signals were present
- Who reviewed it
- How confident the reviewer was
- What evidence is missing
- Whether the evidence snapshot is complete, redacted, partial, or unavailable

The project must preserve uncertainty. Labels such as `scam_like`, `uncertain`, and `insufficient_evidence` are research labels, not legal conclusions.

## Privacy Minimization

Prefer derived fields over raw personal content when possible. Store enough evidence to support auditability, but avoid retaining unnecessary personal identifiers.

Examples:

- Store normalized domain category rather than full tracking URL when full URL is not needed.
- Store OCR text relevant to risk signals rather than complete image text when irrelevant personal details appear.
- Store redacted screenshots outside git only when needed for reviewer audit.

## Current Authorization Status

As of repo initialization, there is no recorded approval for automated Threads or Meta collection.

Phase-1 work should assume:

- Manual or semi-manual sample collection only.
- Stakeholder-provided examples only if they can be legally shared.
- No crawler, scraper, browser automation, or bulk collection pipeline.
