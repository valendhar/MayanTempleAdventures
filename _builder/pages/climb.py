"""The Climb tab (English and German): the pyramid overview, the hub, every floor and the summit.

Images that are not uploaded yet render as placeholders that show their ID.
"""
from components import T, catalog, facts, feature, pair, room, tags

# ------------------------------------------------------------------ campaign data
# One row per floor: number, name, rooms, new mechanic, enemies, reward (None = no reward).
FLOORS = {
    0: (("The Initiation", "Die Einweihung"), "F0", ("All core verbs", "Alle Grundverben"),
        ("Risen Guardian", "Erweckter Wächter"), ("Obsidian macuahuitl; the Threshold opens", "Obsidian-Macuahuitl; die Schwelle öffnet sich")),
    1: (("The Drowned Gallery", "Die ertrunkene Galerie"), "T1A · T1B",
        ("Water hazards, logs, drain, lift", "Wassergefahren, Baumstämme, Abfluss, Aufzug"),
        ("Risen Guardians", "Erweckte Wächter"), None),
    2: (("The Root Cellars", "Die Wurzelkeller"), "T1C · T1D",
        ("Swing, slick slope, ranged combat", "Schwingen, rutschiger Hang, Fernkampf"),
        ("Cave Bats", "Höhlenfledermäuse"), ("Spirit Blowgun; Tier I shortcut", "Geisterblasrohr; Abkürzung zu Stufe I")),
    3: (("Hall of Blades", "Halle der Klingen"), "T2A · T2B",
        ("Saws, pendulums, breakable tiles, plate sequence", "Sägen, Pendel, zerbrechliche Fliesen, Plattenfolge"),
        ("Scarab Swarms, Husk Archers", "Skarabäenschwärme, Hülsenschützen"), ("Sunburst Sling in the shop", "Sonnenschleuder im Laden")),
    4: (("The Dart Colonnade", "Die Pfeilkolonnade"), "T2C · T2D",
        ("Darts, fire vents, rotatable shield statues, wave fight", "Pfeile, Feuerdüsen, drehbare Schildstatuen, Wellenkampf"),
        ("Husk Archers, Obsidian Panther", "Hülsenschützen, Obsidianpanther"), None),
    5: (("The Collapsing Stair", "Die einstürzende Treppe"), "T2E · T2F",
        ("Crumbling stairs, boulders, the first chase", "Bröckelnde Treppen, Felsbrocken, die erste Verfolgung"),
        ("Guardian Spirit", "Wächtergeist"), ("Tier II shortcut", "Abkürzung zu Stufe II")),
    6: (("The Tilting Sanctum", "Das kippende Heiligtum"), "T3A · T3B",
        ("Seesaws, rotating discs", "Wippen, rotierende Scheiben"),
        ("Risen Guardians, Husk Archers", "Erweckte Wächter, Hülsenschützen"), None),
    7: (("The Vanishing Path", "Der verschwindende Pfad"), "T3C · T3D",
        ("Phasing platforms, the memory path", "Phasende Plattformen, der Gedächtnispfad"),
        ("Stone Sentries", "Steinwächter"), ("K'in's Glyph Scan", "K'ins Glyphenscan")),
    8: (("The Gear Ascent", "Der Zahnradaufstieg"), "T3E · B1",
        ("Lifts, gears, timed switches", "Aufzüge, Zahnräder, Zeitschalter"),
        ("The Gearwarden", "Der Zahnradwächter"), ("Tier III shortcut", "Abkürzung zu Stufe III")),
    9: (("The Ember Forge", "Die Glutschmiede"), "T4A · T4B",
        ("Lava, fire jets, burning bridges", "Lava, Feuerstrahlen, brennende Brücken"),
        ("Risen Guardians, Obsidian Panther", "Erweckte Wächter, Obsidianpanther"), ("Fire Orb, Ember Censer", "Feuerkugel, Glutweihrauchfass")),
    10: (("The Buried Ossuary", "Das verschüttete Beinhaus"), "T4C · T4D",
         ("Cracked walls, heavy plates, boulders", "Rissige Wände, schwere Platten, Felsbrocken"),
         ("A crowd of Risen, Stone Sentry", "Erweckte in Scharen, Steinwächter"), ("Earth Orb", "Erdkugel")),
    11: (("The Broken Ramparts", "Die zerbrochenen Wälle"), "T4E · T4F",
         ("Wind gusts, updrafts, open to the sky", "Windböen, Aufwinde, offen zum Himmel"),
         ("Cave Bats, Husk Archers", "Höhlenfledermäuse, Hülsenschützen"), ("Wind Orb", "Windkugel")),
    12: (("The Sunken Reservoir", "Das versunkene Reservoir"), "T4G · T4H",
         ("Rising water, currents, air pockets", "Steigendes Wasser, Strömungen, Lufttaschen"),
         ("Obsidian Panther, Scarab Swarms", "Obsidianpanther, Skarabäenschwärme"), ("Water Orb; Tier IV shortcut", "Wasserkugel; Abkürzung zu Stufe IV")),
    13: (("The Mirror Sanctum", "Das Spiegelheiligtum"), "T5A · T5B",
         ("Mirrors, light beams", "Spiegel, Lichtstrahlen"),
         ("Husk Archers, Stone Sentries", "Hülsenschützen, Steinwächter"), None),
    14: (("The Hall of Lies", "Die Halle der Lügen"), "T5C · T5D",
         ("Illusion floors, false walls, a chase", "Trugböden, falsche Wände, eine Verfolgung"),
         ("Guardian Spirit", "Wächtergeist"), None),
    15: (("The Totem Vault", "Das Totemgewölbe"), "T5E · B2",
         ("Totem alignment, torches", "Totems ausrichten, Fackeln"),
         ("The Jaguar Priest", "Der Jaguarpriester"), ("Tier V shortcut", "Abkürzung zu Stufe V")),
    16: (("The Elemental Gauntlet", "Der Elementarspießrutenlauf"), "T6A · T6B",
         ("All four orbs combined", "Alle vier Kugeln kombiniert"),
         ("Mixed elites", "Gemischte Elitegegner"), None),
    17: (("The Inner Sanctum", "Das innere Heiligtum"), "T6C · T6D",
         ("Every trap, timed doors", "Alle Fallen, Zeittüren"),
         ("The Priest's Lieutenant", "Der Leutnant des Priesters"), ("Sun Orb; the way to the summit", "Sonnenkugel; der Weg zum Gipfel")),
    18: (("The Sky Altar", "Der Himmelsaltar"), "SKY",
         ("Boss phases on the braziers", "Bossphasen an den Feuerbecken"),
         ("The Hollow High Priest", "Der Hohle Hohepriester"), ("The ending choice; the Trials unlock", "Die Wahl am Ende; die Prüfungen werden freigeschaltet")),
}
# floors whose last room before the Portal Chamber is a Spirit Shrine
SHRINE_FLOORS = {2, 5, 8, 12, 15, 17}


def floor_title(ctx, n):
    return ctx.t(f"Floor {n} · ", f"Ebene {n} · ") + T(ctx, FLOORS[n][0])


def floor_meta(ctx, n):
    _, _, mech, enemies, reward = FLOORS[n]
    t = ctx.t
    rows = [(t("New", "Neu"), T(ctx, mech)), (t("Enemies", "Gegner"), T(ctx, enemies))]
    if reward:
        rows.append((t("Reward", "Belohnung"), T(ctx, reward)))
    return '<dl class="floor-meta">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def floor_end(ctx, n):
    u, t = ctx.url, ctx.t
    pc = f"<a href='{u('climb/shared-rooms.html')}#portal-chamber'>{t('Portal Chamber', 'Portalkammer')}</a>"
    if n == 17:
        return t(f"The Lieutenant's vault opens onto the stair to the <a href='{u('climb/sky-altar.html')}'>Sky Altar</a>.",
                 f"Das Gewölbe des Leutnants öffnet sich zur Treppe hinauf zum <a href='{u('climb/sky-altar.html')}'>Himmelsaltar</a>.")
    if n in SHRINE_FLOORS:
        sr = f"<a href='{u('climb/shared-rooms.html')}#spirit-shrine'>{t('Spirit Shrine', 'Geisterschrein')}</a>"
        return t(f"Then a {sr} to rest, and the {pc}.", f"Danach ein {sr} zum Ausruhen und die {pc}.")
    return t(f"Then the {pc}, and up.", f"Danach die {pc}, und weiter nach oben.")


