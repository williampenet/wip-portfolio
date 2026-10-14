# WiP Portfolio — context for agents

William Pénet's personal portfolio site (job search, senior Product / AI product builder roles).
Status: **private, work in progress.** Do not make the repo public or deploy it publicly
until William says the site is finished.

Read before any change:
- `PRODUCT.md` — audience, purpose, positioning, voice (binding on all copy).
- `DESIGN.md` — design tokens, typography, layout rules.
- `.taste/` and `.impeccable/design.json` — design-tool state (brief and design decisions).
- `docs/BUILD_LOG.md` — dated log of human and agent actions.

## How the site is built
- Sources: `content.md` (every text), `src/index.template.html` (markup and CSS), `assets/`.
- `python3 build.py` (no dependency) inlines fonts and images and writes the generated pages:
  `index.html` and `<slug>/index.html` (about, ai-works, freelance, b-sides, data-for-good,
  time-for-the-planet).
- Never edit a generated `index.html` by hand: edit the sources, run the build, commit both.
- CI (`.github/workflows/build.yml`) fails if the committed pages differ from a fresh build.
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

## Rules
- Repo and docs in English; conversation with William in French.
- Every claim or conclusion is sourced (official doc, measurement, test) or marked "unverified".
- No secrets in the repo. Contact surfaces are public by design (mailto, LinkedIn).
