"""Navigation tree for the whole site.

Each node: ((english label, german label), path, children)
- path is relative to the language root, e.g. "characters/kaya.html"
  (the German copy of every page lives under de/ with the same path)
- a node with children and a path gets a "landing" link plus a dropdown
"""

NAV = [
    (("Home", "Start"), "index.html", []),
    (("The Game", "Das Spiel"), "game/index.html", [
        (("Overview & Pillars", "Überblick & Säulen"), "game/index.html", []),
        (("How It Plays", "So wird gespielt"), "game/how-it-plays.html", []),
        (("Climbers & Co-op", "Kletterer & Koop"), "game/climbers-and-co-op.html", []),
        (("Weapons & Powers", "Waffen & Kräfte"), "game/weapons-and-powers.html", []),
    ]),
    (("UEFN Islands", "UEFN-Inseln"), "islands/index.html", [
        (("Overview & Roadmap", "Überblick & Roadmap"), "islands/index.html", []),
        (("1 · Trap Galleries", "1 · Trap Galleries"), "islands/trap-galleries.html", []),
        (("2 · Ascent of the Sun Temple", "2 · Ascent of the Sun Temple"), "islands/ascent.html", []),
        (("3 · Sun Temple Dig", "3 · Sun Temple Dig"), "islands/sun-temple-dig.html", []),
        (("4 · Illusion Depths", "4 · Illusion Depths"), "islands/illusion-depths.html", []),
        (("5 · Orb Raiders", "5 · Orb Raiders"), "islands/orb-raiders.html", []),
    ]),
    (("Story", "Geschichte"), "story/index.html", [
        (("The Story", "Die Geschichte"), "story/index.html", []),
        (("Lore & History", "Vorgeschichte & Legenden"), "story/lore.html", []),
        (("The Short Story", "Die Kurzgeschichte"), "story/short-story.html", []),
        (("Chapter 1 · The Overlooked Find", "Kapitel 1 · Der übersehene Fund"), "story/chapter-1.html", []),
    ]),
    (("World", "Welt"), "world/index.html", [
        (("The Living Temple", "Der lebende Tempel"), "world/index.html", []),
        (("The Threshold", "Die Schwelle"), "world/threshold.html", []),
        (("Records & Relics", "Aufzeichnungen & Relikte"), "world/relics.html", []),
    ]),
    (("Characters", "Figuren"), "characters/index.html", [
        (("Kaya", "Kaya"), "characters/kaya.html", []),
        (("K'in", "K'in"), "characters/kin.html", []),
        (("Oxlahun", "Oxlahun"), "characters/oxlahun.html", []),
        (("Dr. Isabel Kaan", "Dr. Isabel Kaan"), "characters/isabel-kaan.html", []),
        (("Risen Guardians", "Erweckte Wächter"), "characters/guardians/index.html", [
            (("The Guardians", "Die Wächter"), "characters/guardians/index.html", []),
            (("Ah Kuk", "Ah Kuk"), "characters/guardians/ah-kuk.html", []),
            (("Ix Nicte", "Ix Nicte"), "characters/guardians/ix-nicte.html", []),
            (("Chak Tun", "Chak Tun"), "characters/guardians/chak-tun.html", []),
            (("Ah Zac", "Ah Zac"), "characters/guardians/ah-zac.html", []),
            (("Kan Uk", "Kan Uk"), "characters/guardians/kan-uk.html", []),
        ]),
        (("Carved Climbers", "Gemeißelte Kletterer"), "characters/climbers/index.html", [
            (("The Mural", "Das Wandbild"), "characters/climbers/index.html", []),
            (("Mateo Vance", "Mateo Vance"), "characters/climbers/mateo-vance.html", []),
            (("Lisbet", "Lisbet"), "characters/climbers/lisbet.html", []),
            (("Joaquin Reyes", "Joaquin Reyes"), "characters/climbers/joaquin-reyes.html", []),
            (("Wren", "Wren"), "characters/climbers/wren.html", []),
            (("Odalys", "Odalys"), "characters/climbers/odalys.html", []),
        ]),
        (("The Hollow High Priest", "Der Hohle Hohepriester"), "characters/hollow-high-priest.html", []),
        (("Creatures & Bosses", "Kreaturen & Bosse"), "characters/creatures.html", []),
        (("Cast Lineup", "Größenvergleich"), "characters/lineup.html", []),
    ]),
    (("The Climb", "Der Aufstieg"), "climb/index.html", [
        (("The Pyramid", "Die Pyramide"), "climb/index.html", []),
        (("The Threshold Hub", "Die Schwelle (Hub)"), "climb/threshold.html", []),
        (("The Shell", "The Shell"), "climb/floor-0.html", []),
        (("Tier I · Flooded Foundations", "Stufe I · Überflutete Fundamente"), "climb/tier-1.html", []),
        (("Tier II · Trap Galleries", "Stufe II · Fallengalerien"), "climb/tier-2.html", []),
        (("Tier III · Shifting Vaults", "Stufe III · Wandernde Gewölbe"), "climb/tier-3.html", []),
        (("Tier IV · Elemental Sanctums", "Stufe IV · Elementarheiligtümer"), "climb/tier-4.html", []),
        (("Tier V · Illusion Depths", "Stufe V · Tiefen der Täuschung"), "climb/tier-5.html", []),
        (("Tier VI · The Ascension", "Stufe VI · Die Erhebung"), "climb/tier-6.html", []),
        (("The Sky Altar", "Der Himmelsaltar"), "climb/sky-altar.html", []),
        (("Shared Rooms", "Gemeinsame Räume"), "climb/shared-rooms.html", []),
    ]),
    (("Art & Assets", "Kunst & Assets"), "art/index.html", [
        (("Art Direction", "Art Direction"), "art/index.html", []),
        (("Modular Kits", "Modulare Kits"), "art/kits.html", []),
        (("Gameplay Props", "Gameplay-Objekte"), "art/props.html", []),
        (("Hero Items & Relics", "Heldengegenstände & Relikte"), "art/relics.html", []),
        (("Threshold & Forecourt", "Schwelle & Vorplatz"), "art/threshold-set.html", []),
        (("Level Set Pieces", "Level-Setpieces"), "art/set-pieces.html", []),
    ]),
]


def all_paths(nodes=NAV):
    """Every page path in nav order, with its breadcrumb trail of (en, de) labels."""
    out = []

    def walk(items, trail):
        for label, path, kids in items:
            if path and path not in [p for p, _ in out]:
                out.append((path, trail + [label]))
            walk(kids, trail + [label])

    walk(nodes, [])
    return out
