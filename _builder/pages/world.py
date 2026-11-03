"""World tab: The Living Temple, The Threshold, Records & Relics (English and German)."""
from components import feature, pair


# ------------------------------------------------------------------ living temple
def living_temple(ctx):
    u, t = ctx.url, ctx.t
    rules = [
        t("Death inside the temple returns a climber to the Threshold, memories intact.",
          "Wer im Tempel stirbt, kehrt mit allen Erinnerungen in die Schwelle zurück."),
        t("The temple keeps a record of every climber, on the mural and in the codex.",
          "Der Tempel hält jeden Kletterer fest, auf dem Wandbild und im Codex."),
        t("The chambers above shift; the Threshold never does.",
          "Die Kammern darüber verändern sich, die Schwelle nie."),
        t("The traps are physical: they can be read, timed and investigated.",
          "Die Fallen sind greifbar: Man kann sie lesen, timen und untersuchen."),
    ]
    rule_html = "".join(f"<li>{r}</li>" for r in rules)

    return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose">
      <p class="big">{t("The Sun Temple is not a ruin to be explored. It is a structure that remembers, reacts and makes every climb a test.",
                        "Der Sonnentempel ist keine Ruine, die man erkundet. Er ist ein Bauwerk, das sich erinnert, reagiert und jeden Aufstieg zur Prüfung macht.")}</p>
      <p>{t("Its chambers shift to trap greedy intruders, its traps are physical and readable, and its motives remain a mystery. "
            "The only stable place inside is the Threshold, the base hall where every climb begins and every death returns.",
            "Seine Kammern verschieben sich, um gierige Eindringlinge zu fangen, seine Fallen sind greifbar und lesbar, und seine Absichten "
            "bleiben ein Rätsel. Der einzige beständige Ort im Inneren ist die Schwelle, die Grundhalle, in der jeder Aufstieg beginnt und "
            "in die jeder Tod zurückführt.")}</p>
    </div>
    <div class="rules">
      <p class="kicker">{t("Rules of the temple", "Regeln des Tempels")}</p>
      <ul>{rule_html}</ul>
    </div>
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "HOME-CLIMB", t("Inside", "Im Inneren"), t("A pyramid that climbs toward the sun", "Eine Pyramide, die zur Sonne aufsteigt"),
    t("<p>Six tiers stack inside the pyramid: flooded foundations, trap galleries, shifting vaults, four elemental sanctums, the illusion "
      "depths and a final ascension. Each tier has its own look, its own hazards and its own piece of the temple's history.</p>"
      f"<p>On the flat summit stands the small temple with the great Sun Portal, dark since the sealing. <a href='{u('climb/index.html')}'>The climb, tier by tier →</a></p>",
      "<p>Sechs Stufen liegen übereinander im Inneren der Pyramide: überflutete Fundamente, Fallengalerien, wandernde Gewölbe, vier "
      "Elementarheiligtümer, die Tiefen der Täuschung und eine letzte Erhebung. Jede Stufe hat ihren eigenen Look, ihre eigenen Gefahren "
      "und ihr eigenes Stück Tempelgeschichte.</p><p>Auf dem flachen Gipfel steht der kleine Tempel mit dem großen Sonnenportal, dunkel "
      f"seit der Versiegelung. <a href='{u('climb/index.html')}'>Der Aufstieg, Stufe für Stufe →</a></p>"))}
  {feature(ctx, "HUB05", t("The way in", "Der Eingang"), t("The serpent-headed tunnel", "Der Tunnel der Schlangenköpfe"),
    t("<p>Two enormous feathered serpents guard the entrance, their bodies carved up the first terrace, a sun mask on the lintel between "
      "them. A few worn steps lead down into the dark, toward a faint golden glow.</p>",
      "<p>Zwei gewaltige Federschlangen bewachen den Eingang, ihre Körper sind die erste Terrasse hinaufgemeißelt, zwischen ihnen prangt "
      "eine Sonnenmaske auf dem Türsturz. Ein paar ausgetretene Stufen führen hinab ins Dunkel, auf ein schwaches goldenes Leuchten zu.</p>"),
    flip=True)}
  {feature(ctx, "A-04", t("Outside", "Draußen"), t("Jungle and camp", "Dschungel und Lager"),
    t("<p>Dense jungle presses against the stone and hides the pyramid's base beneath vines and roots. At the foot of the pyramid, "
      "Isabel Kaan's old camp is the last taste of ordinary life: a canvas tent, supply crates, a kettle ticking on the campfire. "
      "Every climb in the game starts here.</p>",
      "<p>Dichter Dschungel drängt sich an den Stein und verbirgt den Fuß der Pyramide unter Ranken und Wurzeln. Am Fuß der Pyramide "
      "ist Isabel Kaans altes Lager der letzte Rest gewöhnlichen Lebens: ein Segeltuchzelt, Vorratskisten, ein Kessel, der über dem Lagerfeuer leise tickt. "
      "Jeder Aufstieg im Spiel beginnt hier.</p>"))}
  {feature(ctx, "HUB04", t("The terraces", "Die Terrassen"), t("Eight steps to the sky", "Acht Stufen bis zum Himmel"),
    t("<p>Eight sloped terraces with stepped cornices, jade bands and recessed sun panels rise to the summit temple, with the grand stair "
      "running up the front between serpent-headed balustrades.</p><p>Roots and moss weather the outside slowly; inside, the temple "
      "changes deliberately. Telling the two apart is part of reading the place.</p>",
      "<p>Acht geneigte Terrassen mit gestuften Gesimsen, Jadebändern und eingelassenen Sonnenreliefs steigen zum Gipfeltempel auf; die "
      "große Treppe führt vorn zwischen Balustraden mit Schlangenköpfen hinauf.</p><p>Wurzeln und Moos verwittern das Äußere langsam, "
      "im Inneren verändert sich der Tempel absichtlich. Beides auseinanderzuhalten gehört dazu, diesen Ort zu lesen.</p>"), flip=True)}
