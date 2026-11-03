"""The Game tab: Overview & Pillars, How It Plays, Weapons & Powers (English and German)."""


def feature(ctx, img, kicker, title, text, flip=False, caption=None):
    cls = " flip" if flip else ""
    k = f'<p class="kicker">{kicker}</p>' if kicker else ""
    return (f'<div class="feature{cls}"><div class="feature-media">{ctx.figure(img, caption, alt=title)}</div>'
            f'<div class="feature-text">{k}<h3>{title}</h3>{text}</div></div>')


# ------------------------------------------------------------------ overview
def overview(ctx):
    u, t = ctx.url, ctx.t
    pillars = [
        ("01", t("Ascend", "Aufsteigen"),
         t("Every run is a climb. The temple beneath you is progress made visible: the hub sits at the foot of a real pyramid, and the Sky Altar you are climbing toward is its actual summit.",
           "Jeder Durchlauf ist ein Aufstieg. Der Tempel unter dir macht Fortschritt sichtbar: Der Hub liegt am Fuß einer echten Pyramide, und der Himmelsaltar, zu dem du aufsteigst, ist ihr tatsächlicher Gipfel.")),
        ("02", t("Fight", "Kämpfen"),
         t("Melee and ranged combat against cursed priests and awakened creatures. The obsidian macuahuitl comes first, then the blowgun, the sling and the ember censer.",
           "Nah- und Fernkampf gegen verfluchte Priester und erwachte Kreaturen. Zuerst kommt das Obsidian-Macuahuitl, dann das Blasrohr, die Schleuder und das Glutweihrauchfass.")),
        ("03", t("Solve", "Lösen"),
         t("Puzzles grow with the climb: one mechanic per room in the lower tiers, combined mechanics in the middle, layered perception puzzles under pressure near the top.",
           "Die Rätsel wachsen mit dem Aufstieg: eine Mechanik pro Raum in den unteren Stufen, kombinierte Mechaniken in der Mitte und vielschichtige Wahrnehmungsrätsel unter Zeitdruck nahe der Spitze.")),
        ("04", t("Grow for good", "Dauerhaft wachsen"),
         t("The four Elemental Orbs and the upgrades bought in the Threshold stay with every Climber between runs, each one opens routes that were closed before, and your own carving on the Spirit Mural grows with every tier.",
           "Die vier Elementarkugeln und die in der Schwelle gekauften Verbesserungen bleiben jedem Kletterer über alle Durchläufe erhalten, jede davon öffnet Wege, die vorher verschlossen waren, und dein eigenes Relief auf dem Geisterwandbild wächst mit jeder Stufe.")),
        ("05", t("Never alone", "Nie allein"),
         t("Climb with up to three friends, and every room is still solvable alone. K'in teaches, warns, foreshadows and remembers: she draws ghost paths after a missed jump, flickers before a trap fires and greets every return.",
           "Kletter mit bis zu drei Freunden, und jeder Raum bleibt trotzdem allein lösbar. K'in lehrt, warnt, deutet an und erinnert sich: Nach einem verpatzten Sprung zeichnet sie Geisterpfade, sie flackert, bevor eine Falle auslöst, und begrüßt jede Rückkehr.")),
    ]
    pillar_html = "".join(f'<li><span class="num">{n}</span><div><h3>{nm}</h3><p>{d}</p></div></li>' for n, nm, d in pillars)

    facts = [
        (t("Genre", "Genre"), t("Co-op action-adventure platformer with a roguelite climb",
                                "Koop-Action-Adventure-Plattformer mit Roguelite-Aufstieg")),
        (t("Platform", "Plattform"), t("A Fortnite island, built in UEFN", "Eine Fortnite-Insel, gebaut im UEFN")),
        (t("Inspirations", "Vorbilder"), t("Ratchet &amp; Clank and Jak &amp; Daxter for tone; Hades for the return-and-grow loop",
                                          "Ratchet &amp; Clank und Jak &amp; Daxter für den Stil; Hades für den Kreislauf aus Rückkehr und Wachstum")),
        (t("Players", "Spieler"), t("1–4, co-op; you play your own Fortnite character", "1–4, Koop; du spielst deine eigene Fortnite-Figur")),
        (t("Campaign", "Kampagne"), t("The Shell, seventeen floors in six tiers, and the Sky Altar summit",
                                      "The Shell, siebzehn Ebenen in sechs Stufen und der Himmelsaltar auf dem Gipfel")),
        (t("Setting", "Schauplatz"), t("The interior of one living stepped pyramid, plus the jungle forecourt and the open summit",
                                       "Das Innere einer lebenden Stufenpyramide, dazu der Dschungelvorplatz und der offene Gipfel")),
    ]
    fact_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    q1, q2 = t("“", "„"), t("”", "“")
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Ascent of the Sun Temple: Climbers is the flagship of Mayan Temple Adventures: a co-op climb for up "
                        "to four players through an ancient Mayan sun temple that is alive. It rearranges itself and swallows "
                        "everyone who climbs it.",
                        "Ascent of the Sun Temple: Climbers ist die Hauptinsel von Mayan Temple Adventures: ein Koop-Aufstieg "
                        "für bis zu vier Spieler durch einen uralten Maya-Sonnentempel, der lebt. Er ordnet sich ständig neu "
                        "und verschlingt jeden, der ihn erklimmt.")}</p>
      <p>{t("You play a Climber, in your own Fortnite character. Kaya, a young explorer, climbs the first floor beside "
            "you, and K'in, the temple's last spirit, guides you the rest of the way. Floor by floor your party fights the "
            "risen guardians, survives the traps, solves the orb puzzles and earns the elemental powers the builders once "
            "held, until you carry the Sun Orb to the great portal on the summit and vote on the temple's fate: restore the "
            f"cycle, or break it. <a href='{u('game/climbers-and-co-op.html')}'>Climbers and co-op →</a>",
            "Du spielst einen Kletterer, in deiner eigenen Fortnite-Figur. Kaya, eine junge Entdeckerin, steigt die erste "
            "Ebene an deiner Seite hinauf, und K'in, der letzte Geist des Tempels, führt dich den Rest des Wegs. Ebene für "
            "Ebene kämpft deine Gruppe gegen die erweckten Wächter, übersteht die Fallen, löst die Kugelrätsel und erringt "
            "die Elementarkräfte der Erbauer, bis ihr die Sonnenkugel zum großen Portal auf dem Gipfel tragt und über das "
            "Schicksal des Tempels abstimmt: den Kreislauf wiederherstellen oder ihn durchbrechen. "
            f"<a href='{u('game/climbers-and-co-op.html')}'>Kletterer und Koop →</a>")}</p>
      <p>{t(f"The story explains the structure. The temple <em>{q1}rearranges itself to trap greedy adventurers{q2}</em>, so "
            "shuffled room layouts belong to the world rather than to a menu. And "
            f"<em>{q1}the cycle begins again… unless you break it{q2}</em>: when a Climber dies, K'in pulls their spirit back "
            "to the Threshold. What the spirit keeps between cycles, the Elemental Orbs and the fragments gathered on the way, "
            "is what makes the next climb go further.",
            f"Die Geschichte erklärt die Struktur. Der Tempel <em>{q1}ordnet sich neu, um gierige Abenteurer in die Falle zu "
            f"locken{q2}</em>, also gehören wechselnde Raumabfolgen zur Welt und nicht zu einem Menü. Und "
            f"<em>{q1}der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn{q2}</em>: Stirbt ein Kletterer, zieht "
            "K'in seinen Geist zurück an die Schwelle. Was der Geist von Kreislauf zu Kreislauf behält, die Elementarkugeln und "
            "die gesammelten Geistsplitter, bringt den nächsten Aufstieg weiter.")}</p>
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
  {feature(ctx, "A-04", t("First steps", "Erste Schritte"), t("The jungle forecourt", "Der Dschungelvorplatz"),
    t("<p>Every climb begins at the camp at the foot of the pyramid, Dr. Isabel Kaan's old dig: a canvas tent, a kettle on the fire, two straw "
      "training dummies and a carved target to practise on. Ahead, between two great feathered-serpent heads, the low "
      "tunnel leads into the Threshold.</p><p>The pyramid is always in view, so the summit is a goal you can see from "
      "the very first minute.</p>",
      "<p>Jeder Aufstieg beginnt im Lager am Fuß der Pyramide, Dr. Isabel Kaans alter Grabung: ein Segeltuchzelt, ein Kessel über dem Feuer, zwei "
      "Trainingspuppen aus Stroh und eine geschnitzte Zielscheibe zum Üben. Vor ihr führt der niedrige Tunnel zwischen zwei "
      "gewaltigen Federschlangenköpfen hinein in die Schwelle.</p><p>Die Pyramide ist immer zu sehen, der Gipfel ist also "
      "von der ersten Minute an ein sichtbares Ziel.</p>"))}
  {feature(ctx, "KEYART", t("Look and feel", "Look and Feel"), t("Colourful, playful, grounded", "Farbenfroh, verspielt, glaubwürdig"),
    t("<p>Painterly and stylized in the register of Ratchet &amp; Clank and Jak &amp; Daxter, but believable: carved "
      "limestone, jade inlay, hammered gold, glowing glyphs, mossy weathered stone, obsidian and torch flame.</p>"
      "<p>Four energy colours mark every interactive object: <span class='c-gold'>gold for sun</span>, "
      "<span class='c-blue'>blue for water</span>, <span class='c-red'>red for fire</span> and "
      f"<span class='c-green'>green for growth</span>. <a href='{u('art/index.html')}'>More on the art direction →</a></p>",
      "<p>Malerisch und stilisiert wie Ratchet &amp; Clank und Jak &amp; Daxter, aber glaubwürdig: behauener Kalkstein, "
      "Jade-Einlagen, gehämmertes Gold, leuchtende Glyphen, bemooster, verwitterter Stein, Obsidian und Fackelschein.</p>"
      "<p>Vier Energiefarben kennzeichnen jedes interaktive Objekt: <span class='c-gold'>Gold für die Sonne</span>, "
      "<span class='c-blue'>Blau für Wasser</span>, <span class='c-red'>Rot für Feuer</span> und "
      f"<span class='c-green'>Grün für Wachstum</span>. <a href='{u('art/index.html')}'>Mehr zur Art Direction →</a></p>"),
    flip=True)}
