---
title: 双语支持
description: 中英双语系统的运作方式与维护方法。
---

# 双语支持

模板发布站点的两个完整版本：英文位于站点根目录，中文位于 `/zh/` 下。两者由同一次 `mkdocs build` 通过 `i18n` 插件（`mkdocs-static-i18n`）生成。

## 工作原理

插件以 `docs_structure: folder` 模式运行，把每个语言目录映射到对应的输出位置：

| 源目录 | 构建到 | URL |
| --- | --- | --- |
| `docs/en/` | `site/` | `https://<you>.github.io/<repo>/` |
| `docs/zh/` | `site/zh/` | `https://<you>.github.io/<repo>/zh/` |

插件配置：

```yaml
plugins:
  - i18n:
      docs_structure: folder
      reconfigure_material: true
      reconfigure_search: true
      languages:
        - locale: en
          default: true
          name: English
          build: true
        - locale: zh
          name: 简体中文
          build: true
          nav_translations:
            Home: 首页
            About: 关于
```

各项说明：

- `docs_structure: folder` —— 每种语言在 `docs/` 中拥有自己的目录。默认语言（`en`）构建到站点根目录；其他语言构建到 `/zh/`。
- `en` 上的 `default: true` —— 该语言的内容用作回退源（见下文）。
- `nav_translations` —— 导航的中文标题。`nav` 中的每个条目都可以在此翻译；未翻译的条目保留英文标题。小节标题（如 `Getting Started`）的翻译方式相同。
- `reconfigure_search: true` —— 中文站点的搜索索引会按正确的语言设置重建。

页头的语言切换器来自 `extra.alternate`：

```yaml
extra:
  alternate:
    - name: English
      link: .
      lang: en
    - name: 简体中文
      link: zh/
      lang: zh
```

插件会为每种语言的构建重写这些链接，因此切换器始终指向另一语言中的对应页面。构建日志还会警告 `link` 值应为绝对路径；这一警告可以忽略——GitHub Pages 项目站点位于 `/<repo>/` 下而非域名根，相对链接才是正确的。

## 用两种语言写页面

1. 编写 `docs/en/<path>.md`。
2. 以相同的相对路径创建 `docs/zh/<path>.md`，内容为翻译稿。
3. 把中文标题加入 `nav_translations`。

构建按文件在语言目录内的路径进行匹配。内容中的相对链接（如 `[下一页](../getting-started/deployment.md)`）会按语言重写，两个版本都在各自语言内导航。`docs/assets/` 中的文件是共享的：同一条 `../assets/images/…` 路径在两种语言下都有效。

## 翻译缺失时的行为

页面只有英文版本时，构建不会失败。中文 URL 会回退到英文内容（默认语言回退）。翻译未完成时这一行为很方便，但该页面在中文站点会显示英文内容。

## 中文界面语言

模板设置了 `reconfigure_material: true`，主题会跟随各语言：中文页面获得中文界面文字（搜索框提示、目录标题等），以及 `<html lang="zh">` 属性。把它改为 `false` 则界面文字保持英文，内容仍为双语。

## 添加第三种语言

1. 创建目录，如 `docs/fr/`，并翻译页面。
2. 在插件配置中注册该语言（`locale: fr`、`name: Français`、`build: true`、`nav_translations: …`）。
3. 添加 `extra.alternate` 条目，`link: fr/`。
4. 更新 `docs/scripts/hooks.py`：`on_post_build` 钩子会把 `sitemap.xml` 复制到每个非默认语言目录，目前硬编码了列表 `["zh"]`。

## 保持翻译同步

- 每个 pull request 都会运行 `mkdocs build --strict`；页面链接到某种语言中不存在的文件时检查会失败。
- 回退机制掩盖了缺失的页面，因此翻译可以后补而不影响站点。
- 建议的检查习惯：修改英文页面后，在同一个 pull request 中检查对应的中文页面。
