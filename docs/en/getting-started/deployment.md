---
title: Deploy with GitHub Pages
description: Publish the workshop site to GitHub Pages in approximately ten minutes.
---

# Deploy with GitHub Pages

This page describes the procedure for publishing the site, from an empty repository to a live deployment at `https://<you>.github.io/<your-repo>/`. The template performs the heavy lifting: a GitHub Actions workflow builds the site with MkDocs and publishes it to the `gh-pages` branch.

## Step 1 — Create a repository from the template

1. Open [github.com/CedricHaskell/WorkshopTemplate](https://github.com/CedricHaskell/WorkshopTemplate).
2. Click **Use this template** → **Create a new repository**.
3. Choose a repository name. The name determines the site URL: `git-workshop` results in `https://<you>.github.io/git-workshop/`.
4. Set visibility to **Public**. GitHub Pages on free accounts, and the [giscus](https://giscus.app) discussion board, both require a public repository.
5. Click **Create repository**.

!!! tip "Why "Use this template" instead of "Fork"?"

    A fork retains a link to the original repository and does not run workflows until Actions is enabled manually. A template copy is an independent repository, which is preferable for a site that will be customized extensively.

## Step 2 — Grant the workflow permission to deploy

The publish workflow pushes the built site to the `gh-pages` branch using the built-in `GITHUB_TOKEN`. New repositories default to *read-only* token permissions; the write permission must be granted: 

1. Open **Settings** → **Actions** → **General**.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Click **Save**.

## Step 3 — Trigger the first build

Creating a repository from a template is not a push event, so the workflow has not yet run. Any commit triggers it:

1. Open `mkdocs.yml` and click the pencil icon to edit.
2. Change `site_name: "Workshop Template"` to the name of the workshop.
3. Update `site_url` and `repo_url` at the same time; see [Step 5](#step-5-configure-site-identity).
4. Commit the change (top-right button; e.g. `chore: rename site`).

The **Actions** tab then shows the *publish site* workflow. If the tab reports that workflows are disabled, use the button on that page to enable them.

## Step 4 — Point GitHub Pages at the `gh-pages` branch

The workflow builds the site into the `gh-pages` branch. GitHub Pages must be configured to serve it:

1. Open **Settings** → **Pages**.
2. Under **Build and deployment** → **Source**, select **Deploy from a branch**.
3. Set **Branch** to `gh-pages` and the folder to `/ (root)`, then click **Save**.

The site is then available at `https://<you>.github.io/<your-repo>/`.

## Step 5 — Configure site identity

At minimum, update the following fields in `mkdocs.yml`:

```yaml
site_name: "My Workshop"                    # shown in the header and the browser tab
site_description: "A workshop about ..."    # used for SEO
site_author: "Your Name"
site_url: "https://<you>.github.io/<your-repo>/"   # canonical URLs and the language switcher
repo_url: "https://github.com/<you>/<your-repo>"
repo_name: "<your-repo>"
```

The branding assets in `docs/assets/` ship with the SSTIA logo. To use a custom logo, replace the following files:

- `logo.svg` — the logo in the header, to the left of the site name
- `favicon.svg` — the browser-tab icon

Finally, the **discussion board** must be pointed at the new repository. The template ships pre-configured for the original repository, so comments do not load on a copy until the configuration is updated. The procedure is described in [Discussion Board](../discussion.md).

## Local preview (optional)

For local editing with live reload:

```bash
git clone https://github.com/<you>/<your-repo>.git
cd <your-repo>
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

The preview is served at <http://localhost:8000>; saved changes reload the page automatically. The Chinese version is at <http://localhost:8000/zh/>.

- `mkdocs serve` — live preview server (the command above)
- `mkdocs build` — build the static site into `site/` for inspection
- `mkdocs build --strict` — build and fail on any broken link; this is what CI runs on pull requests

## The automation

Two workflows ship in `.github/workflows/`:

| Workflow | Trigger | Function |
| --- | --- | --- |
| `publish_site.yaml` | every push to `main` | installs dependencies, runs `mkdocs build`, pushes `site/` to the `gh-pages` branch |
| `health_check.yaml` | every pull request | runs `mkdocs build --strict`; pull requests with broken links fail CI |

## Troubleshooting

| Symptom | Cause and remedy |
| --- | --- |
| Site returns **404** | Pages is not yet pointed at `gh-pages` — perform [Step 4](#step-4-point-github-pages-at-the-gh-pages-branch) |
| Workflow never runs | No commit was pushed after repository creation, or Actions is disabled — see [Step 3](#step-3-trigger-the-first-build) |
| Workflow fails at the deploy step | Workflow permissions are read-only — see [Step 2](#step-2-grant-the-workflow-permission-to-deploy) |
| Site is live but links are broken or point to the wrong domain | `site_url` in `mkdocs.yml` still refers to the original template — update it ([Step 5](#step-5-configure-site-identity)) |
| Comments show an error on every page | giscus is still configured for the template repository — see [Discussion Board](../discussion.md) |