</section>
"""


# ------------------------------------------------------------------ how it plays
def how_it_plays(ctx):
    u, t = ctx.url, ctx.t
    loops = [
        (t("Room", "Raum"),
         t("Arrive on the four arrival pads, traverse and fight, solve the room's lock, then gather at the exit: the gate opens once the whole party stands there.",
           "Auf den vier Ankunftsplattformen ankommen, durchqueren und kämpfen, das Schloss des Raums lösen und euch am Ausgang sammeln: Das Tor öffnet sich, sobald die ganze Gruppe dort steht.")),
        (t("Floor", "Ebene"),
         t("Room A, then Room B with the floor's Key Orb, then the Portal Chamber: socket the orb, hear K'in's line, light a mural fragment, bank your coins and ascend. The party carries one Key Orb, and whoever falls drops it.",
           "Raum A, dann Raum B mit der Schlüsselkugel der Ebene, dann die Portalkammer: Kugel einsetzen, K'ins Satz hören, ein Wandbildfragment entzünden, Münzen sichern und aufsteigen. Die Gruppe trägt eine Schlüsselkugel, und wer fällt, lässt sie fallen.")),
        (t("Run", "Durchlauf"),
         t("Leave the Threshold and climb. In the story, a fallen Climber returns at the room's checkpoint while anyone in the party still stands. Only a party wipe pulls everyone back to the Threshold: some unbanked coins are lost, Spirit Fragments are kept.",
           "Die Schwelle verlassen und aufsteigen. In der Story kehrt ein gefallener Kletterer am Checkpoint des Raums zurück, solange noch jemand aus der Gruppe steht. Erst wenn alle fallen, zieht der Tempel die ganze Gruppe an die Schwelle zurück: Ein Teil der ungesicherten Münzen geht verloren, die Geistsplitter bleiben.")),
        (t("Meta", "Meta"),
         t("Spend fragments at the Threshold, unlock weapons and gear, fill the Spirit Mural, open tier shortcuts and claim the Elemental Orbs that reshape the climb.",
           "Splitter in der Schwelle ausgeben, Waffen und Ausrüstung freischalten, das Geisterwandbild füllen, Abkürzungen zu den Stufen öffnen und die Elementarkugeln erringen, die den Aufstieg verändern.")),
    ]
    loop_html = "".join(f'<li><span class="loop-label">{n}</span><p>{d}</p></li>' for n, d in loops)

    modes = [
        (t("The Ascent", "Der Aufstieg"), t("Story", "Story"),
         t("A fixed, hand-built room order. The first playthrough, with the Shell as the tutorial that teaches every core verb once.",
           "Eine feste, von Hand gebaute Raumfolge. Der erste Durchgang, mit The Shell als Tutorial, das jede Kernaktion einmal beibringt.")),
        (t("Trials of the Shifting Temple", "Prüfungen des wandelnden Tempels"), t("Opens tier by tier", "Öffnet sich Stufe für Stufe"),
         t("Rooms shuffle within each tier while the tier order stays fixed, and a tier's Trials open as soon as the party clears it in the story. Stackable <em>Temple's Wrath</em> curses add tougher undead, faster traps, fewer checkpoints, roaming Guardian Spirits and timed floors, and each level earns better rewards.",
           "Innerhalb jeder Stufe werden die Räume gemischt, die Reihenfolge der Stufen bleibt fest, und die Prüfungen einer Stufe öffnen sich, sobald die Gruppe sie in der Story geschafft hat. Stapelbare Flüche des <em>Zorns des Tempels</em> bringen zähere Untote, schnellere Fallen, weniger Checkpoints, umherstreifende Wächtergeister und Ebenen auf Zeit, und jede Stufe bringt bessere Belohnungen.")),
        (t("Expedition", "Expedition"), t("Replay", "Wiederholen"),
         t("Return to any cleared floor in its story layout with your full kit, to collect idols, earn medallions and open the orb-gated side routes.",
           "Kehre mit voller Ausrüstung in jede abgeschlossene Ebene in ihrer Story-Fassung zurück, um Idole zu sammeln, Medaillons zu verdienen und die durch Kugeln versperrten Nebenwege zu öffnen.")),
    ]
    mode_html = "".join(f'<article class="mode"><p class="kicker">{s}</p><h3>{n}</h3><p>{d}</p></article>' for n, s, d in modes)
    trial = [
        (t("Before the run", "Vor dem Durchlauf"), t("Temple's Wrath", "Zorn des Tempels"),
         t("Ten stackable curses, from more undead and faster traps to no checkpoints and a silent K'in. The higher the Wrath, the richer the reward.",
           "Zehn stapelbare Flüche, von mehr Untoten und schnelleren Fallen bis zu fehlenden Checkpoints und einer schweigenden K'in. Je höher der Zorn, desto reicher die Belohnung.")),
        (t("At every Spirit Shrine", "An jedem Geisterschrein"), t("Blessings", "Segen"),
         t("Each Climber picks one of three blessings for the run, in the four energy colours: faster sprints, slower traps, quicker revives, burning blades.",
           "Jeder Kletterer wählt einen von drei Segen für den Durchlauf, in den vier Energiefarben: schnellere Sprints, langsamere Fallen, schnellere Wiederbelebung, brennende Klingen.")),
        (t("From every boss", "Von jedem Boss"), t("Sun Shards", "Sonnensplitter"),
         t("Each boss beaten in the Trials drops a shard. Four of them make a Trial Sun, which opens the hardest run of all: Eclipse.",
           "Jeder in den Prüfungen besiegte Boss lässt einen Splitter fallen. Vier davon ergeben eine Prüfungssonne, die den härtesten Durchlauf von allen öffnet: Eclipse.")),
    ]
    trial_html = "".join(f'<article class="mode"><p class="kicker">{s}</p><h3>{n}</h3><p>{d}</p></article>' for s, n, d in trial)

    collect = [
        ("P07", t("Energy Orbs", "Energiekugeln"),
         t("In-room puzzle currency in four colours. Sun poured into water makes growth.",
           "Rätselwährung innerhalb eines Raums, in vier Farben. Sonne in Wasser gegossen ergibt Wachstum.")),
        ("P08", t("Key Orb", "Schlüsselkugel"),
         t("One per floor. Socketing it opens the Portal Chamber's great door.",
           "Eine pro Ebene. Eingesetzt öffnet sie das große Tor der Portalkammer.")),
        ("P09", t("Golden Idols", "Goldene Idole"),
         t("Exactly one hidden in every room, for lore and completion.",
           "Genau eines in jedem Raum versteckt, für Hintergrundwissen und Vollständigkeit.")),
        ("P10", t("Coins and Spirit Fragments", "Münzen und Geistsplitter"),
         t("Coins are spent during a run and mostly lost on death. Fragments are what the spirit keeps.",
           "Münzen werden während eines Durchlaufs ausgegeben und gehen beim Tod größtenteils verloren. Die Splitter behält der Geist.")),
        ("P11", t("Codex pages, scrolls and medallions", "Codexseiten, Schriftrollen und Medaillons"),
         t("Painted map pages, lore scrolls, glyph echoes, ancient shards for cosmetics, and trial medallions for speed, no damage, all coins and deathless runs.",
           "Bemalte Kartenseiten, Schriftrollen mit Legenden, Glyphen-Echos, uralte Scherben für kosmetische Extras und Prüfungsmedaillons für Tempo, keinen Schaden, alle Münzen und Durchläufe ohne Tod.")),
    ]
    collect_html = "".join(
        f'<article class="item">{ctx.figure(i, n, show_caption=False)}<div><h3>{n}</h3><p>{d}</p></div></article>'
        for i, n, d in collect)

    return f"""
