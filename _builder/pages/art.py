"""Art & Assets tab (English and German): art direction and the asset sheet catalogues.

Every sheet shows as a placeholder with its ID until it is uploaded.
"""
from components import catalog, feature

KIT = "art/kits.html"

KITS = [
    ("K01", ("Temple wall kit", "Tempelwand-Kit"),
     ("Full, half and quarter walls, corners, parapets, trims and a weathered variant",
      "Ganze, halbe und Viertelwände, Ecken, Brüstungen, Zierleisten und eine verwitterte Variante")),
    ("K02", ("Floor, stair and ramp kit", "Boden-, Treppen- und Rampen-Kit"),
     ("Tiles, steep Maya stairs, ramps, landings, broken pit edges and a three-step dais",
      "Fliesen, steile Maya-Treppen, Rampen, Absätze, abgebrochene Grubenkanten und ein dreistufiges Podest")),
    ("K03", ("Doorway, arch and slab-door kit", "Kit für Durchgänge, Bögen und Steintüren"),
     ("Corbel arches, serpent-framed doors, and slab doors that slide or drop",
      "Kragbögen, von Schlangen gerahmte Türen und Steintüren, die gleiten oder herabfallen")),
    ("K04", ("Pillar and column kit", "Pfeiler- und Säulen-Kit"),
     ("Carved square pillars, drum columns, feathered-serpent columns and broken stumps",
      "Gemeißelte Vierkantpfeiler, Trommelsäulen, Säulen der gefiederten Schlange und abgebrochene Stümpfe")),
    ("K05", ("Ceiling, corbel vault and sunbeam kit", "Decken-, Kraggewölbe- und Sonnenstrahl-Kit"),
     ("Stepped vaults, beamed ceilings, and cracks with volumetric sunbeams",
      "Stufengewölbe, Balkendecken und Risse mit volumetrischen Sonnenstrahlen")),
    ("K06", ("Glyph panel and relief kit", "Glyphentafel- und Relief-Kit"),
     ("Glyph blocks, friezes, stelae, and the same block dormant and glowing in all four energy colours",
      "Glyphenblöcke, Friese, Stelen und derselbe Block ruhend und leuchtend in allen vier Energiefarben")),
    ("K07", ("Rubble, ruin and debris kit", "Schutt-, Ruinen- und Trümmer-Kit"),
     ("Broken blocks that keep their carving, so rubble reads as a broken temple",
      "Zerbrochene Blöcke, die ihre Reliefs behalten, damit Schutt als zerstörter Tempel lesbar bleibt")),
    ("K08", ("Moss, vine and root overgrowth kit", "Moos-, Ranken- und Wurzel-Kit"),
     ("Vines, root curtains, strangler figs, ferns and glowing mushrooms",
      "Ranken, Wurzelvorhänge, Würgefeigen, Farne und leuchtende Pilze")),
    ("K09", ("Water edge, spout and drain kit", "Kit für Wasserkanten, Speier und Abflüsse"),
     ("Pool rims, jaguar-head spouts, channels and algae tide lines",
      "Beckenränder, Jaguarkopf-Speier, Kanäle und Algenränder")),
    ("K10", ("Light source kit", "Lichtquellen-Kit"),
     ("Torches, braziers, oil lamps, candles and copal burners, lit and unlit",
      "Fackeln, Feuerbecken, Öllampen, Kerzen und Kopalbrenner, entzündet und erloschen")),
    ("K11", ("Clay pots, jars and baskets", "Tontöpfe, Krüge und Körbe"),
     ("Breakable containers with intact, cracked and broken states",
      "Zerbrechliche Behälter, ganz, gesprungen und zerbrochen")),
    ("K12", ("Bridge kit", "Brücken-Kit"),
     ("Stone slab bridges, and rope bridges intact, burning and collapsing",
      "Brücken aus Steinplatten sowie Seilbrücken, intakt, brennend und einstürzend")),
    ("K13", ("Balcony, ledge, plinth and niche kit", "Balkon-, Sims-, Sockel- und Nischen-Kit"),
     ("Archer perches, galleries, narrow ledges and wall niches",
      "Plätze für Schützen, Galerien, schmale Simse und Wandnischen")),
    ("K14", ("Breakable crate and explorer supply kit", "Kit für zerbrechliche Kisten und Forschervorräte"),
     ("Crates sized to climb on, barrels, rope and bundles",
      "Kisten in Klettergröße, Fässer, Seile und Bündel")),
    ("K15", ("Floor medallions and glyph rings", "Bodenmedaillons und Glyphenringe"),
     ("The orb-shrine ring, the boss arena ring and calendar medallions, dormant and active",
      "Der Ring des Kugelschreins, der Ring der Bossarena und Kalendermedaillons, ruhend und aktiv")),
]

