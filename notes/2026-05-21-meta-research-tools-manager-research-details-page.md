# Meta Research Tools Manager Research Details Page Snapshot

- Date recorded: 2026-05-21
- Source: user-provided screenshots of the Meta Research Tools Manager application draft
- Page section: `Research details`
- URL / application identifier: intentionally omitted from git
- Screenshot files: not stored in git
- Repo-safe privacy note: this note records the research-program text and form state only. It does not record the visible application ID, logged-in account identity, access credentials, screenshots, raw Threads evidence, handles, URLs, or item-level controlled artifacts.
- Related official documentation record: [../docs/54-meta-official-product-documentation-requirements.md](../docs/54-meta-official-product-documentation-requirements.md)

## Visible Page State

- Left application stepper state:
  - `Personal information`: completed
  - `Organization`: completed
  - `Research details`: active
  - `Collaborators`: not yet completed in the visible screenshot
  - `Terms and Conditions`: not yet completed in the visible screenshot
- Main panel title: `Research details`
- Main panel helper text: `Tell us about the research you will be doing with access to Meta Content Library.`
- Bottom controls visible: `Back`, `Save`, and `Next`
- In the second screenshot, `Next` appears enabled after the required selections and confirmations are checked.

## Filled Fields

| Field | Observed value / state | Counter / state |
|---|---|---|
| Research program title | `Metadata-Driven Public Scam Pattern Analysis and Reviewer Su` | `60/60` |
| Research program description | Filled; full text recorded below | `1772/4000` |
| Relevant data for your research | Filled; full text recorded below | `1552/4000` |
| EU systemic-risk question | `Yes` selected | Selected |
| Meta Content Library web-based tool | Selected | Checked and greyed in the visible UI |
| Meta Content Library API via secure computing platform | Selected | Checked |
| Secure computing platform | `Meta Secure Research Environment` | Selected |
| Secure computing platform alternative | `SOMAR Virtual Data Enclave` | Not selected |
| Required confirmation: product documentation and fields/API understanding | Checked | Checked |
| Required confirmation: scientific discipline or public-interest social good | Checked | Checked |

## Research Program Title

Observed field value:

```text
Metadata-Driven Public Scam Pattern Analysis and Reviewer Su
```

Field state:

- The title field is at its maximum visible counter: `60/60`.
- The observed title appears to end at `Su`, likely because the form limit was reached before the intended word was complete.
- Before submission, consider shortening the title so it does not look truncated.

Possible shorter title if a later revision is desired:

```text
Metadata-Driven Public Scam Analysis and Reviewer Support
```

## Research Program Description

Observed field value:

```text
This research program focuses on the computational analysis of publicly available social media content related to online scam patterns, misleading financial narratives, and coordinated public-risk behaviors on large-scale social platforms.
The primary objective of the research is to explore how metadata-driven analysis and AI-assisted reviewer workflows can support scalable public-interest safety research while minimizing unnecessary exposure to sensitive or personally identifiable information.
The project investigates how public social media content may exhibit observable behavioral and temporal patterns associated with suspicious or potentially harmful online activities, including investment-related scam narratives, engagement anomalies, repetitive promotional structures, and coordinated dissemination behaviors.
The research does not seek to identify, track, or profile individual users, nor does it attempt to perform automated enforcement or legal attribution. Instead, the project focuses on understanding platform-scale public-risk patterns, reviewer bottlenecks, and governance challenges associated with large-scale public content analysis.
Methodologically, the research emphasizes metadata-first analysis, synthetic benchmarking, human-in-the-loop review workflows, uncertainty-aware prioritization, and governance-aware computational approaches. Publicly available content and aggregate behavioral indicators are used to study how reviewer-assist systems may improve scalability and consistency in public-interest online safety analysis.
The broader goal of the project is to contribute to research on AI-assisted governance, scalable reviewer support systems, and public-interest computational social science methodologies for online risk analysis.
```

Observed counter: `1772/4000`.

## Relevant Data For Your Research

Observed field value:

