"""The UEFN Islands tab: the five Fortnite islands built from the Sun Temple (English and German).

Each island has a painting (ISL-*, no logo) for cards, and a thumbnail (THUMB-*, made by _builder/compose_thumbnail.py)
shown whole as the page header. Both fall back to an existing picture until uploaded.
"""
from components import feature, facts

# (path, key-art id, fallback picture, name, genre line, players, build order)
ISLANDS = [
    ("islands/trap-galleries.html", "ISL-TRAPS", "T2A-SCENE", "Trap Galleries: 18 Floors",
     ("Deathrun", "Deathrun"), ("1–16 players", "1–16 Spieler")),
    ("islands/ascent.html", "ISL-ASCENT", "KEYART", "Ascent of the Sun Temple: Climbers",
     ("Co-op adventure · the flagship", "Koop-Abenteuer · die Hauptinsel"), ("1–4 players", "1–4 Spieler")),
    ("islands/kaan-expedition.html", "ISL-DIG", "A-04", "Kaan Expedition: Sun Temple Dig",
     ("Tycoon", "Tycoon"), ("1–8 players", "1–8 Spieler")),
    ("islands/illusion-depths.html", "ISL-DEPTHS", "T5A-SCENE", "Illusion Depths",
     ("Co-op escape rooms", "Koop-Escape-Rooms"), ("2–4 players", "2–4 Spieler")),
    ("islands/orb-raiders.html", "ISL-RAIDERS", "T4E-SCENE", "Orb Raiders",
     ("PvPvE extraction", "PvPvE-Extraction"), ("8–16 players", "8–16 Spieler")),
]


def art(ctx, path):
    for p, key, fallback, *_ in ISLANDS:
        if p == path:
            return ctx.pick(key, fallback)


def loops(ctx, rows):
    return '<ol class="loops loops-grid">' + "".join(
        f'<li><span class="loop-label">{ctx.t(*n)}</span><p>{ctx.t(*d)}</p></li>' for n, d in rows) + "</ol>"


def modes(ctx, rows):
    return '<div class="modes">' + "".join(
        f'<article class="mode"><p class="kicker">{ctx.t(*k)}</p><h3>{ctx.t(*n)}</h3><p>{ctx.t(*d)}</p></article>'
        for k, n, d in rows) + "</div>"


