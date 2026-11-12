"""The Game tab: Overview & Pillars, How It Plays, The Return, Reading the Temple, Weapons & Powers (English and German)."""
from components import feature


RETURN_ART = [("ACT-TEA", ("Tea with Oxlahun", "Tee mit Oxlahun")),
              ("ACT-SATCHEL", ("Too much in the satchel", "Zu viel in der Tasche")),
              ("ACT-WAYSTALL", ("A Waystall", "Ein Wegstand"))]
READING_ART = [("ACT-RUBBING", ("Taking a rubbing", "Eine Abreibung nehmen")),
               ("F6-BENCH", ("The workbench on Floor 6", "Die Werkbank auf Ebene 6"))]
WEAPON_ART = [("ACT-W09", ("The Surveyor's Staff", "Der Stab des Landvermessers")),
              ("ACT-W10", ("Lisbet's Rope", "Lisbets Seil")),
              ("ACT-W11", ("Joaquin's Lantern", "Joaquins Laterne"))]


def art_row(ctx, items):
    """A row of extra images; each appears once it has been uploaded."""
    shots = [(i, ctx.t(*c)) for i, c in items if ctx.has(i)]
    return f'<div style="margin-top:32px">{ctx.gallery(shots, cls="gallery-3")}</div>' if shots else ""


def modes(rows):
    return '<div class="modes">' + "".join(
        f'<article class="mode"><p class="kicker">{k}</p><h3>{n}</h3><p>{d}</p></article>' for k, n, d in rows) + "</div>"


def steps(rows, grid=True):
    cls = "loops loops-grid" if grid else "loops"
    return f'<ol class="{cls}">' + "".join(f'<li><span class="loop-label">{n}</span><p>{d}</p></li>' for n, d in rows) + "</ol>"


def table(head, rows):
    th = "".join(f"<th>{h}</th>" for h in head)
    body = "".join("<tr>" + "".join((f"<th scope='row'>{c}</th>" if i == 0 else f"<td>{c}</td>") for i, c in enumerate(r)) + "</tr>"
                   for r in rows)
    return f'<div class="table-wrap"><table class="orb-table"><thead><tr>{th}</tr></thead><tbody>{body}</tbody></table></div>'


# ------------------------------------------------------------------ overview
def overview(ctx):
    u, t = ctx.url, ctx.t
    pillars = [
        ("01", t("Read", "Lesen"),
         t("Kaya is a scholar, and she wins by understanding. Her goggles read enemies, traps, floors and walls, and what she learns is the one thing death can't take.",
           "Kaya ist Gelehrte, und sie gewinnt, indem sie versteht. Ihre Brille liest Gegner, Fallen, Böden und Wände, und was sie lernt, ist das Einzige, was ihr der Tod nicht nehmen kann.")),
        ("02", t("Fight", "Kämpfen"),
         t("Most chambers are fights: cursed priests, awakened creatures, stone that charges. Traps hurt everyone, so a good reader turns the temple's defences on its own guards.",
           "Die meisten Kammern sind Kämpfe: verfluchte Priester, erwachte Kreaturen, Stein, der angreift. Fallen treffen alle, also richtet eine gute Leserin die Verteidigung des Tempels gegen seine eigenen Wächter.")),
        ("03", t("Ascend", "Aufsteigen"),
         t("Twenty-seven floors up one pyramid, from flooded foundations to open sky. The summit is in view from the first minute.",
           "Siebenundzwanzig Ebenen eine Pyramide hinauf, von überfluteten Fundamenten bis unter den freien Himmel. Der Gipfel ist von der ersten Minute an zu sehen.")),
        ("04", t("Return", "Zurückkehren"),
         t("Death moves the story. Every return brings a new line, a new carving, a sale, a reading, something earned. You always come back with more than you left with.",
           "Der Tod treibt die Geschichte voran. Jede Rückkehr bringt einen neuen Satz, ein neues Relief, einen Verkauf, eine Lesart, etwas Verdientes. Du kommst immer mit mehr zurück, als du mitgenommen hast.")),
        ("05", t("Never alone, never sure", "Nie allein, nie sicher"),
         t("K'in guides and warns, and she also edits the record. Oxlahun helps, and he also profits. Everyone is kind to you. Check it anyway.",
           "K'in führt und warnt, und sie redigiert auch die Überlieferung. Oxlahun hilft, und er verdient auch daran. Alle sind freundlich zu dir. Prüf es trotzdem nach.")),
    ]
    pillar_html = "".join(f'<li><span class="num">{n}</span><div><h3>{nm}</h3><p>{d}</p></div></li>' for n, nm, d in pillars)

    facts = [
        (t("Genre", "Genre"), t("Single-player third-person action roguelite with platforming and puzzles",
                                "Third-Person-Action-Roguelite für einen Spieler, mit Plattforming und Rätseln")),
        (t("Engine", "Engine"), t("Unreal Engine 5", "Unreal Engine 5")),
        (t("You play", "Du spielst"), t("Kaya, a 23-year-old scholar looking for her mother", "Kaya, eine 23-jährige Gelehrte auf der Suche nach ihrer Mutter")),
        (t("Inspirations", "Vorbilder"), t("Ratchet &amp; Clank and Jak &amp; Daxter for tone; Hades for the loop of dying and returning",
                                          "Ratchet &amp; Clank und Jak &amp; Daxter für den Stil; Hades für den Kreislauf aus Sterben und Zurückkehren")),
        (t("The climb", "Der Aufstieg"), t("27 floors in six tiers, from the Shell to the Sky Altar", "27 Ebenen in sechs Stufen, von The Shell bis zum Himmelsaltar")),
        (t("A run", "Ein Durchlauf"), t("25 to 45 minutes", "25 bis 45 Minuten")),
    ]
    fact_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)
    q1, q2 = t("“", "„"), t("”", "“")
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Kaya is a scholar, not a warrior. She climbs a living Mayan pyramid to prove her missing mother right, and it kills her. Every time.",
                        "Kaya ist Gelehrte, keine Kriegerin. Sie erklimmt eine lebende Maya-Pyramide, um zu beweisen, dass ihre verschwundene Mutter recht hatte, und die Pyramide tötet sie. Jedes Mal.")}</p>
      <p>{t("She wakes on the stone floor of the Threshold with her notebook dry and her memories intact, pours tea with the trader who profits from her "
            "dying, sells what she carried out, reads what she copied, and goes back up knowing more. The temple takes her gold. It never takes her notes.",
            "Sie erwacht auf dem Steinboden der Schwelle, das Notizbuch trocken und die Erinnerung unversehrt, trinkt Tee mit dem Händler, der an ihrem Sterben "
            "verdient, verkauft, was sie herausgetragen hat, liest, was sie abgeschrieben hat, und steigt mit mehr Wissen wieder hinauf. Der Tempel nimmt ihr Gold. Ihre Notizen nimmt er nie.")}</p>
      <p>{t(f"The story explains the structure. The temple <em>{q1}rearranges itself to trap greedy adventurers{q2}</em>, so shuffled chambers belong to the "
            f"world rather than to a menu. And <em>{q1}the cycle begins again… unless you break it{q2}</em>: every death pulls Kaya back to the Threshold, and "
            f"that is where the real game happens. <a href='{u('game/the-return.html')}'>The Return</a>",
            f"Die Geschichte erklärt die Struktur. Der Tempel <em>{q1}ordnet sich neu, um gierige Abenteurer in die Falle zu locken{q2}</em>, also gehören wechselnde "
            f"Kammern zur Welt und nicht zu einem Menü. Und <em>{q1}der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn{q2}</em>: Jeder Tod zieht Kaya "
            f"zurück an die Schwelle, und genau dort spielt das eigentliche Spiel. <a href='{u('game/the-return.html')}'>Die Rückkehr</a>")}</p>
    </div>
    <dl class="facts">{fact_html}</dl>
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Design pillars", "Design-Säulen")}</p>
  <h2>{t("Five ideas every room has to serve", "Fünf Ideen, denen jeder Raum dienen muss")}</h2>
  <ol class="pillar-list">{pillar_html}</ol>
