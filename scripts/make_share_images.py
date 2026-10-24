#!/usr/bin/env python3
"""Generate the link-preview image and the icon files (dev-only, not run in CI).

Writes, from assets/logo.webp, the fonts in assets/ and the texts in content.md:
  assets/share/og-image.png        1200x630 Open Graph / X card image
  assets/share/icon-512.png        square icon (web manifest size, Google favicon >= 48 px)
  assets/share/apple-touch-icon.png  180x180

Needs Pillow and fontTools (+ brotli for woff2):
    pip install pillow fonttools brotli
    python3 scripts/make_share_images.py
"""
import io
import pathlib
import re

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "share"

# DESIGN.md tokens
CANVAS = "#F8F6F3"
INK = "#14121A"
BODY = "#4A4552"
MUTED = "#6B6472"
HAIRLINE = "#E4E0DB"
ACCENT = "#4A2244"


def ttf(rel):
    font = TTFont(ROOT / rel)
    font.flavor = None
    buf = io.BytesIO()
    font.save(buf)
    buf.seek(0)
    return buf


def sans(size, weight):
    f = ImageFont.truetype(ttf("assets/instrument-sans-latin.woff2"), size)
    f.set_variation_by_axes([weight])
    return f


def mono(size):
    return ImageFont.truetype(ttf("assets/fonts/ibm-plex-mono-latin-500.woff2"), size)


def home_field(key):
    text = (ROOT / "content.md").read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    home = text.split("# Home", 1)[1].split("\n# ", 1)[0]
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", home, flags=re.M)
    return m.group(1).strip() if m else None


def og_image(logo):
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), CANVAS)
    d = ImageDraw.Draw(img)
    pad = 80

    # Logo, top left
    lw = 230
    lg = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
    img.paste(lg, (pad - 8, pad - 10), lg)

    name = home_field("name") or "William Pénet"
    role = (home_field("title.en") or "").split("—", 1)[-1].strip() or "Senior Product Builder"
    url = home_field("url") or "williampenet.github.io/wip-portfolio"
    url = re.sub(r"^https?://", "", url).rstrip("/")

    y = 300
    d.text((pad, y), name, font=sans(92, 700), fill=INK)
    y += 112
    d.text((pad, y), role, font=sans(46, 600), fill=ACCENT)
    y += 66
    d.text((pad, y), "Ten years of product. I build things, with and without AI.", font=sans(30, 400), fill=BODY)

    d.line((pad, H - 70, W - pad, H - 70), fill=HAIRLINE, width=2)
    d.text((pad, H - 56), url, font=mono(22), fill=MUTED)
    return img


def square_icon(logo, size, bg=CANVAS):
    img = Image.new("RGB", (size, size), bg)
    inner = round(size * 0.84)
    lg = logo.copy()
    lg.thumbnail((inner, inner), Image.LANCZOS)
    img.paste(lg, ((size - lg.width) // 2, (size - lg.height) // 2), lg)
    return img


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    logo = Image.open(ROOT / "WiP - Logo.png").convert("RGBA")
    targets = {
        "og-image.png": og_image(logo),
        "icon-512.png": square_icon(logo, 512),
        "apple-touch-icon.png": square_icon(logo, 180),
    }
    for name, im in targets.items():
        p = OUT / name
        im.save(p, optimize=True)
        print(f"wrote {p.relative_to(ROOT)} {im.size[0]}x{im.size[1]} ({p.stat().st_size / 1024:.0f} KB)")


if __name__ == "__main__":
    main()