def table(ctx, head, rows):
    th = "".join(f"<th>{ctx.t(*h)}</th>" for h in head)
    body = "".join("<tr>" + "".join(
        f'<{"th scope=row" if i == 0 else "td"}>{ctx.t(*c) if isinstance(c, tuple) else c}</{"th" if i == 0 else "td"}>'
        for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="table-wrap"><table class="orb-table"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


def back_link(ctx):
    return (f'<p class="island-back"><a class="text-link" href="{ctx.url("islands/index.html")}">'
            f'{ctx.t("All five islands and the roadmap", "Alle fünf Inseln und die Roadmap")}</a></p>')


# ------------------------------------------------------------------ overview & roadmap
def overview(ctx):
    u, t = ctx.url, ctx.t
    cards = []
    for k, (p, key, fb, name, genre, players) in enumerate(ISLANDS):
        cards.append(feature(
            ctx, ctx.pick(key, fb), t(f"Island {k + 1} · ", f"Insel {k + 1} · ") + t(*genre), name,
            f"<p>{t(*players)}. {t(*BLURBS[p])}</p><p><a href='{u(p)}'>{t('Read the island design', 'Zum Inseldesign')} →</a></p>",
            flip=bool(k % 2)))

    roadmap = [
        (("Foundation", "Fundament"),
         ("The shared base every island is built on: one room standard, one library of traps, platforms and puzzle pieces, "
          "and party play for up to four from the start. Nothing is released yet.",
          "Die gemeinsame Basis aller Inseln: ein Raumstandard, eine Bibliothek aus Fallen, Plattformen und Rätselteilen und "
          "Gruppenspiel für bis zu vier von Anfang an. Noch wird nichts veröffentlicht.")),
        (("Island 1", "Insel 1"),
         ("Trap Galleries ships first. It is quick to build, needs no combat, and shows how the temple's art, gap sizes "
          "and thumbnails land with real Fortnite players.",
          "Trap Galleries erscheint zuerst. Die Insel ist schnell gebaut, braucht keinen Kampf und zeigt, wie die Grafik "
          "des Tempels, die Sprungweiten und die Vorschaubilder bei echten Fortnite-Spielern ankommen.")),
        (("Island 2", "Insel 2"),
         ("The flagship opens in early access: the Threshold, the Shell with Kaya, and Floors 1 to 5. One tier follows "
          "per content update, with Trials opening tier by tier, until the Sky Altar.",
          "Die Hauptinsel startet im Early Access: die Schwelle, The Shell mit Kaya und die Ebenen 1 bis 5. Mit jedem "
          "Inhaltsupdate folgt eine Stufe, die Prüfungen öffnen sich Stufe für Stufe, bis zum Himmelsaltar.")),
        (("Island 3", "Insel 3"),
         ("Kaan Expedition, once the flagship is live: Isabel Kaan's abandoned camp as a tycoon, with real temple rooms "
          "as short dives.",
          "Kaan Expedition, sobald die Hauptinsel läuft: Isabel Kaans verlassenes Lager als Tycoon, mit echten "
          "Tempelräumen als kurze Tauchgänge.")),
        (("Island 4", "Insel 4"),
         ("Illusion Depths, once the puzzle rooms of Tiers III and V exist in the flagship and can be recut for teams.",
          "Illusion Depths, sobald die Rätselräume der Stufen III und V in der Hauptinsel stehen und für Teams "
          "umgebaut werden können.")),
        (("Island 5", "Insel 5"),
         ("Orb Raiders comes last, because it needs everything else: tuned combat, the four orb powers and the Tier IV "
          "sanctums. It is tested first as a weekend event.",
          "Orb Raiders kommt zuletzt, weil es alles andere braucht: abgestimmten Kampf, die vier Kugelkräfte und die "
          "Heiligtümer aus Stufe IV. Zuerst wird es als Wochenend-Event getestet.")),
    ]

    shared = [
        (("Who you are", "Wer du bist"), ("You are a Climber", "Du bist ein Kletterer"),
         ("On every island you play as your own Fortnite character. Kaya, K'in and Oxlahun are the people you meet.",
          "Auf jeder Insel spielst du deine eigene Fortnite-Figur. Kaya, K'in und Oxlahun sind die Menschen, denen du begegnest.")),
        (("What they share", "Was sie teilen"), ("One temple, one set of rooms", "Ein Tempel, ein Satz Räume"),
         ("Every island is cut from the same sealed rooms, traps and art. A room built once can serve a race, a dive, a "
          "puzzle chamber and the campaign.",
          "Jede Insel entsteht aus denselben versiegelten Räumen, Fallen und Grafiken. Ein einmal gebauter Raum kann einem "
          "Rennen, einem Tauchgang, einer Rätselkammer und der Kampagne dienen.")),
        (("How they connect", "Wie sie verbunden sind"), ("Each island stands alone", "Jede Insel steht für sich"),
         ("Each island keeps its own progress. They point to each other through the story, matching cosmetics and links "
          "to the flagship.",
          "Jede Insel speichert ihren eigenen Fortschritt. Sie verweisen über die Geschichte, passende kosmetische "
          "Gegenstände und Links zur Hauptinsel aufeinander.")),
    ]

    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("Mayan Temple Adventures is a family of five Fortnite islands, all set in and around the same living "
                      "Mayan sun temple.",
                      "Mayan Temple Adventures ist eine Familie aus fünf Fortnite-Inseln, die alle in und um denselben "
                      "lebenden Maya-Sonnentempel spielen.")}</p>
    <p>{t("At the centre is the flagship, a co-op climb for up to four players through the Shell, seventeen floors and "
          "the Sky Altar. The other four islands take parts of that temple and turn them into their own genre: a "
          "deathrun through its traps, a tycoon at its foot, co-op escape rooms in its puzzle halls, and a raid on its "
          "elemental sanctums.",
          "Im Zentrum steht die Hauptinsel, ein Koop-Aufstieg für bis zu vier Spieler durch The Shell, siebzehn Ebenen "
          "und den Himmelsaltar. Die anderen vier Inseln nehmen Teile dieses Tempels und machen daraus ein eigenes "
          "Genre: einen Deathrun durch seine Fallen, einen Tycoon an seinem Fuß, Koop-Escape-Rooms in seinen "
          "Rätselhallen und einen Raubzug durch seine Elementarheiligtümer.")}</p>
  </div>
  {modes(ctx, shared)}
</section>

<section class="band"><div class="wrap section">
  <h2>{t("Five islands", "Fünf Inseln")}</h2>
  {"".join(cards)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Roadmap", "Roadmap")}</p>
  <h2>{t("Built in this order", "In dieser Reihenfolge gebaut")}</h2>
  <p class="lede-sm">{t("Every phase ships something playable, and each one tests what the next one depends on. "
                        "Everything before the flagship lowers its risk; everything after it reuses its rooms.",
                        "Jede Phase liefert etwas Spielbares, und jede prüft, worauf die nächste aufbaut. Alles vor der "
                        "Hauptinsel senkt ihr Risiko, alles danach nutzt ihre Räume weiter.")}</p>
  {loops(ctx, roadmap)}
</section>
"""


BLURBS = {
    "islands/trap-galleries.html": (
        "A race up eighteen trap-filled stages inside the temple, with no enemies and no weapons, just timing and nerve.",
        "Ein Wettlauf durch achtzehn Fallenstufen im Inneren des Tempels, ohne Gegner und ohne Waffen, nur mit Timing und Nerven."),
    "islands/ascent.html": (
        "The full climb from the Shell to the Sky Altar, with combat, puzzles, the orb powers and the story, plus the "
        "shuffled Trials and Expedition replays.",
        "Der ganze Aufstieg von The Shell bis zum Himmelsaltar, mit Kampf, Rätseln, den Kugelkräften und der Geschichte, "
        "dazu die gemischten Prüfungen und die Expeditionen."),
    "islands/kaan-expedition.html": (
        "Restore Dr. Isabel Kaan's abandoned dig at the foot of the pyramid, plot by plot, and dive into real temple "
        "rooms for the rare finds.",
        "Bau Dr. Isabel Kaans verlassene Grabung am Fuß der Pyramide Parzelle für Parzelle wieder auf und tauch in echte "
        "Tempelräume, um seltene Funde zu bergen."),
    "islands/illusion-depths.html": (
        "Five puzzle chambers where one player can see what the others must do. Talk, or stay lost.",
        "Fünf Rätselkammern, in denen ein Spieler sieht, was die anderen tun müssen. Redet miteinander, oder ihr bleibt verloren."),
    "islands/orb-raiders.html": (
        "Crews of Climbers raid the four elemental sanctums for relics and orbs, then race for a Sun Portal before the "
        "temple seals.",
        "Kletterer-Crews plündern die vier Elementarheiligtümer nach Relikten und Kugeln und rennen dann zu einem "
        "Sonnenportal, bevor der Tempel sich versiegelt."),
}


# ------------------------------------------------------------------ island 1: deathrun
def trap_galleries(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Deathrun, parkour, platformer", "Deathrun, Parkour, Plattformer")),
        (t("Players", "Spieler"), t("1–16; races for 2–16", "1–16; Rennen für 2–16")),
        (t("Session", "Spielzeit"), t("20–40 minutes; a first full climb takes 25–45", "20–40 Minuten; ein erster kompletter Aufstieg dauert 25–45")),
        (t("Structure", "Aufbau"), t("Six galleries of three stages each", "Sechs Galerien mit je drei Stufen")),
        (t("Build order", "Reihenfolge"), t("Island 1, the first release", "Insel 1, die erste Veröffentlichung")),
    ])
    galleries = [
        (t("I · Flooded Foundations", "I · Überflutete Fundamente"),
         t("The Shell Run, Drowned Logs, Root Swing", "The Shell Run, Treibende Stämme, Wurzelschwung"),
         t("stepping stones, spike strips, floating logs, vine swings", "Trittsteine, Stachelleisten, treibende Stämme, Lianenschwünge")),
        (t("II · Trap Galleries", "II · Fallengalerien"),
         t("Saw Lanes, Dart Colonnade, Collapsing Stair", "Sägebahnen, Pfeilkolonnade, Einstürzende Treppe"),
         t("saws on tracks, dart lanes, crumbling stairs, boulders", "Sägen auf Schienen, Pfeilbahnen, bröckelnde Treppen, Felsbrocken")),
        (t("III · Shifting Vaults", "III · Wandernde Gewölbe"),
         t("Seesaw Pit, Phase Bridges, Calendar Well", "Wippengrube, Phasenbrücken, Kalenderbrunnen"),
         t("seesaws, vanishing platforms, rotating discs", "Wippen, verschwindende Plattformen, rotierende Scheiben")),
        (t("IV · Elemental Sanctums", "IV · Elementarheiligtümer"),
         t("Lava Channels, Broken Ramparts, Rising Cistern", "Lavakanäle, Zerbrochene Wälle, Steigende Zisterne"),
         t("burning bridges, wind gusts, rising water", "brennende Brücken, Windböen, steigendes Wasser")),
        (t("V · Illusion Depths", "V · Tiefen der Täuschung"),
         t("False Floors, Beam Maze, Spirit Chase", "Trugböden, Strahlenlabyrinth, Geisterjagd"),
         t("illusion tiles, sweeping beams, the Guardian Spirit", "Trugkacheln, kreisende Strahlen, der Wächtergeist")),
        (t("VI · Ascension", "VI · Erhebung"),
         t("Elemental Gauntlet, Trap Crucible, The Sky Stair", "Elementarer Spießrutenlauf, Fallenschmelztiegel, Die Himmelstreppe"),
         t("every hazard at once, then the open-sky terraces", "alle Gefahren auf einmal, dann die Terrassen unter freiem Himmel")),
    ]
    gal_rows = "".join(f"<tr><th scope='row'>{g}</th><td>{s}</td><td>{h}</td></tr>" for g, s, h in galleries)
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Climbers race the living temple. Eighteen stages, built only from its traps and moving "
                        "platforms, climb from the flooded foundations to the open sky above the summit.",
                        "Kletterer liefern sich ein Rennen mit dem lebenden Tempel. Achtzehn Stufen, nur aus seinen Fallen "
                        "und beweglichen Plattformen gebaut, führen von den überfluteten Fundamenten bis unter den "
                        "offenen Himmel über dem Gipfel.")}</p>
      <p>{t("There are no enemies, no weapons and no puzzles: only timing. K'in warns before every stage and has dry "
            f"words after every fall. Each gallery takes the look of one tier of <a href='{u('climb/index.html')}'>the climb</a>, "
            "so this island is also the first look at the flagship.",
            "Es gibt keine Gegner, keine Waffen und keine Rätsel, nur Timing. K'in warnt vor jeder Stufe und hat nach jedem "
            "Sturz trockene Worte übrig. Jede Galerie übernimmt das Aussehen einer Stufe "
            f"<a href='{u('climb/index.html')}'>des Aufstiegs</a>, damit ist diese Insel auch der erste Blick auf die Hauptinsel.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, ctx.pick("ISL-ECHO", "HOME-NEVERALONE"), t("Par time", "Richtzeit"), t("Kaya's Echo", "Kayas Echo"),
    t("<p>A golden ghost of Kaya runs every stage at a set pace. Finish to earn bronze, finish without dying for "
      "silver, and beat her Echo for gold.</p><p>It puts Kaya on screen without anyone having to play her.</p>",
      "<p>Ein goldener Geist von Kaya läuft jede Stufe in einem festen Tempo. Ins Ziel kommen bringt Bronze, ohne Tod "
      "ins Ziel kommen Silber, und wer ihr Echo schlägt, holt Gold.</p><p>So ist Kaya im Bild, ohne dass jemand sie "
      "spielen muss.</p>"))}
  {feature(ctx, ctx.pick("ISL-WALL", "SKY-01"), t("The summit", "Der Gipfel"), t("The Wall of Climbers", "Die Wand der Kletterer"),
    t("<p>Everyone who reaches the top has their sigil carved into a mural on the summit, a smaller twin of the "
      f"<a href='{u('characters/climbers/index.html')}'>Spirit Mural</a> in the flagship. The first summit also earns "
      "the Climber's Goggles.</p>",
      "<p>Wer oben ankommt, bekommt sein Zeichen in ein Wandbild auf dem Gipfel gemeißelt, einen kleineren Zwilling des "
      f"<a href='{u('characters/climbers/index.html')}'>Geisterwandbilds</a> auf der Hauptinsel. Der erste Gipfel bringt "
      "außerdem die Kletterer-Brille.</p>"), flip=True)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Six galleries", "Sechs Galerien")}</p>
  <h2>{t("Three stages per tier of the temple", "Drei Stufen pro Tempelstufe")}</h2>
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Gallery", "Galerie")}</th><th>{t("Stages", "Stufen")}</th><th>{t("What you dodge", "Wovor du dich hütest")}</th></tr></thead>
    <tbody>{gal_rows}</tbody>
  </table></div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Modes", "Modi")}</p>
  <h2>{t("Five ways to climb", "Fünf Arten aufzusteigen")}</h2>
  {modes(ctx, [
    (("Default", "Standard"), ("Climb", "Climb"),
     ("A checkpoint at every stage, unlimited falls, and you resume at your highest stage.",
      "Ein Checkpoint an jeder Stufe, beliebig viele Stürze, und du machst an deiner höchsten Stufe weiter.")),
    (("For the skilled", "Für Könner"), ("Hardcore", "Hardcore"),
     ("Checkpoints only at the start of each gallery, and a medal for making it to the top.",
      "Checkpoints nur am Anfang jeder Galerie und eine Medaille für den Weg nach oben.")),
    (("Against the clock", "Gegen die Uhr"), ("Speedrun", "Speedrun"),
     ("The full climb on a timer, with times per stage and Kaya's Echo as par.",
      "Der ganze Aufstieg auf Zeit, mit Zeiten pro Stufe und Kayas Echo als Richtzeit.")),
    (("Together", "Gemeinsam"), ("Race", "Rennen"),
     ("Up to 16 Climbers start together. The first to the Wall of Climbers wins.",
      "Bis zu 16 Kletterer starten gemeinsam. Wer zuerst die Wand der Kletterer erreicht, gewinnt.")),
    (("Every day", "Jeden Tag"), ("Wrath of the Day", "Zorn des Tages"),
     ("One twist for everyone each day: faster spikes, shorter platforms, a stage in fog.",
      "Jeden Tag eine Wendung für alle: schnellere Stacheln, kürzere Plattformen, eine Stufe im Nebel.")),
  ])}
  {back_link(ctx)}
</div></section>
"""


# ------------------------------------------------------------------ island 2: the flagship
def ascent(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Co-op adventure, platformer, puzzle", "Koop-Abenteuer, Plattformer, Rätsel")),
        (t("Players", "Spieler"), t("1–4, as one party", "1–4, als eine Gruppe")),
        (t("Session", "Spielzeit"), t("One floor in 15–25 minutes", "Eine Ebene in 15–25 Minuten")),
        (t("Campaign", "Kampagne"), t("The Shell, seventeen floors, the Sky Altar", "The Shell, siebzehn Ebenen, der Himmelsaltar")),
        (t("Release", "Veröffentlichung"), t("Early access with Floors 0–5, then one tier per update",
                                             "Early Access mit den Ebenen 0–5, dann eine Stufe pro Update")),
    ])
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("The heart of Mayan Temple Adventures: the whole climb through the living pyramid, for up to four "
                        "friends.",
                        "Das Herz von Mayan Temple Adventures: der ganze Aufstieg durch die lebende Pyramide, für bis zu "
                        "vier Freunde.")}</p>
      <p>{t("Kaya climbs the Shell beside you, dies on its traps, and wakes at the Threshold to read the wall. From then "
            "on she sends your party up for evidence while K'in guides you floor by floor and Oxlahun sells you what you "
            "need. Your own likeness is carved into the Spirit Mural the first time the temple takes you.",
            "Kaya klettert mit dir durch The Shell, stirbt an seinen Fallen und erwacht an der Schwelle, um die Wand zu "
            "lesen. Von da an schickt sie deine Gruppe nach Beweisen aus, während K'in euch Ebene für Ebene führt und "
            "Oxlahun euch verkauft, was ihr braucht. Dein eigenes Abbild wird ins Geisterwandbild gemeißelt, sobald der "
            "Tempel dich zum ersten Mal holt.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Four modes, one island", "Vier Modi, eine Insel")}</p>
  <h2>{t("The campaign, and the reasons to come back", "Die Kampagne, und Gründe zurückzukommen")}</h2>
  {modes(ctx, [
    (("First session", "Erste Sitzung"), ("The prologue", "Der Prolog"),
     ("Twenty minutes from Isabel's camp to the first carving: the Shell with Kaya, her death, and the wall.",
      "Zwanzig Minuten von Isabels Lager bis zur ersten Gravur: The Shell mit Kaya, ihr Tod und die Wand.")),
    (("Story", "Story"), ("The Ascent", "Der Aufstieg"),
     ("Floors 0 to 18 in a fixed, hand-built order, with every boss and every story beat.",
      "Die Ebenen 0 bis 18 in fester, von Hand gebauter Reihenfolge, mit jedem Boss und jedem Story-Moment.")),
    (("Replay", "Wiederholen"), ("Trials of the Shifting Temple", "Prüfungen des wandelnden Tempels"),
     ("Rooms shuffle within a tier, under curses you choose. Each tier's Trials open as soon as you clear it.",
      "Die Räume einer Stufe werden gemischt, unter Flüchen, die du wählst. Die Prüfungen einer Stufe öffnen sich, "
      "sobald du sie geschafft hast.")),
    (("Replay", "Wiederholen"), ("Expedition", "Expedition"),
     ("Any cleared floor with your full kit, to open the side routes your orbs now reach.",
      "Jede geschaffte Ebene mit voller Ausrüstung, um die Nebenwege zu öffnen, die deine Kugeln jetzt erreichen.")),
  ])}