</div></section>
"""


# ------------------------------------------------------------------ threshold
def threshold(ctx):
    u, t = ctx.url, ctx.t
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("The Threshold is the temple's still centre: a vast square stone hall at the base of the pyramid, lit by a single "
                      "fissure in the ceiling.",
                      "Die Schwelle ist der ruhende Mittelpunkt des Tempels: eine gewaltige quadratische Steinhalle am Fuß der Pyramide, "
                      "erhellt von einem einzigen Spalt in der Decke.")}</p>
    <p>{t("It is a place of return, orientation, trade and ritual. Its scale is imposing, but its familiar layout lends it an unsettling "
          "calm after the confusion of the floors above. The architecture here never changes. What changes is the record.",
          "Sie ist ein Ort der Rückkehr, der Orientierung, des Handels und des Rituals. Ihre Größe ist überwältigend, doch ihr vertrauter "
          "Grundriss verleiht ihr nach dem Durcheinander der oberen Ebenen eine beunruhigende Ruhe. Die Architektur verändert sich hier nie. "
          "Was sich verändert, ist die Aufzeichnung.")}</p>
  </div>
  {pair(ctx, "A-02", t("The hall and the forecourt from above", "Halle und Vorplatz von oben"),
        "CX-HUB", t("The same hall as a page of the codex Kaya finds", "Dieselbe Halle als Seite des Codex, den Kaya findet"))}
</section>

<section class="band"><div class="wrap section">
  <p class="kicker">{t("Inside the hall", "In der Halle")}</p>
  <h2>{t("Five places, one evidence room", "Fünf Orte, ein Beweisraum")}</h2>
  {feature(ctx, "HUB06", t("The centre", "Die Mitte"), t("The Round Altar", "Der runde Altar"),
    t("<p>A low circular altar carved as a great calendar wheel stands in the middle of the hall. K'in floats above it to greet every "
      "returning climber. What first looks like a ceremonial welcome can come to feel like a checkpoint in a system Kaya does not understand.</p>",
      "<p>In der Mitte der Halle steht ein flacher, runder Altar, gemeißelt wie ein großes Kalenderrad. K'in schwebt darüber und begrüßt "
      "jeden zurückkehrenden Kletterer. Was zuerst wie ein feierlicher Empfang wirkt, fühlt sich mit der Zeit an wie ein Kontrollpunkt in "
      "einem System, das Kaya nicht versteht.</p>"))}
  {feature(ctx, "HUB07", t("The way up", "Der Weg nach oben"), t("The Three Portals", "Die drei Portale"),
    t("<p>Three huge round portals stand on a raised dais. The middle one swirls with gold and leads back into the climb. The two side "
      "portals stay sealed, carved shut like closed serpent eyes, and their silence feels deliberate.</p>",
      "<p>Drei riesige runde Portale stehen auf einem erhöhten Podest. Das mittlere wirbelt golden und führt zurück in den Aufstieg. Die "
      "beiden seitlichen bleiben versiegelt, verschlossen wie geschlossene Schlangenaugen, und ihr Schweigen wirkt beabsichtigt.</p>"),
    flip=True)}
  {feature(ctx, "HUB08", t("The record", "Die Aufzeichnung"), t("The Spirit Mural", "Das Geisterwandbild"),
    t("<p>Above the portals the whole wall is a carved history: builders holding four orbs in balance, the Sun Portal burning, the "
      "elements turning on each other, priests falling into undeath, orbs scattering and the temple sealing itself. Panels light up as "
      "the climb progresses.</p><p>It is archive, memorial and accusation at once. And one panel looks freshly re-cut in paler stone.</p>",
      "<p>Über den Portalen ist die ganze Wand eine gemeißelte Chronik: Erbauer, die vier Kugeln im Gleichgewicht halten, das brennende "
      "Sonnenportal, Elemente, die sich gegeneinander wenden, Priester, die in den Untod stürzen, verstreute Kugeln und der Tempel, der "
      "sich selbst versiegelt. Mit dem Aufstieg leuchten immer mehr Tafeln auf.</p><p>Es ist Archiv, Denkmal und Anklage zugleich. Und "
      "eine Tafel sieht aus, als wäre sie frisch in hellerem Stein nachgemeißelt.</p>"))}
  {feature(ctx, "HUB10", t("The trade", "Der Handel"), t("The Offering Table", "Der Opfertisch"),
    t("<p>Oxlahun's stall: lamps, copal, jade beads, a bent brass lantern, a surveyor's notched staff, and a tray of glowing Spirit "
      "Fragments laid out like sweets, every item wearing a blank bark-paper tag. An offering place has become a market, and the "
      f"difference matters. <a href='{u('characters/oxlahun.html')}'>Oxlahun →</a></p>",
      "<p>Oxlahuns Stand: Lampen, Kopal, Jadeperlen, eine verbogene Messinglaterne, der gekerbte Stab eines Landvermessers und ein Tablett "
      "mit leuchtenden Geistsplittern, ausgelegt wie Süßigkeiten, jedes Stück mit einem leeren Anhänger aus Rindenpapier. Aus einem "
      f"Opferplatz ist ein Markt geworden, und dieser Unterschied zählt. <a href='{u('characters/oxlahun.html')}'>Oxlahun →</a></p>"),
    flip=True)}
  {feature(ctx, "HUB11", t("The quiet witness", "Der stille Zeuge"), t("The Lectern and Codex", "Lesepult und Codex"),
    t("<p>A stone lectern shaped like a crouching jaguar, carved with a scribe-monkey, holds an open screenfold codex painted with maps "
      "of the temple's chambers. New pages glow as they are added. In its margin, small tally marks are easy to overlook, and hard to "
      "explain.</p>",
      "<p>Ein steinernes Lesepult in Gestalt eines kauernden Jaguars, verziert mit einem schreibenden Affen, trägt einen aufgeschlagenen "
      "Faltcodex mit gemalten Karten der Tempelkammern. Neue Seiten leuchten auf, sobald sie hinzukommen. An seinem Rand stehen kleine "
      "Strichlisten, die man leicht übersieht und schwer erklären kann.</p>"))}
</div></section>
"""


