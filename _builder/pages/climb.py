"""The Climb tab (English and German): the pyramid overview, the hub, every floor and the summit.

Images that are not uploaded yet render as placeholders that show their ID.
"""
from components import T, catalog, facts, feature, pair, room, run_strip, shape_glyph, tags

# ------------------------------------------------------------------ campaign data
# One row per floor: number, name, rooms, new mechanic, enemies, reward (None = no reward).
FLOORS = {
    0: (("The Shell", "The Shell"), "F0", ("All core verbs, your first death", "Alle Grundverben, dein erster Tod"),
        ("Risen Guardian", "Erweckter Wächter"), ("Obsidian macuahuitl, the goggles, the Threshold", "Obsidian-Macuahuitl, die Brille, die Schwelle")),
    1: (("The Drowned Gallery", "Die ertrunkene Galerie"), "T1A · T1B",
        ("Water as the level's state, Finds, the Portal Chamber's choice", "Wasser als Zustand der Ebene, Funde, die Wahl in der Portalkammer"),
        ("Risen Guardians, Risen Novices, Drowned Risen, Temple Leeches", "Erweckte Wächter, Erweckte Novizen, Ertrunkene Erweckte, Tempelegel"), ("Oxlahun's Waystall bell", "Oxlahuns Rastplatzglocke")),
    2: (("The Root Cellars", "Die Wurzelkeller"), "T1C · T1D",
        ("Swings, slick slopes, ranged combat, shields", "Schwingen, rutschige Hänge, Fernkampf, Schilde"),
        ("Cave Bats, Risen Bearers", "Höhlenfledermäuse, Erweckte Schildträger"), ("Spirit Blowgun; the first Lens-only crack", "Geisterblasrohr; der erste Riss, den nur die Linse zeigt")),
    3: (("The Sump", "Der Sumpf"), "SUMP",
        ("Your first boss, your first Sun Gate", "Dein erster Boss, dein erstes Sonnentor"),
        ("The Mire Mother", "Die Schlammmutter"), ("Tier II Sun Gate", "Sonnentor zu Stufe II")),
    4: (("Hall of Blades", "Halle der Klingen"), "T2A · T2B",
        ("Saws, pendulums, plate order, luring enemies into traps", "Sägen, Pendel, Plattenfolge, Gegner in Fallen locken"),
        ("Scarab Swarms, Husk Archers", "Skarabäenschwärme, Hülsenschützen"), ("Sunburst Sling, found on the floor", "Sonnenschleuder, auf der Ebene gefunden")),
    5: (("The Dart Colonnade", "Die Pfeilkolonnade"), "T2C · T2D",
        ("Darts, shield statues, thieves, a big wave fight", "Pfeile, Schildstatuen, Diebe, ein großer Wellenkampf"),
        ("Thief Monkeys, Obsidian Panther, Censer Priest", "Diebesaffen, Obsidianpanther, Räucherpriester"), None),
    6: (("The Builders' Workshop", "Die Werkstatt der Erbauer"), "WORK",
        ("Build your own traps; recut the temple's", "Eigene Fallen bauen; die des Tempels nachmeißeln"),
        ("Marching waves of Risen", "Marschierende Wellen von Erweckten"), ("Isabel's Chisel and the Trap Ledger", "Isabels Meißel und das Fallenverzeichnis")),
    7: (("The Breathing Court", "Der atmende Hof"), "COURT",
        ("Watchers, freezing, the heist", "Wächteraugen, Erstarren, der Raubzug"),
        ("Eye-Bearers, Thief Monkeys", "Augenträger, Diebesaffen"), ("Serpent Roll; the Great Idol, if you dare", "Schlangenrolle; das Große Idol, wenn du dich traust")),
    8: (("The Collapsing Stair", "Die einstürzende Treppe"), "T2E · T2F",
        ("Crumbling stairs, boulders, the first chase", "Bröckelnde Treppen, Felsbrocken, die erste Verfolgung"),
        ("Guardian Spirit, Chak Tun", "Wächtergeist, Chak Tun"), ("Tier III Sun Gate", "Sonnentor zu Stufe III")),
    9: (("The Tilting Sanctum", "Das kippende Heiligtum"), "T3A · T3B",
        ("Seesaws, weighted floors, rotating discs", "Wippen, gewichtsabhängige Böden, rotierende Scheiben"),
        ("Stone Sentries, Husk Archers", "Steinwächter, Hülsenschützen"), None),
    10: (("The Counting Well", "Der zählende Brunnen"), "WELL",
         ("K'in's calls; the day signs as a language", "K'ins Rufe; die Tageszeichen als Sprache"),
         ("Bone Hurlers, Risen Bearers, Stone Sentry", "Knochenwerfer, Erweckte Schildträger, Steinwächter"), ("The Sign Lexicon", "Das Zeichen-Lexikon")),
    11: (("The Vanishing Path", "Der verschwindende Pfad"), "T3C · T3D",
         ("Phasing platforms, song stones, the memory path", "Phasende Plattformen, Klangsteine, der Gedächtnispfad"),
         ("Stone Sentries, Bone Hurlers", "Steinwächter, Knochenwerfer"), ("Lens II: hidden paths hold while you look", "Linse II: verborgene Pfade tragen, solange du hinsiehst")),
    12: (("The Gear Ascent", "Der Zahnradaufstieg"), "T3E · B1",
         ("Lifts, gears, timed switches, a rival", "Aufzüge, Zahnräder, Zeitschalter, ein Rivale"),
         ("Gear Crawlers, the Priest's Lieutenant, the Gearwarden", "Zahnradkrabbler, der Leutnant des Priesters, der Zahnradwächter"), ("Tier IV Sun Gate", "Sonnentor zu Stufe IV")),
    13: (("The Sun Well", "Der Sonnenbrunnen"), "RING",
         ("A hub with four wings, in the order you choose", "Ein Knotenpunkt mit vier Flügeln, in beliebiger Reihenfolge"),
         ("Roaming Risen, Guardian Spirit, the Fourfold Echo", "Umherstreifende Erweckte, Wächtergeist, das Vierfache Echo"), ("Tier V Sun Gate", "Sonnentor zu Stufe V")),
    14: (("The Ember Forge", "Die Glutschmiede"), "T4A · T4B",
         ("Lava, fire jets, burning bridges", "Lava, Feuerstrahlen, brennende Brücken"),
         ("Magma Salamanders, the Salamander Queen", "Magmasalamander, die Salamanderkönigin"), ("Fire Orb, Ember Censer", "Feuerkugel, Glutweihrauchfass")),
    15: (("The Buried Ossuary", "Das verschüttete Beinhaus"), "T4C · T4D",
         ("Cracked walls, heavy plates, crowds", "Rissige Wände, schwere Platten, Massen"),
         ("A crowd of Risen, Strangler Vines, the Strangler", "Erweckte in Scharen, Würgeranken, der Würger"), ("Earth Orb", "Erdkugel")),
    16: (("The Broken Ramparts", "Die zerbrochenen Wälle"), "T4E · T4F",
         ("Wind gusts, updrafts, open to the sky", "Windböen, Aufwinde, offen zum Himmel"),
         ("Gale Husks, the Lieutenant, the Stormwing Husk", "Sturmhülsen, der Leutnant, die Sturmschwinge"), ("Wind Orb", "Windkugel")),
    17: (("The Sunken Reservoir", "Das versunkene Reservoir"), "T4G · T4H",
         ("Rising water, currents, air pockets", "Steigendes Wasser, Strömungen, Lufttaschen"),
         ("Drowned Risen, Panthers, the Cenote Serpent Elder", "Ertrunkene Erweckte, Panther, die Alte Cenote-Schlange"), ("Water Orb", "Wasserkugel")),
    18: (("The Mirror Sanctum", "Das Spiegelheiligtum"), "T5A",
         ("Mirrors, the reading gallery", "Spiegel, die Lesegalerie"),
         ("Mirror Shades, Husk Archers", "Spiegelschatten, Hülsenschützen"), ("Mirror Step; the jaguar glyph", "Spiegelschritt; die Jaguarglyphe")),
    19: (("The Prism Vault", "Das Prismengewölbe"), "T5B",
         ("Colour mixing under attack", "Farben mischen unter Beschuss"),
         ("Mirror Shades, Stone Sentry", "Spiegelschatten, Steinwächter"), ("Serpent glyph", "Schlangenglyphe")),
    20: (("The Hall of Lies", "Die Halle der Lügen"), "T5C · TWIN · T5D",
         ("False floors, twin halls, your own Echo", "Trugböden, Zwillingshallen, dein eigenes Echo"),
         ("Mirror Shades, the Lieutenant, Guardian Spirit", "Spiegelschatten, der Leutnant, Wächtergeist"), ("Monkey glyph", "Affenglyphe")),
    21: (("The Totem Vault", "Das Totemgewölbe"), "T5E · B2",
         ("A totem order you have to work out", "Eine Totemfolge, die du herausfinden musst"),
         ("The Jaguar Priest", "Der Jaguarpriester"), ("Tier VI Sun Gate", "Sonnentor zu Stufe VI")),
    22: (("The Elemental Gauntlet", "Der Elementarspießrutenlauf"), "T6A · T6B",
         ("All four orbs, one route", "Alle vier Kugeln, eine Route"),
         ("Elite Guardians", "Elite-Wächter"), None),
    23: (("The Trap Crucible", "Der Fallenschmelztiegel"), "T6C",
         ("Every trap; your chisel at full strength", "Alle Fallen; dein Meißel in voller Stärke"),
         ("Everything", "Alles"), None),
    24: (("The Inner Sanctum", "Das innere Heiligtum"), "T6D",
         ("The last duel, the vault", "Das letzte Duell, das Gewölbe"),
         ("The Priest's Lieutenant", "Der Leutnant des Priesters"), ("The Sun Orb", "Die Sonnenkugel")),
    25: (("The Last Breath", "Der letzte Atem"), "LAST",
         ("Carrying the Sun Orb through a temple that's awake", "Die Sonnenkugel durch einen hellwachen Tempel tragen"),
         ("Guardian Spirit, Eye-Bearers, everything", "Wächtergeist, Augenträger, alles"), ("The way to the summit", "Der Weg zum Gipfel")),
    26: (("The Sky Altar", "Der Himmelsaltar"), "SKY",
         ("Boss phases on the braziers, the final choice", "Bossphasen an den Feuerbecken, die letzte Wahl"),
         ("The Hollow High Priest", "Der Hohle Hohepriester"), ("The ending; the Trials open", "Das Ende; die Prüfungen öffnen sich")),
}
LAST_FLOOR = 26
# Side view (DESIGN_SideScroller_Floors.md §5): the direction each floor runs in, and its size in screens.
# H across, V up or down, D diagonal, R a ring around a well, A an arena; "H>A" runs across into an arena.
SHAPES = {0: ("H>V", 17), 1: ("H", 20), 2: ("V", 26), 3: ("H>A", 10), 4: ("H", 28), 5: ("H", 22), 6: ("H", 12),
          7: ("V", 18), 8: ("D", 18), 9: ("H", 22), 10: ("V", 12), 11: ("H", 20), 12: ("V", 26), 13: ("R", 10),
          14: ("V", 20), 15: ("V", 20), 16: ("H", 20), 17: ("V", 20), 18: ("H", 18), 19: ("V", 18), 20: ("H", 20),
          21: ("H>A", 16), 22: ("V", 28), 23: ("H", 22), 24: ("H>A", 16), 25: ("V", 20), 26: ("A", 6)}


def floor_title(ctx, n):
    return ctx.t(f"Floor {n} · ", f"Ebene {n} · ") + T(ctx, FLOORS[n][0])


def floor_meta(ctx, n):
    _, _, mech, enemies, reward = FLOORS[n]
    t = ctx.t
    shape, screens = SHAPES[n]
    rows = [(t("Shape", "Form"), f"{shape_glyph(ctx, shape)} {t(f'{screens} screens', f'{screens} Bildschirme')}"),
            (t("New", "Neu"), T(ctx, mech)), (t("Enemies", "Gegner"), T(ctx, enemies))]
    if reward:
        rows.append((t("Reward", "Belohnung"), T(ctx, reward)))
    return '<dl class="floor-meta">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def floor_end(ctx, n):
    u, t = ctx.url, ctx.t
    pc = f"<a href='{u('climb/shared-rooms.html')}#portal-chamber'>{t('Portal Chamber', 'Portalkammer')}</a>"
    if n == 24:
        return t("The vault opens, and the Sun Orb is yours. Now you have to get it out.",
                 "Das Gewölbe öffnet sich, und die Sonnenkugel gehört dir. Jetzt musst du sie hinausbringen.")
    if n == 25:
        return t(f"Daylight, and the doors of the <a href='{u('climb/sky-altar.html')}'>Sky Altar</a>.",
                 f"Tageslicht und die Tore zum <a href='{u('climb/sky-altar.html')}'>Himmelsaltar</a>.")
    if n in (14, 15, 16, 17):
        return t("Then back down to the Sun Well and its shrine. Pick another wing, or go home alive.",
                 "Dann zurück hinunter zum Sonnenbrunnen und seinem Schrein. Wähl einen anderen Flügel oder geh lebend nach Hause.")
    return t(f"Then the {pc}, and the stair up.", f"Danach die {pc} und die Treppe nach oben.")


# ------------------------------------------------------------------ tiers
# Each room: (code, name, tags, paragraphs, scene, map, codex, extra)
def R(code, name, tag_pairs, text, scene=None, map_id=None, codex=None, extra=None, flip=False):
    """flip is accepted for readability only: rooms alternate sides automatically.
    map_id and codex are left over from the top-down design and are no longer shown."""
    return (code, name, tag_pairs, text, scene or f"{code}-SCENE", None, None, extra)