</div></section>

<section class="wrap section">
  <h2>{t("Where to read more", "Wo du mehr liest")}</h2>
  {modes(ctx, [
    (("The Game", "Das Spiel"), (f"<a href='{u('game/index.html')}'>Overview &amp; Pillars</a>", f"<a href='{u('game/index.html')}'>Überblick &amp; Säulen</a>"),
     ("What the flagship is, and the five ideas behind it.", "Was die Hauptinsel ist und welche fünf Ideen dahinterstehen.")),
    (("The Game", "Das Spiel"), (f"<a href='{u('game/climbers-and-co-op.html')}'>Climbers &amp; Co-op</a>", f"<a href='{u('game/climbers-and-co-op.html')}'>Kletterer &amp; Koop</a>"),
     ("Playing as yourself, the mural, and how a party of four climbs.", "Als du selbst spielen, das Wandbild und wie eine Vierergruppe klettert.")),
    (("The Climb", "Der Aufstieg"), (f"<a href='{u('climb/index.html')}'>The Pyramid</a>", f"<a href='{u('climb/index.html')}'>Die Pyramide</a>"),
     ("Every tier, floor and room, from the Shell to the Sky Altar.", "Jede Stufe, Ebene und jeder Raum, von The Shell bis zum Himmelsaltar.")),
  ])}
  {back_link(ctx)}