# ------------------------------------------------------------------ relics
def relics(ctx):
    u, t = ctx.url, ctx.t
    return f"""
<section class="wrap section narrow-top">
  <div class="prose">
    <p class="big">{t("The temple is full of small things that do not add up. Read closely, they turn the Threshold into a crime scene.",
                      "Der Tempel steckt voller Kleinigkeiten, die nicht zusammenpassen. Genau gelesen machen sie die Schwelle zum Tatort.")}</p>
  </div>
</section>

<section class="band"><div class="wrap section">
  {feature(ctx, "HUB09", t("On the mural", "Auf dem Wandbild"), t("The Carved Climbers", "Die gemeißelten Kletterer"),
    t("<p>One likeness for every climber K'in has lost: a surveyor sighting along his notched staff, a woman with a rope coil and an "
      "empty loop, a young man holding up an open lantern, a small figure with a satchel, a carving left half finished, a warden looking "
      "back over his shoulder, and the newest of all, a young explorer with goggles and twin braids, still pale with fresh dust.</p>"
      f"<p><a href='{u('characters/climbers/index.html')}'>Meet the Carved Climbers →</a></p>",
      "<p>Ein Abbild für jeden Kletterer, den K'in verloren hat: ein Landvermesser, der an seinem gekerbten Stab entlangpeilt, eine Frau "
      "mit Seilrolle und leerer Schlinge, ein junger Mann mit erhobener, offener Laterne, eine kleine Gestalt mit Umhängetasche, ein nur "
      "zur Hälfte vollendetes Relief, ein Wächter, der über die Schulter zurückblickt, und das neueste von allen, eine junge Entdeckerin "
      "mit Schutzbrille und zwei Zöpfen, noch hell vom frischen Staub.</p>"
      f"<p><a href='{u('characters/climbers/index.html')}'>Zu den gemeißelten Kletterern →</a></p>"))}
  {feature(ctx, "HUB13", t("Around the hall", "In der Halle"), t("Traces in the Threshold", "Spuren in der Schwelle"),
    t("<p>A cross-shaped game board scratched into a step, with dried beans for counters. A broom worn into a long slant. A patch of "
      "lime floor polished to glass. A folded palm-leaf whistle and a flower glazed in amber wax. A scrap of modern twill that does not "
      "belong here at all. Three tiny limestone keepsakes carved with traps. A chalk tally in bar-and-dot numerals.</p>"
      "<p>Each one belongs to someone, and each one is a clue.</p>",
      "<p>Ein kreuzförmiges Spielbrett, in eine Stufe geritzt, mit getrockneten Bohnen als Spielsteinen. Ein Besen, schräg abgenutzt. "
      "Eine Stelle im Kalkboden, poliert wie Glas. Eine Pfeife aus gefaltetem Palmblatt und eine Blüte, glasiert in Bernsteinwachs. Ein "
      "Fetzen moderner Köperstoff, der überhaupt nicht hierher gehört. Drei winzige Andenken aus Kalkstein mit eingeschnitzten Fallen. "
      "Eine Strichliste aus Kreide in Balken-und-Punkt-Zahlen.</p><p>Jedes Stück gehört jemandem, und jedes ist ein Hinweis.</p>"),
    flip=True)}
  {feature(ctx, "W08", t("Kaya's method", "Kayas Methode"), t("The field kit", "Die Feldausrüstung"),
    t("<p>A worn field notebook with a pencil in the elastic, her mother's battered notebook with a frayed ribbon, a folding rule, rubbing "
      "paper and charcoal, soft brushes, a trowel, a brass compass, a canteen, a magnifying lens and the bronze goggles.</p>"
      "<p>Kaya's tools do not reveal the past by magic. They make her claims testable: a rubbing preserves the shape of a carving, not "
      "its intention, and she writes possible reading rather than presenting a guess as fact.</p>",
      "<p>Ein abgenutztes Feldnotizbuch mit Bleistift im Gummiband, das zerfledderte Notizbuch ihrer Mutter mit ausgefranstem Lesebändchen, "
      "ein Zollstock, Papier und Kohle für Abriebe, weiche Pinsel, eine Kelle, ein Messingkompass, eine Feldflasche, eine Lupe und die "
      "Bronzebrille.</p><p>Kayas Werkzeuge enthüllen die Vergangenheit nicht durch Magie. Sie machen ihre Behauptungen überprüfbar: Ein "
      "Abrieb bewahrt die Form eines Reliefs, nicht seine Absicht, und sie schreibt mögliche Lesart, statt eine Vermutung als Tatsache auszugeben.</p>"))}
  {feature(ctx, "P10", t("The economy of the loop", "Die Wirtschaft der Schleife"), t("Spirit Fragments", "Geistsplitter"),
    t("<p>Small translucent golden shards, what a climber's spirit keeps when the temple takes them back. Oxlahun buys and sells them. "
      "Their trade only works because climbers keep dying and returning, and nobody has said exactly what they are.</p>",
      "<p>Kleine, durchscheinende goldene Splitter: das, was der Geist eines Kletterers behält, wenn der Tempel ihn zurückholt. Oxlahun "
      "kauft und verkauft sie. Dieser Handel funktioniert nur, weil Kletterer immer wieder sterben und zurückkehren, und niemand hat je "
      "genau gesagt, was sie eigentlich sind.</p>"), flip=True)}
</div></section>
"""


