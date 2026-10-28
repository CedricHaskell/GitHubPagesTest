---
title: Introduction
description: What the Workshop Template is, what it provides, and who it is intended for.
---

# Introduction

## Intended audience

The template is intended for **workshop hosts** — instructors who design and run hands-on sessions such as hackathons, tutorials, or training courses. It addresses several recurring needs:

- maintaining a worksheet in a version-controlled, shareable form;
- distributing updated materials to participants without re-sending files;
- providing a discussion space attached to the exercises;
- maintaining English and Chinese versions of the same material.

It converts the worksheet into a static website, following the approach of [MIT's Missing Semester](https://missing.csail.mit.edu/): a single searchable site that contains all materials.

## Included features

| Feature | Description |
| --- | --- |
| Bilingual (EN / 中文) | Two complete versions of every page, switchable from the header. The Chinese site is served under `/zh/` |
| One-push deploy | A push to `main` triggers GitHub Actions, which builds the site and publishes it to GitHub Pages |
| Rich Markdown | Tables, code blocks, admonitions, task lists, content tabs, emoji, LaTeX math, and Mermaid diagrams |
| Material theme | The [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme with light/dark modes, tabs, and search |
| Images and videos | Bundled demo files (`image_demo.png`, `video_demo.mp4`) demonstrate media embedding |
| Discussion board | Per-page comment threads powered by [giscus](https://giscus.app) and GitHub Discussions |
| Interactive widgets | The `md_in_html` extension allows arbitrary HTML/CSS/JS to be embedded — see the [Game Demo](../advanced/game-demo.md) |
| CI health check | Each pull request runs `mkdocs build --strict`, which fails on broken links |

## Prerequisites

The requirements are minimal:

- a **GitHub account** (free);
- basic **Markdown** — familiarity with `# Title` and `**bold**` is sufficient for most of the work. The [Markdown Basics](../authoring/markdown.md) page covers the rest.

Python is not required: all editing can be performed in the GitHub web editor, and Actions builds the site. A local Python environment is needed only for [local preview](deployment.md#local-preview).

## Organization of this documentation

The documentation forms a walkthrough, but each page is self-contained:

1. **Getting Started** — deployment and repository layout (this section)
2. **Authoring** — writing pages: Markdown, colors, media, bilingual content
3. **Discussion Board** — comments for participants
4. **Advanced** — customization: theme overrides, hooks, plugins, embedded widgets

> The site hosting this documentation is built from the template. While reading, the [repository](https://github.com/CedricHaskell/WorkshopTemplate) can be consulted in parallel: every feature described here corresponds to real files in `docs/` and `mkdocs.yml`.

## Next step

[Deploy your own copy →](deployment.md)