</section>
"""


# ------------------------------------------------------------------ island 3: tycoon
def kaan_expedition(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Tycoon, simulation, adventure", "Tycoon, Simulation, Abenteuer")),
        (t("Players", "Spieler"), t("1–8, one plot each", "1–8, je eine Parzelle")),
        (t("Session", "Spielzeit"), t("30–60 minutes, with a reason to return each day", "30–60 Minuten, mit einem Grund, täglich wiederzukommen")),
        (t("Story role", "Rolle in der Geschichte"), t("Kaya restarts her mother's dig", "Kaya nimmt die Grabung ihrer Mutter wieder auf")),
        (t("Build order", "Reihenfolge"), t("Island 3, after the flagship is live", "Insel 3, nachdem die Hauptinsel läuft")),
    ])
    layers = [
        (("1 · Topsoil", "1 · Oberboden"), ("pottery sherds, obsidian flakes", "Tonscherben, Obsidiansplitter"),
         ("Root Cellar", "Wurzelkeller")),
        (("2 · Flooded Trench", "2 · Überfluteter Graben"), ("jade beads, waterlogged carvings", "Jadeperlen, wassergetränkte Schnitzereien"),
         ("Drowned Gallery, Sluice Hall", "Versunkene Galerie, Schleusenhalle")),
        (("3 · Carved Stone", "3 · Behauener Stein"), ("glyph rubbings, carved stone heads", "Glyphenabriebe, steinerne Köpfe"),
         ("Blowgun Shrine, Plate Vault", "Blasrohrschrein, Plattengewölbe")),
        (("4 · Sealed Gallery", "4 · Versiegelte Galerie"), ("golden idols, trap mechanisms, Key Orb shards", "Goldene Idole, Fallenmechanismen, Splitter von Schlüsselkugeln"),
         ("Saw Gallery, Dart Colonnade, Collapsing Stair", "Sägegalerie, Pfeilkolonnade, Einstürzende Treppe")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Dr. Isabel Kaan's excavation camp still stands at the foot of the pyramid, abandoned the day she "
                        "went higher. Each player claims a plot of it and brings the dig back to life.",
                        "Dr. Isabel Kaans Grabungslager steht noch am Fuß der Pyramide, verlassen an dem Tag, an dem sie "
                        "weiter hinaufging. Jeder Spieler übernimmt eine Parzelle und erweckt die Grabung wieder zum Leben.")}</p>
      <p>{t("Your crew digs up relics while you build. Oxlahun buys every find at a friend's rate. Kaya runs the field "
            "tent and trades her mother's notebook pages for the relics she asks for. And the tunnel into the temple is "
            "open: short dives into real rooms from the climb bring back the rarest finds.",
            "Deine Crew gräbt Relikte aus, während du baust. Oxlahun kauft jeden Fund zum Freundschaftspreis. Kaya führt "
            "das Feldzelt und tauscht die Notizbuchseiten ihrer Mutter gegen die Relikte, um die sie bittet. Und der "
            "Tunnel in den Tempel steht offen: Kurze Tauchgänge in echte Räume des Aufstiegs bringen die seltensten Funde.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Core loops", "Kernkreisläufe")}</p>
  <h2>{t("From ten seconds to a whole season", "Von zehn Sekunden bis zu einer ganzen Saison")}</h2>
  {loops(ctx, [
    (("Collect", "Einsammeln"), ("Walk over the sorting table to bank what your crew has dug up.",
                                 "Über den Sortiertisch gehen und sichern, was deine Crew ausgegraben hat.")),
    (("Build", "Bauen"), ("Add a structure, hire crew or dig deeper.", "Ein Gebäude hinzufügen, Leute einstellen oder tiefer graben.")),
    (("Dive", "Tauchen"), ("Enter the pyramid tunnel, alone or with visitors, clear one temple room in 3–5 minutes and "
                           "come out with rare relics.",
                           "In den Pyramidentunnel gehen, allein oder mit Besuchern, in 3–5 Minuten einen Tempelraum "
                           "schaffen und mit seltenen Relikten herauskommen.")),
    (("Layer", "Schicht"), ("Dig through to the next depth: a new kind of relic and a new dive room.",
                            "Bis zur nächsten Tiefe graben: eine neue Art Relikt und ein neuer Tauchraum.")),
    (("Field season", "Grabungssaison"), ("Close the season, reset the plot and keep a permanent bonus, with each "
                                          "season dated in the Long Count, as Isabel would have done.",
                                          "Die Saison abschließen, die Parzelle zurücksetzen und einen dauerhaften Bonus "
                                          "behalten, jede Saison in der Langen Zählung datiert, wie Isabel es getan hätte.")),
  ])}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("The dig", "Die Grabung")}</p>
  <h2>{t("Four layers, four kinds of find", "Vier Schichten, vier Arten von Funden")}</h2>
  <p class="lede-sm">{t("Each layer matches a part of the temple, so the dig quietly teaches what the climb holds.",
                        "Jede Schicht passt zu einem Teil des Tempels, so zeigt die Grabung ganz nebenbei, was der Aufstieg bereithält.")}</p>
  {table(ctx, [("Layer", "Schicht"), ("Finds", "Funde"), ("Opens dives into", "Öffnet Tauchgänge in")], layers)}
</section>

<section class="band"><div class="wrap section">
  {modes(ctx, [
    (("Shared", "Gemeinsam"), ("The Museum Tent", "Das Museumszelt"),
     ("Every player's rarest find of the season goes on display in the commons, with their name on it.",
      "Der seltenste Fund jedes Spielers aus der Saison wird im Gemeinschaftsbereich ausgestellt, mit seinem Namen daran.")),
    (("Together", "Gemeinsam"), ("Visits and co-op dives", "Besuche und Koop-Tauchgänge"),
     ("Walk through any plot, and join a neighbour's dive to split the finds with a bonus for both.",
      "Durch jede Parzelle spazieren und beim Tauchgang eines Nachbarn mitmachen, um die Funde mit Bonus für beide zu teilen.")),
    (("When night falls", "Wenn es Nacht wird"), ("Night raids", "Nächtliche Überfälle"),
     ("Every so often Risen Guardians walk out of the pyramid toward the plots. Torches and stakes keep them off. "
      "Players never steal from each other.",
      "Ab und zu kommen Erweckte Wächter aus der Pyramide auf die Parzellen zu. Fackeln und Pfähle halten sie fern. "
      "Spieler bestehlen einander nie.")),
  ])}
  {back_link(ctx)}
</div></section>
"""


