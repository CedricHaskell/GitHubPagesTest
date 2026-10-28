---
title: 模板介绍
description: 本模板的用途、提供的内容以及适用人群。
---

# 模板介绍

## 适用人群

本模板面向 **workshop 主讲人**——设计并主持动手实践课程（hackathon、教程、培训）的讲师。它解决以下常见需求：

- 以版本可控、便于分享的形式维护讲义；
- 向参与者分发更新后的材料，而无需反复发送文件；
- 为练习提供配套的讨论空间；
- 同时维护同一份材料的英文与中文版本。

模板把讲义转换为静态网站，做法与 [MIT's Missing Semester](https://missing.csail.mit.edu/) 一致：一个可搜索的站点容纳全部材料。

## 包含的功能

| 功能 | 说明 |
| --- | --- |
| 双语（EN / 中文） | 每个页面都有两个完整版本，可从页头切换。中文站点位于 `/zh/` 下 |
| 一键部署 | 推送到 `main` 即触发 GitHub Actions，自动构建并发布到 GitHub Pages |
| 丰富的 Markdown | 表格、代码块、提示框、任务列表、内容标签页、emoji、LaTeX 公式、Mermaid 图表 |
| Material 主题 | 成熟的 [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) 主题，支持明暗模式、标签页与搜索 |
| 图片与视频 | 模板自带的示例文件（`image_demo.png`、`video_demo.mp4`）演示媒体嵌入方法 |
| 讨论区 | 每页一条评论线程，由 [giscus](https://giscus.app) 与 GitHub Discussions 提供支持 |
| 交互式组件 | `md_in_html` 扩展允许嵌入任意 HTML/CSS/JS——见[小游戏 Demo](../advanced/game-demo.md) |
| CI 健康检查 | 每个 pull request 运行 `mkdocs build --strict`，链接失效即构建失败 |

## 前置条件

要求很低：

- 一个 **GitHub 账号**（免费）；
- 基础的 **Markdown**——会写 `# 标题` 和 `**加粗**` 即可完成大部分工作，其余见 [Markdown 基础](../authoring/markdown.md)。

Python 并非必需：所有编辑都可以在 GitHub 网页编辑器中完成，由 Actions 负责构建。只有在需要[本地预览](deployment.md#local-preview)时才要安装 Python 环境。

## 文档结构

文档按顺序组织，但每页都自成一体：

1. **快速上手**——部署与仓库结构（即本节）
2. **内容编写**——撰写页面：Markdown、配色、媒体、双语内容
3. **讨论区**——为参与者配置评论
4. **高级功能**——自定义：主题覆盖、钩子、插件、内嵌组件

> 承载本文档的网站就是由模板构建的。阅读时可以对照[仓库](https://github.com/CedricHaskell/WorkshopTemplate)：文中描述的每个特性都对应 `docs/` 与 `mkdocs.yml` 中的真实文件。

## 下一步

[部署自己的副本 →](deployment.md)