</div></section>

<section class="wrap section">
  {feature(ctx, "A-04", t("First steps", "Erste Schritte"), t("The camp and the pyramid", "Das Lager und die Pyramide"),
    t("<p>Everything begins at the camp at the foot of the pyramid, Dr. Isabel Kaan's old dig: a canvas tent, a kettle on the fire, two straw training "
      "dummies and a carved target to practise on. Ahead, between two great feathered-serpent heads, the low tunnel leads into the Threshold.</p>"
      "<p>The camp is always a short walk from the hall, and it fills up as you restore it.</p>",
      "<p>Alles beginnt im Lager am Fuß der Pyramide, Dr. Isabel Kaans alter Grabung: ein Segeltuchzelt, ein Kessel über dem Feuer, zwei Trainingspuppen aus "
      "Stroh und eine geschnitzte Zielscheibe zum Üben. Vor dir führt der niedrige Tunnel zwischen zwei gewaltigen Federschlangenköpfen hinein in die Schwelle.</p>"
      "<p>Das Lager liegt immer nur ein paar Schritte von der Halle entfernt und füllt sich, je mehr du es wiederherstellst.</p>"))}
  {feature(ctx, "KEYART", t("Look and feel", "Look and Feel"), t("Colourful, playful, grounded", "Farbenfroh, verspielt, glaubwürdig"),
    t("<p>Painterly and stylized in the register of Ratchet &amp; Clank and Jak &amp; Daxter, but believable: carved limestone, jade inlay, hammered gold, "
      "glowing glyphs, mossy weathered stone, obsidian and torch flame.</p>"
      "<p>Five day signs mark everything in the temple, each with its own colour and shape: <span class='c-gold'>Ajaw, the sun</span>, "
      "<span class='c-blue'>Imix, water</span>, <span class='c-red'>K'ak', fire</span>, <span class='c-green'>K'an, growth</span> and "
      "<span class='c-white'>Ik', wind</span>.</p>",
      "<p>Malerisch und stilisiert wie Ratchet &amp; Clank und Jak &amp; Daxter, aber glaubwürdig: behauener Kalkstein, Jade-Einlagen, gehämmertes Gold, "
      "leuchtende Glyphen, bemooster, verwitterter Stein, Obsidian und Fackelschein.</p>"
      "<p>Fünf Tageszeichen kennzeichnen alles im Tempel, jedes mit eigener Farbe und Form: <span class='c-gold'>Ajaw, die Sonne</span>, "
      "<span class='c-blue'>Imix, das Wasser</span>, <span class='c-red'>K'ak', das Feuer</span>, <span class='c-green'>K'an, das Wachstum</span> und "
      "<span class='c-white'>Ik', der Wind</span>.</p>"), flip=True)}
</section>
"""


# ------------------------------------------------------------------ how it plays
def how_it_plays(ctx):
    u, t = ctx.url, ctx.t
    loops = [
        (t("Chamber", "Kammer"),
         t("45 to 120 seconds. The door seals. Fight, cross, or both. Then choose the next gate by the reward carved on it.",
           "45 bis 120 Sekunden. Die Tür schließt sich. Kämpfen, durchqueren oder beides. Dann wählst du das nächste Tor nach der Belohnung, die darauf gemeißelt ist.")),
        (t("Floor", "Ebene"),
         t("Two to four fights around the floor's authored rooms, then the Key Orb, then the Portal Chamber: take a rubbing, ring Oxlahun's bell, and decide whether to climb on.",
           "Zwei bis vier Kämpfe rund um die von Hand gebauten Räume der Ebene, dann die Schlüsselkugel, dann die Portalkammer: Abrieb nehmen, Oxlahuns Glocke läuten und entscheiden, ob du weiter aufsteigst.")),
        (t("Run", "Durchlauf"),
         t("25 to 45 minutes from a lit Sun Gate, until you die or walk home. Your health carries over from room to room, and healing is rare.",
           "25 bis 45 Minuten von einem entzündeten Sonnentor aus, bis du stirbst oder nach Hause gehst. Deine Gesundheit bleibt von Raum zu Raum gleich, und Heilung ist selten.")),
        (t("Return", "Rückkehr"),
         t(f"Wake at the Threshold. Sell or study what you carried, spend what you earned, and go back. <a href='{u('game/the-return.html')}'>The Return</a>",
           f"An der Schwelle erwachen. Verkaufen oder erforschen, was du getragen hast, ausgeben, was du verdient hast, und wieder hinauf. <a href='{u('game/the-return.html')}'>Die Rückkehr</a>")),
    ]
    gates = [
        (t("Day sign stone", "Tageszeichenstein"), t("A blessing from that sign. The main way to build power in a run.", "Ein Segen dieses Zeichens. Der wichtigste Weg, in einem Durchlauf stärker zu werden.")),
        (t("Coin bowl", "Münzschale"), t("Coins to spend at the next Waystall or shrine.", "Münzen für den nächsten Rastplatz oder Schrein.")),
        (t("Satchel", "Tasche"), t("A cache of Finds to carry out and sell.", "Ein Vorrat an Funden, die du hinausträgst und verkaufst.")),
        (t("Gold shard", "Goldsplitter"), t("Spirit Fragments, which you always keep.", "Geistsplitter, die du immer behältst.")),
        (t("Honey jar", "Honigtopf"), t("More maximum health. Rare.", "Mehr maximale Gesundheit. Selten.")),
        (t("Chisel", "Meißel"), t("A graving that changes your weapon for this run.", "Eine Gravur, die deine Waffe für diesen Durchlauf verändert.")),
        (t("Open book", "Offenes Buch"), t("A codex or lore page. Permanent.", "Eine Codex- oder Legendenseite. Dauerhaft.")),
        (t("Water basin", "Wasserbecken"), t("A Spirit Shrine: heal and shop, no fight.", "Ein Geisterschrein: heilen und einkaufen, kein Kampf.")),
        (t("Red sigil", "Rotes Siegel"), t("An elite chamber. Harder, and worth double.", "Eine Elitekammer. Härter und doppelt so viel wert.")),
    ]
    signs = [
        (f"<span class='c-blue'>Imix</span>", t("Water · three waves", "Wasser · drei Wellen"), t("Control: slows, knockback, currents", "Kontrolle: Verlangsamung, Rückstoß, Strömung")),
        (f"<span class='c-red'>K'ak'</span>", t("Fire · a flame", "Feuer · eine Flamme"), t("Burning, damage over time, area", "Brennen, Schaden über Zeit, Fläche")),
        (f"<span class='c-green'>K'an</span>", t("Growth · a maize cob", "Wachstum · ein Maiskolben"), t("Toughness, roots, stagger", "Zähigkeit, Wurzeln, Taumeln")),
        (f"<span class='c-white'>Ik'</span>", t("Wind · a spiral", "Wind · eine Spirale"), t("Speed, dodging, reach", "Tempo, Ausweichen, Reichweite")),
        (f"<span class='c-gold'>Ajaw</span>", t("Sun · a disc", "Sonne · eine Scheibe"), t("Focus, reading, coins", "Fokus, Lesen, Münzen")),
    ]
    collect = [
        ("P07", t("Energy Orbs", "Energiekugeln"),
         t("Puzzle energy in the temple's colours. Sun poured into water makes growth.", "Rätselenergie in den Farben des Tempels. Sonne in Wasser gegossen ergibt Wachstum.")),
        ("P08", t("Key Orb", "Schlüsselkugel"),
         t("One per floor. Socketing it opens the Portal Chamber's great door.", "Eine pro Ebene. Eingesetzt öffnet sie das große Tor der Portalkammer.")),
        ("P09", t("Golden Idols", "Goldene Idole"),
         t("One hidden in every authored room, off the safe path. Worth a good price, and a line of lore.", "Eines in jedem von Hand gebauten Raum, abseits des sicheren Wegs. Einen guten Preis wert und eine Zeile Legende.")),
        ("P10", t("Coins and Spirit Fragments", "Münzen und Geistsplitter"),
         t("Coins die with you. Fragments are what the spirit keeps.", "Münzen sterben mit dir. Die Splitter behält der Geist.")),
        ("P11", t("Codex pages and scrolls", "Codexseiten und Schriftrollen"),
         t("Evidence, and the most valuable things you can carry. Oxlahun agrees, which is interesting.", "Beweise, und das Wertvollste, was du tragen kannst. Oxlahun sieht das genauso, was interessant ist.")),
    ]
    collect_html = "".join(
        f'<article class="item">{ctx.figure(i, n, show_caption=False)}<div><h3>{n}</h3><p>{d}</p></div></article>' for i, n, d in collect)

    return f"""
