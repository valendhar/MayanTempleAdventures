"""Story tab: The Story, Lore & History, The Short Story (English and German)."""
from components import feature, facts


# ------------------------------------------------------------------ the story
def story(ctx):
    u, t = ctx.url, ctx.t
    lines = [
        (t("Tier I", "Stufe I"), t("The Flooded Foundations", "Die überfluteten Fundamente"),
         t("The ancients harnessed balance.", "Die Alten bändigten das Gleichgewicht.")),
        (t("Tier II", "Stufe II"), t("The Trap Galleries", "Die Fallengalerien"),
         t("The first element betrayed them.", "Das erste Element verriet sie.")),
        (t("Tier III", "Stufe III"), t("The Shifting Vaults", "Die wandernden Gewölbe"),
         t("The temple learned to move, so no thief would find the same path twice.",
           "Der Tempel lernte, sich zu bewegen, damit kein Dieb denselben Weg zweimal findet.")),
        (t("Tier IV", "Stufe IV"), t("The Elemental Sanctums", "Die Elementarheiligtümer"),
         t("The orbs scattered, and guardians were born.", "Die Kugeln zerstreuten sich, und Wächter wurden geboren.")),
        (t("Tier V", "Stufe V"), t("The Illusion Depths", "Die Tiefen der Täuschung"),
         t("The elements turned on one another.", "Die Elemente wandten sich gegeneinander.")),
        (t("Tier VI", "Stufe VI"), t("The Ascension", "Die Erhebung"),
         t("A single orb chose memory over power.", "Eine einzige Kugel wählte die Erinnerung statt der Macht.")),
        (t("Summit", "Gipfel"), t("The Sky Altar", "Der Himmelsaltar"),
         t("The cycle begins again… unless you break it.", "Der Kreislauf beginnt von vorn … es sei denn, du durchbrichst ihn.")),
    ]
    q = t("“", "„")
    line_html = "".join(
        f'<li><div class="row"><span class="t-num">{n}</span><span class="t-name">{nm}</span>'
        f'<span class="t-line">{q}{l}{t("”", "“")}</span></div></li>' for n, nm, l in lines)

    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("Kaya came to the Sun Temple with a field notebook, a satchel of brushes and charcoal, and one purpose: to prove her mother right.",
                      "Kaya kam mit einem Feldnotizbuch, einer Tasche voller Pinsel und Kohle und einem einzigen Ziel zum Sonnentempel: zu beweisen, dass ihre Mutter recht hatte.")}</p>
    <p>{t("Her mother, the epigrapher Dr. Isabel Kaan, spent years arguing that the great mural in the temple's base hall records a "
          "betrayal the builders deliberately hid. Her colleagues laughed her out of the field. Kaya wakes K'in, the last spirit of "
          "the temple, climbs onto the first floor, and dies in a corridor of rising spikes within the hour.",
          "Ihre Mutter, die Epigraphikerin Dr. Isabel Kaan, vertrat jahrelang die These, dass das große Wandbild in der Grundhalle des "
          "Tempels einen Verrat festhält, den die Erbauer absichtlich verborgen haben. Ihre Kollegen lachten sie aus dem Fach. Kaya weckt "
          "K'in, den letzten Geist des Tempels, steigt auf die erste Ebene und stirbt keine Stunde später in einem Gang voller "
          "hochschnellender Stacheln.")}</p>
    <p>{t("She wakes on the stone floor of the Threshold, exactly where she started, and K'in greets her as though nothing is wrong.",
          "Sie erwacht auf dem Steinboden der Schwelle, genau dort, wo sie begonnen hat, und K'in begrüßt sie, als wäre nichts geschehen.")}</p>
    <p>{t("In the game, you are Kaya. Each death brings you back to that floor, and each return, the wall has changed. You read it, you climb for the evidence, and the story moves forward every time the temple kills you.",
          "Im Spiel bist du Kaya. Jeder Tod bringt dich auf diesen Boden zurück, und bei jeder Rückkehr hat sich die Wand verändert. Du liest sie, du kletterst nach den Beweisen, und die Geschichte geht jedes Mal weiter, wenn der Tempel dich tötet.")}</p>
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "B-07", t("The first death", "Der erste Tod"), t("The temple does not forget", "Der Tempel vergisst nicht"),
    t("<p>Anyone who dies inside the temple wakes again in the Threshold with their memories intact. Death is not erased, it is "
      "recorded: the mural gains a likeness of every climber, and tally marks gather in the margin of an old codex.</p>"
      "<p>Every return is a second chance for the climber, and another entry in the temple's archive.</p>",
      "<p>Wer im Tempel stirbt, erwacht mit allen Erinnerungen wieder in der Schwelle. Der Tod wird nicht ausgelöscht, er wird "
      "aufgezeichnet: Das Wandbild erhält ein Abbild jedes Kletterers, und am Rand eines alten Codex sammeln sich Strichlisten.</p>"
      "<p>Jede Rückkehr ist eine zweite Chance für den Kletterer und ein weiterer Eintrag im Archiv des Tempels.</p>"))}
  {feature(ctx, "HUB09", t("The likeness", "Das Abbild"), t("A carving she never made", "Ein Relief, das sie nie gemeißelt hat"),
    t("<p>On the Spirit Mural, in pale limestone still dusted with fresh chips, a new figure has appeared: a slender young woman "
      "with twin braids, a satchel on her left hip and goggles pushed up on her forehead.</p>"
      "<p>Beside it stand older carvings of the climbers who came before her: a surveyor with a notched staff, a woman with a coil of "
      "rope, a young man with a lantern, a small figure with a satchel much like Kaya's, and one carving that was never finished. "
      "The wall is not finished either: her carving changes every time she falls. "
      f"<a href='{u('characters/climbers/index.html')}'>Meet the Carved Climbers →</a></p>",
      "<p>Auf dem Geisterwandbild ist in hellem Kalkstein, noch bestäubt von frischen Splittern, eine neue Figur erschienen: eine "
      "schlanke junge Frau mit zwei Zöpfen, einer Tasche an der linken Hüfte und einer hochgeschobenen Schutzbrille auf der Stirn.</p>"
      "<p>Daneben stehen ältere Reliefs der Kletterer, die vor ihr kamen: ein Landvermesser mit gekerbtem Messstab, eine Frau mit "
      "einem Seil über der Schulter, ein junger Mann mit einer Laterne, eine kleine Gestalt mit einer Tasche, die Kayas sehr ähnlich "
      "sieht, und ein Relief, das nie vollendet wurde. Auch die Wand ist nicht vollendet: Ihr Relief verändert sich jedes Mal, wenn sie fällt. "
      f"<a href='{u('characters/climbers/index.html')}'>Zu den gemeißelten Kletterern →</a></p>"),
    flip=True)}
  {feature(ctx, "HOME-NEVERALONE", t("The guide", "Die Führerin"), t("A spirit who edits history", "Ein Geist, der Geschichte umschreibt"),
    t("<p>K'in is gentle, patient and indispensable. She lights the way, warns of traps and pulls Kaya's spirit back after every fall. "
      "She also tells the temple's history in short, memorable lines, and the oldest glyphs on the wall do not always agree with her.</p>"
      "<p>You have to decide how much of K'in's account to carry, and whether to keep climbing with a guide no one can fully trust.</p>",
      "<p>K'in ist sanft, geduldig und unverzichtbar. Sie weist den Weg, warnt vor Fallen und holt Kayas Geist nach jedem Sturz zurück. "
      "Sie erzählt auch die Geschichte des Tempels in kurzen, einprägsamen Sätzen, und die ältesten Glyphen an der Wand stimmen nicht "
      "immer mit ihr überein.</p><p>Du musst entscheiden, wie viel von K'ins Version du mit dir tragen willst und ob du mit einer Führerin weiterkletterst, der niemand ganz vertrauen kann.</p>"))}
