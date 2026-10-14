---
name: WiP Portfolio
description: A quiet, type-led personal portfolio that reads like a working document still being revised — the hiring manager's product memo.
colors:
  canvas: "#F8F6F3"
  surface: "#FFFFFF"
  panel: "#EFEBE6"
  ink: "#14121A"
  body: "#4A4552"
  muted: "#6B6472"
  hairline: "#E4E0DB"
  hairline-strong: "#D8D2CB"
  media-note: "#655E56"
  accent: "#4A2244"
  accent-ink: "#3B1A36"
  accent-pressed: "#2E1428"
  accent-tint-onink: "#EBD9E4"
typography:
  display:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "68px"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "36px"
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  title:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "26px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  lead:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "19px"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  button:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "15px"
    fontWeight: 600
    letterSpacing: "-0.005em"
  meta:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "14px"
    fontWeight: 500
    lineHeight: 1.5
  label:
    fontFamily: "'Instrument Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.08em"
rounded:
  control: "8px"
  panel: "12px"
  media: "16px"
  notch: "32px"
spacing:
  u: "8px"
  tight: "12px"
  gap: "24px"
  comfort: "48px"
  pad-y: "128px"
  pad-x: "40px"
  prose: "680px"
  maxw: "1240px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "#FFFFFF"
    rounded: "{rounded.control}"
    padding: "13px 22px"
  button-primary-hover:
    backgroundColor: "{colors.accent-ink}"
    textColor: "#FFFFFF"
  button-primary-active:
    backgroundColor: "{colors.accent-pressed}"
    textColor: "#FFFFFF"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "13px 22px"
  button-ghost-hover:
    backgroundColor: "{colors.ink}"
    textColor: "#FFFFFF"
  button-onink:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "13px 22px"
  button-onink-hover:
    backgroundColor: "{colors.accent-tint-onink}"
    textColor: "{colors.ink}"
  tool-card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.body}"
    rounded: "{rounded.media}"
    padding: "28px"
  contact-panel:
    backgroundColor: "{colors.ink}"
    textColor: "#FFFFFF"
    rounded: "{rounded.media}"
    padding: "96px 72px"
---

# Design System: WiP Portfolio

## Overview

**Creative North Star: "Work in Progress"**

WiP is both the author's initials and the thesis of the page: William Pénet, and Work in Progress. The identity is anti-perfectionism — always something cooking, humility over polish, ship rather than wait. The page itself behaves like a draft the author trusts: nothing is pretending to be finished, every element reads as revisable, and the one deliberate "cut corner" (the signature notch on every photographic frame) proves it.

The system is almost monochrome on a warm off-white canvas. A single heavy grotesque — Instrument Sans at display size — does the compositional work that imagery or ornament would do in a louder system. Hairline rules make the document's outline visible before any copy is read. A single studio-plum accent appears only where William has committed to a decision: a primary action, a hover state, a link under the pointer. Everything else is neutral, structural, and quiet. The restraint is what makes the mark land; the mark is what proves the restraint is a choice rather than a limitation.

The anti-reference is as important as the reference. This is not a shiny landing page. No glassmorphism, no gradients, no parallax, no 3D, no glow, no stacked shadows, no hover lifts, no eyebrows above headings, no decorative chrome. The craft is in rhythm, type, and the notch.

**Key Characteristics:**

- Warm off-white canvas (`#F8F6F3`), near-black ink (`#14121A`), one studio-plum accent (`#4A2244`).
- A single typeface across every role: Instrument Sans, four weights.
- No shadows anywhere. Depth comes from tonal surface steps and 1px hairline rules.
- A 32px radial-mask notch on every photographic frame — the only ornamental device.
- Generous whitespace. 128px band padding desktop, 72px mobile. Prose capped at 680px.
- Motion reveals once per element and never resets; frames stay fixed while their contents settle.

## Colors

A near-monochrome warm palette with one saturated accent. Canvas and panels step tonally from warm paper to flat white to deeper paper, and the deep ink closes the page as a single dark panel. The studio-plum accent reads humanist and refined — the color of a well-used fountain-pen cap — warm enough to agree with the cream canvas, cool enough to escape the Anthropic red/orange category entirely.

### Primary