<section class="wrap section narrow-top">
  <p class="kicker">{t("Four nested loops", "Vier verschachtelte Kreisläufe")}</p>
  <h2>{t("From one chamber to the whole temple", "Von der einzelnen Kammer zum ganzen Tempel")}</h2>
  {steps(loops, grid=False)}
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, ctx.pick("ACT-LENS", "T5C-SCENE"), t("Read", "Lesen"), t("The goggles change what you see", "Die Brille verändert, was du siehst"),
    t("<p>Hold a button and Kaya lowers her mother's bronze goggles. Time slows for a moment. Enemy weak points, trap timings, false floors and hidden cracks show themselves.</p>"
      f"<p>It runs on Focus, which you earn by fighting well. <a href='{u('game/reading.html')}'>Reading the Temple</a></p>",
      "<p>Halt eine Taste, und Kaya senkt die Bronzebrille ihrer Mutter. Die Zeit wird kurz langsamer. Schwachstellen der Gegner, Takt der Fallen, Trugböden und verborgene Risse zeigen sich.</p>"
      f"<p>Das kostet Fokus, den du durch guten Kampf verdienst. <a href='{u('game/reading.html')}'>Den Tempel lesen</a></p>"))}
  {feature(ctx, "B-10", t("Fight", "Kämpfen"), t("Up to twelve at once", "Bis zu zwölf auf einmal"),
    t("<p>Light combos, a heavy finisher, ranged tools and a quick dodge with a moment of invulnerability. Risen Guardians shamble, Bearers block, archers hold the high ground, "
      "panthers flank, Stone Sentries charge, and Guardian Spirits can only be outrun.</p>"
      f"<p><a href='{u('characters/creatures.html')}'>Meet the creatures and bosses</a></p>",
      "<p>Leichte Kombos, ein schwerer Abschlussschlag, Fernwaffen und ein schnelles Ausweichen mit einem Moment der Unverwundbarkeit. Erweckte Wächter schlurfen heran, Schildträger blocken, "
      "Schützen halten die Anhöhen, Panther greifen von der Seite an, Steinwächter stürmen los, und Wächtergeistern kann man nur davonlaufen.</p>"
      f"<p><a href='{u('characters/creatures.html')}'>Zu den Kreaturen und Bossen</a></p>"), flip=True)}
  {feature(ctx, "T2A-SCENE", t("Use the room", "Den Raum nutzen"), t("Traps hurt everyone", "Fallen treffen alle"),
    t("<p>Spikes, saws, pendulums, dart walls, fire vents, crushers and boulders fire on a beat you can learn, and they do triple damage to enemies. Luring a wave into a saw is often better than fighting it.</p>"
      "<p>On Floor 6 Kaya finds a chisel. From then on she can recut a trap's glyph, so that for a few seconds it hits only her enemies.</p>",
      "<p>Stacheln, Sägen, Pendel, Pfeilwände, Feuerdüsen, Stampfer und Felsbrocken folgen einem Takt, den du lernen kannst, und sie richten bei Gegnern dreifachen Schaden an. Eine Welle in eine Säge zu locken ist oft besser, als sie zu bekämpfen.</p>"
      "<p>Auf Ebene 6 findet Kaya einen Meißel. Von da an kann sie die Glyphe einer Falle nachmeißeln, sodass sie für ein paar Sekunden nur noch ihre Feinde trifft.</p>"))}
  {feature(ctx, "B-05", t("Move", "Bewegen"), t("Platforming between the fights", "Plattforming zwischen den Kämpfen"),
    t("<p>Run, sprint, jump, mantle and swim, across sliding slabs, swinging platforms, seesaws, rotating calendar discs, crumbling floors, phase steps, updrafts and lifts.</p>"
      "<p>A missed jump costs a little health and puts you back on the last safe ledge. It never costs the room.</p>",
      "<p>Laufen, sprinten, springen, hochziehen und schwimmen, über gleitende Steinplatten, schwingende Plattformen, Wippen, rotierende Kalenderscheiben, bröckelnde Böden, Phasenstufen, Aufwinde und Aufzüge.</p>"
      "<p>Ein verpatzter Sprung kostet etwas Gesundheit und setzt dich auf den letzten sicheren Sims zurück. Den Raum kostet er nie.</p>"), flip=True)}
  {feature(ctx, "B-08", t("Solve", "Lösen"), t("Puzzles that come back changed", "Rätsel, die verändert zurückkommen"),
    t("<p>Carry energy orbs, press plates in a mural's order, bounce sunlight off mirrors, split beams through prisms, sing with the song stones, align animal totems.</p>"
      "<p>The first solve is a study. After that, the room is Known: the temple reseeds the answer, your notebook keeps the method, and the second solve takes thirty seconds with something trying to kill you.</p>",
      "<p>Energiekugeln tragen, Platten in der Reihenfolge eines Wandbilds drücken, Sonnenlicht über Spiegel lenken, Strahlen durch Prismen teilen, mit den Klangsteinen singen, Tiertotems ausrichten.</p>"
      "<p>Das erste Lösen ist ein Studium. Danach ist der Raum bekannt: Der Tempel mischt die Lösung neu, dein Notizbuch bewahrt die Methode, und das zweite Lösen dauert dreißig Sekunden, während etwas versucht, dich umzubringen.</p>"))}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Carved gates", "Gemeißelte Tore")}</p>
  <h2>{t("Every exit is a choice", "Jeder Ausgang ist eine Entscheidung")}</h2>
  <p class="lede-sm">{t("Most chambers end in two or three gates, each with a glowing glyph that shows what lies behind it.",
                        "Die meisten Kammern enden in zwei oder drei Toren, jedes mit einer leuchtenden Glyphe, die zeigt, was dahinter liegt.")}</p>
  {table([t("Glyph", "Glyphe"), t("What it gives you", "Was es dir bringt")], gates)}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Blessings", "Segen")}</p>
  <h2>{t("Five day signs, a new build every run", "Fünf Tageszeichen, in jedem Durchlauf ein neuer Aufbau")}</h2>
  <p class="lede-sm">{t("Blessings change your strike, heavy attack, shot, dodge and goggles until you die. Two signs can combine into something rarer.",
                        "Segen verändern deinen Schlag, schweren Angriff, Schuss, dein Ausweichen und deine Brille, bis du stirbst. Zwei Zeichen können sich zu etwas Selteneren verbinden.")}</p>
  {table([t("Sign", "Zeichen"), t("Means", "Bedeutung"), t("Plays like", "Spielt sich wie")], signs)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("After the summit", "Nach dem Gipfel")}</p>
  <h2>{t("Two more portals", "Zwei weitere Portale")}</h2>
  {modes([
    (t("Left portal", "Linkes Portal"), t("Expedition", "Expedition"),
     t("Return to any cleared floor at low danger with your full kit, to open orb-gated side routes and collect idols and evidence.",
       "Kehre mit voller Ausrüstung bei geringer Gefahr in jede geschaffte Ebene zurück, um durch Kugeln versperrte Nebenwege zu öffnen und Idole und Beweise zu sammeln.")),
    (t("Right portal", "Rechtes Portal"), t("Trials of the Shifting Temple", "Prüfungen des wandelnden Tempels"),
     t("Opens after the first summit. Choose curses from <em>Temple's Wrath</em> before a run: more undead, faster traps, a hunting spirit, a silent K'in. The higher the Wrath, the richer the reward.",
       "Öffnet sich nach dem ersten Gipfel. Wähle vor einem Durchlauf Flüche aus dem <em>Zorn des Tempels</em>: mehr Untote, schnellere Fallen, ein jagender Geist, eine schweigende K'in. Je höher der Zorn, desto reicher die Belohnung.")),
    (t("Every chamber", "Jede Kammer"), t("Your own ghost", "Dein eigener Geist"),
     t("Your best time through any chamber walks ahead of you as a faint golden figure, if you want something to race.",
       "Deine beste Zeit durch jede Kammer läuft als schwache goldene Gestalt vor dir her, wenn du etwas zum Wettrennen suchst.")),
  ])}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Collectibles", "Sammelobjekte")}</p>
  <h2>{t("What Kaya carries out", "Was Kaya herausträgt")}</h2>
  <div class="items">{collect_html}</div>
