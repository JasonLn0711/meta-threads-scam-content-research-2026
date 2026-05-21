# Decision 0024: Record First-Principle Meta Research Tools Application Strategy

- Date: 2026-05-21
- Status: accepted

## Decision

Adopt a first-principle application strategy for Meta Research Tools Manager:

> The scarce resource is trust, not data volume or model power.

The Research Tools Manager application should be framed as public-interest, metadata-first, governance-aware reviewer-support research, not as app development, platform policing, scraping, or autonomous scam detection.

## Context

The project now has a documented official access route through Meta Content Library / API and a repo-safe transcript of the Research Tools Manager application workflow.

The screenshot and notes clarify that this route is not a normal developer API setup. It is a controlled research access application reviewed through CASD. The application must therefore demonstrate credible research purpose, institutional accountability, data governance, privacy awareness, and misuse prevention.

## Options Considered

1. Treat Research Tools Manager as an API setup task.
2. Treat it as a broad data request for scam detection.
3. Treat it as a governed public-interest research access application.

## Rationale

Option 3 best matches the repo's hard boundaries and the project's actual contribution.

The strongest claim is not that the project has a powerful model. The strongest claim is that it can study public scam-like narratives and reduce reviewer burden while preserving uncertainty, minimizing over-enforcement risk, and avoiding raw evidence exposure in git.

## Consequences

- Application preparation should use `templates/meta_research_tools_application_prep.md`.
- The canonical strategy note is `docs/53-first-principle-meta-research-tools-application-strategy.md`.
- Data authorization requests should explain why official research access is safer and more reproducible than scraping or generic API use.
- Future model notes, including Breeze Guard 26, remain secondary to the governance and reviewer-support research design.
- The project should not claim full-platform monitoring, legal fraud determination, autonomous enforcement, or account-level accusation.

## Follow-Up

Before submitting through Research Tools Manager, complete the application prep template outside git if it contains sensitive collaborator, institutional, ethics, or access details.
