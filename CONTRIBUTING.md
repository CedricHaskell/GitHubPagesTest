# Contributing

The repository is a documentation template, so most contributions are content or configuration changes. All contributions are welcome: bug reports, new teaching pages, translations, and configuration improvements.

## Getting started

1. Open an issue first to describe the change. This avoids work on a design the maintainers would not accept.
2. Fork the repository and create a feature branch from `main`.
3. Set up a local preview:

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate        # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    mkdocs serve
    ```

4. Make the change, then verify the build:

    ```bash
    mkdocs build --strict
    ```

The health check workflow runs the same command on every pull request; broken links or unresolved files fail CI.

## Content conventions

- **Bilingual pages**: every page exists twice — `docs/en/<path>.md` (default language) and `docs/zh/<path>.md` (translation) — with the same relative path. If the Chinese file is missing, the site falls back to the English content; merged changes are expected to include both versions.
- **Navigation**: new pages are registered in `nav` in `mkdocs.yml`, and their Chinese titles are added to `nav_translations` under the `zh` language entry. Pages not listed in `nav` are not built.
- **Assets**: shared files go in `docs/assets/` — images in `docs/assets/images/`, videos in `docs/assets/videos/`. Everything under `docs/` is published, so do not commit private files there.
- **Frontmatter**: each page carries a `title` and a `description`. Pages with a comment thread add `discussions: true`.
- **Style**: the documentation is written in a neutral, official tone. Avoid decorative emoji and casual phrasing.

## Commit messages

Follow the convention used in the repository history:

- `feat:` — new functionality or pages
- `fix:` — bug fixes
- `chore:` — maintenance and configuration
- `deploy:` — site deployments (generated)

## Pull requests

- Target the `main` branch.
- Describe the change and, for content changes, confirm that both language versions were updated.
- Keep the strict build warning-free: the build log should not contain warnings about unresolved links or missing translations.