# ------------------------------------------------------------------ island 4: escape rooms
def illusion_depths(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Co-op escape room, puzzle", "Koop-Escape-Room, Rätsel")),
        (t("Players", "Spieler"), t("2–4 per team; solo with K'in reading for you", "2–4 pro Team; allein mit K'in als Leserin")),
        (t("Session", "Spielzeit"), t("One chamber in 15–25 minutes; all five in about 90", "Eine Kammer in 15–25 Minuten; alle fünf in etwa 90")),
        (t("Story frame", "Rahmen"), t("Kaya's reading lessons", "Kayas Leselektionen")),
        (t("Build order", "Reihenfolge"), t("Island 4, once Tiers III and V exist in the flagship",
                                            "Insel 4, sobald die Stufen III und V auf der Hauptinsel stehen")),
    ])
    chambers = [
        (("Chamber 1 · Tier III", "Kammer 1 · Stufe III"), ("The Memory Path", "Der Pfad der Erinnerung"),
         ("Repeat K'in's song on the stones, then cross a path only the Reader can see.",
          "K'ins Lied auf den Steinen nachspielen, dann einen Pfad überqueren, den nur der Leser sieht.")),
        (("Chamber 2 · Tier V", "Kammer 2 · Stufe V"), ("The Mirror Sanctum", "Das Spiegelheiligtum"),
         ("Aim bronze mirrors as a team while the sun shafts move.", "Bronzespiegel als Team ausrichten, während die Sonnenschächte wandern.")),
        (("Chamber 3 · Tier V", "Kammer 3 · Stufe V"), ("The Prism Vault", "Das Prismengewölbe"),
         ("Tint and mix beams of light. One wrong mix floods the vault with fire.",
          "Lichtstrahlen färben und mischen. Eine falsche Mischung flutet das Gewölbe mit Feuer.")),
        (("Chamber 4 · Tier V", "Kammer 4 · Stufe V"), ("The Hall of Lies", "Die Halle der Lügen"),
         ("Two mirrored halls: each side sees the true floor of the other, never its own.",
          "Zwei gespiegelte Hallen: Jede Seite sieht den echten Boden der anderen, nie den eigenen.")),
        (("Chamber 5 · Tier V", "Kammer 5 · Stufe V"), ("The Totem Vault", "Das Totemgewölbe"),
         ("Turn four totems to an order assembled from the glyphs of the first four chambers.",
          "Vier Totems in eine Reihenfolge drehen, die aus den Glyphen der ersten vier Kammern entsteht.")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Five puzzle chambers recut from the temple's quietest and strangest halls, built so that no one "
                        "can solve them alone.",
                        "Fünf Rätselkammern, umgebaut aus den stillsten und seltsamsten Hallen des Tempels, so gebaut, "
                        "dass niemand sie allein lösen kann.")}</p>
      <p>{t("Kaya frames it as a lesson: the Depths test those who read. At the start of each chamber one player takes "
            "K'in's Glyph Lens and becomes the <strong>Reader</strong>, looking down from a gallery that shows hidden "
            "glyphs, true floors and light paths. The others are the <strong>Climbers</strong>, the only ones who can "
            "work the mechanisms. The roles swap at every stage. The island shares its name with "
            f"<a href='{u('climb/tier-5.html')}'>Tier V</a>, where most of its rooms come from.",
            "Kaya nennt es eine Lektion: Die Tiefen prüfen die, die lesen. Am Anfang jeder Kammer nimmt ein Spieler "
            "K'ins Glyphenlinse und wird zum <strong>Leser</strong>. Er blickt von einer Galerie herab, die verborgene "
            "Glyphen, echte Böden und Lichtwege zeigt. Die anderen sind die <strong>Kletterer</strong>, die als Einzige "
            "die Mechanismen bedienen können. An jeder Station wechseln die Rollen. Die Insel teilt ihren Namen mit "
            f"<a href='{u('climb/tier-5.html')}'>Stufe V</a>, aus der die meisten ihrer Räume stammen.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Five chambers", "Fünf Kammern")}</p>
  <h2>{t("Each one hides a glyph for the last", "Jede verbirgt eine Glyphe für die letzte")}</h2>
  {modes(ctx, chambers)}
