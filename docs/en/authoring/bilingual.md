---
title: Bilingual Support
description: How the English/Chinese dual-language system works and how to maintain it.
---

# Bilingual Support

The template publishes two complete versions of the site: English at the site root, Chinese under `/zh/`. Both are produced from the same `mkdocs build` by the `i18n` plugin (`mkdocs-static-i18n`).

## How it works

The plugin runs with `docs_structure: folder`, which maps each language folder to its output location:

| Source folder | Built to | URL |
| --- | --- | --- |
| `docs/en/` | `site/` | `https://<you>.github.io/<repo>/` |
| `docs/zh/` | `site/zh/` | `https://<you>.github.io/<repo>/zh/` |

The plugin configuration:

```yaml
plugins:
  - i18n:
      docs_structure: folder
      reconfigure_material: true
      reconfigure_search: true
      languages:
        - locale: en
          default: true
          name: English
          build: true
        - locale: zh
          name: 简体中文
          build: true
          nav_translations:
            Home: 首页
            About: 关于
```

The pieces:

- `docs_structure: folder` — each language lives in its own folder inside `docs/`. The default language (`en`) builds to the site root; other languages build to `/zh/`.
- `default: true` on `en` — the language whose content is used as a fallback (see below).
- `nav_translations` — Chinese titles for the navigation. Every entry in `nav` can be translated here; entries without a translation keep their English title. Section titles (e.g. `Getting Started`) are translated the same way.
- `reconfigure_search: true` — the search index is rebuilt for the Chinese site with the correct language settings.

The language switcher in the header comes from `extra.alternate`:

```yaml
extra:
  alternate:
    - name: English
      link: .
      lang: en
    - name: 简体中文
      link: zh/
      lang: zh
```

The plugin rewrites these links for each language build, so the switcher always points at the matching page in the other language. The build log additionally warns that the `link` values should be absolute paths; this warning can be ignored — relative links are correct for GitHub Pages project sites, which live under `/<repo>/` rather than at the domain root.

## Writing a page in both languages

1. Write `docs/en/<path>.md`.
2. Create `docs/zh/<path>.md` with the same relative path, containing the translation.
3. Add the Chinese title to `nav_translations`.

The build matches files by their path inside the language folder. Relative links inside the content (e.g. `[next](../getting-started/deployment.md)`) are rewritten per language, so both versions navigate within their own language. Files in `docs/assets/` are shared: the same `../assets/images/…` path works from either language.

## If a translation is missing

The build does not fail when a page exists only in English. The Chinese URL serves the English content (the default-language fallback). This is convenient while translations are pending, but the Chinese site then shows English content for that page.

## The Chinese UI language

The template sets `reconfigure_material: true`, so the theme follows each language: the Chinese pages get Chinese interface strings (search placeholder, table-of-contents title, and the like) and an `<html lang="zh">` attribute. Setting it to `false` keeps the interface strings in English while the content remains bilingual.

## Adding a third language

1. Create the folder, e.g. `docs/fr/`, and translate the pages into it.
2. Register the language in the plugin configuration (`locale: fr`, `name: Français`, `build: true`, `nav_translations: …`).
3. Add an `extra.alternate` entry with `link: fr/`.
4. Update `docs/scripts/hooks.py`: the `on_post_build` hook copies `sitemap.xml` into each non-default language folder and currently hardcodes the list `["zh"]`.

## Keeping translations in sync

- Every pull request runs `mkdocs build --strict`; pages that link to files missing in one language fail the check.
- The fallback hides a missing page, so a translation can be added later without breaking the site.
- A useful review habit: after changing the English page, check the corresponding Chinese page in the same pull request.
