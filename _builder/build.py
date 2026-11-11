#!/usr/bin/env python3
"""Static site builder for the Mayan Temple Adventures design site.

Usage:  python3 _builder/build.py [output_dir]

- Reads page content from _builder/pages/*.py (each defines PAGES = {path: page_dict})
- Converts images in _builder/images/originals/<ID>.<ext> into web-sized WebP files
- Writes plain HTML pages (no Jekyll, no framework) into the output folder
"""
import html
import importlib.util
import os
import shutil
import sys
import zlib
from pathlib import Path

from PIL import Image

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from site_map import NAV, all_paths  # noqa: E402

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parent
ORIGINALS = HERE / "images" / "originals"
IMG_OUT = OUT / "assets" / "img"

SITE_TITLE = "Mayan Temple Adventures"
SITE_TAGLINE = "A Mayan pyramid that rearranges itself around you."
AUTHOR = "Mike Stevanovic"
COPYRIGHT = "Mike Stevanovic"
YEAR = "2026"

FULL_MAX = 2400
THUMB_MAX = 960

IMAGES = {}  # id -> dict(w, h, tw, th)

LANGS = ("en", "de")
PREFIX = {"en": "", "de": "de/"}

UI = {
    "menu": ("Menu", "Menü"),
    "home": ("Home", "Start"),
    "prev": ("Previous", "Zurück"),
    "next": ("Next", "Weiter"),
    "skip": ("Skip to content", "Zum Inhalt springen"),
    "show_pages": ("Show {} pages", "Seiten unter {} anzeigen"),
    "image_coming": ("image coming", "Bild folgt"),
    "close": ("Close", "Schließen"),
    "prev_img": ("Previous image", "Vorheriges Bild"),
    "next_img": ("Next image", "Nächstes Bild"),
    "lang_label": ("Language", "Sprache"),
    "foot_by": ("Fortnite islands in design by {}. Planned in Unreal Editor for Fortnite (UEFN).",
                "Fortnite-Inseln in Entwicklung von {}. Geplant im Unreal Editor for Fortnite (UEFN)."),
    "foot_note": ("In development. All art shown is concept and design work, not in-engine capture.",
                  "In Entwicklung. Alle gezeigten Bilder sind Konzept- und Designarbeiten, keine Aufnahmen aus der Engine."),
    "rights": ("All rights reserved.", "Alle Rechte vorbehalten."),
    "trademark": ("Fortnite, Unreal Editor for Fortnite and Epic Games are trademarks of Epic Games, Inc. "
                  "This project is not affiliated with or endorsed by Epic Games.",
                  "Fortnite, Unreal Editor for Fortnite und Epic Games sind Marken von Epic Games, Inc. "
                  "Dieses Projekt steht in keiner Verbindung zu Epic Games und wird nicht von Epic Games unterstützt."),
    "stub_kicker": ("Coming soon", "Demnächst"),
    "stub_prep": ("In preparation", "In Vorbereitung"),
    "stub_text": ("This page is being written. Check back soon.",
                  "Diese Seite entsteht gerade. Schau bald wieder vorbei."),
    "tagline": ("A Mayan pyramid that rearranges itself around you.",
                "Eine Maya-Pyramide, die sich um dich herum neu ordnet."),
}


def tr(value, lang):
    """Resolve an (en, de) pair, or return a plain string unchanged."""
    if isinstance(value, (tuple, list)) and len(value) == 2 and all(isinstance(v, str) for v in value):
        return value[LANGS.index(lang)]
    return value


FLAG_US = ('<svg viewBox="0 0 60 32" aria-hidden="true"><rect width="60" height="32" fill="#B22234"/>'
           '<g fill="#fff">' + "".join(f'<rect y="{y:.2f}" width="60" height="2.46"/>' for y in [2.46*i for i in range(1, 13, 2)]) +
           '</g><rect width="26" height="17.2" fill="#3C3B6E"/>'
           '<g fill="#fff">' + "".join(f'<circle cx="{x}" cy="{y}" r="0.9"/>' for y in (3, 7, 11, 15) for x in (3, 8, 13, 18, 23)) +
           '</g></svg>')
FLAG_DE = ('<svg viewBox="0 0 60 32" aria-hidden="true"><rect width="60" height="10.67" fill="#000"/>'
           '<rect y="10.67" width="60" height="10.67" fill="#DD0000"/><rect y="21.33" width="60" height="10.67" fill="#FFCE00"/></svg>')