PROPS = [
    ("P01", ("Arrival pad", "Ankunftsfeld"), ("Round carved teleport pad: dormant, active and arriving",
                                              "Rundes, gemeißeltes Teleportfeld: ruhend, aktiv und bei der Ankunft")),
    ("P02", ("Checkpoint stele", "Kontrollpunkt-Stele"), ("A sun-faced stele that lights when touched",
                                                          "Eine Stele mit Sonnengesicht, die bei Berührung aufleuchtet")),
    ("P03", ("Exit gate", "Ausgangstor"), ("A corbel-arch gate whose slab sinks to reveal a golden veil",
                                           "Ein Tor mit Kragbogen, dessen Platte versinkt und einen goldenen Schleier freigibt")),
    ("P04", ("Pressure plate set", "Druckplatten-Set"), ("Square, strip, heavy-weight and ground-pound plates; pressed and wrong",
                                                         "Quadratische, Streifen-, Schwergewichts- und Stampfplatten; gedrückt und falsch")),
    ("P05", ("Puzzle doors", "Rätseltüren"), ("A sliding relief door and an energy door with a jaguar-mouth orb socket",
                                              "Eine gleitende Relieftür und eine Energietür mit Kugelfassung im Jaguarmaul")),
    ("P06", ("Orb pedestals and sockets", "Kugelsockel und Fassungen"), ("Cupped-hand sockets, a jaguar-mouth wall socket and a glyph-ring pedestal",
                                                                         "Fassungen aus gewölbten Händen, eine Wandfassung im Jaguarmaul und ein Glyphenring-Sockel")),
    ("P07", ("Energy orbs", "Energiekugeln"), ("Gold sun, blue water, red fire and green growth; sun into water makes growth",
                                               "Goldene Sonne, blaues Wasser, rotes Feuer und grünes Wachstum; Sonne in Wasser ergibt Wachstum")),
    ("P08", ("Key Orb", "Schlüsselkugel"), ("One per floor: a golden orb in a jade-and-gold cage that unfolds like petals",
                                            "Eine pro Ebene: eine goldene Kugel in einem Käfig aus Jade und Gold, der sich wie Blütenblätter öffnet")),
    ("P09", ("Golden idols", "Goldene Idole"), ("Eight collectible seated figures, one hidden in every room",
                                                "Acht sammelbare sitzende Figuren, eine in jedem Raum versteckt")),
    ("P10", ("Coins and Spirit Fragments", "Münzen und Geistsplitter"), ("Bronze, silver and gold coins, and translucent golden soul shards",
                                                                          "Münzen aus Bronze, Silber und Gold sowie durchscheinende goldene Seelensplitter")),
    ("P11", ("Small collectibles", "Kleine Sammelobjekte"), ("Codex pages, lore scrolls, glyph echoes, shards and trial medallions",
                                                             "Codexseiten, Schriftrollen, Glyphenechos, Splitter und Prüfungsmedaillons")),
    ("P12", ("Stone platform kit", "Steinplattform-Kit"), ("Static, sliding, floating and ferry platforms",
                                                           "Feste, gleitende, schwebende und Fährplattformen")),
    ("P13", ("Floor spike trap", "Stachelfalle im Boden"), ("Obsidian-tipped spikes: retracted, warning and extended",
                                                            "Stacheln mit Obsidianspitzen: eingefahren, warnend und ausgefahren")),
    ("P14", ("Serpent-head trap emitters", "Schlangenkopf-Fallenwerfer"), ("A fireball spitter, a fire jet and a dart head",
                                                                           "Ein Feuerballspeier, ein Feuerstrahl und ein Pfeilkopf")),
    ("P15", ("Fire pit and floor fire vents", "Feuergrube und Feuerdüsen im Boden"), ("A tiling fire pit, jaguar-mask vents and a vent ring",
                                                                                      "Eine kachelbare Feuergrube, Düsen mit Jaguarmaske und ein Düsenring")),
    ("P16", ("Energy beam totems and seal barrier", "Strahlentotems und Siegelbarriere"), ("A blue-white beam barrier, and a golden seal that dissolves",
                                                                                           "Eine blauweiße Strahlenbarriere und ein goldenes Siegel, das sich auflöst")),
    ("P17", ("Objective totem", "Zieltotem"), ("Four glyph slots that light as a room's goals are met",
                                               "Vier Glyphenfelder, die aufleuchten, sobald die Ziele eines Raums erfüllt sind")),
    ("P18", ("Glyph targets", "Glyphenziele"), ("Wall targets and a training post for the blowgun",
                                                "Wandziele und ein Übungspfahl für das Blasrohr")),
    ("P19", ("Crumbling floor tiles and stairs", "Bröckelnde Bodenfliesen und Treppen"), ("Intact, triggered, collapsing and respawning",
                                                                                          "Intakt, ausgelöst, einstürzend und wieder erscheinend")),
    ("P20", ("Cracked breakable walls", "Rissige, zerbrechliche Wände"), ("Hinted with a green glow, shattered by the Earth Orb",
                                                                          "Durch grünes Leuchten angedeutet, von der Erdkugel zerschmettert")),
    ("P21", ("Boulders", "Felsbrocken"), ("A rolling boulder, a release chute, a pushable boulder and a weight plate",
                                          "Ein rollender Felsbrocken, eine Auslöserutsche, ein schiebbarer Felsbrocken und eine Gewichtsplatte")),
    ("P22", ("Guardian niches and burial props", "Wächternischen und Grabobjekte"), ("Niches, burial benches and sarcophagi where guardians rise",
                                                                                     "Nischen, Grabbänke und Sarkophage, aus denen sich Wächter erheben")),
]