<section class="wrap section narrow-top">
  <p class="kicker">{t("Four nested loops", "Vier verschachtelte Kreisläufe")}</p>
  <h2>{t("From one room to the whole temple", "Vom einzelnen Raum zum ganzen Tempel")}</h2>
  <ol class="loops">{loop_html}</ol>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "B-05", t("Move", "Bewegen"), t("Platforming that never waits", "Plattforming, das nie wartet"),
    t("<p>Run, sprint, jump, mantle, crouch and swim, across a platform set that keeps changing: sliding slabs, floating "
      "and swinging platforms, seesaws, rotating calendar discs, crumbling floors, vanishing phase steps, updrafts and "
      "lifts.</p><p>Every room hands you one new idea, then the next room asks you to use it while something else is "
      "trying to kill you.</p>",
      "<p>Laufen, sprinten, springen, hochziehen, ducken und schwimmen, über Plattformen, die sich ständig ändern: "
      "gleitende Steinplatten, schwebende und schwingende Plattformen, Wippen, rotierende Kalenderscheiben, bröckelnde "
      "Böden, verschwindende Phasenstufen, Aufwinde und Aufzüge.</p><p>Jeder Raum gibt dir eine neue Idee an die Hand, "
      "und der nächste verlangt, dass du sie anwendest, während etwas anderes versucht, dich umzubringen.</p>"))}
  {feature(ctx, "B-07", t("Read", "Lesen"), t("Traps with a rhythm", "Fallen mit Rhythmus"),
    t("<p>Spikes, fire vents, fireball serpent heads, saw tracks, pendulums, dart walls, rolling boulders and crushing "
      "walls. Each fires on a readable beat, and K'in flickers a warning before it goes off.</p><p>Getting through "
      "once is luck. Getting through clean means you have learned the beats.</p>",
      "<p>Stacheln, Feuerdüsen, feuerspeiende Schlangenköpfe, Sägeschienen, Pendel, Pfeilwände, rollende Felsbrocken und "
      "zermalmende Wände. Jede Falle folgt einem lesbaren Takt, und K'in flackert warnend, bevor sie auslöst.</p>"
      "<p>Einmal durchzukommen ist Glück. Sauber durchzukommen heißt, den Takt gelernt zu haben.</p>"), flip=True)}
  {feature(ctx, "B-10", t("Fight", "Kämpfen"), t("Cursed priests and awakened stone", "Verfluchte Priester und erwachter Stein"),
    t("<p>Light combos and a heavy finisher with the macuahuitl, then ranged tools for archers on ledges and targets "
      "out of reach. Risen Guardians shamble, Husk Archers hold the high ground, Obsidian Panthers flank, Stone "
      "Sentries charge, and Guardian Spirits can only be outrun.</p>"
      f"<p><a href='{u('characters/creatures.html')}'>Meet the creatures and bosses →</a></p>",
      "<p>Leichte Kombos und ein schwerer Abschlussschlag mit dem Macuahuitl, dann Fernwaffen gegen Bogenschützen auf "
      "Simsen und unerreichbare Ziele. Erweckte Wächter schlurfen heran, Hülsenschützen halten die Anhöhen, "
      "Obsidianpanther greifen von der Seite an, Steinwächter stürmen los, und Wächtergeistern kann man nur davonlaufen.</p>"
      f"<p><a href='{u('characters/creatures.html')}'>Zu den Kreaturen und Bossen →</a></p>"))}
  {feature(ctx, "B-08", t("Solve", "Lösen"), t("Orbs, plates, light and memory", "Kugeln, Platten, Licht und Erinnerung"),
    t("<p>Carry energy orbs between pedestals, press plates in the order a mural shows, bounce sunlight off bronze "
      "mirrors, split beams through coloured prisms, align animal totems and walk a path that is only visible while "
      "K'in sings.</p><p>K'in lights the orb that is wrong rather than the one that is right, so the solving is still "
      "yours.</p>",
      "<p>Energiekugeln zwischen Sockeln tragen, Platten in der Reihenfolge drücken, die ein Wandbild zeigt, Sonnenlicht "
      "über Bronzespiegel lenken, Strahlen durch farbige Prismen teilen, Tiertotems ausrichten und einen Pfad gehen, der "
      "nur sichtbar ist, solange K'in singt.</p><p>K'in lässt die falsche Kugel aufleuchten, nicht die richtige, damit "
      "das Lösen deine Sache bleibt.</p>"), flip=True)}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Modes", "Modi")}</p>
  <h2>{t("One room pool, three ways to climb", "Ein Raumpool, drei Arten aufzusteigen")}</h2>
  <div class="modes">{mode_html}</div>
  <h3 class="sub-head">{t("Inside a Trial", "In einer Prüfung")}</h3>
  <div class="modes">{trial_html}</div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Collectibles and economy", "Sammelobjekte und Wirtschaft")}</p>
  <h2>{t("What Climbers carry out of every room", "Was Kletterer aus jedem Raum mitnehmen")}</h2>
  <div class="items">{collect_html}</div>