</div></section>
"""


# ------------------------------------------------------------------ the return
def the_return(ctx):
    u, t = ctx.url, ctx.t
    ritual = [
        (t("Stone under her cheek", "Stein an der Wange"),
         t("She wakes on the Threshold floor. There's no wound, only an ache. The sunbeam has moved one seam. Another dot goes into the count on the back page of her notebook.",
           "Sie erwacht auf dem Boden der Schwelle. Keine Wunde, nur ein Schmerz. Der Sonnenstrahl ist eine Fuge weitergewandert. Ein weiterer Punkt kommt in die Zählung auf der letzten Seite ihres Notizbuchs.")),
        (t("K'in's greeting", "K'ins Gruß"),
         t("A line chosen by what just happened: a new killer, a new floor, a boss, or the same words worn smooth.",
           "Ein Satz, ausgewählt nach dem, was gerade geschehen ist: ein neuer Mörder, eine neue Ebene, ein Boss, oder dieselben, glattgeschliffenen Worte.")),
        (t("Oxlahun's table", "Oxlahuns Tisch"),
         t("“Tell me where it got you.” He pours tea, buys what you carried, and carves a little limestone keepsake of whatever killed you.",
           "„Erzähl mir, wo es dich erwischt hat.“ Er gießt Tee ein, kauft, was du getragen hast, und schnitzt ein kleines Andenken aus Kalkstein von dem, was dich getötet hat.")),
        (t("The field desk", "Der Feldschreibtisch"),
         t("Any Find can be studied here for Insight instead of sold. You can't do both.",
           "Jeder Fund lässt sich hier für Einsicht erforschen, statt ihn zu verkaufen. Beides geht nicht.")),
        (t("The Spirit Mural", "Das Geisterwandbild"),
         t("New panels light up. Kaya's own carving has changed. You work on your rubbings at the reading desk.",
           "Neue Tafeln leuchten auf. Kayas eigenes Relief hat sich verändert. Am Lesepult arbeitest du an deinen Abrieben.")),
        (t("The Memory Wheel", "Das Erinnerungsrad"),
         t("Spend Spirit Fragments on permanent talents at the round altar.", "Gib am runden Altar Geistsplitter für dauerhafte Talente aus.")),
        (t("The portals", "Die Portale"),
         t("Pick a Sun Gate, a weapon and a keepsake, and go back up. It all takes about a minute, and you can skip any of it.",
           "Wähle ein Sonnentor, eine Waffe und ein Andenken, und steig wieder auf. Das Ganze dauert etwa eine Minute, und du kannst alles überspringen.")),
    ]
    keep = [
        (t("Coins", "Münzen"), t("Lost", "Verloren"), t("Lost, so spend them", "Verloren, also ausgeben")),
        (t("Blessings and gravings", "Segen und Gravuren"), t("Lost", "Verloren"), t("Lost", "Verloren")),
        (t("Finds in the satchel", "Funde in der Tasche"), t("Kept, but death-touched: they sell for 40%", "Behalten, aber vom Tod berührt: Verkauf für 40 %"), t("Clean, with the Long Carry bonus", "Sauber, mit dem Bonus fürs lange Tragen")),
        (t("Spirit Fragments", "Geistsplitter"), t("All kept, plus a bonus for how high you got", "Alle behalten, dazu ein Bonus für die erreichte Höhe"), t("All kept", "Alle behalten")),
        (t("Notebook, rubbings, lexicon", "Notizbuch, Abriebe, Lexikon"), t("Always kept", "Immer behalten"), t("Always kept", "Immer behalten")),
        (t("Elemental Orbs, weapons, talents", "Elementarkugeln, Waffen, Talente"), t("Always kept", "Immer behalten"), t("Always kept", "Immer behalten")),
    ]
    shop = [
        (t("Sell", "Verkaufen"), t("Finds for Jade", "Funde gegen Jade"),
         t("Jade buys weapons, camp restoration and permanent stock. He always pays best for anything with writing on it.",
           "Jade kauft Waffen, die Wiederherstellung des Lagers und dauerhaftes Sortiment. Für alles, worauf etwas geschrieben steht, zahlt er immer am besten.")),
        (t("Bounties", "Aufträge"), t("Three requests per return", "Drei Wünsche pro Rückkehr"),
         t("“Two jade masks. No questions.” Double pay, and a reason to choose your next route.",
           "„Zwei Jademasken. Keine Fragen.“ Doppelter Lohn und ein Grund, die nächste Route zu wählen.")),
        (t("Pawn", "Verpfänden"), t("A loan against your gear", "Ein Kredit auf deine Ausrüstung"),
         t("Pledge a weapon or keepsake for a large coin advance before a hard climb. Die, and the tab doubles.",
           "Verpfände vor einem harten Aufstieg eine Waffe oder ein Andenken für einen großen Münzvorschuss. Stirbst du, verdoppelt sich die Rechnung.")),
        (t("The Waystall", "Der Rastplatz"), t("A bell and a speaking tube", "Eine Glocke und ein Sprechrohr"),
         t("On the floors, you ring, a tray slides out, and his voice comes down the tube. Nobody knows how.",
           "Auf den Ebenen läutest du, ein Tablett gleitet heraus, und seine Stimme kommt das Rohr herunter. Niemand weiß, wie.")),
        (t("The tagged goods", "Die Waren mit Etikett"), t("A brass lantern, a notched staff", "Eine Messinglaterne, ein gekerbter Stab"),
         t("His table holds things that once belonged to someone. Each has a blank tag. You can buy them.",
           "Auf seinem Tisch liegen Dinge, die einmal jemandem gehört haben. Jedes trägt ein leeres Etikett. Du kannst sie kaufen.")),
    ]
    camp = [
        (t("Kettle", "Kessel"), t("Tea before a run: extra health on the first floor", "Tee vor dem Durchlauf: mehr Gesundheit auf der ersten Ebene")),
        (t("Map table", "Kartentisch"), t("Shows idols, side routes and evidence on each floor", "Zeigt Idole, Nebenwege und Beweise jeder Ebene")),
        (t("Rope rack", "Seilgestell"), t("More room in the satchel", "Mehr Platz in der Tasche")),
        (t("Isabel's desk", "Isabels Schreibtisch"), t("Better study results, and her notebook pages", "Bessere Forschungsergebnisse und ihre Notizbuchseiten")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("Dying is how the game moves forward. Every return brings something new: a line, a carving, a sale, a reading. You never go back up empty-handed.",
                      "Sterben ist der Weg, auf dem das Spiel vorankommt. Jede Rückkehr bringt etwas Neues: einen Satz, ein Relief, einen Verkauf, eine Lesart. Du steigst nie mit leeren Händen wieder auf.")}</p>
  </div>
  <div style="margin-top:32px">{feature(ctx, ctx.pick("ACT-RETURN", "A-03"), t("The ritual", "Das Ritual"), t("Back in the Threshold", "Zurück in der Schwelle"),
    t("<p>The hall never changes, and that's the point. What changes is the record: what people say to you, what's on the table, and what's on the wall.</p>",
      "<p>Die Halle verändert sich nie, und genau das ist der Punkt. Was sich verändert, ist die Überlieferung: was die Leute zu dir sagen, was auf dem Tisch liegt und was an der Wand steht.</p>"))}</div>
  {steps(ritual)}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("What death takes", "Was der Tod nimmt")}</p>
  <h2>{t("The temple takes your gold. It never takes your notes.", "Der Tempel nimmt dein Gold. Deine Notizen nimmt er nie.")}</h2>
  {table([t("Item", "Gegenstand"), t("If you die", "Wenn du stirbst"), t("If you walk home", "Wenn du nach Hause gehst")], keep)}
</div></section>

<section class="wrap section">
  {feature(ctx, ctx.pick("ACT-CS-OXLAHUN", "HOME-OXLAHUN"), t("The trader", "Der Händler"), t("“Tell me where it got you.”", "„Erzähl mir, wo es dich erwischt hat.“"),
    t(f"<p><a href='{u('characters/oxlahun.html')}'>Oxlahun</a> is really useful, and he has never once been wrong about a floor. His business also only works while climbers keep dying.</p>"
      "<p>Every new thing that kills you earns a free carving of it. Equip one per run, and it helps against that killer. Dying somewhere new is how you get the tool against it.</p>",
      f"<p><a href='{u('characters/oxlahun.html')}'>Oxlahun</a> ist wirklich nützlich, und er hat sich noch nie in einer Ebene geirrt. Sein Geschäft läuft allerdings auch nur, solange Kletterer weiter sterben.</p>"
      "<p>Alles Neue, das dich tötet, bringt dir eine kostenlose Schnitzerei davon. Rüste pro Durchlauf eine aus, und sie hilft gegen genau diesen Mörder. An einer neuen Stelle zu sterben ist der Weg zum Werkzeug dagegen.</p>"))}
  {modes(shop)}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("At every Portal Chamber", "In jeder Portalkammer")}</p>
  <h2>{t("Climb on, or go home rich?", "Weiter aufsteigen oder reich nach Hause gehen?")}</h2>
  {modes([
    (t("Risk it", "Es riskieren"), t("Climb on", "Weiter aufsteigen"),
     t("Keep everything and risk everything. Each floor without banking raises your Long Carry bonus on what you hold.",
       "Alles behalten und alles riskieren. Jede Ebene ohne Absichern erhöht deinen Bonus fürs lange Tragen.")),
    (t("Pay for safety", "Für Sicherheit zahlen"), t("Use the Drop", "Den Schacht benutzen"),
     t("Pay part of your coins to send your Finds down the offering chute. They reach Oxlahun clean, and the bonus resets.",
       "Zahl einen Teil deiner Münzen, um deine Funde den Opferschacht hinunterzuschicken. Sie kommen sauber bei Oxlahun an, und der Bonus beginnt von vorn.")),
    (t("Walk away", "Weggehen"), t("Go home alive", "Lebend nach Hause"),
     t("Take the return portal. Your Finds are clean and the bonus pays out. Your blessings and coins are gone.",
       "Nimm das Rückkehrportal. Deine Funde sind sauber, und der Bonus zahlt sich aus. Deine Segen und Münzen sind weg.")),
  ])}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Sell or study", "Verkaufen oder erforschen")}</p>
  <h2>{t("The decision behind every Find", "Die Entscheidung hinter jedem Fund")}</h2>
  <p class="lede-sm">{t(f"Every Find can pay for your next upgrade, or teach you something. Sell it for Jade, or study it for Insight, which levels up the goggles and opens new readings. <a href='{u('game/reading.html')}'>Reading the Temple</a>",
                        f"Jeder Fund kann dein nächstes Upgrade bezahlen oder dir etwas beibringen. Verkauf ihn für Jade oder erforsche ihn für Einsicht, die die Brille verbessert und neue Lesarten öffnet. <a href='{u('game/reading.html')}'>Den Tempel lesen</a>")}</p>
  {feature(ctx, ctx.pick("ACT-CAMP", "HUB01"), t("Home", "Zuhause"), t("A camp that fills up", "Ein Lager, das sich füllt"),
    t("<p>Isabel's camp stands thirty steps from the hall. Jade restores it slot by slot, and each slot gives you something real.</p>",
      "<p>Isabels Lager liegt dreißig Schritte von der Halle entfernt. Jade stellt es Platz für Platz wieder her, und jeder Platz bringt dir etwas Echtes.</p>"))}
  {table([t("Slot", "Platz"), t("What it does", "Was er bewirkt")], camp)}
  {feature(ctx, ctx.pick("ACT-WHEEL", "HUB06"), t("Permanent", "Dauerhaft"), t("The Memory Wheel", "Das Erinnerungsrad"),
    t("<p>The round altar is a calendar wheel, and K'in tends it. Spirit Fragments buy lasting talents: a spirit K'in can catch once before it falls, more health, a second dodge, a keener eye. Every talent has two versions you can swap between.</p>",
      "<p>Der runde Altar ist ein Kalenderrad, und K'in pflegt es. Geistsplitter kaufen dauerhafte Talente: einen Geist, den K'in einmal auffangen kann, bevor er fällt, mehr Gesundheit, ein zweites Ausweichen, ein schärferes Auge. Jedes Talent hat zwei Fassungen, zwischen denen du wechseln kannst.</p>"), flip=True)}
{art_row(ctx, RETURN_ART)}
</section>
"""