# ------------------------------------------------------------------ tiers
# Each room: (code, name, tags, paragraphs, scene, map, codex, extra)
def R(code, name, tag_pairs, text, scene=None, map_id=None, codex=None, extra=None, flip=False):
    """flip is accepted for readability only: rooms alternate sides automatically."""
    return (code, name, tag_pairs, text, scene or f"{code}-SCENE", map_id or f"{code}-MAP", codex or f"CX-{code}", extra)


KEY = ("Key Orb room", "Raum der Schlüsselkugel")

TIERS = {
    1: dict(
        title=("Tier I · The Flooded Foundations", "Stufe I · Die überfluteten Fundamente"),
        line=("The ancients harnessed balance.", "Die Alten bändigten das Gleichgewicht."),
        lede=("The temple's flooded base: water, weight and the first ranged weapon.",
              "Die geflutete Basis des Tempels: Wasser, Gewicht und die erste Fernkampfwaffe."),
        intro=(("Two floors at the foot of the pyramid, where the builders first held the elements in balance and the water never "
                "left. Each room asks one question at a time: where to stand, when to cross, what to shoot.",
                "Zwei Ebenen am Fuß der Pyramide, wo die Erbauer die Elemente zum ersten Mal im Gleichgewicht hielten und das Wasser "
                "nie wieder abfloss. Jeder Raum stellt genau eine Frage: wo du stehst, wann du hinübergehst, worauf du zielst."),),
        floors={
            1: [R("T1A", ("The Drowned Gallery", "Die ertrunkene Galerie"), [("Water", "Wasser"), ("Timing", "Timing")],
                  [("A tall flooded hall of dark green water. Kaya crosses stone islands and floating logs that drift between them, and "
                    "one island has a band of spikes on a timer.",
                    "Eine hohe, geflutete Halle voller dunkelgrünem Wasser. Kaya überquert Steininseln und treibende Baumstämme dazwischen, "
                    "und auf einer Insel fährt in festem Takt ein Streifen Stacheln aus."),
                   ("Deep water hides temple leeches. The shallow wading lane along the east wall is safe from them but slow, and two "
                    "guardians wade in it, so the coward's route costs time and a fight. The golden idol sits on a pillar in the water.",
                    "Im tiefen Wasser lauern Tempelegel. Die flache Watspur an der Ostwand ist sicher vor ihnen, aber langsam, und zwei "
                    "Wächter waten darin, also kostet der Weg des Feiglings Zeit und einen Kampf. Das goldene Idol steht auf einer Säule im Wasser.")],
                  scene="D-02", map_id="D-01"),
               R("T1B", ("The Sluice Hall", "Die Schleusenhalle"), [KEY, ("Drain", "Abfluss")],
                  [("The Key Orb sits on a pedestal at the bottom of a flooded channel, and a current pushes you back out.",
                    "Die Schlüsselkugel liegt auf einem Sockel am Grund eines gefluteten Kanals, und eine Strömung drückt dich wieder hinaus."),
                   ("Ride a stone lift to a balcony and press the plate there: the water drains through the sluice gate and the current "
                    "stops. Take the orb and the room fights back, as three Risen Guardians rise in the galleries. The idol is on a "
                    "column, reached from a crate.",
                    "Fahr mit einem Steinaufzug zu einem Balkon und tritt dort auf die Platte: Das Wasser fließt durch das Schleusentor ab, "
                    "und die Strömung versiegt. Nimm die Kugel, und der Raum wehrt sich, denn in den Galerien erheben sich drei Erweckte "
                    "Wächter. Das Idol steht auf einer Säule, die du von einer Kiste aus erreichst.")],
                  scene="D-04", map_id="D-03")],
            2: [R("T1C", ("The Root Cellar", "Der Wurzelkeller"), [("Swing", "Schwingen"), ("Slope", "Hang")],
                  [("A slick moss slope ends above a pit of tangled roots. Wooden platforms hang from vines and swing like pendulums "
                    "across it, with a root island between them.",
                    "Ein rutschiger Moosabhang endet über einer Grube voller verschlungener Wurzeln. Holzplattformen hängen an Ranken und "
                    "schwingen wie Pendel darüber, mit einer Wurzelinsel dazwischen."),
                   ("Cave bats swoop through the dark. Glowing fungus lights the way.",
                    "Höhlenfledermäuse stoßen durch die Dunkelheit herab. Leuchtende Pilze weisen den Weg.")],
                  scene="D-06", map_id="D-05"),
               R("T1D", ("The Blowgun Shrine", "Der Blasrohrschrein"), [KEY, ("Ranged", "Fernkampf")],
                  [("A square shrine with a raised altar that holds the Spirit Blowgun, the first ranged weapon.",
                    "Ein quadratischer Schrein mit einem erhöhten Altar, auf dem das Geisterblasrohr liegt, die erste Fernkampfwaffe."),
                   ("Three round glyph targets sit high on the walls. Hit all three and the Key Orb rises from the altar, while cave bats "
                    "harass the shooter.",
                    "Hoch an den Wänden sitzen drei runde Glyphenziele. Triff alle drei, und die Schlüsselkugel steigt aus dem Altar, "
                    "während Höhlenfledermäuse den Schützen bedrängen.")],
                  scene="D-08", map_id="D-07")],
        },
        set_pieces=[("T1-01", ("Logs and stone islands", "Baumstämme und Steininseln")),
                    ("T1-02", ("Sluice gate and channel", "Schleusentor und Kanal")),
                    ("T1-03", ("Stone lift with chains and counterweight", "Steinaufzug mit Ketten und Gegengewicht")),
                    ("T1-04", ("Root pit and glowing fungus", "Wurzelgrube und Leuchtpilze")),
                    ("T1-05", ("Vine swing platforms", "Schwingende Rankenplattformen")),
                    ("T1-06", ("The blowgun altar", "Der Blasrohraltar"))],
    ),
    2: dict(
        title=("Tier II · The Trap Galleries", "Stufe II · Die Fallengalerien"),
        line=("The first element betrayed them.", "Das erste Element verriet sie."),
        lede=("Three floors of traps built to stop thieves: blades, darts, fire and the first chase.",
              "Drei Ebenen voller Fallen, gebaut gegen Diebe: Klingen, Pfeile, Feuer und die erste Verfolgung."),
        intro=(("After the betrayal, the priests turned the galleries into a defence. Every trap here has a rhythm you can learn, "
                "and each room still teaches one at a time, until the stair gives way and the temple sends something after you.",
                "Nach dem Verrat machten die Priester die Galerien zu einer Verteidigungsanlage. Jede Falle hier hat einen Rhythmus, den "
                "du lernen kannst, und jeder Raum lehrt noch immer einen nach dem anderen, bis die Treppe nachgibt und der Tempel dir "
                "etwas hinterherschickt."),),
        floors={
            3: [R("T2A", ("The Saw Gallery", "Die Sägengalerie"), [("Blades", "Klingen"), ("Lanes", "Bahnen")],
                  [("A long hall split into three lanes by low walls. Circular saw blades race along floor tracks across all three "
                    "lanes, pendulum blades swing over the middle one, and strips of floor crumble into a trench.",
                    "Eine lange Halle, durch niedrige Mauern in drei Bahnen geteilt. Kreissägeblätter rasen auf Bodenschienen durch alle "
                    "drei Bahnen, über der mittleren schwingen Pendelklingen, und Bodenstreifen zerbröckeln in einen Graben."),
                   ("Scarab swarms break the rhythm just when you have found it.",
                    "Skarabäenschwärme brechen den Rhythmus genau dann, wenn du ihn gefunden hast.")]),
               R("T2B", ("The Plate Vault", "Das Plattengewölbe"), [KEY, ("Sequence", "Reihenfolge")],
                  [("A sealed vault stands in the middle of a square room, ringed by four pressure plates. A mural on the far wall shows "
                    "the correct glyph order.",
                    "In der Mitte eines quadratischen Raums steht ein versiegeltes Gewölbe, umgeben von vier Druckplatten. Ein Wandbild an "
                    "der Rückwand zeigt die richtige Reihenfolge der Glyphen."),
                   ("Husk Archers shoot from the balconies and darts fly from the walls while you work out the sequence.",
                    "Hülsenschützen schießen von den Balkonen, und Pfeile fliegen aus den Wänden, während du die Reihenfolge herausfindest.")],
                  flip=True)],
            4: [R("T2C", ("The Dart Colonnade", "Die Pfeilkolonnade"), [("Darts", "Pfeile"), ("Cover", "Deckung")],
                  [("A long pillared colonnade. Darts shoot from bat-face masks in the pillars and fire vents flare in the floor.",
                    "Eine lange Säulenkolonnade. Aus Fledermausmasken in den Säulen schießen Pfeile, und im Boden lodern Feuerdüsen auf."),
                   ("Rotate the stone shield statues to block the dart lanes. Archers hold a gallery at the far end.",
                    "Dreh die steinernen Schildstatuen, um die Schussbahnen zu blockieren. Am anderen Ende halten Schützen eine Galerie.")]),
               R("T2D", ("The Orb Guard Court", "Der Hof der Kugelwacht"), [KEY, ("Wave fight", "Wellenkampf")],
                  [("A combat court around a raised dais that holds the Key Orb, ringed by fire vents.",
                    "Ein Kampfhof um ein erhöhtes Podest mit der Schlüsselkugel, umringt von Feuerdüsen."),
                   ("A wave fight: guardians first, then archers on the corner plinths, then the first Obsidian Panther.",
                    "Ein Wellenkampf: zuerst Wächter, dann Schützen auf den Ecksockeln, dann der erste Obsidianpanther.")])],
            5: [R("T2E", ("The Collapsing Stair", "Die einstürzende Treppe"), [("Crumbling", "Bröckeln"), ("Boulders", "Felsbrocken")],
                  [("A tall shaft of zig-zag stair flights. The steps crumble behind you while boulders roll down toward you.",
                    "Ein hoher Schacht aus Treppenläufen im Zickzack. Die Stufen bröckeln hinter dir weg, während Felsbrocken auf dich "
                    "zurollen.")]),
               R("T2F", ("The Chase Shaft", "Der Fluchtschacht"), [KEY, ("Chase", "Verfolgung")],
                  [("A spiral ramp around a dark void. A huge, unkillable Guardian Spirit rises from below, and the ramp crumbles behind "
                    "you. The first chase: run.",
                    "Eine Spiralrampe um einen dunklen Abgrund. Von unten steigt ein riesiger, unbesiegbarer Wächtergeist auf, und die "
                    "Rampe zerbröckelt hinter dir. Die erste Verfolgung: Lauf.")],
                  flip=True)],
        },
        set_pieces=[("T2-01", ("Saw blade on a floor track", "Sägeblatt auf Bodenschiene")),
                    ("T2-02", ("Pendulum blade", "Pendelklinge")),
                    ("T2-03", ("The sealed central vault", "Das versiegelte Mittelgewölbe")),
                    ("T2-04", ("Dart emitters and dart pillar", "Pfeilwerfer und Pfeilsäule")),
                    ("T2-05", ("Rotatable shield statues", "Drehbare Schildstatuen")),
                    ("T2-06", ("The spiral ramp shaft", "Der Spiralrampenschacht"))],
    ),
    3: dict(
        title=("Tier III · The Shifting Vaults", "Stufe III · Die wandernden Gewölbe"),
        line=("The temple learned to move, so no thief would find the same path twice.",
              "Der Tempel lernte, sich zu bewegen, damit kein Dieb denselben Weg zweimal findet."),
        lede=("The temple starts to move: seesaws, turning discs, vanishing paths and gears.",
              "Der Tempel beginnt sich zu bewegen: Wippen, drehende Scheiben, verschwindende Pfade und Zahnräder."),
        intro=(("From here on, rooms combine mechanics. The floor tilts under your weight, platforms phase in and out on a beat, and "
                "K'in can only show you the way once. The tier ends in the Gearwarden's arena.",
                "Ab hier verbinden die Räume mehrere Mechaniken. Der Boden kippt unter deinem Gewicht, Plattformen erscheinen und "
                "verschwinden im Takt, und K'in kann dir den Weg nur ein einziges Mal zeigen. Die Stufe endet in der Arena des "
                "Zahnradwächters."),),
        floors={
            6: [R("T3A", ("The Seesaw Hall", "Die Wippenhalle"), [("Weight", "Gewicht"), ("Tilt", "Neigung")],
                  [("Long stone seesaws over a deep pit tilt under Kaya's weight, followed by a tilting bridge. Archers watch from the "
                    "side ledges.",
                    "Lange steinerne Wippen über einer tiefen Grube kippen unter Kayas Gewicht, danach folgt eine kippende Brücke. "
                    "Schützen lauern auf den Seitensimsen.")]),
               R("T3B", ("The Disc Well", "Der Scheibenbrunnen"), [KEY, ("Rotation", "Drehung")],
                  [("Rotating stone discs, carved like calendar wheels, spiral up a tall well at different speeds. The Key Orb waits on "
                    "the highest one.",
                    "Rotierende Steinscheiben, gemeißelt wie Kalenderräder, winden sich in unterschiedlichem Tempo einen hohen Brunnen "
                    "hinauf. Die Schlüsselkugel wartet auf der obersten.")],
                  flip=True)],
            7: [R("T3C", ("The Phase Bridges", "Die Phasenbrücken"), [("Phasing", "Phasen"), ("Rhythm", "Rhythmus")],
                  [("Square platforms flicker between solid stone and glowing outlines over a void, in three colour-keyed groups. "
                    "K'in pulses on the beat.",
                    "Quadratische Plattformen flackern über einem Abgrund zwischen festem Stein und leuchtenden Umrissen, in drei "
                    "farbcodierten Gruppen. K'in pulsiert im Takt.")]),
               R("T3D", ("The Memory Path", "Der Gedächtnispfad"), [KEY, ("Memory", "Gedächtnis")],
                  [("K'in sings from a pedestal and, for a moment, reveals a winding path of floating steps over a pit. Then it is gone, "
                    "and you walk it from memory while Stone Sentries patrol below.",
                    "K'in singt von einem Sockel und enthüllt für einen Moment einen gewundenen Pfad aus schwebenden Stufen über einer "
                    "Grube. Dann ist er verschwunden, und du gehst ihn aus dem Gedächtnis, während unten Steinwächter patrouillieren."),
                   ("The reward is K'in's Glyph Scan.", "Die Belohnung ist K'ins Glyphenscan.")],
                  flip=True)],
            8: [R("T3E", ("The Gear Shaft", "Der Zahnradschacht"), [("Gears", "Zahnräder"), ("Timed switches", "Zeitschalter")],
                  [("A mechanical shaft of huge turning stone gears, lifts, chains and timed wall switches.",
                    "Ein mechanischer Schacht aus riesigen, sich drehenden Steinzahnrädern, Aufzügen, Ketten und Wandschaltern auf Zeit.")]),
               R("B1", ("The Gearwarden Arena", "Die Arena des Zahnradwächters"), [("Boss", "Boss")],
                  [("A circular arena with a rotating gear ring and four steam-vent pillars. The Gearwarden, a nine-metre construct of "
                    "carved blocks and gears around an amber core, charges. Make it crash into a pillar to expose the core.",
                    "Eine runde Arena mit einem rotierenden Zahnkranz und vier Dampfsäulen. Der Zahnradwächter, ein neun Meter hohes "
                    "Konstrukt aus gemeißelten Blöcken und Zahnrädern um einen Bernsteinkern, stürmt los. Lass ihn gegen eine Säule "
                    "krachen, um den Kern freizulegen.")],
                  flip=True, extra=("E14", ("The Gearwarden", "Der Zahnradwächter")))],
        },
        set_pieces=[("T3-01", ("Seesaws and tilting bridge", "Wippen und kippende Brücke")),
                    ("T3-02", ("Rotating calendar discs", "Rotierende Kalenderscheiben")),
                    ("T3-03", ("Phase platforms", "Phasenplattformen")),
                    ("T3-04", ("Memory path spirit steps and singing pedestal", "Geisterstufen des Gedächtnispfads und singender Sockel")),
                    ("T3-05", ("Wall gears, chains, counterweights and switches", "Wandzahnräder, Ketten, Gegengewichte und Schalter")),
                    ("T3-06", ("Gearwarden arena: gear ring and vent pillars", "Arena des Zahnradwächters: Zahnkranz und Dampfsäulen"))],
    ),
    4: dict(
        title=("Tier IV · The Elemental Sanctums", "Stufe IV · Die Elementarheiligtümer"),
        line=("The orbs scattered, and guardians were born.", "Die Kugeln zerstreuten sich, und Wächter wurden geboren."),
        lede=("Four sanctums, four elements: the tier where Kaya claims the Elemental Orbs.",
              "Vier Heiligtümer, vier Elemente: die Stufe, in der Kaya die Elementarkugeln erringt."),
        intro=(("Each of the four floors keeps one of the scattered orbs. Fire, Earth, Wind and Water are permanent powers: once "
                "Kaya holds one, rooms she has already cleared can be read in a new way.",
                "Jede der vier Ebenen bewahrt eine der verstreuten Kugeln. Feuer, Erde, Wind und Wasser sind dauerhafte Kräfte: Sobald "
                "Kaya eine davon besitzt, lassen sich Räume, die sie schon hinter sich hat, neu lesen."),),
        floors={
            9: [R("T4A", ("The Lava Channels", "Die Lavakanäle"), [("Lava", "Lava"), ("Fire jets", "Feuerstrahlen")],
                  [("Three channels of glowing lava, crossed by burning rope bridges that collapse behind you, while serpent heads on "
                    "the banks breathe jets of fire.",
                    "Drei Kanäle voller glühender Lava, überspannt von brennenden Seilbrücken, die hinter dir einstürzen, während "
                    "Schlangenköpfe an den Ufern Feuerstrahlen speien.")]),
               R("T4B", ("The Ember Vault", "Das Glutgewölbe"), [("Fire Orb", "Feuerkugel")],
                  [("Raise the red Fire Orb and the Ember Censer, light the four corner braziers, and burn away the vine-choked door.",
                    "Heb die rote Feuerkugel und das Glutweihrauchfass, entzünde die vier Feuerbecken in den Ecken und brenne die von "
                    "Ranken überwucherte Tür frei.")],
                  flip=True)],
            10: [R("T4C", ("The Buried Ossuary", "Das verschüttete Beinhaus"), [("Boulders", "Felsbrocken"), ("Heavy plates", "Schwere Platten")],
                   [("A crypt of bone niches, stylized rather than gory. Push a boulder onto heavy plates while guardians crowd in; "
                     "cracked walls hide side routes.",
                     "Eine Gruft voller Knochennischen, stilisiert statt schaurig. Schieb einen Felsbrocken auf schwere Platten, während "
                     "Wächter heranströmen; rissige Wände verbergen Nebenwege.")]),
                R("T4D", ("The Root Vault", "Das Wurzelgewölbe"), [("Earth Orb", "Erdkugel")],
                   [("A root-covered sanctum. Claim the Earth Orb, and its ground-pound shatters the wall to reveal the exit.",
                     "Ein von Wurzeln überwuchertes Heiligtum. Nimm die Erdkugel, und ihr Bodenstampfer zerschmettert die Wand und "
                     "legt den Ausgang frei.")],
                   flip=True)],
            11: [R("T4E", ("The Shattered Wall", "Die zerschmetterte Mauer"), [("Gusts", "Böen"), ("Ledges", "Simse")],
                   [("A hall high in the pyramid whose outer wall has collapsed, open to the sky and the jungle canopy. Cling to narrow "
                     "ledges as gusts push you toward the edge and updrafts lift you over the gaps.",
                     "Eine Halle hoch oben in der Pyramide, deren Außenwand eingestürzt ist, offen zum Himmel und zum Blätterdach des "
                     "Dschungels. Halt dich an schmalen Simsen fest, während Böen dich zum Rand drücken und Aufwinde dich über die "
                     "Lücken heben.")]),
                R("T4F", ("The Updraft Spire", "Die Aufwindspitze"), [("Wind Orb", "Windkugel")],
                   [("A roofless spire with four swirling updraft columns. Claim the Wind Orb and glide between them to a high ledge.",
                     "Eine dachlose Turmspitze mit vier wirbelnden Aufwindsäulen. Nimm die Windkugel und gleite zwischen ihnen zu einem "
                     "hohen Sims.")],
                   flip=True)],
            12: [R("T4G", ("The Rising Cistern", "Die steigende Zisterne"), [("Rising water", "Steigendes Wasser"), ("Currents", "Strömungen")],
                   [("A huge flooded cistern whose water level keeps rising. Swim for high platforms and air-pocket alcoves against the "
                     "currents.",
                     "Eine riesige geflutete Zisterne, deren Wasserspiegel immer weiter steigt. Schwimm gegen die Strömung zu hohen "
                     "Plattformen und Nischen mit Lufttaschen.")]),
                R("T4H", ("The Reservoir Vault", "Das Reservoirgewölbe"), [("Water Orb", "Wasserkugel")],
                   [("Raise the blue Water Orb, and the water parts like walls to reveal a stone path to the Key Orb.",
                     "Heb die blaue Wasserkugel, und das Wasser teilt sich wie zwei Mauern und gibt einen Steinpfad zur Schlüsselkugel frei.")],
                   flip=True)],
        },
        set_pieces=[("T4-01", ("Lava channel kit", "Lavakanal-Kit")),
                    ("T4-02", ("Elemental Orb altars", "Altäre der Elementarkugeln")),
                    ("T4-03", ("Fire puzzle braziers and vine-choked door", "Feuerbecken des Feuerrätsels und überwucherte Tür")),
                    ("T4-04", ("Ossuary kit", "Beinhaus-Kit")),
                    ("T4-05", ("Broken rampart edge and wind banners", "Zerbrochene Wallkante und Windbanner")),
                    ("T4-06", ("Updraft vents and gust emitters", "Aufwinddüsen und Böenwerfer")),
                    ("T4-07", ("Rising cistern kit", "Kit der steigenden Zisterne"))],
        orbs=True,
    ),
    5: dict(
        title=("Tier V · The Illusion Depths", "Stufe V · Die Tiefen der Täuschung"),
        line=("The elements turned on one another.", "Die Elemente wandten sich gegeneinander."),
        lede=("Nothing is what it looks like: mirrors, illusions and totems, under pressure.",
              "Nichts ist, wie es aussieht: Spiegel, Täuschungen und Totems, unter Druck."),
        intro=(("The deepest puzzles in the temple are about perception. Light has to be bent, floors have to be doubted, and faces "
                "have to be read, all while something is chasing you. The tier ends with the Jaguar Priest.",
                "Die tiefsten Rätsel des Tempels drehen sich um Wahrnehmung. Licht muss gelenkt, Böden müssen angezweifelt und Gesichter "
                "gelesen werden, und das alles, während dich etwas verfolgt. Die Stufe endet mit dem Jaguarpriester."),),
        floors={
            13: [R("T5A", ("The Sun Shaft Hall", "Die Halle der Sonnenschächte"), [("Mirrors", "Spiegel"), ("Light", "Licht")],
                   [("Sun shafts pour through a broken ceiling. Turn the big bronze mirrors to bounce a beam into the glyph receivers, "
                     "and a stone bridge rises.",
                     "Durch eine zerbrochene Decke fallen Sonnenstrahlen. Dreh die großen Bronzespiegel, um einen Strahl in die "
                     "Glyphenempfänger zu lenken, und eine Steinbrücke hebt sich.")]),
                R("T5B", ("The Prism Vault", "Das Prismengewölbe"), [KEY, ("Colour", "Farbe")],
                   [("A dark vault. Beams split through gold, blue, red and green prisms and must strike the matching animal-head "
                     "receivers around a sealed vault.",
                     "Ein dunkles Gewölbe. Strahlen teilen sich in goldenen, blauen, roten und grünen Prismen und müssen die passenden "
                     "Tierkopfempfänger rund um ein versiegeltes Gewölbe treffen.")],
                   flip=True)],
            14: [R("T5C", ("The False Floors", "Die Trugböden"), [("Illusion", "Täuschung"), ("Scan", "Scannen")],
                   [("Some floor tiles are illusions over a pit, and some walls ripple like water. Scan before you step.",
                     "Manche Bodenfliesen sind Täuschungen über einer Grube, und manche Wände kräuseln sich wie Wasser. Scanne, bevor "
                     "du einen Schritt machst.")]),
                R("T5D", ("The Spirit Chase Hall", "Die Halle der Geisterjagd"), [KEY, ("Chase", "Verfolgung")],
                   [("A very long hall that forks twice, with one branch always an illusion, and the Guardian Spirit surging behind you.",
                     "Eine sehr lange Halle, die sich zweimal gabelt, wobei ein Zweig immer eine Täuschung ist, und hinter dir rauscht "
                     "der Wächtergeist heran.")],
                   flip=True)],
            15: [R("T5E", ("The Totem Alignment", "Die Totemausrichtung"), [("Totems", "Totems"), ("Torches", "Fackeln")],
                   [("Rotate tall animal totems, jaguar, serpent, eagle and monkey, to match the mural. Torches flare when a face is "
                     "right, and Stone Sentries patrol.",
                     "Dreh hohe Tiertotems, Jaguar, Schlange, Adler und Affe, bis sie dem Wandbild entsprechen. Fackeln lodern auf, "
                     "wenn ein Gesicht stimmt, und Steinwächter patrouillieren.")]),
                R("B2", ("The Jaguar Priest Arena", "Die Arena des Jaguarpriesters"), [("Boss", "Boss")],
                   [("The Jaguar Priest phases through shadow between four obsidian totems. Strike him at a totem to shatter it.",
                     "Der Jaguarpriester gleitet durch Schatten zwischen vier Obsidiantotems hin und her. Triff ihn an einem Totem, um "
                     "es zu zerschmettern.")],
                   flip=True, extra=("E15", ("The Jaguar Priest", "Der Jaguarpriester")))],
        },
        set_pieces=[("T5-01", ("Bronze sun mirrors, receivers and rising bridge", "Bronzene Sonnenspiegel, Empfänger und Hebebrücke")),
                    ("T5-02", ("Crystal prisms and colour-lock vault", "Kristallprismen und Farbschlossgewölbe")),
                    ("T5-03", ("Illusion tiles and false walls", "Trugfliesen und falsche Wände")),
                    ("T5-04", ("Rotating animal totems", "Drehbare Tiertotems")),
                    ("T5-05", ("The Jaguar Priest's shadow totems", "Die Schattentotems des Jaguarpriesters"))],
    ),
    6: dict(
        title=("Tier VI · The Ascension", "Stufe VI · Die Erhebung"),
        line=("A single orb chose memory over power.", "Eine einzige Kugel wählte die Erinnerung statt der Macht."),
        lede=("The last two floors: every element and every trap, and the Sun Orb.",
              "Die letzten beiden Ebenen: jedes Element und jede Falle, und die Sonnenkugel."),
        intro=(("Everything Kaya has learned is tested at once. The gauntlet asks for all four orbs in turn, the crucible throws every "
                "trap at her together, and the Priest's Lieutenant guards the vault of the Sun Orb.",
                "Alles, was Kaya gelernt hat, wird auf einmal geprüft. Der Spießrutenlauf verlangt alle vier Kugeln nacheinander, der "
                "Schmelztiegel wirft ihr jede Falle gleichzeitig entgegen, und der Leutnant des Priesters bewacht das Gewölbe der "
                "Sonnenkugel."),),
        floors={
            16: [R("T6A", ("Gauntlet I", "Spießrutenlauf I"), [("Fire", "Feuer"), ("Earth", "Erde")],
                   [("A fire section, burning vines and crossing lava bridges, then an earth section of shattered walls and heavy plates.",
                     "Ein Feuerabschnitt mit brennenden Ranken und Lavabrücken, dann ein Erdabschnitt mit zerschmetterten Wänden und "
                     "schweren Platten.")]),
                R("T6B", ("Gauntlet II", "Spießrutenlauf II"), [KEY, ("Wind", "Wind"), ("Water", "Wasser")],
                   [("A wind section of gusts and updrafts, then a water section where you part the water and ride the currents.",
                     "Ein Windabschnitt mit Böen und Aufwinden, dann ein Wasserabschnitt, in dem du das Wasser teilst und auf den "
                     "Strömungen reitest.")],
                   flip=True)],
            17: [R("T6C", ("The Trap Crucible", "Der Fallenschmelztiegel"), [("Every trap", "Alle Fallen"), ("Timed doors", "Zeittüren")],
                   [("Every trap in the temple at once, in four quadrants: saws, spikes, darts and fire jets, and crushing walls, with "
                     "timed doors between them.",
                     "Alle Fallen des Tempels auf einmal, in vier Quadranten: Sägen, Stacheln, Pfeile und Feuerstrahlen sowie "
                     "zermalmende Wände, mit Zeittüren dazwischen.")]),
                R("T6D", ("The Lieutenant's Hall", "Die Halle des Leutnants"), [("Sun Orb", "Sonnenkugel"), ("Boss", "Boss")],
                   [("The Priest's Lieutenant, an armoured warrior-priest with an eagle helmet and an obsidian spear, guards the vault of "
                     "the Sun Orb. Its exit leads to the summit.",
                     "Der Leutnant des Priesters, ein gepanzerter Kriegerpriester mit Adlerhelm und Obsidianspeer, bewacht das Gewölbe "
                     "der Sonnenkugel. Sein Ausgang führt zum Gipfel.")],
                   flip=True, extra=("E16", ("The Priest's Lieutenant", "Der Leutnant des Priesters")))],
        },
        set_pieces=[("T6-01", ("Crushing walls", "Zermalmende Wände")),
                    ("T6-02", ("Timed doors", "Zeittüren")),
                    ("T6-03", ("The Sun Orb vault and the Lieutenant's throne", "Das Gewölbe der Sonnenkugel und der Thron des Leutnants"))],
        sun=True,
    ),
}


