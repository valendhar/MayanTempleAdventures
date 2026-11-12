"""Climbing together: the co-op crew art, kept as a possible future mode (12 Nov 2026).

The game is single-player: Kaya climbs alone. The paintings of Kaya climbing with a crew were made for the earlier UEFN
co-op design; they stay on the site as concept art for a co-op mode that might come later, never as the solo game.

- CREW_BANDS: page path -> crew images shown at the end of that page in one "Climbing together" band (rope line on top,
  jade-framed images, a link to the page below). One place for every placement, so co-op can grow or vanish in one edit.
- PAGES: game/climbing-together.html, the page that gathers all of it.
Crew images are listed in build.py (CREW) and are never chosen automatically; only these two places name them.
"""
from components import T


# Captions describe what each painting shows.
CAP = {
    "ACT-CS-KAYA": ("Kaya copies a carving while the crew holds the guardians back",
                    "Kaya kopiert ein Relief, während die Gruppe die Wächter zurückhält"),
    "ACT-CS-KIN": ("K'in's light leads the crew through a collapsing hall",
                   "K'ins Licht führt die Gruppe durch eine einstürzende Halle"),
    "ACT-W07": ("The crew around K'in's flame at the round altar", "Die Gruppe um K'ins Flamme am runden Altar"),
    "ACT-CS-OXLAHUN": ("Oxlahun's table, with the whole crew bargaining", "Oxlahuns Tisch, die ganze Gruppe feilscht mit"),
    "ACT-CS-AHKUK": ("Ah Kuk stirs on the stair as the crew creeps past", "Ah Kuk regt sich auf der Treppe, die Gruppe schleicht vorbei"),
    "ACT-CS-IXNICTE": ("Ix Nicte in the flooded hall, and a climber wading closer",
                       "Ix Nicte in der überfluteten Halle, ein Kletterer watet näher"),
    "ACT-CS-CHAKTUN": ("A climber with a lantern under Chak Tun's relief", "Ein Kletterer mit Laterne unter Chak Tuns Relief"),
    "ACT-CS-GUARDIAN": ("The crew against a pack of risen guardians", "Die Gruppe gegen einen Trupp erweckter Wächter"),
    "ACT-CS-PRIEST": ("The crew faces the Hollow High Priest", "Die Gruppe stellt sich dem Hohlen Hohepriester"),
    "ACT-CS-LINEUP": ("The crew lined up in the Threshold", "Die Gruppe aufgereiht in der Schwelle"),
    "HYB-SCENE1": ("The Breathing Court: freeze when the faces look", "Der atmende Hof: erstarren, wenn die Gesichter schauen"),
    "HYB-SCENE2": ("The Spike Court", "Der Stachelhof"),
    "HYB-SCENE3": ("The Great Idol", "Das Große Idol"),
    "HYB-SCENE4": ("The Serpent Run", "Der Schlangenlauf"),
    "ISL-ASCENT": ("Up the great stair beneath the carved walls", "Die große Treppe hinauf, unter den gemeißelten Wänden"),
    "ISL-TRAPS": ("A trap gallery run between saws and gears", "Ein Lauf durch die Fallengalerie zwischen Sägen und Zahnrädern"),
    "ISL-RAIDERS": ("Racing each other for an orb", "Ein Wettlauf um eine Kugel"),
    "ISL-DEPTHS": ("Turning mirrors to steer the light", "Spiegel drehen, um das Licht zu lenken"),
    "ISL-DIG": ("The dig camp at the foot of the pyramid", "Das Grabungslager am Fuß der Pyramide"),
}

CREW_BANDS = {
    "index.html": ["ISL-DEPTHS", "HYB-SCENE2", "ACT-CS-LINEUP"],
    "characters/kaya.html": ["ACT-CS-KAYA"],
    "characters/kin.html": ["ACT-CS-KIN", "ACT-W07"],
    "characters/oxlahun.html": ["ACT-CS-OXLAHUN"],
    "characters/guardians/index.html": ["ACT-CS-GUARDIAN"],
    "characters/guardians/ah-kuk.html": ["ACT-CS-AHKUK"],
    "characters/guardians/ix-nicte.html": ["ACT-CS-IXNICTE"],
    "characters/guardians/chak-tun.html": ["ACT-CS-CHAKTUN"],
    "characters/hollow-high-priest.html": ["ACT-CS-PRIEST"],
    "characters/lineup.html": ["ACT-CS-LINEUP"],
    "climb/threshold.html": ["ISL-ASCENT"],
    "climb/tier-2.html": ["HYB-SCENE1", "HYB-SCENE2", "HYB-SCENE3", "HYB-SCENE4", "ISL-TRAPS"],
    "climb/tier-4.html": ["ISL-RAIDERS"],
    "climb/tier-5.html": ["ISL-DEPTHS"],
    "world/index.html": ["ISL-DIG"],
}