</div></section>

<section class="wrap section">
  <p class="kicker">{t("The mural mystery", "Das Rätsel des Wandbilds")}</p>
  <h2>{t("Two readings of every fragment", "Zwei Lesarten jedes Fragments")}</h2>
  <p class="lede-sm">{t("The wall is evidence. At every Portal Chamber, Kaya takes a rubbing of the fragment that lights up "
                        "and carries it home. K'in has already told her what it means. At the reading desk you find out what the glyphs "
                        "actually say, and the two do not always agree.",
                        "Die Wand ist ein Beweisstück. In jeder Portalkammer nimmt Kaya einen Abrieb des Fragments, das "
                        "aufleuchtet, und trägt ihn nach Hause. K'in hat ihr schon gesagt, was es bedeutet. Am Lesepult findest du heraus, "
                        "was die Glyphen wirklich sagen, und beides stimmt nicht immer überein.")}</p>
  <div class="modes">
    <article class="mode"><p class="kicker">{t("At every Portal Chamber", "In jeder Portalkammer")}</p>
      <h3>{t("K'in's version", "K'ins Version")}</h3>
      <p>{t("One line of history, spoken over the fragment. Short, memorable, and the version the temple wants told.",
            "Ein Satz Geschichte, über dem Fragment gesprochen. Kurz, einprägsam und die Fassung, die der Tempel erzählt haben will.")}</p></article>
    <article class="mode"><p class="kicker">{t("Back at the Threshold", "Zurück an der Schwelle")}</p>
      <h3>{t("Kaya's reading", "Kayas Lesart")}</h3>
      <p>{t("What the carving says when someone reads it slowly, twice. The codex keeps both versions side by side.",
            "Was das Relief sagt, wenn jemand es langsam liest, zweimal. Der Codex hält beide Fassungen nebeneinander fest.")}</p></article>
    <article class="mode"><p class="kicker">{t("On the way up", "Auf dem Weg nach oben")}</p>
      <h3>{t("Things that don't fit", "Dinge, die nicht passen")}</h3>
      <p>{t("Now and then you find something in the stone that nobody mentioned. What it is, you find out for yourself.",
            "Hin und wieder findest du im Stein etwas, das niemand erwähnt hat. Was es ist, findest du selbst heraus.")}</p></article>
  </div>
