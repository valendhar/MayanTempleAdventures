"""The Likeness: chapters of the short story as book-style reading pages (English and German).

Chapter text lives in _builder/story/chapter-<n>.<lang>.md:
  - the first line is "# Chapter 1 : Title"
  - paragraphs are separated by blank lines
  - *text* is italic (Kaya's notebook entries)
A chapter appears on the site as soon as its English file exists. Without a German file, the German page shows the English text.
"""
import html
import re
from pathlib import Path

STORY = Path(__file__).resolve().parent.parent / "story"
WORDS_PER_MINUTE = 230

# number, (en, de) title; matches the outline on story/short-story.html
CHAPTERS = [
    (1, ("The Overlooked Find", "Der übersehene Fund")),
    (2, ("Reading Between the Layers", "Zwischen den Schichten lesen")),
    (3, ("The Confrontation in the Dust", "Die Konfrontation im Staub")),
    (4, ("What the Ground Remembers", "Woran sich der Boden erinnert")),
]
NUMBER_WORDS = {"en": ["One", "Two", "Three", "Four"], "de": ["Eins", "Zwei", "Drei", "Vier"]}


def chapter_path(n):
    return f"story/chapter-{n}.html"


def source(n, lang):
    f = STORY / f"chapter-{n}.{lang}.md"
    if not f.exists() and lang != "en":
        f = STORY / f"chapter-{n}.en.md"
    return f if f.exists() else None


def available():
    return [n for n, _ in CHAPTERS if source(n, "en")]


def typeset(text, lang):
    """Escape, then book typography: curly quotes, ellipses, italics."""
    s = html.escape(text, quote=False)
    s = re.sub(r"\s+,", ",", s)                       # stray space before a comma
    s = s.replace("...", "…")
    if lang == "en":
        s = re.sub(r'(^|[\s(\[—–-])"', "\\1“", s)     # opening double quote
        s = s.replace('"', "”")
    s = s.replace("'", "’")
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def parse(n, lang):
    raw = source(n, lang).read_text(encoding="utf-8").strip()
    blocks = [b.strip() for b in re.split(r"\n\s*\n", raw) if b.strip()]
    if blocks and blocks[0].startswith("#"):
        blocks = blocks[1:]                             # title comes from CHAPTERS
    paras = [" ".join(b.split()) for b in blocks]
    words = sum(len(p.split()) for p in paras)
    return paras, words


def chapter_body(n):
    def body(ctx):
        t, u, L = ctx.t, ctx.url, ctx.lang
        title = ctx.t(*dict(CHAPTERS)[n])
        paras, words = parse(n, L)
        minutes = max(1, round(words / WORDS_PER_MINUTE))
        text = "".join(f"<p>{typeset(p, L)}</p>" for p in paras)
        fallback = ""
        if L == "de" and not (STORY / f"chapter-{n}.de.md").exists():
            fallback = '<p class="reader-note">Dieses Kapitel gibt es bisher nur auf Englisch.</p>'

        later = [(m, ttl) for m, ttl in CHAPTERS if m > n]
        if later:
            m, ttl = later[0]
            if m in available():
                nxt = (f'<a class="reader-next" href="{u(chapter_path(m))}"><span>{t("Next chapter", "Nächstes Kapitel")}</span>'
                       f'{t("Chapter", "Kapitel")} {m}: {t(*ttl)}</a>')
            else:
                nxt = (f'<p class="reader-next is-soon"><span>{t("Next chapter", "Nächstes Kapitel")}</span>'
                       f'{t("Chapter", "Kapitel")} {m}: {t(*ttl)} · {t("coming soon", "folgt bald")}</p>')
        else:
            nxt = f'<p class="reader-next is-soon"><span>{t("The end", "Ende")}</span>{t("The Likeness", "Das Abbild")}</p>'

        return f"""
<div class="reader-progress" aria-hidden="true"><span></span></div>
<article class="reader" data-reader lang="{L}">
  <div class="reader-tools" role="group" aria-label="{t('Reading settings', 'Leseeinstellungen')}">
    <a class="reader-back" href="{u('story/short-story.html')}">{t("The Likeness", "Das Abbild")}</a>
    <span class="reader-tool-group">
      <button type="button" data-size="-1" aria-label="{t('Smaller text', 'Kleinere Schrift')}">A<sup>−</sup></button>
      <button type="button" data-size="1" aria-label="{t('Larger text', 'Größere Schrift')}">A<sup>+</sup></button>
      <button type="button" data-theme-toggle aria-pressed="false">{t("Night", "Nacht")}</button>
    </span>
  </div>
  <header class="reader-head">
    <p class="reader-series">{t("The Likeness", "Das Abbild")}</p>
    <p class="reader-num">{t("Chapter", "Kapitel")} {NUMBER_WORDS[L][n - 1]}</p>
    <h1>{html.escape(title)}</h1>
    <p class="reader-meta">{t(f"About {minutes} minutes to read", f"Etwa {minutes} Minuten Lesezeit")}</p>
    <span class="reader-ornament" aria-hidden="true"></span>
  </header>
  <div class="reader-text">{fallback}{text}</div>
  <footer class="reader-end">
    <span class="reader-ornament" aria-hidden="true"></span>
    <p class="reader-fin">{t(f"End of Chapter {n}", f"Ende von Kapitel {n}")}</p>
    {nxt}
    <a class="text-link" href="{u('story/short-story.html')}">{t("About the story and all chapters", "Über die Geschichte und alle Kapitel")}</a>
  </footer>
</article>
"""
    return body


PAGES = {}
for _n in available():
    _en, _de = dict(CHAPTERS)[_n]
    PAGES[chapter_path(_n)] = dict(
        title=(f"Chapter {_n} · {_en}", f"Kapitel {_n} · {_de}"),
        description=(f"The Likeness, Chapter {_n}: {_en}. A short story set in the Sun Temple.",
                     f"Das Abbild, Kapitel {_n}: {_de}. Eine Kurzgeschichte aus dem Sonnentempel."),
        body=chapter_body(_n), custom_header=True, no_pager=True, og="HUB09")