# The island prototype's thumbnails (the temple as five Fortnite islands, Nov 2026), shown once as history.
PROTOTYPE = [("THUMB-ASCENT", "Ascent of the Sun Temple"), ("THUMB-TRAPS", "Trap Galleries"),
             ("THUMB-RAIDERS", "Orb Raiders"), ("THUMB-DEPTHS", "Illusion Depths"), ("THUMB-DIG", "Sun Temple Dig")]


def _fig(ctx, img, cls="crew-fig"):
    return ctx.figure(img, T(ctx, CAP[img]), cls=cls)


def crew_band(ctx):
    """The band at the end of a page that has crew art, or nothing."""
    imgs = [i for i in CREW_BANDS.get(ctx.path, []) if ctx.exists(i)]
    if not imgs or ctx.path == "game/climbing-together.html":
        return ""
    t = ctx.t
    n = {2: 2, 4: 2}.get(len(imgs), 3)   # four images as two by two, otherwise up to three across
    single = len(imgs) == 1
    text = t("Ascent of the Sun Temple is played alone. These paintings show an idea for later: friends climbing with "
             "Kaya.",
             "Ascent of the Sun Temple spielt man allein. Diese Bilder zeigen eine Idee für später: Freunde, die mit "
             "Kaya klettern.")
    link = f'<a class="text-link" href="{ctx.url("game/climbing-together.html")}">{t("Climbing together", "Gemeinsam klettern")}</a>'
    head = (f'<div class="crew-head"><p class="kicker">{t("Co-op concept", "Koop-Konzept")}</p>'
            f'<h2>{t("Not always alone", "Nicht immer allein")}</h2><p>{text}</p><p>{link}</p></div>')
    figs = "".join(_fig(ctx, i) for i in imgs)
    layout = "crew-one" if single else f"crew-grid crew-cols-{n}"
    return f'<section class="crew-band"><div class="wrap">{head}<div class="{layout}">{figs}</div></div></section>'


