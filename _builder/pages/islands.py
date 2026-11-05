"""The Game Types tab: every Fortnite game built from the Sun Temple (English and German).

The tab and its URLs still live under islands/, because the pages started as one page per island. How the game
types are grouped into Fortnite islands (one each, or several behind a hub) is still open.

Each game type has a painting (ISL-*, no logo) for cards, and a thumbnail (THUMB-*, made by
_builder/compose_thumbnail.py) shown whole as the page header. Both fall back to an existing picture until uploaded.
"""
from components import feature, facts

# Number words for "nine game types"; the count always comes from len(ISLANDS).
COUNT = {5: ("five", "fünf"), 6: ("six", "sechs"), 7: ("seven", "sieben"), 8: ("eight", "acht"), 9: ("nine", "neun"),
         10: ("ten", "zehn"), 11: ("eleven", "elf"), 12: ("twelve", "zwölf")}


def count_word(ctx, capital=False):
    w = ctx.t(*COUNT[len(ISLANDS)])
    return w[0].upper() + w[1:] if capital else w


# (path, key-art id, fallback picture, name, genre line, players), in the order the site lists them:
# the flagship first, then the other temple islands, then the four newer game types.
ISLANDS = [
    ("islands/ascent.html", "ISL-ASCENT", "KEYART", "Ascent of the Sun Temple",
     ("Co-op adventure · the flagship", "Koop-Abenteuer · die Hauptinsel"), ("1–4 players", "1–4 Spieler")),
    ("islands/trap-galleries.html", "ISL-TRAPS", "T2A-SCENE", "Trap Galleries: 18 Floors",
     ("Deathrun", "Deathrun"), ("1–16 players", "1–16 Spieler")),
    ("islands/sun-temple-dig.html", "ISL-DIG", "A-04", "Sun Temple Dig",
     ("Tycoon", "Tycoon"), ("1–8 players", "1–8 Spieler")),
    ("islands/illusion-depths.html", "ISL-DEPTHS", "T5A-SCENE", "Illusion Depths",
     ("Co-op escape rooms", "Koop-Escape-Rooms"), ("2–4 players", "2–4 Spieler")),
    ("islands/orb-raiders.html", "ISL-RAIDERS", "T4E-SCENE", "Orb Raiders",
     ("PvPvE extraction", "PvPvE-Extraction"), ("8–16 players", "8–16 Spieler")),
    ("islands/hold-your-breath.html", "ISL-HYB", "HYB-SCENE1", "Hold Your Breath",
     ("Party heist · freeze and steal", "Party-Raubzug · erstarren und stehlen"), ("1–8 players", "1–8 Spieler")),
    ("islands/lost-passages.html", "ISL-LP", "T2E-SCENE", "The Lost Passages",
     ("Side-view trap platformer", "Fallen-Plattformer in Seitenansicht"), ("1 player", "1 Spieler")),
    ("islands/trap-architects.html", "ISL-TA", "T2C-SCENE", "Trap Architects",
     ("Build-and-run party game", "Bau-und-Lauf-Partyspiel"), ("2–8 players", "2–8 Spieler")),
    ("islands/calendar-fall.html", "ISL-CF", "T3B-SCENE", "Calendar Fall",
     ("Party knockout", "Party-Knockout"), ("2–16 players", "2–16 Spieler")),
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


def shots(ctx, items):
    """A gallery of the pictures that exist so far; nothing at all until the first one is uploaded."""
    have = [(i, ctx.t(*c)) for i, c in items if ctx.has(i)]
    return ctx.gallery(have) if have else ""


def back_link(ctx):
    return (f'<p class="island-back"><a class="text-link" href="{ctx.url("islands/index.html")}">'
            f'{ctx.t("All " + count_word(ctx) + " game types and the roadmap", "Alle " + count_word(ctx) + " Spieltypen und die Roadmap")}</a></p>')


# ------------------------------------------------------------------ overview & roadmap
def overview(ctx):
    u, t = ctx.url, ctx.t
    cards = []
    for k, (p, key, fb, name, genre, players) in enumerate(ISLANDS):
        cards.append(feature(
            ctx, ctx.pick(key, fb), t(*genre), name,
            f"<p>{t(*players)}. {t(*BLURBS[p])}</p><p><a href='{u(p)}'>{t('Read the design', 'Zum Design')} →</a></p>",
            flip=bool(k % 2)))

    roadmap = [
        (("Foundation", "Fundament"),
         ("The shared base every island is built on: one room standard, one library of traps, platforms and puzzle pieces, "
          "and party play for up to four from the start. Nothing is released yet.",
          "Die gemeinsame Basis aller Inseln: ein Raumstandard, eine Bibliothek aus Fallen, Plattformen und Rätselteilen und "
          "Gruppenspiel für bis zu vier von Anfang an. Noch wird nichts veröffentlicht.")),
        (("First builds", "Erste Bauten"),
         ("Hold Your Breath and The Lost Passages are built first. They are small, complete games, and building them "
          "defines the shared modular kit of walls, floors and traps that every other game type reuses.",
          "Hold Your Breath und The Lost Passages entstehen zuerst. Es sind kleine, vollständige Spiele, und mit ihnen "
          "entsteht das gemeinsame Baukasten-Set aus Wänden, Böden und Fallen, das alle anderen Spieltypen weiterverwenden.")),
        (("Release 1", "Veröffentlichung 1"),
         ("Trap Galleries ships first. It is quick to build, needs no combat, and shows how the temple's art, gap sizes "
          "and thumbnails land with real Fortnite players.",
          "Trap Galleries erscheint zuerst. Die Insel ist schnell gebaut, braucht keinen Kampf und zeigt, wie die Grafik "
          "des Tempels, die Sprungweiten und die Vorschaubilder bei echten Fortnite-Spielern ankommen.")),
        (("Release 2", "Veröffentlichung 2"),
         ("The flagship opens in early access: the Threshold, the Shell with Kaya, and Floors 1 to 5. One tier follows "
          "per content update, with Trials opening tier by tier, until the Sky Altar.",
          "Die Hauptinsel startet im Early Access: die Schwelle, The Shell mit Kaya und die Ebenen 1 bis 5. Mit jedem "
          "Inhaltsupdate folgt eine Stufe, die Prüfungen öffnen sich Stufe für Stufe, bis zum Himmelsaltar.")),
        (("Release 3", "Veröffentlichung 3"),
         ("Sun Temple Dig, once the flagship is live: Isabel Kaan's abandoned camp as a tycoon, with real temple rooms "
          "as short dives.",
          "Sun Temple Dig, sobald die Hauptinsel läuft: Isabel Kaans verlassenes Lager als Tycoon, mit echten "
          "Tempelräumen als kurze Tauchgänge.")),
        (("Release 4", "Veröffentlichung 4"),
         ("Illusion Depths, once the puzzle rooms of Tiers III and V exist in the flagship and can be recut for teams.",
          "Illusion Depths, sobald die Rätselräume der Stufen III und V in der Hauptinsel stehen und für Teams "
          "umgebaut werden können.")),
        (("Release 5", "Veröffentlichung 5"),
         ("Orb Raiders comes last, because it needs everything else: tuned combat, the four orb powers and the Tier IV "
          "sanctums. It is tested first as a weekend event.",
          "Orb Raiders kommt zuletzt, weil es alles andere braucht: abgestimmten Kampf, die vier Kugelkräfte und die "
          "Heiligtümer aus Stufe IV. Zuerst wird es als Wochenend-Event getestet.")),
        (("Later", "Später"),
         ("Trap Architects and Calendar Fall follow once the kit and the trap timings are proven. Trap Architects also "
          "becomes the lab for a Keeper mode in Trap Galleries.",
          "Trap Architects und Calendar Fall folgen, sobald das Baukasten-Set und die Fallen-Timings erprobt sind. "
          "Trap Architects wird außerdem zum Labor für einen Keeper-Modus in Trap Galleries.")),
    ]

    shared = [
        (("Who you are", "Wer du bist"), ("You are a Climber", "Du bist ein Kletterer"),
         ("In every game type you play as your own Fortnite character. Kaya, K'in and Oxlahun are the people you meet.",
          "In jedem Spieltyp spielst du deine eigene Fortnite-Figur. Kaya, K'in und Oxlahun sind die Menschen, denen du begegnest.")),
        (("What they share", "Was sie teilen"), ("One temple, one kit", "Ein Tempel, ein Baukasten"),
         ("Every game type is built from the same modular kit of rooms, traps and art. A room built once can serve a "
          "race, a heist, a puzzle chamber and the campaign.",
          "Jeder Spieltyp entsteht aus demselben modularen Baukasten aus Räumen, Fallen und Grafiken. Ein einmal gebauter "
          "Raum kann einem Rennen, einem Raubzug, einer Rätselkammer und der Kampagne dienen.")),
        (("How they connect", "Wie sie verbunden sind"), ("Islands and a hub", "Inseln und ein Hub"),
         ("The big game types get their own Fortnite island. The shorter ones may share one island, reached from a hub "
          "in the temple. All of them point to each other through the story and to the flagship.",
          "Die großen Spieltypen bekommen eine eigene Fortnite-Insel. Die kürzeren teilen sich vielleicht eine Insel, die "
          "man über einen Hub im Tempel erreicht. Alle verweisen über die Geschichte aufeinander und auf die Hauptinsel.")),
    ]

    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("Mayan Temple Adventures is a family of " + count_word(ctx) + " Fortnite game types, all set in "
                      "and around the same living Mayan sun temple.",
                      "Mayan Temple Adventures ist eine Familie aus " + count_word(ctx) + " Fortnite-Spieltypen, die alle "
                      "in und um denselben lebenden Maya-Sonnentempel spielen.")}</p>
    <p>{t("At the centre is the flagship, a co-op climb for up to four players through the Shell, seventeen floors and "
          "the Sky Altar. Four more take parts of that temple and turn them into their own genre: a deathrun through "
          "its traps, a tycoon at its foot, co-op escape rooms in its puzzle halls, and a raid on its elemental "
          "sanctums. The newest four are shorter games: a freeze-and-steal heist, a side-view trap platformer, a "
          "party game where you build traps for your friends, and a knockout on the temple's calendar.",
          "Im Zentrum steht die Hauptinsel, ein Koop-Aufstieg für bis zu vier Spieler durch The Shell, siebzehn Ebenen "
          "und den Himmelsaltar. Vier weitere nehmen Teile dieses Tempels und machen daraus ein eigenes Genre: einen "
          "Deathrun durch seine Fallen, einen Tycoon an seinem Fuß, Koop-Escape-Rooms in seinen Rätselhallen und einen "
          "Raubzug durch seine Elementarheiligtümer. Die neuesten vier sind kürzere Spiele: ein Raubzug, bei dem du "
          "erstarren musst, ein Fallen-Plattformer in Seitenansicht, ein Partyspiel, in dem du Fallen für deine Freunde "
          "baust, und ein Knockout auf dem Kalender des Tempels.")}</p>
  </div>
  {modes(ctx, shared)}
