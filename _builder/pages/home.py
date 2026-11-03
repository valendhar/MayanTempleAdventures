"""Home page (English and German)."""


def body(ctx):
    u, t = ctx.url, ctx.t
    hero_style = ctx.bg("A-01")

    facts = [
        (t("Genre", "Genre"), t("Co-op action-adventure platformer", "Koop-Action-Adventure-Plattformer")),
        (t("Platform", "Plattform"), t("Fortnite islands, built in UEFN", "Fortnite-Inseln, gebaut im UEFN")),
        (t("Tone", "Stil"), "Ratchet &amp; Clank, Jak &amp; Daxter"),
        (t("Structure", "Aufbau"), t("The Shell, six tiers, then the summit", "The Shell, sechs Stufen, dann der Gipfel")),
        (t("Players", "Spieler"), t("1–4 co-op, as your own Fortnite character", "1–4 im Koop, als deine eigene Fortnite-Figur")),
        (t("Islands", "Inseln"), t("Five, all set in one temple", "Fünf, alle im selben Tempel")),
    ]
    fact_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in facts)

    pillars = [
        ("B-11", t("Ascend", "Aufsteigen"),
         t("Every run is a climb. The temple beneath you is progress made visible, floor by floor toward the summit.",
           "Jeder Durchlauf ist ein Aufstieg. Der Tempel unter dir macht den Fortschritt sichtbar, Ebene für Ebene bis zum Gipfel.")),
        ("B-10", t("Fight", "Kämpfen"),
         t("Melee and ranged combat against cursed priests and awakened creatures, with an obsidian macuahuitl in hand.",
           "Nah- und Fernkampf gegen verfluchte Priester und erwachte Kreaturen, mit einem Obsidian-Macuahuitl in der Hand.")),
        ("B-08", t("Solve", "Lösen"),
         t("Orb, plate, mirror and totem puzzles that grow deeper the higher you climb.",
           "Rätsel mit Kugeln, Druckplatten, Spiegeln und Totems, die immer anspruchsvoller werden, je höher du steigst.")),
        ("T4B-SCENE", t("Grow for good", "Dauerhaft wachsen"),
         t("The four Elemental Orbs and hub upgrades persist between runs, and your own carving on the Spirit Mural grows with every tier.",
           "Die vier Elementarkugeln und die Verbesserungen aus dem Hub bleiben über Durchläufe hinweg erhalten, und dein eigenes Relief auf dem Geisterwandbild wächst mit jeder Stufe.")),
        (ctx.pick("HOME-NEVERALONE", "W07"), t("Never alone", "Nie allein"),
         t("Climb with up to three friends, while K'in, the last spirit of the temple, teaches, warns and remembers.",
           "Kletter mit bis zu drei Freunden, während K'in, der letzte Geist des Tempels, lehrt, warnt und sich erinnert.")),
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

    # One card per Fortnite island, in build order (see pages/islands.py).
    islands = [
        ("islands/trap-galleries.html", ctx.pick("ISL-TRAPS", "T2A-SCENE"), "Trap Galleries", t("Deathrun · 1–16", "Deathrun · 1–16")),
        ("islands/ascent.html", ctx.pick("ISL-ASCENT", "KEYART"), "Ascent of the Sun Temple", t("Co-op adventure · 1–4", "Koop-Abenteuer · 1–4")),
        ("islands/kaan-expedition.html", ctx.pick("ISL-DIG", "A-04"), "Kaan Expedition", t("Tycoon · 1–8", "Tycoon · 1–8")),
        ("islands/illusion-depths.html", ctx.pick("ISL-DEPTHS", "T5A-SCENE"), "Illusion Depths", t("Co-op escape rooms · 2–4", "Koop-Escape-Rooms · 2–4")),
        ("islands/orb-raiders.html", ctx.pick("ISL-RAIDERS", "T4E-SCENE"), "Orb Raiders", t("PvPvE · 8–16", "PvPvE · 8–16")),
    ]
    island_html = "".join(
        f'<li><a class="island-card" href="{u(p)}">{ctx.figure(i, alt=n, link=False)}'
        f'<span class="island-num">{k + 1}</span><span class="island-name">{n}</span><span class="island-line">{g}</span></a></li>'
        for k, (p, i, n, g) in enumerate(islands))

    if ctx.has("KEYART"):
        alt = t("Mayan Temple Adventure: Ascent of the Sun Temple. Kaya and K'in at their jungle camp below the great stepped pyramid.",
                "Mayan Temple Adventure: Ascent of the Sun Temple. Kaya und K'in in ihrem Dschungellager unter der großen Stufenpyramide.")
        hero_art = (f'<div class="hero-art"><img src="{ctx.img_src("KEYART", "full")}" alt="{alt}" '
                    f'width="1672" height="941" fetchpriority="high"></div>')
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
      <p class="hero-sub">{t("Five Fortnite islands in one living temple, built in UEFN. At their heart, a co-op climb for up to four friends.",
                             "Fünf Fortnite-Inseln in einem lebenden Tempel, gebaut im UEFN. In ihrem Zentrum ein Koop-Aufstieg für bis zu vier Freunde.")}</p>
      <div class="cta-row">
        <a class="btn btn-gold" href="{u('climb/index.html')}">{t("Explore the climb", "Den Aufstieg erkunden")}</a>
        <a class="btn btn-ghost" href="{u('islands/index.html')}">{t("See the five islands", "Die fünf Inseln ansehen")}</a>
      </div>
    </div>
    <dl class="facts">{fact_html}</dl>
  </div>
</section>

<section class="wrap section intro">
  <h2 class="intro-title">{t("One temple. Eighteen floors. A spirit who has seen every climber fall.",
         "Ein Tempel. Achtzehn Ebenen. Ein Geist, der jeden Kletterer hat fallen sehen.")}</h2>
  <div class="intro-text">
    <p class="big">{t("You and up to three friends enter an ancient Mayan sun temple as Climbers, each in your own Fortnite "
                      "character. The temple is alive: it rearranges itself and swallows everyone who climbs it.",
                      "Du und bis zu drei Freunde betretet als Kletterer einen uralten Maya-Sonnentempel, jeder in seiner "
                      "eigenen Fortnite-Figur. Der Tempel lebt: Er ordnet sich ständig neu und verschlingt jeden, der ihn erklimmt.")}</p>
    <p>{t("Kaya, a young explorer, climbs the first floor with you and dies on its traps. She wakes at the Threshold to "
          "find herself carved into the temple's wall, and stays to read it. K'in, the temple's last spirit, guides you on. "
          "Floor by floor your party fights the risen guardians, survives the traps, solves the orb puzzles and earns the "
          "elemental powers the builders once held. Whoever falls is pulled back, and carved into the wall beside Kaya. At "
          "the summit you carry the Sun Orb to the great portal and decide the temple's fate together: restore the cycle, "
          "or break it.",
          "Kaya, eine junge Entdeckerin, steigt die erste Ebene mit euch hinauf und stirbt an ihren Fallen. Sie erwacht an "
          "der Schwelle, findet sich selbst in die Wand des Tempels gemeißelt und bleibt, um sie zu lesen. K'in, der letzte "
          "Geist des Tempels, führt euch weiter. Ebene für Ebene kämpft deine Gruppe gegen die erweckten Wächter, übersteht "
          "die Fallen, löst die Kugelrätsel und erringt die Elementarkräfte, die einst die Erbauer besaßen. Wer fällt, wird "
          "zurückgeholt und neben Kaya in die Wand gemeißelt. Auf dem Gipfel tragt ihr die Sonnenkugel zum großen Portal und "
          "entscheidet gemeinsam über das Schicksal des Tempels: den Kreislauf wiederherstellen oder ihn durchbrechen.")}</p>
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
    <h2>{t("One temple, five islands", "Ein Tempel, fünf Inseln")}</h2>
    <a class="text-link" href="{u('islands/index.html')}">{t("The islands and the roadmap", "Die Inseln und die Roadmap")}</a>
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
        description=("Mayan Temple Adventures: five Fortnite islands in a living Mayan pyramid, led by a co-op climb for up to four players.",
                     "Mayan Temple Adventures: fünf Fortnite-Inseln in einer lebenden Maya-Pyramide, angeführt von einem Koop-Aufstieg für bis zu vier Spieler."),
        body=body,
        custom_header=True,
        no_pager=True,
        og="KEYART",
    )
}
