"""The Climb tab (English and German). Pages not defined here still build as "coming soon" stubs."""
from components import facts, pair


def tags(ctx, pairs):
    return '<p class="tags">' + "".join(f"<span>{ctx.t(en, de)}</span>" for en, de in pairs) + "</p>"


def route(ctx, rooms):
    """A numbered route: the rooms of a floor in the order the player meets them."""
    items = []
    for n, (img, name, tag_pairs, text, note) in enumerate(rooms, 1):
        t = ctx.t
        note_html = f'<p class="station-note">{t(*note)}</p>' if note else ""
        items.append(
            f'<li class="station"><span class="station-num" aria-hidden="true">{n}</span>'
            f'<div class="station-media">{ctx.figure(img, alt=t(*name))}</div>'
            f'<div class="station-text"><h3>{t(*name)}</h3>{tags(ctx, tag_pairs)}<p>{t(*text)}</p>{note_html}</div></li>')
    return f'<ol class="route" role="list">{"".join(items)}</ol>'


# ------------------------------------------------------------------ Floor 0
def floor_0(ctx):
    u, t = ctx.url, ctx.t
    ix_nicte = u("characters/guardians/ix-nicte.html")
    story = u("story/short-story.html")
    rooms = [
        ("B-03", ("The entry hall", "Die Eingangshalle"), [("Spawn", "Startpunkt"), ("Movement", "Bewegung")],
         ("Where Kaya spawns. Wide, quiet, and lit by one shaft through the roof, so you can learn the camera and the jump with "
          "nothing at stake.",
          "Hier erscheint Kaya. Weit, still und erhellt von einem einzigen Lichtschacht im Dach, damit du Kamera und Sprung lernen "
          "kannst, ohne dass etwas auf dem Spiel steht."),
         (f"On a half-submerged step, <a href='{ix_nicte}'>Ix Nicte</a>, Keeper of the First Step, stands dormant.",
          f"Auf einer halb überfluteten Stufe ruht <a href='{ix_nicte}'>Ix Nicte</a>, die Hüterin der ersten Stufe.")),
        ("B-04", ("The fire-vent floor", "Der Boden der Feuerdüsen"), [("Timed hazard", "Getaktete Gefahr"), ("Fixed beat", "Fester Takt")],
         ("Five stepping stones over a pit of flame. The first hazard, and the one that teaches you to read timing off the floor "
          "rather than off an enemy.",
          "Fünf Trittsteine über einer Grube voller Flammen. Die erste Gefahr, und die, die dir beibringt, das Timing am Boden "
          "abzulesen statt an einem Gegner."), None),
        ("B-05", ("The chasm", "Die Schlucht"), [("Fall", "Absturz"), ("Platforming", "Plattformen")],
         ("The floor runs out over a deep chasm. Sliding slabs and floating platforms carry you across, and not one of them waits "
          "for you. A golden idol glints on a ledge.",
          "Der Boden endet über einer tiefen Schlucht. Gleitende Steinplatten und schwebende Plattformen tragen dich hinüber, und "
          "keine davon wartet auf dich. Auf einem Vorsprung glänzt ein goldenes Idol."), None),
        ("B-06", ("The pressure plate", "Die Druckplatte"), [("Puzzle", "Rätsel"), ("Gate", "Tor")],
         ("Stand on the carved plate and the door lifts. Step off and it drops. The first room that asks you to think about where "
          "your weight is.",
          "Stell dich auf die gemeißelte Platte, und die Tür hebt sich. Steig herunter, und sie fällt. Der erste Raum, in dem du "
          "darüber nachdenken musst, wo dein Gewicht steht."), None),
        ("B-07", ("The trap corridor", "Der Fallenkorridor"), [("Layered hazard", "Überlagerte Gefahren"), ("Corridor", "Korridor")],
         ("Two hazards on different rhythms in one narrow run: retractable spikes in the floor, and a stone serpent spitting fire "
          "from the end. Getting through once is luck; getting through clean means you have learned both beats.",
          "Zwei Gefahren in unterschiedlichem Rhythmus in einem engen Gang: einfahrende Stacheln im Boden und eine steinerne "
          "Schlange, die am Ende Feuer speit. Einmal durchzukommen ist Glück; sauber durchzukommen heißt, dass du beide Takte "
          "gelernt hast."),
         (f"This is where Kaya dies in <a href='{story}'>the short story</a>.",
          f"Hier stirbt Kaya in <a href='{story}'>der Kurzgeschichte</a>.")),
        ("B-08", ("The orb shrine", "Der Kugelschrein"), [("Puzzle", "Rätsel"), ("Shrine", "Schrein")],
         ("Orbs on pedestals, gold, blue and red, around a ring of glyphs, with one correct arrangement. K'in lights the orb that "
          "is wrong rather than the one that is right, so the solving is still yours.",
          "Kugeln auf Sockeln, gold, blau und rot, um einen Ring aus Glyphen, mit genau einer richtigen Anordnung. K'in lässt die "
          "Kugel aufleuchten, die falsch liegt, nicht die richtige, damit das Lösen deine Sache bleibt."), None),
        ("B-09", ("The beam switchback", "Die Strahlen-Serpentine"), [("Toggle hazard", "Schaltende Gefahr"), ("Timing", "Timing")],
         ("Blue-white energy beams cross a switchback ramp and switch on a toggle. Nothing is dodged here. It is walked, on the "
          "right half of the second.",
          "Blauweiße Energiestrahlen kreuzen eine Serpentinenrampe und schalten im Takt an und aus. Hier wird nichts ausgewichen. "
          "Hier wird gegangen, in der richtigen Hälfte der Sekunde."), None),
        ("B-10", ("The sword shrine", "Der Schwertschrein"), [("Combat", "Kampf"), ("Reward", "Belohnung")],
         ("Kaya lifts the obsidian macuahuitl off its pedestal, and the first guardian stands up. First real combat, on a high "
          "landing that overlooks the atrium.",
          "Kaya hebt das Obsidian-Macuahuitl von seinem Sockel, und der erste Wächter erhebt sich. Der erste echte Kampf, auf einem "
          "hohen Absatz über dem Atrium."), None),
        ("B-11", ("The bridge to the portal", "Die Brücke zum Portal"), [("Exit", "Ausgang"), ("Next floor", "Nächste Ebene")],
         ("A narrow bridge crosses high over the atrium to the round portal on top of the Sun Pillar. Step through and Floor 0 "
          "seals behind you, sword in hand.",
          "Eine schmale Brücke führt hoch über das Atrium zum runden Portal auf der Spitze der Sonnensäule. Tritt hindurch, und "
          "Ebene 0 versiegelt sich hinter dir, das Schwert in der Hand."), None),
    ]
    fact_rows = [
        (t("Place in the climb", "Platz im Aufstieg"), t("The first floor, below Tier I", "Die erste Ebene, unter Stufe I")),
        (t("Rooms", "Räume"), t("Nine spaces on one route", "Neun Räume auf einer Route")),
        (t("Teaches", "Lehrt"), t("Every core verb once: move, time, think, fight", "Jedes Grundverb genau einmal: laufen, timen, denken, kämpfen")),
        (t("Enemies", "Gegner"), t("One Risen Guardian", "Ein Erweckter Wächter")),
        (t("Reward", "Belohnung"), t("The obsidian macuahuitl, and the Threshold opens", "Das Obsidian-Macuahuitl, und die Schwelle öffnet sich")),
    ]
    set_pieces = [
        ("F0-01", t("The Sun Pillar", "Die Sonnensäule")),
        ("F0-02", t("Stepping stones and spawn platform", "Trittsteine und Startplattform")),
        ("F0-03", t("The sword shrine", "Der Schwertschrein")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Floor 0 was designed as one object before a single room was painted. The cutaway, the plan and the codex "
                        "page all describe the same nine spaces and the single route through them.",
                        "Ebene 0 wurde als ein einziges Objekt entworfen, bevor auch nur ein Raum gemalt wurde. Schnitt, Grundriss "
                        "und Codexseite beschreiben dieselben neun Räume und die eine Route hindurch.")}</p>
      <p>{t("The route spirals upward from a flooded atrium to a portal on top of the Sun Pillar, which stands in that same atrium. "
            "It is the tutorial: it teaches every core verb once, and nothing twice.",
            "Die Route windet sich von einem gefluteten Atrium nach oben bis zu einem Portal auf der Spitze der Sonnensäule, die "
            "in genau diesem Atrium steht. Sie ist das Tutorial: Sie lehrt jedes Grundverb genau einmal und keines doppelt.")}</p>
    </div>
    {facts(fact_rows)}
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("One floor, three drawings", "Eine Ebene, drei Zeichnungen")}</h2>
  {pair(ctx, "B-01", t("The floor from above", "Die Ebene von oben"),
        "CX-F0", t("The same floor as a codex page", "Dieselbe Ebene als Codexseite"))}
  <div class="drawing-wide">{ctx.figure("B-02", t("Isometric cutaway: the route spirals upward", "Isometrischer Schnitt: Die Route windet sich nach oben"), cls="sheet")}</div>
