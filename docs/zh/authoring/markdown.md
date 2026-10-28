---
title: Markdown 基础
description: 本模板支持的 Markdown 方言，附渲染示例。
---

# Markdown 基础

模板支持标准 Markdown 以及 `mkdocs.yml` 的 `markdown_extensions` 中列出的扩展（表格、任务列表、内容标签页、提示框、emoji、LaTeX 公式、Mermaid 图表与原生 HTML）。本页的每个示例都由站点实际渲染，源代码放在可折叠块中。

## 文本基础

```markdown
# 一级标题
## 二级标题
### 三级标题

**加粗**，*斜体*，***加粗斜体***，~~删除线~~，`行内代码`

- 无序列表项
- 另一项
    - 嵌套项（缩进 4 个空格）

1. 有序列表项
2. 另一项

[内部链接](../getting-started/deployment.md)
[外部链接](https://www.mkdocs.org/)

> 引用块。

---

段落内换行需要  
两个尾随空格。
```

- `#` 到 `######` 生成右侧的目录；悬停在标题上会出现永久链接（`¶` 符号），便于链接到讲义的某一小节。
- 中文标题生成的锚点 ID 会被丢弃全部非 ASCII 字符（例如"第 1 步"的 ID 是 `#1`）。需要稳定、可读的链接时，用属性语法显式指定 ID：`## 部署步骤 {#deploy-steps}`，随后即可用 `[跳转](#deploy-steps)` 引用。
- 内部链接使用相对当前文件的路径，如 `../getting-started/deployment.md`。MkDocs 会在每个页面上、在两种语言中把它转换成正确的 URL。
- 块级元素之间需要空行；段内换行使用两个尾随空格。

## 表格

| 命令 | 作用 |
| --- | --- |
| `mkdocs serve` | 启动实时预览服务器 |
| `mkdocs build` | 构建静态站点到 `site/` |
| `mkdocs build --strict` | 构建并在链接失效时报错 |

```markdown
| 命令 | 作用 |
| --- | --- |
| `mkdocs serve` | 启动实时预览服务器 |
| `mkdocs build` | 构建静态站点到 `site/` |
| `mkdocs build --strict` | 构建并在链接失效时报错 |
```

第二行（`---`）必不可少；列宽自动计算。对齐方式在分隔行中用冒号设置（`:---`、`:---:`、`---:`）。

## 代码块

```python
def greet(name: str) -> str:
    """返回一句问候。"""
    return f"Hello, {name}!"
```

````markdown
```python
def greet(name: str) -> str:
    """返回一句问候。"""
    return f"Hello, {name}!"
```
````

- 带语言标记的围栏代码块会获得语法高亮；右上角的复制按钮由 `content.code.copy` 主题特性提供。
- 要在代码块中展示围栏本身（如上例），外层围栏使用四个反引号。

## 提示框

!!! note "带自定义标题的 note"
    Note 用于补充信息。

!!! tip
    Tip 用于可选的改进建议。

!!! warning
    Warning 描述可能引起问题的操作。

!!! danger "注意"
    Danger 用于标记破坏性操作。

```markdown
!!! note "带自定义标题的 note"
    Note 用于补充信息。

!!! tip
    Tip 用于可选的改进建议。

!!! warning
    Warning 描述可能引起问题的操作。

!!! danger "注意"
    Danger 用于标记破坏性操作。
```

其他可用类型：`info`、`success`、`failure`、`bug`、`example`、`quote`。语法为 `!!! 类型 "可选标题"` 加缩进的正文。

## 可折叠块

??? example "解答——点击展开"
    把解答藏在可折叠块中是讲义中常见的做法。

    ```python
    print("Hello, world!")
    ```

```markdown
??? example "解答——点击展开"
    把解答藏在可折叠块中是讲义中常见的做法。
```

使用 `???+ 类型` 可以让块默认展开。

## 任务列表

- [x] Fork 模板仓库
- [x] 启用 GitHub Pages
- [ ] 编写讲义
- [ ] 发布活动通知

```markdown
- [x] Fork 模板仓库
- [x] 启用 GitHub Pages
- [ ] 编写讲义
```

复选框由 `pymdownx.tasklist` 渲染。它们在浏览器中是只读的——勾选状态来自源文件——适合作为讲义中的阅读清单与进度跟踪。

## 内容标签页

=== "题目"
    创建页面 `docs/en/my-exercise.md`，并注册到 `nav`。

=== "解答"
    !!! tip
        别忘了 `docs/zh/` 中的中文镜像。

```markdown
=== "题目"
    创建页面 `docs/en/my-exercise.md`，并注册到 `nav`。

=== "解答"
    !!! tip
        别忘了 `docs/zh/` 中的中文镜像。
```

每个 `=== "标签"` 开启一个标签页；内容缩进四个空格，可以是任意 Markdown，包括提示框与代码块。内容标签页常用于把解答藏在点击之后。

## Emoji

`pymdownx.emoji` 扩展渲染短代码，如 `:smile:` → :smile:、`:rocket:` → :rocket:，以及 Material 图标集的 `:material/rocket-launch:` 图标。短代码参考见 [material icons 搜索](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)。

## 数学公式

行内公式使用 `\( ... \)`：质能方程是 \(E = mc^2\)。

独立公式使用 `\[ ... \]`：

\[
\int_{-\infty}^{+\infty} e^{-x^2} \, dx = \sqrt{\pi}
\]

```markdown
行内公式使用 `\( ... \)`：质能方程是 \(E = mc^2\)。

独立公式使用 `\[ ... \]`：

\[
\int_{-\infty}^{+\infty} e^{-x^2} \, dx = \sqrt{\pi}
\]
```

公式由 MathJax 渲染（`pymdownx.arithmatex` 扩展生成标记，`docs/javascripts/mathjax.js` 提供配置）。美元符号定界符（`$...$`）默认未启用。

## 图表

```mermaid
flowchart LR
    A[编辑 docs/] --> B[提交并推送]
    B --> C[GitHub Action 构建]
    C --> D[站点更新]
```

````markdown
```mermaid
flowchart LR
    A[编辑 docs/] --> B[提交并推送]
    B --> C[GitHub Action 构建]
    C --> D[站点更新]
```
````

Mermaid 语法见 [mermaid.js.org](https://mermaid.js.org/)；流程图、时序图与甘特图均受支持。

## 原生 HTML

`md_in_html` 扩展会把 HTML 原样传递到页面：

<div style="border: 1px solid var(--md-typeset-table-color); border-radius: 4px; padding: 0.5rem 1rem; display: inline-block;">
这段文字是 Markdown 中的原生 HTML。
</div>

```markdown
<div style="border: 1px solid var(--md-typeset-table-color); border-radius: 4px; padding: 0.5rem 1rem; display: inline-block;">
这段文字是 Markdown 中的原生 HTML。
</div>
```

内嵌组件与游戏正是基于这一机制；完整示例见[小游戏 Demo](../advanced/game-demo.md)。

## Frontmatter

每个页面可以以一段 YAML 开头：

```yaml
---
title: 浏览器标签页标题      # 可选；缺省时使用正文 H1
description: 搜索结果中的摘要
discussions: true             # 开启评论线程（见讨论区）
---
```

## 更多扩展

本模板中已启用大部分常用拓展。其他扩展可以用同样的方式添加——见[自定义](../advanced/customization.md)，其中有完整的步骤演示。
