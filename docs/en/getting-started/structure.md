---
title: Structure Overview
description: Organization of the repository and mkdocs.yml, and how the bilingual build works.
---

# Structure Overview

The complete repository layout:

```
.
├── .github/workflows/
│   ├── publish_site.yaml      # push to main → build site → deploy to the gh-pages branch
│   └── health_check.yaml      # on PR → mkdocs build --strict (fails on broken links)
│
├── docs/                      # ← all content lives here
│   ├── en/                    # English source (the default language → site root)
│   │   ├── index.md           #   the home page
│   │   ├── about.md
│   │   └── ...
│   ├── zh/                    # Chinese source (→ /zh/ on the site)
│   │   ├── index.md           #   mirrors docs/en/ page by page
│   │   └── ...
│   ├── assets/                # shared static files (used by BOTH languages)
│   │   ├── images/image_demo.png    # sample image for the media tutorial
│   │   ├── videos/video_demo.mp4    # sample video for the media tutorial
│   │   ├── favicon.svg              # browser-tab icon
│   │   └── logo.svg                 # header logo
│   ├── javascripts/
│   │   └── mathjax.js         # MathJax configuration (loaded on every page)
│   ├── overrides/
│   │   └── comments.html      # giscus discussion board template (see Discussion Board)
│   └── scripts/
│       └── hooks.py           # build hooks, e.g. copying sitemap.xml into /zh/
│
├── mkdocs.yml                 # ← the central configuration: nav, theme, plugins, i18n
├── requirements.txt           # pinned Python dependencies (used by CI and local development)
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## The two halves: `docs/` and `mkdocs.yml`

- **`docs/`** contains *content* — Markdown files and assets.
- **`mkdocs.yml`** contains *everything else* — site name, theme, colors, plugins, and navigation. When the GitHub Action runs `mkdocs build`, it reads this file and converts `docs/` into the static site in `site/`.

## Inside `mkdocs.yml`

| Section | Function |
| --- | --- |
| `site_name` / `site_url` / `repo_url` | Site identity, canonical URLs, repository link |
| `theme` | Material theme configuration: light/dark **palette**, navigation **features** (tabs, top button, search), logo/favicon, and `custom_dir` pointing at `docs/overrides` |
| `markdown_extensions` | The Markdown dialect: tables, math, emoji, Mermaid fences, admonitions — everything demonstrated on the [Markdown Basics](../authoring/markdown.md) page |
| `extra` | `alternate` — the language switcher entries (English → `.`, 简体中文 → `zh/`); plus global JavaScript (MathJax, Mermaid) |
| `plugins` | `search` (full-text), `mkdocs-video` (video embeds), `i18n` (bilingual build), `minify` (smaller HTML) |
| `nav` | **The navigation, which defines the site structure. Only pages listed here are built.** |

## How the bilingual build works

The `i18n` plugin (`mkdocs-static-i18n`) is configured with `docs_structure: folder`:

```
docs/en/**  --(default language)-->  site/**      (the English site)
docs/zh/**  ---------------------->  site/zh/**   (the Chinese site)
```

Two consequences follow:

1. **`nav` paths are language-relative.** The entry `Home: index.md` resolves to `docs/en/index.md` in the English build and to `docs/zh/index.md` in the Chinese build. Languages never appear in the navigation.
2. **`docs/assets/` is shared.** Both language builds reference it; MkDocs rewrites relative paths automatically, so an image referenced from a Chinese page correctly points up to the shared `assets/` folder. Writing `../assets/images/…` works from either language.

The Chinese **navigation titles** come from `nav_translations` in the plugin configuration; the language switcher comes from `extra.alternate`. Details are provided in [Bilingual Support](../authoring/bilingual.md).

## Additional notes

- **Pages not listed in `nav` are not built.** MkDocs renders only files reachable from the navigation, so a new page appears only after registration in `mkdocs.yml`; see [Add a New Page](../authoring/new-pages.md).
- **Everything in `docs/` is copied into the site.** This is why `docs/scripts/hooks.py` and `docs/overrides/` also end up in the published `site/` folder. It is harmless, but any private script placed in `docs/` will be public.