RELICS = [
    ("W01", ("Obsidian Macuahuitl", "Obsidian-Macuahuitl"), ("The melee weapon: obsidian blades, gold bands and a jade glyph strip",
                                                              "Die Nahkampfwaffe: Obsidianklingen, Goldbänder und ein Glyphenstreifen aus Jade")),
    ("W02", ("Spirit Blowgun", "Geisterblasrohr"), ("The first ranged weapon, with a jade hummingbird mouthpiece and a gourd quiver",
                                                     "Die erste Fernkampfwaffe, mit einem Mundstück als Jade-Kolibri und einem Köcher aus Kürbis")),
    ("W03", ("Sunburst Sling", "Sonnenschleuder"), ("A charged sling whose stones glow brighter the longer they charge",
                                                     "Eine Schleuder zum Aufladen; ihre Steine leuchten umso heller, je länger sie laden")),
    ("W04", ("Ember Censer", "Glutweihrauchfass"), ("A fire-god incense burner that throws a short cone of flame",
                                                     "Ein Weihrauchbrenner des Feuergottes, der einen kurzen Flammenkegel ausstößt")),
    ("W05", ("The four Elemental Orbs", "Die vier Elementarkugeln"), ("Fire, Earth, Wind and Water, with the chest-glow emblems they leave once owned",
                                                                       "Feuer, Erde, Wind und Wasser, mit den leuchtenden Brustemblemen, die sie hinterlassen")),
    ("W06", ("The Sun Orb", "Die Sonnenkugel"), ("The brightest object in the game, in a cradle of four carved hands",
                                                  "Das hellste Objekt im Spiel, in einer Wiege aus vier gemeißelten Händen")),
    ("W07", ("K'in, the spirit wisp", "K'in, das Geisterlicht"), ("The companion light and its VFX states",
                                                                   "Das Begleitlicht und seine Effektzustände")),
    ("W08", ("Kaya's field kit", "Kayas Feldausrüstung"), ("Notebooks, rubbing kit, brushes, compass and goggles",
                                                           "Notizbücher, Abriebset, Pinsel, Kompass und Schutzbrille")),
]