PAGES = {
    "world/index.html": dict(
        title=("The Living Temple", "Der lebende Tempel"), kicker=("World", "Welt"), banner="A-04",
        lede=("One stepped pyramid, eight terraces high, that remembers everyone who climbs it.",
              "Eine Stufenpyramide, acht Terrassen hoch, die sich an jeden erinnert, der sie erklimmt."),
        description=("The Sun Temple, its jungle and its rules.", "Der Sonnentempel, sein Dschungel und seine Regeln."),
        body=living_temple, og="HOME-CLIMB"),
    "world/threshold.html": dict(
        title=("The Threshold", "Die Schwelle"), kicker=("World", "Welt"), banner="A-03",
        lede=("The vast square hall at the base of the pyramid, where every climb begins and every death returns.",
              "Die gewaltige quadratische Halle am Fuß der Pyramide, in der jeder Aufstieg beginnt und in die jeder Tod zurückführt."),
        description=("The Threshold: altar, portals, Spirit Mural, offering table and codex.",
                     "Die Schwelle: Altar, Portale, Geisterwandbild, Opfertisch und Codex."),
        body=threshold, og="A-03"),
    "world/relics.html": dict(
        title=("Records & Relics", "Aufzeichnungen & Relikte"), kicker=("World", "Welt"), banner="HOME-KIN",
        lede=("Carvings, keepsakes, tools and fragments: the evidence the temple leaves behind.",
              "Reliefs, Andenken, Werkzeuge und Splitter: die Beweise, die der Tempel hinterlässt."),
        description=("The objects and records of the Sun Temple.", "Die Objekte und Aufzeichnungen des Sonnentempels."),
        body=relics, og="HUB09"),
}
