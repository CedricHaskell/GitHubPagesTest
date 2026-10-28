---
title: 主题与配色
description: 如何修改站点的配色方案、Logo 与图标。
---

# 主题与配色

配色在 `mkdocs.yml` 的 `theme.palette` 段中配置。模板自带两套 palette——一套用于浅色模式，一套用于深色模式——由浏览器的颜色偏好自动选择：

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

## 各配置项的含义

| 配置项 | 作用 |
| --- | --- |
| `media` | 激活该 palette 的 CSS 媒体查询。`prefers-color-scheme` 跟随访问者的系统设置；页头按钮可手动切换 |
| `scheme` | 基础配色方案：`default`（浅色）或 `slate`（深色） |
| `primary` | 主品牌色——页头、导航标签页、表头 |
| `accent` | 辅色——链接、悬停状态、焦点轮廓 |
| `toggle` | 页头明暗切换按钮的图标与文字 |

`primary` 与 `accent` 的取值是 Material 颜色名（见下表）。颜色在浅色与深色方案下渲染略有差异，`scheme` 会自动处理。

## 可用颜色

以下 Material 颜色都可以用作 `primary` 和 `accent`：

| | | | |
| --- | --- | --- | --- |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#EF5350;vertical-align:middle"></span> `red` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#E91E63;vertical-align:middle"></span> `pink` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#9C27B0;vertical-align:middle"></span> `purple` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#673AB7;vertical-align:middle"></span> `deep purple` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#3F51B5;vertical-align:middle"></span> `indigo` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#2196F3;vertical-align:middle"></span> `blue` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#03A9F4;vertical-align:middle"></span> `light blue` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#00BCD4;vertical-align:middle"></span> `cyan` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#009688;vertical-align:middle"></span> `teal` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#4CAF50;vertical-align:middle"></span> `green` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#8BC34A;vertical-align:middle"></span> `light green` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#CDDC39;vertical-align:middle"></span> `lime` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FFEB3B;vertical-align:middle"></span> `yellow` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FFC107;vertical-align:middle"></span> `amber` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FF9800;vertical-align:middle"></span> `orange` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#FF5722;vertical-align:middle"></span> `deep orange` |
| <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#795548;vertical-align:middle"></span> `brown` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#9E9E9E;vertical-align:middle"></span> `grey` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#607D8B;vertical-align:middle"></span> `blue grey` | <span style="display:inline-block;width:12px;height:12px;border-radius:3px;background:#000000;vertical-align:middle"></span> `black` / `white` |

## 示例

**两种方案使用不同配色。** 以 teal/light green 为例：

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

**仅深色主题。** 只保留一条，并去掉 `media` 键：

```yaml
palette:
  - scheme: slate
    primary: cyan
    accent: cyan
```

**仅浅色主题。** 同理使用 `scheme: default`。没有第二套 palette 时，页头的明暗切换按钮会消失。

## Logo 与图标

两者都在 `theme` 下配置，文件位于 `docs/assets/`：

```yaml
theme:
  favicon: assets/favicon.svg
  logo: assets/logo.svg
```

用 workshop 自己的品牌文件替换这两个 SVG；保持文件名不变则无需改动配置。Logo 显示在页头，favicon 显示在浏览器标签页。

## Palette 之外

`primary`/`accent` 覆盖不到的颜色（如背景色、组件边框）需要自定义 CSS，通过 `extra_css` 与 `docs/overrides/` 实现；见[自定义](../advanced/customization.md)。