# ---------------------------------------------------------------- images
def process_images():
    (IMG_OUT / "full").mkdir(parents=True, exist_ok=True)
    (IMG_OUT / "thumb").mkdir(parents=True, exist_ok=True)
    for src in sorted(ORIGINALS.glob("*")):
        if src.suffix.lower() not in (".png", ".jpg", ".jpeg", ".webp"):
            continue
        img_id = src.stem.upper()
        full = IMG_OUT / "full" / f"{img_id}.webp"
        thumb = IMG_OUT / "thumb" / f"{img_id}.webp"
        is_logo = img_id.startswith("LOGO")
        with Image.open(src) as im:
            im.load()
            mode = "RGBA" if im.mode in ("RGBA", "LA", "P") else "RGB"
            im = im.convert(mode)
            fresh = full.exists() and full.stat().st_mtime >= src.stat().st_mtime
            if not fresh:
                f = im.copy()
                f.thumbnail((FULL_MAX, FULL_MAX), Image.LANCZOS)
                f.save(full, "WEBP", quality=88 if is_logo else 82, method=6)
                t = im.copy()
                t.thumbnail((THUMB_MAX, THUMB_MAX), Image.LANCZOS)
                t.save(thumb, "WEBP", quality=80, method=6)
            with Image.open(full) as f:
                w, h = f.size
            with Image.open(thumb) as t:
                tw, th = t.size
        IMAGES[img_id] = dict(w=w, h=h, tw=tw, th=th)
    # Images already converted in an earlier build (originals not kept in the repo)
    for full in sorted((IMG_OUT / "full").glob("*.webp")):
        img_id = full.stem.upper()
        thumb = IMG_OUT / "thumb" / full.name
        if img_id in IMAGES or not thumb.exists():
            continue
        with Image.open(full) as f, Image.open(thumb) as t:
            IMAGES[img_id] = dict(w=f.size[0], h=f.size[1], tw=t.size[0], th=t.size[1])


# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=True)


class Ctx:
    """Per-page context: knows how deep the page is so links stay relative."""

    def __init__(self, path, lang="en"):
        self.path = path            # logical page path, same in every language
        self.lang = lang
        self.out_path = PREFIX[lang] + path
        self.root = "../" * self.out_path.count("/")

    def t(self, en, de):
        return de if self.lang == "de" else en

    def ui(self, key, *args):
        text = tr(UI[key], self.lang)
        return text.format(*args) if args else text

    def url(self, target):
        """Link to another page in the current language."""
        return self.root + PREFIX[self.lang] + target

    def asset(self, target):
        """Link to a shared file (css, js, images, favicon)."""
        return self.root + target

    def lang_url(self, lang):
        return self.root + PREFIX[lang] + self.path

    @staticmethod
    def swap(img_id):
        """An action shot saved as ACT-<id> replaces the sheet <id> everywhere it is used."""
        act = "ACT-" + img_id.upper()
        return act if act in IMAGES else img_id

    def img_src(self, img_id, kind="thumb"):
        return f"{self.root}assets/img/{kind}/{self.swap(img_id)}.webp"

    def has(self, img_id):
        return img_id.upper() in IMAGES

    def pick(self, *ids):
        """First image id that has been uploaded; falls back to the first id (placeholder)."""
        for i in ids:
            if i.upper() in IMAGES:
                return i
        return ids[0]

    def figure(self, img_id, caption=None, alt=None, cls="", eager=False, link=True, show_caption=True):
        img_id = self.swap(img_id.upper())
        alt = alt or caption or img_id
        cap = f"<figcaption>{caption}</figcaption>" if caption and show_caption else ""
        if img_id in IMAGES:
            m = IMAGES[img_id]
            loading = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
            tag = (f'<img src="{self.img_src(img_id)}" alt="{esc(alt)}" width="{m["tw"]}" '
                   f'height="{m["th"]}" {loading}>')
            if link:
                tag = (f'<a class="lb" href="{self.img_src(img_id, "full")}" '
                       f'data-caption="{esc(caption or "")}">{tag}</a>')
            return f'<figure class="fig {cls}">{tag}{cap}</figure>'
        return (
            f'<figure class="fig ph {cls}"><div class="ph-box" role="img" aria-label="{esc(alt)}">'
            f'<span class="ph-id">{img_id}</span><span class="ph-note">{self.ui("image_coming")}</span></div>{cap}</figure>'
        )

    def gallery(self, items, cls=""):
        figs = "".join(self.figure(i, c) for i, c in items)
        return f'<div class="gallery {cls}">{figs}</div>'

    def bg(self, img_id):
        img_id = self.swap(img_id.upper())
        if img_id in IMAGES:
            return f"background-image:url('{self.img_src(img_id, 'full')}')"
        return ""


