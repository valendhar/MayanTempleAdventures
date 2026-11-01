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
         t("The four Elemental Orbs and the upgrades bought in the Threshold stay with Kaya between runs, and each one opens routes that were closed before.",
           "Die vier Elementarkugeln und die in der Schwelle gekauften Verbesserungen bleiben Kaya über alle Durchläufe erhalten, und jede davon öffnet Wege, die vorher verschlossen waren.")),
        ("05", t("Never alone", "Nie allein"),
         t("K'in teaches, warns, foreshadows and remembers. She draws ghost paths after a missed jump, flickers before a trap fires and greets every return.",
           "K'in lehrt, warnt, deutet an und erinnert sich. Nach einem verpatzten Sprung zeichnet sie Geisterpfade, sie flackert, bevor eine Falle auslöst, und begrüßt jede Rückkehr.")),
    ]
    pillar_html = "".join(f'<li><span class="num">{n}</span><div><h3>{nm}</h3><p>{d}</p></div></li>' for n, nm, d in pillars)

    facts = [
        (t("Genre", "Genre"), t("Third-person action-adventure platformer with a roguelite climb",
                                "Third-Person-Action-Adventure-Plattformer mit Roguelite-Aufstieg")),
        (t("Planned engine", "Geplante Engine"), "Unreal Engine 5"),
        (t("Inspirations", "Vorbilder"), t("Ratchet &amp; Clank and Jak &amp; Daxter for tone; Hades for the return-and-grow loop",
                                          "Ratchet &amp; Clank und Jak &amp; Daxter für den Stil; Hades für den Kreislauf aus Rückkehr und Wachstum")),
        (t("Players", "Spieler"), t("Solo first. Every room has two arrival pads and wide corridors for 2-player co-op",
                                    "Zuerst solo. Jeder Raum hat zwei Ankunftsplattformen und breite Gänge für Koop zu zweit")),
        (t("Campaign", "Kampagne"), t("Floor 0, seventeen floors in six tiers, and the Sky Altar summit",
                                      "Ebene 0, siebzehn Ebenen in sechs Stufen und der Himmelsaltar auf dem Gipfel")),
        (t("Setting", "Schauplatz"), t("The interior of one living stepped pyramid, plus the jungle forecourt and the open summit",
                                       "Das Innere einer lebenden Stufenpyramide, dazu der Dschungelvorplatz und der offene Gipfel")),
    ]
    fact_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    q1, q2 = t("“", "„"), t("”", "“")
    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("Kaya, a young explorer, wakes K'in, the last spirit of an ancient Mayan sun temple, at its threshold. "
                        "The temple is alive: it rearranges itself and swallows everyone who climbs it.",
                        "Kaya, eine junge Entdeckerin, weckt an der Schwelle eines uralten Maya-Sonnentempels K'in, dessen letzten Geist. "
                        "Der Tempel lebt: Er ordnet sich ständig neu und verschlingt jeden, der ihn erklimmt.")}</p>
      <p>{t("Floor by floor she fights the risen guardians, survives the traps, solves the orb puzzles and earns the "
            "elemental powers the builders once held, until she carries the Sun Orb to the great portal on the summit and "
            "decides the temple's fate: restore the cycle, or break it.",
            "Ebene für Ebene kämpft sie gegen die erweckten Wächter, übersteht die Fallen, löst die Kugelrätsel und erringt die "
            "Elementarkräfte der Erbauer, bis sie die Sonnenkugel zum großen Portal auf dem Gipfel trägt und über das Schicksal "
            "des Tempels entscheidet: den Kreislauf wiederherstellen oder ihn durchbrechen.")}</p>
      <p>{t(f"The story explains the structure. The temple <em>{q1}rearranges itself to trap greedy adventurers{q2}</em>, so "
            "shuffled room layouts belong to the world rather than to a menu. And "
            f"<em>{q1}the cycle begins again… unless you break it{q2}</em>: when Kaya dies, K'in pulls her spirit back to the "
            "Threshold. What her spirit keeps between cycles, the Elemental Orbs and the fragments she has gathered, is what "
            "makes the next climb go further.",
            f"Die Geschichte erklärt die Struktur. Der Tempel <em>{q1}ordnet sich neu, um gierige Abenteurer in die Falle zu "
            f"locken{q2}</em>, also gehören wechselnde Raumabfolgen zur Welt und nicht zu einem Menü. Und "
            f"<em>{q1}der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn{q2}</em>: Stirbt Kaya, zieht K'in ihren "
            "Geist zurück an die Schwelle. Was ihr Geist von Kreislauf zu Kreislauf behält, die Elementarkugeln und die "
            "gesammelten Geistsplitter, bringt den nächsten Aufstieg weiter.")}</p>
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
    t("<p>Every climb begins at Kaya's camp at the foot of the pyramid: a canvas tent, a kettle on the fire, two straw "
      "training dummies and a carved target to practise on. Ahead, between two great feathered-serpent heads, the low "
      "tunnel leads into the Threshold.</p><p>The pyramid is always in view, so the summit is a goal you can see from "
      "the very first minute.</p>",
      "<p>Jeder Aufstieg beginnt in Kayas Lager am Fuß der Pyramide: ein Segeltuchzelt, ein Kessel über dem Feuer, zwei "
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
         t("Arrive on the twin pads, traverse and fight, solve the room's lock, and the exit gate opens to the next room.",
           "Auf den Zwillingsplattformen ankommen, durchqueren und kämpfen, das Schloss des Raums lösen, und das Ausgangstor öffnet sich zum nächsten Raum.")),
        (t("Floor", "Ebene"),
         t("Room A, then Room B with the floor's Key Orb, then the Portal Chamber: socket the orb, hear K'in's line, light a mural fragment, bank your coins and ascend.",
           "Raum A, dann Raum B mit der Schlüsselkugel der Ebene, dann die Portalkammer: Kugel einsetzen, K'ins Satz hören, ein Wandbildfragment entzünden, Münzen sichern und aufsteigen.")),
        (t("Run", "Durchlauf"),
         t("Leave the Threshold and climb. Death pulls Kaya's spirit back: most coins are lost, Spirit Fragments are kept. Or reach the summit.",
           "Die Schwelle verlassen und aufsteigen. Der Tod zieht Kayas Geist zurück: Die meisten Münzen gehen verloren, die Geistsplitter bleiben. Oder der Gipfel ist erreicht.")),
        (t("Meta", "Meta"),
         t("Spend fragments at the Threshold, unlock weapons and gear, fill the Spirit Mural, open tier shortcuts and claim the Elemental Orbs that reshape the climb.",
           "Splitter in der Schwelle ausgeben, Waffen und Ausrüstung freischalten, das Geisterwandbild füllen, Abkürzungen zu den Stufen öffnen und die Elementarkugeln erringen, die den Aufstieg verändern.")),
    ]
    loop_html = "".join(f'<li><span class="loop-label">{n}</span><p>{d}</p></li>' for n, d in loops)

    modes = [
        (t("The Ascent", "Der Aufstieg"), t("Story", "Story"),
         t("A fixed, hand-built room order. The first playthrough, with Floor 0 as the tutorial that teaches every core verb once.",
           "Eine feste, von Hand gebaute Raumfolge. Der erste Durchgang, mit Ebene 0 als Tutorial, das jede Kernaktion einmal beibringt.")),
        (t("Trials of the Shifting Temple", "Prüfungen des wandelnden Tempels"), t("Unlocked after the first summit", "Freigeschaltet nach dem ersten Gipfel"),
         t("Rooms shuffle within each tier while the tier order stays fixed. Stackable <em>Temple's Wrath</em> curses add tougher undead, faster traps, fewer checkpoints, roaming Guardian Spirits and timed floors, and each level earns better rewards.",
           "Innerhalb jeder Stufe werden die Räume gemischt, die Reihenfolge der Stufen bleibt fest. Stapelbare Flüche des <em>Zorns des Tempels</em> bringen zähere Untote, schnellere Fallen, weniger Checkpoints, umherstreifende Wächtergeister und Ebenen auf Zeit, und jede Stufe bringt bessere Belohnungen.")),
        (t("Expedition", "Expedition"), t("Replay", "Wiederholen"),
         t("Return to any cleared floor in its story layout with your full kit, to collect idols, earn medallions and open the orb-gated side routes.",
           "Kehre mit voller Ausrüstung in jede abgeschlossene Ebene in ihrer Story-Fassung zurück, um Idole zu sammeln, Medaillons zu verdienen und die durch Kugeln versperrten Nebenwege zu öffnen.")),
    ]
    mode_html = "".join(f'<article class="mode"><p class="kicker">{s}</p><h3>{n}</h3><p>{d}</p></article>' for n, s, d in modes)

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
      "lifts.</p><p>Every room hands Kaya one new idea, then the next room asks her to use it while something else is "
      "trying to kill her.</p>",
      "<p>Laufen, sprinten, springen, hochziehen, ducken und schwimmen, über Plattformen, die sich ständig ändern: "
      "gleitende Steinplatten, schwebende und schwingende Plattformen, Wippen, rotierende Kalenderscheiben, bröckelnde "
      "Böden, verschwindende Phasenstufen, Aufwinde und Aufzüge.</p><p>Jeder Raum gibt Kaya eine neue Idee an die Hand, "
      "und der nächste verlangt, dass sie sie anwendet, während etwas anderes versucht, sie umzubringen.</p>"))}
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
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Collectibles and economy", "Sammelobjekte und Wirtschaft")}</p>
  <h2>{t("What Kaya carries out of every room", "Was Kaya aus jedem Raum mitnimmt")}</h2>
  <div class="items">{collect_html}</div>