HUB = [
    ("HUB01", ("Explorer camp kit", "Forscherlager-Kit"), ("Tent, campfire and kettle tripod, map table and crates",
                                                           "Zelt, Lagerfeuer und Kesseldreibein, Kartentisch und Kisten")),
    ("HUB02", ("Training dummies", "Übungspuppen"), ("Straw dummies with painted faces, with hit and knocked-down states",
                                                     "Strohpuppen mit aufgemalten Gesichtern, getroffen und umgestoßen")),
    ("HUB03", ("Jungle foliage kit", "Dschungel-Pflanzen-Kit"), ("Ceiba, palms, strangler fig, ferns, bromeliads and canopy cards",
                                                                 "Kapokbaum, Palmen, Würgefeige, Farne, Bromelien und Blätterdach-Karten")),
    ("HUB04", ("Pyramid exterior kit", "Kit für die Außenseite der Pyramide"), ("Terrace walls, the grand stair with serpent balustrades, the summit parapet",
                                                                               "Terrassenmauern, die große Treppe mit Schlangenbalustraden, die Brüstung am Gipfel")),
    ("HUB05", ("Serpent-head tunnel entrance", "Tunneleingang mit Schlangenköpfen"), ("Two giant feathered serpents and a sun mask over the tunnel",
                                                                                     "Zwei riesige gefiederte Schlangen und eine Sonnenmaske über dem Tunnel")),
    ("HUB06", ("K'in's round altar", "K'ins runder Altar"), ("A calendar-wheel altar, dormant and awakened",
                                                             "Ein Altar als Kalenderrad, ruhend und erwacht")),
    ("HUB07", ("Round stone portal set", "Set der runden Steinportale"), ("Sealed, dormant, igniting and active portals, and the three-portal dais",
                                                                         "Versiegelte, ruhende, zündende und aktive Portale sowie das Podest der drei Portale")),
    ("HUB08", ("The Spirit Mural", "Das Geisterwandbild"), ("The carved history wall: dark, partly lit and fully lit",
                                                            "Die gemeißelte Geschichtswand: dunkel, teilweise erleuchtet und ganz erleuchtet")),
    ("HUB09", ("Mural relief figures", "Relieffiguren des Wandbilds"), ("The Carved Climbers and the order as relief panels",
                                                                        "Die gemeißelten Kletterer und der Orden als Relieftafeln")),
    ("HUB10", ("The offering table", "Der Opfertisch"), ("Oxlahun's stall with tagged goods and spirit shards",
                                                         "Oxlahuns Stand mit beschrifteten Waren und Geistsplittern")),
    ("HUB11", ("Codex lectern", "Codex-Lesepult"), ("A jaguar-backed lectern with a glowing screenfold codex",
                                                    "Ein Lesepult auf einem Jaguarrücken mit einem leuchtenden Faltcodex")),
    ("HUB12", ("Tier shortcut pads", "Abkürzungsfelder der Stufen"), ("Six emblem pads, locked and unlocked",
                                                                      "Sechs Emblemfelder, gesperrt und freigeschaltet")),
    ("HUB13", ("Threshold story props", "Erzählobjekte der Schwelle"),
     ("Game board, broom, polished floor, palm whistle, waxed flower, twill scrap, keepsakes and a chalk tally",
      "Spielbrett, Besen, polierter Boden, Palmblattpfeife, gewachste Blüte, Stofffetzen, Andenken und eine Kreidestrichliste")),
]


def intro(ctx, en, de):
    return f'<section class="wrap section narrow-top"><div class="prose"><p class="big">{ctx.t(en, de)}</p></div></section>'


def kits(ctx):
    return intro(ctx, "Fifteen modular kits build every room in the temple. Each sheet shows the pieces and their variants on one page.",
                 "Fünfzehn modulare Kits bauen jeden Raum des Tempels. Jedes Blatt zeigt die Teile und ihre Varianten auf einer Seite.") + \
        f'<section class="band"><div class="wrap section">{catalog(ctx, KITS)}</div></section>'


def props(ctx):
    return intro(ctx, "Everything a Climber can step on, pick up, solve or be hurt by: twenty-two sheets of shared gameplay props.",
                 "Alles, worauf ein Kletterer treten, was er aufheben, lösen oder woran er sich verletzen kann: zweiundzwanzig Blätter mit "
                 "gemeinsamen Gameplay-Objekten.") + \
        f'<section class="band"><div class="wrap section">{catalog(ctx, PROPS)}</div></section>'


