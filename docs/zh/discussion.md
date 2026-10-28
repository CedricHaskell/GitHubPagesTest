---
title: 讨论区
description: 每页讨论区的运作方式，以及如何为新仓库配置 giscus。
discussions: true
---

# 讨论区

每个页面都可以有自己的讨论线程。讨论区由 [giscus](https://giscus.app/) 提供支持，评论以 GitHub Discussions 的形式存放在站点仓库中——参与者用 GitHub 账号登录发言，主讲人在仓库的 Discussions 标签页中进行管理。

## 模板如何接线

模板附带 `docs/overrides/comments.html`，这是一个 Jinja 模板，仅当页面 frontmatter 中设置 `discussions: true` 时才渲染 giscus 组件：

```yaml
---
discussions: true
---
```

本页就带有该标记；下方的评论线程是现场演示。

要让该覆盖生效，必须由页面模板将其引入。创建 `docs/overrides/main.html`，内容如下：

```html
{% extends "base.html" %}

{% block content %}
  {{ super() }}
  {% include "comments.html" %}
{% endblock %}
```

说明：

- `mkdocs.yml` 中的 `custom_dir: docs/overrides` 让 MkDocs 优先在 `docs/overrides/` 中查找模板。
- `main.html` 继承主题的 `base.html`（其中包含完整的页面骨架）。
- `{{ super() }}` 渲染正常的页面内容；随后的 `{% include %}` 在内容之后追加评论区。

!!! warning "激活步骤"
    模板仓库提供了 `comments.html`；如果 `docs/overrides/` 中没有 `main.html`，评论区不会被渲染。复制模板后请确认两个文件都存在。

## 把 giscus 指向你的仓库

`comments.html` 出厂时配置的是模板的原仓库。要让评论在新站点上工作，必须更新配置：

1. **确认仓库为公开**，并启用 Discussions：**Settings → General → Features → Discussions**。
2. **安装 giscus 应用**：打开 [github.com/apps/giscus](https://github.com/apps/giscus)，授予它访问仓库的权限。
3. **获取配置**：打开 [giscus.app](https://giscus.app)，填写仓库，选择一个分类（默认的 `Announcements` 分类即可），复制生成的四个值。
4. **编辑 `docs/overrides/comments.html`**，替换四个 `data-*` 属性：

```html
data-repo="<you>/<your-repo>"
data-repo-id="R_..."
data-category="Announcements"
data-category-id="DIC_..."
```

| 属性 | 含义 |
| --- | --- |
| `data-repo` / `data-repo-id` | 存放讨论的仓库 |
| `data-category` / `data-category-id` | 创建线程所用的 GitHub Discussions 分类 |
| `data-mapping="pathname"` | 每个页面 URL 一条线程 |
| `data-strict="1"` | 只有完全相同的 URL 才匹配——页面与其查询参数不共享线程 |
| `data-reactions-enabled="1"` | 评论的表情回应 |
| `data-input-position="bottom"` | 评论输入框位于已有评论下方 |
| `data-theme` | 组件的明暗主题；由页面脚本动态设置 |
| `data-lang` | 组件界面语言（`en`、`zh-CN` 等） |

使用 `data-mapping="pathname"` 与 `data-strict="1"` 时，每个页面独占一条线程，首次访问时创建。英文页面与其中文对应页是不同 URL（`/discussion/` 与 `/zh/discussion/`），因此各有一条线程。

## 主题同步

`comments.html` 内置一段小脚本，监听站点的明暗方案并把当前主题发送给 giscus iframe，因此组件会跟随明暗切换，无需配置。

## 注意事项

- **评论只在部署后可用。** 组件需要公开仓库与真实的页面 URL；本地预览（<http://localhost:8000>）不会加载评论。
- 管理在仓库的 **Discussions** 标签页进行，线程就是普通的讨论帖。
- 在页面上禁用讨论区：从 frontmatter 中移除 `discussions: true`。
- giscus 不支持私有仓库。