- **Studio Plum** (`#4A2244`): the one saturated color on the page. Used on the primary button fill, on hovered links, on the thin link underline when active, and on focus rings. **Darker Plum** (`#3B1A36`) is the primary-button hover; **Pressed Plum** (`#2E1428`) is the active-press color; **Pink Tint** (`#EBD9E4`) is the hover background for white buttons sitting inside the deep-ink contact panel.

### Neutral

- **Draft Paper** (`#F8F6F3`): the warm off-white canvas that holds every band. The whole system sits on this.
- **Clean Surface** (`#FFFFFF`): used only on tool cards and reserved for small enclosed modules on the canvas.
- **Deeper Paper** (`#EFEBE6`): the backing color of every media frame — a half-step down from the canvas, enough to read as a container without needing a border.
- **Deep Ink** (`#14121A`): primary heading color, logo wordmark, ghost-button border; also the full background of the Contact band. Not pure black; carries a trace of indigo so it reads warm against the paper.
- **Body Ink** (`#4A4552`): running paragraph color. Soft enough that headlines separate cleanly; dark enough to pass contrast at 17px.
- **Muted Ink** (`#6B6472`): meta, section eyebrows, subtitles, link-column labels. The quiet third tier.
- **Hairline** (`#E4E0DB`): default rule color, 1px, used sparingly beneath landmarks and between project entries.
- **Hairline Strong** (`#D8D2CB`): underline for in-copy text links; one tier darker than the default rule so a link reads as a decided surface rather than a passing divider.
- **Media Note** (`#655E56`): the small-caps "Portrait" / "Working context" labels inside placeholder media frames. Reserved for placeholder scaffolding; disappears once real photography lands.

### Named Rules

**The One Accent Rule.** The studio-plum is used on ≤10% of any given screen. Its rarity is the point. If a band carries the accent on two different elements, the band is doing too much and should be split.

**The No-Gray Rule.** Secondary and tertiary text are tinted ink, not gray. The muted and body tones carry a trace of warm indigo; they're never desaturated flat gray.

## Typography

**Display Font:** Instrument Sans (with `-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif` fallback)
**Body Font:** Instrument Sans — same family, body weight.
**Label Font:** Instrument Sans — same family, uppercase with letter-spacing.

**Character:** A single geometric grotesque with a quiet confidence. Instrument Sans is cut for product UI but behaves at display size without feeling corporate; its slightly condensed proportions let 68px headlines sit on a 46/54 split without crowding. Variable weight (400–700) means every role in the hierarchy is one family, one voice.

### Hierarchy

- **Display** (700, 68px, 1.05 line-height, −0.02em tracking, `text-wrap: balance`): hero headline only. Drops to 52px below 980px and to 40px at 1.1 line-height below 680px.
- **Headline** (600, 36px, 1.15 line-height, −0.015em tracking, `text-wrap: balance`): section titles (`Selected work`, `How I think about it`, etc.). Drops to 30px on narrow screens.
- **Title** (600, 26px, 1.25 line-height, −0.01em tracking): project names, about heading, contact heading. Drops to 22px on narrow screens.
- **Lead** (400, 19px, 1.55 line-height): the one-sentence positioning paragraph under the hero. Drops to 17px on narrow screens.
- **Body** (400, 17px, 1.6 line-height, 65–75ch): running paragraphs. Drops to 16px on narrow screens.
- **Button** (600, 15px, −0.005em tracking): button and nav link labels.
- **Meta** (500, 14px, 1.5 line-height, muted color): project right-align meta, metadata values, footer copyright.
- **Label** (600, 12px, 1.4 line-height, 0.08em tracking, UPPERCASE, muted color): small-caps section eyebrows, metalist dt, footer column headings.

### Named Rules

**The One-Voice Rule.** Everything on the page is Instrument Sans. No secondary typeface — not for code, not for data, not for small-caps labels, not for "technical" accents. Variable weight carries every tonal shift.

**The Statement Rule.** Headlines are statements, not slogans. "I build the products I manage." is a sentence that ends in a period. No ampersands as decoration, no colons dangling, no three-word fragments.

## Layout