def relics(ctx):
    u, t = ctx.url, ctx.t
    return f"""
<section class="wrap section narrow-top"><div class="prose">
  <p class="big">{t("The objects the story turns on: the Climbers' weapons, the orbs, K'in, and the kit Kaya inherited from her mother.",
                    "Die Gegenstände, um die sich die Geschichte dreht: die Waffen der Kletterer, die Kugeln, K'in und die Ausrüstung, die Kaya von "
                    "ihrer Mutter geerbt hat.")}</p>
  <p><a class="text-link" href="{u('game/weapons-and-powers.html')}">{t("How the weapons and powers play", "Wie sich Waffen und Kräfte spielen")}</a></p>
</div></section>
<section class="band"><div class="wrap section">{catalog(ctx, RELICS)}</div></section>
"""


def threshold_set(ctx):
    u, t = ctx.url, ctx.t
    return f"""
<section class="wrap section narrow-top"><div class="prose">
  <p class="big">{t("The camp, the forecourt and the great hall at the base of the pyramid, built from thirteen sheets.",
                    "Das Lager, der Vorplatz und die große Halle am Fuß der Pyramide, gebaut aus dreizehn Blättern.")}</p>
  <p><a class="text-link" href="{u('climb/threshold.html')}">{t("How the Threshold plays", "Wie die Schwelle funktioniert")}</a></p>
</div></section>
<section class="band"><div class="wrap section">{catalog(ctx, HUB)}</div></section>
"""


def set_pieces(ctx):
    # imported here so the climb data stays the single source for tier set pieces
    from importlib import util
    from pathlib import Path
    spec = util.spec_from_file_location("climb_data", Path(__file__).with_name("climb.py"))
    climb = util.module_from_spec(spec)
    spec.loader.exec_module(climb)
    u, t = ctx.url, ctx.t
    groups = [("floor-0", "The Shell", "climb/floor-0.html",
               [("F0-01", ("The Sun Pillar", "Die Sonnensäule")),
                ("F0-02", ("Stepping stones and spawn platform", "Trittsteine und Startplattform")),
                ("F0-03", ("The sword shrine", "Der Schwertschrein"))])]
    for n, tier in climb.TIERS.items():
        groups.append((f"tier-{n}", t(*tier["title"]), f"climb/tier-{n}.html", tier["set_pieces"]))
    groups.append(("sky-altar", t("The Sky Altar", "Der Himmelsaltar"), "climb/sky-altar.html",
                   [("SKY-01", ("Summit temple and Sun Portal", "Gipfeltempel und Sonnenportal")),
                    ("SKY-02", ("The four elemental braziers", "Die vier Elementar-Feuerbecken")),
                    ("SKY-03", ("Sun Orb altar and the two choice pedestals", "Altar der Sonnenkugel und die beiden Sockel der Wahl"))]))
    groups.append(("shared-rooms", t("Shared rooms", "Gemeinsame Räume"), "climb/shared-rooms.html",
                   [("PC01", ("Portal Chamber set", "Set der Portalkammer")),
                    ("SR01", ("Spirit Shrine set", "Set des Geisterschreins"))]))
    out = [intro(ctx, "The one-off pieces each level is built around, grouped by where they stand in the climb.",
                 "Die Einzelstücke, um die herum jedes Level gebaut ist, geordnet nach ihrem Platz im Aufstieg.")]
    for i, (anchor, title, path, rows) in enumerate(groups):
        band = ' class="band"' if i % 2 == 0 else ""
        out.append(f"""
<section{band} id="{anchor}"><div class="wrap section">
  <div class="section-head"><h2>{title}</h2><a class="text-link" href="{u(path)}">{t("See the level", "Zum Level")}</a></div>
  {catalog(ctx, [(i_, nm, None) for i_, nm in rows], cls="catalog-3")}
</div></section>""")
    return "".join(out)


