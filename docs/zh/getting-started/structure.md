---
title: 结构总览
description: 仓库与 mkdocs.yml 的组织方式，以及双语构建的底层原理。
---

# 结构总览

完整的仓库布局：

```
.
├── .github/workflows/
│   ├── publish_site.yaml      # 推送到 main → 构建站点 → 部署到 gh-pages 分支
│   └── health_check.yaml      # PR 时 → mkdocs build --strict（链接失效即失败）
│
├── docs/                      # ← 所有内容都在这里
│   ├── en/                    # 英文源（默认语言 → 站点根目录）
│   │   ├── index.md           #   首页
│   │   ├── about.md
│   │   └── ...
│   ├── zh/                    # 中文源（→ 站点的 /zh/）
│   │   ├── index.md           #   与 docs/en/ 逐页对应
│   │   └── ...
│   ├── assets/                # 共享静态文件（两种语言共用）
│   │   ├── images/image_demo.png    # 媒体教程的示例图片
│   │   ├── videos/video_demo.mp4    # 媒体教程的示例视频
│   │   ├── favicon.svg              # 浏览器标签页图标
│   │   └── logo.svg                 # 页头 Logo
│   ├── javascripts/
│   │   └── mathjax.js         # MathJax 配置（每个页面都会加载）
│   ├── overrides/
│   │   └── comments.html      # giscus 讨论区模板（见讨论区一节）
│   └── scripts/
│       └── hooks.py           # 构建钩子，例如把 sitemap.xml 复制进 /zh/
│
├── mkdocs.yml                 # ← 核心配置：导航、主题、插件、i18n
├── requirements.txt           # 固定的 Python 依赖（CI 与本地开发共用）
├── CONTRIBUTING.md
├── LICENSE
└── README.md
```

## 两个部分：`docs/` 与 `mkdocs.yml`

- **`docs/`** 存放*内容*——Markdown 文件与素材。
- **`mkdocs.yml`** 存放*其余一切*——站点名称、主题、配色、插件与导航。GitHub Action 运行 `mkdocs build` 时读取该文件，把 `docs/` 转换成 `site/` 里的静态站点。

## `mkdocs.yml` 内部

| 配置段 | 作用 |
| --- | --- |
| `site_name` / `site_url` / `repo_url` | 站点标识、规范 URL、仓库链接 |
| `theme` | Material 主题配置：明暗 **palette**、导航 **features**（标签页、返回顶部、搜索）、Logo/图标，以及指向 `docs/overrides` 的 `custom_dir` |
| `markdown_extensions` | Markdown 方言：表格、公式、emoji、Mermaid 代码块、提示框——即 [Markdown 基础](../authoring/markdown.md) 页演示的全部内容 |
| `extra` | `alternate`——语言切换器条目（English → `.`，简体中文 → `zh/`）；以及全局 JavaScript（MathJax、Mermaid） |
| `plugins` | `search`（全文搜索）、`mkdocs-video`（视频嵌入）、`i18n`（双语构建）、`minify`（压缩 HTML） |
| `nav` | **导航即站点结构。只有列在此处的页面才会被构建。** |

## 双语构建的原理

`i18n` 插件（`mkdocs-static-i18n`）配置为 `docs_structure: folder`：

```
docs/en/**  --（默认语言）-->  site/**      （英文站点）
docs/zh/**  ---------------->  site/zh/**   （中文站点）
```

由此产生两个结论：

1. **`nav` 中的路径是相对语言目录的。** 条目 `Home: index.md` 在英文构建中解析为 `docs/en/index.md`，在中文构建中解析为 `docs/zh/index.md`。导航中从不出现语言前缀。
2. **`docs/assets/` 是共享的。** 两种语言的构建都会引用它；MkDocs 会自动重写相对路径，因此中文页面引用的图片能正确指向共享的 `assets/` 目录。只需写 `../assets/images/…`，在两种语言下都有效。

中文的**导航标题**来自插件配置中的 `nav_translations`；语言切换器来自 `extra.alternate`。详见[双语支持](../authoring/bilingual.md)。

## 补充说明

- **未列入 `nav` 的页面不会被构建。** MkDocs 只渲染导航可达的文件，因此新页面必须在 `mkdocs.yml` 中注册后才会出现；见[新建页面](../authoring/new-pages.md)。
- **`docs/` 中的一切都会复制进站点。** 因此 `docs/scripts/hooks.py` 与 `docs/overrides/` 也会出现在发布的 `site/` 目录中。这无害，但放在 `docs/` 下的私有脚本将会公开。