</div></section>

<section class="wrap section">
  <h2>{t("Nine rooms, one way up", "Neun Räume, ein Weg nach oben")}</h2>
  <p class="lede-sm">{t("In the order Kaya meets them, from the flooded atrium to the portal on the Sun Pillar.",
                        "In der Reihenfolge, in der Kaya sie betritt, vom gefluteten Atrium bis zum Portal auf der Sonnensäule.")}</p>
  {route(ctx, rooms)}
</section>

<section class="band"><div class="wrap section">
  <div class="section-head">
    <h2>{t("Set pieces", "Setpieces")}</h2>
    <a class="text-link" href="{u('art/set-pieces.html')}">{t("All level set pieces", "Alle Level-Setpieces")}</a>
  </div>
  {ctx.gallery(set_pieces, cls="gallery-3")}
</div></section>
"""


PAGES = {
    "climb/floor-0.html": dict(
        title=("Floor 0 · The Initiation", "Ebene 0 · Die Einweihung"), kicker=("The Climb", "Der Aufstieg"),
        lede=("The tutorial floor: nine spaces on one route, and every core verb taught once.",
              "Die Tutorial-Ebene: neun Räume auf einer Route, und jedes Grundverb wird genau einmal gelehrt."),
        description=("Floor 0, The Initiation: the tutorial floor of Ascent of the Sun Temple, room by room.",
                     "Ebene 0, Die Einweihung: die Tutorial-Ebene von Ascent of the Sun Temple, Raum für Raum."),
        banner=["B-03", "B-11"], og=["B-02", "B-11"],
        body=floor_0),
}