</section>

<section class="wrap section">
  <p class="kicker">{t("K'in's history", "K'ins Geschichte")}</p>
  <h2>{t("One line for every tier", "Ein Satz für jede Stufe")}</h2>
  <p class="lede-sm">{t("Each tier ends in a Portal Chamber, where a fragment of the mural lights up and K'in speaks one line of the temple's history. "
                        "Together they tell the official version of what happened. Whether it is the true one is another matter.",
                        "Jede Stufe endet in einer Portalkammer, wo ein Fragment des Wandbilds aufleuchtet und K'in einen Satz der Tempelgeschichte spricht. "
                        "Zusammen ergeben sie die offizielle Fassung der Ereignisse. Ob es die wahre ist, steht auf einem anderen Blatt.")}</p>
  <ol class="tiers lines">{line_html}</ol>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "E-03", t("The ending", "Das Ende"), t("Restore the cycle, or break it", "Den Kreislauf wiederherstellen oder durchbrechen"),
    t("<p>At the summit, Kaya places the Sun Orb on the altar before the great Sun Portal. Two pedestals flank it: one "
      "glowing gold, one deep violet.</p><p>Restoring the cycle keeps the temple alive as it is. Breaking it ends the loop for good. "
      "You won't know enough to choose the first time you get there, and what either choice costs depends on what you've read on the way up.</p>",
      "<p>Auf dem Gipfel legt Kaya die Sonnenkugel auf den Altar vor dem großen Sonnenportal. Zwei Sockel stehen daneben: "
      "einer glüht golden, der andere tief violett.</p>"
      "<p>Wird der Kreislauf wiederhergestellt, bleibt der Tempel lebendig, wie er ist. Wird er durchbrochen, endet die Schleife "
      "für immer. Beim ersten Mal weißt du noch nicht genug, um zu wählen, und was jede Entscheidung kostet, hängt davon ab, was du auf dem Weg nach oben gelesen hast.</p>"))}
