---
title: Theme & Colors
description: How to change the color scheme, logo, and favicon of the site.
---

# Theme & Colors

Colors are configured in the `theme.palette` section of `mkdocs.yml`. The template ships with two palettes — one for light mode, one for dark mode — and the browser's color preference selects between them:

```yaml
theme:
  palette:
    # Palette toggle for light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    # Palette toggle for dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: cyan
      accent: cyan
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
```

## What each setting does

| Setting | Function |
| --- | --- |
| `media` | CSS media query that activates this palette. `prefers-color-scheme` follows the visitor's OS setting; the header button switches manually |
| `scheme` | Base color scheme: `default` (light) or `slate` (dark) |
| `primary` | Main brand color — header, navigation tabs, table headers |
| `accent` | Secondary color — links, hover states, focus outlines |
| `toggle` | Icon and label of the light/dark switch in the header |

The `primary` and `accent` values are Material color names (below). Colors rendered slightly differently in light and dark schemes; the `scheme` handles that automatically.

## Available colors

All Material colors below are valid values for `primary` and `accent`:

| | | | |
| --- | --- | --- | --- |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#EF5350;vertical-align:middle"></span> `red` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#E91E63;vertical-align:middle"></span> `pink` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#9C27B0;vertical-align:middle"></span> `purple` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#673AB7;vertical-align:middle"></span> `deep purple` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#3F51B5;vertical-align:middle"></span> `indigo` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#2196F3;vertical-align:middle"></span> `blue` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#03A9F4;vertical-align:middle"></span> `light blue` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#00BCD4;vertical-align:middle"></span> `cyan` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#009688;vertical-align:middle"></span> `teal` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#4CAF50;vertical-align:middle"></span> `green` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#8BC34A;vertical-align:middle"></span> `light green` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#CDDC39;vertical-align:middle"></span> `lime` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FFEB3B;vertical-align:middle"></span> `yellow` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FFC107;vertical-align:middle"></span> `amber` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FF9800;vertical-align:middle"></span> `orange` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FF5722;vertical-align:middle"></span> `deep orange` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#795548;vertical-align:middle"></span> `brown` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#9E9E9E;vertical-align:middle"></span> `grey` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#607D8B;vertical-align:middle"></span> `blue grey` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#000000;vertical-align:middle"></span> `black` / `white` |

## Examples

**Different colors per scheme.** A teal/light-green identity:

```yaml
palette:
  - media: "(prefers-color-scheme: light)"
    scheme: default
    primary: teal
    accent: light green
    toggle:
      icon: material/brightness-7
      name: Switch to dark mode
  - media: "(prefers-color-scheme: dark)"
    scheme: slate
    primary: teal
    accent: light green
    toggle:
      icon: material/brightness-4
      name: Switch to light mode
```

**Single dark theme.** To serve dark mode only, keep one entry and remove the `media` key:

```yaml
palette:
  - scheme: slate
    primary: cyan
    accent: cyan
```

**Single light theme.** The same with `scheme: default`. Without a second palette, the light/dark switch disappears from the header.

## Logo and favicon

Both are set under `theme` and live in `docs/assets/`:

```yaml
theme:
  favicon: assets/favicon.svg
  logo: assets/logo.svg
```

Replace these two SVG files with the workshop's own branding; keeping the filenames means no configuration change. The logo appears in the header, the favicon in the browser tab.

## Beyond the palette

Colors not covered by `primary`/`accent` (e.g. background tints or component borders) require custom CSS via `extra_css` and `docs/overrides/`; see [Customization](../advanced/customization.md).
