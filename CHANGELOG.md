# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-10-28

Initial release.

### Added

- MkDocs and Material for MkDocs setup with pinned Python dependencies (`requirements.txt`)
- GitHub Actions automation: build and deployment to GitHub Pages on every push to `main` (`publish_site.yaml`), and a `mkdocs build --strict` health check on pull requests (`health_check.yaml`)
- Bilingual site structure (English / 简体中文) via mkdocs-static-i18n: per-language navigation translations (`nav_translations`), header language switcher, Chinese UI strings, and fallback to the default language for untranslated pages
- Per-page discussion board powered by giscus and GitHub Discussions, enabled by frontmatter and synchronized with the site's light/dark theme
- Media support: image embedding with sizing and captions, video embedding via the mkdocs-video plugin, with bundled demo assets (`image_demo.png`, `video_demo.mp4`)
- Markdown extensions: tables, task lists, content tabs, admonitions, emoji, LaTeX math, Mermaid diagrams, and raw HTML
- Theme configuration: light/dark color palettes, Material color schemes, logo and favicon
- Build hooks: `sitemap.xml` copied into language subdirectories after each build
- Complete bilingual documentation: introduction, deployment, repository structure, page authoring, Markdown reference, theming, media, internationalization, discussion board, and customization
- Embedded Snake game demo illustrating interactive HTML/CSS/JS widgets
- Project files: README, CONTRIBUTING, SECURITY
- MIT license

[Unreleased]: https://github.com/CedricHaskell/WorkshopTemplate/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/CedricHaskell/WorkshopTemplate/releases/tag/v0.1.0
