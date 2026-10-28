---
title: Add a New Page
description: How to create a new page, register it in the navigation, and provide its Chinese version.
---

# Add a New Page

Adding a page involves three steps: create the Markdown file, register it in `nav`, and provide the Chinese mirror. Each step is described below.

## Step 1 — Create the Markdown file

Create the file in the English folder, e.g. `docs/en/authoring/example.md`. The path determines the URL: `docs/en/authoring/example.md` becomes `https://<you>.github.io/<your-repo>/authoring/example/`.

Files can be created in the GitHub web editor (**Add file → Create new file**) or locally. Folder names use lowercase and hyphens, e.g. `getting-started/`.

Every page starts with optional frontmatter:

```yaml
---
title: Example Page        # used for the browser tab; independent of the H1
description: A one-sentence summary shown in search results
discussions: true          # optional: enable the comment thread (see Discussion Board)
---

# Example Page

Page content starts here.
```

The `title` in frontmatter is metadata only; the visible heading is the `#` line in the body.

## Step 2 — Register the page in `nav`

MkDocs builds only pages listed in `nav` in `mkdocs.yml`. Add the page to the appropriate section:

```yaml
nav:
  - Home: index.md
  - Getting Started:
      - Introduction: getting-started/introduction.md
      - Deploy with GitHub Pages: getting-started/deployment.md
  - Authoring:
      - Add a New Page: authoring/new-pages.md
      - Example Page: authoring/example.md      # ← new entry
  - Discussion Board: discussion.md
```

Notes on this syntax:

- `- Title: path` adds a page; the title appears in the sidebar and tabs.
- Indented entries under a bare key (`- Getting Started:`) form a section with subpages.
- The path is relative to the language folder — `authoring/example.md` means `docs/en/authoring/example.md` in the English build and `docs/zh/authoring/example.md` in the Chinese build. The language prefix is never written in `nav`.
- Pages can appear in any order; the `nav` order defines the sidebar and prev/next navigation.

For the Chinese navigation to show a translated title, add it to `nav_translations` in the `i18n` plugin configuration:

```yaml
plugins:
  - i18n:
      languages:
        - locale: zh
          nav_translations:
            Example Page: 示例页面
```

## Step 3 — Create the Chinese version

Create `docs/zh/authoring/example.md` with the same relative path, containing the translated content. The bilingual system matches files by path, so the two files must share their location inside their language folders.

If the Chinese file is missing, the build does not fail: the Chinese URL serves the English content instead. This fallback is convenient while a translation is in progress, but the nav item, content, and search results then appear in English on the Chinese site. Details: [Bilingual Support](bilingual.md).

## Verification

Commit the changes. On the next build (or after `mkdocs serve` reloads):

- the page appears in the navigation and the previous/next links;
- `/authoring/example/` serves the English version;
- `/zh/authoring/example/` serves the Chinese version;
- the language switcher swaps between them.

## Summary

| Step | Action |
| --- | --- |
| 1 | Create `docs/en/<path>.md` |
| 2 | Add `- Title: <path>.md` to `nav` in `mkdocs.yml`; add the Chinese title to `nav_translations` |
| 3 | Create `docs/zh/<path>.md` with translated content |