def tier_rooms(tier):
    return [r for rooms in tier["floors"].values() for r in rooms]


def tier_page(n):
    tier = TIERS[n]

    def body(ctx):
        u, t = ctx.url, ctx.t
        floors = sorted(tier["floors"])
        first, last = floors[0], floors[-1]
        rewards = [T(ctx, FLOORS[f][4]) for f in floors if FLOORS[f][4]]
        enemies = []
        for f in floors:
            for e in T(ctx, FLOORS[f][3]).split(", "):
                if e not in enemies:
                    enemies.append(e)
        fact_rows = [
            (t("Floors", "Ebenen"), f"{first}–{last}" if first != last else str(first)),
            (t("Rooms", "Räume"), ", ".join(r[0] for r in tier_rooms(tier))),
            (t("Enemies", "Gegner"), ", ".join(enemies)),
            (t("Rewards", "Belohnungen"), "; ".join(rewards) if rewards else t("Progress toward the summit", "Fortschritt zum Gipfel")),
        ]
        intro = "".join(f"<p>{T(ctx, p)}</p>" for p in tier["intro"])
        q = t("“", "„") + T(ctx, tier["line"]) + t("”", "“")
        sections = []
        for i, f in enumerate(floors):
            rooms = "".join(room(ctx, code, name, text, scene, mp, cx, tag_pairs=tg, flip=(j % 2 == 1), extra=ex)
                            for j, (code, name, tg, text, scene, mp, cx, ex) in enumerate(tier["floors"][f]))
            band = " band" if i % 2 == 0 else ""
            sections.append(f"""
<section class="floor{band}" id="floor-{f}"><div class="wrap section">
  <div class="floor-head"><h2>{floor_title(ctx, f)}</h2>{floor_meta(ctx, f)}</div>
  {rooms}
  <p class="floor-end">{floor_end(ctx, f)}</p>
</div></section>""")
        extra = ""
        if tier.get("orbs"):
            extra = feature(ctx, "W05", None, t("The four Elemental Orbs", "Die vier Elementarkugeln"),
                            t(f"<p>Fire burns, Earth breaks, Wind lifts and Water parts. Each orb is a permanent power that stays with Kaya "
                              f"between runs, and each opens routes in floors she has already climbed.</p>"
                              f"<p><a class='text-link' href='{u('game/weapons-and-powers.html')}'>How the orbs work</a></p>",
                              f"<p>Feuer brennt, Erde bricht, Wind hebt und Wasser teilt. Jede Kugel ist eine dauerhafte Kraft, die Kaya "
                              f"über alle Durchläufe hinweg behält, und jede öffnet Wege in Ebenen, die sie schon erklommen hat.</p>"
                              f"<p><a class='text-link' href='{u('game/weapons-and-powers.html')}'>Wie die Kugeln funktionieren</a></p>"))
        if tier.get("sun"):
            extra = feature(ctx, "W06", None, t("The Sun Orb", "Die Sonnenkugel"),
                            t(f"<p>The brightest object in the game, resting in a cradle of four carved hands. Kaya carries it up the last "
                              f"stair to the <a href='{u('climb/sky-altar.html')}'>Sky Altar</a>.</p>",
                              f"<p>Das hellste Objekt im Spiel, gebettet in eine Wiege aus vier gemeißelten Händen. Kaya trägt sie die "
                              f"letzte Treppe hinauf zum <a href='{u('climb/sky-altar.html')}'>Himmelsaltar</a>.</p>"))
        extra_html = f'<section class="wrap section">{extra}</section>' if extra else ""
        return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <blockquote class="kin-line"><p>{q}</p><cite>K'in</cite></blockquote>
      {intro}
    </div>
    {facts(fact_rows)}
  </div>