def direction(ctx):
    u, t = ctx.url, ctx.t
    palette = [("#EFE6CE", ("Limestone", "Kalkstein")), ("#F0B24A", ("Torch gold", "Fackelgold")), ("#DF4A2A", ("Ember", "Glut")),
               ("#33C0A2", ("Jade", "Jade")), ("#152230", ("Wet stone", "Nasser Stein")), ("#070B10", ("Deep dark", "Tiefes Dunkel"))]
    swatches = "".join(f'<li><span class="swatch" style="background:{h}"></span><span class="sw-name">{t(*n)}</span>'
                       f'<span class="sw-hex">{h}</span></li>' for h, n in palette)
    energies = [("c-gold", ("Gold: the sun", "Gold: die Sonne")), ("c-blue", ("Blue: water", "Blau: Wasser")),
                ("c-red", ("Red: fire", "Rot: Feuer")), ("c-green", ("Green: growth", "Grün: Wachstum"))]
    energy_html = "".join(f'<li class="{c}">{t(*n)}</li>' for c, n in energies)
    return f"""
<section class="wrap section narrow-top">
  {feature(ctx, "KEYART", None, t("Painterly, stylized, believable", "Malerisch, stilisiert, glaubwürdig"),
           t("<p>The look sits in the register of Ratchet &amp; Clank and Jak &amp; Daxter: stylized and readable, but grounded. "
             "Colour is rich without being oversaturated, textures are soft and hand-painted, and shapes are chunky enough to read "
             "at a glance while you are jumping.</p>",
             "<p>Der Look bewegt sich im Register von Ratchet &amp; Clank und Jak &amp; Daxter: stilisiert und gut lesbar, aber "
             "geerdet. Die Farben sind satt, ohne zu übersättigen, die Texturen weich und handgemalt, und die Formen kräftig genug, "
             "um sie mitten im Sprung auf einen Blick zu erfassen.</p>"))}
  {feature(ctx, "HOME-CLIMB", None, t("Seven materials, and nothing else", "Sieben Materialien, und sonst nichts"),
           t("<p>Carved pale limestone, jade inlay, hammered gold, glowing glyphs, mossy weathered stone, obsidian and torch flame. "
             "Nothing in the temple uses a material outside this list.</p>",
             "<p>Gemeißelter heller Kalkstein, Jade-Einlagen, gehämmertes Gold, leuchtende Glyphen, bemooster verwitterter Stein, "
             "Obsidian und Fackelflammen. Nichts im Tempel verwendet ein Material außerhalb dieser Liste.</p>"), flip=True)}
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "P07", None, t("Four energy colours", "Vier Energiefarben"),
           t(f"<p>Every interactive object is marked in one of four colours:</p><ul class='energies'>{energy_html}</ul>"
             "<p>On top of that, jade means solvable, ember means it can kill you, and gold only ever means the way out.</p>",
             f"<p>Jedes interaktive Objekt trägt eine von vier Farben:</p><ul class='energies'>{energy_html}</ul>"
             "<p>Darüber hinaus heißt Jade lösbar, Glut heißt tödlich, und Gold bedeutet immer nur eines: den Weg hinaus.</p>"))}
  {feature(ctx, "B-08", None, t("Three lighting states", "Drei Lichtzustände"),
           t("<p>A room is dark before it is solved, saturated while it is running, and gold once it lets you through: unlit, "
             "charged, resolved. You can read your progress in a room from its light alone.</p>",
             "<p>Ein Raum ist dunkel, bevor er gelöst ist, satt, solange er läuft, und golden, sobald er dich durchlässt: "
             "unbeleuchtet, geladen, gelöst. Den Fortschritt in einem Raum liest du allein an seinem Licht ab.</p>"), flip=True)}
  {feature(ctx, "T4B-SCENE", None, t("Two render styles", "Zwei Darstellungsstile"),
           t(f"<p>Characters are polished stylized 3D in a modern animated-film look, set on neutral grey sheets so they double as "
             f"modelling references. The level scenes are painterly. See the <a href='{u('characters/lineup.html')}'>cast lineup</a>.</p>"
             "<p>The guardians' sigils glow a cold silver-white, deliberately outside the elemental palette. Kan Uk is the "
             "exception: his burns a banked amber.</p>",
             f"<p>Figuren sind polierte, stilisierte 3D-Modelle im Look moderner Animationsfilme, auf neutral grauen Blättern, damit "
             f"sie zugleich als Modellierreferenz dienen. Die Levelszenen sind malerisch. Siehe die <a href='{u('characters/lineup.html')}'>Figurenübersicht</a>.</p>"
             "<p>Die Siegel der Wächter leuchten kalt silberweiß, bewusst außerhalb der Elementarpalette. Kan Uk ist die Ausnahme: "
             "Seines glimmt in gedämpftem Bernstein.</p>"))}
</div></section>

<section class="wrap section">
  <h2>{t("The screen palette", "Die Bildschirmpalette")}</h2>
  <p class="lede-sm">{t("Six colours from the game's art bible, used for the interface and the level art.",
                        "Sechs Farben aus der Art Bible des Spiels, für die Benutzeroberfläche und die Levelgrafik.")}</p>
  <ul class="swatches">{swatches}</ul>
</section>

<section class="band"><div class="wrap section">
  <h2>{t("From concept to level", "Vom Konzept zum Level")}</h2>
  <div class="prose">
    <p>{t("The concept art is mood reference, not layout. Positions and sizes come from the level layout data, built on a 5.12 m "
          "grid with a 3.84 m storey height, so every painted room can be rebuilt to scale from the modular kits.",
          "Die Konzeptgrafik ist Stimmungsreferenz, kein Grundriss. Positionen und Größen stammen aus den Level-Layoutdaten, "
          "aufgebaut auf einem 5,12-m-Raster mit 3,84 m Geschosshöhe, sodass sich jeder gemalte Raum maßstabsgetreu aus den "
          "modularen Kits nachbauen lässt.")}</p>
    <p><a class="text-link" href="{u(KIT)}">{t("The modular kits", "Die modularen Kits")}</a></p>
  </div>
</div></section>
"""