</section>

<section class="band"><div class="wrap section">
  <h2>{t(count_word(ctx, True) + " game types", count_word(ctx, True) + " Spieltypen")}</h2>
  {"".join(cards)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Roadmap", "Roadmap")}</p>
  <h2>{t("Built in this order", "In dieser Reihenfolge gebaut")}</h2>
  <p class="lede-sm">{t("Every phase ships something playable, and each one tests what the next one depends on. "
                        "Everything before the flagship lowers its risk; everything after it reuses its rooms and kit.",
                        "Jede Phase liefert etwas Spielbares, und jede prüft, worauf die nächste aufbaut. Alles vor der "
                        "Hauptinsel senkt ihr Risiko, alles danach nutzt ihre Räume und den Baukasten weiter.")}</p>
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
    "islands/sun-temple-dig.html": (
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
    "islands/hold-your-breath.html": (
        "Steal the temple's golden idols and freeze whenever its stone eyes open. Move while it looks, and you drop "
        "everything.",
        "Stiehl die goldenen Idole des Tempels und erstarre, sobald seine Steinaugen sich öffnen. Wer sich bewegt, "
        "während er hinsieht, verliert alles."),
    "islands/lost-passages.html": (
        "A side-on trap platformer through the builders' hidden passages, one screen and one trap puzzle at a time.",
        "Ein Fallen-Plattformer in Seitenansicht durch die verborgenen Gänge der Erbauer, ein Bildschirm und ein "
        "Fallenrätsel nach dem anderen."),
    "islands/trap-architects.html": (
        "Sixty seconds to build a trap section, then everyone runs everyone's traps. Hard is good; fair is required.",
        "Sechzig Sekunden, um einen Fallenabschnitt zu bauen, dann laufen alle durch die Fallen aller. Schwer ist gut, "
        "fair ist Pflicht."),
    "islands/calendar-fall.html": (
        "K'in calls a day sign and every stone that wears it falls. Three turning calendar wheels, one sacred well, "
        "one Climber left standing.",
        "K'in ruft ein Tageszeichen, und jeder Stein, der es trägt, fällt. Drei drehende Kalenderräder, ein heiliger "
        "Brunnen, ein Kletterer, der stehen bleibt."),
}


# ------------------------------------------------------------------ island 1: deathrun
def trap_galleries(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Deathrun, parkour, platformer", "Deathrun, Parkour, Plattformer")),
        (t("Players", "Spieler"), t("1–16; races for 2–16", "1–16; Rennen für 2–16")),
        (t("Session", "Spielzeit"), t("20–40 minutes; a first full climb takes 25–45", "20–40 Minuten; ein erster kompletter Aufstieg dauert 25–45")),
        (t("Structure", "Aufbau"), t("Six galleries of three stages each", "Sechs Galerien mit je drei Stufen")),
        (t("Release", "Veröffentlichung"), t("The first release", "Die erste Veröffentlichung")),
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
def sun_temple_dig(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Tycoon, simulation, adventure", "Tycoon, Simulation, Abenteuer")),
        (t("Players", "Spieler"), t("1–8, one plot each", "1–8, je eine Parzelle")),
        (t("Session", "Spielzeit"), t("30–60 minutes, with a reason to return each day", "30–60 Minuten, mit einem Grund, täglich wiederzukommen")),
        (t("Story role", "Rolle in der Geschichte"), t("Kaya restarts her mother's dig", "Kaya nimmt die Grabung ihrer Mutter wieder auf")),
        (t("Release", "Veröffentlichung"), t("After the flagship is live", "Nachdem die Hauptinsel läuft")),
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
        (t("Release", "Veröffentlichung"), t("Once Tiers III and V exist in the flagship",
                                            "Sobald die Stufen III und V auf der Hauptinsel stehen")),
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
        (t("Release", "Veröffentlichung"), t("Last, tested first as a weekend event", "Zuletzt, zuerst als Wochenend-Event getestet")),
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


# ------------------------------------------------------------------ game type: Hold Your Breath
def hold_your_breath(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Party game, stealth, heist", "Partyspiel, Schleichen, Raubzug")),
        (t("Players", "Spieler"), t("1–8; alone it becomes a time trial", "1–8; allein wird es ein Zeitrennen")),
        (t("Round", "Runde"), t("4 minutes; a session is 4–6 rounds", "4 Minuten; eine Sitzung sind 4–6 Runden")),
        (t("Map", "Karte"), t("The Breathing Court: four rooms and the Serpent Run", "Der atmende Hof: vier Räume und der Schlangenlauf")),
        (t("Tone", "Stil"), t("No weapons, no damage, no building", "Keine Waffen, kein Schaden, kein Bauen")),
    ])
    rooms = [
        (("Entry Hall", "Eingangshalle"), ("A practice face that teaches the rule before the round starts, and K'in's brazier, where idols are banked.",
                                           "Ein Übungsgesicht, das die Regel vor der Runde beibringt, und K'ins Feuerschale, an der Idole abgegeben werden.")),
        (("Gallery of Eyes", "Galerie der Augen"), ("Twin heads with a random beat, pillars to hide behind and green leaf-glyph shade.",
                                                    "Zwillingsköpfe mit zufälligem Takt, Pfeiler zum Verstecken und grüne Blattglyphen als Schatten.")),
        (("Spike Court", "Stachelhof"), ("The Sun Mask keeps a steady, learnable beat. When it looks, the spikes rise: freeze, and be on a sun stone.",
                                         "Die Sonnenmaske hält einen festen, lernbaren Takt. Wenn sie hinsieht, steigen die Stacheln: erstarren, und zwar auf einem Sonnenstein.")),
        (("Jaguar Sanctum", "Jaguarheiligtum"), ("The greedy room: short rests, long looks, and the Great Idol on its altar.",
                                                 "Der gierige Raum: kurze Pausen, lange Blicke und das Große Idol auf seinem Altar.")),
        (("Serpent Run", "Schlangenlauf"), ("The shortcut home. It opens only while someone carries the Great Idol, has no shade, and crosses a crumbling bridge.",
                                            "Die Abkürzung nach Hause. Sie öffnet sich nur, solange jemand das Große Idol trägt, hat keinen Schatten und führt über eine bröckelnde Brücke.")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Sneak into the living temple, steal its golden idols, and freeze whenever the temple holds its breath.",
                        "Schleich dich in den lebenden Tempel, stiehl seine goldenen Idole und erstarre, sobald der Tempel den Atem anhält.")}</p>
      <p>{t("Stone heads open their eyes on a drumbeat. Anyone still moving is blown back to the last shrine and drops "
            "their loot. Up to eight Climbers race, freeze, pose and steal idols from each other in four-minute rounds. "
            "Steal them, Climbers, and K'in will pretend she didn't see you.",
            "Steinköpfe öffnen auf einen Trommelschlag ihre Augen. Wer sich dann noch bewegt, wird zum letzten Schrein "
            "zurückgeblasen und verliert seine Beute. Bis zu acht Kletterer rennen, erstarren, posieren und stehlen "
            "einander die Idole, in Runden von vier Minuten. Stehlt sie, Kletterer, und K'in tut so, als hätte sie nichts gesehen.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "HYB-SCENE1", t("The one rule", "Die eine Regel"), t("The temple breathes", "Der Tempel atmet"),
    t("<p>Each room has a watcher, a stone face with its own beat. While it sleeps, you move. When it stirs, its "
      "eyes glow orange and you have a second to find a spot. When it looks, its eyes blaze gold, and anyone who "
      "moves is seen.</p><p>Green leaf-glyph shade hides you. Standing emotes are safe, so every look ends in a row "
      "of Fortnite characters frozen in their best statue pose.</p>",
      "<p>Jeder Raum hat einen Wächter, ein Steingesicht mit eigenem Takt. Solange es schläft, bewegst du dich. Wenn "
      "es sich regt, glühen seine Augen orange, und du hast eine Sekunde, um einen Platz zu finden. Wenn es hinsieht, "
      "lodern seine Augen golden, und wer sich bewegt, wird gesehen.</p><p>Grüne Blattglyphen spenden Schatten und "
      "verstecken dich. Emotes im Stehen sind sicher, also endet jeder Blick mit einer Reihe von Fortnite-Figuren in "
      "ihrer besten Statuenpose.</p>"))}
  {feature(ctx, "HYB-SCENE3", t("Idols", "Idole"), t("Take it, or take it from someone", "Nimm es, oder nimm es jemandem ab"),
    t("<p>Small idols are worth 2 points, the Great Idol 5. Carry one to K'in's brazier to bank it. Stay close to a "
      "carrier for half a second and the idol jumps to you, but stealing during a look gets you caught too: steal "
      "the moment the eyes close.</p><p>The Great Idol glows, so shade won't hide its carrier, and taking it wakes "
      "the temple: every watcher breathes faster until it is banked.</p>",
      "<p>Kleine Idole bringen 2 Punkte, das Große Idol 5. Bring eins zu K'ins Feuerschale, um es zu sichern. Bleib "
      "eine halbe Sekunde nah an einem Träger, und das Idol springt zu dir. Wer aber während eines Blicks stiehlt, "
      "wird selbst erwischt: Stiehl, sobald sich die Augen schließen.</p><p>Das Große Idol leuchtet, darum versteckt "
      "der Schatten seinen Träger nicht, und wer es nimmt, weckt den Tempel: Alle Wächter atmen schneller, bis es "
      "gesichert ist.</p>"), flip=True)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("The map", "Die Karte")}</p>
  <h2>{t("The Breathing Court", "Der atmende Hof")}</h2>
  <div class="feature">
    <div class="feature-media">{ctx.figure("HYB-MAP", alt=t("Map of the Breathing Court", "Karte des atmenden Hofs"))}</div>
    <div class="feature-text">
      <p>{t("One temple interior, four rooms deep, with the Serpent Run along its side. Each room breathes at its own "
            "tempo, so every trip is a choice between the safe way through the shade and the fast way through the open.",
            "Ein Tempelinneres, vier Räume tief, mit dem Schlangenlauf an der Seite. Jeder Raum atmet in seinem eigenen "
            "Tempo, also ist jeder Weg eine Wahl zwischen dem sicheren Weg durch den Schatten und dem schnellen über freie Fläche.")}</p>
      {table(ctx, [("Room", "Raum"), ("What happens there", "Was dort passiert")], rooms)}
    </div>
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "HYB-SCENE2", t("Room three", "Raum drei"), t("Freeze on gold", "Auf Gold erstarren"),
    t("<p>In the Spike Court, freezing is not enough. When the Sun Mask looks, the spikes rise everywhere except "
      "on the fourteen sun stones, so you need to stop on gold, not on grey.</p>",
      "<p>Im Stachelhof reicht Erstarren nicht. Wenn die Sonnenmaske hinsieht, steigen die Stacheln überall außer auf "
      "den vierzehn Sonnensteinen, du musst also auf Gold stehen bleiben, nicht auf Grau.</p>"))}
  {feature(ctx, "HYB-SCENE4", t("The shortcut", "Die Abkürzung"), t("The Serpent Run", "Der Schlangenlauf"),
    t("<p>Taking the Great Idol opens the Serpent Door. The corridor behind it is the fast way home, about fifteen "
      "seconds instead of forty, but its serpent watcher is quick, there is no shade at all, and its bridge "
      "crumbles under your feet.</p>",
      "<p>Wer das Große Idol nimmt, öffnet die Schlangentür. Der Gang dahinter ist der schnelle Weg nach Hause, "
      "etwa fünfzehn Sekunden statt vierzig, aber sein Schlangenwächter ist schnell, es gibt keinen Schatten, und die "
      "Brücke bröckelt unter deinen Füßen.</p>"), flip=True)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("A round", "Eine Runde")}</p>
  <h2>{t("Four minutes, and the temple wakes up", "Vier Minuten, und der Tempel wacht auf")}</h2>
  {loops(ctx, [
    (("Lobby", "Lobby"), ("The practice face catches you once, so you learn the rule without reading a word.",
                          "Das Übungsgesicht erwischt dich einmal, so lernst du die Regel, ohne ein Wort zu lesen.")),
    (("4:00", "4:00"), ("The gates drop with a gong. Race for the idols.", "Mit einem Gong fallen die Tore. Lauf zu den Idolen.")),
    (("2:00", "2:00"), ("The temple stirs: every watcher rests a little less.", "Der Tempel regt sich: Jeder Wächter ruht etwas kürzer.")),
    (("0:30", "0:30"), ("Sunset: every idol is worth double, and the Serpent Door stays open.",
                        "Sonnenuntergang: Jedes Idol zählt doppelt, und die Schlangentür bleibt offen.")),
    (("Results", "Ergebnis"), ("The top three stand on the podium; everyone else freezes for the photo.",
                               "Die besten drei stehen auf dem Podest, alle anderen erstarren fürs Foto.")),
  ])}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Modes and the future", "Modi und Zukunft")}</p>
  <h2>{t("Alone, together, and later", "Allein, gemeinsam und später")}</h2>
  {modes(ctx, [
    (("1 player", "1 Spieler"), ("Solo Heist", "Solo-Raubzug"),
     ("Bank the Great Idol three times against the clock, with fixed beats you can learn. Gold, silver and bronze times.",
      "Sichere das Große Idol dreimal gegen die Uhr, mit festen Takten, die du lernen kannst. Zeiten für Gold, Silber und Bronze.")),
    (("2–8 players", "2–8 Spieler"), ("Party rounds", "Partyrunden"),
     ("Most points wins. Ties go to the most Great Idols banked, then to the fewest catches.",
      "Die meisten Punkte gewinnen. Bei Gleichstand zählen die meisten gesicherten Großen Idole, dann die wenigsten Erwischungen.")),
    (("Into the series", "In die Reihe"), ("Watchers everywhere", "Wächter überall"),
     ("The watcher becomes a stage in Trap Galleries and the Stone Sentries of the flagship; waking the temple becomes a curse in its Trials.",
      "Der Wächter wird zu einer Stufe in Trap Galleries und zu den Steinwächtern der Hauptinsel, das Wecken des Tempels zu einem Fluch in ihren Prüfungen.")),
  ])}
  {back_link(ctx)}