</div></section>
"""


# ------------------------------------------------------------------ lore
def lore(ctx):
    u, t = ctx.url, ctx.t
    q1, q2 = t("“", "„"), t("”", "“")
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("The temple's history survives in three versions: the carved Spirit Mural, an old codex on a lectern, and the short lines "
                      "K'in speaks at each tier. They do not quite agree.",
                      "Die Geschichte des Tempels ist in drei Fassungen überliefert: im gemeißelten Geisterwandbild, in einem alten Codex auf einem "
                      "Lesepult und in den kurzen Sätzen, die K'in auf jeder Stufe spricht. Ganz einig sind sie sich nicht.")}</p>
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "W05", t("The balance", "Das Gleichgewicht"), t("Four elements, four orbs", "Vier Elemente, vier Kugeln"),
    t("<p>The priesthood of the Sun Temple harnessed fire, earth, wind and water through four sacred orbs, and built the temple around "
      "the Sun Portal on its summit. Balance among the elements was their highest ideal, and the source of their power.</p>",
      "<p>Die Priesterschaft des Sonnentempels bändigte Feuer, Erde, Wind und Wasser mit vier heiligen Kugeln und baute den Tempel um "
      "das Sonnenportal auf seinem Gipfel. Das Gleichgewicht der Elemente war ihr höchstes Ideal und die Quelle ihrer Macht.</p>"))}
  {feature(ctx, "HUB08", t("The betrayal", "Der Verrat"), t("One element broke the balance", "Ein Element zerbrach das Gleichgewicht"),
    t("<p>Then one element betrayed the others. The balance shattered, the priests were cursed into undeath and the orbs scattered up "
      "through the floors as wards.</p>"
      f"<p>K'in's account is simple: {q1}The first element betrayed them.{q2} But one panel of the mural has been re-cut in newer stone "
      "with different tool marks, and the older glyphs around it suggest the first element may have been the one betrayed.</p>",
      "<p>Dann verriet ein Element die anderen. Das Gleichgewicht zerbrach, die Priester wurden zu Untoten verflucht, und die Kugeln "
      "verstreuten sich als Schutzzauber über alle Ebenen.</p>"
      f"<p>K'ins Version ist einfach: {q1}Das erste Element verriet sie.{q2} Doch eine Tafel des Wandbilds wurde in jüngerem Stein mit "
      "anderen Werkzeugspuren neu gemeißelt, und die älteren Glyphen ringsum legen nahe, dass das erste Element vielleicht das verratene war.</p>"),
    flip=True)}
  {feature(ctx, "HOME-PRIEST", t("The curse", "Der Fluch"), t("The priests who never left", "Die Priester, die nie gegangen sind"),
    t("<p>The cursed priests still walk the temple as Risen Guardians, wrapped like funerary bundles, a cold sigil glowing on each chest. "
      "Their high priest waits on the summit as a towering hollow skeleton, four stolen lights circling in his open ribcage.</p>"
      "<p>Whether he caused the betrayal, or only took the blame for it, is one of the questions the climb has to answer. "
      f"<a href='{u('characters/guardians/index.html')}'>The Risen Guardians →</a></p>",
      "<p>Die verfluchten Priester wandeln noch immer als Erweckte Wächter durch den Tempel, eingewickelt wie Grabbündel, auf jeder Brust "
      "ein kalt leuchtendes Siegel. Ihr Hohepriester wartet auf dem Gipfel als riesiges, hohles Skelett, in dessen offenem Brustkorb vier "
      "gestohlene Lichter kreisen.</p><p>Ob er den Verrat verursacht hat oder nur die Schuld dafür trägt, ist eine der Fragen, die der "
      f"Aufstieg beantworten muss. <a href='{u('characters/guardians/index.html')}'>Zu den Erweckten Wächtern →</a></p>"))}
  {feature(ctx, "W06", t("The sealing", "Die Versiegelung"), t("A temple that closed itself", "Ein Tempel, der sich selbst verschloss"),
    t("<p>After the catastrophe the pyramid sealed itself and the Sun Portal went dark. K'in, once a priestess, chose to stay.</p>"
      "<p>Since then the temple has rearranged its chambers to trap greedy intruders, and the cycle of death and return has run long "
      "enough for the mural to fill with the faces of climbers.</p>",
      "<p>Nach der Katastrophe versiegelte sich die Pyramide, und das Sonnenportal erlosch. K'in, einst eine Priesterin, entschied sich zu bleiben.</p>"
      "<p>Seitdem ordnet der Tempel seine Kammern neu, um gierige Eindringlinge zu fangen, und der Kreislauf aus Tod und Rückkehr läuft "
      "schon so lange, dass sich das Wandbild mit den Gesichtern von Kletterern gefüllt hat.</p>"), flip=True)}
</div></section>

<section class="wrap section">
  {feature(ctx, "W08", t("The scholar who was right", "Die Gelehrte, die recht hatte"), t("Dr. Isabel Kaan's theory", "Die Theorie von Dr. Isabel Kaan"),
    t("<p>Kaya's mother, an epigrapher, argued that the Spirit Mural records a betrayal the builders deliberately hid. Her peers dismissed "
      "the theory, and she has been missing ever since. Her battered notebook travels in Kaya's satchel, next to Kaya's own.</p>"
      "<p>Kaya enters the temple to vindicate her, and has to learn the difference between proving a point and reading what the evidence "
      f"actually says. <a href='{u('characters/isabel-kaan.html')}'>Dr. Isabel Kaan →</a></p>",
      "<p>Kayas Mutter, eine Epigraphikerin, vertrat die These, dass das Geisterwandbild einen Verrat festhält, den die Erbauer absichtlich "
      "verborgen haben. Ihre Fachkollegen taten die Theorie ab, und seitdem ist sie verschwunden. Ihr abgegriffenes Notizbuch reist in "
      "Kayas Tasche, neben Kayas eigenem.</p><p>Kaya betritt den Tempel, um sie zu rehabilitieren, und muss lernen, dass es ein Unterschied "
      f"ist, recht behalten zu wollen oder zu lesen, was die Beweise tatsächlich sagen. <a href='{u('characters/isabel-kaan.html')}'>Dr. Isabel Kaan →</a></p>"))}
</section>
"""