</div></section>

<section class="wrap section">
  {feature(ctx, "T5B-SCENE", t("Replay", "Wiederholen"), t("Stars, hints and Remix", "Sterne, Hinweise und Remix"),
    t("<p>Each chamber awards up to three stars: one for finishing, two for beating par, three for beating par "
      "without hints. K'in offers three levels of hint per stage, from a nudge to the answer, and each one costs "
      "score.</p><p>After a first full clear, Remix gives every puzzle a new solution, so the rooms stay the same and "
      "the answers don't. Finishing all five unlocks Kaya's full translation of the Spirit Mural.</p>",
      "<p>Jede Kammer vergibt bis zu drei Sterne: einen fürs Schaffen, zwei für eine Zeit unter der Richtzeit, drei "
      "für eine Zeit unter der Richtzeit ohne Hinweise. K'in bietet pro Station drei Hinweisstufen, vom Anstupsen bis "
      "zur Lösung, und jede kostet Punkte.</p><p>Nach dem ersten kompletten Durchgang gibt Remix jedem Rätsel eine neue "
      "Lösung: Die Räume bleiben gleich, die Antworten nicht. Wer alle fünf schafft, schaltet Kayas vollständige "
      "Übersetzung des Geisterwandbilds frei.</p>"))}
  {back_link(ctx)}