</div></section>
"""


# ------------------------------------------------------------------ game type: The Lost Passages
LP_SCREENS = [
    ("S01", ("The Crack", "Der Spalt"), ("Move, jump, and poke the tripwire before the spear finds you.", "Laufen, springen und den Stolperdraht anstupsen, bevor der Speer dich findet.")),
    ("S02", ("Dart Hall", "Pfeilhalle"), ("Ember Charges, a cracked floor with gold below, and a pressure stone you poke from afar.", "Glutladungen, ein rissiger Boden mit Gold darunter und ein Druckstein, den du aus der Ferne anstupst.")),
    ("S03", ("Guardian Gallery", "Wächtergalerie"), ("The first Risen Guardian, and a crumbling walkway above it.", "Der erste Erweckte Wächter und ein bröckelnder Steg über ihm.")),
    ("S04", ("The Sealed Floor", "Der versiegelte Boden"), ("Read the mural, press the plates in its order: serpent, jaguar, eagle.", "Lies das Wandbild und drück die Platten in seiner Reihenfolge: Schlange, Jaguar, Adler.")),
    ("S05", ("Bat Shaft", "Fledermausschacht"), ("Drop down staggered ledges between two cave bats.", "Über versetzte Simse nach unten, zwischen zwei Höhlenfledermäusen.")),
    ("S06", ("Pendulum Hall", "Pendelhalle"), ("Two blades half a swing apart, and a rope up to the first Big Idol.", "Zwei Klingen, einen halben Schwung versetzt, und ein Seil hinauf zum ersten Großen Idol.")),
    ("S07", ("Fire Vents", "Feuerdüsen"), ("Three vents fire as a wave; ride right behind it.", "Drei Düsen feuern als Welle, lauf direkt hinter ihr her.")),
    ("S08", ("Crusher Chamber", "Stampferkammer"), ("Two crushers on a five-second cycle, and a wall worth blowing open.", "Zwei Stampfer im Fünf-Sekunden-Takt und eine Wand, die sich aufzusprengen lohnt.")),
    ("S09", ("The Long Drop", "Der lange Fall"), ("Big drops down a tall shaft, with darts on the second ledge.", "Große Sprünge einen hohen Schacht hinab, mit Pfeilen auf dem zweiten Sims.")),
    ("S10", ("Boulder Run I", "Felsenflucht I"), ("A plate clicks, a boulder drops. Run, and jump the pit at full speed.", "Eine Platte klickt, ein Felsbrocken fällt. Renn und spring in vollem Lauf über die Grube.")),
    ("S11", ("Boulder Run II", "Felsenflucht II"), ("Duck into the slot and let the boulder smash the wall for you.", "Duck dich in die Nische und lass den Felsbrocken die Wand für dich einschlagen.")),
    ("S12", ("Spear Corridor", "Speergang"), ("Spike strips rise as a wave; a rope leads to the third Big Idol.", "Stachelleisten steigen als Welle, ein Seil führt zum dritten Großen Idol.")),
    ("S13", ("Calendar Lift", "Kalenderaufzug"), ("A faster guardian, then a calendar stone that lifts you up.", "Ein schnellerer Wächter, dann ein Kalenderstein, der dich nach oben trägt.")),
    ("S14", ("The Sun Door", "Die Sonnentür"), ("A crumbling chain you must not stop on, and someone waiting at the door.", "Eine bröckelnde Kette, auf der du nicht stehen bleiben darfst, und jemand, der an der Tür wartet.")),
]


def lost_passages(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Side-view trap platformer", "Fallen-Plattformer in Seitenansicht")),
        (t("Players", "Spieler"), t("1; a duo mode for two is planned", "1; ein Duo-Modus für zwei ist geplant")),
        (t("Level 1", "Level 1"), t("14 screens; 10–15 minutes for a first finish", "14 Bildschirme; 10–15 Minuten bis zum ersten Ziel")),
        (t("Lives", "Leben"), t("5, with a checkpoint on every screen", "5, mit einem Checkpoint auf jedem Bildschirm")),
        (t("Tone", "Stil"), t("No blood: a fall turns you to gold dust", "Kein Blut: Wer stirbt, zerfällt zu Goldstaub")),
    ])
    rows = "".join(f"<tr><th scope='row'>{t(*n)}</th><td>{t(*d)}</td></tr>" for _, n, d in LP_SCREENS)
    shots = [(f"LP1-{k}", t(*n)) for k, n, _ in LP_SCREENS if ctx.has(f"LP1-{k}")]
    gallery = ctx.gallery(shots, cls="gallery-3") if shots else ""
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("A side-on, one-screen-at-a-time trap platformer inside the Sun Temple.",
                        "Ein Fallen-Plattformer in Seitenansicht im Inneren des Sonnentempels, ein Bildschirm nach dem anderen.")}</p>
      <p>{t("The builders never used the grand stair: they had their own way down, hidden inside the walls, and they "
            "trapped every inch of it. You found the crack. K'in found you. Every screen is a trap puzzle: spears from "
            "the ceiling, darts, crushers, pendulums, and a boulder that wants you flat. One touch and you're dust. "
            "Learn the screen, beat it on the next try, and keep your lives for the screens that matter.",
            "Die Erbauer benutzten nie die große Treppe: Sie hatten ihren eigenen Weg nach unten, versteckt in den Wänden, "
            "und jeden Zentimeter davon mit Fallen gesichert. Du hast den Spalt gefunden. K'in hat dich gefunden. Jeder "
            "Bildschirm ist ein Fallenrätsel: Speere aus der Decke, Pfeile, Stampfer, Pendel und ein Felsbrocken, der dich "
            "platt machen will. Eine Berührung, und du bist Staub. Lern den Bildschirm, schaff ihn beim nächsten Versuch und "
            "heb dir deine Leben für die Bildschirme auf, auf die es ankommt.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, ctx.pick("LP1-S01", "T2E-SCENE"), t("How it plays", "So wird gespielt"), t("One screen, one puzzle", "Ein Bildschirm, ein Rätsel"),
    t("<p>A fixed camera shows one screen at a time and cuts to the next when you cross the edge. Every trap is fully "
      "in view before you commit, so the second try feels clever, not lucky.</p><p>Treasure and three hidden Big "
      "Idols pull good players off the safe path.</p>",
      "<p>Eine feste Kamera zeigt jeweils einen Bildschirm und schneidet zum nächsten, sobald du den Rand überquerst. "
      "Jede Falle ist ganz zu sehen, bevor du dich festlegst, also fühlt sich der zweite Versuch klug an, nicht wie "
      "Glück.</p><p>Schätze und drei versteckte Große Idole locken gute Spieler vom sicheren Weg.</p>"))}
  {feature(ctx, ctx.pick("LP1-S10", "P21"), t("The toolkit", "Die Ausrüstung"), t("Handle the traps, don't just dodge them", "Fallen bedienen, nicht nur ausweichen"),
    t("<p><strong>Staff poke:</strong> trips wires and pressure stones from a safe distance and staggers guardians. "
      "<strong>Ember Charges:</strong> break cracked blocks and stun enemies, but step away from the hiss. "
      "<strong>Ropes:</strong> unroll from bronze anchors to reach secret ledges.</p><p>The main path never needs a "
      "rope or a charge. They are for treasure, so using them is greed, never a dead end.</p>",
      "<p><strong>Stabstoß:</strong> löst Drähte und Drucksteine aus sicherer Entfernung aus und bringt Wächter ins "
      "Taumeln. <strong>Glutladungen:</strong> sprengen rissige Blöcke und betäuben Gegner, aber geh weg, wenn es "
      "zischt. <strong>Seile:</strong> rollen sich an Bronzeankern ab und führen zu geheimen Simsen.</p><p>Der "
      "Hauptweg braucht nie ein Seil oder eine Ladung. Sie sind für Schätze da, also sind sie Gier, nie eine Sackgasse.</p>"),
    flip=True)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Level 1", "Level 1")}</p>
  <h2>{t("The Builders' Way Down", "Der Weg der Erbauer nach unten")}</h2>
  <p class="lede-sm">{t("Fourteen screens in a zig-zag down through the pyramid's wall, then a lift up to the hidden Sun Door. "
                        "Four Sun Gates save your progress along the way.",
                        "Vierzehn Bildschirme im Zickzack durch die Wand der Pyramide nach unten, dann ein Aufzug hinauf zur "
                        "verborgenen Sonnentür. Vier Sonnentore sichern unterwegs deinen Fortschritt.")}</p>
  {gallery}
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Screen", "Bildschirm")}</th><th>{t("What it teaches", "Was er lehrt")}</th></tr></thead>
    <tbody>{rows}</tbody>
  </table></div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Fair on the second try", "Fair beim zweiten Versuch")}</p>
  <h2>{t("K'in keeps it fair", "K'in sorgt für Fairness")}</h2>
  {loops(ctx, [
    (("Warns once", "Warnt einmal"), ("The first time you near a trap, K'in flies to it, glows and says one line. Never twice.",
                                      "Wenn du einer Falle zum ersten Mal nahe kommst, fliegt K'in hin, leuchtet und sagt einen Satz. Nie zweimal.")),
    (("Shows what got you", "Zeigt, was dich erwischt hat"), ("After a death, the thing that killed you glows for three seconds, with a hint.",
                                                             "Nach einem Tod leuchtet drei Sekunden lang, was dich erwischt hat, mit einem Hinweis.")),
    (("Draws the way", "Zeigt den Weg"), ("After three deaths on one screen, she offers to show the builders' path.",
                                         "Nach drei Toden auf einem Bildschirm bietet sie an, den Weg der Erbauer zu zeigen.")),
    (("Carries you", "Trägt dich"), ("After six, she can carry you to the next screen, for a price in points.",
                                     "Nach sechs kann sie dich zum nächsten Bildschirm tragen, gegen Punkte.")),
  ])}
</div></section>

<section class="wrap section">
  {feature(ctx, ctx.pick("LP1-S14", "CS-KAYA"), t("The rival", "Die Rivalin"), t("Kaya got here first", "Kaya war zuerst da"),
    t("<p>A scratched note on the first wall says she was here. At the Sun Door, Kaya's golden Echo waits with folded "
      "arms: <em>“You took the trapped way down? I took the stairs.”</em></p><p>Later, her Echo runs the level at par "
      "time, and beating her is what gold means.</p>",
      "<p>Eine eingeritzte Notiz an der ersten Wand verrät, dass sie hier war. An der Sonnentür wartet Kayas goldenes "
      "Echo mit verschränkten Armen: <em>„Du hast den Weg mit den Fallen genommen? Ich die Treppe.“</em></p><p>Später "
      "läuft ihr Echo das Level in Richtzeit, und sie zu schlagen heißt Gold.</p>"))}
  {modes(ctx, [
    (("After the first finish", "Nach dem ersten Ziel"), ("Classic mode", "Klassischer Modus"),
     ("No Sun Gates, three lives, no skip. Game over means the whole level again.",
      "Keine Sonnentore, drei Leben, kein Überspringen. Game over heißt: das ganze Level von vorn.")),
    (("Coming next", "Als Nächstes"), ("Levels 2 and 3", "Level 2 und 3"),
     ("The Drowned Cisterns, with water as a timer, and the Shifting Vault, whose walls move between your deaths.",
      "Die ertrunkenen Zisternen, mit Wasser als Zeitgeber, und das wandernde Gewölbe, dessen Wände sich zwischen deinen Toden verschieben.")),
    (("Into the series", "In die Reihe"), ("Side passages", "Seitengänge"),
     ("The same traps with the same timings appear in Trap Galleries, and in the flagship a cracked wall can open into a side-view passage.",
      "Dieselben Fallen mit denselben Timings tauchen in Trap Galleries auf, und auf der Hauptinsel kann eine rissige Wand in einen Gang in Seitenansicht führen.")),
  ])}
  {back_link(ctx)}
</section>
"""