The system is built on an 8px base unit. The container caps at 1240px, prose caps at 680px — a reading column narrower than most magazine columns because the voice is confident enough to hold the reader at that measure. Side padding steps from 40px → 28px → 22px across three breakpoints; vertical band padding steps from 128px → 88px → 72px.

Hero is a **46/54 grid** — the headline column on the left (46%), the notched portrait frame on the right (54%), 72px gap. The headline column holds the entire argument; the portrait frame carries the signature device. Positioning uses a **three-column pattern** with a hairline rule above each column — the only place rules appear outside landmark borders. Project entries use a **54/46 grid** — the write-up on the left dominates, the media on the right balances. Toolbox is a three-column grid of white rounded cards. About uses a **1/2 grid** — a tight small-caps label at left, heading plus paragraph at right.

### Breakpoints

- **≤980px:** hero becomes single column; project single column; about single column; cols3 keeps 3 columns but closes gap to 36px; tools drops to 2 columns; display drops to 52px.
- **≤680px:** cols3 collapses to 1; principles collapse to 1; tools collapse to 1; metalist collapses to 1 column; contact padding shrinks to 56×28; display drops to 40px and tightens to 1.1 line-height; body steps down to 16px.

### Named Rules

**The Band Economy Rule.** Each band carries at most one of: the signature notch, a hairline rule, the accent. More than one and the band is doing two things; split it.

**The Prose Measure Rule.** Running paragraphs are capped at 680px even inside a 1240px container. The whitespace is the pause between claims.

## Elevation & Depth

**No shadows anywhere.** The system is flat by doctrine. Separation comes from two sources: (1) tonal surface steps between canvas (`#F8F6F3`), paper (`#EFEBE6`), surface (`#FFFFFF`), and ink (`#14121A`); and (2) 1px hairline rules under landmarks, between project entries, and above the footer. Both are quiet; neither pretends to be lift.

Depth is also carried by the signature **notch** cut out of one corner of every photographic frame. The notch is not an elevation device — it's a form device — but it is the one place where a surface's silhouette departs from the orthogonal grid, and that departure is enough to make the frame read as a distinct object without needing a shadow.

### Named Rules

**The Flat Rule.** No `box-shadow`, no `drop-shadow`, no filter blur, no inner glow, no colored halo. Hover and focus states change color only — never scale, never shift, never lift.

**The Hairline Rule.** Rules are 1px, `#E4E0DB`, and used only where they do work: beneath the nav, above the footer, under positioning columns, between project entries, and as the base of in-copy text links (one tier darker, `#D8D2CB`). They are never used as decoration.

## Shapes

A three-step radius scale plus one signature cut. The form language is rectilinear and quiet, with the notch doing all the character work.

- **8px (control):** buttons and small radii. Enough to read as finished, small enough to still feel editorial.
- **12px (panel):** reserved for small ambient panels. Rarely used in the current system.
- **16px (media):** media frames, tool cards, the contact section. The dominant radius; anything that holds content gets 16px.
- **32px (notch):** exactly twice the media radius. Only applied to photographic frames via a radial-mask gradient on one corner. Produces a concave quarter-round cut that reads as a deliberately removed corner.

### Named Rules

**The Signature Notch Rule.** Every photographic image sits in a 16px rounded frame with exactly one 32px notch cut from the corner nearest the adjoining text block. The notch radius is literal — 32px — and never scales with the image. It is applied only to photographic and product media; never to cards, panels, buttons, or the logo. No border, no shadow, no overlay accompanies the notch. During the entrance animation, the frame geometry stays fixed; only the image inside it moves.

**The Rectilinear Rule.** Outside the notch and the radii above, every surface is a rectangle. No pill buttons, no circles, no polygons, no clipped diagonals, no radial masks beyond the single notch.

## Components

### Buttons

Shape: 8px rounded rectangle, 13px top/bottom and 22px left/right padding, 15px/600 label with −0.005em tracking. Transitions are `.16s linear` on background, border, and color — color-only hover feedback with no scale, no translate, no shadow. The four variants are used at specific sites, not interchangeably.