# ------------------------------------------------------------------ reading
def reading(ctx):
    u, t = ctx.url, ctx.t
    lens = [
        (t("Enemy sigils", "Gegner-Siegel"), t("Marks a weak point, and each enemy type you read stays in the notebook and gets easier", "Markiert eine Schwachstelle, und jede gelesene Gegnerart bleibt im Notizbuch und wird leichter")),
        (t("Traps", "Fallen"), t("Shows a timing ring on the trap and its trigger", "Zeigt einen Taktring an der Falle und ihrem Auslöser")),
        (t("Floors and walls", "Böden und Wände"), t("Shows false floors, hidden paths, cracked walls and secret passages", "Zeigt Trugböden, verborgene Pfade, rissige Wände und geheime Gänge")),
        (t("Glyphs", "Glyphen"), t("Adds what you see to your lexicon", "Fügt hinzu, was du siehst, deinem Lexikon")),
    ]
    method = [
        (t("Take a rubbing", "Einen Abrieb nehmen"),
         t("At each Portal Chamber, charcoal and paper over the fragment that just lit up. Once per floor, and yours for good.",
           "In jeder Portalkammer Kohle und Papier auf das Fragment, das gerade aufgeleuchtet ist. Einmal pro Ebene und für immer dein.")),
        (t("Build a lexicon", "Ein Lexikon aufbauen"),
         t("Each glyph you've seen has a meaning that's blank, possible or confirmed.",
           "Jede Glyphe, die du gesehen hast, hat eine Bedeutung, die leer, möglich oder bestätigt ist.")),
        (t("Read it", "Lesen"),
         t("At the desk, K'in's version sits on one side. On the other you fill in the glyphs. A wrong guess costs nothing; the sentence just doesn't resolve.",
           "Am Pult steht K'ins Fassung auf der einen Seite. Auf der anderen füllst du die Glyphen aus. Ein falscher Versuch kostet nichts; der Satz löst sich nur nicht auf.")),
        (t("Confirm it", "Bestätigen"),
         t("Isabel's rule: never act on an unverified reading. A meaning is confirmed when two sources agree.",
           "Isabels Regel: Handle nie nach einer ungeprüften Lesart. Eine Bedeutung gilt als bestätigt, wenn zwei Quellen übereinstimmen.")),
    ]
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("Everyone else who climbed this temple took the stairs. Kaya reads the wall.", "Alle anderen, die diesen Tempel erklommen, nahmen die Treppe. Kaya liest die Wand.")}</p>
    <p>{t("Reading is the game's signature. It's how she survives the fights, how she finds what's hidden, and how the story reaches you. Everything she learns stays with her through every death.",
          "Lesen ist das Markenzeichen des Spiels. So übersteht sie die Kämpfe, so findet sie, was verborgen ist, und so erreicht dich die Geschichte. Alles, was sie lernt, bleibt ihr über jeden Tod hinaus.")}</p>
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, ctx.pick("ACT-LENS", "T5C-SCENE"), t("Her mother's goggles", "Die Brille ihrer Mutter"), t("The Lens", "Die Linse"),
    t("<p>The bronze goggles Isabel left behind. Hold a button to lower them, and the world answers.</p>",
      "<p>Die Bronzebrille, die Isabel zurückließ. Halt eine Taste, um sie zu senken, und die Welt antwortet.</p>"))}
  {table([t("What you read", "Was du liest"), t("What it gives you", "Was es dir bringt")], lens)}