```text
The research primarily requires access to publicly available Threads and other Meta platform content that includes public posts, engagement metadata, timestamps, public interaction indicators, producer-level public information, and aggregate behavioral signals relevant to large-scale scam-pattern analysis.
Relevant data types include:
* Public post text and associated metadata
* Public engagement indicators such as reactions, shares, and views
* Temporal posting patterns and trend signals
* Public producer/account-level metadata
* Hashtag and topic propagation patterns
* Aggregate interaction structures and dissemination behaviors
The research does not require access to private messages, non-public user data, personally sensitive information, or hidden platform moderation systems.
The requested data access is relevant because the research aims to analyze how public online scam narratives and suspicious promotional behaviors evolve over time, propagate across public social environments, and create reviewer scalability challenges in public-interest safety analysis workflows.
The project also studies how metadata-driven prioritization and reviewer-assist methodologies may improve the efficiency and consistency of human review processes under conditions of limited reviewer capacity and large-scale public content volume.
Only publicly accessible or platform-approved research data will be used, and the research will emphasize aggregate analysis, governance-aware methodologies, and synthetic benchmarking approaches where appropriate.
```

Observed counter: `1552/4000`.

## EU Systemic-Risk Question

Visible question:

```text
Will your research contribute to the detection, identification and understanding of systemic risks in the European Union?
```

Observed selected answer:

```text
Yes
```

Repo interpretation:

- This selection should be treated as an explicit systemic-risk claim, not a harmless form detail.
- If this answer remains `Yes`, the application should be ready to explain how the research contributes to understanding public online scam narratives, coordinated public-risk behaviors, or platform-scale safety workflows relevant to systemic-risk analysis.
- The claim should stay bounded: the project studies public-risk patterns and reviewer-assist governance, not legal attribution or autonomous enforcement.

## Selected Research Tools And Platform

Observed selected tools:

- `Meta Content Library (web-based tool)`
- `Meta Content Library API (via secure computing platform)`

Observed secure computing platform:

- Selected: `Meta Secure Research Environment`
- Not selected: `SOMAR Virtual Data Enclave`

Repo interpretation:

- The application is requesting both the web-based research interface and API access.
- Programmatic API work should be assumed to occur only inside the approved secure computing platform.
- This selection does not authorize local downloads, scraping, browser automation, or local raw-data storage.

## Required Confirmations

Observed checked confirmations:

1. `I confirm that I have read the product documentation for Meta Content Library and/or that I understand the various fields, data types, and API endpoints (if applicable) surfaced through MCL.`
2. `I confirm that the research I propose to conduct with Meta Content Library either contributes to advancing knowledge within a scientific discipline or furthers social good in the public interest.`

Repo interpretation:

- These confirmations should be true at submission time.
- The first confirmation should be backed by the official product-documentation notes already recorded in `docs/51-meta-content-library-api-access.md`.
- The detailed product-documentation requirements snapshot is recorded in `docs/54-meta-official-product-documentation-requirements.md`.
- The second confirmation is supported by the project's public-interest, metadata-first, uncertainty-preserving reviewer-support framing.

## Observed UI Notes

- The word `benchmarking` was underlined by browser spellcheck in both long text fields.
- This appears to be browser spellcheck behavior, not an application validation error.
- No visible validation error is shown in the screenshots.

## Pre-Submission Checks

- Shorten or complete the title so it does not end mid-word.
- Confirm the `Yes` answer to the EU systemic-risk question is intentional and supportable.
- Confirm the API request is necessary for the research program and is not merely a convenience request.
- Confirm Meta Secure Research Environment is the intended secure platform.
- Confirm the product documentation has actually been reviewed before relying on the checked confirmation.
- Keep application IDs, access emails, screenshots, private account details, raw content, handles, URLs, exports, and credentials outside git.

## Governance Reading

This page is consistent with the repo's first-principle stance:

- public-interest research, not app development
- metadata-first analysis, not raw-data maximization
- reviewer support, not autonomous enforcement
- aggregate analysis, not individual accusation
- controlled official access, not scraping
- uncertainty preservation, not final legal or fraud determination
