# Publishing your PDFs

## Where each link is edited

| Material | Upload folder | Link setting |
|---|---|---|
| Lesson worksheet | `static/downloads/` | `worksheet_url` in the lesson's `index.md` |
| Lesson answer key | `static/downloads/` | `answer_key_url` |
| Lesson cards | `static/downloads/` | `flashcards_url` |
| Alphabet chart, passport, general references | `static/downloads/` | matching `url` in `data/resources.yaml` |
| Paid workbook or book | your storefront, not this public repo | `shop_url` in `hugo.yaml` or a public product-page link |
| YouTube video | YouTube | `youtube_url` in the lesson front matter |

## Example: complete lesson 02 publication

1. Render and check your free worksheet, key and cards from your private repository.
2. Copy only the release PDFs into this site's `static/downloads/` directory.
3. Set the fields in `content/lessons/02/index.md`:

```yaml
youtube_url: "https://www.youtube.com/watch?v=YOUR_ACTUAL_VIDEO_ID"
worksheet_url: "downloads/lesson-02-worksheet.pdf"
answer_key_url: "downloads/lesson-02-answers.pdf"
flashcards_url: "downloads/lesson-02-flashcards.pdf"
```

The video URL above is a documentation example; replace it with a real URL before publishing. The delivered site has empty values instead of fake links.

4. Run `blogdown::serve_site()` and click each link.
5. Commit the three PDFs and the edited lesson page, then push.

You can publish the worksheet before the video or vice versa. Buttons are controlled independently. The lesson index's “Watch now” label appears only when `youtube_url` is filled.

To remove a link, set its field back to an empty string. The PDF may remain public through history or its direct URL unless you also remove it; do not treat this as a paid-download access control.

## Common mistakes

- Do not use `C:/Users/...` or `file:///...` links.
- Do not include `static/` in the URL.
- Avoid a leading slash; use `downloads/file.pdf` so project-site prefixes are handled correctly.
- Do not copy the full course ZIP or private repository into this site.
- Avoid filenames differing only by case.
- To link to the existing personal homepage, use the full `https://noushinn.github.io/` URL; internal site links stay inside the project.
