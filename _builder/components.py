"""Shared building blocks for page modules."""


def feature(ctx, img, kicker, title, text, flip=False, caption=None):
    """Image beside a text block; flip puts the image on the right."""
    cls = " flip" if flip else ""
    k = f'<p class="kicker">{kicker}</p>' if kicker else ""
    return (f'<div class="feature{cls}"><div class="feature-media">{ctx.figure(img, caption, alt=title)}</div>'
            f'<div class="feature-text">{k}<h3>{title}</h3>{text}</div></div>')


def pair(ctx, a, cap_a, b, cap_b):
    """Two images side by side with captions."""
    return f'<div class="pair">{ctx.figure(a, cap_a)}{ctx.figure(b, cap_b)}</div>'


def facts(rows):
    return '<dl class="facts">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def T(ctx, v):
    """Resolve an (en, de) pair for the current page language; plain strings pass through."""
    return ctx.t(*v) if isinstance(v, (tuple, list)) else v


def tags(ctx, pairs):
    """Small outlined labels, e.g. what a room teaches."""
    if not pairs:
        return ""
    return '<p class="tags">' + "".join(f"<span>{T(ctx, p)}</span>" for p in pairs) + "</p>"


def catalog(ctx, rows, cls=""):
    """Asset sheets as a grid: picture (shown whole), ID, name and one line.
    rows: (image_id, name, line) with name/line as (en, de) pairs; line may be None."""
    items = []
    for img, name, line in rows:
        nm = T(ctx, name)
        ln = f"<p>{T(ctx, line)}</p>" if line else ""
        items.append(f'<article class="cat-item">{ctx.figure(img, alt=nm, cls="cat-fig")}'
                     f'<p class="cat-id">{img}</p><h3>{nm}</h3>{ln}</article>')
    return f'<div class="catalog {cls}">{"".join(items)}</div>'


def run_strip(ctx, screens, label, start=1):
    """The side-scrolling strip: 16:9 side-view screens laid edge to edge like one level, read left to right,
    with a gold route line and the screen numbers under them.
    screens: (image_id or list of ids to pick from, (en, de) name)."""
    items = []
    for n, (img, name) in enumerate(screens, start):
        img = ctx.pick(*img) if isinstance(img, (list, tuple)) else img
        nm = T(ctx, name)
        items.append(f'<li class="strip-screen">{ctx.figure(img, alt=nm)}'
                     f'<p class="strip-cap"><span class="strip-num">{n:02d}</span>{nm}</p></li>')
    t = ctx.t
    return (f'<div class="strip" data-strip>'
            f'<div class="strip-view" role="region" aria-label="{label}" tabindex="0"><ol class="strip-track">{"".join(items)}</ol></div>'
            f'<div class="strip-controls"><button type="button" class="strip-btn" data-dir="-1" aria-label="{t("Scroll left", "Nach links")}">'
            f'<span aria-hidden="true">&#8249;</span></button><button type="button" class="strip-btn" data-dir="1" '
            f'aria-label="{t("Scroll right", "Nach rechts")}"><span aria-hidden="true">&#8250;</span></button></div></div>')


SHAPE_NAMES = {"H": ("Horizontal", "Waagerecht"), "V": ("Vertical", "Senkrecht"), "D": ("Diagonal, rising", "Diagonal, steigend"),
               "R": ("Ring around a well", "Ring um einen Brunnen"), "A": ("Arena", "Arena")}


def shape_glyph(ctx, code):
    """A small drawn sign for a floor's shape: the direction the level runs in side view.
    code: H, V, D, R or A, or two joined by '>' (e.g. 'H>V': runs across, then climbs)."""
    paths = {
        "H": '<path d="M3 12h16M15 8l4 4-4 4"/>',
        "V": '<path d="M12 21V5M8 9l4-4 4 4"/>',
        "D": '<path d="M4 20L19 5M12 5h7v7"/>',
        "R": '<circle cx="12" cy="12" r="7"/><path d="M12 5v14"/>',
        "A": '<rect x="4" y="7" width="16" height="11" rx="1"/><path d="M8 18v-4M16 18v-4"/>',
    }
    parts = code.split(">")
    svgs = "".join(f'<svg viewBox="0 0 24 24" aria-hidden="true">{paths[p]}</svg>' for p in parts)
    name = ctx.t(" then ", ", dann ").join(T(ctx, SHAPE_NAMES[p]) for p in parts)
    return f'<span class="shape" title="{name}">{svgs}<span class="sr-only">{name}</span></span>'


def room(ctx, code, name, text, scene, map_id=None, codex_id=None, tag_pairs=(), flip=False, extra=None):
    """One room of a floor: its scene beside the text. (Top-down maps and codex plans were retired with the 3D design;
    map_id and codex_id are accepted and ignored.)
    text: list of (en, de) paragraphs. extra: optional (image_id, caption), or a list of them, shown only once uploaded."""
    t = ctx.t
    nm = T(ctx, name)
    paras = "".join(f"<p>{T(ctx, p)}</p>" for p in text)
    extras = [e for e in (extra if isinstance(extra, list) else [extra]) if e and ctx.has(e[0])]
    extra_html = ""
    if len(extras) == 1:
        extra_html = f'<div class="room-extra">{ctx.figure(extras[0][0], T(ctx, extras[0][1]))}</div>'
    elif extras:
        extra_html = f'<div class="room-extra">{ctx.gallery([(i, T(ctx, c)) for i, c in extras], cls="gallery-3")}</div>'
    drawings = ""
    return (f'<article class="room{" flip" if flip else ""}" id="{code.lower()}">'
            f'<div class="room-scene">{ctx.figure(scene, alt=nm)}</div>'
            f'<div class="room-body"><p class="room-code">{code}</p><h3>{nm}</h3>{tags(ctx, tag_pairs)}{paras}{drawings}</div>'
            f'{extra_html}</article>')
