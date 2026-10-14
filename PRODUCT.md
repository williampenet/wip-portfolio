# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Hiring managers and recruiters at tech companies evaluating William Pénet for a senior Product role. They typically arrive cold from an application reply, a LinkedIn message, or a recruiter outreach — one visit, usually a minute or two, deciding whether to start an interview conversation.

## Product Purpose

A single-page personal portfolio that convinces a hiring manager William is worth interviewing. Success is a reply to the contact email or a scheduled call. It is not a lead-gen page for consulting, a link-in-bio, or a personal blog.

## Positioning

The outcome a visitor should feel is pinned: William is a **Product Builder with full AI fluency**, not a "simple Product Manager." The current site's headline — "I build the products I manage" — and its frame → decide → build → explain-the-trade-offs mechanism are a working hypothesis in that direction. Exact wording is open; the market signal (Product Builder, AI-fluent) is the constraint future surface work must honor.

## Operating Context

- Opened cold, with no prior conversation. The page must stand alone.
- Reading budget is roughly a minute or two before a hiring manager decides to reply, bookmark, or close.
- Visitors are likely to arrive on desktop (from an email client or application tracker) and on mobile (from LinkedIn). The deliverable must work on both without a build server.
- The link itself is often forwarded internally; the page is read with other candidates' pages open in adjacent tabs.

## Capabilities and Constraints

- Single-file self-contained deliverable. `build.py` base64-inlines the font (`assets/instrument-sans-latin.woff2`) and the logo (`assets/logo.webp`) into `src/index.template.html` and writes `index.html`. No backend, no runtime dependencies, no accounts, no analytics. The site can be served from GitHub Pages, any static host, or sent as a direct file.
- Build command: `python3 build.py` from the project root.
- Section anchors: `#top`, `#work`, `#about`, `#contact`. Keyboard affordances already in place (skip link, aria landmarks, focus-visible rings).
- Contact surfaces: `mailto:william.penet@gmail.com` and a LinkedIn link. The current LinkedIn `href` is a placeholder (`https://www.linkedin.com/in/` with no slug) — undecided factual gap.
- Copyright "© 2026" is current.

## Brand Commitments

- **Name / wordmark:** WiP (William Pénet). Logo at `assets/logo.webp`.
- **Voice:** plain, direct, trade-off-aware, slightly contrarian. No PM jargon, no startup clichés, no hedging adjectives. This is a binding constraint on all copy.
- **Legal entity:** WiP EURL (statuts in parent folder; not displayed on-site).

## Evidence on Hand

- **Nightcrawler** — the one live shipped build. URL: https://williampenet.github.io/nightcrawler/. Concert discovery that reads a visitor's taste against venue listings. Taste comes from typed-in artists or a Spotify connection enriched with MusicBrainz style data; a Mistral model scores each concert and sorts it into Must Not Miss / For You / Discovery. State lives in the browser; no accounts, no backend. Solo-built. This is the current anchor case for "builds what he manages."
- Six confirmed principles, written in William's voice: *Cut before you add; Ship it to learn it; Name the trade-off; Build enough to be dangerous; Plain words; Go and look.*
- Toolbox the site commits to: Discovery (interviews, framing, opportunity mapping, desk research); Prototyping (Figma, hand-built HTML prototypes, clickable flows); AI-assisted build (Claude Code, Mistral, prompt design, model evaluation); Data (SQL, event instrumentation, funnel analysis); Writing (page-length specs, decision records, written trade-offs); Delivery (scoping and slicing, release planning, post-release review).
- Instrument Sans is the pinned typeface; the font file ships with the build.

**Absences future work must not fabricate:**

- No testimonials, no quotes from colleagues or managers.
- No logos of past employers, companies, or clients.
- No quantitative metrics (revenue, DAU, conversion, headcount) unless William supplies verified numbers.
- No case studies beyond Nightcrawler. "More builds in progress" is acknowledged on the page but is not evidence.
- Portrait and "working context" image areas are placeholders. Real photography is not yet shot, and whether it will be shot is undecided.
- LinkedIn URL slug is undecided; the current `href` is a placeholder.

## Product Principles

- **Convey Product Builder with AI fluency, not Product Manager.** The feeling the visitor leaves with is the brief.
- **Plain words win.** Any PM-ism, buzzword, or hedging adjective gets cut on sight. If a sentence could appear on a hundred other PM portfolios, it fails.
- **Ship a self-contained deliverable.** No backend, no runtime dependencies, no third-party tracking. The site must open from a `file://` path or any static host.
- **Only verified evidence appears on the page.** Placeholders are labeled as placeholders. Nightcrawler is the anchor until more live builds exist.
- **Trade-offs are stated out loud.** The absence of case studies, metrics, or photography is honest surface, not a problem to paper over.

## Accessibility & Inclusion

Current build already provides a skip link, aria landmarks on the primary nav and main sections, focus-visible outlines, and a `.sr` utility for screen-reader-only content. No formal standard (WCAG AA/AAA) was pinned by William. Preserve existing a11y affordances; no additional product-specific requirement established.