</section>
{"".join(sections)}
{extra_html}
<section class="band" id="set-pieces"><div class="wrap section">
  <div class="section-head">
    <h2>{t("Set pieces", "Setpieces")}</h2>
    <a class="text-link" href="{u('art/set-pieces.html')}#tier-{n}">{t("All level set pieces", "Alle Level-Setpieces")}</a>
  </div>
  {catalog(ctx, [(i, nm, None) for i, nm in tier["set_pieces"]], cls="catalog-3")}
</div></section>
"""
    rooms = tier_rooms(tier)
    scenes = [r[4] for r in rooms]
    return dict(title=tier["title"], kicker=("The Climb", "Der Aufstieg"), lede=tier["lede"],
                description=tier["lede"], banner=scenes, og=scenes, body=body)


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
    stations = []
    for n, (img, name, tag_pairs, text, note) in enumerate(rooms, 1):
        note_html = f'<p class="station-note">{t(*note)}</p>' if note else ""
        stations.append(
            f'<li class="station"><span class="station-num" aria-hidden="true">{n}</span>'
            f'<div class="station-media">{ctx.figure(img, alt=t(*name))}</div>'
            f'<div class="station-text"><h3>{t(*name)}</h3>{tags(ctx, tag_pairs)}<p>{t(*text)}</p>{note_html}</div></li>')
    fact_rows = [
        (t("Place in the climb", "Platz im Aufstieg"), t("The first floor, below Tier I", "Die erste Ebene, unter Stufe I")),
        (t("Rooms", "Räume"), t("Nine spaces on one route", "Neun Räume auf einer Route")),
        (t("Teaches", "Lehrt"), t("Every core verb once: move, time, think, fight", "Jedes Grundverb genau einmal: laufen, timen, denken, kämpfen")),
        (t("Enemies", "Gegner"), t("One Risen Guardian", "Ein Erweckter Wächter")),
        (t("Reward", "Belohnung"), t("The obsidian macuahuitl, and the Threshold opens", "Das Obsidian-Macuahuitl, und die Schwelle öffnet sich")),
    ]
    set_pieces = [
        ("F0-01", ("The Sun Pillar", "Die Sonnensäule"), None),
        ("F0-02", ("Stepping stones and spawn platform", "Trittsteine und Startplattform"), None),
        ("F0-03", ("The sword shrine", "Der Schwertschrein"), None),
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
  <ol class="route" role="list">{"".join(stations)}</ol>
  <p class="floor-end">{t(f"Then the Portal Chamber, and up into <a href='{u('climb/tier-1.html')}'>the Flooded Foundations</a>.",
                           f"Danach die Portalkammer und hinauf in <a href='{u('climb/tier-1.html')}'>die überfluteten Fundamente</a>.")}</p>
</section>

<section class="band"><div class="wrap section">
  <div class="section-head">
    <h2>{t("Set pieces", "Setpieces")}</h2>
    <a class="text-link" href="{u('art/set-pieces.html')}#floor-0">{t("All level set pieces", "Alle Level-Setpieces")}</a>
  </div>
  {catalog(ctx, set_pieces, cls="catalog-3")}
</div></section>
"""