# ---------------------------------------------------------------- nav
def nav_html(ctx):
    current = ctx.path

    def contains(node):
        label, path, kids = node
        return path == current or any(contains(k) for k in kids)

    def item(node, level, idx):
        label, path, kids = node
        label = tr(label, ctx.lang)
        active = " is-active" if contains(node) else ""
        cur = ' aria-current="page"' if path == current else ""
        if not kids:
            return f'<li class="nav-item{active}"><a href="{ctx.url(path)}"{cur}>{esc(label)}</a></li>'
        sub_id = f"sub-{level}-{idx}-{zlib.crc32(label.encode()) % 99999}"
        sub = "".join(item(k, level + 1, i) for i, k in enumerate(kids))
        return (
            f'<li class="nav-item has-sub level-{level}{active}">'
            f'<div class="nav-row"><a href="{ctx.url(path)}"{cur}>{esc(label)}</a>'
            f'<button class="sub-toggle" aria-expanded="false" aria-controls="{sub_id}" '
            f'aria-label="{esc(ctx.ui('show_pages', label))}"><span class="chev" aria-hidden="true"></span></button></div>'
            f'<ul class="sub" id="{sub_id}">{sub}</ul></li>'
        )

    items = "".join(item(n, 0, i) for i, n in enumerate(NAV))
    logo = (
        f'<img src="{ctx.img_src("LOGO", "thumb")}" alt="{esc(SITE_TITLE)}" class="brand-logo">'
        if "LOGO" in IMAGES
        else f'<span class="brand-text">{esc(SITE_TITLE)}</span>'
    )
    langs = "".join(
        f'<a href="{ctx.lang_url(l)}" hreflang="{l}" lang="{l}" class="lang-link{" is-current" if l == ctx.lang else ""}"'
        f'{" aria-current=\"true\"" if l == ctx.lang else ""} title="{name}">{flag}<span class="sr">{name}</span></a>'
        for l, name, flag in (("en", "English", FLAG_US), ("de", "Deutsch", FLAG_DE)))
    return f"""
<header class="site-header">
  <div class="bar">
    <a class="brand" href="{ctx.url('index.html')}">{logo}</a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="main-nav">
      <span class="burger" aria-hidden="true"></span><span class="menu-label">{ctx.ui("menu")}</span></button>
    <nav id="main-nav" class="main-nav" aria-label="Main"><ul class="nav-list">{items}</ul></nav>
    <div class="lang-switch" role="group" aria-label="{ctx.ui("lang_label")}">{langs}</div>
  </div>
</header>"""


def pager(ctx):
    paths = all_paths()
    idx = [p for p, _ in paths].index(ctx.path) if ctx.path in [p for p, _ in paths] else -1
    if idx < 0:
        return ""
    prev_ = paths[idx - 1] if idx > 0 else None
    next_ = paths[idx + 1] if idx + 1 < len(paths) else None
    a = (f'<a class="prev" href="{ctx.url(prev_[0])}"><small>{ctx.ui("prev")}</small>{esc(tr(prev_[1][-1], ctx.lang))}</a>'
         if prev_ else "<span></span>")
    b = (f'<a class="next" href="{ctx.url(next_[0])}"><small>{ctx.ui("next")}</small>{esc(tr(next_[1][-1], ctx.lang))}</a>'
         if next_ else "<span></span>")
    return f'<nav class="pager" aria-label="Page">{a}{b}</nav>'


def footer(ctx):
    return f"""
<footer class="site-footer">
  <div class="wrap foot">
    <div>
      <p class="foot-title">{esc(SITE_TITLE)}</p>
      <p>{esc(ctx.ui("foot_by", AUTHOR))}</p>
    </div>
    <p class="foot-note">{ctx.ui("foot_note")}<br>
    © {YEAR} {esc(COPYRIGHT)}. {ctx.ui("rights")}<br>
    {ctx.ui("trademark")}</p>
  </div>
</footer>"""


def crumbs(ctx, trail):
    if ctx.path == "index.html" or len(trail) < 2:
        return ""
    parts = [f'<a href="{ctx.url("index.html")}">{ctx.ui("home")}</a>'] + [esc(tr(t, ctx.lang)) for t in trail[:-1]]
    return f'<p class="crumbs">{" / ".join(parts)}</p>'


def first_uploaded(ids):
    """A page's banner/og may be one image id or a list of candidates; use the first one uploaded.
    A single id is returned as-is even when missing, so existing pages behave exactly as before."""
    if isinstance(ids, (list, tuple)):
        return next((i for i in ids if i.upper() in IMAGES), None)
    return ids


