# Validation notes

- Built successfully with Hugo 0.147.9 on Linux.
- All 50 lesson cards render in the chaptered lesson index.
- Lesson pages 01, 25 and 50 checked for correct previous/next ordering.
- Generated internal navigation and image references pass the supplied link checker.
- Empty video/PDF fields render non-clickable availability labels.
- Brand assets are included; the public package contains no private lesson scripts or paid PDFs.
- GitHub Action tag files were retrieved for checkout, configure-pages, upload-pages-artifact and deploy-pages.

Not exercised here: RStudio execution (R is unavailable in this environment), authenticated GitHub deployment, full desktop/mobile visual inspection or interactive filtering in a browser. A browser runtime was attempted but could not launch reliably. Use `blogdown::serve_site()` for the final visual review before publishing. The site includes responsive CSS and a progressive-enhancement search/filter; all lesson links remain available without JavaScript.

## Your brief release check

1. Open Home, Lessons, one lesson page, Resources and Shop on desktop and a narrow window.
2. Search for a lesson and change chapters; clear the search to restore all lessons.
3. Add one real free PDF and confirm its link opens in the local preview.
4. Read the two launch posts and About page; customize any wording you want.
5. Enable GitHub Actions in Pages, push and inspect the deployment result.