KEY = ("Key Orb room", "Raum der Schlüsselkugel")

# further images for a room, by room code; each appears once it has been uploaded
MORE_ART = {
    "COURT": [("HYB-SCENE2", ("The Spike Court", "Der Stachelhof")), ("HYB-SCENE3", ("The Great Idol", "Das Große Idol"))],
    "WELL": [("CF-DRUMS", ("The drums", "Die Trommeln"))],
    "T3D": [("F11-SONG", ("The song stones", "Die Singsteine"))],
    "T4E": [("ACT-LT-AMBUSH", ("The Lieutenant", "Der Leutnant"))],
    "T6C": [("F23-SCENE", ("Every trap, turned", "Alle Fallen, umgedreht"))],
}

TIERS = {
    1: dict(
        title=("Tier I · The Flooded Foundations", "Stufe I · Die überfluteten Fundamente"),
        line=("The ancients harnessed balance.", "Die Alten bändigten das Gleichgewicht."),
        lede=("The temple's flooded base: water, leeches, the first ranged weapon and the first boss.",
              "Die geflutete Basis des Tempels: Wasser, Egel, die erste Fernkampfwaffe und der erste Boss."),
        intro=(("Three floors at the foot of the pyramid, where the builders first held the elements in balance and the water never "
                "left. Here water is the level's state: every floor has a water line that Kaya changes, and the change stays. This is "
                "where you learn a run: shrines, shortcuts, keeping your health, and deciding when to stop.",
                "Drei Ebenen am Fuß der Pyramide, wo die Erbauer die Elemente zum ersten Mal im Gleichgewicht hielten und das Wasser "
                "nie wieder abfloss. Hier ist das Wasser der Zustand der Ebene: Jede Ebene hat eine Wasserlinie, die Kaya verändert, und "
                "die Veränderung bleibt. Hier lernst du einen Durchlauf: Schreine, Abkürzungen, Gesundheit bewahren und entscheiden, wann du aufhörst."),),
        floors={
            1: [R("T1A", ("The Drowned Gallery", "Die ertrunkene Galerie"), [("Water", "Wasser"), ("Timing", "Timing")],
                  [("Four screens of stone islands over dark leech water, with floating logs drifting between them on a slow current. "
                    "A log sinks a little under Kaya, and further under two Risen. Drowned Risen surface along the route: a ripple shows "
                    "you where.",
                    "Vier Bildschirme voller Steininseln über dunklem Egelwasser, dazwischen treiben Baumstämme in einer langsamen Strömung. "
                    "Ein Stamm sinkt unter Kaya ein wenig ein, unter zwei Erweckten noch tiefer. Entlang des Wegs tauchen Ertrunkene Erweckte "
                    "auf: Eine Kräuselung zeigt dir, wo."),
                   ("The idol lies under the west ledge, and the leeches are the timer for the dive. Two things stay out of reach for "
                    "now: an idol on a ledge too high to jump, and a deep current that throws you back.",
                    "Das Idol liegt unter dem Westsims, und die Egel sind die Uhr für den Tauchgang. Zwei Dinge bleiben vorerst außer "
                    "Reichweite: ein Idol auf einem Sims, zu hoch für jeden Sprung, und eine tiefe Strömung, die dich zurückwirft.")],
                  scene="D-02"),
               R("T1B", ("The Sluice Hall", "Die Schleusenhalle"), [KEY, ("Drain", "Abfluss"), ("Shaft", "Schacht")],
                  [("A shaft three screens deep. The Key Orb lies at the bottom of a channel with a strong current: swim down with it, "
                    "past the leeches. A plate on a balcony on the way down opens the sluice, and the whole lower floor drains for good.",
                    "Ein Schacht, drei Bildschirme tief. Die Schlüsselkugel liegt am Grund eines Kanals mit starker Strömung: Schwimm mit "
                    "ihr hinab, an den Egeln vorbei. Eine Platte auf einem Balkon auf halbem Weg öffnet die Schleuse, und die ganze untere "
                    "Ebene läuft leer, für immer."),
                   ("Taking the orb wakes three Risen. The lift up takes eight seconds: fight on its platform, or jump for the stairs. "
                    "Below, the drained gallery is a dry walk back to the Entry Shrine, and a plate lift you open from below becomes the "
                    "floor's shortcut.",
                    "Wer die Kugel nimmt, weckt drei Erweckte. Der Aufzug nach oben braucht acht Sekunden: Kämpf auf seiner Plattform "
                    "oder spring zur Treppe. Darunter führt die trockengelegte Galerie zurück zum Eingangsschrein, und ein Plattenaufzug, "
                    "den du von unten öffnest, wird zur Abkürzung der Ebene.")],
                  scene="D-04")],
            2: [R("T1C", ("The Root Cellar", "Der Wurzelkeller"), [("Swing", "Schwingen"), ("Slope", "Hang"), ("Climb", "Aufstieg")],
                  [("A tall root shaft, climbed from the bottom. Slick moss slopes slide Kaya back down unless she jumps, and vine "
                    "swings cross the shaft: hold to swing, let go to fly, and keep the momentum.",
                    "Ein hoher Wurzelschacht, von unten erklommen. Rutschige Moosflächen tragen Kaya wieder hinab, wenn sie nicht "
                    "springt, und Ranken schwingen quer durch den Schacht: halten, um zu schwingen, loslassen, um zu fliegen, und den Schwung behalten."),
                   ("Cave bats dive with a screech. A fall costs a little health and drops you a level into a pit of slow Risen: "
                    "falling is a lower route, never a restart. In the dark fungus pit, the glowing caps are the only light, and bursting "
                    "one poisons whatever stands near it.",
                    "Höhlenfledermäuse stoßen kreischend herab. Ein Sturz kostet etwas Gesundheit und lässt dich eine Etage tiefer in eine "
                    "Grube voller langsamer Erweckter fallen: Fallen ist ein tieferer Weg, nie ein Neustart. In der dunklen Pilzgrube sind "
                    "die leuchtenden Hüte das einzige Licht, und wer einen platzen lässt, vergiftet, was in der Nähe steht.")],
                  scene="D-06"),
               R("T1D", ("The Blowgun Shrine", "Der Blasrohrschrein"), [KEY, ("Ranged", "Fernkampf"), ("New key", "Neuer Schlüssel")],
                  [("At the top of the shaft, Kaya takes the Spirit Blowgun. Three glyph targets rise high on the walls, and every hit "
                    "wakes two Risen below, so she shoots while she's chased. The last target raises the Key Orb.",
                    "Oben im Schacht nimmt Kaya das Geisterblasrohr. Drei Glyphenziele steigen hoch an den Wänden auf, und jeder Treffer "
                    "weckt unten zwei Erweckte, also schießt sie, während sie gejagt wird. Das letzte Ziel hebt die Schlüsselkugel."),
                   ("On the way out, a far target across the shaft drops a root bridge: the first use of the new key, and a shortcut "
                    "straight back down to the Mid Shrine. In the Portal Chamber, the Lens shows a thin crack that K'in's path walks past.",
                    "Auf dem Rückweg lässt ein fernes Ziel auf der anderen Seite des Schachts eine Wurzelbrücke fallen: der erste Einsatz "
                    "des neuen Schlüssels und eine Abkürzung direkt hinunter zum Mittleren Schrein. In der Portalkammer zeigt die Linse einen "
                    "feinen Riss, an dem K'ins Pfad vorbeiführt.")],
                  scene="D-08")],
            3: [R("SUMP", ("The Mire Mother's Cistern", "Die Zisterne der Schlammmutter"), [("Boss", "Boss"), ("Drain", "Abfluss")],
                  [("A long, low overflow channel first, where the water rises on a cycle from ankle to over your head, then a pump hall "
                    "that teaches the boss's rule: water down means danger exposed. Then the cistern, side-on: four stone islands at two "
                    "heights, four sluice gates in the walls, and the Mire Mother, an enormous glossy leech with glowing teal spots.",
                    "Zuerst ein langer, niedriger Überlaufkanal, in dem das Wasser im Takt vom Knöchel bis über den Kopf steigt, dann eine "
                    "Pumpenhalle, die die Regel des Bosses lehrt: Wasser runter heißt Gefahr offen. Dann die Zisterne, von der Seite: vier "
                    "Steininseln auf zwei Höhen, vier Schleusentore in den Wänden und die Schlammmutter, ein riesiger glänzender Egel mit "
                    "leuchtend türkisen Flecken."),
                   ("Her spots glow before she lunges: roll under the arc and strike her side, or pogo off her back. When she sinks out "
                    "of reach, shoot the sluice targets with the Blowgun and leave her beached. Beat her, and the first Sun Gate lights.",
                    "Ihre Flecken glühen, bevor sie zustößt: Roll unter dem Bogen hindurch und triff ihre Seite, oder federe von ihrem "
                    "Rücken ab. Taucht sie außer Reichweite, schieß mit dem Blasrohr auf die Schleusenziele und lass sie auf dem Trockenen "
                    "liegen. Besiege sie, und das erste Sonnentor leuchtet auf.")],
                  scene=["F3-SCENE", "D-04"], extra=("ACT-BOSS-MIRE", ("The Mire Mother", "Die Schlammmutter")))],
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
        lede=("Five floors of traps: blades, darts, a workshop, a temple that breathes, and the first chase.",
              "Fünf Ebenen voller Fallen: Klingen, Pfeile, eine Werkstatt, ein Tempel, der atmet, und die erste Verfolgung."),
        intro=(("After the betrayal, the priests turned the galleries into a defence. Every trap here has a rhythm you can learn, and every trap "
                "hurts your enemies too. By the end of this tier you'll be building them yourself.",
                "Nach dem Verrat machten die Priester die Galerien zu einer Verteidigungsanlage. Jede Falle hier hat einen Rhythmus, den "
                "du lernen kannst, und jede Falle trifft auch deine Feinde. Am Ende dieser Stufe baust du sie selbst."),),
        floors={
            4: [R("T2A", ("The Saw Gallery", "Die Sägengalerie"), [("Blades", "Klingen"), ("Lanes", "Bahnen")],
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
            5: [R("T2C", ("The Dart Colonnade", "Die Pfeilkolonnade"), [("Darts", "Pfeile"), ("Cover", "Deckung")],
                  [("A long pillared colonnade. Darts shoot from bat-face masks in the pillars and fire vents flare in the floor.",
                    "Eine lange Säulenkolonnade. Aus Fledermausmasken in den Säulen schießen Pfeile, und im Boden lodern Feuerdüsen auf."),
                   ("Rotate the stone shield statues to block the dart lanes. Archers hold a gallery at the far end.",
                    "Dreh die steinernen Schildstatuen, um die Schussbahnen zu blockieren. Am anderen Ende halten Schützen eine Galerie.")]),
               R("T2D", ("The Orb Guard Court", "Der Hof der Kugelwacht"), [KEY, ("Wave fight", "Wellenkampf")],
                  [("A combat court around a raised dais that holds the Key Orb, ringed by fire vents.",
                    "Ein Kampfhof um ein erhöhtes Podest mit der Schlüsselkugel, umringt von Feuerdüsen."),
                   ("A wave fight: guardians first, then archers on the corner plinths, then the first Obsidian Panther.",
                    "Ein Wellenkampf: zuerst Wächter, dann Schützen auf den Ecksockeln, dann der erste Obsidianpanther.")])],
            6: [R("WORK", ("The Builders' Workshop", "Die Werkstatt der Erbauer"), [("Build", "Bauen"), ("Defend", "Verteidigen"), ("Run", "Laufen")],
                  [("The workshop where the temple's trap makers worked. A chisel lies on the bench, and the slots in the corridor outside still answer to anyone who knows the old glyphs.",
                    "Die Werkstatt, in der die Fallenbauer des Tempels arbeiteten. Auf der Werkbank liegt ein Meißel, und die Plätze im Gang draußen hören noch immer auf jeden, der die alten Glyphen kennt."),
                   ("You have sixty seconds and a budget to fill each section: spikes, fire vents, crumbling tiles, fake floors, boulder plates, dart walls and swinging blades. Then the Risen march. Fight beside your traps through three waves.",
                    "Du hast sechzig Sekunden und ein Budget, um jeden Abschnitt zu füllen: Stacheln, Feuerdüsen, bröckelnde Fliesen, Trugböden, Felsplatten, Pfeilwände und Pendelklingen. Dann marschieren die Erweckten. Kämpf drei Wellen lang an der Seite deiner Fallen."),
                   ("Then the gate opens at the far end of the corridor, and your traps are still running. You have to run what you built. The temple has rules, so there's always a way through, and from now on you can recut any marked trap in the game.",
                    "Dann öffnet sich das Tor am anderen Ende des Gangs, und deine Fallen laufen noch. Du musst durch das laufen, was du gebaut hast. Der Tempel hat Regeln, also gibt es immer einen Weg hindurch, und ab jetzt kannst du jede markierte Falle im Spiel nachmeißeln.")],
                  scene=["F6-SCENE", "T2A-SCENE"], extra=("F6-RUN", ("Running what you built", "Durch das laufen, was du gebaut hast")))],
            7: [R("COURT", ("The Breathing Court", "Der atmende Hof"), [("Freeze", "Erstarren"), ("Heist", "Raubzug")],
                  [("The Sun Temple sleeps, and it breathes. When it holds its breath, stone faces in the walls open their eyes. Stirring, the eyes glow orange. Looking, they blaze gold, and anything that moves is blown back and drops what it carries. Green leaf-glyph shade hides you.",
                    "Der Sonnentempel schläft, und er atmet. Wenn er den Atem anhält, öffnen Steingesichter in den Wänden ihre Augen. Regen sie sich, glühen die Augen orange. Sehen sie hin, lodern sie golden, und alles, was sich bewegt, wird zurückgeblasen und verliert, was es trägt. Grüne Blattglyphen spenden Schatten und verstecken dich."),
                   ("Four rooms, each with its own beat: the Entry Hall, the Gallery of Eyes, the Spike Court, where you also have to stand on gold, and the Jaguar Sanctum. The Risen freeze when the temple looks, so you can walk up to them. Eye-Bearers don't. Thief Monkeys are after the same idols you are.",
                    "Vier Räume, jeder mit eigenem Takt: die Eingangshalle, die Galerie der Augen, der Stachelhof, in dem du außerdem auf Gold stehen musst, und das Jaguarheiligtum. Die Erweckten erstarren, wenn der Tempel hinsieht, du kannst also zu ihnen hingehen. Augenträger erstarren nicht. Diebesaffen sind hinter denselben Idolen her wie du."),
                   ("The Key Orb sits beside the Great Idol, the richest single thing on this tier. You only need the orb. Take the idol as well, and the whole temple wakes, the carrier glows, and the Serpent Door opens onto a fast, shadeless way home over a crumbling bridge.",
                    "Die Schlüsselkugel liegt neben dem Großen Idol, dem Wertvollsten dieser Stufe. Du brauchst nur die Kugel. Nimmst du auch das Idol, erwacht der ganze Tempel, die Trägerin leuchtet, und die Schlangentür öffnet einen schnellen, schattenlosen Heimweg über eine bröckelnde Brücke.")],
                  scene=["HYB-SCENE1", "T2A-SCENE"], extra=("HYB-SCENE4", ("The Serpent Run", "Der Schlangenlauf")))],
            8: [R("T2E", ("The Collapsing Stair", "Die einstürzende Treppe"), [("Crumbling", "Bröckeln"), ("Boulders", "Felsbrocken")],
                  [("A tall shaft of zig-zag stair flights. The steps crumble behind you while boulders roll down toward you.",
                    "Ein hoher Schacht aus Treppenläufen im Zickzack. Die Stufen bröckeln hinter dir weg, während Felsbrocken auf dich "
                    "zurollen.")]),
               R("T2F", ("The Chase Shaft", "Der Fluchtschacht"), [KEY, ("Chase", "Verfolgung")],
                  [("A spiral ramp around a dark void. A huge, unkillable Guardian Spirit rises from below, and the ramp crumbles behind "
                    "you. The first chase: run.",
                    "Eine Spiralrampe um einen dunklen Abgrund. Von unten steigt ein riesiger, unbesiegbarer Wächtergeist auf, und die "
                    "Rampe zerbröckelt hinter dir. Die erste Verfolgung: Lauf.")],
                  flip=True),
               R("MARGIN", ("The Margin", "Der Rand"), [("Boss", "Boss")],
                  [("A long gallery whose walls are carved panels, and the last thing you expect: the carving at the edge of the wall has stepped down from it. Chak Tun, Warden of the Panels, walks the gallery with his staff, hides in one panel and steps out of another. The Lens shows you which stone is fresh.",
                    "Eine lange Galerie, deren Wände aus gemeißelten Tafeln bestehen, und das Letzte, was du erwartest: Das Relief am Rand der Wand ist herabgestiegen. Chak Tun, Wächter der Tafeln, geht mit seinem Stab durch die Galerie, verschwindet in einer Tafel und tritt aus einer anderen. Die Linse zeigt dir, welcher Stein frisch ist.")],
                  scene=["ACT-BOSS-CHAKTUN", "T2B-SCENE"])],
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
        intro=(("From here on, rooms combine mechanics. The floor tilts under your weight, platforms phase in and out on a beat, the day signs "
                "become a language, and K'in can only show you the way once. The tier ends in the Gearwarden's arena.",
                "Ab hier verbinden die Räume mehrere Mechaniken. Der Boden kippt unter deinem Gewicht, Plattformen erscheinen und "
                "verschwinden im Takt, die Tageszeichen werden zu einer Sprache, und K'in kann dir den Weg nur ein einziges Mal zeigen. "
                "Die Stufe endet in der Arena des Zahnradwächters."),),
        floors={
            9: [R("T3A", ("The Seesaw Hall", "Die Wippenhalle"), [("Weight", "Gewicht"), ("Tilt", "Neigung")],
                  [("Long stone seesaws over a deep pit tilt toward the side with more weight on it, and that includes your enemies. A tilting "
                    "bridge follows, and archers watch from the side ledges.",
                    "Lange steinerne Wippen über einer tiefen Grube kippen zu der Seite mit dem meisten Gewicht, und dazu zählen auch deine Feinde. Danach "
                    "folgt eine kippende Brücke, und Schützen lauern auf den Seitensimsen.")]),
               R("T3B", ("The Disc Well", "Der Scheibenbrunnen"), [KEY, ("Rotation", "Drehung")],
                  [("Rotating stone discs, carved like calendar wheels, spiral up a tall well at different speeds. The Key Orb waits on "
                    "the highest one.",
                    "Rotierende Steinscheiben, gemeißelt wie Kalenderräder, winden sich in unterschiedlichem Tempo einen hohen Brunnen "
                    "hinauf. Die Schlüsselkugel wartet auf der obersten.")],
                  flip=True)],
            10: [R("WELL", ("The Counting Well", "Der zählende Brunnen"), [("Signs", "Zeichen"), ("Survive", "Überleben")],
                   [("A square shaft with three stone calendar wheels stacked over a sacred well. Every stone carries one of the five day signs. K'in calls a sign, and every stone that wears it glows, shakes and drops. Then the wheels click round under your feet.",
                     "Ein quadratischer Schacht mit drei übereinanderliegenden Kalenderrädern aus Stein über einem heiligen Brunnen. Jeder Stein trägt eines der fünf Tageszeichen. K'in ruft ein Zeichen, und jeder Stein, der es trägt, glüht, bebt und fällt. Dann rücken die Räder unter deinen Füßen weiter."),
                    ("Enemies fall too, and the Risen can't read. Fight them on the signs that are about to go. A fall lands you on the wheel below; the well costs far more. From Dawn to Eclipse the calls speed up, until K'in stops telling you what falls and tells you only what holds.",
                     "Auch Gegner fallen, und die Erweckten können nicht lesen. Bekämpf sie auf den Zeichen, die gleich verschwinden. Ein Sturz bringt dich auf das Rad darunter; der Brunnen kostet weit mehr. Von der Morgendämmerung bis zur Finsternis werden die Rufe schneller, bis K'in dir nicht mehr sagt, was fällt, sondern nur noch, was hält."),
                    ("Five glyph drums stand on the rim. Shoot one, and the next call favours that sign. It's the first time you tell the temple what to do. On later runs she stops saying the names, and you have to read them.",
                     "Fünf Glyphentrommeln stehen am Rand. Schieß auf eine, und der nächste Ruf begünstigt dieses Zeichen. Es ist das erste Mal, dass du dem Tempel sagst, was er tun soll. In späteren Durchläufen sagt sie die Namen nicht mehr, und du musst sie lesen.")],
                   scene=["CF-SCENE1", "T3B-SCENE"], extra=("CF-SCENE2", ("Eclipse", "Finsternis")))],
            11: [R("T3C", ("The Phase Bridges", "Die Phasenbrücken"), [("Phasing", "Phasen"), ("Rhythm", "Rhythmus")],
                  [("Square platforms flicker between solid stone and glowing outlines over a void, in three colour-keyed groups. "
                    "K'in pulses on the beat.",
                    "Quadratische Plattformen flackern über einem Abgrund zwischen festem Stein und leuchtenden Umrissen, in drei "
                    "farbcodierten Gruppen. K'in pulsiert im Takt.")]),
               R("T3D", ("The Memory Path", "Der Gedächtnispfad"), [KEY, ("Memory", "Gedächtnis")],
                  [("Play K'in's song back on the song stones, and for a moment a winding path of floating steps appears over a pit. Then it is gone, "
                    "and you walk it from memory while Stone Sentries patrol below.",
                    "Spiel K'ins Lied auf den Klangsteinen nach, und für einen Moment erscheint ein gewundener Pfad aus schwebenden Stufen über einer "
                    "Grube. Dann ist er verschwunden, und du gehst ihn aus dem Gedächtnis, während unten Steinwächter patrouillieren."),
                   ("Or lower your goggles, and pay in Focus to see the whole path. You may see more than she showed you.",
                    "Oder senk die Brille und bezahl mit Fokus, um den ganzen Pfad zu sehen. Vielleicht siehst du mehr, als sie dir gezeigt hat.")],
                  flip=True)],
            12: [R("T3E", ("The Gear Shaft", "Der Zahnradschacht"), [("Gears", "Zahnräder"), ("Timed switches", "Zeitschalter")],
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
        lede=("Four sanctums around the Sun Well, in the order you choose: the tier where Kaya claims the Elemental Orbs.",
              "Vier Heiligtümer um den Sonnenbrunnen, in beliebiger Reihenfolge: die Stufe, in der Kaya die Elementarkugeln erringt."),
        intro=(("This tier opens onto the Sun Well, a round hall with four archways. Behind each wing waits one of the scattered orbs, and you choose the order. "
                "Fire, Earth, Wind and Water are permanent powers: once Kaya holds one, every floor she's already climbed reads in a new way. The more orbs you own, the harder the wings get.",
                "Diese Stufe öffnet sich zum Sonnenbrunnen, einer runden Halle mit vier Bögen. Hinter jedem Flügel wartet eine der verstreuten Kugeln, und du wählst die Reihenfolge. "
                "Feuer, Erde, Wind und Wasser sind dauerhafte Kräfte: Sobald Kaya eine davon besitzt, liest sich jede Ebene, die sie schon erklommen hat, neu. Je mehr Kugeln du besitzt, desto härter werden die Flügel."),),
        floors={
            13: [R("RING", ("The Sun Well", "Der Sonnenbrunnen"), [("Hub", "Knotenpunkt"), ("Boss", "Boss")],
                   [("A huge round hall around a sealed vault over a pit of light, with four archways glowing red, green, white and blue. Risen roam the ring, and from your second orb on, a Guardian Spirit patrols it. You can see it coming and go around it.",
                     "Eine riesige runde Halle um ein versiegeltes Gewölbe über einer Grube aus Licht, mit vier Bögen, die rot, grün, weiß und blau leuchten. Erweckte streifen durch den Ring, und ab deiner zweiten Kugel patrouilliert dort ein Wächtergeist. Du siehst ihn kommen und kannst ihm ausweichen."),
                    ("Between wings you can rest at the basin, take another wing, or go home alive. When all four orbs are yours, the vault opens, and something tall made of their light is standing in the pit.",
                     "Zwischen den Flügeln kannst du am Becken rasten, den nächsten Flügel nehmen oder lebend nach Hause gehen. Wenn alle vier Kugeln dir gehören, öffnet sich das Gewölbe, und etwas Hohes aus ihrem Licht steht in der Grube.")],
                   scene=["F13-SCENE", "T4B-SCENE"], extra=("ACT-BOSS-ECHO", ("The Fourfold Echo", "Das Vierfache Echo")))],
            14: [R("T4A", ("The Lava Channels", "Die Lavakanäle"), [("Lava", "Lava"), ("Fire jets", "Feuerstrahlen")],
                  [("Three channels of glowing lava, crossed by burning rope bridges that collapse behind you, while serpent heads on "
                    "the banks breathe jets of fire.",
                    "Drei Kanäle voller glühender Lava, überspannt von brennenden Seilbrücken, die hinter dir einstürzen, während "
                    "Schlangenköpfe an den Ufern Feuerstrahlen speien.")]),
               R("T4B", ("The Ember Vault", "Das Glutgewölbe"), [("Fire Orb", "Feuerkugel")],
                  [("Raise the red Fire Orb and the Ember Censer, light the four corner braziers, and burn away the vine-choked door. Behind it, the Salamander Queen waits in her lava.",
                    "Heb die rote Feuerkugel und das Glutweihrauchfass, entzünde die vier Feuerbecken in den Ecken und brenne die von "
                    "Ranken überwucherte Tür frei. Dahinter wartet die Salamanderkönigin in ihrer Lava.")],
                  flip=True, extra=("ACT-GUARD-SALAMANDER", ("The Salamander Queen", "Die Salamanderkönigin")))],
            15: [R("T4C", ("The Buried Ossuary", "Das verschüttete Beinhaus"), [("Boulders", "Felsbrocken"), ("Heavy plates", "Schwere Platten")],
                   [("A crypt of bone niches, stylized rather than gory. Push a boulder onto heavy plates while guardians crowd in; "
                     "cracked walls hide side routes.",
                     "Eine Gruft voller Knochennischen, stilisiert statt schaurig. Schieb einen Felsbrocken auf schwere Platten, während "
                     "Wächter heranströmen; rissige Wände verbergen Nebenwege.")]),
                R("T4D", ("The Root Vault", "Das Wurzelgewölbe"), [("Earth Orb", "Erdkugel")],
                   [("A root-covered sanctum. Claim the Earth Orb, and its ground-pound shatters the wall. Beyond it, the Strangler has been growing for a long time.",
                     "Ein von Wurzeln überwuchertes Heiligtum. Nimm die Erdkugel, und ihr Bodenstampfer zerschmettert die Wand. Dahinter "
                     "wächst der Würger schon sehr lange.")],
                   flip=True, extra=("ACT-GUARD-STRANGLER", ("The Strangler", "Der Würger")))],
            16: [R("T4E", ("The Shattered Wall", "Die zerschmetterte Mauer"), [("Gusts", "Böen"), ("Ledges", "Simse")],
                   [("A hall high in the pyramid whose outer wall has collapsed, open to the sky and the jungle canopy. Cling to narrow "
                     "ledges as gusts push you toward the edge and updrafts lift you over the gaps.",
                     "Eine Halle hoch oben in der Pyramide, deren Außenwand eingestürzt ist, offen zum Himmel und zum Blätterdach des "
                     "Dschungels. Halt dich an schmalen Simsen fest, während Böen dich zum Rand drücken und Aufwinde dich über die "
                     "Lücken heben.")]),
                R("T4F", ("The Updraft Spire", "Die Aufwindspitze"), [("Wind Orb", "Windkugel")],
                   [("A roofless spire with four swirling updraft columns. Claim the Wind Orb and glide between them to a high ledge, where the Stormwing Husk rides the storm.",
                     "Eine dachlose Turmspitze mit vier wirbelnden Aufwindsäulen. Nimm die Windkugel und gleite zwischen ihnen zu einem "
                     "hohen Sims, wo die Sturmschwinge den Sturm reitet.")],
                   flip=True, extra=("ACT-GUARD-STORMWING", ("The Stormwing Husk", "Die Sturmschwinge")))],
            17: [R("T4G", ("The Rising Cistern", "Die steigende Zisterne"), [("Rising water", "Steigendes Wasser"), ("Currents", "Strömungen")],
                   [("A huge flooded cistern whose water level keeps rising. Swim for high platforms and air-pocket alcoves against the "
                     "currents.",
                     "Eine riesige geflutete Zisterne, deren Wasserspiegel immer weiter steigt. Schwimm gegen die Strömung zu hohen "
                     "Plattformen und Nischen mit Lufttaschen.")]),
                R("T4H", ("The Reservoir Vault", "Das Reservoirgewölbe"), [("Water Orb", "Wasserkugel")],
                   [("Raise the blue Water Orb, and the water parts like walls to reveal a stone path. The Cenote Serpent Elder swims through those walls.",
                     "Heb die blaue Wasserkugel, und das Wasser teilt sich wie zwei Mauern und gibt einen Steinpfad frei. Die Alte Cenote-Schlange schwimmt durch diese Mauern.")],
                   flip=True, extra=("ACT-GUARD-SERPENT", ("The Cenote Serpent Elder", "Die Alte Cenote-Schlange")))],
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
        intro=(("The deepest puzzles in the temple are about perception, and this is where a reader is at home. Each room has a raised reading gallery: from up there the Lens shows the truth "
                "of the room, but the mechanisms are down on the floor. You read, you remember, and you act, under attack. The tier ends with the Jaguar Priest.",
                "Die tiefsten Rätsel des Tempels drehen sich um Wahrnehmung, und hier ist eine Leserin zu Hause. Jeder Raum hat eine erhöhte Lesegalerie: Von dort oben zeigt die Linse die Wahrheit "
                "des Raums, aber die Mechanismen liegen unten. Du liest, du merkst es dir und du handelst, unter Beschuss. Die Stufe endet mit dem Jaguarpriester."),),
        floors={
            18: [R("T5A", ("The Sun Shaft Hall", "Die Halle der Sonnenschächte"), [("Mirrors", "Spiegel"), ("Light", "Licht")],
                   [("Sun shafts pour through a broken ceiling. Turn the big bronze mirrors to bounce a beam into the glyph receivers, "
                     "and a stone bridge rises. Enemies who stand in a beam burn.",
                     "Durch eine zerbrochene Decke fallen Sonnenstrahlen. Dreh die großen Bronzespiegel, um einen Strahl in die "
                     "Glyphenempfänger zu lenken, und eine Steinbrücke hebt sich. Gegner, die im Strahl stehen, verbrennen."),
                  ("Mirror Shades walk the hall: faceless figures that split into copies, and only the real one has a gold crack. Then the sun moves, and you have to do it all again.",
                   "Spiegelschatten gehen durch die Halle: gesichtslose Gestalten, die sich in Kopien teilen, und nur die echte hat einen goldenen Riss. Dann wandert die Sonne, und du musst alles noch einmal tun.")])],
            19: [R("T5B", ("The Prism Vault", "Das Prismengewölbe"), [KEY, ("Colour", "Farbe")],
                   [("A dark vault. Beams split through gold, blue, red and green prisms and must strike the matching animal-head "
                     "receivers around a sealed vault. Some receivers need a mixed colour, and the recipe is written in glyphs on the wall. A wrong mix floods the vault with fire, which burns your enemies too.",
                     "Ein dunkles Gewölbe. Strahlen teilen sich in goldenen, blauen, roten und grünen Prismen und müssen die passenden "
                     "Tierkopfempfänger rund um ein versiegeltes Gewölbe treffen. Manche Empfänger brauchen eine gemischte Farbe, und das Rezept steht in Glyphen an der Wand. Eine falsche Mischung flutet das Gewölbe mit Feuer, das auch deine Feinde verbrennt.")],
                   flip=True)],
            20: [R("T5C", ("The False Floors", "Die Trugböden"), [("Illusion", "Täuschung"), ("Lens", "Linse")],
                   [("Some floor tiles are illusions over a pit, and some walls ripple like water. Read before you step, or watch where the Risen won't walk.",
                     "Manche Bodenfliesen sind Täuschungen über einer Grube, und manche Wände kräuseln sich wie Wasser. Lies, bevor "
                     "du einen Schritt machst, oder achte darauf, wo die Erweckten nicht hintreten.")]),
                R("TWIN", ("The Twin Halls", "Die Zwillingshallen"), [("Your Echo", "Dein Echo"), ("Spirit glass", "Geisterglas")],
                   [("The hall splits behind a wall of spirit glass. On the far side walks a golden Echo of Kaya, copying every move half a step behind. You can see the true floor of her hall, but not your own. Walk your route so she survives hers, and reach the exit plates together.",
                     "Die Halle teilt sich hinter einer Wand aus Geisterglas. Auf der anderen Seite geht ein goldenes Echo von Kaya, das jede Bewegung einen halben Schritt später nachahmt. Du siehst den wahren Boden ihrer Halle, aber nicht den deiner eigenen. Geh deine Route so, dass sie ihre überlebt, und erreicht die Ausgangsplatten gemeinsam."),
                    ("Once, through the glass, she turns and looks back at you. She isn't supposed to do that.",
                     "Einmal dreht sie sich durch das Glas zu dir um und sieht dich an. Das sollte sie nicht können.")],
                   scene=["F20-TWIN", "T5C-SCENE"], flip=True),
                R("T5D", ("The Spirit Chase Hall", "Die Halle der Geisterjagd"), [KEY, ("Chase", "Verfolgung")],
                   [("A very long hall that forks twice, with one branch always an illusion, and the Guardian Spirit surging behind you.",
                     "Eine sehr lange Halle, die sich zweimal gabelt, wobei ein Zweig immer eine Täuschung ist, und hinter dir rauscht "
                     "der Wächtergeist heran.")],
                   flip=True)],
            21: [R("T5E", ("The Totem Alignment", "Die Totemausrichtung"), [("Totems", "Totems"), ("Torches", "Fackeln")],
                   [("Rotate tall animal totems, jaguar, serpent, eagle and monkey. The mural is broken, so the order comes from the glyphs you earned on the floors below. Torches flare when a face is "
                     "right, Stone Sentries patrol, and a shadow walks the room and undoes any totem it passes.",
                     "Dreh hohe Tiertotems, Jaguar, Schlange, Adler und Affe. Das Wandbild ist zerbrochen, also ergibt sich die Reihenfolge aus den Glyphen, die du auf den Ebenen darunter errungen hast. Fackeln lodern auf, "
                     "wenn ein Gesicht stimmt, Steinwächter patrouillieren, und ein Schatten geht durch den Raum und macht jedes Totem rückgängig, an dem er vorbeikommt.")]),
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
        lede=("The last four floors: every element, every trap, the Sun Orb, and getting it out alive.",
              "Die letzten vier Ebenen: jedes Element, jede Falle, die Sonnenkugel und der Weg lebend hinaus."),
        intro=(("Everything you've learned is tested at once. The gauntlet asks for all four orbs on one route, the crucible throws every trap at you and gives your chisel its "
                "last test, and the Priest's Lieutenant guards the vault of the Sun Orb. Then you have to carry it out.",
                "Alles, was du gelernt hast, wird auf einmal geprüft. Der Spießrutenlauf verlangt alle vier Kugeln auf einer Route, der Schmelztiegel wirft dir jede Falle entgegen und stellt "
                "deinen Meißel ein letztes Mal auf die Probe, und der Leutnant des Priesters bewacht das Gewölbe der Sonnenkugel. Dann musst du sie hinaustragen."),),
        floors={
            22: [R("T6A", ("Gauntlet I", "Spießrutenlauf I"), [("Fire", "Feuer"), ("Earth", "Erde")],
                   [("A fire section, burning vines and crossing lava bridges, then an earth section of shattered walls and heavy plates.",
                     "Ein Feuerabschnitt mit brennenden Ranken und Lavabrücken, dann ein Erdabschnitt mit zerschmetterten Wänden und "
                     "schweren Platten.")]),
                R("T6B", ("Gauntlet II", "Spießrutenlauf II"), [KEY, ("Wind", "Wind"), ("Water", "Wasser")],
                   [("A wind section of gusts and updrafts, then a water section where you part the water and ride the currents.",
                     "Ein Windabschnitt mit Böen und Aufwinden, dann ein Wasserabschnitt, in dem du das Wasser teilst und auf den "
                     "Strömungen reitest.")],
                   flip=True)],
            23: [R("T6C", ("The Trap Crucible", "Der Fallenschmelztiegel"), [("Every trap", "Alle Fallen"), ("Timed doors", "Zeittüren")],
                   [("Every trap in the temple at once, in four quadrants: saws, spikes, darts and fire jets, and crushing walls, with "
                     "timed doors between them. Recut what you can, and let them do your work.",
                     "Alle Fallen des Tempels auf einmal, in vier Quadranten: Sägen, Stacheln, Pfeile und Feuerstrahlen sowie "
                     "zermalmende Wände, mit Zeittüren dazwischen. Meißle nach, was du kannst, und lass sie deine Arbeit tun.")])],
            24: [R("T6D", ("The Lieutenant's Hall", "Die Halle des Leutnants"), [("Sun Orb", "Sonnenkugel"), ("Boss", "Boss")],
                   [("The Priest's Lieutenant, an armoured warrior-priest with an eagle helmet and an obsidian spear, has ambushed you three times on the way up, and walked away each time. "
                     "He guards the vault of the Sun Orb, and this time he doesn't leave.",
                     "Der Leutnant des Priesters, ein gepanzerter Kriegerpriester mit Adlerhelm und Obsidianspeer, hat dich auf dem Weg nach oben dreimal überfallen und ist jedes Mal gegangen. "
                     "Er bewacht das Gewölbe der Sonnenkugel, und diesmal geht er nicht.")],
                   flip=True, extra=("E16", ("The Priest's Lieutenant", "Der Leutnant des Priesters")))],
            25: [R("LAST", ("The Last Breath", "Der letzte Atem"), [("Escape", "Flucht"), ("Sun Orb", "Sonnenkugel")],
                   [("Carrying the Sun Orb is the heaviest thing you've done. You glow, and shade doesn't hide you. Every watcher in the temple is awake. There is no Waystall and no shrine, only one basin halfway. If you die, the orb goes back to its vault.",
                     "Die Sonnenkugel zu tragen ist das Schwerste, was du je getan hast. Du leuchtest, und Schatten versteckt dich nicht. Jedes Wächterauge im Tempel ist wach. Es gibt keinen Rastplatz und keinen Schrein, nur ein Becken auf halbem Weg. Stirbst du, kehrt die Kugel in ihr Gewölbe zurück."),
                    ("Everything comes back for one last climb: the long stair with a spirit behind you, a hall of giant faces, one last calendar, and a mirror walk. K'in stops speaking on this floor, for the first time since you met her.",
                     "Alles kehrt für einen letzten Aufstieg zurück: die lange Treppe mit einem Geist im Rücken, eine Halle voller riesiger Gesichter, ein letzter Kalender und ein Spiegelgang. K'in hört auf dieser Ebene auf zu sprechen, zum ersten Mal, seit du sie getroffen hast.")],
                   scene=["F25-SCENE", "T6C-SCENE"])],
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
            (t("Screens", "Bildschirme"), str(sum(SHAPES[f][1] for f in floors))),
            (t("Signature rooms", "Prägende Räume"), ", ".join(r[0] for r in tier_rooms(tier))),
            (t("Enemies", "Gegner"), ", ".join(enemies)),
            (t("Rewards", "Belohnungen"), "; ".join(rewards) if rewards else t("Progress toward the summit", "Fortschritt zum Gipfel")),
        ]
        intro = "".join(f"<p>{T(ctx, p)}</p>" for p in tier["intro"])
        if n != 1:
            intro += ("<p class='tier-note'>" + t("Below are each floor's signature rooms. In side view, every floor is a hand-built level around them, "
                                                  "with its Sun Shrines, shortcuts and reward doors; the full floor sheets are drawn one tier at a time.",
                                                  "Unten stehen die prägenden Räume jeder Ebene. In der Seitenansicht ist jede Ebene ein von Hand gebautes Level um sie herum, "
                                                  "mit Sonnenschreinen, Abkürzungen und Belohnungstüren; die vollständigen Ebenenblätter entstehen Stufe für Stufe.") + "</p>")
        q = t("“", "„") + T(ctx, tier["line"]) + t("”", "“")
        sections = []
        for i, f in enumerate(floors):
            rooms = "".join(room(ctx, code, name, text, ctx.pick(*scene) if isinstance(scene, (list, tuple)) else scene, mp, cx, tag_pairs=tg, flip=(j % 2 == 1), extra=MORE_ART.get(code, []) + [ex])
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
                            t(f"<p>Fire burns, Earth breaks, Wind lifts and Water parts. Each orb is a permanent power that stays with "
                              f"Kaya between runs, and each opens routes in floors she has already climbed.</p>"
                              f"<p><a class='text-link' href='{u('game/weapons-and-powers.html')}'>How the orbs work</a></p>",
                              f"<p>Feuer brennt, Erde bricht, Wind hebt und Wasser teilt. Jede Kugel ist eine dauerhafte Kraft, die "
                              f"Kaya über alle Durchläufe hinweg behält, und jede öffnet Wege in Ebenen, die sie schon erklommen hat.</p>"
                              f"<p><a class='text-link' href='{u('game/weapons-and-powers.html')}'>Wie die Kugeln funktionieren</a></p>"))
        if tier.get("sun"):
            extra = feature(ctx, "W06", None, t("The Sun Orb", "Die Sonnenkugel"),
                            t(f"<p>The brightest object in the game, resting in a cradle of four carved hands. You carry it up the "
                              f"last stair to the <a href='{u('climb/sky-altar.html')}'>Sky Altar</a>.</p>",
                              f"<p>Das hellste Objekt im Spiel, gebettet in eine Wiege aus vier gemeißelten Händen. Du trägst sie die "
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
  <h2>{t("Set pieces", "Setpieces")}</h2>
  {catalog(ctx, [(i, nm, None) for i, nm in tier["set_pieces"]], cls="catalog-3")}
</div></section>
"""
    rooms = tier_rooms(tier)
    scenes = [i for r in rooms for i in (r[4] if isinstance(r[4], (list, tuple)) else [r[4]])]
    return dict(title=tier["title"], kicker=("The Climb", "Der Aufstieg"), lede=tier["lede"],
                description=tier["lede"], banner=scenes, og=scenes, body=body)


# ------------------------------------------------------------------ Floor 0
# The 17 screens of the vertical slice (VERTICAL_SLICE_Floor0_Design.md §5.2). Each shows its SCR picture once it is
# uploaded, and until then the closest existing painting.
SHELL_SCREENS = [
    (["SCR-01", "HUB01"], ("The camp at dawn", "Das Lager im Morgengrauen")),
    (["SCR-02", "A-04"], ("The trail", "Der Pfad")),
    (["SCR-03", "HUB05"], ("The serpent tunnel", "Der Schlangentunnel")),
    (["SCR-04", "A-03"], ("Down to the Threshold", "Hinab zur Schwelle")),
    (["SCR-05", "B-03"], ("The flooded atrium", "Das geflutete Atrium")),
    (["SCR-06", "F0-01"], ("The Sun Pillar", "Die Sonnensäule")),
    (["SCR-07", "B-07"], ("The spike corridor", "Der Stachelgang")),
    (["SCR-08", "B-04"], ("The fire gallery", "Die Feuergalerie")),
    (["SCR-09", "B-05"], ("The edge of the chasm", "Der Rand der Schlucht")),
    (["SCR-10", "F0-02"], ("The far side", "Die andere Seite")),
    (["SCR-11", "B-06"], ("The plate door and the climb", "Die Plattentür und der Aufstieg")),
    (["SCR-12", "B-08"], ("The orb shrine", "Der Kugelschrein")),
    (["SCR-13", "B-09"], ("The beam stair", "Die Strahlentreppe")),
    (["SCR-14", "T3C-SCENE"], ("The beam stair, upper", "Die Strahlentreppe, oben")),
    (["SCR-15", "B-10"], ("The sword shrine", "Der Schwertschrein")),
    (["SCR-16", "F0-03"], ("The root curtain and the broken bridge", "Der Wurzelvorhang und die zerbrochene Brücke")),
    (["SCR-17", "B-11"], ("The portal on the Sun Pillar", "Das Portal auf der Sonnensäule")),
]


def floor_0(ctx):
    u, t = ctx.url, ctx.t
    ix_nicte = u("characters/guardians/ix-nicte.html")
    story = u("story/short-story.html")
    rooms = [
        ("B-03", ("The flooded atrium", "Das geflutete Atrium"), [("Spawn", "Startpunkt"), ("Jump", "Springen"), ("Swim", "Schwimmen")],
         ("A spawn platform, stone islands in knee-deep water, and a pool to swim. The portal glows on top of the Sun Pillar far "
          "above you, so the goal of the floor is in view from its first second. Two things here are out of reach for now: a glyph "
          "target high over the pool, and a ledge too tall to climb.",
          "Eine Startplattform, Steininseln in knietiefem Wasser und ein Becken zum Schwimmen. Das Portal leuchtet hoch über dir auf "
          "der Spitze der Sonnensäule, also ist das Ziel der Ebene von der ersten Sekunde an zu sehen. Zwei Dinge hier sind vorerst "
          "außer Reichweite: ein Glyphenziel hoch über dem Becken und ein Sims, zu hoch zum Klettern."),
         (f"On a half-submerged step, <a href='{ix_nicte}'>Ix Nicte</a>, Keeper of the First Step, stands dormant. K'in goes quiet near her.",
          f"Auf einer halb überfluteten Stufe ruht <a href='{ix_nicte}'>Ix Nicte</a>, die Hüterin der ersten Stufe. In ihrer Nähe wird K'in still.")),
        ("B-07", ("The spike corridor", "Der Stachelgang"), [("Lens", "Linse"), ("Sun Shrine", "Sonnenschrein")],
         ("The first Sun Shrine stands at its door. Inside, a low corridor: three spike strips on different beats, and a stone serpent "
          "spitting fire from the far end. The Lens shows which plates are safe.",
          "Der erste Sonnenschrein steht an seiner Tür. Drinnen ein niedriger Gang: drei Stachelleisten in verschiedenen Takten und "
          "eine steinerne Schlange, die vom anderen Ende Feuer speit. Die Linse zeigt, welche Platten sicher sind."),
         (f"The last plate kills you, as it kills Kaya in <a href='{story}'>the short story</a>. It is meant to happen. You wake at the Threshold, Oxlahun pours the tea, and there's a new face on the wall. When you come back, the temple has moved: the end door has dropped to a low slot, and you roll through it.",
          f"Die letzte Platte tötet dich, wie sie Kaya in <a href='{story}'>der Kurzgeschichte</a> tötet. Das soll so sein. Du erwachst an der Schwelle, Oxlahun gießt Tee ein, und an der Wand ist ein neues Gesicht. Wenn du zurückkommst, hat sich der Tempel bewegt: Die Tür am Ende ist zu einem niedrigen Schlitz geworden, und du rollst hindurch.")),
        ("B-04", ("The fire gallery", "Die Feuergalerie"), [("Timing", "Timing"), ("Push", "Schieben")],
         ("Five stepping stones over a pit of flame, with vents firing on a two-second beat. One block, one rule: push it into a "
          "vent's mouth, and that vent stays shut for good.",
          "Fünf Trittsteine über einer Grube voller Flammen, mit Düsen, die im Zwei-Sekunden-Takt feuern. Ein Block, eine Regel: "
          "Schieb ihn in die Öffnung einer Düse, und diese Düse bleibt für immer zu."), None),
        ("B-05", ("The chasm", "Die Schlucht"), [("Moving platforms", "Bewegte Plattformen"), ("Finds", "Funde")],
         ("A still slab, a sliding one, a lifting one and a ferry, over a drop into the dark. A golden idol waits on a wall ledge. "
          "A fall costs a little health and puts you back on the platform you left.",
          "Eine ruhende Platte, eine gleitende, eine steigende und eine Fähre, über einem Sturz ins Dunkel. Auf einem Wandsims "
          "wartet ein goldenes Idol. Ein Sturz kostet etwas Gesundheit und setzt dich auf die Plattform zurück, von der du kamst."), None),
        ("B-06", ("The plate door and the climb", "Die Plattentür und der Aufstieg"), [("Carry", "Tragen"), ("Ledge grab", "Simsgriff")],
         ("Carry a stone block onto the plate, and the door holds. A second Sun Shrine. Behind the door a shaft climbs four storeys "
          "on ledges, and a ladder at the top can be kicked down: the floor's first shortcut.",
          "Trag einen Steinblock auf die Platte, und die Tür bleibt offen. Ein zweiter Sonnenschrein. Hinter der Tür steigt ein "
          "Schacht vier Stockwerke über Simse hinauf, und oben lässt sich eine Leiter hinuntertreten: die erste Abkürzung der Ebene."), None),
        ("B-08", ("The orb shrine", "Der Kugelschrein"), [("Puzzle", "Rätsel")],
         ("Three pedestals, gold, blue and red. Sun poured into water makes growth; fire is the decoy. Growth in the socket sends a "
          "vine across the floor that bursts open the way on.",
          "Drei Sockel, gold, blau und rot. Sonne in Wasser gegossen ergibt Wachstum; Feuer ist die Falle. Wachstum in der Fassung "
          "schickt eine Ranke über den Boden, die den Weg weiter aufsprengt."), None),
        ("B-09", ("The beam switchback", "Die Strahlen-Serpentine"), [("Toggle hazard", "Schaltende Gefahr"), ("Timing", "Timing")],
         ("Two ramps climb back to the left, each crossed by a blue-white beam: one a plate turns off, one on a two-second cycle. "
          "Nothing is dodged here. It is walked, on the right half of the beat.",
          "Zwei Rampen steigen nach links zurück, jede von einem blauweißen Strahl gekreuzt: einen schaltet eine Platte ab, einer läuft "
          "im Zwei-Sekunden-Takt. Hier wird nichts ausgewichen. Hier wird gegangen, in der richtigen Hälfte des Takts."), None),
        ("B-10", ("The sword shrine", "Der Schwertschrein"), [("Combat", "Kampf"), ("Parry", "Parieren")],
         ("A high landing over the atrium. Kaya lifts the obsidian macuahuitl, and the first Risen Guardian steps out of its niche: "
          "the combo, the heavy strike, the roll, and the parry when its mark burns gold. Then two more Risen and a Novice.",
          "Ein hoher Absatz über dem Atrium. Kaya hebt das Obsidian-Macuahuitl, und der erste Erweckte Wächter tritt aus seiner "
          "Nische: die Kombo, der schwere Schlag, die Rolle und die Parade, wenn sein Zeichen golden glüht. Dann zwei weitere Erweckte und ein Novize."), None),
        ("B-11", ("The bridge to the portal", "Die Brücke zum Portal"), [("Cut", "Schneiden"), ("Pogo", "Abfedern")],
         ("Two hits cut the root curtain: the first lock the new blade opens. A bridge runs back over the atrium, broken in the middle, "
          "where spike urns stand on posts. Strike down on them and they throw you on. On the Sun Pillar: the portal, a third shrine, and "
          "a vine ladder down to the start.",
          "Zwei Hiebe durchtrennen den Wurzelvorhang: das erste Schloss, das die neue Klinge öffnet. Eine Brücke führt zurück über das "
          "Atrium, in der Mitte zerbrochen, wo Stachelurnen auf Pfosten stehen. Schlag von oben auf sie, und sie werfen dich weiter. Auf "
          "der Sonnensäule: das Portal, ein dritter Schrein und eine Rankenleiter hinunter zum Anfang."), None),
    ]
    stations = []
    for n, (img, name, tag_pairs, text, note) in enumerate(rooms, 1):
        note_html = f'<p class="station-note">{t(*note)}</p>' if note else ""
        stations.append(
            f'<li class="station"><span class="station-num" aria-hidden="true">{n}</span>'
            f'<div class="station-media">{ctx.figure(img, alt=t(*name))}</div>'
            f'<div class="station-text"><h3>{t(*name)}</h3>{tags(ctx, tag_pairs)}<p>{t(*text)}</p>{note_html}</div></li>')
    fact_rows = [
        (t("Place in the climb", "Platz im Aufstieg"), t("The first level, below Tier I", "Die erste Ebene, unter Stufe I")),
        (t("Size", "Größe"), f'{shape_glyph(ctx, "H>V")} ' + t("17 screens: 4 outside, 13 inside", "17 Bildschirme: 4 draußen, 13 drinnen")),
        (t("Teaches", "Lehrt"), t("Every base move in a safe order: run, jump, ledge grab, swim, push, carry, roll, parry, pogo",
                                  "Jede Grundbewegung in sicherer Reihenfolge: laufen, springen, Simsgriff, schwimmen, schieben, tragen, rollen, parieren, abfedern")),
        (t("Enemies", "Gegner"), t("Your first Risen Guardian, and a Novice", "Dein erster Erweckter Wächter und ein Novize")),
        (t("Reward", "Belohnung"), t("The obsidian macuahuitl and the Lens", "Das Obsidian-Macuahuitl und die Linse")),
        (t("Also", "Außerdem"), t("Your first death, on purpose", "Dein erster Tod, mit Absicht")),
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
      <p class="big">{t("The Shell is the first level, and the vertical slice: the half hour that has to prove the whole game. It is played "
                        "side-on, in two rows of screens.",
                        "The Shell ist die erste Ebene und der Vertical Slice: die halbe Stunde, die das ganze Spiel beweisen muss. Sie wird "
                        "von der Seite gespielt, in zwei Reihen von Bildschirmen.")}</p>
      <p>{t("The lower row runs right, from the flooded atrium through the spike corridor, the fire gallery and the chasm. A shaft "
            "climbs. The upper row runs back left, to a bridge high over the atrium and the portal on top of the Sun Pillar, which "
            "glowed above you from the first second. It teaches every base move once, shows you two locks you can't open yet, and "
            "kills you once, on purpose, so that the first thing you really learn is the Return.",
            "Die untere Reihe läuft nach rechts, vom gefluteten Atrium durch den Stachelgang, die Feuergalerie und die Schlucht. Ein "
            "Schacht steigt auf. Die obere Reihe läuft zurück nach links, zu einer Brücke hoch über dem Atrium und dem Portal auf der "
            "Spitze der Sonnensäule, das von der ersten Sekunde an über dir leuchtete. Sie lehrt jede Grundbewegung einmal, zeigt dir zwei "
            "Schlösser, die du noch nicht öffnen kannst, und tötet dich einmal, mit Absicht, damit das Erste, was du wirklich lernst, die Rückkehr ist.")}</p>
    </div>
    {facts(fact_rows)}
  </div>
</section>

<section class="band strip-band"><div class="wrap section">
  <div class="section-head">
    <h2>{t("Seventeen screens, camp to portal", "Siebzehn Bildschirme, vom Lager zum Portal")}</h2>
  </div>
  <p class="lede-sm">{t("Every screen is one frame of the game camera, 30.72 by 17.28 metres of the temple, in the order you play them. "
                        "The first four are outside: the camp, the trail and the serpent tunnel down to the Threshold.",
                        "Jeder Bildschirm ist ein Bild der Spielkamera, 30,72 mal 17,28 Meter Tempel, in der Reihenfolge, in der du sie spielst. "
                        "Die ersten vier liegen draußen: das Lager, der Pfad und der Schlangentunnel hinab zur Schwelle.")}</p>
</div>
{run_strip(ctx, SHELL_SCREENS, t("The Shell, screen by screen", "The Shell, Bildschirm für Bildschirm"))}
</section>

<section class="wrap section">
  <h2>{t("Nine rooms, two rows, one way up", "Neun Räume, zwei Reihen, ein Weg nach oben")}</h2>
  <p class="lede-sm">{t("In the order you meet them, from the flooded atrium to the portal on the Sun Pillar.",
                        "In der Reihenfolge, in der du sie betrittst, vom gefluteten Atrium bis zum Portal auf der Sonnensäule.")}</p>
  <ol class="route" role="list">{"".join(stations)}</ol>
  <p class="floor-end">{t(f"Then home to the Threshold. Oxlahun's table opens, the Memory Wheel lights, and the middle portal leads up into <a href='{u('climb/tier-1.html')}'>the Flooded Foundations</a>.",
                           f"Dann nach Hause zur Schwelle. Oxlahuns Tisch öffnet sich, das Erinnerungsrad leuchtet auf, und das mittlere Portal führt hinauf in <a href='{u('climb/tier-1.html')}'>die überfluteten Fundamente</a>.")}</p>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("Set pieces", "Setpieces")}</h2>
  {catalog(ctx, set_pieces, cls="catalog-3")}
</div></section>
"""


# ------------------------------------------------------------------ the pyramid (overview)
OVERVIEW_CARDS = [
    ("climb/threshold.html", ["A-03"], ("The Threshold", "Die Schwelle"), ("Where every climb begins", "Wo jeder Aufstieg beginnt")),
    ("climb/floor-0.html", ["B-03", "B-11"], ("The Shell", "The Shell"), ("Where every verb is learned", "Wo du jedes Grundverb lernst")),
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
    for n in range(0, LAST_FLOOR + 1):
        name, _, mech, _, reward = FLOORS[n]
        shape, screens = SHAPES[n]
        tier = 0 if n == 0 else 7 if n == LAST_FLOOR else next(k for k, v in TIERS.items() if n in v["floors"])
        path = "climb/floor-0.html" if n == 0 else "climb/sky-altar.html" if n == LAST_FLOOR else f"climb/tier-{tier}.html#floor-{n}"
        rows.append(f"<tr><td class='num'>{n}</td><th><a href='{u(path)}'>{T(ctx, name)}</a></th>"
                    f"<td class='shape-cell'>{shape_glyph(ctx, shape)}<span class='screens'>{screens}</span></td>"
                    f"<td>{T(ctx, mech)}</td><td>{T(ctx, reward) if reward else '–'}</td></tr>")
    anatomy = [
        (t("Entry Shrine", "Eingangsschrein"), t("Lit when you arrive from the stair below.", "Leuchtet auf, wenn du von der Treppe darunter ankommst.")),
        (t("The main path", "Der Hauptweg"), t("Three to five beats around one new idea: teach it, develop it, twist it, conclude it. A landmark you can see from far away leads you on.",
                                               "Drei bis fünf Takte um eine neue Idee: lehren, entwickeln, verdrehen, abschließen. Ein Wahrzeichen, das du von weit her siehst, führt dich.")),
        (t("Pockets and secrets", "Taschen und Geheimnisse"), t("Reward doors rerolled each run, pockets locked until a later ability, and at least one cracked wall or Lens-only crack.",
                                                                "Belohnungstüren, in jedem Durchlauf neu gewürfelt, Taschen, die erst eine spätere Fähigkeit öffnet, und mindestens eine rissige Wand oder ein Riss, den nur die Linse zeigt.")),
        (t("Mid Shrine and shortcut", "Mittlerer Schrein und Abkürzung"), t("A Sun Shrine halfway, and a shortcut opened from the far side that stays open for good.",
                                                                           "Ein Sonnenschrein auf halbem Weg und eine Abkürzung, von der anderen Seite geöffnet, die für immer offen bleibt.")),
        (t("Signature rooms and the boss", "Prägende Räume und der Boss"), t("The floor's authored rooms, then a shrine right before the boss door: back in the fight in seconds.",
                                                                              "Die von Hand gebauten Räume der Ebene, dann ein Schrein direkt vor der Bosstür: in Sekunden zurück im Kampf.")),
        (t("Portal Chamber", "Portalkammer"), t("Socket the Key Orb, take a rubbing, ring the bell, then climb on, send your Finds down, or go home.",
                                               "Schlüsselkugel einsetzen, Abrieb nehmen, Glocke läuten, dann weiter aufsteigen, die Funde hinunterschicken oder nach Hause gehen.")),
    ]
    anatomy_html = '<ol class="loops loops-grid">' + "".join(f'<li><span class="loop-label">{k}</span><p>{v}</p></li>' for k, v in anatomy) + "</ol>"
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("One pyramid, climbed from the inside and seen from the side: the Shell, then twenty-five floors in six tiers, then the open summit. Thirteen floors below the Sun Well, thirteen above it.",
                        "Eine Pyramide, von innen erklommen und von der Seite gesehen: The Shell, dann fünfundzwanzig Ebenen in sechs Stufen, dann der offene Gipfel. Dreizehn Ebenen unter dem Sonnenbrunnen, dreizehn darüber.")}</p>
      <p>{t("Every floor is a hand-built side-scrolling level of six to twenty-eight screens, and it stays the same from run to run, so you can learn it. "
            "What the temple remembers stays changed: shrines you lit, shortcuts you opened, water you drained. What it resets is what you fight for: "
            "the enemies, the Finds, and the glyphs on the reward doors.",
            "Jede Ebene ist ein von Hand gebautes Side-Scrolling-Level aus sechs bis achtundzwanzig Bildschirmen, und sie bleibt von Durchlauf zu Durchlauf gleich, damit du sie lernen kannst. "
            "Was der Tempel sich merkt, bleibt verändert: Schreine, die du entzündet hast, Abkürzungen, die du geöffnet hast, Wasser, das du abgelassen hast. Was er zurücksetzt, ist das, worum du kämpfst: "
            "die Gegner, die Funde und die Glyphen an den Belohnungstüren.")}</p>
      <p>{t("Each tier has its own direction. Tier I climbs flooded shafts, Tier II runs along trap galleries, and Tier IV sends you four ways at once. Beat a tier's boss and its Sun Gate lights, so your next run can start there.",
            "Jede Stufe hat ihre eigene Richtung. Stufe I steigt durch geflutete Schächte, Stufe II läuft durch Fallengalerien, und Stufe IV schickt dich in vier Richtungen zugleich. Besiege den Boss einer Stufe, und ihr Sonnentor leuchtet auf, sodass dein nächster Durchlauf dort beginnen kann.")}</p>
    </div>
    {facts([(t("Floors", "Ebenen"), t("27: the Shell, 25 floors in six tiers, the summit", "27: The Shell, 25 Ebenen in sechs Stufen, der Gipfel")),
            (t("Screens", "Bildschirme"), t("About 505, plus 72 one-screen rooms in the Builders' Ways", "Rund 505, dazu 72 Ein-Bildschirm-Räume in den Wegen der Erbauer")),
            (t("Per floor", "Pro Ebene"), t("Sun Shrines, a shortcut, reward doors, locked pockets, a secret, the Portal Chamber", "Sonnenschreine, eine Abkürzung, Belohnungstüren, verschlossene Taschen, ein Geheimnis, die Portalkammer")),
            (t("Bosses", "Bosse"), t("Mire Mother, Chak Tun, Gearwarden, Fourfold Echo, Jaguar Priest, Priest's Lieutenant, Hollow High Priest, and four sanctum guardians",
                                     "Schlammmutter, Chak Tun, Zahnradwächter, Vierfaches Echo, Jaguarpriester, Leutnant des Priesters, Hohler Hohepriester und vier Hüter der Heiligtümer")),
            (t("Secrets", "Geheimnisse"), t(f"Six <a href='{u('climb/builders-ways.html')}'>Builders' Ways</a> hidden in the walls", f"Sechs <a href='{u('climb/builders-ways.html')}'>Wege der Erbauer</a>, verborgen in den Wänden"))])}
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("From the Threshold to the sun", "Von der Schwelle zur Sonne")}</h2>
  <div class="cards cards-3">{"".join(cards)}</div>
</div></section>

<section class="wrap section">
  <div class="split">
    <div class="split-media">{ctx.figure("HOME-CLIMB", t("The pyramid in cutaway, floor by floor", "Die Pyramide im Schnitt, Ebene für Ebene"))}</div>
    <div class="split-text">
      <p class="kicker">{t("Every floor", "Jede Ebene")}</p>
      <h2>{t("One template, twenty-seven levels", "Eine Vorlage, siebenundzwanzig Level")}</h2>
      <p>{t("Every floor is built from the same parts, in the same order, so a new floor is always readable even when everything on it is new. "
            "What changes from floor to floor is the one new idea at its heart, and the direction it runs in.",
            "Jede Ebene ist aus denselben Teilen gebaut, in derselben Reihenfolge, damit eine neue Ebene immer lesbar bleibt, auch wenn alles darauf neu ist. "
            "Was sich von Ebene zu Ebene ändert, ist die eine neue Idee in ihrem Kern und die Richtung, in die sie läuft.")}</p>
    </div>
  </div>
  <div class="anatomy">{anatomy_html}</div>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("The campaign, floor by floor", "Die Kampagne, Ebene für Ebene")}</h2>
  <p class="lede-sm">{t("The arrows show which way each level runs in side view; the number is its size in screens.",
                        "Die Pfeile zeigen, in welche Richtung jedes Level in der Seitenansicht läuft; die Zahl ist seine Größe in Bildschirmen.")}</p>
  <div class="table-wrap"><table class="orb-table campaign">
    <thead><tr><th>{t("Floor", "Ebene")}</th><th>{t("Name", "Name")}</th><th>{t("Shape", "Form")}</th><th>{t("The new idea", "Die neue Idee")}</th><th>{t("Reward", "Belohnung")}</th></tr></thead>
    <tbody>{"".join(rows)}</tbody>
  </table></div>
</div></section>
"""


# ------------------------------------------------------------------ the Threshold hub
def threshold_hub(ctx):
    u, t = ctx.url, ctx.t
    stations = [
        ("HUB06", ("The Memory Wheel", "Das Erinnerungsrad"),
         ("The round altar is a calendar wheel. K'in floats above it, greets you after every return with a line that changes as the climb goes on, and tends your permanent talents.",
          "Der runde Altar ist ein Kalenderrad. K'in schwebt darüber, begrüßt dich nach jeder Rückkehr mit einem Satz, der sich im Lauf des Aufstiegs verändert, und pflegt deine dauerhaften Talente.")),
        ("HUB12", ("Six Sun Gates", "Sechs Sonnentore"),
         ("In the back wall, one per tier. Beat a tier's boss and its gate lights, so a later run can start higher up, with a head start to match. Any lit Sun Shrine on a cleared floor can be a start point too.",
          "In der Rückwand, eines pro Stufe. Besiege den Boss einer Stufe, und ihr Tor leuchtet auf, sodass ein späterer Durchlauf weiter oben beginnen kann, mit passendem Vorsprung. Auch jeder entzündete Sonnenschrein auf einer geschafften Ebene kann ein Startpunkt sein.")),
        ("HUB10", ("The offering table", "Der Opfertisch"),
         ("Oxlahun's table: sell your Finds, take a bounty, buy weapons and stock, pawn your gear, drink the tea, and collect a carving of whatever just killed you.",
          "Oxlahuns Tisch: Funde verkaufen, Aufträge annehmen, Waffen und Vorräte kaufen, Ausrüstung verpfänden, Tee trinken und eine Schnitzerei von dem abholen, was dich gerade getötet hat.")),
        ("HUB11", ("The reading desk", "Das Lesepult"),
         ("The lectern and the codex. Bring your rubbings here, fill in the glyphs from your lexicon, and set K'in's version beside what the wall says.",
          "Das Lesepult und der Codex. Bring deine Abriebe hierher, füll die Glyphen aus deinem Lexikon aus und stell K'ins Fassung neben das, was die Wand sagt.")),
        ("HUB08", ("The Spirit Mural", "Das Geisterwandbild"),
         ("The temple's record. Each floor you clear lights another fragment, and your own carving changes as your count rises.",
          "Die Aufzeichnung des Tempels. Jede geschaffte Ebene lässt ein weiteres Fragment aufleuchten, und dein eigenes Relief verändert sich, je höher deine Zählung steigt.")),
    ]
    modes = [
        (("The Ascent", "Der Aufstieg"), ("Middle portal", "Mittleres Portal"),
         ("The climb. Open from the start: choose a lit Sun Gate, a weapon and a keepsake, and go.",
          "Der Aufstieg. Von Anfang an offen: Wähl ein leuchtendes Sonnentor, eine Waffe und ein Andenken, und los.")),
        (("Expedition", "Expedition"), ("Left portal", "Linkes Portal"),
         ("Sealed until your first tier is cleared. Revisit any cleared floor at low danger with your full kit, for side routes, idols and evidence.",
          "Versiegelt, bis deine erste Stufe geschafft ist. Besuch jede geschaffte Ebene bei geringer Gefahr mit voller Ausrüstung, für Nebenwege, Idole und Beweise.")),
        (("Trials of the Shifting Temple", "Prüfungen des wandelnden Tempels"), ("Right portal", "Rechtes Portal"),
         ("Sealed until your first summit. The whole climb under curses you choose, for the richest rewards.",
          "Versiegelt bis zu deinem ersten Gipfel. Der ganze Aufstieg unter Flüchen, die du selbst wählst, für die reichsten Belohnungen.")),
    ]
    mode_html = "".join(f'<div class="mode"><p class="mode-where">{T(ctx, w)}</p><h3>{T(ctx, n)}</h3><p>{T(ctx, d)}</p></div>'
                        for n, w, d in modes)
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("The Threshold is where you wake after every death. It's where you practise, sell, study, spend what you earned "
                      "and see how far you have come.",
                      "Die Schwelle ist der Ort, an dem du nach jedem Tod erwachst. Hier übst du, verkaufst, forschst, "
                      "gibst aus, was du verdient hast, und siehst, wie weit du gekommen bist.")}</p>
    <p>{t(f"This page is about how the hub plays. For its history and the clues hidden in it, see <a href='{u('world/threshold.html')}'>World: The Threshold</a>.",
          f"Diese Seite zeigt, wie der Hub funktioniert. Seine Geschichte und die darin versteckten Hinweise findest du unter <a href='{u('world/threshold.html')}'>Welt: Die Schwelle</a>.")}</p>
  </div>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("Outside: the forecourt", "Draußen: der Vorplatz")}</h2>
  {feature(ctx, "HUB01", None, t("The explorer camp", "Das Forscherlager"),
           t("<p>Isabel Kaan's old camp at the foot of the pyramid: tent, campfire and kettle, a map table and crates. It's where the game "
             "begins, thirty steps from the hall, and the pyramid is always in view.</p>"
             "<p>The camp has eight slots to restore with Jade, from a kettle and a lantern line to a codex shelf and "
             "Isabel's desk. Each one gives you something real, like a map table that shows what's left to find on every floor.</p>",
             "<p>Isabel Kaans altes Lager am Fuß der Pyramide: Zelt, Lagerfeuer und Kessel, ein Kartentisch und Kisten. Hier beginnt das "
             "Spiel, dreißig Schritte von der Halle entfernt, und die Pyramide ist immer im Blick.</p>"
             "<p>Das Lager hat acht Plätze, die sich mit Jade wiederherstellen lassen, vom Kessel und einer Laternenkette "
             "bis zum Codexregal und Isabels Schreibtisch. Jeder bringt dir etwas Echtes, etwa ein Kartentisch, der zeigt, was es auf "
             "jeder Ebene noch zu finden gibt.</p>"))}
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
           t("<p>Three round portals stand on the dais beneath the mural. At first only the middle one is open.</p>",
             "<p>Drei runde Portale stehen auf dem Podest unter dem Wandbild. Zuerst ist nur das mittlere offen.</p>"))}
  <div class="modes">{mode_html}</div>
  {catalog(ctx, stations, cls="catalog-hub")}
</section>

<section class="band"><div class="wrap section">
  <h2>{t("Threshold and forecourt assets", "Assets für Schwelle und Vorplatz")}</h2>
  {catalog(ctx, [("HUB03", ("Jungle foliage kit", "Dschungel-Pflanzen-Kit"), None),
                 ("HUB04", ("Pyramid exterior kit", "Kit für die Außenseite der Pyramide"), None),
                 ("A-04", ("The jungle and the camp", "Der Dschungel und das Lager"), None)], cls="catalog-3")}
</div></section>
"""


# ------------------------------------------------------------------ shared rooms
def shared_rooms(ctx):
    u, t = ctx.url, ctx.t
    pc = room(ctx, "PC", ("The Portal Chamber", "Die Portalkammer"),
              [("Every floor ends here. You set the Key Orb in the socket of carved cupped hands, a fragment of the mural lights, and K'in speaks one line. Take a rubbing of the fragment. Ring the brass bell, and a tray slides out of the wall with Oxlahun's voice behind it.",
                "Jede Ebene endet hier. Du setzt die Schlüsselkugel in die Schale aus gemeißelten Händen, ein Fragment des Wandbilds leuchtet auf, und K'in spricht einen Satz. Nimm einen Abrieb des Fragments. Läute die Messingglocke, und ein Tablett gleitet aus der Wand, mit Oxlahuns Stimme dahinter."),
               ("Then decide. Climb the three-step dais through the great round Portal Door and keep your Finds at risk. Pay to send them down the offering chute. Or take the small blue return portal and walk home alive.",
                "Dann entscheide. Steig das dreistufige Podest hinauf durch die große runde Portaltür und lass deine Funde im Risiko. Zahl, um sie den Opferschacht hinunterzuschicken. Oder nimm das kleine blaue Rückkehrportal und geh lebend nach Hause.")],
              "C-02", tag_pairs=[("End of every floor", "Ende jeder Ebene")])
    sr = room(ctx, "SR", ("The Sun Shrine", "Der Sonnenschrein"),
              [("The checkpoint. A stone sun disc on a plinth that glows green-gold once it's lit. Resting at it refills Oxlahun's tea gourd, "
                "two sips that each heal a good part of your health, and saves your place. It also wakes the floor's ordinary enemies again, "
                "so rest or press on is a real choice.",
                "Der Kontrollpunkt. Eine steinerne Sonnenscheibe auf einem Sockel, die grüngolden leuchtet, sobald sie entzündet ist. Wer an "
                "ihr rastet, füllt Oxlahuns Teekürbis wieder auf, zwei Schlucke, die jeweils einen guten Teil der Gesundheit heilen, und sichert "
                "seinen Platz. Sie weckt aber auch die gewöhnlichen Gegner der Ebene wieder, also ist Rasten oder Weitergehen eine echte Wahl."),
               ("Every floor has one or more, and one stands right before every boss door. A lit shrine on a cleared floor is also a start "
                "point from the Threshold: the way back to the pockets you couldn't open the first time.",
                "Jede Ebene hat einen oder mehrere, und einer steht direkt vor jeder Bosstür. Ein entzündeter Schrein auf einer geschafften "
                "Ebene ist außerdem ein Startpunkt von der Schwelle aus: der Weg zurück zu den Taschen, die du beim ersten Mal nicht öffnen konntest.")],
              ctx.pick("SCR-06", "C-04"), tag_pairs=[("Every floor", "Jede Ebene"), ("Checkpoint", "Kontrollpunkt")], flip=True)
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("Two rooms appear on every floor of the climb. They are where it pauses: to rest, to bank what you carry, to "
                      "hear K'in, and to breathe.",
                      "Zwei Räume tauchen auf jeder Ebene des Aufstiegs auf. In ihnen hält er inne: um zu rasten, um zu sichern, "
                      "was du trägst, um K'in zu hören und um durchzuatmen.")}</p>
  </div>
</section>
<section class="band" id="portal-chamber"><div class="wrap section">{pc}</div></section>
<section class="wrap section" id="sun-shrine">{sr}</section>
<section class="band"><div class="wrap section">
  <h2>{t("Set pieces", "Setpieces")}</h2>
  {catalog(ctx, [("PC01", ("Portal Chamber set", "Set der Portalkammer"), None),
                 ("SR01", ("Shrine set", "Set des Schreins"), None)], cls="catalog-3")}
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
      <p>{t("The summit is the only floor under the open sky, a single arena screen seen side-on: a glyph-carved platform with four broken columns, four great braziers in "
            "the corners, red for fire, blue for water, white for wind and green for earth, and the small summit temple with the dark "
            "Sun Portal.",
            "Der Gipfel ist die einzige Ebene unter freiem Himmel, ein einziger Arena-Bildschirm von der Seite: eine glyphenbedeckte Plattform mit vier zerbrochenen Säulen, vier großen "
            "Feuerbecken in den Ecken, rot für Feuer, blau für Wasser, weiß für Wind und grün für Erde, und der kleine Gipfeltempel "
            "mit dem dunklen Sonnenportal.")}</p>
    </div>
    {facts([(t("Floor", "Ebene"), "26"), (t("Boss", "Boss"), t("The Hollow High Priest", "Der Hohle Hohepriester")),
            (t("Ending", "Ende"), t("Restore the cycle, or break it", "Den Kreislauf wiederherstellen oder durchbrechen")),
            (t("Afterwards", "Danach"), t("The temple resets, and the Trials open", "Der Tempel beginnt von vorn, und die Prüfungen öffnen sich"))])}
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "E-02", None, t("The fight", "Der Kampf"),
           t(f"<p>The <a href='{u('characters/hollow-high-priest.html')}'>Hollow High Priest</a>, the order's former head, waits on the "
             f"plateau with four stolen lights circling in his open ribcage. His phases are played on the braziers: light each one with its orb, and "
             f"you pull that light out of his chest and take a move away from him. Then there's a fifth light he never held.</p>",
             f"<p>Der <a href='{u('characters/hollow-high-priest.html')}'>Hohle Hohepriester</a>, einst das Oberhaupt des Ordens, "
             f"wartet auf dem Plateau, vier gestohlene Lichter kreisen in seinem offenen Brustkorb. Seine Phasen spielen an den "
             f"Feuerbecken: Entzünde jedes mit seiner Kugel, und du ziehst dieses Licht aus seiner Brust und nimmst ihm einen Angriff. Dann gibt es noch ein fünftes Licht, das er nie besaß.</p>"))}
  {feature(ctx, "E-03", None, t("The choice", "Die Wahl"),
           t(f"<p>The Sun Orb goes on the altar before the Sun Portal. Two pedestals flank it: gold to restore the cycle, violet "
             f"to break it. Reaching the summit doesn't mean you know enough to choose. What each choice costs is told in "
             f"<a href='{u('story/index.html')}'>the story</a>.</p>"
             f"<p>After your first summit, the Trials of the Shifting Temple open, and the climb goes on.</p>",
             f"<p>Die Sonnenkugel kommt auf den Altar vor dem Sonnenportal. Zwei Sockel stehen daneben: gold, um den Kreislauf "
             f"wiederherzustellen, violett, um ihn zu durchbrechen. Den Gipfel zu erreichen heißt noch nicht, genug zu wissen, um zu wählen. Was jede Wahl kostet, erzählt <a href='{u('story/index.html')}'>die Geschichte</a>.</p>"
             f"<p>Nach deinem ersten Gipfel öffnen sich die Prüfungen des wandelnden Tempels, und der Aufstieg geht weiter.</p>"), flip=True)}
  {boss}
</div></section>

<section class="wrap section">
  <h2>{t("Set pieces", "Setpieces")}</h2>
  {catalog(ctx, [("SKY-01", ("Summit temple and Sun Portal", "Gipfeltempel und Sonnenportal"), None),
                 ("SKY-02", ("The four elemental braziers", "Die vier Elementar-Feuerbecken"), None),
                 ("SKY-03", ("Sun Orb altar and the two choice pedestals", "Altar der Sonnenkugel und die beiden Sockel der Wahl"), None)], cls="catalog-3")}
</section>
"""


# ------------------------------------------------------------------ the builders' ways
LP_SCREENS = [
    ("S01", ("The Crack", "Der Spalt"), ("Move, jump, and poke the tripwire before the spear finds you.", "Laufen, springen und den Stolperdraht anstupsen, bevor der Speer dich findet.")),
    ("S02", ("Dart Hall", "Pfeilhalle"), ("Ember Charges, a cracked floor with gold below, and a pressure stone you poke from afar.", "Glutladungen, ein rissiger Boden mit Gold darunter und ein Druckstein, den du aus der Ferne anstupst.")),
    ("S03", ("Guardian Gallery", "Wächtergalerie"), ("A Risen Guardian on patrol, and a crumbling walkway above it.", "Ein Erweckter Wächter auf Patrouille und ein bröckelnder Steg über ihm.")),
    ("S04", ("The Sealed Floor", "Der versiegelte Boden"), ("Read the mural, press the plates in its order: serpent, jaguar, eagle.", "Lies das Wandbild und drück die Platten in seiner Reihenfolge: Schlange, Jaguar, Adler.")),
    ("S05", ("Bat Shaft", "Fledermausschacht"), ("Drop down staggered ledges between two cave bats.", "Über versetzte Simse nach unten, zwischen zwei Höhlenfledermäusen.")),
    ("S06", ("Pendulum Hall", "Pendelhalle"), ("Two blades half a swing apart, and a rope up to the first Big Idol.", "Zwei Klingen, einen halben Schwung versetzt, und ein Seil hinauf zum ersten Großen Idol.")),
    ("S07", ("Fire Vents", "Feuerdüsen"), ("Three vents fire as a wave; ride right behind it.", "Drei Düsen feuern als Welle, lauf direkt hinter ihr her.")),
    ("S08", ("Crusher Chamber", "Stampferkammer"), ("Two crushers on a five-second cycle, and a wall worth blowing open.", "Zwei Stampfer im Fünf-Sekunden-Takt und eine Wand, die sich aufzusprengen lohnt.")),
    ("S09", ("The Long Drop", "Der lange Fall"), ("Big drops down a tall shaft, with darts on the second ledge.", "Große Sprünge einen hohen Schacht hinab, mit Pfeilen auf dem zweiten Sims.")),
    ("S10", ("Boulder Run I", "Felsenflucht I"), ("A plate clicks, a boulder drops. Run, and jump the pit at full speed.", "Eine Platte klickt, ein Felsbrocken fällt. Renn und spring in vollem Lauf über die Grube.")),
    ("S11", ("Boulder Run II", "Felsenflucht II"), ("Duck into the slot and let the boulder smash the wall for you.", "Duck dich in die Nische und lass den Felsbrocken die Wand für dich einschlagen.")),
    ("S12", ("Spear Corridor", "Speergang"), ("Spike strips rise as a wave; a rope leads to the third Big Idol.", "Stachelleisten steigen als Welle, ein Seil führt zum dritten Großen Idol.")),
    ("S13", ("Calendar Lift", "Kalenderaufzug"), ("A faster guardian, then a calendar stone that lifts you.", "Ein schnellerer Wächter, dann ein Kalenderstein, der dich hebt.")),
    ("S14", ("The Sun Door", "Die Sonnentür"), ("A crumbling chain you must not stop on, and someone waiting at the door.", "Eine bröckelnde Kette, auf der du nicht stehen bleiben darfst, und jemand, der an der Tür wartet.")),
]
WAYS = [
    (("I · The Builders' Way Down", "I · Der Weg der Erbauer nach unten"), ("The Root Cellars", "Die Wurzelkeller"), "14", ("Trap galleries; the boulder run", "Fallengalerien; die Felsenflucht")),
    (("II · The Drowned Cisterns", "II · Die ertrunkenen Zisternen"), ("The Dart Colonnade", "Die Pfeilkolonnade"), "12", ("Water as a timer; a flood chase", "Wasser als Zeitgeber; eine Flucht vor der Flut")),
    (("III · The Shifting Vault", "III · Das wandernde Gewölbe"), ("The Vanishing Path", "Der verschwindende Pfad"), "12", ("Walls that move between your deaths", "Wände, die sich zwischen deinen Toden verschieben")),
    (("IV · The Kiln Passage", "IV · Der Brennofengang"), ("The Sun Well", "Der Sonnenbrunnen"), "12", ("Fire; the lava wave", "Feuer; die Lavawelle")),
    (("V · The Glass Way", "V · Der gläserne Weg"), ("The Hall of Lies", "Die Halle der Lügen"), "12", ("False floors; falling through three screens", "Trugböden; ein Sturz durch drei Bildschirme")),
    (("VI · The Carver's Stair", "VI · Die Treppe des Steinmetzen"), ("The Inner Sanctum", "Das innere Heiligtum"), "10", ("The last long drop", "Der letzte lange Fall")),
]


def builders_ways(ctx):
    u, t = ctx.url, ctx.t
    rows = "".join(f"<tr><th scope='row'>{T(ctx, n)}</th><td>{T(ctx, w)}</td><td>{c}</td><td>{T(ctx, d)}</td></tr>" for n, w, c, d in WAYS)
    screens = "".join(f"<tr><th scope='row'>{T(ctx, n)}</th><td>{T(ctx, d)}</td></tr>" for _, n, d in LP_SCREENS)
    shots = [(f"LP1-{k}", T(ctx, n)) for k, n, _ in LP_SCREENS if ctx.has(f"LP1-{k}")]
    shots += [(f"WAY-{i}", T(ctx, w[0])) for i, w in enumerate(WAYS[1:], 2) if ctx.has(f"WAY-{i}")]
    gallery = ctx.gallery(shots, cls="gallery-3 gallery-169") if shots else ""
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("The builders never used the grand stair: they had their own way down, hidden inside the walls, and they trapped every inch of it.",
                        "Die Erbauer benutzten nie die große Treppe: Sie hatten ihren eigenen Weg nach unten, versteckt in den Wänden, und jeden Zentimeter davon mit Fallen gesichert.")}</p>
      <p>{t("Six cracks in the temple's walls, each one visible only through the Lens. Behind them, the rules get harder: one fixed screen at a time, one touch and you're dust, five lives for the whole Way. They use the same moves as the rest of the game at their very limit, and they run down through the pyramid to a hidden Sun Door that opens onto the Threshold.",
            "Sechs Risse in den Wänden des Tempels, jeder nur durch die Linse zu sehen. Dahinter werden die Regeln härter: jeweils ein fester Bildschirm, eine Berührung, und du bist Staub, fünf Leben für den ganzen Weg. Sie nutzen dieselben Bewegungen wie der Rest des Spiels an ihrer äußersten Grenze und führen durch die Pyramide nach unten zu einer verborgenen Sonnentür, die sich zur Schwelle öffnet.")}</p>
      <p>{t("They're the most dangerous way to walk home alive, and the richest. Finds carried out through a Way are worth half as much again, and they hold relics you can't get anywhere else.",
            "Sie sind der gefährlichste Weg, lebend nach Hause zu gehen, und der reichste. Funde, die du durch einen Weg hinausträgst, sind anderthalbmal so viel wert, und dort liegen Relikte, die es sonst nirgends gibt.")}</p>
    </div>
    {facts([(t("View", "Ansicht"), t("Side-on, one fixed screen at a time", "Von der Seite, jeweils ein fester Bildschirm")),
            (t("Lives", "Leben"), t("5 for the Way; one touch and you're dust", "5 für den Weg; eine Berührung, und du bist Staub")),
            (t("Tools", "Werkzeuge"), t("Staff poke, Ember Charges, ropes", "Stabstoß, Glutladungen, Seile")),
            (t("Fair play", "Fairness"), t("K'in warns once per trap and shows you what got you", "K'in warnt einmal pro Falle und zeigt dir, was dich erwischt hat"))])}
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, ctx.pick("LP1-S01", "T2E-SCENE"), t("How they play", "Wie sie sich spielen"), t("One screen, one puzzle", "Ein Bildschirm, ein Rätsel"),
    t("<p>A fixed camera shows one screen and cuts to the next when you cross the edge. Every trap is fully in view before you commit, so the second try feels clever, not lucky.</p>"
      "<p>Learn the screen, beat it on the next try, and keep your lives for the screens that matter. If you run out, the Way throws you out, and you count as dead.</p>",
      "<p>Eine feste Kamera zeigt einen Bildschirm und schneidet zum nächsten, sobald du den Rand überquerst. Jede Falle ist ganz zu sehen, bevor du dich festlegst, also fühlt sich der zweite Versuch klug an, nicht wie Glück.</p>"
      "<p>Lern den Bildschirm, schaff ihn beim nächsten Versuch und heb dir deine Leben für die Bildschirme auf, auf die es ankommt. Gehen sie dir aus, wirft dich der Weg hinaus, und du giltst als tot.</p>"))}
  {feature(ctx, ctx.pick("LP1-S02", "P21"), t("The toolkit", "Die Ausrüstung"), t("Handle the traps, don't just dodge them", "Fallen bedienen, nicht nur ausweichen"),
    t("<p><strong>Staff poke:</strong> trips wires and pressure stones from a safe distance. <strong>Ember Charges:</strong> break cracked blocks, but step away from the hiss. "
      "<strong>Ropes:</strong> unroll from bronze anchors to reach secret ledges.</p><p>The main path never needs a rope or a charge. They're for treasure, so using them is greed, never a dead end.</p>",
      "<p><strong>Stabstoß:</strong> löst Drähte und Drucksteine aus sicherer Entfernung aus. <strong>Glutladungen:</strong> sprengen rissige Blöcke, aber geh weg, wenn es zischt. "
      "<strong>Seile:</strong> rollen sich an Bronzeankern ab und führen zu geheimen Simsen.</p><p>Der Hauptweg braucht nie ein Seil oder eine Ladung. Sie sind für Schätze da, also sind sie Gier, nie eine Sackgasse.</p>"), flip=True)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Six Ways", "Sechs Wege")}</p>
  <h2>{t("Hidden behind the walls", "Verborgen hinter den Wänden")}</h2>
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Way", "Weg")}</th><th>{t("Crack found on", "Riss zu finden in")}</th><th>{t("Screens", "Bildschirme")}</th><th>{t("Theme", "Thema")}</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Way I", "Weg I")}</p>
  <h2>{t("The Builders' Way Down", "Der Weg der Erbauer nach unten")}</h2>
  <p class="lede-sm">{t("Fourteen screens in a zig-zag down through the pyramid's wall. On the first wall, a scratch in a hand Kaya knows.",
                        "Vierzehn Bildschirme im Zickzack durch die Wand der Pyramide. An der ersten Wand ein Kratzer in einer Handschrift, die Kaya kennt.")}</p>
  {gallery}
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Screen", "Bildschirm")}</th><th>{t("What it teaches", "Was er lehrt")}</th></tr></thead>
    <tbody>{screens}</tbody>
  </table></div>
</div></section>
"""


PAGES = {
    "climb/builders-ways.html": dict(
        title=("The Builders' Ways", "Die Wege der Erbauer"), kicker=("The Climb", "Der Aufstieg"),
        banner=["LP1-S10", "T2E-SCENE"], og=["LP1-S10", "T2E-SCENE"],
        lede=("Six secret one-screen trap gauntlets inside the walls: the most dangerous way home, and the richest.",
              "Sechs geheime Fallen-Spießrutenläufe in den Wänden, Bildschirm für Bildschirm: der gefährlichste Weg nach Hause und der reichste."),
        description=("The Builders' Ways: optional one-screen trap gauntlets hidden inside the Sun Temple's walls, the game's hardest platforming.",
                     "Die Wege der Erbauer: optionale Fallen-Plattformer-Level, verborgen in den Wänden des Sonnentempels."),
        body=builders_ways),
    "climb/index.html": dict(
        title=("The Pyramid", "Die Pyramide"), kicker=("The Climb", "Der Aufstieg"),
        lede=("The Shell, twenty-five floors in six tiers, and the summit.", "The Shell, fünfundzwanzig Ebenen in sechs Stufen und der Gipfel."),
        description=("The structure of the climb in Ascent of the Sun Temple, from the Threshold to the Sky Altar.",
                     "Der Aufbau des Aufstiegs in Ascent of the Sun Temple, von der Schwelle bis zum Himmelsaltar."),
        banner=["HOME-CLIMB"], og=["HOME-CLIMB"], body=pyramid),
    "climb/threshold.html": dict(
        title=("The Threshold Hub", "Die Schwelle (Hub)"), kicker=("The Climb", "Der Aufstieg"),
        lede=("Where you wake after every death: practise, sell, study, spend, and see how far you have come.",
              "Wo du nach jedem Tod erwachst: üben, verkaufen, forschen, ausgeben und sehen, wie weit du gekommen bist."),
        description=("How the Threshold works as the game's hub: camp, portals, Sun Gates, Oxlahun's table, the reading desk and the mural.",
                     "Wie die Schwelle als Hub des Spiels funktioniert: Lager, Portale, Sonnentore, Oxlahuns Tisch, das Lesepult und das Wandbild."),
        banner=["A-03"], og=["A-03"], body=threshold_hub),
    "climb/floor-0.html": dict(
        title=("The Shell", "The Shell"), kicker=("The Climb", "Der Aufstieg"),
        lede=("The first level and the vertical slice: seventeen side-on screens, every base move taught once, and your first death.",
              "Die erste Ebene und der Vertical Slice: siebzehn Bildschirme von der Seite, jede Grundbewegung einmal gelehrt, und dein erster Tod."),
        description=("The Shell: the tutorial floor of Ascent of the Sun Temple, room by room.",
                     "The Shell: die Tutorial-Ebene von Ascent of the Sun Temple, Raum für Raum."),
        banner=["SCR-05", "B-03", "B-11"], og=["SCR-05", "B-11"], body=floor_0),
    "climb/sky-altar.html": dict(
        title=("The Sky Altar", "Der Himmelsaltar"), kicker=("The Climb", "Der Aufstieg"),
        lede=("Floor 26: the open summit, the last fight, and the choice.",
              "Ebene 26: der offene Gipfel, der letzte Kampf und die Wahl."),
        description=("The Sky Altar, the summit of the Sun Temple: the plateau, the final fight and the ending choice.",
                     "Der Himmelsaltar, der Gipfel des Sonnentempels: das Plateau, der letzte Kampf und die Wahl am Ende."),
        banner=["E-02", "E-03"], og=["E-02", "E-03"], body=sky_altar),
    "climb/shared-rooms.html": dict(
        title=("Shrines & Portals", "Schreine & Portale"), kicker=("The Climb", "Der Aufstieg"),
        lede=("The Sun Shrines where you rest and start again, and the Portal Chamber that ends every floor.",
              "Die Sonnenschreine, an denen du rastest und neu beginnst, und die Portalkammer am Ende jeder Ebene."),
        description=("The Sun Shrine and the Portal Chamber, the two rooms on every floor of the climb.",
                     "Der Sonnenschrein und die Portalkammer, die beiden Räume auf jeder Ebene des Aufstiegs."),
        banner=["C-02", "C-04"], og=["C-02", "C-04"], body=shared_rooms),
}
for _n in TIERS:
    PAGES[f"climb/tier-{_n}.html"] = tier_page(_n)