# ------------------------------------------------------------------ short story
def reader_available():
    from importlib import util
    from pathlib import Path
    spec = util.spec_from_file_location("reader_data", Path(__file__).with_name("reader.py"))
    mod = util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.available()


def short_story(ctx):
    u, t = ctx.url, ctx.t
    chapters = [
        ("1", t("The Overlooked Find", "Der übersehene Fund"),
         t("Kaya arrives at the foot of the pyramid, wakes K'in, and dies in the Shell within the hour. When she wakes at the Threshold, "
           "something on the mural is new.",
           "Kaya erreicht den Fuß der Pyramide, weckt K'in und stirbt keine Stunde später in The Shell. Als sie an der Schwelle erwacht, "
           "ist etwas auf dem Wandbild neu.")),
        ("2", t("Reading Between the Layers", "Zwischen den Schichten lesen"),
         t("She reads the wall like a crime scene: a fresh carving, a panel cut in newer stone, tally marks in a codex margin. "
           "Oxlahun is very helpful.",
           "Sie liest die Wand wie einen Tatort: ein frisches Relief, eine Tafel in jüngerem Stein, Strichlisten am Rand eines Codex. "
           "Oxlahun ist sehr hilfsbereit.")),
        ("3", t("The Confrontation in the Dust", "Die Konfrontation im Staub"),
         t("Kaya brings her questions to K'in in front of the mural. The temple answers before K'in does.",
           "Kaya stellt K'in vor dem Wandbild ihre Fragen. Der Tempel antwortet, bevor K'in es tut.")),
        ("4", t("What the Ground Remembers", "Woran sich der Boden erinnert"),
         t("Kaya decides what to carry up the stairs, and what to write down in her own hand.",
           "Kaya entscheidet, was sie die Stufen hinauftragen will und was sie mit eigener Hand aufschreibt.")),
    ]
    ready = {f"{n}" for n in reader_available()}

    # a short looping scene for a chapter card, scaled to the card width
    loops = {"1": ("the-likeness", t("Kaya at the Spirit Mural, with K'in glowing beside the middle portal",
                                     "Kaya am Geisterwandbild, neben ihr leuchtet K'in vor dem mittleren Portal"))}

    def chapter_loop(n):
        if n not in loops:
            return ""
        name, alt = loops[n]
        return (f'<span class="chapter-loop"><picture>'
                f'<source media="(prefers-reduced-motion: reduce)" srcset="{ctx.asset(f"assets/media/{name}-still.webp")}">'
                f'<img src="{ctx.asset(f"assets/media/{name}.webp")}" alt="{alt}" width="480" height="270" loading="lazy" decoding="async">'
                f'</picture></span>')

    def chapter_card(n, nm, d):
        if n in ready:
            return (f'<a class="mode chapter is-ready" href="{u(f"story/chapter-{n}.html")}"><p class="kicker">{t("Chapter", "Kapitel")} {n}</p>'
                    f'<h3>{nm}</h3><p>{d}</p>{chapter_loop(n)}<span class="chapter-cta">{t("Read the chapter", "Kapitel lesen")}</span></a>')
        return (f'<article class="mode chapter"><p class="kicker">{t("Chapter", "Kapitel")} {n}</p><h3>{nm}</h3><p>{d}</p>'
                f'<span class="chapter-soon">{t("Coming soon", "Folgt bald")}</span></article>')
    ch_html = "".join(chapter_card(n, nm, d) for n, nm, d in chapters)

    fact_rows = [
        (t("Title", "Titel"), t("The Likeness (working title)", "Das Abbild (Arbeitstitel)")),
        (t("Genre", "Genre"), t("Archaeology mystery", "Archäologie-Mystery")),
        (t("Length", "Umfang"), t("Four chapters, about 4,000 to 6,000 words", "Vier Kapitel, etwa 4.000 bis 6.000 Wörter")),
        (t("Placement", "Einordnung"), t("A standalone opening to Kaya's adventure", "Ein eigenständiger Auftakt zu Kayas Abenteuer")),
        (t("Status", "Stand"), t("In progress", "In Arbeit")),
    ]

    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="story-quote left">{t("Kaya dies on her very first trap and wakes at the Threshold to find her own likeness freshly carved into the "
                                     "Spirit Mural, beside a betrayal panel that contradicts what the temple's spirit guide has told her. To keep "
                                     "climbing, she must decide how much of K'in's edited history she is willing to carry.",
                                     "Kaya stirbt an der allerersten Falle und erwacht an der Schwelle. Dort findet sie ihr eigenes Abbild, frisch in "
                                     "das Geisterwandbild gemeißelt, neben einer Verratstafel, die dem widerspricht, was ihr die Geistführerin des "
                                     "Tempels erzählt hat. Um weiterzuklettern, muss sie entscheiden, wie viel von K'ins umgeschriebener Geschichte "
                                     "sie mit sich tragen will.")}</p>
      <p>{t("A contained, atmospheric mystery with the heart of a coming-of-age adventure: the pleasure of watching a scholar read a wall "
            "like a crime scene. The mood is warm, curious and a little melancholic, with eerie rather than gory danger.",
            "Ein dichtes, atmosphärisches Mystery mit dem Herzen einer Coming-of-Age-Geschichte: das Vergnügen, einer Gelehrten dabei "
            "zuzusehen, wie sie eine Wand liest wie einen Tatort. Die Stimmung ist warm, neugierig und ein wenig melancholisch, die "
            "Gefahr eher unheimlich als blutig.")}</p>
    </div>
    {facts(fact_rows)}
  </div>
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Four chapters", "Vier Kapitel")}</p>
  <h2>{t("From the camp to the middle portal", "Vom Lager bis zum mittleren Portal")}</h2>
  <div class="chapters">{ch_html}</div>