</div></section>
"""


# ------------------------------------------------------------------ weapons & powers
def weapons(ctx):
    u, t = ctx.url, ctx.t
    arms = [
        ("W01", t("Obsidian Macuahuitl", "Obsidian-Macuahuitl"), t("Melee · found in the Shell", "Nahkampf · gefunden in The Shell"),
         t("A flat paddle war-club of dark hardwood edged with black obsidian blades, banded in hammered gold with a jade "
           "glyph strip down its centre. Light combo plus a heavy finisher; on a heavy attack the glyphs flare gold. "
           "Lifting it from the sword shrine is what wakes the first guardian.",
           "Eine flache Kriegskeule aus dunklem Hartholz, besetzt mit schwarzen Obsidianklingen, mit Bändern aus gehämmertem "
           "Gold und einem Jadestreifen voller Glyphen in der Mitte. Leichte Kombo plus schwerer Abschlussschlag; beim "
           "schweren Angriff glühen die Glyphen golden auf. Wer sie aus dem Schwertschrein hebt, weckt den ersten Wächter.")),
        ("W02", t("Spirit Blowgun", "Geisterblasrohr"), t("Ranged, fast · found on Floor 2", "Fernkampf, schnell · gefunden auf Ebene 2"),
         t("A long reed-and-wood tube with a carved jade hummingbird mouthpiece, gold bands and a painted gourd quiver. "
           "The first ranged weapon: it strikes glyph targets high on shrine walls and keeps archers honest.",
           "Ein langes Rohr aus Schilf und Holz mit einem geschnitzten Kolibri-Mundstück aus Jade, Goldbändern und einem "
           "bemalten Kalebassen-Köcher. Die erste Fernwaffe: Sie trifft Glyphenziele hoch an Schreinwänden und hält "
           "Bogenschützen in Schach.")),
        ("W03", t("Sunburst Sling", "Sonnenschleuder"), t("Ranged, charged · from the Threshold after Tier I", "Fernkampf, aufladbar · in der Schwelle nach Stufe I"),
         t("Braided cotton cords, a pouch backed by a small gold sun disc and carved river stones that glow brighter the "
           "longer the shot is charged. A fully charged stone leaves like a small sun, and cracks armoured husks.",
           "Geflochtene Baumwollschnüre, eine Tasche mit einer kleinen goldenen Sonnenscheibe und geschnitzte Flusssteine, "
           "die umso heller leuchten, je länger der Schuss aufgeladen wird. Ein voll aufgeladener Stein fliegt los wie "
           "eine kleine Sonne und knackt gepanzerte Hülsen.")),
        ("W04", t("Ember Censer", "Glutweihrauchfass"), t("Short flame cone · found with the Fire Orb", "Kurzer Flammenkegel · gefunden mit der Feuerkugel"),
         t("A clay incense burner shaped like the face of an old fire god, swung on a bronze chain. It breathes a short "
           "cone of flame, lights braziers and burns away vine-choked doors.",
           "Ein Räuchergefäß aus Ton in Gestalt eines alten Feuergottes, an einer Bronzekette geschwungen. Es speit einen "
           "kurzen Flammenkegel, entzündet Feuerschalen und brennt von Ranken überwucherte Türen frei.")),
    ]
    arm_html = "".join(
        f'<article class="item item-wide">{ctx.figure(i, n, show_caption=False)}<div><p class="kicker">{s}</p><h3>{n}</h3><p>{d}</p></div></article>'
        for i, n, s, d in arms)

    orbs = [
        (t("Fire", "Feuer"), "c-red", t("Floor 9 · The Ember Forge", "Ebene 9 · Die Glutschmiede"),
         t("Ignite braziers and burn vine doors", "Feuerschalen entzünden, Rankentüren abbrennen"), t("Flame attack", "Flammenangriff")),
        (t("Earth", "Erde"), "c-green", t("Floor 10 · The Buried Ossuary", "Ebene 10 · Das verschüttete Beinhaus"),
         t("Shatter cracked walls, weigh down heavy plates", "Rissige Wände zertrümmern, schwere Platten beschweren"), t("Ground-pound", "Bodenstampfer")),
        (t("Wind", "Wind"), "c-white", t("Floor 11 · The Broken Ramparts", "Ebene 11 · Die zerbrochenen Wälle"),
         t("Glide, dash and ride updrafts", "Gleiten, sprinten und Aufwinde nutzen"), t("Gust push", "Windstoß")),
        (t("Water", "Wasser"), "c-blue", t("Floor 12 · The Sunken Reservoir", "Ebene 12 · Das versunkene Reservoir"),
         t("Part and lower water, swim faster", "Wasser teilen und absenken, schneller schwimmen"), t("Douse hazards", "Gefahren löschen")),
    ]
    orb_rows = "".join(
        f'<tr><th scope="row" class="{c}">{n}</th><td>{w}</td><td>{tv}</td><td>{f}</td></tr>' for n, c, w, tv, f in orbs)

    return f"""