def climbing_together(ctx):
    t = ctx.t
    have = lambda ids: [i for i in ids if ctx.exists(i)]   # noqa: E731
    floors = have(["HYB-SCENE1", "HYB-SCENE2", "HYB-SCENE3", "HYB-SCENE4", "ISL-TRAPS", "ISL-RAIDERS", "ISL-DEPTHS",
                   "ISL-DIG"])
    cast = have(["ACT-CS-KAYA", "ACT-CS-KIN", "ACT-W07", "ACT-CS-OXLAHUN", "ACT-CS-GUARDIAN", "ACT-CS-AHKUK",
                 "ACT-CS-IXNICTE", "ACT-CS-CHAKTUN", "ACT-CS-PRIEST"])
    proto = [(i, n) for i, n in PROTOTYPE if ctx.exists(i)]
    ideas = [
        (t("The wall carves everyone", "Die Wand meißelt alle"),
         t("The Spirit Mural already keeps a panel for every climber who fell. With friends, each of them would get "
           "their own, next to Kaya's.",
           "Das Geisterwandbild hält schon für jeden gefallenen Kletterer eine Tafel fest. Mit Freunden bekäme jeder "
           "seine eigene, neben Kayas.")),
        (t("Kaya still reads", "Kaya liest weiter"),
         t("The goggles, the notebook and the reading stay hers. Friends would carry, guard and climb, and the wall "
           "would still talk only to her.",
           "Brille, Notizbuch und das Lesen bleiben ihre Sache. Freunde würden tragen, schützen und klettern, und die "
           "Wand spräche weiter nur mit ihr.")),
        (t("Rooms with a second way through", "Räume mit einem zweiten Weg"),
         t("Every room stays solvable alone. Company would only add speed or another route: one drains the channel "
           "while the others wait at the stair.",
           "Jeder Raum bleibt allein lösbar. Gesellschaft brächte nur Tempo oder einen anderen Weg: einer lässt den "
           "Kanal ab, während die anderen an der Treppe warten.")),
    ]
    idea_html = "".join(f"<div><h3>{h}</h3><p>{p}</p></div>" for h, p in ideas)
    gallery = lambda ids, cls: (f'<div class="crew-grid {cls}">' + "".join(_fig(ctx, i) for i in ids) + "</div>")  # noqa: E731
    proto_html = ""
    if proto:
        figs = "".join(ctx.figure(i, n, cls="crew-fig proto-fig") for i, n in proto)
        proto_html = f"""
<section class="wrap section crew-section">
  <div class="crew-head"><h2>{t("Where the idea started", "Wo die Idee herkommt")}</h2>
  <p>{t("Before Ascent of the Sun Temple became a single-player game, the temple was planned as five Fortnite islands "
        "for up to four players. These were their covers.",
        "Bevor Ascent of the Sun Temple ein Spiel für einen Spieler wurde, war der Tempel als fünf Fortnite-Inseln für "
        "bis zu vier Spieler geplant. Das waren ihre Titelbilder.")}</p></div>
  <div class="crew-grid crew-cols-5">{figs}</div>
</section>"""
    lineup = _fig(ctx, "ACT-CS-LINEUP", cls="crew-fig crew-hero") if ctx.exists("ACT-CS-LINEUP") else ""
    return f"""
<section class="wrap section crew-section">
  <div class="crew-intro">
    <div>
      <p class="big">{t("Ascent of the Sun Temple is a single-player game, and the first release is built for one "
                        "climber: Kaya.",
                        "Ascent of the Sun Temple ist ein Spiel für einen Spieler, und die erste Fassung ist für eine "
                        "Kletterin gebaut: Kaya.")}</p>
      <p>{t("While the temple was being designed, it was also painted with a whole crew climbing it together. Those "
            "paintings are too good to bury, and the idea behind them isn't dead either. This page keeps both: what "
            "a co-op climb could be one day, and how it would look. Nothing here is promised for launch.",
            "Während der Tempel entworfen wurde, entstanden auch Bilder einer ganzen Gruppe, die ihn gemeinsam "
            "erklimmt. Diese Bilder sind zu gut, um sie zu begraben, und die Idee dahinter ist auch nicht tot. Diese "
            "Seite bewahrt beides: wie ein gemeinsamer Aufstieg eines Tages sein könnte, und wie er aussähe. Nichts "
            "davon ist für den Start versprochen.")}</p>
    </div>
    {lineup}
  </div>
  <div class="crew-ideas">{idea_html}</div>
</section>
<section class="crew-band crew-band-page"><div class="wrap">
  <div class="crew-head"><h2>{t("In and around the temple", "Im Tempel und davor")}</h2>
  <p>{t("The same camp and the same rooms as the solo climb, with company.",
        "Dasselbe Lager und dieselben Räume wie beim Aufstieg allein, nur in Gesellschaft.")}</p></div>
  {gallery(floors, "crew-cols-4")}
</div></section>
<section class="wrap section crew-section">
  <div class="crew-head"><h2>{t("With the cast", "Mit den Figuren")}</h2>
  <p>{t("K'in, Oxlahun, the guardians and the High Priest, met by more than one climber.",
        "K'in, Oxlahun, die Wächter und der Hohepriester, getroffen von mehr als einem Kletterer.")}</p></div>
  {gallery(cast, "crew-cols-3")}
</section>
{proto_html}"""


PAGES = {
    "game/climbing-together.html": dict(
        title=("Climbing Together", "Gemeinsam klettern"), kicker=("Co-op concept", "Koop-Konzept"),
        banner="ISL-ASCENT",
        lede=("The game is played alone. This is what a climb with friends could look like one day.",
              "Das Spiel spielt man allein. So könnte ein Aufstieg mit Freunden eines Tages aussehen."),
        description=("Concept art and ideas for a possible co-op mode of Ascent of the Sun Temple.",
                     "Konzeptbilder und Ideen für einen möglichen Koop-Modus von Ascent of the Sun Temple."),
        body=climbing_together, og="ISL-ASCENT"),
}

PAGE_BANDS = [crew_band]
