# Security

## Reporting a vulnerability

To report a security issue in this template, use the GitHub **Report a vulnerability** flow (Security tab → Advisories) on this repository. DON'T open an issue and make it visible to everyone.

Include a description of the issue, the affected files, and — if possible — a minimal reproduction. Do not include sensitive data in public reports.

## Scope

The template consists of static configuration and content; it contains no server-side code. In scope:

- `mkdocs.yml` and the build configuration
- `docs/scripts/hooks.py` and the templates under `docs/overrides/`
- `.github/workflows/`
- Markdown content that embeds executable JavaScript (e.g. the game demo)

Out of scope: GitHub Pages infrastructure, GitHub Actions runners, and third-party projects (MkDocs, Material for MkDocs, giscus, MathJax, Mermaid, and the plugins listed in `requirements.txt`). Vulnerabilities in those projects should be reported to their maintainers.

## Guidance for adopters

Sites built from this template inherit the following properties:

- The published site is static HTML/CSS/JS and exposes no server-side attack surface.
- Comments are served by a third-party iframe from giscus.app and stored as GitHub Discussions in the configured repository.
- Embedded widgets execute in visitors' browsers. Do not embed secrets, API keys, or other credentials in Markdown pages or in `docs/assets/` — everything under `docs/` is published.
- Python dependencies are pinned in `requirements.txt`. Enabling Dependabot version updates is recommended to receive security fixes.
- The deploy workflow uses the built-in `GITHUB_TOKEN`, scoped to the repository by `permissions: contents: write`. Keep the repository's Actions setting at read/write as documented in the deployment guide.
- The discussion board (giscus) requires a public repository. Do not enable it for private or internal-only workshops.

## Supported versions

Only the latest commit on the `main` branch is supported. There is no backporting or long-term support policy.