<section class="wrap section narrow-top">
  <p class="kicker">{t("Weapons", "Waffen")}</p>
  <h2>{t("An explorer's arsenal, found in the temple", "Das Arsenal der Entdecker, gefunden im Tempel")}</h2>
  <p class="lede-sm">{t("Climbers enter with empty hands. Every weapon is a discovery, and each one changes what you can "
                        "reach as much as what you can fight.",
                        "Kletterer betreten den Tempel mit leeren Händen. Jede Waffe ist eine Entdeckung und verändert, "
                        "was du erreichen kannst, ebenso sehr wie das, was du bekämpfen kannst.")}</p>
  <div class="items">{arm_html}</div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "W05", t("Permanent powers", "Dauerhafte Kräfte"), t("The four Elemental Orbs", "Die vier Elementarkugeln"),
    t("<p>The builders harnessed fire, earth, wind and water through four sacred orbs. Climbers claim them one by one "
      "in the Elemental Sanctums, and unlike everything else they gather, the orbs stay with each spirit through every "
      "death.</p><p>Each orb is a traversal tool, a combat power and a key. Rooms that need an orb only enter the Trials "
      "room pool once the party owns it, so the temple literally grows with you. If a friend has not claimed an orb yet, "
      "K'in lends them a glowing echo of it for that room.</p>",
      "<p>Die Erbauer bändigten Feuer, Erde, Wind und Wasser mit vier heiligen Kugeln. Kletterer erringen sie "
      "nacheinander in den Elementarheiligtümern, und anders als alles andere, was sie sammeln, bleiben die Kugeln jedem "
      "Geist über jeden Tod hinaus erhalten.</p><p>Jede Kugel ist Fortbewegungswerkzeug, Kampfkraft und Schlüssel "
      "zugleich. Räume, die eine Kugel erfordern, kommen erst in den Raumpool der Prüfungen, wenn die Gruppe sie besitzt; "
      "der Tempel wächst also buchstäblich mit euch. Hat ein Freund eine Kugel noch nicht errungen, leiht K'in ihm für "
      "diesen Raum ein leuchtendes Echo davon.</p>"))}
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Orb", "Kugel")}</th><th>{t("Earned on", "Errungen auf")}</th><th>{t("Traversal", "Fortbewegung")}</th><th>{t("Combat", "Kampf")}</th></tr></thead>
    <tbody>{orb_rows}</tbody>
  </table></div>
