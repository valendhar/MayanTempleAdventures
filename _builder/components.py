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


def room(ctx, code, name, text, scene, map_id, codex_id, tag_pairs=(), flip=False, extra=None):
    """One room of a floor: scene beside the text, with its codex page and top-down map underneath the text.
    text: list of (en, de) paragraphs. extra: optional (image_id, caption) shown only once uploaded."""
    t = ctx.t
    nm = T(ctx, name)
    paras = "".join(f"<p>{T(ctx, p)}</p>" for p in text)
    extra_html = ""
    if extra and ctx.has(extra[0]):
        extra_html = f'<div class="room-extra">{ctx.figure(extra[0], T(ctx, extra[1]))}</div>'
    drawings = (f'<div class="room-drawings">{ctx.figure(codex_id, t("Codex page", "Codexseite"), cls="codex")}'
                f'{ctx.figure(map_id, t("From above", "Draufsicht"), cls="map")}</div>')
    return (f'<article class="room{" flip" if flip else ""}" id="{code.lower()}">'
            f'<div class="room-scene">{ctx.figure(scene, alt=nm)}</div>'
            f'<div class="room-body"><p class="room-code">{code}</p><h3>{nm}</h3>{tags(ctx, tag_pairs)}{paras}{drawings}</div>'
            f'{extra_html}</article>')