# ------------------------------------------------------------------ the pyramid (overview)
OVERVIEW_CARDS = [
    ("climb/threshold.html", ["A-03"], ("The Threshold", "Die Schwelle"), ("Where every climb begins", "Wo jeder Aufstieg beginnt")),
    ("climb/floor-0.html", ["B-03", "B-11"], ("Floor 0", "Ebene 0"), ("The Initiation", "Die Einweihung")),
    ("climb/tier-1.html", ["D-02", "D-04"], ("Tier I", "Stufe I"), TIERS[1]["line"]),
    ("climb/tier-2.html", ["T2A-SCENE"], ("Tier II", "Stufe II"), TIERS[2]["line"]),
    ("climb/tier-3.html", ["T3A-SCENE"], ("Tier III", "Stufe III"), TIERS[3]["line"]),
    ("climb/tier-4.html", ["T4B-SCENE"], ("Tier IV", "Stufe IV"), TIERS[4]["line"]),
    ("climb/tier-5.html", ["T5A-SCENE"], ("Tier V", "Stufe V"), TIERS[5]["line"]),
    ("climb/tier-6.html", ["T6A-SCENE"], ("Tier VI", "Stufe VI"), TIERS[6]["line"]),
    ("climb/sky-altar.html", ["E-03"], ("The Sky Altar", "Der Himmelsaltar"),
     ("The cycle begins again… unless you break it.", "Der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn.")),
]