</div></section>

<section class="wrap section">
  {feature(ctx, "W06", t("The goal", "Das Ziel"), t("The Sun Orb", "Die Sonnenkugel"),
    t("<p>The brightest thing in the game. A blazing golden orb with a living sun glyph at its core, cradled in four "
      "carved gold hands set with red, green, white and blue gems, one for each element.</p>"
      "<p>It waits in a sealed vault behind the Priest's Lieutenant on Floor 17. Carried to the Sky Altar, it opens the "
      "Sun Portal and puts the final choice in the party's hands: every Climber steps onto Restore or Break, and the "
      f"majority decides. <a href='{u('climb/sky-altar.html')}'>The summit →</a></p>",
      "<p>Das hellste Objekt im Spiel. Eine lodernde goldene Kugel mit einer lebendigen Sonnenglyphe im Kern, gehalten "
      "von vier geschnitzten Goldhänden mit roten, grünen, weißen und blauen Edelsteinen, einem für jedes Element.</p>"
      "<p>Sie wartet in einem versiegelten Gewölbe hinter dem Leutnant des Priesters auf Ebene 17. Zum Himmelsaltar "
      "getragen, öffnet sie das Sonnenportal und legt die letzte Entscheidung in die Hände der Gruppe: Jeder Kletterer "
      "tritt auf Wiederherstellen oder Durchbrechen, und die Mehrheit entscheidet. "
      f"<a href='{u('climb/sky-altar.html')}'>Zum Gipfel →</a></p>"))}
  {feature(ctx, "P07", t("Puzzle energy", "Rätselenergie"), t("Energy Orbs", "Energiekugeln"),
    t("<p>The working orbs of every puzzle room: gold sun, blue water, red fire and green growth, each held in a "
      "gold-and-jade band. They can be carried, socketed and combined: pour sun into water and you get growth.</p>",
      "<p>Die Arbeitskugeln jedes Rätselraums: goldene Sonne, blaues Wasser, rotes Feuer und grünes Wachstum, jede in "
      "einem Band aus Gold und Jade gefasst. Sie lassen sich tragen, einsetzen und kombinieren: Gießt man Sonne in "
      "Wasser, entsteht Wachstum.</p>"), flip=True)}