</div></section>

<section class="wrap section">
  {feature(ctx, "HOME-NEVERALONE", t("Two guides", "Zwei Führer"), t("K'in's path, or your own eyes", "K'ins Pfad oder deine eigenen Augen"),
    t("<p>K'in's ghost path is free, always safe and always there. The Lens costs Focus and is always true.</p>"
      "<p>On the lower floors they agree. Higher up, you may start to notice what her path walks past.</p>",
      "<p>K'ins Geisterpfad ist kostenlos, immer sicher und immer da. Die Linse kostet Fokus und ist immer wahr.</p>"
      "<p>Auf den unteren Ebenen stimmen beide überein. Weiter oben fällt dir vielleicht auf, woran ihr Pfad vorbeiführt.</p>"), flip=True)}
  {feature(ctx, ctx.pick("ACT-RECUT", "T2C-SCENE"), t("From Floor 6", "Ab Ebene 6"), t("Recut", "Nachmeißeln"),
    t("<p>A chisel changes how Kaya sees the temple's defences. With the Lens on, she can recut a marked trap's glyph, and for a few seconds it hits only her enemies. The trap makers built everything to answer to the old glyphs, and she can read them.</p>",
      "<p>Ein Meißel verändert, wie Kaya die Verteidigung des Tempels sieht. Mit der Linse kann sie die Glyphe einer markierten Falle nachmeißeln, und für ein paar Sekunden trifft sie nur noch ihre Feinde. Die Fallenbauer haben alles so gebaut, dass es auf die alten Glyphen hört, und sie kann sie lesen.</p>"))}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("The wall is evidence", "Die Wand ist ein Beweisstück")}</p>
  <h2>{t("Two readings of every fragment", "Zwei Lesarten jedes Fragments")}</h2>
  <p class="lede-sm">{t(f"K'in tells you what a fragment means. The glyphs say what they say. They don't always agree, and <a href='{u('story/index.html')}'>the story</a> lives in the difference.",
                        f"K'in sagt dir, was ein Fragment bedeutet. Die Glyphen sagen, was sie sagen. Sie stimmen nicht immer überein, und <a href='{u('story/index.html')}'>die Geschichte</a> lebt in diesem Unterschied.")}</p>
  {steps(method, grid=False)}
