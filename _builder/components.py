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