</section>
"""


# ------------------------------------------------------------------ climbers & co-op
def climbers(ctx):
    u, t = ctx.url, ctx.t
    kaya_steps = [
        (t("Floor 0", "Ebene 0"),
         t("Kaya climbs the Shell beside the party, waits for you at every section and points the way. In the spike "
           "corridor the temple takes her, and she dissolves into gold light.",
           "Kaya steigt mit der Gruppe durch The Shell, wartet an jedem Abschnitt auf euch und zeigt den Weg. Im "
           "Stachelkorridor holt der Tempel sie, und sie zerfällt in goldenes Licht.")),
        (t("The Threshold", "Die Schwelle"),
         t("You find her back at the Threshold, alive, staring at her own fresh carving on the Spirit Mural. From then on "
           "she stays to read the wall, and sends Climbers up for the evidence she needs: mural fragments, codex pages, "
           "her mother's notes.",
           "Ihr findet sie an der Schwelle wieder, lebendig, vor ihrem eigenen frischen Relief auf dem Geisterwandbild. Von "
           "da an bleibt sie, um die Wand zu lesen, und schickt Kletterer nach den Beweisen aus, die sie braucht: "
           "Wandbildfragmente, Codexseiten, die Notizen ihrer Mutter.")),
        (t("On the way up", "Auf dem Weg nach oben"),
         t("Three times on the climb, Kaya meets the party with something new she has read in the stone. What she finds "
           "is for the players to discover.",
           "Dreimal auf dem Weg nach oben trifft Kaya die Gruppe mit etwas Neuem, das sie im Stein gelesen hat. Was sie "
           "findet, sollen die Spieler selbst entdecken.")),
    ]
    kaya_html = "".join(f'<li><span class="loop-label">{n}</span><p>{d}</p></li>' for n, d in kaya_steps)

    rules = [
        (t("At the exit gate", "Am Ausgangstor"), t("No one left behind", "Niemand bleibt zurück"),
         t("A room's exit opens when its lock is solved and every living Climber stands at the gate.",
           "Der Ausgang eines Raums öffnet sich, wenn sein Schloss gelöst ist und jeder lebende Kletterer am Tor steht.")),
        (t("Per floor", "Pro Ebene"), t("One Key Orb", "Eine Schlüsselkugel"),
         t("The party carries a single Key Orb to the Portal Chamber. If its carrier falls, anyone can pick it up.",
           "Die Gruppe trägt eine einzige Schlüsselkugel zur Portalkammer. Fällt ihr Träger, kann jeder sie aufheben.")),
        (t("When you fall", "Wenn du fällst"), t("Back on your feet", "Wieder auf den Beinen"),
         t("In the story, a fallen Climber returns at the room's checkpoint after a few seconds, as long as someone in "
           "the party is still standing.",
           "In der Story kehrt ein gefallener Kletterer nach ein paar Sekunden am Checkpoint des Raums zurück, solange "
           "noch jemand aus der Gruppe steht.")),
        (t("Orbs you lack", "Fehlende Kugeln"), t("Borrowed echoes", "Geliehene Echos"),
         t("If a room needs an Elemental Orb a friend has not claimed yet, K'in lends them a glowing echo of it for that "
           "room only.",
           "Braucht ein Raum eine Elementarkugel, die ein Freund noch nicht errungen hat, leiht K'in ihm ein leuchtendes "
           "Echo davon, nur für diesen Raum.")),
        (t("Between sessions", "Zwischen den Sitzungen"), t("Catch up together", "Gemeinsam aufholen"),
         t("Progress belongs to each player. Friends who are behind still earn everything, and get the floor credited when "
           "the party clears it.",
           "Der Fortschritt gehört jedem Spieler selbst. Freunde, die zurückliegen, verdienen trotzdem alles und bekommen "
           "die Ebene angerechnet, wenn die Gruppe sie schafft.")),
        (t("On the summit", "Auf dem Gipfel"), t("The ending vote", "Die Abstimmung"),
         t("Each Climber stands at Restore or Break. The majority decides, and every player's own save remembers how they "
           "voted.",
           "Jeder Kletterer stellt sich auf Wiederherstellen oder Durchbrechen. Die Mehrheit entscheidet, und jeder "
           "Spielstand merkt sich, wie sein Spieler gestimmt hat.")),
    ]
    rule_html = "".join(f'<article class="mode"><p class="kicker">{k}</p><h3>{n}</h3><p>{d}</p></article>' for k, n, d in rules)

    rooms = [
        (t("1 · The Drowned Gallery", "1 · Die ertrunkene Galerie"),
         t("One Climber drains the channel from the balcony while the others wait at the stairs.",
           "Ein Kletterer lässt den Kanal vom Balkon aus ab, während die anderen an der Treppe warten.")),
        (t("3 · Hall of Blades", "3 · Halle der Klingen"),
         t("Stand on the four corner plates together, in the right order, and the dart volley never fires.",
           "Steht gemeinsam in der richtigen Reihenfolge auf den vier Eckplatten, und die Pfeilsalve feuert nie.")),
        (t("5 · The Collapsing Stair", "5 · Die einstürzende Treppe"),
         t("The Guardian Spirit speeds up while anyone lags behind, so the party has to move as one.",
           "Der Wächtergeist wird schneller, solange jemand zurückbleibt, also muss sich die Gruppe gemeinsam bewegen.")),
        (t("8 · The Gear Ascent", "8 · Der Zahnradaufstieg"),
         t("The Gearwarden turns toward the nearest Climber: one lures it into a vent pillar while the others strike its core.",
           "Der Zahnradwächter wendet sich dem nächsten Kletterer zu: Einer lockt ihn an eine Dampfsäule, während die anderen seinen Kern treffen.")),
        (t("10 · The Buried Ossuary", "10 · Das verschüttete Beinhaus"),
         t("Two Climbers pushing a boulder move it twice as fast.",
           "Zwei Kletterer, die einen Felsbrocken schieben, bewegen ihn doppelt so schnell.")),
        (t("11 · The Broken Ramparts", "11 · Die zerbrochenen Wälle"),
         t("The first Climber up an updraft can lower a rope ladder for the rest.",
           "Wer zuerst mit dem Aufwind oben ist, kann den anderen eine Strickleiter herablassen.")),
        (t("14 · The Hall of Lies", "14 · Die Halle der Lügen"),
         t("Glyph Scan shows the false tiles only to the Climber using it, who has to guide the others across.",
           "Der Glyphenscan zeigt die falschen Kacheln nur dem Kletterer, der ihn benutzt, und der muss die anderen hinüberlotsen.")),
        (t("15 · The Totem Vault", "15 · Das Totemgewölbe"),
         t("The Jaguar Priest hides in one of four totems, so the party splits up to cover them all.",
           "Der Jaguarpriester versteckt sich in einem von vier Totems, also teilt sich die Gruppe auf, um alle zu bewachen.")),
        (t("16 · The Elemental Gauntlet", "16 · Der Elementarspießrutenlauf"),
         t("Each Climber takes an orb role: the one who burns, the one who breaks, the one who glides, the one who parts the water.",
           "Jeder Kletterer übernimmt eine Kugelrolle: einer brennt, einer bricht, einer gleitet, einer teilt das Wasser.")),
    ]
    room_rows = "".join(f"<tr><th scope='row'>{n}</th><td>{d}</td></tr>" for n, d in rooms)

    scale = [("1", "×1", "×1"), ("2", "×1.5", "×1.6"), ("3", "×2", "×2.2"), ("4", "×2.5", "×2.8")]
    scale_rows = "".join(f"<tr><th scope='row'>{p}</th><td>{e}</td><td>{b}</td></tr>" for p, e, b in scale)

    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("You are a Climber. You play your own Fortnite character, and K'in greets you the way she greets "
                      "everyone the temple lets in: climbing soul.",
                      "Du bist ein Kletterer. Du spielst deine eigene Fortnite-Figur, und K'in begrüßt dich so, wie sie "
                      "jeden begrüßt, den der Tempel einlässt: kletternde Seele.")}</p>
    <p>{t(f"The temple has always kept a record of the people it takes. The <a href='{u('characters/climbers/index.html')}'>Carved "
          "Climbers</a> on the Spirit Mural came before you. You are next.",
          f"Der Tempel hat schon immer festgehalten, wen er holt. Die <a href='{u('characters/climbers/index.html')}'>gemeißelten "
          "Kletterer</a> auf dem Geisterwandbild waren vor dir da. Du bist der Nächste.")}</p>
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, ctx.pick("MURAL-CLIMBERS", "HUB08"), t("Your likeness", "Dein Abbild"), t("Carved into the wall", "In die Wand gemeißelt"),
    t("<p>The first time a Climber dies, a new panel is cut into the Spirit Mural: a carved figure, your name in a glyph "
      "frame, and a sigil you choose from the four totem animals, jaguar, serpent, eagle or monkey.</p>"
      "<p>The panel grows with you. Every tier you clear adds a band to it, and the ending you reach can gild it. Everyone "
      "in the Threshold sees everyone else's panel, so the wall becomes a record of who has climbed how far.</p>",
      "<p>Wenn ein Kletterer zum ersten Mal stirbt, wird eine neue Tafel in das Geisterwandbild geschlagen: eine "
      "gemeißelte Gestalt, dein Name in einem Glyphenrahmen und ein Zeichen, das du aus den vier Totemtieren wählst, "
      "Jaguar, Schlange, Adler oder Affe.</p><p>Die Tafel wächst mit dir. Jede geschaffte Stufe fügt ein Band hinzu, und "
      "das Ende, das du erreichst, kann sie vergolden. Alle in der Schwelle sehen die Tafeln der anderen, so wird die Wand "
      "zu einem Verzeichnis, wer wie weit gekommen ist.</p>"))}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Kaya in the game", "Kaya im Spiel")}</p>
  <h2>{t("Beside you first, then at the wall", "Erst an deiner Seite, dann an der Wand")}</h2>
  <p class="lede-sm">{t(f"<a href='{u('characters/kaya.html')}'>Kaya</a> is no longer the one you play. She is the one you climb with, "
                        "and then the one you climb for.",
                        f"<a href='{u('characters/kaya.html')}'>Kaya</a> ist nicht mehr die Figur, die du spielst. Sie ist die, "
                        "mit der du kletterst, und dann die, für die du kletterst.")}</p>
  <ol class="loops loops-grid">{kaya_html}</ol>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Up to four", "Bis zu vier")}</p>
  <h2>{t("How a party climbs", "Wie eine Gruppe klettert")}</h2>
  <p class="lede-sm">{t("Every room can still be solved alone. Playing together only adds speed, or a second way through.",
                        "Jeder Raum bleibt allein lösbar. Gemeinsames Spielen bringt nur mehr Tempo oder einen zweiten Weg.")}</p>
  <div class="modes">{rule_html}</div>
</div></section>

<section class="wrap section">
  <p class="kicker">{t("Floor by floor", "Ebene für Ebene")}</p>
  <h2>{t("Rooms that play differently together", "Räume, die sich gemeinsam anders spielen")}</h2>
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Floor", "Ebene")}</th><th>{t("With a party", "Mit einer Gruppe")}</th></tr></thead>
    <tbody>{room_rows}</tbody>
  </table></div>
  <h3 class="sub-head">{t("Enemies grow with the party", "Gegner wachsen mit der Gruppe")}</h3>
  <div class="table-wrap"><table class="orb-table scale-table">
    <thead><tr><th>{t("Climbers", "Kletterer")}</th><th>{t("Enemies in a room", "Gegner im Raum")}</th><th>{t("Boss health", "Lebenspunkte der Bosse")}</th></tr></thead>
    <tbody>{scale_rows}</tbody>
  </table></div>
</section>
"""