</div></section>

<section class="wrap section">
  {feature(ctx, "HUB11", t("The notebook", "Das Notizbuch"), t("Noted, not read", "Notiert, nicht gelesen"),
    t("<p>The map, the bestiary, the trap ledger, the lexicon and the journal are all pages of Kaya's field notebook, written in her voice. Every new enemy, trap and death adds a line.</p>"
      "<p>On the back page she keeps a count, in her mother's bar-and-dot numerals. It started at 412.</p>",
      "<p>Karte, Bestiarium, Fallenverzeichnis, Lexikon und Tagebuch sind alles Seiten von Kayas Feldnotizbuch, in ihrer Stimme geschrieben. Jeder neue Gegner, jede Falle und jeder Tod fügt eine Zeile hinzu.</p>"
      "<p>Auf der letzten Seite führt sie eine Zählung, in den Balken-und-Punkt-Zahlen ihrer Mutter. Sie begann bei 412.</p>"))}
{art_row(ctx, READING_ART)}
</section>
"""


# ------------------------------------------------------------------ weapons & powers
def weapons(ctx):
    u, t = ctx.url, ctx.t
    arms = [
        ("W01", t("Obsidian Macuahuitl", "Obsidian-Macuahuitl"), t("Melee · found in the Shell", "Nahkampf · gefunden in The Shell"),
         t("A flat war-club of dark hardwood edged with black obsidian blades, banded in hammered gold. Light combo plus a heavy finisher. Lifting it from the sword shrine is what wakes the first guardian.",
           "Eine flache Kriegskeule aus dunklem Hartholz, besetzt mit schwarzen Obsidianklingen, mit Bändern aus gehämmertem Gold. Leichte Kombo plus schwerer Abschlussschlag. Wer sie aus dem Schwertschrein hebt, weckt den ersten Wächter.")),
        ("W02", t("Spirit Blowgun", "Geisterblasrohr"), t("Ranged, fast · found on Floor 2", "Fernkampf, schnell · gefunden auf Ebene 2"),
         t("A long reed tube with a carved jade hummingbird mouthpiece. It strikes glyph targets high on shrine walls and keeps archers honest.",
           "Ein langes Schilfrohr mit einem geschnitzten Kolibri-Mundstück aus Jade. Es trifft Glyphenziele hoch an Schreinwänden und hält Bogenschützen in Schach.")),
        ("W03", t("Sunburst Sling", "Sonnenschleuder"), t("Ranged, charged · from Oxlahun's table", "Fernkampf, aufladbar · von Oxlahuns Tisch"),
         t("Braided cords and carved river stones that glow brighter the longer the shot is charged. A full charge cracks armour.",
           "Geflochtene Schnüre und geschnitzte Flusssteine, die umso heller leuchten, je länger der Schuss aufgeladen wird. Voll aufgeladen knackt er Panzer.")),
        ("W04", t("Ember Censer", "Glutweihrauchfass"), t("Short flame cone · found with the Fire Orb", "Kurzer Flammenkegel · gefunden mit der Feuerkugel"),
         t("A clay burner shaped like an old fire god, swung on a bronze chain. It breathes a short cone of flame and lights braziers.",
           "Ein Räuchergefäß aus Ton in Gestalt eines alten Feuergottes, an einer Bronzekette geschwungen. Es speit einen kurzen Flammenkegel und entzündet Feuerschalen.")),
    ]
    arm_html = "".join(
        f'<article class="item item-wide">{ctx.figure(i, n, show_caption=False)}<div><p class="kicker">{s}</p><h3>{n}</h3><p>{d}</p></div></article>'
        for i, n, s, d in arms)
    bought = [
        (t("The Surveyor's Staff", "Der Stab des Landvermessers"), t("Melee, long reach", "Nahkampf, große Reichweite"), t("Its tip fires triggers and plates from a safe distance.", "Seine Spitze löst Auslöser und Platten aus sicherer Entfernung aus.")),
        (t("A coil of rope", "Eine Seilrolle"), t("Melee, pull", "Nahkampf, Ziehen"), t("A weighted line that drags enemies into traps and pits, and swings from anchors.", "Eine beschwerte Leine, die Gegner in Fallen und Gruben zieht und an Ankern schwingt.")),
        (t("A brass lantern", "Eine Messinglaterne"), t("Ranged, area", "Fernkampf, Fläche"), t("Throws burning oil. It also shows hidden things nearby without using Focus.", "Wirft brennendes Öl. Zeigt außerdem Verborgenes in der Nähe, ohne Fokus zu verbrauchen.")),
    ]
    orbs = [
        (t("Fire", "Feuer"), "c-red", t("The Ember Forge", "Die Glutschmiede"), t("Ignite braziers, burn vines and rope", "Feuerschalen entzünden, Ranken und Seile verbrennen"), t("Flame burst", "Flammenstoß")),
        (t("Earth", "Erde"), "c-green", t("The Buried Ossuary", "Das verschüttete Beinhaus"), t("Shatter cracked walls, weigh down plates", "Rissige Wände zertrümmern, Platten beschweren"), t("Ground pound that breaks shields", "Bodenstampfer, der Schilde bricht")),
        (t("Wind", "Wind"), "c-white", t("The Broken Ramparts", "Die zerbrochenen Wälle"), t("Glide, air dash, ride updrafts", "Gleiten, Luftsprint, Aufwinde nutzen"), t("Gust that pushes enemies off ledges", "Windstoß, der Gegner von Simsen stößt")),
        (t("Water", "Wasser"), "c-blue", t("The Sunken Reservoir", "Das versunkene Reservoir"), t("Part and lower water, douse fire", "Wasser teilen und absenken, Feuer löschen"), t("Surge that knocks down and soaks", "Welle, die umwirft und durchnässt")),
    ]
    orb_rows = "".join(f'<tr><th scope="row" class="{c}">{n}</th><td>{w}</td><td>{tv}</td><td>{f}</td></tr>' for n, c, w, tv, f in orbs)
    return f"""
