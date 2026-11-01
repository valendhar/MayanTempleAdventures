"""Home page (English and German)."""


def body(ctx):
    u, t = ctx.url, ctx.t
    hero_style = ctx.bg("A-01")

    facts = [
        (t("Genre", "Genre"), t("Third-person action-adventure platformer", "Third-Person-Action-Adventure-Plattformer")),
        (t("Planned engine", "Geplante Engine"), "Unreal Engine 5"),
        (t("Tone", "Stil"), "Ratchet &amp; Clank, Jak &amp; Daxter"),
        (t("Structure", "Aufbau"), t("Floor 0, six tiers, then the summit", "Ebene 0, sechs Stufen, dann der Gipfel")),
        (t("Players", "Spieler"), t("Solo, with 2-player co-op rooms", "Solo, mit Koop-Räumen für 2 Spieler")),
        (t("Stage", "Stand"), t("World, story and art direction in design", "Welt, Geschichte und Art Direction in Ausarbeitung")),
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
         t("The four Elemental Orbs and hub upgrades persist between runs and reshape what you can reach.",
           "Die vier Elementarkugeln und die Verbesserungen aus dem Hub bleiben über Durchläufe hinweg erhalten und öffnen neue Wege.")),
        (ctx.pick("HOME-NEVERALONE", "W07"), t("Never alone", "Nie allein"),
         t("K'in, the last spirit of the temple, teaches, warns, foreshadows and remembers.",
           "K'in, der letzte Geist des Tempels, lehrt, warnt, deutet an und erinnert sich.")),
    ]
    pillar_html = "".join(
        f'<article class="pillar">{ctx.figure(i, alt=n)}<h3>{n}</h3><p>{d}</p></article>'
        for i, n, d in pillars)

    cast = [
        (ctx.pick("HOME-KAYA", "CS-KAYA"), "Kaya", t("The explorer", "Die Entdeckerin"), "characters/kaya.html"),
        (ctx.pick("HOME-KIN", "CS-KIN"), "K'in", t("The spirit guide", "Die Geistführerin"), "characters/kin.html"),
        (ctx.pick("HOME-OXLAHUN", "CS-OXLAHUN"), "Oxlahun", t("The trader", "Der Händler"), "characters/oxlahun.html"),
        (ctx.pick("HOME-PRIEST", "CS-PRIEST"), t("The Hollow High Priest", "Der Hohle Hohepriester"),
         t("The summit's keeper", "Der Hüter des Gipfels"), "characters/hollow-high-priest.html"),
    ]
    cast_html = "".join(
        f'<a class="card" href="{u(p)}">{ctx.figure(i, alt=n, link=False)}<span class="card-body">'
        f'<span class="card-kicker">{r}</span><span class="card-title">{n}</span></span></a>'
        for i, n, r, p in cast)

    tiers = [
        (t("Floor 0", "Ebene 0"), t("The Initiation", "Die Einweihung"), "", "climb/floor-0.html"),
        (t("Tier I", "Stufe I"), t("The Flooded Foundations", "Die überfluteten Fundamente"),
         t("The ancients harnessed balance.", "Die Alten bändigten das Gleichgewicht."), "climb/tier-1.html"),
        (t("Tier II", "Stufe II"), t("The Trap Galleries", "Die Fallengalerien"),
         t("The first element betrayed them.", "Das erste Element verriet sie."), "climb/tier-2.html"),
        (t("Tier III", "Stufe III"), t("The Shifting Vaults", "Die wandernden Gewölbe"),
         t("The temple learned to move, so no thief would find the same path twice.",
           "Der Tempel lernte, sich zu bewegen, damit kein Dieb denselben Weg zweimal findet."), "climb/tier-3.html"),
        (t("Tier IV", "Stufe IV"), t("The Elemental Sanctums", "Die Elementarheiligtümer"),
         t("The orbs scattered, and guardians were born.", "Die Kugeln zerstreuten sich, und Wächter wurden geboren."), "climb/tier-4.html"),
        (t("Tier V", "Stufe V"), t("The Illusion Depths", "Die Tiefen der Täuschung"),
         t("The elements turned on one another.", "Die Elemente wandten sich gegeneinander."), "climb/tier-5.html"),
        (t("Tier VI", "Stufe VI"), t("The Ascension", "Die Erhebung"),
         t("A single orb chose memory over power.", "Eine einzige Kugel wählte die Erinnerung statt der Macht."), "climb/tier-6.html"),
        (t("Summit", "Gipfel"), t("The Sky Altar", "Der Himmelsaltar"),
         t("The cycle begins again… unless you break it.", "Der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn."),
         "climb/sky-altar.html"),
    ]
    first_line = t("Where every climb begins.", "Wo jeder Aufstieg beginnt.")
    tier_html = "".join(
        f'<li><a href="{u(p)}"><span class="t-num">{n}</span><span class="t-name">{nm}</span>'
        + (f'<span class="t-line">{t("“", "„")}{l}{t("”", "“")}</span>' if l else f'<span class="t-line">{first_line}</span>')
        + "</a></li>"
        for n, nm, l, p in tiers)

    if ctx.has("KEYART"):
        alt = t("Mayan Temple Adventure: Ascent of the Sun Temple. Kaya and K'in at their jungle camp below the great stepped pyramid.",
                "Mayan Temple Adventure: Ascent of the Sun Temple. Kaya und K'in in ihrem Dschungellager unter der großen Stufenpyramide.")
        hero_top = (f'<section class="hero hero-art"><div class="hero-art-frame">'
                    f'<img src="{ctx.img_src("KEYART", "full")}" alt="{alt}" fetchpriority="high"></div>'
                    f'<div class="wrap hero-inner">')
    else:
        hero_top = (f'<section class="hero" style="{hero_style}"><div class="hero-shade"></div>'
                    f'<div class="wrap hero-inner"><h1 class="hero-title">Ascent of the<br><span>Sun Temple</span></h1>')

    return f"""
{hero_top}
    <p class="hero-hook">{t("A Mayan pyramid that rearranges itself around you.", "Eine Maya-Pyramide, die sich um dich herum neu ordnet.")}</p>
    <p class="hero-sub">{t("A third-person action-adventure platformer, planned for Unreal Engine 5.",
                           "Ein Third-Person-Action-Adventure-Plattformer, geplant für Unreal Engine 5.")}</p>
    <div class="cta-row">
      <a class="btn btn-gold" href="{u('climb/index.html')}">{t("Explore the climb", "Den Aufstieg erkunden")}</a>
      <a class="btn btn-ghost" href="{u('characters/index.html')}">{t("Meet the cast", "Die Figuren kennenlernen")}</a>
    </div>
  </div>
</section>

<section class="wrap section intro">
  <div class="intro-text">
    <p class="kicker">{t("The game", "Das Spiel")}</p>
    <h2>{t("One temple. Eighteen floors. A spirit who has seen every climber fall.",
           "Ein Tempel. Achtzehn Ebenen. Ein Geist, der jeden Kletterer hat fallen sehen.")}</h2>
    <p class="big">{t("Kaya, a young explorer, wakes K'in, the last spirit of an ancient Mayan sun temple, at its threshold. "
                      "The temple is alive: it rearranges itself and swallows everyone who climbs it.",
                      "Kaya, eine junge Entdeckerin, weckt an der Schwelle eines uralten Maya-Sonnentempels K'in, dessen letzten Geist. "
                      "Der Tempel lebt: Er ordnet sich ständig neu und verschlingt jeden, der ihn erklimmt.")}</p>
    <p>{t("Floor by floor she fights the risen guardians, survives the traps, solves the orb puzzles and earns the "
          "elemental powers the builders once held. When she dies, the temple pulls her back to the Threshold, and she climbs "
          "again a little wiser. At the summit she carries the Sun Orb to the great portal and decides the temple's fate: "
          "restore the cycle, or break it.",
          "Ebene für Ebene kämpft sie gegen die erweckten Wächter, übersteht die Fallen, löst die Kugelrätsel und erringt die "
          "Elementarkräfte, die einst die Erbauer besaßen. Stirbt sie, zieht der Tempel sie zurück an die Schwelle, und sie "
          "steigt erneut auf, ein wenig klüger als zuvor. Auf dem Gipfel trägt sie die Sonnenkugel zum großen Portal und "
          "entscheidet über das Schicksal des Tempels: den Kreislauf wiederherstellen oder ihn durchbrechen.")}</p>
    <a class="text-link" href="{u('game/index.html')}">{t("Read the full overview →", "Zum vollständigen Überblick →")}</a>
  </div>
  <dl class="facts">{fact_html}</dl>
</section>

<section class="band">
  <div class="wrap section">
    <p class="kicker">{t("Design pillars", "Design-Säulen")}</p>
    <h2>{t("Five ideas hold up the whole climb", "Fünf Ideen tragen den ganzen Aufstieg")}</h2>
    <div class="pillars">{pillar_html}</div>
  </div>
</section>

<section class="wrap section split">
  <div class="split-media">{ctx.figure("A-03", alt=t("The Threshold, the base hall of the temple", "Die Schwelle, die Grundhalle des Tempels"))}</div>
  <div class="split-text">
    <p class="kicker">{t("The world", "Die Welt")}</p>
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
    <a class="text-link" href="{u('world/index.html')}">{t("Enter the world →", "Die Welt betreten →")}</a>
  </div>
</section>

<section class="band">
  <div class="wrap section">
    <div class="section-head">
      <div><p class="kicker">{t("Characters", "Figuren")}</p><h2>{t("Who waits inside", "Wer drinnen wartet")}</h2></div>
      <a class="text-link" href="{u('characters/index.html')}">{t("The full cast →", "Alle Figuren →")}</a>
    </div>
    <div class="cards cards-4">{cast_html}</div>
  </div>
</section>

<section class="wrap section climb">
  <div class="climb-map">{ctx.figure(ctx.pick("HOME-CLIMB", "CX-00"), alt=t("The pyramid and its six tiers", "Die Pyramide und ihre sechs Stufen"))}</div>
  <div class="climb-list">
    <p class="kicker">{t("The climb", "Der Aufstieg")}</p>
    <h2>{t("Floor by floor to the sun", "Ebene für Ebene zur Sonne")}</h2>
    <p>{t("Each tier ends in a Portal Chamber, where a fragment of the mural and one line from K'in reveal the next piece "
          "of the temple's history.",
          "Jede Stufe endet in einer Portalkammer, wo ein Fragment des Wandbilds und ein Satz von K'in das nächste Stück "
          "der Tempelgeschichte enthüllen.")}</p>
    <ol class="tiers">{tier_html}</ol>
  </div>
</section>

<section class="story-band">
  <div class="wrap section story-inner">
    <p class="kicker">{t("Short story · in progress", "Kurzgeschichte · in Arbeit")}</p>
    <h2>{t("The Likeness", "Das Abbild")}</h2>
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
        description=("Ascent of the Sun Temple: a third-person action-adventure platformer inside a living Mayan pyramid, planned for Unreal Engine 5.",
                     "Ascent of the Sun Temple: ein Third-Person-Action-Adventure-Plattformer in einer lebenden Maya-Pyramide, geplant für Unreal Engine 5."),
        body=body,
        custom_header=True,
        no_pager=True,
        og="KEYART",
    )
}