</div></section>

<section class="wrap section">
  {feature(ctx, "HUB11", t("The evidence", "Die Beweise"), t("Three clues, two witnesses", "Drei Hinweise, zwei Zeugen"),
    t("<p>Kaya has three clues: the carved likeness, the re-cut panel, and the codex open on the lectern, whose margin is marked with "
      "tallies that add up to more deaths than she remembers.</p>"
      "<p>And she has two witnesses: a patient, grieving spirit she needs for every trap above her, and Oxlahun, the talkative trader "
      "at the offering table, who buys and sells Spirit Fragments and has every reason to want her to keep dying.</p>",
      "<p>Kaya hat drei Hinweise: das gemeißelte Abbild, die neu gemeißelte Tafel und den aufgeschlagenen Codex auf dem Lesepult, an "
      "dessen Rand Strichlisten mehr Tode zählen, als sie in Erinnerung hat.</p>"
      "<p>Und sie hat zwei Zeugen: einen geduldigen, trauernden Geist, den sie für jede Falle über ihr braucht, und Oxlahun, den "
      "redseligen Händler am Opfertisch, der Geistsplitter kauft und verkauft und allen Grund hat, sich zu wünschen, dass sie weiter stirbt.</p>"))}
  {feature(ctx, "HOME-OXLAHUN", t("The soft antagonist", "Der sanfte Gegenspieler"), t("A friend at the offering table", "Ein Freund am Opfertisch"),
    t("<p>Friendly, useful and invested in her failure. On a first read Oxlahun's help is help; on a second read it is something else.</p>"
      f"<p><a href='{u('characters/oxlahun.html')}'>Oxlahun →</a></p>",
      "<p>Freundlich, nützlich und an ihrem Scheitern interessiert. Beim ersten Lesen ist Oxlahuns Hilfe einfach Hilfe, beim zweiten Lesen "
      f"etwas anderes.</p><p><a href='{u('characters/oxlahun.html')}'>Oxlahun →</a></p>"), flip=True)}
