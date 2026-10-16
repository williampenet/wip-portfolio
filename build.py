#!/usr/bin/env python3
"""Build the WiP portfolio.

Reads every text from content.md, inlines fonts and images into
src/index.template.html, and writes:
  index.html                      home
  <slug>/index.html               one static page per folder and About,
                                  so every URL works without JavaScript.

Usage:  python3 build.py
"""
import base64
import html as htmlmod
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
TEMPLATE = ROOT / "src" / "index.template.html"
CONTENT = ROOT / "content.md"

ASSETS = {
    "{{FONT_B64}}": "assets/instrument-sans-latin.woff2",
    "{{MONO400_B64}}": "assets/fonts/ibm-plex-mono-latin-400.woff2",
    "{{MONO500_B64}}": "assets/fonts/ibm-plex-mono-latin-500.woff2",
    "{{LOGO_B64}}": "assets/logo.webp",
    "{{DK_BUILT_B64}}": "assets/dock/stuff-i-built.png",
    "{{DK_FREELANCE_B64}}": "assets/dock/freelance.png",
    "{{DK_BSIDES_B64}}": "assets/dock/b-sides.png",
    "{{DK_GITHUB_B64}}": "assets/dock/github.png",
}

# Folder pages, in dock order. Their text lives in content.md under "# Page: <slug>".
FOLDERS = ["stuff-i-built", "career", "b-sides"]

MIME = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
        ".webp": "image/webp", ".svg": "image/svg+xml"}

ICONS = {  # Lucide icons (ISC licence), used with `icon:` and {icon}
    "scan-text": '<path d="M3 7V5a2 2 0 0 1 2-2h2"/><path d="M17 3h2a2 2 0 0 1 2 2v2"/><path d="M21 17v2a2 2 0 0 1-2 2h-2"/><path d="M7 21H5a2 2 0 0 1-2-2v-2"/><path d="M7 8h8M7 12h10M7 16h6"/>',
    "briefcase": '<path d="M12 12h.01"/><path d="M16 6V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/><path d="M22 13a18.15 18.15 0 0 1-20 0"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
    "moon": '<path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/>',
    "heart-handshake": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/><path d="M12 5 9.04 7.96a2.17 2.17 0 0 0 0 3.08c.82.82 2.13.85 3 .07l2.07-1.9a2.82 2.82 0 0 1 3.79 0l2.96 2.66"/><path d="m18 15-2-2"/><path d="m15 18-2-2"/>',
    "sprout": '<path d="M7 20h10"/><path d="M10 20c5.5-2.5.8-6.4 3-10"/><path d="M9.5 9.4c1.1.8 1.8 2.2 2.3 3.7-2 .4-3.5.4-4.8-.3-1.2-.6-2.3-1.9-3-4.2 2.8-.5 4.4 0 5.5.8z"/><path d="M14.1 6a7 7 0 0 0-1.1 4c1.9-.1 3.3-.6 4.3-1.4 1-1 1.6-2.3 1.7-4.6-2.7.1-4 1-4.9 2z"/>',
    "hammer": '<path d="m15 12-8.373 8.373a1 1 0 1 1-3-3L12 9"/><path d="m18 15 4-4"/><path d="m21.5 11.5-1.914-1.914A2 2 0 0 1 19 8.172V7l-2.26-2.26a6 6 0 0 0-4.202-1.756L9 2.96l.92.82A6.18 6.18 0 0 1 12 8.4V10l2 2h1.172a2 2 0 0 1 1.414.586L18.5 14.5"/>',
}

NEW_TAB = {"en": " (opens in a new tab)", "fr": " (nouvel onglet)"}
BACK = ('<a class="back" href="{{ROOT}}" data-nav="home"><svg width="14" height="14" viewBox="0 0 24 24" '
        'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
        'aria-hidden="true"><path d="m12 19-7-7 7-7"/><path d="M19 12H5"/></svg>'
        '<span data-l="en">Back</span><span data-l="fr" lang="fr">Retour</span></a>')


class ContentError(SystemExit):
    pass


# ---------------------------------------------------------------- parsing

