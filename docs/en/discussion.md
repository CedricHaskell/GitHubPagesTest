---
title: Discussion Board
description: How the per-page discussion board works and how to configure giscus for a new repository.
discussions: true
---

# Discussion Board

Each page can carry its own discussion thread. The board is powered by [giscus](https://giscus.app/), which stores comments as GitHub Discussions in the site's repository — participants sign in with their GitHub account, and the host moderates from the repository's Discussions tab.

## How the template wires it up

The template ships `docs/overrides/comments.html`, a Jinja template that renders the giscus widget **only when the page sets `discussions: true` in its frontmatter**:

```yaml
---
discussions: true
---
```

This page carries that flag; the comment thread below is the live demonstration.

For the override to take effect, it must be included by a page template. Create `docs/overrides/main.html` with the following content:

```html
{% extends "base.html" %}

{% block content %}
  {{ super() }}
  {% include "comments.html" %}
{% endblock %}
```

Explanation:

- `custom_dir: docs/overrides` in `mkdocs.yml` makes MkDocs look for templates in `docs/overrides/` first.
- `main.html` extends the theme's `base.html` (which contains the full page skeleton).
- `{{ super() }}` renders the normal page content; the `{% include %}` then appends the comment section after it.

!!! warning "Activation step"
    The template repository provides `comments.html`; if `main.html` is not present in `docs/overrides/`, the comment section is never rendered. Verify both files exist after copying the template.

## Pointing giscus at your repository

`comments.html` ships pre-configured for the template's original repository. For comments to work on a new site, the configuration must be updated:

1. **Make sure the repository is public**, and enable Discussions: **Settings → General → Features → Discussions**.
2. **Install the giscus app**: open [github.com/apps/giscus](https://github.com/apps/giscus) and grant it access to the repository.
3. **Collect the configuration**: open [giscus.app](https://giscus.app), fill in the repository, pick a category (the default `Announcements` category works), and copy the four generated values.
4. **Edit `docs/overrides/comments.html`** and replace the four `data-*` attributes:

```html
data-repo="<you>/<your-repo>"
data-repo-id="R_..."
data-category="Announcements"
data-category-id="DIC_..."
```

| Attribute | Meaning |
| --- | --- |
| `data-repo` / `data-repo-id` | The repository that stores the discussions |
| `data-category` / `data-category-id` | The GitHub Discussions category threads are created in |
| `data-mapping="pathname"` | One thread per page URL |
| `data-strict="1"` | Only the exact URL matches — a page and its query strings do not share a thread |
| `data-reactions-enabled="1"` | Emoji reactions on comments |
| `data-input-position="bottom"` | Comment box below the existing comments |
| `data-theme` | Light/dark widget theme; set dynamically by the page script |
| `data-lang` | Widget interface language (`en`, `zh-CN`, …) |

With `data-mapping="pathname"` and `data-strict="1"`, every page owns one thread, created on first visit. The English page and its Chinese counterpart are separate URLs (`/discussion/` vs `/zh/discussion/`) and therefore get separate threads.

## Theme synchronization

`comments.html` includes a small script that watches the site's color scheme and sends the current theme to the giscus iframe, so the widget follows the light/dark toggle without configuration.

## Notes

- **Comments work only after deployment.** The widget needs the public repository and the real page URL; the local preview (<http://localhost:8000>) does not load comments.
- Moderation happens in the repository's **Discussions** tab, where threads are ordinary discussion posts.
- To disable the board on a page, remove `discussions: true` from its frontmatter.
- Private repositories are not supported by giscus.