# ------------------------------------------------------------------ game type: Trap Architects
def trap_architects(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Build-and-run party game, obby", "Bau-und-Lauf-Partyspiel, Obby")),
        (t("Players", "Spieler"), t("2–8; alone: a timed trial and a workshop", "2–8; allein: ein Zeitrennen und eine Werkstatt")),
        (t("Round", "Runde"), t("60 s to build, 150 s to run; a match is 3 rounds", "60 s bauen, 150 s laufen; ein Match hat 3 Runden")),
        (t("Map", "Karte"), t("The Architects' Gallery: eight sections in a U", "Die Galerie der Architekten: acht Abschnitte in U-Form")),
        (t("Tone", "Stil"), t("No damage between players; a trap only sends you back", "Kein Schaden zwischen Spielern; eine Falle schickt dich nur zurück")),
    ])
    palette = [
        (("Spike strip", "Stachelleiste"), "2", ("Red-tipped slots, a click before they rise", "Rot gespitzte Schlitze, ein Klicken, bevor sie steigen")),
        (("Fire vent", "Feuerdüse"), "2", ("A soot ring and a puff of smoke", "Ein Rußring und ein Rauchstoß")),
        (("Crumble tile", "Bröckelplatte"), "2", ("Hairline cracks; it falls once you step on it", "Haarrisse; sie fällt, sobald du draufsteigst")),
        (("Fake floor", "Trugboden"), "3", ("A slightly lighter glyph that doesn't glow on the drumbeat", "Eine etwas hellere Glyphe, die beim Trommelschlag nicht leuchtet")),
        (("Boulder plate", "Felsplatte"), "3", ("A raised plate and a rope over the exit arch", "Eine erhöhte Platte und ein Seil über dem Ausgangsbogen")),
        (("Dart wall", "Pfeilwand"), "3", ("Dart holes, and a click before each volley", "Pfeillöcher und ein Klicken vor jeder Salve")),
        (("Swinging blade", "Pendelklinge"), "3", ("Always in view, always swinging", "Immer zu sehen, immer in Bewegung")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("The temple's builders were trap makers. Now you are.", "Die Erbauer des Tempels waren Fallenbauer. Jetzt bist du einer.")}</p>
      <p>{t("Every round, each player gets one section of a temple corridor and sixty seconds to fill its trap slots. "
            "Then everyone runs the whole chained gauntlet, their own section included. Score for getting through, "
            "score for catching your friends, and get a bonus for building something hard and fair.",
            "Jede Runde bekommt jeder Spieler einen Abschnitt eines Tempelgangs und sechzig Sekunden, um seine Fallenplätze "
            "zu füllen. Dann laufen alle durch den ganzen verketteten Parcours, den eigenen Abschnitt eingeschlossen. Punkte "
            "fürs Durchkommen, Punkte fürs Erwischen deiner Freunde und ein Bonus für etwas, das schwer und fair ist.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("A round", "Eine Runde")}</p>
  <h2>{t("Build, then run what everyone built", "Bauen, dann durch alles laufen, was alle gebaut haben")}</h2>
  {loops(ctx, [
    (("Build · 60 s", "Bauen · 60 s"), ("Walk to a slot and press interact to cycle through traps. They work while you build, so you test them on yourself.",
                                         "Geh zu einem Platz und drück Interagieren, um durch die Fallen zu schalten. Sie funktionieren schon beim Bauen, also testest du sie an dir selbst.")),
    (("Lock · 6 s", "Sperren · 6 s"), ("The temple tunes the timings so every lane can be cleared, and fills any empty lane.",
                                       "Der Tempel stimmt die Timings so ab, dass jede Bahn schaffbar ist, und füllt leere Bahnen auf.")),
    (("Run · 150 s", "Laufen · 150 s"), ("Run all eight sections in order. Caught? Back to that section's start.",
                                         "Lauf alle acht Abschnitte der Reihe nach. Erwischt? Zurück an den Anfang dieses Abschnitts.")),
    (("Results", "Ergebnis"), ("Round scores, the podium, and the most feared trap: “Lena's Fake Floor, five catches.”",
                               "Rundenpunkte, das Podest und die gefürchtetste Falle: „Lenas Trugboden, fünf Erwischte.“")),
  ])}
  {shots(ctx, [("TA-SCENE1", ("Build: sixty seconds to set the traps", "Bauen: sechzig Sekunden für die Fallen")),
                ("TA-SCENE2", ("Run: caught by a friend's fake floor", "Laufen: erwischt vom Trugboden eines Freundes")),
                ("TA-MAP", ("The Architects' Gallery", "Die Galerie der Architekten"))])}
</div></section>

<section class="wrap section">
  {feature(ctx, ctx.pick("ISL-TA", "T2C-SCENE"), t("The palette", "Die Auswahl"), t("Seven traps, and every one has a tell", "Sieben Fallen, und jede verrät sich"),
    t("<p>Each section has six floor slots in three rows and two strips between them. A budget of 10 points grows to "
      "14 over a match, so later rounds get nastier.</p>",
      "<p>Jeder Abschnitt hat sechs Bodenplätze in drei Reihen und zwei Streifen dazwischen. Ein Budget von 10 Punkten "
      "wächst im Lauf eines Matches auf 14, also werden spätere Runden gemeiner.</p>"))}
  {table(ctx, [("Trap", "Falle"), ("Cost", "Kosten"), ("How you spot it", "Woran du sie erkennst")], palette)}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("The fairness engine", "Die Fairness-Maschine")}</p>
  <h2>{t("Hard is allowed. Impossible is not.", "Schwer ist erlaubt. Unmöglich nicht.")}</h2>
  {modes(ctx, [
    (("Rule 1", "Regel 1"), ("One trick per row", "Ein Trick pro Reihe"),
     ("Crumble tiles, fake floors and boulder plates are tricks. Each row holds at most one, so every row has an honest half.",
      "Bröckelplatten, Trugböden und Felsplatten sind Tricks. Jede Reihe hat höchstens einen, also hat jede Reihe eine ehrliche Hälfte.")),
    (("Rule 2", "Regel 2"), ("Never both halves at once", "Nie beide Hälften gleichzeitig"),
     ("When two timed traps share a row, the temple shifts one so they are never dangerous together.",
      "Wenn zwei Zeitfallen eine Reihe teilen, verschiebt der Tempel eine, damit sie nie gleichzeitig gefährlich sind.")),
    (("Rule 3", "Regel 3"), ("You run your own lane", "Du läufst deine eigene Bahn"),
     ("Your traps catch you too. So you build a puzzle with a trick in it, not a wall.",
      "Deine Fallen erwischen auch dich. Also baust du ein Rätsel mit einem Trick, keine Wand.")),
  ])}
  <p class="lede-sm">{t("The bonus called Fair and Fierce pays a lane that caught someone and was still cleared by half the runners.",
                        "Der Bonus „Fair und Fies“ belohnt eine Bahn, die jemanden erwischt hat und trotzdem von der Hälfte der Läufer geschafft wurde.")}</p>
</div></section>

<section class="wrap section">
  {modes(ctx, [
    (("1 player", "1 Spieler"), ("Temple Trial", "Tempelprüfung"),
     ("Run eight hand-made temple lanes against the clock for gold, silver or bronze.",
      "Lauf acht von Hand gebaute Tempelbahnen gegen die Uhr, für Gold, Silber oder Bronze.")),
    (("1 player", "1 Spieler"), ("Workshop", "Werkstatt"),
     ("Build your signature lane and save it. It fills empty sections on other players' servers: “Built by Tomas, last Tuesday.”",
      "Bau deine Signaturbahn und speichere sie. Sie füllt leere Abschnitte auf den Servern anderer Spieler: „Gebaut von Tomas, letzten Dienstag.“")),
    (("Into the series", "In die Reihe"), ("Keeper mode", "Keeper-Modus"),
     ("Its fairness rules become the anti-grief rules of a Keeper mode in Trap Galleries, where one player fires the traps live.",
      "Ihre Fairness-Regeln werden zu den Anti-Grief-Regeln eines Keeper-Modus in Trap Galleries, in dem ein Spieler die Fallen live auslöst.")),
  ])}
  {back_link(ctx)}
</section>
"""


# ------------------------------------------------------------------ game type: Calendar Fall
def calendar_fall(ctx):
    u, t = ctx.url, ctx.t
    card = facts([
        (t("Genre", "Genre"), t("Party knockout, last one standing", "Party-Knockout, der Letzte gewinnt")),
        (t("Players", "Spieler"), t("2–16; alone: a survival time trial", "2–16; allein: ein Überlebens-Zeitrennen")),
        (t("Round", "Runde"), t("Under 4 minutes, usually about 3", "Unter 4 Minuten, meist etwa 3")),
        (t("Map", "Karte"), t("The Counting Well: three calendar wheels over a sacred well", "Der zählende Brunnen: drei Kalenderräder über einem heiligen Brunnen")),
        (t("Tone", "Stil"), t("No weapons; touch the well and you're out for the round", "Keine Waffen; wer den Brunnen berührt, ist für die Runde raus")),
    ])
    signs = [
        ("Ajaw", ("Sun", "Sonne"), ("Gold", "Gold"), ("Sun disc with four rays", "Sonnenscheibe mit vier Strahlen"), ("Bronze gong", "Bronzegong")),
        ("Imix", ("Water", "Wasser"), ("Blue", "Blau"), ("Three waves", "Drei Wellen"), ("Water drum", "Wassertrommel")),
        ("K'ak'", ("Fire", "Feuer"), ("Red", "Rot"), ("Flame", "Flamme"), ("Gourd rattle", "Kürbisrassel")),
        ("K'an", ("Maize, growth", "Mais, Wachstum"), ("Green", "Grün"), ("Maize cob", "Maiskolben"), ("Clay flute", "Tonflöte")),
        ("Ik'", ("Wind", "Wind"), ("White", "Weiß"), ("Spiral", "Spirale"), ("Conch horn", "Muschelhorn")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("The floor is a giant Mayan calendar, and the temple is counting the days.",
                        "Der Boden ist ein riesiger Maya-Kalender, und der Tempel zählt die Tage.")}</p>
      <p>{t("K'in calls a day sign. Every stone carved with that sign shakes, then drops. The stone wheels click round "
            "under your feet, three floors stacked over a sacred well. Read the glyph, find a safe stone, stay up. Last "
            "Climber standing wins the day. K'in will call them. She is sorry in advance.",
            "K'in ruft ein Tageszeichen. Jeder Stein, in den dieses Zeichen gemeißelt ist, bebt und fällt dann. Die "
            "Steinräder drehen sich unter deinen Füßen weiter, drei Ebenen übereinander über einem heiligen Brunnen. Lies "
            "die Glyphe, finde einen sicheren Stein, bleib oben. Wer als letzter Kletterer steht, gewinnt den Tag. K'in "
            "wird die Zeichen rufen. Es tut ihr jetzt schon leid.")}</p>
    </div>
    {card}
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Five day signs", "Fünf Tageszeichen")}</p>
  <h2>{t("A colour, a shape and a sound for every sign", "Eine Farbe, eine Form und ein Klang für jedes Zeichen")}</h2>
  <p class="lede-sm">{t("Four are real day signs of the Maya calendar; K'ak', the Maya word for fire, is the fifth. Each "
                        "glyph is carved deep enough to read as a shape even without colour.",
                        "Vier sind echte Tageszeichen des Maya-Kalenders, K'ak', das Maya-Wort für Feuer, ist das fünfte. "
                        "Jede Glyphe ist tief genug gemeißelt, um auch ohne Farbe als Form lesbar zu sein.")}</p>
  {table(ctx, [("Sign", "Zeichen"), ("Meaning", "Bedeutung"), ("Colour", "Farbe"), ("Shape", "Form"), ("Call", "Ruf")], signs)}
</div></section>

<section class="wrap section">
  {feature(ctx, ctx.pick("ISL-CF", "T3B-SCENE"), t("A call", "Ein Ruf"), t("Read it, then move", "Lesen, dann laufen"),
    t("<p>The wheels click one step. K'in names a sign, its glyph lights up on the walls, and every stone that wears it "
      "glows and shakes. Then it drops, and whoever stood on it falls.</p><p>Falling a floor is not the end: you land "
      "on the wheel below, with one floor less between you and the well. Only the water puts you out.</p>",
      "<p>Die Räder rücken einen Schritt weiter. K'in nennt ein Zeichen, seine Glyphe leuchtet an den Wänden auf, und "
      "jeder Stein, der es trägt, glüht und bebt. Dann fällt er, und wer darauf stand, stürzt.</p><p>Eine Ebene tiefer "
      "zu fallen ist nicht das Ende: Du landest auf dem Rad darunter, mit einer Ebene weniger zwischen dir und dem "
      "Brunnen. Nur das Wasser wirft dich raus.</p>"))}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("A round", "Eine Runde")}</p>
  <h2>{t("From dawn to eclipse", "Von der Morgendämmerung bis zur Finsternis")}</h2>
  {loops(ctx, [
    (("Dawn", "Morgendämmerung"), ("One sign per call, slow, with a long warning.", "Ein Zeichen pro Ruf, langsam, mit langer Warnung.")),
    (("Midday", "Mittag"), ("The outer wheels start to turn, and every third call names two signs.",
                            "Die äußeren Räder beginnen sich zu drehen, und jeder dritte Ruf nennt zwei Zeichen.")),
    (("Afternoon", "Nachmittag"), ("Two signs every call, and the wheels sometimes reverse.",
                                   "Zwei Zeichen bei jedem Ruf, und die Räder drehen manchmal um.")),
    (("Eclipse", "Finsternis"), ("K'in now calls what stays, not what falls: “Only Ajaw holds.” The top floors stop coming back.",
                                 "K'in ruft jetzt, was bleibt, nicht was fällt: „Nur Ajaw hält.“ Die oberen Ebenen kommen nicht mehr zurück.")),
  ])}
  {shots(ctx, [("CF-SCENE1", ("A call: the called stones drop", "Ein Ruf: die gerufenen Steine fallen")),
                ("CF-SCENE2", ("Eclipse: only one sign holds", "Finsternis: nur ein Zeichen hält")),
                ("CF-MAP", ("The Counting Well", "Der zählende Brunnen"))])}
</div></section>

<section class="wrap section">
  {modes(ctx, [
    (("A second chance", "Eine zweite Chance"), ("K'in's Feather", "K'ins Feder"),
     ("Every 30 seconds a golden feather appears. Hold it, and the next time you touch the well K'in catches you instead.",
      "Alle 30 Sekunden erscheint eine goldene Feder. Wer sie hält, wird beim nächsten Kontakt mit dem Brunnen von K'in aufgefangen.")),
    (("Out, not bored", "Raus, aber nicht gelangweilt"), ("The drum gallery", "Die Trommelgalerie"),
     ("Players who are out drum for a sign from the rim and nudge which one K'in calls next.",
      "Wer raus ist, trommelt vom Rand für ein Zeichen und beeinflusst, welches K'in als Nächstes ruft.")),
    (("1 player", "1 Spieler"), ("Solo Survival", "Solo-Überleben"),
     ("The same calls in the same order for everyone each update. Survive as long as you can.",
      "Für alle dieselben Rufe in derselben Reihenfolge, bis zum nächsten Update. Überlebe so lange wie möglich.")),
    (("Into the series", "In die Reihe"), ("The Disc Well", "Der Scheibenbrunnen"),
     (f"The wheels come from the flagship's Disc Well in <a href='{u('climb/tier-3.html')}'>Tier III</a>, and the five signs become the glyph language of its puzzles.",
      f"Die Räder stammen aus dem Scheibenbrunnen der Hauptinsel in <a href='{u('climb/tier-3.html')}'>Stufe III</a>, und die fünf Zeichen werden zur Glyphensprache ihrer Rätsel.")),
  ])}
  {back_link(ctx)}
</section>
"""


PAGES = {
    "islands/index.html": dict(
        title=("Game Types", "Spieltypen"), kicker=("Mayan Temple Adventures", "Mayan Temple Adventures"),
        banner=["ISL-ALL", "KEYART"],
        lede=("One temple, " + COUNT[len(ISLANDS)][0] + " game types, all built from the same rooms, traps and characters.",
              "Ein Tempel, " + COUNT[len(ISLANDS)][1] + " Spieltypen, alle aus denselben Räumen, Fallen und Figuren gebaut."),
        description=("The " + COUNT[len(ISLANDS)][0] + " Fortnite game types of Mayan Temple Adventures, and the order they are built in.",
                     "Die " + COUNT[len(ISLANDS)][1] + " Fortnite-Spieltypen von Mayan Temple Adventures und die Reihenfolge, in der sie entstehen."),
        body=overview, og=["ISL-ALL", "KEYART"]),
    "islands/trap-galleries.html": dict(
        title=("Trap Galleries: 18 Floors", "Trap Galleries: 18 Floors"), kicker=("Game type · Deathrun", "Spieltyp · Deathrun"),
        banner=["THUMB-TRAPS", "ISL-TRAPS", "T2A-SCENE"], banner_full=True,
        lede=("Eighteen trap stages up the inside of the temple. No enemies, no weapons, just timing.",
              "Achtzehn Fallenstufen im Inneren des Tempels hinauf. Keine Gegner, keine Waffen, nur Timing."),
        description=("A deathrun through the Sun Temple's traps for 1–16 players.",
                     "Ein Deathrun durch die Fallen des Sonnentempels für 1–16 Spieler."),
        body=trap_galleries, og=["THUMB-TRAPS", "ISL-TRAPS", "T2A-SCENE"]),
    "islands/ascent.html": dict(
        title=("Ascent of the Sun Temple", "Ascent of the Sun Temple"),
        kicker=("Game type · The flagship", "Spieltyp · Die Hauptinsel"),
        banner=["THUMB-ASCENT", "ISL-ASCENT", "KEYART"], banner_full=True,
        lede=("The whole climb, for up to four friends: the Shell, seventeen floors and the Sky Altar.",
              "Der ganze Aufstieg, für bis zu vier Freunde: The Shell, siebzehn Ebenen und der Himmelsaltar."),
        description=("The co-op flagship, from the prologue with Kaya to the Sky Altar.",
                     "Die Koop-Hauptinsel, vom Prolog mit Kaya bis zum Himmelsaltar."),
        body=ascent, og=["THUMB-ASCENT", "ISL-ASCENT", "KEYART"]),
    "islands/sun-temple-dig.html": dict(
        title=("Sun Temple Dig", "Sun Temple Dig"), kicker=("Game type · Tycoon", "Spieltyp · Tycoon"),
        banner=["THUMB-DIG", "ISL-DIG", "A-04"], banner_full=True,
        lede=("Restore Isabel Kaan's abandoned camp, plot by plot, and dive into the temple for the rare finds.",
              "Bau Isabel Kaans verlassenes Lager Parzelle für Parzelle wieder auf und tauch in den Tempel, um seltene Funde zu bergen."),
        description=("A tycoon at the foot of the pyramid, with short dives into real temple rooms.",
                     "Ein Tycoon am Fuß der Pyramide, mit kurzen Tauchgängen in echte Tempelräume."),
        body=sun_temple_dig, og=["THUMB-DIG", "ISL-DIG", "A-04"]),
    "islands/illusion-depths.html": dict(
        title=("Illusion Depths", "Illusion Depths"), kicker=("Game type · Co-op escape rooms", "Spieltyp · Koop-Escape-Rooms"),
        banner=["THUMB-DEPTHS", "ISL-DEPTHS", "T5A-SCENE"], banner_full=True,
        lede=("Five puzzle chambers where one player can see what the others must do.",
              "Fünf Rätselkammern, in denen ein Spieler sieht, was die anderen tun müssen."),
        description=("Co-op escape rooms recut from the temple's puzzle halls.",
                     "Koop-Escape-Rooms, umgebaut aus den Rätselhallen des Tempels."),
        body=illusion_depths, og=["THUMB-DEPTHS", "ISL-DEPTHS", "T5A-SCENE"]),
    "islands/orb-raiders.html": dict(
        title=("Orb Raiders", "Orb Raiders"), kicker=("Game type · PvPvE", "Spieltyp · PvPvE"),
        banner=["THUMB-RAIDERS", "ISL-RAIDERS", "T4E-SCENE"], banner_full=True,
        lede=("Raid the elemental sanctums for relics and orbs, then make it to a Sun Portal before the temple seals.",
              "Plündere die Elementarheiligtümer nach Relikten und Kugeln und erreich ein Sonnenportal, bevor der Tempel sich versiegelt."),
        description=("A light extraction raid on the four elemental sanctums.",
                     "Ein leichter Extraction-Raid durch die vier Elementarheiligtümer."),
        body=orb_raiders, og=["THUMB-RAIDERS", "ISL-RAIDERS", "T4E-SCENE"]),
    "islands/hold-your-breath.html": dict(
        title=("Hold Your Breath", "Hold Your Breath"), kicker=("Game type · Party heist", "Spieltyp · Party-Raubzug"),
        banner=["THUMB-HYB", "ISL-HYB", "HYB-SCENE1"], banner_full=True,
        lede=("Steal the temple's idols, and freeze whenever its stone eyes open.",
              "Stiehl die Idole des Tempels und erstarre, sobald seine Steinaugen sich öffnen."),
        description=("A freeze-and-steal party heist for 1–8 players inside the living Sun Temple.",
                     "Ein Party-Raubzug zum Erstarren und Stehlen für 1–8 Spieler im lebenden Sonnentempel."),
        body=hold_your_breath, og=["THUMB-HYB", "ISL-HYB", "HYB-SCENE1"]),
    "islands/lost-passages.html": dict(
        title=("The Lost Passages", "The Lost Passages"), kicker=("Game type · Trap platformer", "Spieltyp · Fallen-Plattformer"),
        banner=["THUMB-LP", "ISL-LP", "LP1-S10", "T2E-SCENE"], banner_full=True,
        lede=("The builders' hidden way down through the temple walls, one trap-filled screen at a time.",
              "Der verborgene Weg der Erbauer durch die Tempelwände nach unten, ein Fallenbildschirm nach dem anderen."),
        description=("A single-player side-view trap platformer through the Sun Temple's hidden passages.",
                     "Ein Fallen-Plattformer in Seitenansicht für einen Spieler durch die verborgenen Gänge des Sonnentempels."),
        body=lost_passages, og=["THUMB-LP", "ISL-LP", "LP1-S10", "T2E-SCENE"]),
    "islands/trap-architects.html": dict(
        title=("Trap Architects", "Trap Architects"), kicker=("Game type · Build and run", "Spieltyp · Bauen und laufen"),
        banner=["THUMB-TA", "ISL-TA", "T2C-SCENE"], banner_full=True,
        lede=("Build a trap section in sixty seconds, then run everyone else's.",
              "Bau in sechzig Sekunden einen Fallenabschnitt und lauf dann durch die aller anderen."),
        description=("A build-and-run party game for 2–8 players, with a fairness engine that keeps every lane beatable.",
                     "Ein Bau-und-Lauf-Partyspiel für 2–8 Spieler, mit einer Fairness-Maschine, die jede Bahn schaffbar hält."),
        body=trap_architects, og=["THUMB-TA", "ISL-TA", "T2C-SCENE"]),
    "islands/calendar-fall.html": dict(
        title=("Calendar Fall", "Calendar Fall"), kicker=("Game type · Party knockout", "Spieltyp · Party-Knockout"),
        banner=["THUMB-CF", "ISL-CF", "T3B-SCENE"], banner_full=True,
        lede=("K'in calls a day sign, and every stone that wears it falls.",
              "K'in ruft ein Tageszeichen, und jeder Stein, der es trägt, fällt."),
        description=("A last-one-standing knockout for 2–16 players on three turning calendar wheels.",
                     "Ein Knockout für 2–16 Spieler auf drei drehenden Kalenderrädern, bei dem der Letzte gewinnt."),
        body=calendar_fall, og=["THUMB-CF", "ISL-CF", "T3B-SCENE"]),
}