def pyramid(ctx):
    u, t = ctx.url, ctx.t
    cards = []
    for path, imgs, name, line in OVERVIEW_CARDS:
        img = ctx.pick(*imgs)
        cards.append(f'<a class="card" href="{u(path)}">{ctx.figure(img, alt=T(ctx, name), link=False)}<span class="card-body">'
                     f'<span class="card-title">{T(ctx, name)}</span><span class="card-kicker">{T(ctx, line)}</span></span></a>')
    rows = []
    for n in range(0, 19):
        name, _, mech, _, reward = FLOORS[n]
        tier = 0 if n == 0 else 7 if n == 18 else next(k for k, v in TIERS.items() if n in v["floors"])
        path = "climb/floor-0.html" if n == 0 else "climb/sky-altar.html" if n == 18 else f"climb/tier-{tier}.html#floor-{n}"
        rows.append(f"<tr><td class='num'>{n}</td><th><a href='{u(path)}'>{T(ctx, name)}</a></th>"
                    f"<td>{T(ctx, mech)}</td><td>{T(ctx, reward) if reward else '–'}</td></tr>")
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("One pyramid, climbed from the inside: Floor 0, then seventeen floors in six tiers, then the open summit.",
                        "Eine Pyramide, von innen erklommen: Ebene 0, dann siebzehn Ebenen in sechs Stufen, dann der offene Gipfel.")}</p>
      <p>{t("Every floor runs the same way. Room A, then Room B, which holds the floor's Key Orb, then the Portal Chamber, where Kaya "
            "sockets the orb, K'in speaks one line, a fragment of the mural lights, and she ascends. Every room has two arrival pads "
            "for co-op and exactly one golden idol.",
            "Jede Ebene läuft gleich ab. Raum A, dann Raum B mit der Schlüsselkugel der Ebene, dann die Portalkammer: Dort setzt Kaya "
            "die Kugel ein, K'in spricht einen Satz, ein Fragment des Wandbilds leuchtet auf, und sie steigt weiter. Jeder Raum hat "
            "zwei Ankunftsfelder für den Koop-Modus und genau ein goldenes Idol.")}</p>
      <p>{t("Puzzles scale with the climb: one mechanic per room in Tiers I and II, combined mechanics in III and IV, and layered "
            "perception puzzles under pressure in V and VI.",
            "Die Rätsel wachsen mit dem Aufstieg: eine Mechanik pro Raum in den Stufen I und II, kombinierte Mechaniken in III und IV "
            "und vielschichtige Wahrnehmungsrätsel unter Druck in V und VI.")}</p>
    </div>
    {facts([(t("Floors", "Ebenen"), t("Floor 0, 17 floors in six tiers, the summit", "Ebene 0, 17 Ebenen in sechs Stufen, der Gipfel")),
            (t("Per floor", "Pro Ebene"), t("Room A, Room B with the Key Orb, Portal Chamber", "Raum A, Raum B mit Schlüsselkugel, Portalkammer")),
            (t("Bosses", "Bosse"), t("Gearwarden, Jaguar Priest, Priest's Lieutenant, Hollow High Priest", "Zahnradwächter, Jaguarpriester, Leutnant des Priesters, Hohler Hohepriester")),
            (t("Co-op", "Koop"), t("Two arrival pads in every room", "Zwei Ankunftsfelder in jedem Raum"))])}
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("From the Threshold to the sun", "Von der Schwelle zur Sonne")}</h2>
  <div class="cards cards-3">{"".join(cards)}</div>
</div></section>

<section class="wrap section">
  <div class="pair pair-wide">
    {ctx.figure("CX-00", t("The codex map Kaya finds inside the pyramid. In the game its pages are collectible maps and loading screens.",
                         "Die Codexkarte, die Kaya in der Pyramide findet. Im Spiel sind ihre Seiten sammelbare Karten und Ladebildschirme."))}
    {ctx.figure("HOME-CLIMB", t("The pyramid in cutaway, floor by floor", "Die Pyramide im Schnitt, Ebene für Ebene"))}
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("The campaign, floor by floor", "Die Kampagne, Ebene für Ebene")}</h2>
  <div class="table-wrap"><table class="orb-table campaign">
    <thead><tr><th>{t("Floor", "Ebene")}</th><th>{t("Name", "Name")}</th><th>{t("New mechanic", "Neue Mechanik")}</th><th>{t("Reward", "Belohnung")}</th></tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table></div>
