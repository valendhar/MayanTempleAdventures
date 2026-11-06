"""Home page (English and German)."""


def body(ctx):
    u, t = ctx.url, ctx.t
    hero_style = ctx.bg("A-01")


    facts = [
        (t("Genre", "Genre"), t("Single-player action roguelite", "Action-Roguelite für einen Spieler")),
        (t("Engine", "Engine"), t("Built in Unreal Engine 5", "Gebaut in der Unreal Engine 5")),
        (t("You play", "Du spielst"), t("Kaya, a scholar who reads what kills her", "Kaya, eine Gelehrte, die liest, was sie tötet")),
        (t("The climb", "Der Aufstieg"), t("27 floors in six tiers, then the summit", "27 Ebenen in sechs Stufen, dann der Gipfel")),
        (t("A run", "Ein Durchlauf"), t("25 to 45 minutes, until you die or walk home", "25 bis 45 Minuten, bis du stirbst oder nach Hause gehst")),
        (t("Tone", "Stil"), "Ratchet &amp; Clank, Jak &amp; Daxter, Hades"),
    ]
    fact_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    pillars = [
        (ctx.pick("ACT-LENS", "HOME-ISABEL"), t("Read", "Lesen"),
         t("Kaya wins by understanding. Her goggles read enemies, traps, floors and walls, and what she learns is the one thing death can't take.",
           "Kaya gewinnt, indem sie versteht. Ihre Brille liest Gegner, Fallen, Böden und Wände, und was sie lernt, ist das Einzige, was ihr der Tod nicht nehmen kann.")),
        ("B-10", t("Fight", "Kämpfen"),
         t("Most chambers are fights against cursed priests and awakened creatures, and every trap in the room hurts them too.",
           "Die meisten Kammern sind Kämpfe gegen verfluchte Priester und erwachte Kreaturen, und jede Falle im Raum trifft auch sie.")),
        ("B-11", t("Ascend", "Aufsteigen"),
         t("Twenty-seven floors up one pyramid, with the summit in view from the first minute.",
           "Siebenundzwanzig Ebenen eine Pyramide hinauf, mit dem Gipfel im Blick von der ersten Minute an.")),
        (ctx.pick("ACT-RETURN", "A-03"), t("Return", "Zurückkehren"),
         t("Death moves the story. Every return brings a new line, a sale, a reading, a carving of whatever got you.",
           "Der Tod treibt die Geschichte voran. Jede Rückkehr bringt einen neuen Satz, einen Verkauf, eine Lesart, eine Schnitzerei von dem, was dich erwischt hat.")),
        (ctx.pick("HOME-NEVERALONE", "W07"), t("Never alone, never sure", "Nie allein, nie sicher"),
         t("K'in guides and warns, and she also edits the record. Oxlahun helps, and he also profits.",
           "K'in führt und warnt, und sie redigiert auch die Überlieferung. Oxlahun hilft, und er verdient auch daran.")),
    ]
    # All pillar pictures show as 16:9. HOME-NEVERALONE is 4:3, so it is cropped a little,
    # framed to keep both Kaya's head and boots and K'in's light in view.
    focus = {"HOME-NEVERALONE": "focus-35"}
    pillar_html = "".join(
        f'<li class="pillar">{ctx.figure(i, alt=n, link=False, cls=focus.get(i.upper(), ""))}<h3>{n}</h3><p>{d}</p></li>'
        for i, n, d in pillars)

    cast = [
        (ctx.pick("HOME-KAYA", "CS-KAYA"), "Kaya", t("The reader", "Die Leserin"), "characters/kaya.html"),
        (ctx.pick("HOME-KIN", "CS-KIN"), "K'in", t("The spirit guide", "Die Geistführerin"), "characters/kin.html"),
        (ctx.pick("HOME-OXLAHUN", "CS-OXLAHUN"), "Oxlahun", t("The trader", "Der Händler"), "characters/oxlahun.html"),
        (ctx.pick("HOME-PRIEST", "CS-PRIEST"), t("The Hollow High Priest", "Der Hohle Hohepriester"),
         t("The summit's keeper", "Der Hüter des Gipfels"), "characters/hollow-high-priest.html"),
    ]
    cast_html = "".join(
        f'<a class="portrait" href="{u(p)}">{ctx.figure(i, alt=n, link=False)}'
        f'<span class="portrait-text"><span class="portrait-name">{n}</span><span class="portrait-role">{r}</span></span></a>'
        for i, n, r, p in cast)

    # Listed summit first so the list reads top-down like the pyramid itself.
    tiers = [
        (t("Summit", "Gipfel"), t("The Sky Altar", "Der Himmelsaltar"),
         t("The cycle begins again… unless you break it.", "Der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn."),
         "climb/sky-altar.html"),
        (t("Tier VI", "Stufe VI"), t("The Ascension", "Die Erhebung"),
         t("A single orb chose memory over power.", "Eine einzige Kugel wählte die Erinnerung statt der Macht."), "climb/tier-6.html"),
        (t("Tier V", "Stufe V"), t("The Illusion Depths", "Die Tiefen der Täuschung"),
         t("The elements turned on one another.", "Die Elemente wandten sich gegeneinander."), "climb/tier-5.html"),
        (t("Tier IV", "Stufe IV"), t("The Elemental Sanctums", "Die Elementarheiligtümer"),
         t("The orbs scattered, and guardians were born.", "Die Kugeln zerstreuten sich, und Wächter wurden geboren."), "climb/tier-4.html"),
        (t("Tier III", "Stufe III"), t("The Shifting Vaults", "Die wandernden Gewölbe"),
         t("The temple learned to move, so no thief would find the same path twice.",
           "Der Tempel lernte, sich zu bewegen, damit kein Dieb denselben Weg zweimal findet."), "climb/tier-3.html"),
        (t("Tier II", "Stufe II"), t("The Trap Galleries", "Die Fallengalerien"),
         t("The first element betrayed them.", "Das erste Element verriet sie."), "climb/tier-2.html"),
        (t("Tier I", "Stufe I"), t("The Flooded Foundations", "Die überfluteten Fundamente"),
         t("The ancients harnessed balance.", "Die Alten bändigten das Gleichgewicht."), "climb/tier-1.html"),
        (t("Start", "Start"), "The Shell", "", "climb/floor-0.html"),
    ]
    first_line = t("Where every climb begins.", "Wo jeder Aufstieg beginnt.")
    oq, cq = t("“", "„"), t("”", "“")
    n_steps = len(tiers)
    # --i counts from the bottom step (0) up to the summit, for width and light-up order.
    tier_html = "".join(
        f'<li class="step{" step-summit" if k == 0 else ""}" style="--i:{n_steps - 1 - k}">'
        f'<a href="{u(p)}"><span class="step-num">{n}</span><span class="step-name">{nm}</span>'
        f'<span class="step-line">{(oq + l + cq) if l else first_line}</span></a></li>'
        for k, (n, nm, l, p) in enumerate(tiers))

    # Five floors unlike the rest of the climb. Each falls back to a picture that shows only Kaya until its own art exists.
    islands = [
        ("climb/tier-2.html#floor-6", ctx.pick("F6-SCENE", "T2A-SCENE"), t("The Builders' Workshop", "Die Werkstatt der Erbauer"), t("Build the traps, then run them", "Bau die Fallen, dann lauf hindurch")),
        ("climb/tier-2.html#floor-7", ctx.pick("HYB-SCENE1", "HYB-MAP"), t("The Breathing Court", "Der atmende Hof"), t("Freeze when the temple looks", "Erstarre, wenn der Tempel hinsieht")),
        ("climb/tier-3.html#floor-10", ctx.pick("CF-SCENE1", "T3B-SCENE"), t("The Counting Well", "Der zählende Brunnen"), t("The signs fall when K'in calls", "Die Zeichen fallen, wenn K'in ruft")),
        ("climb/tier-5.html#floor-20", ctx.pick("F20-TWIN", "T5C-SCENE"), t("The Hall of Lies", "Die Halle der Lügen"), t("Your Echo walks beside you", "Dein Echo geht neben dir")),
        ("climb/builders-ways.html", ctx.pick("LP1-S10", "T2E-SCENE"), t("The Builders' Ways", "Die Wege der Erbauer"), t("Secret side-view escape routes", "Geheime Fluchtwege in Seitenansicht")),
    ]
    island_html = "".join(
        f'<li><a class="island-card" href="{u(p)}">{ctx.figure(i, alt=n, link=False)}'
        f'<span class="island-num">{k + 1}</span><span class="island-name">{n}</span><span class="island-line">{g}</span></a></li>'
        for k, (p, i, n, g) in enumerate(islands))

    if ctx.has("KEYART"):
        alt = t("Kaya and K'in at their jungle camp below the great stepped pyramid.",
                "Kaya und K'in in ihrem Dschungellager unter der großen Stufenpyramide.")
        # The title logo is its own layer over the painting, so it stays sharp and can move per screen size.
        logo = ""
        if ctx.has("TITLE-LOCKUP"):
            logo = (f'<h1 class="hero-logo"><img src="{ctx.img_src("TITLE-LOCKUP", "full")}" alt="Mayan Temple Adventures: Ascent of the Sun Temple" '
                    f'fetchpriority="high"></h1>')
        hero_art = (f'<div class="hero-art"><img class="hero-painting" src="{ctx.img_src("KEYART", "full")}" alt="{alt}" '
                    f'width="1672" height="941" fetchpriority="high">{logo}</div>')
        hero_title = ""
    else:
        hero_art = f'<div class="hero-art hero-art-bg" style="{hero_style}"></div>'
        hero_title = '<h1 class="hero-title">Mayan Temple Adventures</h1>'

    return f"""
<section class="hero">
  {hero_art}
  <div class="wrap hero-panel">
    <div class="hero-copy">
      {hero_title}
      <p class="hero-hook">{t("A Mayan pyramid that rearranges itself around you.", "Eine Maya-Pyramide, die sich um dich herum neu ordnet.")}</p>
      <p class="hero-sub">{t("Climb it, die in it, wake up and go back knowing more. A single-player action roguelite, built in Unreal Engine 5.",
                             "Erklimm sie, stirb in ihr, wach auf und steig mit mehr Wissen wieder hinauf. Ein Action-Roguelite für einen Spieler, gebaut in der Unreal Engine 5.")}</p>
      <div class="cta-row">
        <a class="btn btn-gold" href="{u('climb/index.html')}">{t("Explore the climb", "Den Aufstieg erkunden")}</a>
        <a class="btn btn-ghost" href="{u('game/how-it-plays.html')}">{t("How it plays", "So wird gespielt")}</a>
      </div>
    </div>
    <dl class="facts">{fact_html}</dl>
  </div>
</section>

<section class="wrap section intro">
  <h2 class="intro-title">{t("One temple. Twenty-seven floors. A spirit who has seen every climber fall.",
         "Ein Tempel. Siebenundzwanzig Ebenen. Ein Geist, der jeden Kletterer hat fallen sehen.")}</h2>
  <div class="intro-text">
    <p class="big">{t("You are Kaya, a young scholar looking for her missing mother. The Sun Temple is alive: it rearranges itself and swallows everyone who climbs it.",
                      "Du bist Kaya, eine junge Gelehrte auf der Suche nach ihrer verschwundenen Mutter. Der Sonnentempel lebt: Er ordnet sich ständig neu und verschlingt jeden, der ihn erklimmt.")}</p>
    <p>{t("On your first morning it kills you. You wake at the Threshold, unhurt, to find yourself freshly carved into the temple's wall, and K'in, its last spirit, "
          "greets you as if nothing happened. So you go back. Floor by floor you fight the risen guardians, turn the traps on them, read what's written on the walls and earn the "
          "elemental powers the builders once held. Oxlahun buys what you carry out and pours the tea. Each time you fall, you come back knowing more. At the summit you carry "
          "the Sun Orb to the great portal and decide the temple's fate: restore the cycle, or break it.",
          "An deinem ersten Morgen tötet er dich. Du erwachst unversehrt an der Schwelle und findest dich frisch in die Wand des Tempels gemeißelt, und K'in, sein letzter Geist, "
          "begrüßt dich, als wäre nichts geschehen. Also gehst du zurück. Ebene für Ebene kämpfst du gegen die erweckten Wächter, richtest die Fallen gegen sie, liest, was an den Wänden "
          "steht, und erringst die Elementarkräfte, die einst die Erbauer besaßen. Oxlahun kauft, was du heraustragst, und gießt den Tee ein. Jedes Mal, wenn du fällst, kommst du mit mehr "
          "Wissen zurück. Auf dem Gipfel trägst du die Sonnenkugel zum großen Portal und entscheidest über das Schicksal des Tempels: den Kreislauf wiederherstellen oder ihn durchbrechen.")}</p>
    <a class="text-link" href="{u('game/index.html')}">{t("Read the full overview", "Zum vollständigen Überblick")}</a>
  </div>
</section>

<section class="sunlit">
  <div class="wrap section">
    <h2>{t("Five ideas hold up the whole climb", "Fünf Ideen tragen den ganzen Aufstieg")}</h2>
    <ul class="pillars">{pillar_html}</ul>
  </div>
</section>

<section class="wrap section islands-band">
  <div class="section-head">
    <h2>{t("Floors unlike the rest", "Ebenen wie keine anderen")}</h2>
    <a class="text-link" href="{u('climb/index.html')}">{t("All 27 floors", "Alle 27 Ebenen")}</a>
  </div>
  <ol class="island-grid">{island_html}</ol>
</section>

<section class="wrap section split">
  <div class="split-media">{ctx.figure("A-03", alt=t("The Threshold, the base hall of the temple", "Die Schwelle, die Grundhalle des Tempels"))}</div>
  <div class="split-text">
    <h2>{t("One element broke the balance", "Ein Element zerbrach das Gleichgewicht")}</h2>
    <p>{t("Long ago the temple's builders harnessed fire, earth, wind and water through sacred orbs and lived in balance, "
          "until one element betrayed the rest. The balance shattered, the priests were cursed into undeath, the orbs "
          "scattered up through the floors and the temple sealed itself into an endless cycle.",
          "Vor langer Zeit bändigten die Erbauer des Tempels Feuer, Erde, Wind und Wasser mithilfe heiliger Kugeln und lebten "
          "im Gleichgewicht, bis ein Element die anderen verriet. Das Gleichgewicht zerbrach, die Priester wurden zu Untoten "
          "verflucht, die Kugeln verstreuten sich über alle Ebenen, und der Tempel versiegelte sich in einem endlosen Kreislauf.")}</p>
    <p>{t("Every climb starts in the Threshold, the vast base hall where K'in waits above the round altar, three portals "
          "stand beneath the Spirit Mural, and a trader named Oxlahun keeps an offering table. Anyone who dies inside the "
          "temple wakes here again. The mural keeps a record of each of them.",
          "Jeder Aufstieg beginnt in der Schwelle, der gewaltigen Grundhalle: K'in schwebt über dem runden Altar, drei Portale "
          "stehen unter dem Geisterwandbild, und ein Händler namens Oxlahun betreibt einen Opfertisch. Wer im Tempel stirbt, "
          "erwacht hier von Neuem. Das Wandbild hält jeden von ihnen fest.")}</p>
    <a class="text-link" href="{u('world/index.html')}">{t("Enter the world", "Die Welt betreten")}</a>
  </div>
</section>

<section class="cast-band">
  <div class="wrap section">
    <div class="section-head">
      <h2>{t("Who waits inside", "Wer drinnen wartet")}</h2>
      <a class="text-link" href="{u('characters/index.html')}">{t("See the full cast", "Alle Figuren ansehen")}</a>
    </div>
    <div class="cast">{cast_html}</div>
  </div>
</section>

<section class="ascent-band">
  <div class="wrap section">
    <div class="ascent-head">
      <div>
        <h2>{t("Floor by floor to the sun", "Ebene für Ebene zur Sonne")}</h2>
        <p>{t("Each tier ends in a Portal Chamber, where a fragment of the mural and one line from K'in reveal the next piece "
              "of the temple's history.",
              "Jede Stufe endet in einer Portalkammer, wo ein Fragment des Wandbilds und ein Satz von K'in das nächste Stück "
              "der Tempelgeschichte enthüllen.")}</p>
      </div>
      {ctx.figure(ctx.pick("HOME-CLIMB", "CX-00"), alt=t("The pyramid and its six tiers", "Die Pyramide und ihre sechs Stufen"), cls="ascent-map")}
    </div>
    <ol class="ascent">{tier_html}</ol>
  </div>
</section>

<section class="story-band">
  <div class="wrap section story-inner">
    <h2>{t("The Likeness", "Das Abbild")}</h2>
    <p class="story-note">{t("A short story, in progress", "Eine Kurzgeschichte, in Arbeit")}</p>
    <p class="story-quote">{t("Kaya dies on her very first trap and wakes at the Threshold to find her own likeness freshly "
                              "carved into the Spirit Mural, beside a panel that contradicts everything the temple's spirit guide has told her.",
                              "Kaya stirbt schon an der allerersten Falle und erwacht an der Schwelle. Dort findet sie ihr eigenes Abbild, "
                              "frisch in das Geisterwandbild gemeißelt, neben einer Tafel, die allem widerspricht, was ihr die Geistführerin des Tempels erzählt hat.")}</p>
    <a class="btn btn-ghost" href="{u('story/short-story.html')}">{t("About the story", "Über die Geschichte")}</a>
  </div>
</section>
"""


PAGES = {
    "index.html": dict(
        title=("Home", "Start"),
        description=("Ascent of the Sun Temple: a single-player action roguelite in a living Mayan pyramid, built in Unreal Engine 5.",
                     "Ascent of the Sun Temple: ein Action-Roguelite für einen Spieler in einer lebenden Maya-Pyramide, gebaut in der Unreal Engine 5."),
        body=body,
        custom_header=True,
        no_pager=True,
        og=["KEYART-SHARE", "KEYART"],
    )
}