</section>
"""


# ------------------------------------------------------------------ island 5: PvPvE
def orb_raiders(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("PvPvE, extraction, squads", "PvPvE, Extraction, Squads")),
        (t("Players", "Spieler"), t("8–16: four crews of four, or eight duos", "8–16: vier Crews zu viert oder acht Duos")),
        (t("Match", "Match"), t("15 minutes (Raid), 10 minutes (Orb Rush)", "15 Minuten (Raid), 10 Minuten (Orb Rush)")),
        (t("Tone", "Stil"), t("Stylised melee and ranged, no realistic firearms", "Stilisierter Nah- und Fernkampf, keine realistischen Schusswaffen")),
        (t("Build order", "Reihenfolge"), t("Island 5, tested first as a weekend event", "Insel 5, zuerst als Wochenend-Event getestet")),
    ])
    zones = [
        (("Ember Wing", "Glutflügel"), ("Fire", "Feuer"), ("lava channels, burning bridges, fire jets", "Lavakanäle, brennende Brücken, Feuerstrahlen"),
         ("light four braziers in 30 seconds", "vier Feuerschalen in 30 Sekunden entzünden")),
        (("Ossuary Wing", "Beinhausflügel"), ("Earth", "Erde"), ("cracked walls, heavy plates, boulders", "rissige Wände, schwere Platten, Felsbrocken"),
         ("push two boulders onto the plates", "zwei Felsbrocken auf die Platten schieben")),
        (("Rampart Wing", "Wallflügel"), ("Wind", "Wind"), ("gusts, updrafts, open sky", "Böen, Aufwinde, offener Himmel"),
         ("ride the updrafts to the spire top", "mit den Aufwinden zur Turmspitze")),
        (("Reservoir Wing", "Reservoirflügel"), ("Water", "Wasser"), ("rising and falling water, currents", "steigendes und fallendes Wasser, Strömungen"),
         ("claim it at low water", "bei Niedrigwasser holen")),
        (("Sun Well", "Sonnenbrunnen"), ("—", "—"), ("roaming Guardian Spirits", "umherstreifende Wächtergeister"),
         ("the richest vault, opens at 8 minutes", "das reichste Gewölbe, öffnet nach 8 Minuten")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Crews of Climbers work Oxlahun's bounty board, raiding the four elemental sanctums for relics "
                        "and orbs. They are exactly the greedy adventurers the temple was built to trap.",
                        "Kletterer-Crews arbeiten Oxlahuns Kopfgeldtafel ab und plündern die vier Elementarheiligtümer "
                        "nach Relikten und Kugeln. Sie sind genau die gierigen Abenteurer, für die der Tempel als Falle "
                        "gebaut wurde.")}</p>
      <p>{t("Risen guardians patrol the wings, Guardian Spirits roam between them, and the other crews want the same "
            "loot. Grab what you can, then reach a Sun Portal before the temple seals. You only ever risk what you "
            "picked up in that match. K'in warns everyone equally, and does not approve.",
            "Erweckte Wächter patrouillieren in den Flügeln, Wächtergeister streifen zwischen ihnen umher, und die anderen "
            "Crews wollen dieselbe Beute. Schnapp dir, was du kannst, und erreich ein Sonnenportal, bevor der Tempel "
            "sich versiegelt. Du riskierst immer nur, was du in diesem Match aufgehoben hast. K'in warnt alle "
            "gleichermaßen und ist nicht einverstanden.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("The Sanctum Ring", "Der Heiligtumsring")}</p>
  <h2>{t("Four wings around the Sun Well", "Vier Flügel um den Sonnenbrunnen")}</h2>
  <p class="lede-sm">{t(f"Built from the rooms of <a href='{u('climb/tier-4.html')}'>Tier IV</a>, joined into one "
                        "connected map with four jungle camps to start from.",
                        f"Gebaut aus den Räumen von <a href='{u('climb/tier-4.html')}'>Stufe IV</a>, verbunden zu einer "
                        "zusammenhängenden Karte mit vier Dschungellagern als Startpunkten.")}</p>
  {table(ctx, [("Zone", "Zone"), ("Orb", "Kugel"), ("Hazards", "Gefahren"), ("To claim it", "Um sie zu holen")], zones)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("A raid", "Ein Raid")}</p>
  <h2>{t("Fifteen minutes, three portals", "Fünfzehn Minuten, drei Portale")}</h2>
  {loops(ctx, [
    (("0:00", "0:00"), ("Crews spawn at the jungle camps with a basic kit and one bounty card each.",
                        "Die Crews starten in den Dschungellagern mit einer Grundausrüstung und je einer Kopfgeldkarte.")),
    (("6:00", "6:00"), ("The first Sun Portal opens for 60 seconds. Leave early with less, or stay.",
                        "Das erste Sonnenportal öffnet sich für 60 Sekunden. Früh mit weniger gehen oder bleiben.")),
    (("8:00", "8:00"), ("The Sun Well opens, and Guardian Spirits start to roam.",
                        "Der Sonnenbrunnen öffnet sich, und die Wächtergeister beginnen umherzustreifen.")),
    (("Any time", "Jederzeit"), ("Claim an orb and its power is yours for the match, but you glow, and everyone sees "
                                 "you on the map.",
                                 "Wer eine Kugel holt, hat ihre Kraft für das Match, leuchtet aber und ist für alle "
                                 "auf der Karte zu sehen.")),
    (("14:00", "14:00"), ("The last portal opens, and the temple starts sealing its wings one by one.",
                          "Das letzte Portal öffnet sich, und der Tempel beginnt, seine Flügel einen nach dem anderen zu versiegeln.")),
  ])}
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "W05", t("Quick mode", "Schneller Modus"), t("Orb Rush", "Orb Rush"),
    t("<p>Two teams, four orbs on their altars, ten minutes. Hold orbs at your team's Sun Portal to score. Carriers "
      "glow, and an orb drops when its carrier goes down. Quick to read, and the first thing to be built and tested.</p>",
      "<p>Zwei Teams, vier Kugeln auf ihren Altären, zehn Minuten. Wer Kugeln am Sonnenportal seines Teams hält, "
      "punktet. Träger leuchten, und eine Kugel fällt, sobald ihr Träger am Boden ist. Schnell zu verstehen und das "
      "Erste, was gebaut und getestet wird.</p>"))}
  {back_link(ctx)}
</div></section>
"""