</div></section>
"""


# ------------------------------------------------------------------ the Threshold hub
def threshold_hub(ctx):
    u, t = ctx.url, ctx.t
    stations = [
        ("HUB06", ("The round altar", "Der runde Altar"),
         ("K'in waits above it and greets Kaya after every return, with a line that changes as the climb goes on.",
          "K'in schwebt darüber und begrüßt Kaya nach jeder Rückkehr, mit einem Satz, der sich im Lauf des Aufstiegs verändert.")),
        ("HUB12", ("Six tier shortcut pads", "Sechs Abkürzungsfelder"),
         ("Three on each side wall, one per tier. Clear a tier and its pad lights, so a later run can start higher up.",
          "Drei an jeder Seitenwand, eines pro Stufe. Ist eine Stufe geschafft, leuchtet ihr Feld, und ein späterer Durchlauf kann "
          "weiter oben beginnen.")),
        ("HUB10", ("The offering table", "Der Opfertisch"),
         ("Oxlahun's shop: healing, upgrades and new gear, paid for in coins and Spirit Fragments.",
          "Oxlahuns Laden: Heilung, Verbesserungen und neue Ausrüstung, bezahlt mit Münzen und Geistsplittern.")),
        ("HUB11", ("The codex lectern", "Das Codex-Lesepult"),
         ("The codex and lore menu. Every codex page Kaya finds on the way up is added here.",
          "Das Menü für Codex und Hintergrundwissen. Jede Codexseite, die Kaya auf dem Weg nach oben findet, kommt hierher.")),
        ("HUB08", ("The Spirit Mural", "Das Geisterwandbild"),
         ("The progress wall. Each cleared floor lights another fragment of the temple's history.",
          "Die Wand des Fortschritts. Jede geschaffte Ebene lässt ein weiteres Fragment der Tempelgeschichte aufleuchten.")),
    ]
    modes = [
        (("The Ascent", "Der Aufstieg"), ("Middle portal · Story", "Mittleres Portal · Geschichte"),
         ("The campaign, floor by floor to the summit. Open from the start.",
          "Die Kampagne, Ebene für Ebene bis zum Gipfel. Von Anfang an offen.")),
        (("Trials of the Shifting Temple", "Prüfungen des wandelnden Tempels"), ("Left portal", "Linkes Portal"),
         ("Sealed until Kaya reaches the summit for the first time.", "Versiegelt, bis Kaya zum ersten Mal den Gipfel erreicht.")),
        (("Expedition", "Expedition"), ("Right portal", "Rechtes Portal"),
         ("Sealed until a tier has been cleared.", "Versiegelt, bis eine Stufe geschafft ist.")),
    ]
    mode_html = "".join(f'<div class="mode"><p class="mode-where">{T(ctx, w)}</p><h3>{T(ctx, n)}</h3><p>{T(ctx, d)}</p></div>'
                        for n, w, d in modes)
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("The Threshold is where the game lives between runs: where you practise, choose a mode, spend what you earned "
                      "and see how far you have come.",
                      "Die Schwelle ist der Ort, an dem das Spiel zwischen den Durchläufen lebt: Hier übst du, wählst einen Modus, "
                      "gibst aus, was du verdient hast, und siehst, wie weit du gekommen bist.")}</p>
    <p>{t(f"This page is about how the hub plays. For its history and the clues hidden in it, see <a href='{u('world/threshold.html')}'>World: The Threshold</a>.",
          f"Diese Seite zeigt, wie der Hub funktioniert. Seine Geschichte und die darin versteckten Hinweise findest du unter <a href='{u('world/threshold.html')}'>Welt: Die Schwelle</a>.")}</p>
  </div>
  {pair(ctx, "A-02", t("The hall and the forecourt from above", "Halle und Vorplatz von oben"),
        "CX-HUB", t("The same hall as a codex page", "Dieselbe Halle als Codexseite"))}
</section>

<section class="band"><div class="wrap section">
  <h2>{t("Outside: the forecourt", "Draußen: der Vorplatz")}</h2>
  {feature(ctx, "HUB01", None, t("The explorer camp", "Das Forscherlager"),
           t("<p>Kaya's camp at the foot of the pyramid: tent, campfire and kettle, a map table and crates. The game starts here, and "
             "the pyramid is always in view.</p>",
             "<p>Kayas Lager am Fuß der Pyramide: Zelt, Lagerfeuer und Kessel, ein Kartentisch und Kisten. Hier beginnt das Spiel, "
             "und die Pyramide ist immer im Blick.</p>"))}
  {feature(ctx, "HUB02", None, t("Training ground", "Übungsplatz"),
           t("<p>Straw dummies with painted faces and a stone target. Practise every weapon here, with nothing at stake.</p>",
             "<p>Strohpuppen mit aufgemalten Gesichtern und eine Zielscheibe aus Stein. Hier übst du jede Waffe, ohne dass etwas "
             "auf dem Spiel steht.</p>"), flip=True)}
  {feature(ctx, "HUB05", None, t("The tunnel", "Der Tunnel"),
           t("<p>Two giant feathered serpents frame the tunnel into the hall, under a carved sun mask. Walking through it is the "
             "moment the game turns from outside to inside.</p>",
             "<p>Zwei riesige gefiederte Schlangen rahmen den Tunnel in die Halle, unter einer gemeißelten Sonnenmaske. Der Gang "
             "hindurch ist der Moment, in dem das Spiel von draußen nach drinnen wechselt.</p>"))}
</div></section>

<section class="wrap section">
  <h2>{t("Inside: the hall as hub", "Drinnen: die Halle als Hub")}</h2>
  {feature(ctx, "HUB07", None, t("Three portals, three modes", "Drei Portale, drei Modi"),
           t("<p>Three round portals stand on the dais beneath the mural. Each one is a game mode.</p>",
             "<p>Drei runde Portale stehen auf dem Podest unter dem Wandbild. Jedes davon ist ein Spielmodus.</p>"))}
  <div class="modes">{mode_html}</div>
  {catalog(ctx, stations, cls="catalog-hub")}
</section>

<section class="band"><div class="wrap section">
  <div class="section-head">
    <h2>{t("Threshold and forecourt assets", "Assets für Schwelle und Vorplatz")}</h2>
    <a class="text-link" href="{u('art/threshold-set.html')}">{t("The full set", "Das komplette Set")}</a>
  </div>
  {catalog(ctx, [("HUB03", ("Jungle foliage kit", "Dschungel-Pflanzen-Kit"), None),
                 ("HUB04", ("Pyramid exterior kit", "Kit für die Außenseite der Pyramide"), None),
                 ("A-04", ("The jungle and the camp", "Der Dschungel und das Lager"), None)], cls="catalog-3")}
</div></section>
"""


# ------------------------------------------------------------------ shared rooms
def shared_rooms(ctx):
    u, t = ctx.url, ctx.t
    pc = room(ctx, "PC", ("The Portal Chamber", "Die Portalkammer"),
              [("Every floor ends here. Kaya arrives and hears K'in's line at the mural fragment, banks her coins or buys a heal at the "
                "small offering shrine, climbs the three-step dais, sets the Key Orb in the socket of carved cupped hands, and walks "
                "into the great round Portal Door.",
                "Jede Ebene endet hier. Kaya kommt an und hört K'ins Satz am Fragment des Wandbilds, bringt ihre Münzen in Sicherheit "
                "oder kauft am kleinen Opferschrein eine Heilung, steigt das dreistufige Podest hinauf, setzt die Schlüsselkugel in "
                "die Schale aus gemeißelten Händen und geht durch die große runde Portaltür."),
               ("A small blue return portal goes home to the Threshold with progress saved. One shared room replaces seventeen "
                "separate portal rooms.",
                "Ein kleines blaues Rückkehrportal führt mit gespeichertem Fortschritt zurück zur Schwelle. Ein gemeinsamer Raum "
                "ersetzt siebzehn einzelne Portalräume.")],
              "C-02", "C-01", "CX-PC01", tag_pairs=[("End of every floor", "Ende jeder Ebene")])
    sr = room(ctx, "SR", ("The Spirit Shrine", "Der Geisterschrein"),
              [("A calm safe room before each tier's last Portal Chamber: a candlelit altar, a basin of glowing healing water, and three "
                "relics to choose a blessing from, a gold sun amulet, a green jade necklace and a blue shell charm.",
                "Ein ruhiger, sicherer Raum vor der letzten Portalkammer jeder Stufe: ein Altar im Kerzenschein, ein Becken mit "
                "leuchtendem Heilwasser und drei Relikte, aus denen Kaya einen Segen wählt: ein goldenes Sonnenamulett, eine grüne "
                "Jadekette und ein blauer Muschelanhänger.")],
              "C-04", "C-03", "CX-SR01", tag_pairs=[("End of every tier", "Ende jeder Stufe"), ("Safe room", "Sicherer Raum")], flip=True)
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("Two rooms appear again and again on the way up. They are where the climb pauses: to bank what you carry, to "
                      "hear K'in, and to breathe.",
                      "Zwei Räume tauchen auf dem Weg nach oben immer wieder auf. In ihnen hält der Aufstieg inne: um zu sichern, "
                      "was du trägst, um K'in zu hören und um durchzuatmen.")}</p>
  </div>
