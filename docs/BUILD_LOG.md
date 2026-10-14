# Build log

| Date | Actor | Action |
|---|---|---|
| 2026-10-14 | human:william | Asks to work on the portfolio when his Mac is off; repo kept private until the site is finished; creates the empty repo `williampenet/wip-portfolio` |
| 2026-10-14 | agent:orchestrator | Imports the local project (52 files; `.bak`, `.DS_Store`, design-tool cache and screenshots excluded). `python3 build.py` reproduces the committed pages byte for byte (checked on `index.html` and `about/index.html`). Adds CLAUDE.md, this log and a CI build check |
| 2026-10-14 | agent:orchestrator | Private preview published as a claude.ai artifact (home + 6 pages, built from `ca19892`). Found: `william-penet-cv.pdf` is linked but absent from the project |
| 2026-10-14 | human:william | New structure: "AI Works" becomes "Stuff I built" (personal projects); Freelance lists his jobs with a concrete case where possible; asks whether B-Sides should hold Data for Good and Time for the Planet; remove the LinkedIn dock icon |
| 2026-10-14 | agent:orchestrator | Folders reduced from 5 to 3: `stuff-i-built` (Nightcrawler, SpotiBoard), `freelance` (Interflora AI case merged into the Interflora card), `b-sides` (Data for Good and Time for the Planet as two cards, their dock icons reused as card logos). LinkedIn removed from the dock (kept in the About links). Old pages `ai-works/`, `data-for-good/`, `time-for-the-planet/` removed. Local Playwright QA (1280×800 and 375×812): 3 pages render, dock navigation works, no horizontal scroll, no page error |