def parse(path):
    """content.md -> {"home": [...], "about": [...], "pages": {slug: {"fields": [...], "cards": [[...]]}}}"""
    text = re.sub(r"<!--.*?-->", "", path.read_text(encoding="utf-8"), flags=re.S)
    data = {"home": [], "about": [], "pages": {}}
    target = None
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("//"):
            continue
        if line.startswith("## "):
            if not isinstance(target, dict) or line[3:].strip().lower() != "card":
                raise ContentError(f"content.md line {n}: '## Card' must be inside a '# Page:' section")
            target["cards"].append([])
            continue
        if line.startswith("# "):
            title = line[2:].strip()
            low = title.lower()
            if low == "home":
                target = data["home"]
            elif low == "about":
                target = data["about"]
            elif low.startswith("page:"):
                slug = title.split(":", 1)[1].strip()
                if slug not in FOLDERS:
                    raise ContentError(f"content.md line {n}: unknown page '{slug}' (expected one of {', '.join(FOLDERS)})")
                target = data["pages"].setdefault(slug, {"fields": [], "cards": []})
            else:
                raise ContentError(f"content.md line {n}: unknown section '{title}'")
            continue
        m = re.match(r"^([a-z]+(?:\.(?:en|fr))?)\s*:\s*(.*)$", line)
        if not m:
            raise ContentError(f"content.md line {n}: expected 'key: value', got: {line[:60]}")
        if target is None:
            raise ContentError(f"content.md line {n}: field outside of a section")
        bucket = target if isinstance(target, list) else (target["cards"][-1] if target["cards"] else target["fields"])
        bucket.append((m.group(1), m.group(2).strip()))
    return data


def one(entries, key, required=False):
    """Single-value bilingual field -> {"en": ..., "fr": ...} (or None)."""
    vals = {}
    for k, v in entries:
        if k == key:
            vals.setdefault("en", v); vals.setdefault("fr", v)
        elif k == f"{key}.en":
            vals["en"] = v
        elif k == f"{key}.fr":
            vals["fr"] = v
    if not vals:
        if required:
            raise ContentError(f"content.md: missing '{key}'")
        return None
    vals.setdefault("en", vals.get("fr")); vals.setdefault("fr", vals.get("en"))
    return vals


def many(entries, key):
    """Repeated bilingual field (paragraphs) -> list of {"en","fr"} in order."""
    items = []
    for k, v in entries:
        if k == key:
            items.append({"en": v, "fr": v})
        elif k == f"{key}.en":
            items.append({"en": v, "fr": None})
        elif k == f"{key}.fr":
            for it in items:
                if it["fr"] is None:
                    it["fr"] = v
                    break
            else:
                items.append({"en": None, "fr": v})
    for it in items:
        it["en"] = it["en"] if it["en"] is not None else it["fr"]
        it["fr"] = it["fr"] if it["fr"] is not None else it["en"]
    return items


def raw(entries, key):
    for k, v in entries:
        if k == key:
            return v
    return None


# ---------------------------------------------------------------- rendering

def icon_svg(name, cls):
    if name not in ICONS:
        raise ContentError(f"content.md: unknown icon '{name}' (available: {', '.join(ICONS)})")
    return (f'<span class="{cls}" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg></span>')


# Tool logos: `{logo:slug|Name}` in content.md -> brand-coloured logo glued to the tool name.
# Files in assets/tools/<slug>.svg (Simple Icons, CC0; see assets/tools/NOTICE.md).
DARK_SURFACE = "#1E1B23"  # --surface in the dark theme (src/index.template.html)