</section>
<section class="band" id="portal-chamber"><div class="wrap section">{pc}</div></section>
<section class="wrap section" id="spirit-shrine">{sr}</section>
<section class="band"><div class="wrap section">
  <div class="section-head">
    <h2>{t("Set pieces", "Setpieces")}</h2>
    <a class="text-link" href="{u('art/set-pieces.html')}#shared-rooms">{t("All level set pieces", "Alle Level-Setpieces")}</a>
  </div>
  {catalog(ctx, [("PC01", ("Portal Chamber set", "Set der Portalkammer"), None),
                 ("SR01", ("Spirit Shrine set", "Set des Geisterschreins"), None)], cls="catalog-3")}
</div></section>
"""


# ------------------------------------------------------------------ the Sky Altar
def sky_altar(ctx):
    u, t = ctx.url, ctx.t
    q = t("“", "„") + t("The cycle begins again… unless you break it.", "Der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn.") + t("”", "“")
    boss = ""
    if ctx.has("E17"):
        boss = f'<div class="drawing-wide">{ctx.figure("E17", t("The Hollow High Priest, boss sheet", "Der Hohle Hohepriester, Boss-Blatt"), cls="sheet")}</div>'
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <blockquote class="kin-line"><p>{q}</p><cite>K'in</cite></blockquote>
      <p>{t("The summit is the only floor under the open sky: a circular glyph arena with four broken columns, four great braziers in "
            "the corners, red for fire, blue for water, white for wind and green for earth, and the small summit temple with the dark "
            "Sun Portal.",
            "Der Gipfel ist die einzige Ebene unter freiem Himmel: eine runde Glyphenarena mit vier zerbrochenen Säulen, vier großen "
            "Feuerbecken in den Ecken, rot für Feuer, blau für Wasser, weiß für Wind und grün für Erde, und der kleine Gipfeltempel "
            "mit dem dunklen Sonnenportal.")}</p>
    </div>
    {facts([(t("Floor", "Ebene"), "18"), (t("Boss", "Boss"), t("The Hollow High Priest", "Der Hohle Hohepriester")),
            (t("Ending", "Ende"), t("Restore the cycle, or break it", "Den Kreislauf wiederherstellen oder durchbrechen")),
            (t("Afterwards", "Danach"), t("Trials of the Shifting Temple unlocks", "Die Prüfungen des wandelnden Tempels werden freigeschaltet"))])}
  </div>
  {pair(ctx, "E-01", t("The plateau from above", "Das Plateau von oben"), "CX-SKY", t("The summit as a codex page", "Der Gipfel als Codexseite"))}
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "E-02", None, t("The fight", "Der Kampf"),
           t(f"<p>The <a href='{u('characters/hollow-high-priest.html')}'>Hollow High Priest</a>, the order's former head, waits on the "
             f"plateau with four stolen lights circling in his open ribcage. His boss phases are played on the braziers: each one ties "
             f"the fight to an element Kaya has learned on the way up.</p>",
             f"<p>Der <a href='{u('characters/hollow-high-priest.html')}'>Hohle Hohepriester</a>, einst das Oberhaupt des Ordens, "
             f"wartet auf dem Plateau, vier gestohlene Lichter kreisen in seinem offenen Brustkorb. Seine Bossphasen spielen an den "
             f"Feuerbecken: Jede verbindet den Kampf mit einem Element, das Kaya auf dem Weg nach oben gelernt hat.</p>"))}
  {feature(ctx, "E-03", None, t("The choice", "Die Wahl"),
           t(f"<p>Kaya places the Sun Orb on the altar before the Sun Portal. Two pedestals flank it: gold to restore the cycle, violet "
             f"to break it. What each choice costs is told in <a href='{u('story/index.html')}'>the story</a>.</p>"
             f"<p>After the first summit, the left portal in the Threshold opens: Trials of the Shifting Temple.</p>",
             f"<p>Kaya legt die Sonnenkugel auf den Altar vor dem Sonnenportal. Zwei Sockel stehen daneben: gold, um den Kreislauf "
             f"wiederherzustellen, violett, um ihn zu durchbrechen. Was jede Wahl kostet, erzählt <a href='{u('story/index.html')}'>die "
             f"Geschichte</a>.</p><p>Nach dem ersten Gipfel öffnet sich das linke Portal in der Schwelle: die Prüfungen des wandelnden "
             f"Tempels.</p>"), flip=True)}
  {boss}
</div></section>

<section class="wrap section">
  <div class="section-head">
    <h2>{t("Set pieces", "Setpieces")}</h2>
    <a class="text-link" href="{u('art/set-pieces.html')}#sky-altar">{t("All level set pieces", "Alle Level-Setpieces")}</a>
  </div>
  {catalog(ctx, [("SKY-01", ("Summit temple and Sun Portal", "Gipfeltempel und Sonnenportal"), None),
                 ("SKY-02", ("The four elemental braziers", "Die vier Elementar-Feuerbecken"), None),
                 ("SKY-03", ("Sun Orb altar and the two choice pedestals", "Altar der Sonnenkugel und die beiden Sockel der Wahl"), None)], cls="catalog-3")}
</section>
"""


PAGES = {
    "climb/index.html": dict(
        title=("The Pyramid", "Die Pyramide"), kicker=("The Climb", "Der Aufstieg"),
        lede=("Floor 0, seventeen floors in six tiers, and the summit.", "Ebene 0, siebzehn Ebenen in sechs Stufen und der Gipfel."),
        description=("The structure of the climb in Ascent of the Sun Temple, from the Threshold to the Sky Altar.",
                     "Der Aufbau des Aufstiegs in Ascent of the Sun Temple, von der Schwelle bis zum Himmelsaltar."),
        banner=["HOME-CLIMB"], og=["HOME-CLIMB"], body=pyramid),
    "climb/threshold.html": dict(
        title=("The Threshold Hub", "Die Schwelle (Hub)"), kicker=("The Climb", "Der Aufstieg"),
        lede=("Practise, choose a mode, spend what you earned, and see how far you have come.",
              "Üben, einen Modus wählen, ausgeben, was du verdient hast, und sehen, wie weit du gekommen bist."),
        description=("How the Threshold works as the game's hub: camp, portals, shortcuts, shop, codex and mural.",
                     "Wie die Schwelle als Hub des Spiels funktioniert: Lager, Portale, Abkürzungen, Laden, Codex und Wandbild."),
        banner=["A-03"], og=["A-03"], body=threshold_hub),
    "climb/floor-0.html": dict(
        title=("Floor 0 · The Initiation", "Ebene 0 · Die Einweihung"), kicker=("The Climb", "Der Aufstieg"),
        lede=("The tutorial floor: nine spaces on one route, and every core verb taught once.",
              "Die Tutorial-Ebene: neun Räume auf einer Route, und jedes Grundverb wird genau einmal gelehrt."),
        description=("Floor 0, The Initiation: the tutorial floor of Ascent of the Sun Temple, room by room.",
                     "Ebene 0, Die Einweihung: die Tutorial-Ebene von Ascent of the Sun Temple, Raum für Raum."),
        banner=["B-03", "B-11"], og=["B-02", "B-11"], body=floor_0),
    "climb/sky-altar.html": dict(
        title=("The Sky Altar", "Der Himmelsaltar"), kicker=("The Climb", "Der Aufstieg"),
        lede=("Floor 18: the open summit, the last fight, and the choice.",
              "Ebene 18: der offene Gipfel, der letzte Kampf und die Wahl."),
        description=("The Sky Altar, the summit of the Sun Temple: the plateau, the final fight and the ending choice.",
                     "Der Himmelsaltar, der Gipfel des Sonnentempels: das Plateau, der letzte Kampf und die Wahl am Ende."),
        banner=["E-02", "E-03"], og=["E-02", "E-03"], body=sky_altar),
    "climb/shared-rooms.html": dict(
        title=("Shared Rooms", "Gemeinsame Räume"), kicker=("The Climb", "Der Aufstieg"),
        lede=("The Portal Chamber that ends every floor, and the Spirit Shrine that ends every tier.",
              "Die Portalkammer am Ende jeder Ebene und der Geisterschrein am Ende jeder Stufe."),
        description=("The Portal Chamber and the Spirit Shrine, the two rooms shared by every floor of the climb.",
                     "Die Portalkammer und der Geisterschrein, die beiden Räume, die alle Ebenen des Aufstiegs teilen."),
        banner=["C-02", "C-04"], og=["C-02", "C-04"], body=shared_rooms),
}
for _n in TIERS:
    PAGES[f"climb/tier-{_n}.html"] = tier_page(_n)
