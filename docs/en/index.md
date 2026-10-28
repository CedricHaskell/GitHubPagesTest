---
title: Workshop Template
description: A MkDocs + Material template that helps SSTIA workshop hosts ship a bilingual workshop website and worksheet in minutes.
---

# Workshop Template

![hero](../assets/images/hero.svg)

**Workshop Template** is a starter kit for hosting workshops, similar in spirit to [MIT Missing Semester](https://missing.csail.mit.edu/). Instead of writing a worksheet in a Google Doc or a slide deck, the host builds a static website where every exercise, video, and discussion lives on a searchable page.

The complete workflow — from an empty repository to a bilingual (English / 简体中文) workshop site deployed on GitHub Pages — takes approximately ten minutes. No server or frontend framework is required; all content is written in Markdown.

## Why publish the worksheet as a website?

- A single link to share — participants always see the latest version; there is no need to redistribute PDFs after each revision.
- Bilingual support out of the box — English and Chinese versions with a language switcher, suited to SSTIA workshops.
- A built-in discussion board — each page can carry its own comment thread, powered by [giscus](https://giscus.app) and GitHub Discussions.
- Rich media — images, videos, mathematical formulas, diagrams, and interactive widgets require no additional tooling.
- Full-text search — participants can locate any topic quickly.

## Quick start

1. Click **Use this template** on [GitHub](https://github.com/CedricHaskell/WorkshopTemplate) to create a repository.
2. Enable **GitHub Pages** and push any commit — GitHub Actions builds and deploys the site automatically.
3. Edit the Markdown files and commit. The site is live at `https://<you>.github.io/<your-repo>/`.

Detailed instructions are provided in [Deploy with GitHub Pages](getting-started/deployment.md).

## Documentation overview

| Topic | Contents |
| --- | --- |
| [Introduction](getting-started/introduction.md) | Purpose of the template and its intended audience |
| [Deploy with GitHub Pages](getting-started/deployment.md) | From zero to a live site in approximately ten minutes |
| [Structure Overview](getting-started/structure.md) | Organization of the repository and `mkdocs.yml` |
| [Add a New Page](authoring/new-pages.md) | Creating pages and registering them in the navigation |
| [Markdown Basics](authoring/markdown.md) | Supported syntax: tables, math, diagrams, admonitions |
| [Theme & Colors](authoring/theme-colors.md) | Color schemes, logo and favicon |
| [Images & Videos](authoring/media.md) | Embedding media, including the bundled demos |
| [Bilingual Support](authoring/bilingual.md) | How the English/Chinese dual-language system works |
| [Discussion Board](discussion.md) | Per-page comments with giscus |
| [Customization](advanced/customization.md) | Theme overrides, build hooks, plugins |
| [Game Demo](advanced/game-demo.md) | Embedding interactive widgets such as mini-games |

## A working demonstration

This site is built entirely from the template, with no additional code. The layout, colors, language switcher, search bar, and embedded demos all come from the files in the [GitHub repository](https://github.com/CedricHaskell/WorkshopTemplate). The [中文版](./zh/) shows the bilingual system in action.

Suggested starting points:

- [Deploy with GitHub Pages](getting-started/deployment.md) — publish a copy of your own
- [Markdown Basics](authoring/markdown.md) — write the worksheet
- [Theme & Colors](authoring/theme-colors.md) — adapt the site's appearance

---

Built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), deployed by GitHub Actions. Comments are provided by [giscus](https://giscus.app/).