def page_shell(ctx, page, trail):
    L = ctx.lang
    title = tr(page["title"], L)
    full_title = SITE_TITLE if ctx.path == "index.html" else f"{title} · {SITE_TITLE}"
    desc = tr(page.get("description", UI["tagline"]), L)
    og = first_uploaded(page.get("og", "A-01")) or ""
    og_tag = (f'<meta property="og:image" content="{ctx.img_src(og.upper(), "full")}">'
              if og.upper() in IMAGES else "")
    body = page["body"](ctx)
    header_block = ""
    if not page.get("custom_header"):
        kicker = f'<p class="kicker">{esc(tr(page["kicker"], L))}</p>' if page.get("kicker") else ""
        lede = f'<p class="lede">{tr(page["lede"], L)}</p>' if page.get("lede") else ""
        bgimg = first_uploaded(page.get("banner"))
        if page.get("banner_full") and bgimg and ctx.has(bgimg):
            # whole picture, never cropped; the heading sits over its lower fade
            m = IMAGES[ctx.swap(bgimg.upper())]
            header_block = f"""
<section class="page-head page-head-art">
  <div class="page-head-frame"><img src="{ctx.img_src(bgimg.upper(), 'full')}" alt="" width="{m['w']}" height="{m['h']}" fetchpriority="high"></div>
  <div class="wrap page-head-text">{crumbs(ctx, trail)}{kicker}<h1>{esc(title)}</h1>{lede}</div>
</section>"""
        else:
            style = f' style="{ctx.bg(bgimg)}"' if bgimg and ctx.has(bgimg) else ""
            cls = " has-bg" if style else ""
            header_block = f"""
<section class="page-head{cls}"{style}><div class="wrap">
  {crumbs(ctx, trail)}{kicker}<h1>{esc(title)}</h1>{lede}
</div></section>"""
    return f"""<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'de_DE' if L == 'de' else 'en_US'}">
<link rel="alternate" hreflang="en" href="{ctx.lang_url('en')}">
<link rel="alternate" hreflang="de" href="{ctx.lang_url('de')}">
{og_tag}
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0D2621">
<link rel="icon" href="{ctx.asset('favicon.svg')}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,400..800&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{ctx.asset('assets/css/site.css')}">
</head>
<body class="page-{ctx.path.replace('/', '-').replace('.html', '')}">
<a class="skip" href="#main">{ctx.ui("skip")}</a>
{nav_html(ctx)}
<main id="main">
{header_block}
{body}
<div class="wrap">{pager(ctx) if not page.get("no_pager") else ""}</div>
</main>
{footer(ctx)}
<div class="lightbox" hidden><button class="lb-close" aria-label="{ctx.ui('close')}">×</button>
<button class="lb-prev" aria-label="{ctx.ui('prev_img')}">‹</button><button class="lb-next" aria-label="{ctx.ui('next_img')}">›</button>
<figure><img alt=""><figcaption></figcaption></figure></div>
<script src="{ctx.asset('assets/js/site.js')}" defer></script>
</body>
</html>"""


# ---------------------------------------------------------------- pages
def load_pages():
    pages = {}
    for f in sorted((HERE / "pages").glob("*.py")):
        spec = importlib.util.spec_from_file_location(f.stem, f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        pages.update(getattr(mod, "PAGES", {}))
    return pages


def stub(title):
    def body(ctx):
        return (f'<section class="wrap section"><div class="stub"><p class="kicker">{ctx.ui("stub_prep")}</p>'
                f'<h2>{esc(tr(title, ctx.lang))}</h2><p>{ctx.ui("stub_text")}</p></div></section>')
    return dict(title=title, body=body, kicker=UI["stub_kicker"])


def favicon_svg():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
            '<rect width="64" height="64" rx="12" fill="#070B10"/>'
            '<path d="M8 52h48l-6-8H14z M14 44h36l-5-7H19z M19 37h26l-4-7H23z M23 30h18l-4-7H27z" fill="#EFE6CE"/>'
            '<circle cx="32" cy="15" r="6" fill="#F0B24A"/></svg>')


def main():
    process_images()
    pages = load_pages()
    for d in ("css", "js", "media"):
        dst = OUT / "assets" / d
        dst.mkdir(parents=True, exist_ok=True)
        for f in (HERE / "static" / d).glob("*"):
            shutil.copy2(f, dst / f.name)
    (OUT / "favicon.svg").write_text(favicon_svg())
    (OUT / ".nojekyll").write_text("")
    built = 0
    for lang in LANGS:
        for path, trail in all_paths():
            page = pages.get(path) or stub(trail[-1])
            ctx = Ctx(path, lang)
            target = OUT / ctx.out_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(page_shell(ctx, page, trail), encoding="utf-8")
            built += 1
    print(f"Built {built} pages, {len(IMAGES)} images -> {OUT}")


if __name__ == "__main__":
    main()