PAGES = {
    "islands/index.html": dict(
        title=("UEFN Islands", "UEFN-Inseln"), kicker=("Mayan Temple Adventures", "Mayan Temple Adventures"),
        banner=["ISL-ALL", "KEYART"],
        lede=("One temple, five Fortnite islands, all cut from the same rooms, traps and characters.",
              "Ein Tempel, fünf Fortnite-Inseln, alle aus denselben Räumen, Fallen und Figuren geschnitten."),
        description=("The five Fortnite islands of Mayan Temple Adventures, and the order they are built in.",
                     "Die fünf Fortnite-Inseln von Mayan Temple Adventures und die Reihenfolge, in der sie entstehen."),
        body=overview, og=["ISL-ALL", "KEYART"]),
    "islands/trap-galleries.html": dict(
        title=("Trap Galleries: 18 Floors", "Trap Galleries: 18 Floors"), kicker=("Island 1 · Deathrun", "Insel 1 · Deathrun"),
        banner=["THUMB-TRAPS", "ISL-TRAPS", "T2A-SCENE"], banner_full=True,
        lede=("Eighteen trap stages up the inside of the temple. No enemies, no weapons, just timing.",
              "Achtzehn Fallenstufen im Inneren des Tempels hinauf. Keine Gegner, keine Waffen, nur Timing."),
        description=("Island 1: a deathrun through the Sun Temple's traps for 1–16 players.",
                     "Insel 1: ein Deathrun durch die Fallen des Sonnentempels für 1–16 Spieler."),
        body=trap_galleries, og=["THUMB-TRAPS", "ISL-TRAPS", "T2A-SCENE"]),
    "islands/ascent.html": dict(
        title=("Ascent of the Sun Temple: Climbers", "Ascent of the Sun Temple: Climbers"),
        kicker=("Island 2 · The flagship", "Insel 2 · Die Hauptinsel"),
        banner=["THUMB-ASCENT", "ISL-ASCENT", "KEYART"], banner_full=True,
        lede=("The whole climb, for up to four friends: the Shell, seventeen floors and the Sky Altar.",
              "Der ganze Aufstieg, für bis zu vier Freunde: The Shell, siebzehn Ebenen und der Himmelsaltar."),
        description=("Island 2: the co-op flagship, from the prologue with Kaya to the Sky Altar.",
                     "Insel 2: die Koop-Hauptinsel, vom Prolog mit Kaya bis zum Himmelsaltar."),
        body=ascent, og=["THUMB-ASCENT", "ISL-ASCENT", "KEYART"]),
    "islands/kaan-expedition.html": dict(
        title=("Kaan Expedition: Sun Temple Dig", "Kaan Expedition: Sun Temple Dig"), kicker=("Island 3 · Tycoon", "Insel 3 · Tycoon"),
        banner=["THUMB-DIG", "ISL-DIG", "A-04"], banner_full=True,
        lede=("Restore Isabel Kaan's abandoned camp, plot by plot, and dive into the temple for the rare finds.",
              "Bau Isabel Kaans verlassenes Lager Parzelle für Parzelle wieder auf und tauch in den Tempel, um seltene Funde zu bergen."),
        description=("Island 3: a tycoon at the foot of the pyramid, with short dives into real temple rooms.",
                     "Insel 3: ein Tycoon am Fuß der Pyramide, mit kurzen Tauchgängen in echte Tempelräume."),
        body=kaan_expedition, og=["THUMB-DIG", "ISL-DIG", "A-04"]),
    "islands/illusion-depths.html": dict(
        title=("Illusion Depths", "Illusion Depths"), kicker=("Island 4 · Co-op escape rooms", "Insel 4 · Koop-Escape-Rooms"),
        banner=["THUMB-DEPTHS", "ISL-DEPTHS", "T5A-SCENE"], banner_full=True,
        lede=("Five puzzle chambers where one player can see what the others must do.",
              "Fünf Rätselkammern, in denen ein Spieler sieht, was die anderen tun müssen."),
        description=("Island 4: co-op escape rooms recut from the temple's puzzle halls.",
                     "Insel 4: Koop-Escape-Rooms, umgebaut aus den Rätselhallen des Tempels."),
        body=illusion_depths, og=["THUMB-DEPTHS", "ISL-DEPTHS", "T5A-SCENE"]),
    "islands/orb-raiders.html": dict(
        title=("Orb Raiders", "Orb Raiders"), kicker=("Island 5 · PvPvE", "Insel 5 · PvPvE"),
        banner=["THUMB-RAIDERS", "ISL-RAIDERS", "T4E-SCENE"], banner_full=True,
        lede=("Raid the elemental sanctums for relics and orbs, then make it to a Sun Portal before the temple seals.",
              "Plündere die Elementarheiligtümer nach Relikten und Kugeln und erreich ein Sonnenportal, bevor der Tempel sich versiegelt."),
        description=("Island 5: a light extraction raid on the four elemental sanctums.",
                     "Insel 5: ein leichter Extraction-Raid durch die vier Elementarheiligtümer."),
        body=orb_raiders, og=["THUMB-RAIDERS", "ISL-RAIDERS", "T4E-SCENE"]),
}
