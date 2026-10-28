---
title: Customization
description: Theme overrides, global CSS and JavaScript, build hooks, extra plugins, and other extension points.
---

# Customization

Beyond pages and colors, the template has four extension points: theme overrides, global CSS/JavaScript, build hooks, and additional plugins or Markdown extensions.

## Theme overrides

`custom_dir: docs/overrides` makes MkDocs look for templates in `docs/overrides/` before falling back to the theme's own templates. A file there overrides the theme file of the same name.

The worked example is the discussion board: `docs/overrides/main.html` extends the theme and appends the comments section (see [Discussion Board](../discussion.md)):

```html
{% extends "base.html" %}

{% block content %}
  {{ super() }}
  {% include "comments.html" %}
{% endblock %}
```

The pattern generalizes to any block. A maintenance banner, for example, overrides the `announce` block:

```html
{% extends "base.html" %}

{% block announce %}
  The worksheet is being updated; the new version arrives on Friday.
{% endblock %}
```

A custom footer overrides the `footer` block:

```html
{% extends "base.html" %}

{% block footer %}
  <footer>Workshop materials © 2026 — <a href="mailto:you@example.com">contact</a></footer>
{% endblock %}
```

Block names can be found in the theme's `base.html` inside the installed package (`.venv/lib/python3.12/site-packages/material/templates/`).

## Global CSS and JavaScript

- **`extra_css`** loads a stylesheet on every page. Add the file under `docs/assets/css/` (or `docs/stylesheets/`) and list it in `mkdocs.yml`:

    ```yaml
    extra_css:
      - assets/css/custom.css
    ```

- **`extra_javascript`** loads a script on every page. The template already uses it for `javascripts/mathjax.js` (MathJax configuration), and the same mechanism serves custom widgets:

    ```yaml
    extra_javascript:
      - javascripts/mathjax.js
      - assets/js/my-widget.js
    ```

    Because the script loads on every page, use a guarded initializer that activates only where the widget's container exists:

    ```js
    document.addEventListener("DOMContentLoaded", function () {
      var root = document.getElementById("my-widget");
      if (root) initMyWidget(root);
    });
    ```

    This is the production form of the inline game demonstrated on the [Game Demo](game-demo.md) page.

## Build hooks

`docs/scripts/hooks.py` is registered under `hooks:` in `mkdocs.yml`. The template's hook runs after each build and copies `sitemap.xml` into the Chinese folder, so search engines receive the Chinese URLs as well:

```python
import shutil
from pathlib import Path

def on_post_build(config, **kwargs):
    site_dir = Path(config.site_dir)
    root_sitemap = site_dir / "sitemap.xml"
    if not root_sitemap.exists():
        return

    for lang in ["zh"]:
        lang_dir = site_dir / lang
        if lang_dir.is_dir():
            shutil.copy(root_sitemap, lang_dir / "sitemap.xml")
```

Hooks are plain Python functions named after MkDocs events (`on_page_markdown`, `on_page_content`, `on_post_build`, and others). Any such function defined in the file is picked up automatically. Examples: post-processing the rendered HTML of every page (`on_page_content`), or generating additional files after the build. The full event list is in the [MkDocs documentation](https://www.mkdocs.org/dev-guide/plugins/#events).

## More Markdown extensions

`pymdownx.tasklist` (checkboxes) and `pymdownx.tabbed` (content tabs) are enabled in the template; demos are provided on the [Markdown Basics](../authoring/markdown.md) page. The procedure for adding further extensions is the same for all of them. `pymdownx.keys`, for example, renders keyboard-key combinations:

```yaml
markdown_extensions:
  - pymdownx.keys
```

```markdown
Press ++ctrl+alt+delete++ to open the task manager.
```

These extensions all come from `pymdown-extensions`, which is already in `requirements.txt`, so no dependency change is needed.

## Plugins

The enabled plugins:

| Plugin | Function |
| --- | --- |
| `search` | Full-text search (reconfigured per language by `i18n`) |
| `mkdocs-video` | `![type:video](…)` embeds (see [Images & Videos](../authoring/media.md)) |
| `i18n` | The bilingual build |
| `minify` | Minifies the built HTML |

Two further plugins are installed but not enabled, kept as ready options:

- **`mkdocs-redirects`** — old URLs redirect to new ones after a page is renamed or moved.
- **`mkdocs-git-revision-date-localized-plugin`** — displays the last-updated date of each page (useful for worksheets).

Enabling either is a one-line addition to `plugins:` in `mkdocs.yml`.

## Theme features

The `features` list under `theme` toggles Material behaviors. The template enables: `navigation.tabs`, `navigation.sections`, `navigation.top`, `navigation.tracking`, `search.highlight`, `search.share`, `content.code.copy`. Commonly useful additions include `navigation.instant` (faster page transitions), `navigation.footer` (prev/next links at the bottom), and `content.code.annotate` (annotations in code blocks). The full list is in the [Material documentation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/).

## Custom domain

GitHub Pages can serve a custom domain: **Settings → Pages → Custom domain**, then update `site_url` in `mkdocs.yml` accordingly.

## Further reading

- [Material for MkDocs documentation](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs documentation](https://www.mkdocs.org/)
- [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/) — the bilingual plugin
- [giscus](https://giscus.app/) — the discussion board