- **Primary (`.btn--primary`):** Studio Plum fill (`#4A2244`), white text. Hover drops to Darker Plum (`#3B1A36`); active press to Pressed Plum (`#2E1428`). The primary is the one authored moment of color on any band; it is the "name the trade-off" button — it appears only where William has decided.
- **Ghost (`.btn--ghost`):** 1px Deep Ink border, Deep Ink text, transparent fill. Hover inverts fully — Deep Ink becomes the fill, white becomes the text. No intermediate state.
- **On-ink (`.btn--onink`):** white fill, Deep Ink text. Used only inside the Contact panel (which is itself Deep Ink). Hover shifts the fill to Pink Tint (`#EBD9E4`) — the one place the plum accent arrives on dark.
- **On-ink Ghost (`.btn--onink-ghost`):** `rgba(255,255,255,.4)` border, white text, transparent fill. Used only inside the Contact panel beside the On-ink primary. Hover brings the border to full white and tints the fill with 8% white.

### Text Links

- **`.tlink`:** Deep Ink text, 500 weight, 1px underline border in `#D8D2CB`. Hover shifts both color and border to the accent. The underline is a border, not a text-decoration — so its offset stays stable across weights.

### Nav

- **`.nav`:** canvas background, 22px top/bottom padding, brand lockup (52px logo image + 17px/700 wordmark with −0.02em tracking) at left, three primary links at right (15px/500, body color, hover accent). A 1px hairline rule sits beneath the entire nav as the band separator.

### Media Frame

- **`.media`:** 16px radius container with Deeper Paper background. Carries the signature 32px notch via `-webkit-mask: radial-gradient(...)`. Three variants (`--br`, `--bl`, `--tl`) place the notch on different corners. The frame's silhouette is the component; it never carries a shadow or a border.

### Tool Card

- **`.tool`:** white fill, 16px radius, 28px padding. Each card holds a 15px/600 heading and a short unstyled list of 15px items at body ink. No border, no shadow. Three per row at desktop, two at 980px, one at 680px.

### Contact Panel

- **`.contact`:** full-bleed Deep Ink background within the 1240px container, 16px radius, 96×72px padding. The one dark panel on the page. Heading inverts to white; body sits at 72% white; the small-caps label sits at 55% white. Carries the two on-ink button variants side by side.

### Section Heading Block

A reusable triplet: a 1px hairline rule that scales from 0 → full width on reveal, immediately followed by a 36px/600 headline. Where a secondary line is needed, a 14px/500 meta sits on the right baseline-aligned to the heading.

### Signature Component: The Section Rule

A `.rule` element — 1px high, `#E4E0DB`, no border, `transform-origin: left center`. On scroll reveal, it scales horizontally from 0 to 1 over 600ms. It is the one authored moment on nearly every section opening — a visible redraw of the document's outline, confirming that the structure is live and not static.

## Do's and Don'ts

### Do

- **Do** reach for Studio Plum only when a decision has been made. If you can't name what the user is deciding by clicking it, the color is wrong.
- **Do** use the signature notch on every photographic frame and only on photographic frames.
- **Do** vary weight (400 / 500 / 600 / 700) rather than reaching for a second font. The One-Voice Rule is binding.
- **Do** carry the voice from PRODUCT.md verbatim — plain, direct, trade-off-aware, 1st-person-singular, no exclamation marks.
- **Do** cap running paragraphs at 680px even in a 1240px container.
- **Do** use `text-wrap: balance` on display and headline sizes; the line breaks are design.
- **Do** honor `prefers-reduced-motion`: restore every element to its final visible state, keep instantaneous color feedback on controls.

### Don't

- **Don't** add shadows, gradients, glass blur, parallax, or 3D. The Flat Rule is total.
- **Don't** scale, translate, or lift components on hover. Color-only feedback.
- **Don't** place an eyebrow or kicker above a heading. The heading carries its own weight.
- **Don't** use gray for secondary text. Tint the ink; the palette is warm all the way down.
- **Don't** carry the notch to anything that isn't a photographic frame — not to cards, not to panels, not to buttons, not to the logo.
- **Don't** introduce a second accent color. The system is one-accent on purpose.
- **Don't** stage sections with "01 / 02 / 03" numbering. The reader doesn't need the count.
- **Don't** reach for Unicode glyphs or emoji where a drawn SVG icon belongs. The current arrow icon is authored; keep it so.
- **Don't** fabricate testimonials, logos of past employers, or quantitative metrics. Placeholders are labeled as placeholders.
