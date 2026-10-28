---
title: Workshop Template
description: 一个基于 MkDocs + Material 的模板，帮助 SSTIA 的主讲人在几分钟内搭建双语 workshop 网站与讲义。
---

# Workshop Template

![hero](../assets/images/hero.svg)

**Workshop Template** 是一个面向 workshop 的网站模板，思路类似 [MIT Missing Semester](https://missing.csail.mit.edu/)：主讲人不再用 Google Doc 或幻灯片编写讲义，而是把讲义构建成一个静态网站，所有练习、视频和讨论都集中在一个可搜索的页面上。

从空仓库到部署在 GitHub Pages 上的双语（English / 简体中文）网站，整个过程大约需要十分钟。无需服务器、无需前端框架，内容全部使用 Markdown 编写。

## 为什么把讲义做成网站？

- 只需分享一个链接——参与者看到的永远是最新版本，不必在每次修改后重新分发 PDF。
- 开箱即用的双语支持——英文与中文两个版本通过语言切换器互通，适合 SSTIA 的 workshop。
- 内置讨论区——每个页面可以有自己的评论线程，由 [giscus](https://giscus.app) 与 GitHub Discussions 提供支持。
- 丰富的媒体形式——图片、视频、数学公式、图表以及交互式组件都不需要额外工具。
- 全文搜索——参与者可以快速定位任何内容。

## 快速开始

1. 在 [GitHub](https://github.com/CedricHaskell/WorkshopTemplate) 上点击 **Use this template** 创建自己的仓库。
2. 启用 **GitHub Pages** 并推送任意一次提交——GitHub Actions 会自动构建并部署网站。
3. 编辑 Markdown 文件并提交，网站即上线于 `https://<you>.github.io/<your-repo>/`。

详细步骤见[部署到 GitHub Pages](getting-started/deployment.md)。

## 文档目录

| 主题 | 内容 |
| --- | --- |
| [模板介绍](getting-started/introduction.md) | 模板的用途与适用人群 |
| [部署到 GitHub Pages](getting-started/deployment.md) | 从零到上线，大约十分钟 |
| [结构总览](getting-started/structure.md) | 仓库与 `mkdocs.yml` 的组织方式 |
| [新建页面](authoring/new-pages.md) | 创建页面并注册到导航 |
| [Markdown 基础](authoring/markdown.md) | 支持的语法：表格、公式、图表、提示框 |
| [主题与配色](authoring/theme-colors.md) | 配色方案、Logo 与图标 |
| [图片与视频](authoring/media.md) | 嵌入媒体，包括模板自带的示例 |
| [双语支持](authoring/bilingual.md) | 中英双语系统的运作方式 |
| [讨论区](discussion.md) | 使用 giscus 为页面添加评论 |
| [自定义](advanced/customization.md) | 主题覆盖、构建钩子、插件 |
| [小游戏 Demo](advanced/game-demo.md) | 在页面中嵌入交互式组件 |

## 一个可运行的示例

本站完全由模板构建，没有任何额外代码。布局、配色、语言切换器、搜索栏以及内嵌的示例组件，全部来自 [GitHub 仓库](https://github.com/CedricHaskell/WorkshopTemplate) 中的文件。<a href="..">English version</a> 展示双语系统的效果。

建议从以下页面开始：

- [部署到 GitHub Pages](getting-started/deployment.md) —— 发布自己的站点
- [Markdown 基础](authoring/markdown.md) —— 编写讲义
- [主题与配色](authoring/theme-colors.md) —— 调整站点外观

---

基于 [MkDocs](https://www.mkdocs.org/) 与 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 构建，由 GitHub Actions 部署，评论功能由 [giscus](https://giscus.app/) 提供。
