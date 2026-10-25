# WiP Portfolio — context for agents

William Pénet's personal portfolio site (job search, senior Product / AI product builder roles).
Status: **public repo, work in progress** (made public by William on 2026-10-17).
Everything committed is world-readable, including history: never commit secrets or
personal data beyond the public contact surfaces.

Read before any change:
- `PRODUCT.md` — audience, purpose, positioning, voice (binding on all copy).
- `DESIGN.md` — design tokens, typography, layout rules.
- `.taste/` and `.impeccable/design.json` — design-tool state (brief and design decisions).
- `docs/BUILD_LOG.md` — dated log of human and agent actions.

## How the site is built
- Sources: `content.md` (every text), `src/index.template.html` (markup and CSS), `assets/`.
- `python3 build.py` (no dependency) inlines fonts and images and writes the generated pages:
  `index.html` and `<slug>/index.html` (about, stuff-i-built, career, b-sides).
- Never edit a generated `index.html` by hand: edit the sources, run the build, commit both.
- CI (`.github/workflows/build.yml`) fails if the committed pages differ from a fresh build.
- Search and link-preview metadata (title, description, Open Graph, X card, canonical, JSON-LD,
  `sitemap.xml`) come from `content.md` (`title`, `description`, Home `url`) through `build.py`.
  The share image and icons in `assets/share/` are made by `scripts/make_share_images.py`
  (needs Pillow + fontTools; rerun it when the name or role changes, then commit the PNGs).
  After a change, refresh LinkedIn's cached preview with https://www.linkedin.com/post-inspector/.
- `assets/logos-src/` holds original logo files; only processed copies in `assets/logos`,
  `assets/companies` and `assets/dock` are used by the build.

## Where work happens
- GitHub (`williampenet/wip-portfolio`, branch `main`) is the source of truth.
- William's Mac holds a clone in his Obsidian vault:
  `/Users/williampenet/Documents/IDEAVERSE/PRO/WiP Portfolio`.
  Start every local session with `git pull`; end it with commit + push.
- Cloud sessions (Claude app, Mac off) clone the repo and push to `main` (or a PR if the change
  is large or risky).
- Log every session's actions in `docs/BUILD_LOG.md`.

## Preview
- Live site: https://williampenet.github.io/wip-portfolio/ (GitHub Pages, branch `main`, root;
  enabled by William on 2026-10-17). Every push to `main` redeploys it ("pages build and
  deployment" workflow). github.io is blocked from the agent workspace: check it with WebFetch
  or a browser tool.
- Preview = private claude.ai artifact https://claude.ai/artifact/XTgW9uK9Gixs3S9WAX5LUu
  (`index.html` as the page, each `<slug>/index.html` as a file). After a change to `main`,
  republish it to the same URL (Artifact tool, `url` = that link) so William sees it on any device.
- CV: a Google Doc shared by William (link in the dock and in About, `src/index.template.html`).

## Rules
- Repo and docs in English; conversation with William in French.
- Every claim or conclusion is sourced (official doc, measurement, test) or marked "unverified".
- No secrets in the repo. Contact surfaces are public by design (mailto, LinkedIn).
