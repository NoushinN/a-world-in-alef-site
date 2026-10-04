# A World in Alef — public website

A complete, custom blogdown/Hugo website for GitHub Pages. Edit it in RStudio, preview locally, then commit and push. The existing feather banner, alef emblem and ivory/charcoal palette connect the site to your teaching materials.

**Suggested public repository:** `a-world-in-alef` under `NoushinN`.

**Expected project address after you deploy:** `https://noushinn.github.io/a-world-in-alef/`.

This is a separate project site, so your existing `https://noushinn.github.io/` homepage can remain in place. This package does not create a remote repository or publish it automatically from your computer. You choose when to push it to GitHub.

## Navigation

| Tab | Purpose | Edit here |
|---|---|---|
| Home | Banner, welcome, learning pathways, first lessons and journal | `layouts/index.html` and `hugo.yaml` |
| Start Here | A clear first step for new learners | `content/start-here.md` |
| Lessons | Searchable 50-lesson pathway and individual lesson pages | `content/lessons/` |
| Resources | Free reference downloads and practice companions | `data/resources.yaml` |
| Blog | Language, culture and future vlog notes | `content/blog/` |
| About | Brand introduction; space for your personal biography | `content/about.md` |
| Shop | Future workbooks, readers and merchandise | `content/shop/index.md`, `hugo.yaml` |

`Privacy & use` is a footer link. Shop currently says coming later; remove its menu entry in `hugo.yaml` if you prefer to launch without the tab.

## 1. Preview in RStudio

1. Extract the ZIP into a new folder **outside your private teaching repository**.
2. Open `a-world-in-alef.Rproj`.
3. In the **R Console**, run once:

```r
source("scripts/setup.R")
```

4. Preview:

```r
blogdown::serve_site()
```

5. Edit and save a content file; the local preview updates. Stop with:

```r
blogdown::stop_server()
```

Do not use the worksheet Python renderer for this website. blogdown uses Hugo; the supplied `.md` pages do not need a separate Pandoc rendering step. Optional `.Rmd` posts do use Pandoc via blogdown.

Hugo is pinned to **0.147.9**, the version used to test this site. The custom theme is bundled in `layouts/` and `static/css/`, so there is no external theme or Git submodule to install. If you already have a different Hugo version for another project, blogdown can keep this project's version separately.

## 2. Create the public repository and connect RStudio

Recommended beginner workflow:

1. On GitHub, create a new **public** repository named `a-world-in-alef`. Initialize it with a README so `main` exists.
2. Copy its HTTPS clone URL, normally `https://github.com/NoushinN/a-world-in-alef.git` (no trailing period).
3. In RStudio choose **File → New Project → Version Control → Git**, paste that URL, and choose a new local folder.
4. Close that initial project. Copy the website package contents into the cloned folder, replacing the starter README. Include `.github/`, `.Rprofile` and `.gitignore`. Do **not** copy the private course repository.
5. Open `a-world-in-alef.Rproj` in the cloned folder. If RStudio created a second `.Rproj`, retain the supplied project and remove the unused one.
6. In the Git pane, stage the site files, commit with a message such as “Add A World in Alef website”, and push.
7. In GitHub, open this new repository → **Settings → Pages → Source → GitHub Actions**.
8. Open **Actions → Build and publish blogdown site → Run workflow** if the initial push ran before Pages was enabled. After a successful deployment, the workflow displays your live URL.

If the Git pane is absent, Git needs to be installed/configured for RStudio, and the project folder must be a Git clone. Authentication uses your own GitHub sign-in/credential manager. No credentials belong in this repository.

Future workflow: **Pull → edit → preview → commit → push**. Each push to `main` rebuilds and publishes the site. For work you do not want public yet, use a local branch; remember that anything pushed to a public repository is publicly readable, including draft source.

The Pages workflow determines the deployment URL automatically. If you choose another repository name or a custom domain, update `baseURL` in `hugo.yaml` as well so local builds and metadata match.

## 3. Add a PDF link

For lesson 02, copy only the free PDF you want public into:

```text
static/downloads/lesson-02-worksheet.pdf
```

Open `content/lessons/02/index.md` and change:

```yaml
worksheet_url: ""
```

to:

```yaml
worksheet_url: "downloads/lesson-02-worksheet.pdf"
```

Use **forward slashes**, simple filenames, and no initial `static/`. The template adds the project path automatically. Match uppercase/lowercase exactly; GitHub Pages is case-sensitive.

The matching fields are:

```yaml
youtube_url: ""
worksheet_url: ""
answer_key_url: ""
flashcards_url: ""
```

Empty fields show “Coming soon” without a clickable dead link. To link externally, use a full `https://...` URL. To add general reference downloads, edit `data/resources.yaml` and use the same path pattern. See [publishing downloads](docs/downloads.md).

## 4. Add your channel, shop and introduction

In `hugo.yaml`, fill the `youtube_url` and `shop_url` values when ready. The channel link then appears in the footer; the shop page links to your external storefront. This static site does not provide payments, logins, mailing lists or a customer download system.

In `content/about.md`, add your biography if desired. No personal biography has been invented. The two introductory blog posts are editable launch copy, not claims about a past release schedule.

`contact_email` is reserved for a future contact link; it is not currently displayed. If you choose to publish an address, add it to the About page using a Markdown mailto link and update the privacy page.

## 5. Write a blog post

The simplest approach: duplicate one `content/blog/.../` folder, rename it, and edit its `index.md` title, date, description and body.

Or use the R Console:

```r
blogdown::new_post("A new word for today", ext = ".md", subdir = "blog")
```

For R code chunks, copy `docs/rmarkdown-example.Rmd` to a new folder under `content/blog/`, named `index.Rmd`. Set `draft: false` when it is ready. Do not keep `index.md` and `index.Rmd` for the same post. The deployment workflow installs blogdown and compiles R Markdown before building Hugo; extra R packages used by a post must also be installed in that workflow.

## Public and private boundaries

This site contains **public summaries and download placeholders**, not full lesson scripts, paid workbook sources, answer collections or private audio manifests. Only the selected brand/picture assets were copied from the teaching package.

Files inside `static/` are published directly. Do not put paid PDFs there; link to their storefront product pages. A private-repository URL is not a public download link for visitors. Public Git history can retain deleted files, so only upload files you intend to release.

## Build and check

```r
source("scripts/build.R")
```

Generated pages go into `public/`, which is Git-ignored. The GitHub workflow builds this folder itself. Do not push generated HTML as a second site source or change Pages to “Deploy from a branch.”

The optional Python link check is already run by GitHub Actions; you do not need Python for normal RStudio editing:

```bash
python scripts/check_site.py public
```

See [validation notes](docs/validation.md) and [sources](docs/sources.md).

© 2026 A World in Alef. See [rights](RIGHTS.md).
