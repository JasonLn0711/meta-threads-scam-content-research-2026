# Repo Series Naming

## Series Pattern

Use this pattern for the Meta scam-risk research repo family:

```text
meta-[scope]-[risk-domain]-[content-surface]-research-[year]
```

## Required Parts

| Part | Meaning | Example |
|---|---|---|
| `meta` | Meta ecosystem research target | `meta` |
| `[scope]` | Platform or narrower surface; omit only for umbrella projects | `threads`, `instagram`, `facebook` |
| `[risk-domain]` | Risk category under study | `scam`, `misinformation`, `abuse` |
| `[content-surface]` | Content or evidence surface | `ad`, `content`, `comment`, `page`, `listing` |
| `research` | Signals that this is a research program, not production tooling | `research` |
| `[year]` | Budgeting and project-year marker | `2026` |

## Current Series Names

| Repo | Role |
|---|---|
| `meta-scam-ad-research-2026` | Existing umbrella or prior all-Meta scam-ad research repo. |
| `meta-threads-scam-content-research-2026` | Threads-first scam-like content research repo. |

## Why This Repo Uses `content`

The Threads project should not use `ad` because phase 1 includes posts, replies, comments, image text, screenshots, visible redirection, and external links. `content` is the more accurate content-surface term.

## Why This Repo Uses `scam`

Use `scam` rather than `fraud` because phase 1 studies scam-like signals and risk triage. `fraud` can imply a legal conclusion that this research project is not authorized to make.

## Why This Repo Avoids `detection`

`detection` is acceptable in research prose, but it is not ideal in the repo name because it may imply a production detector. This repo should emphasize research, evidence design, and review support.

## Recommended Future Names

```text
meta-instagram-scam-content-research-2026
meta-facebook-scam-page-research-2026
meta-marketplace-scam-listing-research-2026
meta-threads-scam-comment-research-2026
```

## Names To Avoid

```text
threads-fraud-content-research
threads-scam-detection-research
meta-threads-fraud-research
meta-scam-detector
meta-ai-scam-platform
```

Avoid these because they miss the series prefix/year, overstate legal certainty, or imply production system scope.