<section class="wrap section narrow-top">
  <p class="kicker">{t("Weapons", "Waffen")}</p>
  <h2>{t("A scholar's arsenal, found in the temple", "Das Arsenal einer Gelehrten, gefunden im Tempel")}</h2>
  <p class="lede-sm">{t("Kaya enters with a brush and a notebook. Every weapon is a discovery. At the portal, you pick one melee and one ranged weapon for the run.",
                        "Kaya betritt den Tempel mit Pinsel und Notizbuch. Jede Waffe ist eine Entdeckung. Am Portal wählst du eine Nahkampf- und eine Fernwaffe für den Durchlauf.")}</p>
  <div class="items">{arm_html}</div>
  <h3 class="sub-head">{t("From Oxlahun's table", "Von Oxlahuns Tisch")}</h3>
  <p class="lede-sm">{t("Three more weapons wait there with blank tags. They belonged to someone.", "Drei weitere Waffen warten dort mit leeren Etiketten. Sie haben jemandem gehört.")}</p>
  {table([t("Weapon", "Waffe"), t("Type", "Art"), t("What it does", "Was sie kann")], bought)}
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "W05", t("Permanent powers", "Dauerhafte Kräfte"), t("The four Elemental Orbs", "Die vier Elementarkugeln"),
    t(f"<p>The builders harnessed fire, earth, wind and water through four sacred orbs. Kaya claims them in the <a href='{u('climb/tier-4.html')}'>Elemental Sanctums</a>, in any order you choose, and they stay with her through every death.</p>"
      "<p>Each orb is a way to move, a way to fight and a key. Every orb you own opens new routes in floors you've already climbed.</p>",
      f"<p>Die Erbauer bändigten Feuer, Erde, Wind und Wasser mit vier heiligen Kugeln. Kaya erringt sie in den <a href='{u('climb/tier-4.html')}'>Elementarheiligtümern</a>, in beliebiger Reihenfolge, und sie bleiben ihr über jeden Tod hinaus.</p>"
      "<p>Jede Kugel ist Fortbewegung, Kampfkraft und Schlüssel zugleich. Jede Kugel, die du besitzt, öffnet neue Wege in Ebenen, die du schon erklommen hast.</p>"))}
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Orb", "Kugel")}</th><th>{t("Earned in", "Errungen in")}</th><th>{t("Traversal", "Fortbewegung")}</th><th>{t("Combat", "Kampf")}</th></tr></thead>
    <tbody>{orb_rows}</tbody>
  </table></div>
</div></section>

<section class="wrap section">
  {feature(ctx, "W06", t("The goal", "Das Ziel"), t("The Sun Orb", "Die Sonnenkugel"),
    t("<p>The brightest thing in the game: a blazing golden orb with a living sun glyph at its core, cradled in four carved gold hands.</p>"
      "<p>It waits in a sealed vault behind the Priest's Lieutenant on Floor 24. Then Kaya has to carry it through a temple that's fully awake, all the way to the Sky Altar. "
      f"<a href='{u('climb/sky-altar.html')}'>The summit</a></p>",
      "<p>Das hellste Objekt im Spiel: eine lodernde goldene Kugel mit einer lebendigen Sonnenglyphe im Kern, gehalten von vier geschnitzten Goldhänden.</p>"
      "<p>Sie wartet in einem versiegelten Gewölbe hinter dem Leutnant des Priesters auf Ebene 24. Dann muss Kaya sie durch einen hellwachen Tempel bis zum Himmelsaltar tragen. "
      f"<a href='{u('climb/sky-altar.html')}'>Zum Gipfel</a></p>"))}
  {feature(ctx, ctx.pick("ACT-SIGN", "P07"), t("Run powers", "Kräfte für den Durchlauf"), t("Blessings, gravings and keepsakes", "Segen, Gravuren und Andenken"),
    t(f"<p>Day sign blessings and weapon gravings last until you die. Keepsakes, carved by Oxlahun from whatever killed you, are permanent, and you pick one per run. <a href='{u('game/the-return.html')}'>The Return</a></p>",
      f"<p>Segen der Tageszeichen und Waffengravuren halten, bis du stirbst. Andenken, die Oxlahun aus dem schnitzt, was dich getötet hat, sind dauerhaft, und du wählst eines pro Durchlauf. <a href='{u('game/the-return.html')}'>Die Rückkehr</a></p>"), flip=True)}
{art_row(ctx, WEAPON_ART)}
</section>
"""


PAGES = {
    "game/index.html": dict(
        title=("Overview & Pillars", "Überblick & Säulen"), kicker=("The Game", "Das Spiel"), banner="B-11",
        lede=("A single-player action roguelite inside a living Mayan pyramid, built in Unreal Engine 5.",
              "Ein Action-Roguelite für einen Spieler in einer lebenden Maya-Pyramide, gebaut in der Unreal Engine 5."),
        description=("What Ascent of the Sun Temple is, and the five design pillars behind it.",
                     "Was Ascent of the Sun Temple ist und welche fünf Design-Säulen dahinterstehen."),
        body=overview, og="B-11"),
    "game/how-it-plays.html": dict(
        title=("How It Plays", "So wird gespielt"), kicker=("The Game", "Das Spiel"), banner="B-05",
        lede=("Read, fight, move, solve. Then die, return to the Threshold, and climb again knowing more.",
              "Lesen, kämpfen, bewegen, lösen. Dann sterben, an die Schwelle zurückkehren und mit mehr Wissen wieder aufsteigen."),
        description=("The loops, gates, combat, traps, puzzles, blessings and modes of Ascent of the Sun Temple.",
                     "Kreisläufe, Tore, Kampf, Fallen, Rätsel, Segen und Modi von Ascent of the Sun Temple."),
        body=how_it_plays, og="B-05"),
    "game/the-return.html": dict(
        title=("The Return", "Die Rückkehr"), kicker=("The Game", "Das Spiel"), banner=["ACT-RETURN", "A-03"],
        lede=("Wake on the stone floor. Pour the tea. Sell what you carried. Read what you copied. Go back up.",
              "Auf dem Steinboden erwachen. Tee einschenken. Verkaufen, was du getragen hast. Lesen, was du abgeschrieben hast. Wieder hinauf."),
        description=("What happens every time Kaya dies: the Threshold, Oxlahun, Finds, keepsakes, the camp and the Memory Wheel.",
                     "Was jedes Mal geschieht, wenn Kaya stirbt: die Schwelle, Oxlahun, Funde, Andenken, das Lager und das Erinnerungsrad."),
        body=the_return, og=["ACT-RETURN", "A-03"]),
    "game/reading.html": dict(
        title=("Reading the Temple", "Den Tempel lesen"), kicker=("The Game", "Das Spiel"), banner=["ACT-LENS", "HOME-ISABEL"],
        lede=("Kaya's goggles, her chisel, her notebook, and the two versions of every story on the wall.",
              "Kayas Brille, ihr Meißel, ihr Notizbuch und die zwei Fassungen jeder Geschichte an der Wand."),
        description=("The Lens, Recut, rubbings and the lexicon: how Kaya reads the temple.",
                     "Die Linse, das Nachmeißeln, die Abriebe und das Lexikon: wie Kaya den Tempel liest."),
        body=reading, og=["ACT-LENS", "HOME-ISABEL"]),
    "game/weapons-and-powers.html": dict(
        title=("Weapons & Powers", "Waffen & Kräfte"), kicker=("The Game", "Das Spiel"), banner="T4B-SCENE",
        lede=("Seven weapons, four permanent Elemental Orbs and the one Sun Orb that opens the summit.",
              "Sieben Waffen, vier dauerhafte Elementarkugeln und die eine Sonnenkugel, die den Gipfel öffnet."),
        description=("Kaya's weapons, the Elemental Orbs and the Sun Orb.", "Kayas Waffen, die Elementarkugeln und die Sonnenkugel."),
        body=weapons, og="W05"),
}