</section>

<section class="story-band">
  <div class="wrap section story-inner">
    <h2>{t("Start reading", "Jetzt lesen")}</h2>
    <p class="story-note">{t(f"{len(ready)} of 4 chapters published", f"{len(ready)} von 4 Kapiteln veröffentlicht")}</p>
    <p>{t("The story is published chapter by chapter, laid out to be read like a book: at your own pace, in day or night mode.",
          "Die Geschichte erscheint Kapitel für Kapitel und ist gesetzt wie ein Buch: in deinem Tempo, im Tag- oder Nachtmodus.")}</p>
    <a class="btn btn-gold" href="{u('story/chapter-1.html')}">{t("Read Chapter 1", "Kapitel 1 lesen")}</a>
  </div>
</section>
"""


PAGES = {
    "story/index.html": dict(
        title=("The Story", "Die Geschichte"), kicker=("Story", "Geschichte"), banner="E-03",
        lede=("A scholar's daughter, a temple that records every death, and a guide who has been editing history out of love and grief.",
              "Die Tochter einer Gelehrten, ein Tempel, der jeden Tod festhält, und eine Führerin, die die Geschichte aus Liebe und Trauer umgeschrieben hat."),
        description=("The story of Ascent of the Sun Temple: Kaya, K'in, the Carved Climbers and the cycle.",
                     "Die Geschichte von Ascent of the Sun Temple: Kaya, K'in, die gemeißelten Kletterer und der Kreislauf."),
        body=story, og="E-03"),
    "story/lore.html": dict(
        title=("Lore & History", "Vorgeschichte & Legenden"), kicker=("Story", "Geschichte"), banner="HOME-PRIEST",
        lede=("The builders, the four orbs, the betrayal, the curse and the sealing, and why the record cannot be trusted.",
              "Die Erbauer, die vier Kugeln, der Verrat, der Fluch und die Versiegelung, und warum man der Überlieferung nicht trauen kann."),
        description=("The history of the Sun Temple.", "Die Geschichte des Sonnentempels."),
        body=lore, og="HUB08"),
    "story/short-story.html": dict(
        title=("The Short Story", "Die Kurzgeschichte"), kicker=("Story", "Geschichte"), banner="HOME-KIN",
        lede=("“The Likeness”, an archaeology mystery set in the Sun Temple. Four chapters, in progress.",
              "„Das Abbild“, ein Archäologie-Mystery im Sonnentempel. Vier Kapitel, in Arbeit."),
        description=("The Likeness: a short story set in the world of Mayan Temple Adventures.",
                     "Das Abbild: eine Kurzgeschichte aus der Welt von Mayan Temple Adventures."),
        body=short_story, og="HUB09"),
}
