---
title: 部署到 GitHub Pages
description: 在约十分钟内把 workshop 网站发布到 GitHub Pages。
---

# 部署到 GitHub Pages

本页说明从空仓库到站点上线（`https://<you>.github.io/<your-repo>/`）的完整流程。模板承担了主要工作：GitHub Actions 工作流用 MkDocs 构建站点并发布到 `gh-pages` 分支。

## 第 1 步——从模板创建仓库

1. 打开 [github.com/CedricHaskell/WorkshopTemplate](https://github.com/CedricHaskell/WorkshopTemplate)。
2. 点击 **Use this template** → **Create a new repository**。
3. 填写仓库名。仓库名决定站点 URL：`git-workshop` 对应 `https://<you>.github.io/git-workshop/`。
4. 可见性选择 **Public**。免费账号的 GitHub Pages 与 [giscus](https://giscus.app) 讨论区都要求仓库公开。
5. 点击 **Create repository**。

!!! tip "为什么用 "Use this template" 而不是 "Fork"？"

    Fork 会保留与原仓库的关联，且需要手动启用 Actions 才会运行工作流。模板副本是一个独立的仓库，更适合需要大量定制的站点。

## 第 2 步——授予工作流部署权限 {#step-2-grant-the-workflow-permission-to-deploy}

发布工作流使用内置的 `GITHUB_TOKEN` 把构建产物推送到 `gh-pages` 分支。新仓库默认只读权限，需要手动放开：

1. 打开 **Settings** → **Actions** → **General**。
2. 在 **Workflow permissions** 下选择 **Read and write permissions**。
3. 点击 **Save**。

## 第 3 步——触发第一次构建 {#step-3-trigger-the-first-build}

从模板创建仓库不属于 push 事件，因此工作流尚未运行。任意一次提交都会触发它：

1. 打开 `mkdocs.yml`，点击铅笔图标进入编辑。
2. 把 `site_name: "Workshop Template"` 改为 workshop 的名称。
3. 同时更新 `site_url` 与 `repo_url`，见[第 5 步](#step-5-configure-site-identity)。
4. 提交修改（右上角按钮，例如 `chore: rename site`）。

随后 **Actions** 标签页会显示 *publish site* 工作流。如果页面提示工作流被禁用，点击页面上的按钮启用即可。

## 第 4 步——让 GitHub Pages 指向 `gh-pages` 分支 {#step-4-point-github-pages-at-the-gh-pages-branch}

工作流把站点构建到 `gh-pages` 分支，还需要让 GitHub Pages 托管它：

1. 打开 **Settings** → **Pages**。
2. 在 **Build and deployment** → **Source** 中选择 **Deploy from a branch**。
3. **Branch** 设为 `gh-pages`，目录设为 `/ (root)`，点击 **Save**。

站点随后可在 `https://<you>.github.io/<your-repo>/` 访问。

## 第 5 步——配置站点信息 {#step-5-configure-site-identity}

至少更新 `mkdocs.yml` 中的以下字段：

```yaml
site_name: "My Workshop"                    # 页头与浏览器标签页显示的名称
site_description: "A workshop about ..."    # 用于搜索引擎
site_author: "Your Name"
site_url: "https://<you>.github.io/<your-repo>/"   # 规范 URL 与语言切换器依赖此值
repo_url: "https://github.com/<you>/<your-repo>"
repo_name: "<your-repo>"
```

Logo文件默认是SSTIA图标。如果你需要用自己的图标，需要同时替换 `docs/assets/` 中的：

- `logo.svg` —— 页头 Logo，位于站点名称左侧
- `favicon.svg` —— 浏览器标签页图标

最后，**讨论区**必须指向新仓库。模板默认配置的是原仓库，因此评论在副本上不会加载，直到配置被更新。具体步骤见[讨论区](../discussion.md)。

## 本地预览（可选） {#local-preview}

如需本地编辑与实时刷新：

```bash
git clone https://github.com/<you>/<your-repo>.git
cd <your-repo>
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

预览地址为 <http://localhost:8000>，保存即自动刷新页面。中文版位于 <http://localhost:8000/zh/>。

- `mkdocs serve` —— 实时预览服务器（即上面的命令）
- `mkdocs build` —— 把静态站点构建到 `site/` 目录供检查
- `mkdocs build --strict` —— 构建并在链接失效时报错；CI 对 pull request 执行的正是这一命令

## 自动化机制

模板在 `.github/workflows/` 中附带两个工作流：

| 工作流 | 触发时机 | 作用 |
| --- | --- | --- |
| `publish_site.yaml` | 每次推送到 `main` | 安装依赖 → `mkdocs build` → 把 `site/` 推送到 `gh-pages` 分支 |
| `health_check.yaml` | 每个 pull request | 运行 `mkdocs build --strict`；存在失效链接的 PR 无法通过 CI |

## 常见问题

| 现象 | 原因与处理 |
| --- | --- |
| 站点返回 **404** | Pages 尚未指向 `gh-pages` ——执行[第 4 步](#step-4-point-github-pages-at-the-gh-pages-branch) |
| 工作流从不运行 | 创建仓库后没有提交，或 Actions 被禁用 ——见[第 3 步](#step-3-trigger-the-first-build) |
| 工作流在部署步骤失败 | 工作流权限为只读 ——见[第 2 步](#step-2-grant-the-workflow-permission-to-deploy) |
| 站点上线但链接失效或指向错误域名 | `mkdocs.yml` 中的 `site_url` 仍指向原模板 ——更新它（[第 5 步](#step-5-configure-site-identity)） |
| 每个页面评论区都报错 | giscus 仍配置为模板仓库 ——见[讨论区](../discussion.md) |