def _luminance(hexv):
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (int(hexv.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def _contrast(a, b):
    la, lb = sorted((_luminance(a), _luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def tool_logo(m):
    slug, name = m.group(1), m.group(2).strip()
    d = ROOT / "assets" / "tools"
    png, f = d / f"{slug}.png", d / f"{slug}.svg"
    if png.exists() or (f.exists() and not re.search(r'<svg[^>]*\sfill="#', f.read_text(encoding="utf-8"))):
        # A full-colour icon (app icon, favicon) rather than a one-path brand mark: inline it as an image.
        src = png if png.exists() else f
        mime = "image/png" if src.suffix == ".png" else "image/svg+xml"
        uri = f"data:{mime};base64,{base64.b64encode(src.read_bytes()).decode('ascii')}"
        return f'<span class="tool"><img class="tool-logo" src="{uri}" alt="">{name}</span>'
    if not f.exists():
        raise ContentError(f"content.md: tool logo not found: assets/tools/{slug}.svg or .png")
    svg = f.read_text(encoding="utf-8")
    fill = re.search(r'fill="(#[0-9A-Fa-f]{6})"', svg).group(1)
    path = re.search(r'<path d="([^"]+)"', svg).group(1)
    # A near-black logo would vanish on the dark theme: it takes the text colour there instead.
    cls = "tool-logo lo" if _contrast(fill, DARK_SURFACE) < 2 else "tool-logo"
    return (f'<span class="tool"><svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true" '
            f'focusable="false" style="--brand:{fill}"><path d="{path}"/></svg>{name}</span>')


def fmt(text, lang, icon=None):
    """Inline formatting: escape, French spacing, **bold**, links, [placeholders], {icon}."""
    s = htmlmod.escape(text, quote=False)
    if lang == "fr":
        s = re.sub(r" ([:;?!»])", r"&nbsp;\1", s)
        s = s.replace("« ", "«&nbsp;")
        s = re.sub(r"(\d) (\d{3})\b", r"\1&nbsp;\2", s)
        s = re.sub(r"(\d) %", r"\1&nbsp;%", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)

    def link(m):
        label, url = m.group(1), m.group(2)
        if url.startswith("page:"):
            slug = url[5:]
            if slug not in FOLDERS + ["about"]:
                raise ContentError(f"content.md: link to unknown page '{slug}'")
            return f'<a href="{{{{ROOT}}}}{slug}/" data-nav="{slug}">{label}</a>'
        return (f'<a href="{url}" target="_blank" rel="noopener">{label}'
                f'<span class="sr">{NEW_TAB[lang]}</span></a>')

    s = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)
    s = re.sub(r"\[([^\]]+)\](?!\()", r'<span class="placeholder">[\1]</span>', s)
    s = re.sub(r"\{logo:([a-z0-9]+)\|([^}]+)\}", tool_logo, s)
    if "{icon}" in s:
        if not icon:
            raise ContentError("content.md: {icon} used but no 'icon:' set for this page")
        s = s.replace("{icon}", icon_svg(icon, "intro-icon"))
    return s


def inline(v, icon=None):
    """Bilingual inline content (inside an existing element)."""
    en, fr = fmt(v["en"], "en", icon), fmt(v["fr"], "fr", icon)
    if en == fr:
        return en
    return f'<span data-l="en">{en}</span><span data-l="fr" lang="fr">{fr}</span>'


def block(tag, attrs, v, icon=None):
    """Bilingual block: one element if identical, else one per language."""
    en, fr = fmt(v["en"], "en", icon), fmt(v["fr"], "fr", icon)
    a = f" {attrs}" if attrs else ""
    if en == fr:
        return f"<{tag}{a}>{en}</{tag}>"
    return f'<{tag}{a} data-l="en">{en}</{tag}>\n<{tag}{a} data-l="fr" lang="fr">{fr}</{tag}>'


def split_list(v):
    en = [x.strip() for x in v["en"].split("|")]
    fr = [x.strip() for x in v["fr"].split("|")]
    return en, fr


def image_uri(rel):
    f = ROOT / "assets" / rel
    if not f.exists():
        raise ContentError(f"content.md: image not found: assets/{rel}")
    return f"data:{MIME.get(f.suffix.lower(), 'application/octet-stream')};base64,{base64.b64encode(f.read_bytes()).decode('ascii')}"


def render_card(entries):
    compact = (raw(entries, "compact") or "").lower() in ("yes", "oui", "true", "1")
    logo = raw(entries, "logo")
    out = []
    tags = one(entries, "tags")
    if tags:
        en, fr = split_list(tags)
        if len(en) != len(fr):
            raise ContentError(f"content.md: tags.en and tags.fr must have the same number of items ({tags['en']})")
        lis = "".join(f'<li class="tag">{inline({"en": a, "fr": b})}</li>' for a, b in zip(en, fr))
        out.append(f'<ul class="tags" role="list">{lis}</ul>')
    title = one(entries, "title", required=True)
    out.append(f"<h2>{inline(title)}</h2>")
    for p in many(entries, "text"):
        out.append(block("p", 'class="tx"', p))
    facts = one(entries, "facts")
    if facts:
        en, fr = split_list(facts)
        ul = lambda items, lang: "".join(f"<li>{fmt(x, lang)}</li>" for x in items)
        if en == fr:
            out.append(f'<ul class="facts" role="list">{ul(en, "en")}</ul>')
        else:
            out.append(f'<ul class="facts" role="list" data-l="en">{ul(en, "en")}</ul>')
            out.append(f'<ul class="facts" role="list" data-l="fr" lang="fr">{ul(fr, "fr")}</ul>')
    for small in many(entries, "small"):  # repeat `small:` for several lines (e.g. stack, then links)
        out.append(block("p", 'class="small"', small))
    body = "\n".join(out)
    if logo:
        slug, _, initials = [x.strip() for x in logo.partition("|")]
        body = (f'<div class="card-body has-logo"><span class="co-logo" aria-hidden="true">'
                f'{{{{CO:{slug}:{initials or slug[:2].upper()}}}}}</span><div class="card-main">\n{body}\n</div></div>')
    else:
        body = f'<div class="card-body">\n{body}\n</div>'
    media = ""
    image = raw(entries, "image")
    if image:
        rel, _, url = [x.strip() for x in image.partition("|")]
        img = f'<img loading="lazy" src="{image_uri(rel)}" alt="">'
        media = (f'\n<a class="media" href="{url}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">{img}</a>'
                 if url else f'\n<div class="media">{img}</div>')
    cls = "card compact" if compact else "card"
    return f'<article class="{cls}">{body}{media}</article>'


def check_card_order(slug, page):
    """Cards dated in their first tag ("2023 – now", "2014 – 2016") must run most recent first."""
    prev = None
    for entries in page["cards"]:
        tags = one(entries, "tags")
        first = tags["en"].split("|")[0] if tags else ""
        years = re.findall(r"\b(?:19|20)\d{2}\b", first)
        if not years:
            continue  # undated card (project, toolkit): no constraint
        end = 9999 if re.search(r"\bnow\b", first) else int(years[-1])
        key = (end, int(years[0]))
        if prev and key > prev[0]:
            raise ContentError(f"content.md: page '{slug}': '{one(entries, 'title')['en']}' ({first.strip()}) "
                               f"must come before '{prev[1]}': cards run most recent first")
        prev = (key, one(entries, "title")["en"])


def render_folder(slug, page):
    f = page["fields"]
    title = one(f, "title", required=True)
    icon = raw(f, "icon")
    parts = [f'<!-- {title["en"]} -->',
             f'<div class="view" data-view="{slug}">',
             '<div class="page">',
             f'<h1 class="sr" id="page-title-{slug}" tabindex="-1">{inline(title)}</h1>',
             BACK]
    intro = one(f, "intro")
    if intro:
        parts.append(block("p", 'class="intro"', intro, icon))
    parts.append('<div class="cards">')
    parts += [render_card(c) for c in page["cards"]]
    parts.append("</div>")
    parts.append(f'<div class="bottom">{BACK}</div>')
    parts += ["</div>", "</div>", ""]
    return "\n".join(parts)


def render(data):
    home, about = data["home"], data["about"]
    missing = [s for s in FOLDERS if s not in data["pages"]]
    if missing:
        raise ContentError(f"content.md: missing page section(s): {', '.join(missing)}")
    for s in FOLDERS:
        check_card_order(s, data["pages"][s])

    name = raw(home, "name") or "William Pénet"
    head = one(home, "headline", required=True)
    h_en = [x.strip() for x in head["en"].split("|", 1)]
    h_fr = [x.strip() for x in head["fr"].split("|", 1)]
    line1 = inline({"en": h_en[0], "fr": h_fr[0]})
    line2 = inline({"en": h_en[1] if len(h_en) > 1 else "", "fr": h_fr[1] if len(h_fr) > 1 else ""})
    headline = (f'<span class="sr">{htmlmod.escape(name)}, </span>{line1} '
                f'{icon_svg("hammer", "hl-icon")}<br>{line2}')

    a_title = one(about, "title") or {"en": "About", "fr": "À propos"}
    about_h1 = f'<h1 class="sr" id="page-title-about" tabindex="-1">{inline(a_title)}</h1>'
    about_body = "\n".join(block("p", "", p) for p in many(about, "text"))

    titles = one(home, "title") or {"en": f"{name} — Senior Product Manager", "fr": f"{name} — Product Manager senior"}
    desc = one(home, "description") or {"en": "", "fr": ""}

    replacements = {
        "{{DESCRIPTION}}": htmlmod.escape(desc["en"], quote=True),
        "{{HOME_NAME}}": htmlmod.escape(name),
        "{{HOME_HEADLINE}}": headline,
        "{{ABOUT_H1}}": about_h1,
        "{{ABOUT_BODY}}": about_body,
        "{{FOLDER_VIEWS}}": "\n".join(render_folder(s, data["pages"][s]) for s in FOLDERS),
        "{{TITLE_HOME_EN_JS}}": json.dumps(titles["en"], ensure_ascii=False),
        "{{TITLE_HOME_FR_JS}}": json.dumps(titles["fr"], ensure_ascii=False),
    }
    # Dock badges: how many cards each folder holds, so nothing hides behind a folder icon.
    for s in FOLDERS:
        replacements["{{COUNT_" + s.upper().replace("-", "_") + "}}"] = str(len(data["pages"][s]["cards"]))
    page_titles = {"home": titles["en"], "about": f'{a_title["en"]} — {name}'}
    for s in FOLDERS:
        page_titles[s] = f'{one(data["pages"][s]["fields"], "title")["en"]} — {name}'
    return replacements, page_titles


def company_logo(match):
    slug, initials = match.group(1), match.group(2)
    for ext, mime in MIME.items():
        f = ROOT / "assets" / "companies" / f"{slug}{ext}"
        if f.exists():
            data = base64.b64encode(f.read_bytes()).decode("ascii")
            return f'<img src="data:{mime};base64,{data}" alt="">'
    print(f"  (no logo yet for {slug}: using initials)")
    return f'<span class="co-mono">{htmlmod.escape(initials)}</span>'


# ---------------------------------------------------------------- build

def main():
    content = parse(CONTENT)
    replacements, page_titles = render(content)

    html = TEMPLATE.read_text(encoding="utf-8")
    for token, value in replacements.items():
        html = html.replace(token, value)
    for token, rel in ASSETS.items():
        html = html.replace(token, base64.b64encode((ROOT / rel).read_bytes()).decode("ascii"))
    html = re.sub(r"\{\{CO:([a-z0-9-]+):([^}]+)\}\}", company_logo, html)

    for page, title in page_titles.items():
        is_home = page == "home"
        out = (
            html.replace("{{PAGE}}", page)
            .replace("{{ROOT}}", "./" if is_home else "../")
            .replace("{{TITLE}}", htmlmod.escape(title))
            .replace("{{HOME_HIDDEN}}", "" if is_home else ' inert aria-hidden="true"')
            .replace("{{SKIP_TARGET}}", "dock" if is_home else f"page-title-{page}")
        )
        left = re.findall(r"\{\{[A-Z0-9_:a-z-]+\}\}", out)
        if left:
            raise SystemExit(f"unsubstituted token(s) left in output ({page}): {', '.join(sorted(set(left)))}")
        target = ROOT / "index.html" if is_home else ROOT / page / "index.html"
        target.parent.mkdir(exist_ok=True)
        target.write_text(out, encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)} ({target.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