PAGES = {
    "game/index.html": dict(
        title=("Overview & Pillars", "Überblick & Säulen"), kicker=("The Game", "Das Spiel"), banner="B-11",
        lede=("The flagship island: a co-op action-adventure platformer inside a living Mayan pyramid, for up to four players.",
              "Die Hauptinsel: ein Koop-Action-Adventure-Plattformer in einer lebenden Maya-Pyramide, für bis zu vier Spieler."),
        description=("What Ascent of the Sun Temple is, and the five design pillars behind it.",
                     "Was Ascent of the Sun Temple ist und welche fünf Design-Säulen dahinterstehen."),
        body=overview, og="B-11"),
    "game/how-it-plays.html": dict(
        title=("How It Plays", "So wird gespielt"), kicker=("The Game", "Das Spiel"), banner="B-05",
        lede=("Move, read, fight, solve. Then die, return to the Threshold, and climb again a little stronger.",
              "Bewegen, lesen, kämpfen, lösen. Dann sterben, an die Schwelle zurückkehren und etwas stärker erneut aufsteigen."),
        description=("Loops, traversal, traps, combat, puzzles, modes and collectibles.",
                     "Kreisläufe, Fortbewegung, Fallen, Kampf, Rätsel, Modi und Sammelobjekte."),
        body=how_it_plays, og="B-05"),
    "game/climbers-and-co-op.html": dict(
        title=("Climbers & Co-op", "Kletterer & Koop"), kicker=("The Game", "Das Spiel"),
        banner=["COOP-PARTY", "HUB08"],
        lede=("You play yourself, the temple carves you into its wall, and up to four Climbers go up together.",
              "Du spielst dich selbst, der Tempel meißelt dich in seine Wand, und bis zu vier Kletterer steigen gemeinsam auf."),
        description=("Playing as a Climber, the Spirit Mural likeness, Kaya's role and the co-op rules of the flagship.",
                     "Als Kletterer spielen, das Abbild auf dem Geisterwandbild, Kayas Rolle und die Koop-Regeln der Hauptinsel."),
        body=climbers, og=["COOP-PARTY", "HUB08"]),
    "game/weapons-and-powers.html": dict(
        title=("Weapons & Powers", "Waffen & Kräfte"), kicker=("The Game", "Das Spiel"), banner="T4B-SCENE",
        lede=("Four weapons, four permanent Elemental Orbs and the one Sun Orb that opens the summit.",
              "Vier Waffen, vier dauerhafte Elementarkugeln und die eine Sonnenkugel, die den Gipfel öffnet."),
        description=("The Climbers' weapons, the Elemental Orbs and the Sun Orb.",
                     "Die Waffen der Kletterer, die Elementarkugeln und die Sonnenkugel."),
        body=weapons, og="W05"),
}
