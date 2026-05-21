# Decision 0158: Require Meta Content Library / API Route

## Date

2026-05-21

## Decision

For the CIB/165 Threads scam-content research case, record Meta Content Library / API as the preferred official research data-access route where available.

The official Threads API may be used only as a scoped supplementary route when the controlled launch record explicitly approves the endpoint, permissions, query count, fields, storage, retention, and redaction limits.

This decision does not authorize scraping, unofficial APIs, unbounded browser automation, full-platform monitoring, production enforcement, or legal fraud adjudication.

## Context

Decision 0018 authorized API access and research-required automation for the CIB case under controlled run records. It did not name the preferred official Meta route.

The project owner clarified that this case must use the Meta Content Library / API route. Current Meta documentation distinguishes:

- Meta Content Library UI as a controlled-access research interface for public content across Meta technologies.
- Meta Content Library API as programmatic analysis inside Meta Secure Research Environment or an approved third-party cleanroom.
- Official Threads API as a developer API for Threads integrations, including bounded keyword search when approved.

Meta Content Library documentation lists Threads public-profile posts in the public content dataset, but also notes that Threads content is not available for download while that dataset is in development. The project must therefore record UI/API/download coverage per run and treat gaps as limitations.

A user-provided screenshot of the Meta Transparency Center page, marked updated `2026-04-30`, reinforces the same boundary: the page says both tools provide public content from Facebook, Instagram, and WhatsApp Channels, while the web-based tool also provides access to Threads content. The screenshot's Threads section says Threads data includes posts shared by public profiles with 100 or more followers.

## Options Considered

1. Keep generic API authorization without naming a preferred route.
2. Use the regular Threads API as the primary data route.
3. Use Meta Content Library / API as the preferred official research route, with regular Threads API only as scoped supplement.

## Rationale

Option 3 best matches the CIB case and the repo's governance-first design.

Meta Content Library / API is the more research-oriented route for public-interest analysis. It is also more defensible than scraping or unofficial APIs because it has access review, cleanroom constraints, product terms, and documented public-content scope.

The regular Threads API remains useful for bounded keyword search or own-account/reply/insight workflows, but it should not be treated as a full OSINT or platform-monitoring API.

## Consequences

- `docs/51-meta-content-library-api-access.md` records route facts, field mapping, run-record requirements, and stop conditions.
- `governance/data-governance.md` now narrows CIB API authorization toward official Meta routes.
- Source intake and authorization templates now require the route and access environment to be recorded.
- `governance/source-intake-register.md` and `governance/pilot-authorization-register.md` include the Meta Content Library / API route.
- `docs/23-collection-and-redaction-sop.md`, `docs/29-authorized-pilot-execution-plan.md`, and `docs/34-source-intake-and-sampling-frame.md` route API work through the new record.

## Follow-Up

Before the next real run:

- record whether access is through Content Library UI, Content Library API, or official Threads API keyword search
- confirm whether Threads data is available in the approved environment
- confirm whether download/export is allowed for the chosen surface
- record query fields, date ranges, keywords, limits, raw output path, redaction path, retained count, and excluded count
- keep item-level raw outputs, credentials, screenshots, permalinks, handles, and cleanroom artifacts outside git