</div></section>
"""


# ------------------------------------------------------------------ weapons & powers
def weapons(ctx):
    u, t = ctx.url, ctx.t
    arms = [
        ("W01", t("Obsidian Macuahuitl", "Obsidian-Macuahuitl"), t("Melee · found on Floor 0", "Nahkampf · gefunden auf Ebene 0"),
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
  <h2>{t("An explorer's arsenal, found in the temple", "Das Arsenal einer Entdeckerin, gefunden im Tempel")}</h2>
  <p class="lede-sm">{t("Kaya enters as a scholar, not a warrior. Every weapon is a discovery, and each one changes what "
                        "she can reach as much as what she can fight.",
                        "Kaya betritt den Tempel als Gelehrte, nicht als Kriegerin. Jede Waffe ist eine Entdeckung und verändert, "
                        "was sie erreichen kann, ebenso sehr wie das, was sie bekämpfen kann.")}</p>
  <div class="items">{arm_html}</div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "W05", t("Permanent powers", "Dauerhafte Kräfte"), t("The four Elemental Orbs", "Die vier Elementarkugeln"),
    t("<p>The builders harnessed fire, earth, wind and water through four sacred orbs. Kaya claims them one by one in "
      "the Elemental Sanctums, and unlike everything else she gathers, they stay with her spirit through every death.</p>"
      "<p>Each orb is a traversal tool, a combat power and a key. Rooms that need an orb only enter the Trials room pool "
      "once she owns it, so the temple literally grows as she does.</p>",
      "<p>Die Erbauer bändigten Feuer, Erde, Wind und Wasser mit vier heiligen Kugeln. Kaya erringt sie nacheinander in "
      "den Elementarheiligtümern, und anders als alles andere, was sie sammelt, bleiben sie ihrem Geist über jeden Tod "
      "hinaus erhalten.</p><p>Jede Kugel ist Fortbewegungswerkzeug, Kampfkraft und Schlüssel zugleich. Räume, die eine "
      "Kugel erfordern, kommen erst in den Raumpool der Prüfungen, wenn Kaya sie besitzt; der Tempel wächst also "
      "buchstäblich mit ihr.</p>"))}
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
      f"Sun Portal and puts the final choice in Kaya's hands. <a href='{u('climb/sky-altar.html')}'>The summit →</a></p>",
      "<p>Das hellste Objekt im Spiel. Eine lodernde goldene Kugel mit einer lebendigen Sonnenglyphe im Kern, gehalten "
      "von vier geschnitzten Goldhänden mit roten, grünen, weißen und blauen Edelsteinen, einem für jedes Element.</p>"
      "<p>Sie wartet in einem versiegelten Gewölbe hinter dem Leutnant des Priesters auf Ebene 17. Zum Himmelsaltar "
      "getragen, öffnet sie das Sonnenportal und legt die letzte Entscheidung in Kayas Hände. "
      f"<a href='{u('climb/sky-altar.html')}'>Zum Gipfel →</a></p>"))}
  {feature(ctx, "P07", t("Puzzle energy", "Rätselenergie"), t("Energy Orbs", "Energiekugeln"),
    t("<p>The working orbs of every puzzle room: gold sun, blue water, red fire and green growth, each held in a "
      "gold-and-jade band. They can be carried, socketed and combined: pour sun into water and you get growth.</p>",
      "<p>Die Arbeitskugeln jedes Rätselraums: goldene Sonne, blaues Wasser, rotes Feuer und grünes Wachstum, jede in "
      "einem Band aus Gold und Jade gefasst. Sie lassen sich tragen, einsetzen und kombinieren: Gießt man Sonne in "
      "Wasser, entsteht Wachstum.</p>"), flip=True)}
</section>
"""


PAGES = {
    "game/index.html": dict(
        title=("Overview & Pillars", "Überblick & Säulen"), kicker=("The Game", "Das Spiel"), banner="B-11",
        lede=("A third-person action-adventure platformer inside a living Mayan pyramid, planned for Unreal Engine 5.",
              "Ein Third-Person-Action-Adventure-Plattformer in einer lebenden Maya-Pyramide, geplant für Unreal Engine 5."),
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
    "game/weapons-and-powers.html": dict(
        title=("Weapons & Powers", "Waffen & Kräfte"), kicker=("The Game", "Das Spiel"), banner="T4B-SCENE",
        lede=("Four weapons, four permanent Elemental Orbs and the one Sun Orb that opens the summit.",
              "Vier Waffen, vier dauerhafte Elementarkugeln und die eine Sonnenkugel, die den Gipfel öffnet."),
        description=("Kaya's weapons, the Elemental Orbs and the Sun Orb.",
                     "Kayas Waffen, die Elementarkugeln und die Sonnenkugel."),
        body=weapons, og="W05"),
}
