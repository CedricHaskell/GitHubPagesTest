---
title: 自定义
description: 主题覆盖、全局 CSS 与 JavaScript、构建钩子、额外插件等扩展点。
---

# 自定义

除页面与配色之外，模板有四个扩展点：主题覆盖、全局 CSS/JavaScript、构建钩子，以及额外的插件或 Markdown 扩展。

## 主题覆盖

`custom_dir: docs/overrides` 让 MkDocs 优先在 `docs/overrides/` 中查找模板，找不到时才回退到主题自带模板。目录中的文件会覆盖同名主题文件。

现成的例子是讨论区：`docs/overrides/main.html` 继承主题并追加评论区（见[讨论区](../discussion.md)）：

```html
{% extends "base.html" %}

{% block content %}
  {{ super() }}
  {% include "comments.html" %}
{% endblock %}
```

该模式适用于任意 block。例如维护公告横幅覆盖 `announce` block：

```html
{% extends "base.html" %}

{% block announce %}
  讲义正在更新，新版本将于周五发布。
{% endblock %}
```

自定义页脚覆盖 `footer` block：

```html
{% extends "base.html" %}

{% block footer %}
  <footer>Workshop 材料 © 2026 —— <a href="mailto:you@example.com">联系</a></footer>
{% endblock %}
```

block 名称见主题安装目录中的 `base.html`（`.venv/lib/python3.12/site-packages/material/templates/`）。

## 全局 CSS 与 JavaScript

- **`extra_css`** 在每个页面加载样式表。把文件放在 `docs/assets/css/`（或 `docs/stylesheets/`）下，并在 `mkdocs.yml` 中登记：

    ```yaml
    extra_css:
      - assets/css/custom.css
    ```

- **`extra_javascript`** 在每个页面加载脚本。模板已用它加载 `javascripts/mathjax.js`（MathJax 配置），自定义组件使用同一机制：

    ```yaml
    extra_javascript:
      - javascripts/mathjax.js
      - assets/js/my-widget.js
    ```

    由于脚本会在每个页面加载，需要使用守卫式初始化，只在组件容器存在的页面上激活：

    ```js
    document.addEventListener("DOMContentLoaded", function () {
      var root = document.getElementById("my-widget");
      if (root) initMyWidget(root);
    });
    ```

    这正是[小游戏 Demo](game-demo.md) 页面中内嵌游戏的生产化形式。

## 构建钩子

`docs/scripts/hooks.py` 通过 `mkdocs.yml` 中的 `hooks:` 注册。模板的钩子在每次构建后运行，把 `sitemap.xml` 复制进中文目录，使搜索引擎也能获得中文 URL：

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

钩子是以 MkDocs 事件命名的普通 Python 函数（`on_page_markdown`、`on_page_content`、`on_post_build` 等）。文件中定义的任何这类函数都会被自动调用。典型用途：对每个页面渲染后的 HTML 做后处理（`on_page_content`），或在构建后生成额外文件。完整事件列表见 [MkDocs 文档](https://www.mkdocs.org/dev-guide/plugins/#events)。

## 更多 Markdown 扩展

`pymdownx.tasklist`（复选框）与 `pymdownx.tabbed`（内容标签页）在模板中已启用，示例见 [Markdown 基础](../authoring/markdown.md) 页。其他扩展的添加方式与此相同。例如 `pymdownx.keys` 渲染键盘按键组合：

```yaml
markdown_extensions:
  - pymdownx.keys
```

```markdown
按 ++ctrl+alt+delete++ 打开任务管理器。
```

这些扩展都来自 `pymdown-extensions`，它已在 `requirements.txt` 中，无需改动依赖。

## 插件

已启用的插件：

| 插件 | 作用 |
| --- | --- |
| `search` | 全文搜索（由 `i18n` 按语言重建） |
| `mkdocs-video` | `![type:video](…)` 视频嵌入（见[图片与视频](../authoring/media.md)） |
| `i18n` | 双语构建 |
| `minify` | 压缩构建出的 HTML |

另外两个插件已安装但未启用，作为备选：

- **`mkdocs-redirects`** —— 页面重命名或移动后，旧 URL 自动跳转到新 URL。
- **`mkdocs-git-revision-date-localized-plugin`** —— 显示每个页面的最后更新时间（对讲义很有用）。

在 `mkdocs.yml` 的 `plugins:` 中加一行即可启用。

## 主题特性

`theme` 下的 `features` 列表开关 Material 的行为。模板启用了：`navigation.tabs`、`navigation.sections`、`navigation.top`、`navigation.tracking`、`search.highlight`、`search.share`、`content.code.copy`。常用补充包括 `navigation.instant`（更快的页面切换）、`navigation.footer`（底部上一页/下一页链接）、`content.code.annotate`（代码块注解）。完整列表见 [Material 文档](https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/)。

## 自定义域名

GitHub Pages 可以托管自定义域名：**Settings → Pages → Custom domain**，随后更新 `mkdocs.yml` 中的 `site_url`。

## 延伸阅读

- [Material for MkDocs 文档](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs 文档](https://www.mkdocs.org/)
- [mkdocs-static-i18n](https://ultrabug.github.io/mkdocs-static-i18n/) —— 双语插件
- [giscus](https://giscus.app/) —— 讨论区