def head(title, lede, desc, banner, body):
    return dict(title=title, kicker=("Art & Assets", "Kunst & Assets"), lede=lede, description=desc, banner=banner, og=banner, body=body)


PAGES = {
    "art/index.html": head(("Art Direction", "Art Direction"),
                           ("How the temple should look and feel, and the rules that keep it consistent.",
                            "Wie der Tempel aussehen und sich anfühlen soll, und die Regeln, die ihn einheitlich halten."),
                           ("The art direction of Ascent of the Sun Temple: style, materials, colour, light and palette.",
                            "Die Art Direction von Ascent of the Sun Temple: Stil, Materialien, Farbe, Licht und Palette."),
                           ["KEYART"], direction),
    "art/kits.html": head(("Modular Kits", "Modulare Kits"),
                          ("The fifteen kits every room is built from.", "Die fünfzehn Kits, aus denen jeder Raum gebaut ist."),
                          ("Modular environment kits K01 to K15.", "Modulare Umgebungs-Kits K01 bis K15."),
                          ["K01", "HUB04"], kits),
    "art/props.html": head(("Gameplay Props", "Gameplay-Objekte"),
                           ("Pads, plates, doors, traps and collectibles shared by every floor.",
                            "Felder, Platten, Türen, Fallen und Sammelobjekte, die alle Ebenen teilen."),
                           ("Shared gameplay props P01 to P22.", "Gemeinsame Gameplay-Objekte P01 bis P22."),
                           ["P07"], props),
    "art/relics.html": head(("Hero Items & Relics", "Heldengegenstände & Relikte"),
                            ("Weapons, orbs, the spirit wisp and the field kit.", "Waffen, Kugeln, das Geisterlicht und die Feldausrüstung."),
                            ("Hero items, weapons and relics W01 to W08.", "Heldengegenstände, Waffen und Relikte W01 bis W08."),
                            ["W06", "W01"], relics),
    "art/threshold-set.html": head(("Threshold & Forecourt", "Schwelle & Vorplatz"),
                                   ("The camp, the forecourt and the great hall at the base of the pyramid.",
                                    "Das Lager, der Vorplatz und die große Halle am Fuß der Pyramide."),
                                   ("Threshold and forecourt asset sheets HUB01 to HUB13.", "Asset-Blätter für Schwelle und Vorplatz HUB01 bis HUB13."),
                                   ["HUB07", "A-03"], threshold_set),
    "art/set-pieces.html": head(("Level Set Pieces", "Level-Setpieces"),
                                ("The one-off pieces each level is built around.", "Die Einzelstücke, um die herum jedes Level gebaut ist."),
                                ("Level set pieces for every floor of the climb.", "Level-Setpieces für jede Ebene des Aufstiegs."),
                                ["T4B-SCENE"], set_pieces),
}
