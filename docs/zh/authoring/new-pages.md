---
title: 新建页面
description: 如何创建新页面、注册到导航，并提供中文版本。
---

# 新建页面

添加页面分三步：创建 Markdown 文件、在 `nav` 中注册、提供中文版本。以下逐一说明。

## 第 1 步——创建 Markdown 文件

在英文目录中创建文件，例如 `docs/en/authoring/example.md`。文件路径决定 URL：`docs/en/authoring/example.md` 对应 `https://<you>.github.io/<your-repo>/authoring/example/`。

文件可以在 GitHub 网页编辑器中创建（**Add file → Create new file**），也可以在本地创建。目录名使用小写与连字符，例如 `getting-started/`。

每个页面以可选的 frontmatter 开头：

```yaml
---
title: Example Page        # 浏览器标签页标题；与正文 H1 无关
description: 一句话摘要，显示在搜索结果中
discussions: true          # 可选：开启评论线程（见讨论区）
---

# Example Page

正文从这里开始。
```

frontmatter 中的 `title` 只是元数据；可见的标题是正文里的 `#` 行。

## 第 2 步——把页面注册到 `nav`

MkDocs 只构建 `mkdocs.yml` 的 `nav` 中列出的页面。把新页面加入对应小节：

```yaml
nav:
  - Home: index.md
  - Getting Started:
      - Introduction: getting-started/introduction.md
      - Deploy with GitHub Pages: getting-started/deployment.md
  - Authoring:
      - Add a New Page: authoring/new-pages.md
      - Example Page: authoring/example.md      # ← 新条目
  - Discussion Board: discussion.md
```

语法说明：

- `- 标题: 路径` 添加一个页面；标题显示在侧边栏与标签页中。
- 在纯键（如 `- Getting Started:`）下缩进的条目构成一个小节及其子页面。
- 路径相对于语言目录——`authoring/example.md` 在英文构建中表示 `docs/en/authoring/example.md`，在中文构建中表示 `docs/zh/authoring/example.md`。语言前缀从不写入 `nav`。
- 页面顺序任意；`nav` 的顺序决定侧边栏与上一页/下一页导航。

要让中文导航显示翻译后的标题，把它加入 `i18n` 插件配置中的 `nav_translations`：

```yaml
plugins:
  - i18n:
      languages:
        - locale: zh
          nav_translations:
            Example Page: 示例页面
```

## 第 3 步——创建中文版本

以相同的相对路径创建 `docs/zh/authoring/example.md`，内容为翻译稿。双语系统按路径匹配文件，因此两个文件在各自语言目录内的位置必须一致。

如果中文文件缺失，构建不会失败：中文 URL 会回退到英文内容。翻译未完成时这一回退很方便，但该页面在中文站点的导航、内容与搜索结果中会显示英文。详见[双语支持](bilingual.md)。

## 验证

提交修改。下一次构建（或 `mkdocs serve` 刷新）后：

- 页面出现在导航与上一页/下一页链接中；
- `/authoring/example/` 提供英文版本；
- `/zh/authoring/example/` 提供中文版本；
- 语言切换器可以在两者之间切换。

## 小结

| 步骤 | 操作 |
| --- | --- |
| 1 | 创建 `docs/en/<path>.md` |
| 2 | 在 `mkdocs.yml` 的 `nav` 中添加 `- 标题: <path>.md`；把中文标题加入 `nav_translations` |
| 3 | 创建 `docs/zh/<path>.md`，内容为翻译稿 |
