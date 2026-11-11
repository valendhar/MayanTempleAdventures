"""Characters tab (English and German).

Every character page is built from one data entry. Text values are (english, german) pairs.
Extra images listed under "extras" appear automatically once they are uploaded.
"""


def T(ctx, v):
    return v[1] if (isinstance(v, tuple) and ctx.lang == "de") else (v[0] if isinstance(v, tuple) else v)


def q(ctx, text):
    return f'{ctx.t("“", "„")}{text}{ctx.t("”", "“")}'


# ------------------------------------------------------------------ shared pieces
def card(ctx, img, name, role, path):
    # name set over the picture with the role beneath it, like the cast on the home page
    return (f'<a class="card" href="{ctx.url(path)}">{ctx.figure(img, alt=name, link=False)}<span class="card-body">'
            f'<span class="card-title">{name}</span><span class="card-kicker">{role}</span></span></a>')


def extras_gallery(ctx, extras):
    have = [(i, T(ctx, c)) for i, c in extras if ctx.has(i)]
    if not have:
        return ""
    figs = "".join(ctx.figure(i, c) for i, c in have)
    return f'<div class="gallery extras">{figs}</div>'


def own_scene(c):
    """The main cast have their own scene as banner: it is shown whole instead of as a cropped strip."""
    return c.get("banner", "").startswith("HOME-") and not c.get("group")


def character_page(c):
    def body(ctx):
        t = ctx.t
        intro = "".join(f"<p>{T(ctx, p)}</p>" for p in c["intro"])
        facts = "".join(f"<div><dt>{T(ctx, k)}</dt><dd>{T(ctx, v)}</dd></div>" for k, v in c["facts"])
        # once an action shot replaces the sheet (ACT-<id>), the caption no longer calls it a sheet
        cap = ("In action", "In Aktion") if ctx.has("ACT-" + c["sheet"]) else c.get("sheet_caption", ("Character sheet", "Charakterblatt"))
        sheet = ctx.figure(c["sheet"], T(ctx, cap), cls="sheet")
        # a scene already shown whole in the page header is not repeated in the gallery
        shown = c.get("banner") if own_scene(c) else None
        extra = extras_gallery(ctx, [e for e in c.get("extras", []) if e[0] != shown])
        quote = c.get("quote")
        quote_html = ""
        if quote:
            quote_html = (f'<blockquote class="char-quote"><p>{q(ctx, T(ctx, quote[0]))}</p>'
                          f'<cite>{T(ctx, quote[1])}</cite></blockquote>')
        back = ""
        if c.get("group"):
            gpath, glabel = c["group"]
            back = f'<p><a class="text-link" href="{ctx.url(gpath)}">← {T(ctx, glabel)}</a></p>'
        return f"""
<section class="wrap section narrow-top">
  <div class="intro">
    <div class="prose"><p class="big">{T(ctx, c["hook"])}</p>{intro}{back}</div>
    <dl class="facts">{facts}</dl>
  </div>
</section>
<section class="band"><div class="wrap section">
  {sheet}
  {extra}
</div></section>
<section class="wrap section design-row">
  <div>{quote_html}</div>
  <div><p class="kicker">{t("Design notes", "Designnotizen")}</p><p>{T(ctx, c["design"])}</p></div>
</section>
"""

    return dict(title=c["name"], kicker=c["role"], lede=c["lede"], banner=c.get("banner"),
                banner_full=own_scene(c), description=c["lede"], body=body, og=c.get("og", c["sheet"]))


R = ("Role", "Rolle")
WHERE = ("Found", "Zu finden")
SIG = ("Signature", "Erkennungszeichen")
VOICE = ("Voice", "Stimme")
STATE = ("State", "Zustand")
GUARD = ("characters/guardians/index.html", ("All Risen Guardians", "Alle Erweckten Wächter"))
CLIMB = ("characters/climbers/index.html", ("All Carved Climbers", "Alle gemeißelten Kletterer"))

C = {}

# ================================================================== main cast
C["characters/kaya.html"] = dict(
    name="Kaya", role=("The reader", "Die Leserin"), sheet="CS-KAYA", banner="HOME-KAYA", og="HOME-KAYA",
    lede=("Twenty-three, a scholar's daughter, and the first climber in centuries who reads the wall instead of the stair.",
          "Dreiundzwanzig, Tochter einer Gelehrten und seit Jahrhunderten die erste Kletterin, die die Wand liest statt der Treppe."),
    hook=("Kaya survives by reading, not fighting. She arrives with her mother's notebooks, her own rubbing kit and a certainty "
          "that she will be the first living person to read the Spirit Mural.",
          "Kaya überlebt durch Lesen, nicht durch Kämpfen. Sie kommt mit den Notizbüchern ihrer Mutter, ihrer eigenen Ausrüstung "
          "für Abriebe und der Gewissheit, als erster lebender Mensch das Geisterwandbild zu lesen."),
    intro=[
        ("She grew up in field camps, archive basements and the back rows of lecture halls, raised by an epigrapher whose theory "
         "the experts laughed at. She learned to take a rubbing, sketch a glyph and compare tool marks before she was a teenager.",
         "Sie wuchs in Feldlagern, Archivkellern und den hinteren Reihen von Hörsälen auf, großgezogen von einer Epigraphikerin, "
         "deren Theorie die Fachwelt belächelte. Abriebe nehmen, Glyphen skizzieren und Werkzeugspuren vergleichen konnte sie, "
         "bevor sie ein Teenager war."),
        ("Her mother vanished fourteen months ago without a body, a note or a witness. Kaya keeps a daily count of the days on the "
         "back page of her notebook, in her mother's bar-and-dot numerals, and speaks of her in the present tense on purpose. "
         "She has not told anyone, including herself, whether she has come for a mural or a mother.",
         "Ihre Mutter verschwand vor vierzehn Monaten, ohne Leiche, ohne Nachricht, ohne Zeugen. Kaya zählt die Tage auf der "
         "letzten Seite ihres Notizbuchs, in den Balken-und-Punkt-Zahlen ihrer Mutter, und spricht absichtlich in der Gegenwart "
         "von ihr. Sie hat niemandem gesagt, auch sich selbst nicht, ob sie wegen eines Wandbilds gekommen ist oder wegen einer Mutter."),
        ("In the game, the players are Climbers and Kaya is the one they meet. She climbs the Shell beside the party and "
         "dies on its traps like everyone else. Then she stays at the Threshold to read the wall, and sends Climbers up for "
         "the evidence she cannot reach herself: mural fragments, codex pages and her mother's notes.",
         "Im Spiel sind die Spieler Kletterer, und Kaya ist die, der sie begegnen. Sie steigt mit der Gruppe durch The Shell "
         "und stirbt wie alle anderen an seinen Fallen. Dann bleibt sie an der Schwelle, um die Wand zu lesen, und schickt "
         "Kletterer nach den Beweisen aus, an die sie selbst nicht herankommt: Wandbildfragmente, Codexseiten und die Notizen "
         "ihrer Mutter."),
    ],
    facts=[(R, ("Story heroine; in the game, a companion and quest-giver", "Heldin der Geschichte; im Spiel Begleiterin und Auftraggeberin")),
           (("Age", "Alter"), ("23", "23")),
           (SIG, ("Her mother's bronze dig goggles, twin braids, a satchel on the left hip, charcoal behind one ear",
                  "Die bronzene Grabungsbrille ihrer Mutter, zwei Zöpfe, die Tasche an der linken Hüfte, Kohle hinter einem Ohr")),
           (("Method", "Methode"), ("Rubbings, sketches, tool marks, and “possible reading” instead of a guess",
                                     "Abriebe, Skizzen, Werkzeugspuren und „mögliche Lesart“ statt einer Vermutung")),
           (("In the game", "Im Spiel"), ("Floor 0 beside the party, then the Threshold, and three scenes on the way up",
                                          "Ebene 0 an der Seite der Gruppe, dann die Schwelle und drei Szenen auf dem Weg nach oben"))],
    quote=(("Thank you. I mean that. And I'm going to check it anyway.",
            "Danke. Ehrlich. Und ich prüfe es trotzdem nach."), ("Kaya", "Kaya")),
    design=("Everything has to read in motion, at third-person range, against busy carved stone. Her cerulean tunic is the one "
            "cool colour on floors lit almost entirely by torch gold, so she never gets lost in a fire room. The braids hang "
            "straight down her back for clean 3D geometry, and goggles, satchel and braids stay in silhouette from every angle.",
            "Alles muss in Bewegung, aus der Third-Person-Distanz und vor unruhig behauenem Stein lesbar sein. Ihre himmelblaue "
            "Tunika ist die einzige kühle Farbe auf Ebenen, die fast nur von Fackelgold beleuchtet sind, so geht sie selbst in "
            "einem Feuerraum nie verloren. Die Zöpfe hängen für saubere 3D-Geometrie gerade den Rücken hinunter, und Brille, Tasche "
            "und Zöpfe bleiben aus jedem Blickwinkel in der Silhouette erkennbar."),
    extras=[("HOME-KAYA", ("Kaya in action", "Kaya in Aktion")), ("TA-KAYA", ("Turnaround", "Turnaround")),
            ("W08", ("Kaya's field kit", "Kayas Feldausrüstung"))],
)

C["characters/kin.html"] = dict(
    name="K'in", role=("The spirit guide", "Die Geistführerin"), sheet="CS-KIN", banner="HOME-KIN", og="HOME-KIN",
    lede=("The last spirit of the Sun Temple: a fist-sized wisp of honey-gold light who guides every climber and remembers them all.",
          "Der letzte Geist des Sonnentempels: ein faustgroßes Irrlicht aus honiggoldenem Licht, das jeden Kletterer führt und sich an alle erinnert."),
    hook=("K'in is gentle, patient and indispensable. She is also an unreliable source who loves her reader.",
          "K'in ist sanft, geduldig und unverzichtbar. Sie ist auch eine unzuverlässige Quelle, die ihre Leserin liebt."),
    intro=[
        ("Before she was a wisp she was a day-keeper of the temple's priesthood, keeper of the count of days. When the temple "
         "sealed, she chose to stay. Since then she has greeted every climber who woke at the Threshold, and watched most of them die.",
         "Bevor sie ein Irrlicht wurde, war sie Tageshüterin der Priesterschaft des Tempels und führte die Zählung der Tage. Als "
         "sich der Tempel versiegelte, entschied sie sich zu bleiben. Seitdem hat sie jeden Kletterer begrüßt, der an der "
         "Schwelle erwachte, und die meisten von ihnen sterben sehen."),
        ("Her light shows her mood: steady and warm when she is calm, thin and pale when troubled, guttering like a candle under "
         "real strain. In the deepest dark, at the edge of her glow, Kaya sometimes catches the afterimage of a woman. It never "
         "holds long enough to sketch.",
         "Ihr Licht verrät ihre Stimmung: ruhig und warm, wenn sie gelassen ist, dünn und blass, wenn sie beunruhigt ist, und "
         "flackernd wie eine Kerze unter echter Belastung. In tiefster Dunkelheit, am Rand ihres Scheins, erhascht Kaya manchmal "
         "das Nachbild einer Frau. Es bleibt nie lange genug, um es zu skizzieren."),
    ],
    facts=[(R, ("Spirit guide, companion, keeper of the temple's history", "Geistführerin, Begleiterin, Hüterin der Tempelgeschichte")),
           (("Name", "Name"), ("K'in means “sun” or “day” in Maya", "K'in bedeutet auf Maya „Sonne“ oder „Tag“")),
           (("In play", "Im Spiel"), ("Ghost-path hints, trap warnings, secret pulses, lore at murals, greets every return",
                                      "Geisterpfad-Hinweise, Fallenwarnungen, Geheimnis-Impulse, Legenden an Wandbildern, begrüßt jede Rückkehr")),
           (("Habit", "Eigenart"), ("She still keeps the day, tracking the sunbeam through the ceiling crack",
                                     "Sie zählt noch immer die Tage und verfolgt den Sonnenstrahl durch den Deckenspalt"))],
    quote=(("Welcome, climbing soul. Step lightly at first. Let the temple teach you its weight.",
            "Willkommen, kletternde Seele. Tritt anfangs leicht auf. Lass dich vom Tempel sein Gewicht lehren."),
           ("K'in's first greeting", "K'ins erste Begrüßung")),
    design=("K'in has no face and no limbs; every emotion is carried by light. Seven states (idle, hint, warning, secret nearby, "
            "singing, sad and guttering) give her a full performance. She never touches the floor, so she never sets off a trap, "
            "and her scale is fixed against Kaya's shoulder so she never reads as a pickup.",
            "K'in hat weder Gesicht noch Gliedmaßen; jede Emotion wird über Licht transportiert. Sieben Zustände (Ruhe, Hinweis, "
            "Warnung, Geheimnis in der Nähe, Singen, Trauer und Flackern) geben ihr ein vollständiges Spiel. Sie berührt nie den "
            "Boden, löst also nie eine Falle aus, und ihre Größe ist an Kayas Schulter festgelegt, damit sie nie wie ein "
            "Sammelobjekt wirkt."),
    extras=[("W07", ("K'in's light", "K'ins Licht")), ("HOME-NEVERALONE", ("K'in draws the way", "K'in zeigt den Weg")),
            ("HOME-KIN", ("Before the Spirit Mural", "Vor dem Geisterwandbild"))],
)

C["characters/oxlahun.html"] = dict(
    name="Oxlahun", role=("The trader", "Der Händler"), sheet="CS-OXLAHUN", banner="HOME-OXLAHUN", og="HOME-OXLAHUN",
    lede=("The friendliest face in the Threshold, and its quietest threat. Called “Thirteen”, for the number of times he says he has died.",
          "Das freundlichste Gesicht in der Schwelle und ihre leiseste Bedrohung. „Dreizehn“ genannt, nach der Zahl der Tode, die er gestorben sein will."),
    hook=("Oxlahun keeps the offering table: tea, supplies, a keepsake for every first death, and a tray of Spirit Fragments laid "
          "out like sweets.",
          "Oxlahun betreibt den Opfertisch: Tee, Vorräte, ein Andenken für jeden ersten Tod und ein Tablett mit Geistsplittern, "
          "ausgelegt wie Süßigkeiten."),
    intro=[
        ("He is a broad, easy man of no certain age, and the cleanest thing in a hall of damp stone and grey dust. He listens "
         "with his whole body, gets your name in the first minute, and has never once been wrong about a floor.",
         "Er ist ein breiter, gelassener Mann unbestimmten Alters und das Sauberste in einer Halle aus feuchtem Stein und grauem "
         "Staub. Er hört mit dem ganzen Körper zu, kennt deinen Namen nach einer Minute und hat sich bei einer Ebene noch nie geirrt."),
        ("Every climber who returns tells him how they died, and he trades supplies for their Fragments and the gear they pawn "
         "before a hard climb. His help is real. So is the fact that his business only works while climbers keep dying.",
         "Jeder zurückkehrende Kletterer erzählt ihm, wie er gestorben ist, und er tauscht Vorräte gegen Geistsplitter und gegen "
         "die Ausrüstung, die man vor einem schweren Aufstieg verpfändet. Seine Hilfe ist echt. Echt ist aber auch, dass sein "
         "Geschäft nur läuft, solange Kletterer weiter sterben."),
    ],
    facts=[(R, ("Merchant and soft antagonist", "Händler und sanfter Gegenspieler")),
           (WHERE, ("The offering table in the Threshold", "Am Opfertisch in der Schwelle")),
           (SIG, ("A disc of jade in one front tooth, embroidered red-and-indigo vest, spotless hands",
                  "Eine Jadescheibe in einem Schneidezahn, bestickte Weste in Rot und Indigo, makellos saubere Hände")),
           (("Habit", "Eigenart"), ("Carves a tiny limestone keepsake of whatever killed you, “on the house”",
                                     "Schnitzt ein winziges Kalkstein-Andenken an das, was dich getötet hat, „aufs Haus“"))],
    quote=(("First one's on the house. Everybody gets one. Tell me where it got you.",
            "Das erste geht aufs Haus. Jeder kriegt eins. Erzähl mir, wo es dich erwischt hat."), ("Oxlahun", "Oxlahun")),
    design=("Bright, well-kept layers set him apart from the dusty hall at a glance: crimson sash, red-and-indigo embroidery, a "
            "canvas apron with a great many pockets. His hands are never idle, and when he is calculating they stop all at "
            "once; the stillness is his tell.",
            "Leuchtende, gepflegte Kleidungsschichten heben ihn auf den ersten Blick von der staubigen Halle ab: karmesinrote "
            "Schärpe, Stickerei in Rot und Indigo, eine Segeltuchschürze mit unzähligen Taschen. Seine Hände sind nie untätig, und "
            "wenn er rechnet, halten sie schlagartig inne; diese Reglosigkeit verrät ihn."),
    extras=[("HOME-OXLAHUN", ("At the offering table", "Am Opfertisch")), ("HUB10", ("The offering table", "Der Opfertisch")),
            ("TA-OXLAHUN", ("Turnaround", "Turnaround"))],
)

C["characters/isabel-kaan.html"] = dict(
    name="Dr. Isabel Kaan", role=("The missing mother", "Die verschwundene Mutter"), sheet="CS-ISABEL", banner="HOME-ISABEL", og="HOME-ISABEL",
    lede=("An epigrapher who argued that the Spirit Mural hides a betrayal. The experts dismissed her. Fourteen months ago she vanished.",
          "Eine Epigraphikerin, die behauptete, das Geisterwandbild verberge einen Verrat. Die Fachwelt tat es ab. Vor vierzehn Monaten verschwand sie."),
    hook=("Isabel never appears in the present. She exists through her notebooks, her goggles, Kaya's memories, and what other "
          "people do with her name.",
          "Isabel tritt nie in der Gegenwart auf. Sie existiert durch ihre Notizbücher, ihre Brille, Kayas Erinnerungen und das, "
          "was andere mit ihrem Namen anfangen."),
    intro=[
        ("She grew up speaking Yucatec Maya at home and chose epigraphy because the walls were records her people had written to "
         "be read. Her theory came from fragmentary copies of the temple's glyphs: a seam in spacing and grammar on one panel "
         "that no careless copyist or carver would explain.",
         "Sie wuchs zu Hause mit yukatekischem Maya auf und wählte die Epigraphik, weil die Wände Aufzeichnungen waren, die ihr "
         "Volk geschrieben hatte, um gelesen zu werden. Ihre Theorie stützte sich auf bruchstückhafte Abschriften der Tempelglyphen: "
         "einen Bruch in Abstand und Grammatik auf einer Tafel, den kein nachlässiger Kopist oder Steinmetz erklären würde."),
        ("She never stood in the hall herself. Her last paper breaks off mid-sentence: “consistent with, though I would want to "
         "stand in the hall and see the cut for myself before I”. She is missing, not dead, and the story keeps her that way.",
         "Sie selbst stand nie in der Halle. Ihr letzter Aufsatz bricht mitten im Satz ab: „vereinbar mit, obwohl ich in der Halle "
         "stehen und den Schnitt mit eigenen Augen sehen wollte, bevor ich“. Sie ist verschwunden, nicht tot, und die Geschichte "
         "lässt es dabei."),
    ],
    facts=[(R, ("Backstory character, the expert ignored", "Figur der Vorgeschichte, die übergangene Expertin")),
           (("Age", "Alter"), ("51 when she vanished", "51, als sie verschwand")),
           (SIG, ("A red waxed whipstitch on every strap she ever mended, and a hooked stroke on her shell-glyph zero",
                  "Ein roter gewachster Überwendlichstich an jedem Riemen, den sie je geflickt hat, und ein Haken an ihrer Muschel-Null")),
           (("Habit", "Eigenart"), ("A Book of Mistakes, read aloud once a year on her birthday",
                                     "Ein Buch der Irrtümer, das sie einmal im Jahr an ihrem Geburtstag laut vorlas"))],
    quote=(("A wall doesn't lie, but the reader can.", "Eine Wand lügt nicht, aber der Leser kann es."), ("Dr. Isabel Kaan", "Dr. Isabel Kaan")),
    design=("Isabel shares Kaya's high cheekbones, strong nose and stillness, but she is older, smaller and dressed for decades "
            "of fieldwork: canvas, khaki and a sweat-stained field hat, with the same bronze goggles Kaya now wears. The red "
            "whipstitch is a quiet visual link that Kaya keeps looking for in the temple.",
            "Isabel hat Kayas hohe Wangenknochen, die markante Nase und die Ruhe, ist aber älter, kleiner und für Jahrzehnte "
            "Feldarbeit gekleidet: Segeltuch, Khaki und ein verschwitzter Feldhut, dazu dieselbe Bronzebrille, die nun Kaya trägt. "
            "Der rote Überwendlichstich ist ein stilles visuelles Bindeglied, nach dem Kaya im Tempel immer wieder sucht."),
    extras=[("W08", ("The notebooks Kaya carries", "Die Notizbücher, die Kaya bei sich trägt")), ("TA-ISABEL", ("Turnaround", "Turnaround"))],
)

C["characters/hollow-high-priest.html"] = dict(
    name=("The Hollow High Priest", "Der Hohle Hohepriester"), role=("The summit's keeper", "Der Hüter des Gipfels"),
    sheet="CS-PRIEST", banner="HOME-PRIEST", og="HOME-PRIEST",
    lede=("Once the head of the Sun Temple's priesthood. Now a towering hollow skeleton on the Sky Altar, four stolen lights circling in his chest.",
          "Einst das Oberhaupt der Priesterschaft des Sonnentempels. Heute ein riesiges, hohles Skelett auf dem Himmelsaltar, in dessen Brust vier gestohlene Lichter kreisen."),
    hook=("He has two bodies. On the Spirit Mural he is the tallest figure on the wall, carved living and in his prime. On the "
          "summit he waits as the final boss.",
          "Er hat zwei Körper. Auf dem Geisterwandbild ist er die größte Figur, lebendig und in seinen besten Jahren gemeißelt. "
          "Auf dem Gipfel wartet er als letzter Boss."),
    intro=[
        ("He led the priesthood when the builders still held all four elements and the Sun Portal burned. He was the finest "
         "counter of his generation, trained the order's day-keepers, K'in among them, and the order's authority over what the "
         "mural would say ran through him.",
         "Er führte die Priesterschaft, als die Erbauer noch alle vier Elemente beherrschten und das Sonnenportal brannte. Er war "
         "der beste Zähler seiner Generation, bildete die Tageshüter des Ordens aus, darunter K'in, und über ihn lief die Macht "
         "des Ordens darüber, was das Wandbild erzählen durfte."),
        ("When the balance shattered, he did not rise as a guardian. He rose as something taller and emptier, holding red, green, "
         "white and blue light in his open ribcage, and no gold among them. Whether he caused the betrayal, completed it or only "
         "failed to stop it is held for the finale.",
         "Als das Gleichgewicht zerbrach, erhob er sich nicht als Wächter. Er erhob sich als etwas Größeres, Leereres, mit rotem, "
         "grünem, weißem und blauem Licht in seinem offenen Brustkorb, und keinem Gold darunter. Ob er den Verrat verursacht, "
         "vollendet oder nur nicht verhindert hat, bleibt dem Finale vorbehalten."),
    ],
    facts=[(R, ("Final boss and the story's distant antagonist", "Letzter Boss und ferner Gegenspieler der Geschichte")),
           (WHERE, ("The Sky Altar, on the summit", "Der Himmelsaltar, auf dem Gipfel")),
           (SIG, ("A fan of tail feathers like a second sun, jade ear spools, four lights in an open ribcage",
                  "Ein Fächer aus Schwanzfedern wie eine zweite Sonne, Jade-Ohrpflöcke, vier Lichter in einem offenen Brustkorb")),
           (("In life", "Zu Lebzeiten"), ("He kept stingless bees, and gave honey to every novice who first kept the count correctly",
                                          "Er hielt stachellose Bienen und gab jedem Novizen Honig, der zum ersten Mal richtig zählte"))],
    quote=(("The sun does not ask to be checked.", "Die Sonne verlangt nicht, überprüft zu werden."),
           ("Attributed to the high priest", "Dem Hohepriester zugeschrieben")),
    design=("His cold, many-coloured glow throws his shadow in four directions at once, a deliberate opposite of K'in's single, "
            "warm, slightly too long shadow. The skull keeps the sloped brow of his mural portrait, so the carved man can still "
            "be read in the bone.",
            "Sein kaltes, vielfarbiges Leuchten wirft seinen Schatten in vier Richtungen zugleich, als bewusster Gegensatz zu K'ins "
            "einzelnem, warmem, etwas zu langem Schatten. Der Schädel behält die fliehende Stirn seines Wandbildporträts, sodass "
            "man den gemeißelten Mann noch im Knochen erkennt."),
    extras=[("HOME-PRIEST", ("On the Sky Altar", "Auf dem Himmelsaltar")), ("E17", ("Boss sheet", "Boss-Blatt")),
            ("TA-PRIEST", ("Turnaround", "Turnaround"))],
)

# ================================================================== Risen Guardians
C["characters/guardians/ah-kuk.html"] = dict(
    name="Ah Kuk", role=("Receiver of Offerings", "Empfänger der Opfergaben"), sheet="CS-AHKUK", banner="A-03", group=GUARD,
    sheet_caption=("Risen Ah Kuk, turnaround", "Der erweckte Ah Kuk, Turnaround"),
    lede=("A long-boned guardian seated on the lowest step of the dais, so grey with dust that every climber takes him for an offering.",
          "Ein langgliedriger Wächter auf der untersten Stufe des Podests, so grau vor Staub, dass ihn jeder Kletterer für eine Opfergabe hält."),
    hook=("Ah Kuk sits cross-legged with his hands on his knees, palms up, the posture of someone waiting to be handed something.",
          "Ah Kuk sitzt im Schneidersitz, die Hände auf den Knien, die Handflächen nach oben, wie jemand, der darauf wartet, dass man ihm etwas reicht."),
    intro=[
        ("In the builders' day he stood at the foot of the base hall, received what the faithful brought and entered it in the "
         "count. Every living person entering the temple had to pass him. He knew who came in and what they carried.",
         "Zur Zeit der Erbauer stand er am Fuß der Grundhalle, nahm entgegen, was die Gläubigen brachten, und trug es in die "
         "Zählung ein. Jeder Lebende, der den Tempel betrat, musste an ihm vorbei. Er wusste, wer hereinkam und was er bei sich trug."),
        ("When he rises, he comes up in stages, like an old man getting up from a bench, and dust pours off him in sheets. He is "
         "the hall's one unrecorded dead: K'in carves every climber, but she has never carved him.",
         "Wenn er sich erhebt, dann in Etappen, wie ein alter Mann, der von einer Bank aufsteht, und der Staub rieselt in Schwaden "
         "von ihm herab. Er ist der einzige Tote der Halle, der nirgends festgehalten ist: K'in meißelt jeden Kletterer, ihn aber nie."),
    ],
    facts=[(R, ("Named guardian, the Threshold", "Benannter Wächter, die Schwelle")),
           (WHERE, ("Lowest step of the dais, against the left sealed portal", "Unterste Stufe des Podests, am linken versiegelten Portal")),
           (STATE, ("Dormant, until the hall asks the wrong question", "Ruhend, bis in der Halle die falsche Frage gestellt wird")),
           (SIG, ("A cold, pale sigil in a cartouche frame; a game board scratched into the step beside him",
                  "Ein kaltes, blasses Siegel in einer Kartusche; ein Spielbrett, in die Stufe neben ihm geritzt"))],
    quote=(("Count it twice. Say it once.", "Zweimal zählen. Einmal sagen."), ("Ah Kuk, in life", "Ah Kuk, zu Lebzeiten")),
    design=("Standing, he is a head taller than Oxlahun and very thin, the wrapping sagging where the body has dried away. His "
            "sigil glows a cold silver-white, deliberately outside the four elemental colours, so no one reads an element into him.",
            "Aufgerichtet ist er einen Kopf größer als Oxlahun und sehr hager, die Bandagen hängen dort durch, wo der Körper "
            "darunter vertrocknet ist. Sein Siegel leuchtet kalt silberweiß, bewusst außerhalb der vier Elementarfarben, damit "
            "niemand ein Element in ihm sieht."),
    extras=[("E03", ("Seated and risen", "Sitzend und erweckt")), ("TA-AHKUK", ("Turnaround", "Turnaround"))],
)

C["characters/guardians/ix-nicte.html"] = dict(
    name="Ix Nicte", role=("Keeper of the First Step", "Hüterin der ersten Stufe"), sheet="CS-IXNICTE", banner="B-03", group=GUARD,
    lede=("A slight guardian standing ankle-deep in the Shell's flooded atrium, her bound hands closed around a single dried plumeria blossom.",
          "Eine zierliche Wächterin, die knöcheltief im überfluteten Atrium von The Shell steht, die gebundenen Hände um eine einzige getrocknete Frangipaniblüte geschlossen."),
    hook=("She is the first Risen Guardian Kaya sees, and the one K'in appears to recognize.",
          "Sie ist die erste Erweckte Wächterin, die Kaya sieht, und die einzige, die K'in zu erkennen scheint."),
    intro=[
        ("In the builders' day the atrium held a ritual pool. Novices crossed it and took a nikte' blossom from the hands of the "
         "woman at the step, the first thing the order ever gave them. Her name means plumeria.",
         "Zur Zeit der Erbauer lag im Atrium ein Ritualbecken. Novizen durchquerten es und erhielten von der Frau an der Stufe eine "
         "Nikte'-Blüte, das erste Geschenk des Ordens an sie. Ihr Name bedeutet Frangipani."),
        ("Her wrappings are bound in a single unbroken spiral with a flat knot at every hand's width. Whoever did it loved her, or "
         "was very good at it. When Kaya passes, K'in's hints stop and her trail of light hangs on the woman's shoulders for "
         "the length of a slow breath.",
         "Ihre Bandagen sind in einer einzigen ununterbrochenen Spirale gewickelt, mit einem flachen Knoten alle Handbreit. Wer "
         "das getan hat, hat sie geliebt oder war sehr geschickt darin. Als Kaya vorbeigeht, verstummen K'ins Hinweise, und ihre "
         "Lichtspur verweilt einen langen Atemzug lang auf den Schultern der Frau."),
    ],
    facts=[(R, ("Named guardian, the Shell", "Benannte Wächterin, The Shell")),
           (WHERE, ("A half-submerged step on the east wall of the atrium", "Eine halb versunkene Stufe an der Ostwand des Atriums")),
           (STATE, ("Dormant; she does not rise in the story", "Ruhend; in der Geschichte erhebt sie sich nicht")),
           (SIG, ("A plumeria glazed in amber wax, a folded palm-leaf whistle at her hip, one drip per breath",
                  "Eine in Bernsteinwachs glasierte Frangipani, eine gefaltete Palmblattpfeife an der Hüfte, ein Tropfen pro Atemzug"))],
    quote=(("Cross slowly. The first step is the one that remembers you.",
            "Geh langsam hinüber. Die erste Stufe ist die, die sich an dich erinnert."), ("Ix Nicte, in life", "Ix Nicte, zu Lebzeiten")),
    design=("Finer cloth than the other guardians, candle-wax yellow above the waterline and tea-stained below it. She is gentle "
            "and sorrowful rather than threatening: a figure standing the way people wait at a landing for a boat.",
            "Feinerer Stoff als bei den anderen Wächtern, kerzenwachsgelb über der Wasserlinie und teefarben darunter. Sie wirkt "
            "sanft und traurig statt bedrohlich: eine Gestalt, die dasteht, wie man an einem Steg auf ein Boot wartet."),
    extras=[("E04", ("Creature sheet", "Kreaturen-Blatt")), ("TA-IXNICTE", ("Turnaround", "Turnaround"))],
)

C["characters/guardians/chak-tun.html"] = dict(
    name="Chak Tun", role=("Warden of the Panels", "Wächter der Tafeln"), sheet="CS-CHAKTUN", banner="HOME-KIN", group=GUARD,
    lede=("The only named guardian carved into the wall instead of standing in the hall, at the very edge of the panel that was re-cut.",
          "Der einzige benannte Wächter, der in die Wand gemeißelt ist, statt in der Halle zu stehen, direkt am Rand der Tafel, die nachgemeißelt wurde."),
    hook=("A modest figure with a staff stands just outside the betrayal panel, his head turned back over his shoulder. He is the "
          "only figure on the wall who looks back.",
          "Eine bescheidene Gestalt mit Stab steht gleich neben der Verratstafel, den Kopf über die Schulter zurückgewandt. Er ist "
          "die einzige Figur auf der Wand, die zurückblickt."),
    intro=[
        ("In life he walked the length of the wall at dawn and dusk, looking for anything that had changed. He could say what "
         "the wall had looked like on any given day.",
         "Zu Lebzeiten schritt er bei Morgengrauen und Abenddämmerung die Wand ab und suchte nach allem, was sich verändert hatte. "
         "Er konnte sagen, wie die Wand an jedem beliebigen Tag ausgesehen hatte."),
        ("His name cartouche is cut short: the deeper recess of the neighbouring panel overruns the old border by two fingers' "
         "width and cuts straight through it. Under flat light the overrun is invisible. Under raking light it is the one record "
         "in the hall that tells the order of events without being asked.",
         "Seine Namenskartusche ist gekappt: Die tiefere Aussparung der Nachbartafel überschreitet die alte Randlinie um zwei "
         "Fingerbreit und schneidet mitten hindurch. Bei flachem Licht ist die Überschneidung unsichtbar. Bei Streiflicht ist sie "
         "die einzige Aufzeichnung der Halle, die die Reihenfolge der Ereignisse verrät, ohne gefragt zu werden."),
    ],
    facts=[(R, ("Named guardian, carved on the Spirit Mural", "Benannter Wächter, auf dem Geisterwandbild gemeißelt")),
           (WHERE, ("Left margin of the betrayal panel", "Linker Rand der Verratstafel")),
           (STATE, ("A carving; a risen design exists for later", "Ein Relief; ein erweckter Entwurf existiert für später")),
           (SIG, ("A bulge in his cheek: he chewed chicle through every watch", "Eine Wölbung in der Wange: Er kaute auf jeder Wache Chicle"))],
    quote=(("Nobody reads the margin. That is why someone has to stand in it.",
            "Niemand liest den Rand. Deshalb muss jemand darin stehen."), ("Chak Tun, in life", "Chak Tun, zu Lebzeiten")),
    design=("His sheet shows the carving twice, under flat front light (how K'in lights it) and under low raking light (how Kaya "
            "reads it), plus a risen version that keeps the frozen posture: staff grounded, head forever turned back.",
            "Sein Blatt zeigt das Relief zweimal, bei flachem Frontlicht (so beleuchtet es K'in) und bei flachem Streiflicht (so "
            "liest es Kaya), dazu eine erweckte Version, die die erstarrte Haltung beibehält: Stab aufgestützt, Kopf für immer "
            "zurückgewandt."),
    extras=[("TA-CHAKTUN", ("Turnaround", "Turnaround"))],
)

C["characters/guardians/ah-zac.html"] = dict(
    name="Ah Zac", role=("Sweeper of the White Way", "Feger des Weißen Wegs"), sheet="CS-AHZAC", banner="A-03", group=GUARD,
    lede=("A small guardian frozen mid-sweep at the foot of the dais, so still that every climber files him as a statue.",
          "Ein kleiner Wächter, mitten im Fegen erstarrt am Fuß des Podests, so reglos, dass ihn jeder Kletterer für eine Statue hält."),
    hook=("Bent at the waist, one foot forward, both hands closed on a palm-fibre broom, Ah Zac faces the middle portal and has "
          "never finished his stroke.",
          "Vornübergebeugt, einen Fuß vor, beide Hände um einen Besen aus Palmfasern geschlossen, steht Ah Zac vor dem mittleren "
          "Portal und hat seinen Strich nie beendet."),
    intro=[
        ("He kept the limewashed strip between the altar and the portals white, so that nobody walking toward the portal ever "
         "stepped on a loose chip. Every dawn he drew the day's sign in the lime dust with his broom handle, always with a tiny "
         "lizard in the corner, and every dusk he swept it away.",
         "Er hielt den gekalkten Streifen zwischen Altar und Portalen weiß, damit niemand auf dem Weg zum Portal je auf einen "
         "losen Splitter trat. Jeden Morgen zeichnete er mit dem Besenstiel das Zeichen des Tages in den Kalkstaub, immer mit einer "
         "winzigen Eidechse in der Ecke, und jeden Abend fegte er es fort."),
        ("Thirty years of that left a glassy, polished patch at the foot of the step: the hall's one record that was always meant "
         "to vanish. The broom is worn into a long slant along one edge. A sculptor can carve a broom, but only a hand can wear one.",
         "Dreißig Jahre davon hinterließen eine glasig polierte Stelle am Fuß der Stufe: die einzige Aufzeichnung der Halle, die "
         "immer verschwinden sollte. Der Besen ist an einer Kante schräg abgenutzt. Ein Bildhauer kann einen Besen meißeln, aber "
         "nur eine Hand kann ihn abnutzen."),
    ],
    facts=[(R, ("Named guardian, the Threshold", "Benannter Wächter, die Schwelle")),
           (WHERE, ("Foot of the dais, facing the middle portal", "Am Fuß des Podests, mit Blick auf das mittlere Portal")),
           (STATE, ("Dormant, mid-stroke", "Ruhend, mitten im Strich")),
           (SIG, ("Lime-white wrappings that crack like plaster; a broom worn by years of the same stroke",
                  "Kalkweiße Bandagen, die wie Gips reißen; ein Besen, abgenutzt von jahrelang demselben Strich"))],
    quote=(("Mind your feet, friend. I've only just made it white.",
            "Pass auf deine Füße auf, Freund. Ich hab's gerade erst weiß gemacht."), ("Ah Zac, in life", "Ah Zac, zu Lebzeiten")),
    design=("The smallest guardian, and the only one whose wrappings are white instead of brown. Stooped, he stands below an "
            "adult's shoulder; his sigil faces the floor and stays hidden. If he ever rises, it lights the white floor first, "
            "like low moonlight.",
            "Der kleinste Wächter und der einzige, dessen Bandagen weiß statt braun sind. Gebückt reicht er einem Erwachsenen "
            "nicht bis zur Schulter; sein Siegel zeigt zum Boden und bleibt verborgen. Sollte er sich je erheben, erleuchtet es "
            "zuerst den weißen Boden, wie tief stehendes Mondlicht."),
    extras=[("E05", ("Creature sheet", "Kreaturen-Blatt")), ("HUB13", ("His broom and the polished floor", "Sein Besen und der polierte Boden"))],
)

C["characters/guardians/kan-uk.html"] = dict(
    name="Kan Uk", role=("The guardian in the niche", "Der Wächter in der Nische"), sheet="CS-KANUK", banner="A-03", group=GUARD,
    lede=("A lean guardian in a wall niche, with a scrap of modern cloth tucked at his shoulder that no loom in this temple could have made.",
          "Ein hagerer Wächter in einer Wandnische, mit einem Fetzen modernem Stoff an der Schulter, den kein Webstuhl dieses Tempels hätte herstellen können."),
    hook=("Kan Uk has stood in the same niche for a very long time and has never once crossed the room.",
          "Kan Uk steht seit sehr langer Zeit in derselben Nische und hat den Raum nie durchquert."),
    intro=[
        ("At his left shoulder, beneath the wrapping, is a rectangle of dark, tightly woven twill with a hemmed edge and a few "
         "machine-regular stitches. His right thumb and forefinger are worn thin from rubbing it.",
         "An seiner linken Schulter steckt unter den Bandagen ein Rechteck aus dunklem, dicht gewebtem Köperstoff mit gesäumter "
         "Kante und ein paar maschinengleichen Stichen. Sein rechter Daumen und Zeigefinger sind vom Reiben daran ganz dünn."),
        ("He may be a priest of the old order who picked up a foreign scrap over the years. Or the man inside the wrappings was "
         "once a climber, someone who died here and kept the one piece of his old life the curse could not rot. The story holds both.",
         "Vielleicht ist er ein Priester des alten Ordens, der über die Jahre einen fremden Fetzen aufgelesen hat. Oder der Mann "
         "in den Bandagen war einst ein Kletterer, der hier starb und das eine Stück seines alten Lebens behielt, das der Fluch "
         "nicht verrotten lassen konnte. Die Geschichte lässt beides offen."),
    ],
    facts=[(R, ("Named guardian, the Threshold", "Benannter Wächter, die Schwelle")),
           (WHERE, ("A carved wall niche", "Eine gemeißelte Wandnische")),
           (STATE, ("Dormant; never leaves his niche", "Ruhend; verlässt seine Nische nie")),
           (SIG, ("A banked amber sigil, unlike the others; he turns his face up into the sunbeam",
                  "Ein glimmendes Bernsteinsiegel, anders als bei den anderen; er hebt sein Gesicht in den Sonnenstrahl"))],
    quote=(("The rasp. A pause. The rasp again.", "Das Schaben. Eine Pause. Wieder das Schaben."),
           ("How the story renders him", "Wie die Geschichte ihn beschreibt")),
    design=("The only guardian whose sigil is amber instead of silver-white, like an ember under ash. The navy twill patch is the "
            "single modern-looking element on any guardian, and it should read immediately as out of place.",
            "Der einzige Wächter, dessen Siegel bernsteinfarben statt silberweiß ist, wie Glut unter Asche. Der marineblaue "
            "Köperflicken ist das einzige modern wirkende Element an einem Wächter und soll sofort als fehl am Platz auffallen."),
    extras=[("E06", ("Creature sheet", "Kreaturen-Blatt")), ("TA-KANUK", ("Turnaround", "Turnaround"))],
)

# ================================================================== Carved Climbers
C["characters/climbers/mateo-vance.html"] = dict(
    name="Mateo Vance", role=("The surveyor", "Der Landvermesser"), sheet="CS-MATEO", banner="HOME-KIN", group=CLIMB,
    lede=("A broad-shouldered surveyor carved mid-measurement, one eye shut, sighting along a tall notched staff.",
          "Ein breitschultriger Landvermesser, mitten im Messen gemeißelt, ein Auge geschlossen, über einen hohen gekerbten Stab peilend."),
    hook=("Mateo is the only carved climber shown working rather than standing, as if the survey were still in progress.",
          "Mateo ist der einzige gemeißelte Kletterer, der bei der Arbeit gezeigt wird statt stehend, als liefe die Vermessung noch."),
    intro=[
        ("He brought professional tools into a building whose upper floors rearrange themselves to trap intruders. There is a "
         "cruel irony in a man whose craft depends on fixed points working in a pyramid built to move them.",
         "Er brachte professionelle Werkzeuge in ein Bauwerk, dessen obere Ebenen sich neu anordnen, um Eindringlinge zu fangen. "
         "Es liegt eine grausame Ironie darin, dass ein Mann, dessen Handwerk von festen Punkten lebt, in einer Pyramide arbeitete, "
         "die gebaut wurde, um sie zu verschieben."),
        ("His carving is the finest on the wall, so Kaya uses it as her comparison sample for tool marks. The seventeen notches "
         "on his staff may be graduations, or they may be tallies. A surveyor's unit and a captive's count of days look the same "
         "in stone.",
         "Sein Relief ist das feinste auf der Wand, deshalb nutzt Kaya es als Vergleichsprobe für Werkzeugspuren. Die siebzehn "
         "Kerben auf seinem Stab können Maßstriche sein oder Strichlisten. Die Maßeinheit eines Vermessers und die Tageszählung "
         "eines Gefangenen sehen in Stein gleich aus."),
    ],
    facts=[(R, ("Carved Climber, lost to the loop", "Gemeißelter Kletterer, an die Schleife verloren")),
           (SIG, ("A notched staff, a dented hat brim, a closed sighting eye", "Ein gekerbter Stab, eine eingedellte Hutkrempe, ein geschlossenes Peilauge")),
           (("In life", "Zu Lebzeiten"), ("A field surveyor in khaki with a plumb bob at his belt", "Ein Feldvermesser in Khaki mit Senklot am Gürtel"))],
    quote=(("Seventeen notches above the grip. Even intervals. Too even for a decoration.",
            "Siebzehn Kerben über dem Griff. Gleichmäßige Abstände. Zu gleichmäßig für eine Verzierung."), ("Kaya's notebook", "Kayas Notizbuch")),
    design=("Every Carved Climber sheet leads with the relief, shown under flat light and under raking light, followed by a smaller "
            "in-life design in muted colours.",
            "Jedes Blatt der gemeißelten Kletterer beginnt mit dem Relief, bei flachem Licht und bei Streiflicht, gefolgt von einem "
            "kleineren Entwurf der Figur zu Lebzeiten in gedeckten Farben."),
    extras=[("TA-MATEO", ("In-life turnaround", "Turnaround zu Lebzeiten"))],
)

C["characters/climbers/lisbet.html"] = dict(
    name="Lisbet", role=("The one who held the line", "Die das Seil hielt"), sheet="CS-LISBET", banner="HOME-KIN", group=CLIMB,
    lede=("An older climber with a heavy coil of rope and an open hand reaching toward empty stone. She is almost smiling.",
          "Eine ältere Kletterin mit einer schweren Seilrolle und einer offenen Hand, die nach leerem Stein greift. Sie lächelt beinahe."),
    hook=("The rope's free end finishes in a neat loop, sized for a waist other than hers.",
          "Das freie Seilende läuft in eine saubere Schlinge aus, bemessen für eine andere Taille als ihre."),
    intro=[
        ("She came older and more experienced than the climbers Kaya imagines, with rope enough for two, which suggests she meant "
         "to bring someone through. No one is carved beside her.",
         "Sie kam älter und erfahrener als die Kletterer, die Kaya sich vorstellt, mit Seil für zwei, was nahelegt, dass sie jemanden "
         "hindurchbringen wollte. Neben ihr ist niemand gemeißelt."),
        ("The carver kept her laugh lines instead of smoothing them away. Lisbet breaks the pattern Kaya assumed about who the "
         "loop takes: she cannot be filed under greed.",
         "Der Steinmetz hat ihre Lachfalten bewahrt, statt sie zu glätten. Lisbet bricht das Muster, das Kaya über die Opfer der "
         "Schleife angenommen hatte: Unter Gier lässt sie sich nicht einordnen."),
    ],
    facts=[(R, ("Carved Climber, lost to the loop", "Gemeißelte Kletterin, an die Schleife verloren")),
           (SIG, ("A three-strand rope coil, an empty loop, an open hand", "Eine dreischäftige Seilrolle, eine leere Schlinge, eine offene Hand")),
           (("In life", "Zu Lebzeiten"), ("A practical older climber in layered work clothes and gloves", "Eine praktische ältere Kletterin in Arbeitskleidung und Handschuhen"))],
    quote=(("She was careful.", "Sie war vorsichtig."), ("K'in", "K'in")),
    design=("The only carved climber with a trace of a smile, and the only one whose open hand reaches toward nothing. The loop "
            "and the hand read together as an unfinished sentence.",
            "Die einzige gemeißelte Kletterin mit der Spur eines Lächelns und die einzige, deren offene Hand ins Leere greift. "
            "Schlinge und Hand lesen sich zusammen wie ein unvollendeter Satz."),
    extras=[("TA-LISBET", ("In-life turnaround", "Turnaround zu Lebzeiten"))],
)

C["characters/climbers/joaquin-reyes.html"] = dict(
    name="Joaquin Reyes", role=("The one who carried his own light", "Der sein eigenes Licht trug"), sheet="CS-JOAQUIN",
    banner="HOME-KIN", group=CLIMB,
    lede=("The youngest-looking climber on the wall, mid-stride, chin lifted, holding an open lantern at arm's length.",
          "Der jüngste Kletterer auf der Wand, mitten im Schritt, das Kinn erhoben, eine offene Laterne auf Armlänge vor sich."),
    hook=("Why would a climber with a spirit guide carry a light of his own?",
          "Warum sollte ein Kletterer mit einer Geistführerin ein eigenes Licht tragen?"),
    intro=[
        ("His lantern's flame is the deepest cut on the entire wall, a tight star of rays that run farther than the figure needs. "
         "When the sunbeam from the ceiling crack crosses it, the carved lantern looks lit.",
         "Die Flamme seiner Laterne ist der tiefste Schnitt auf der ganzen Wand, ein enger Stern aus Strahlen, die weiter reichen, "
         "als die Figur es bräuchte. Wenn der Sonnenstrahl aus dem Deckenspalt darüberstreicht, scheint die gemeißelte Laterne zu brennen."),
        ("A climber who trusted K'in's light completely would not have brought a second one. He brought his own to check the "
         "passage against what he was told, which makes him Kaya's predecessor.",
         "Ein Kletterer, der K'ins Licht völlig vertraut hätte, hätte kein zweites mitgebracht. Er brachte sein eigenes mit, um "
         "den Weg mit dem zu vergleichen, was man ihm erzählte, und ist damit Kayas Vorgänger."),
    ],
    facts=[(R, ("Carved Climber, lost to the loop", "Gemeißelter Kletterer, an die Schleife verloren")),
           (SIG, ("An open cage lantern, a shielding hand, sleeves a little too long", "Eine offene Käfiglaterne, eine schützende Hand, etwas zu lange Ärmel")),
           (("In life", "Zu Lebzeiten"), ("A young explorer in an oversized field jacket with a brass lantern", "Ein junger Entdecker in zu großer Feldjacke mit Messinglaterne"))],
    quote=(("Rays cut deeper than the figure. Shutter open. A hand held out to shelter a flame in a room with no wind.",
            "Strahlen tiefer geschnitten als die Figur. Klappe offen. Eine Hand, die eine Flamme schützt, in einem Raum ohne Wind."),
           ("Kaya's notebook", "Kayas Notizbuch")),
    design=("Cut with a looser, quicker confidence than the careful work around him. His sheet shows the relief once in shadow "
            "and once with daylight crossing it, so the carved flame seems to catch.",
            "Mit lockererer, schnellerer Sicherheit gemeißelt als die sorgfältige Arbeit um ihn herum. Sein Blatt zeigt das Relief "
            "einmal im Schatten und einmal mit einfallendem Tageslicht, sodass die gemeißelte Flamme aufzuleuchten scheint."),
    extras=[("TA-JOAQUIN", ("In-life turnaround", "Turnaround zu Lebzeiten"))],
)

C["characters/climbers/wren.html"] = dict(
    name="Wren", role=("The one who looks like Kaya", "Die Gestalt, die Kaya gleicht"), sheet="CS-WREN", banner="HOME-KIN", group=CLIMB,
    lede=("A small, quiet figure, head bent, one hand hidden inside a satchel whose buckle matches Kaya's own, stroke for stroke.",
          "Eine kleine, stille Gestalt, den Kopf gesenkt, eine Hand in einer Umhängetasche verborgen, deren Schnalle Strich für Strich der von Kaya gleicht."),
    hook=("Wren's age and gender are left open. What is not open is the buckle.",
          "Wrens Alter und Geschlecht bleiben offen. Nicht offen ist die Schnalle."),
    intro=[
        ("Wren came equipped for documentation: a satchel, a flap built to open quickly, the shape of a brush or a rolled page at "
         "its mouth. The carver hid the hand that reaches inside, so the gesture stays interrupted.",
         "Wren kam ausgerüstet zum Dokumentieren: eine Umhängetasche, eine Klappe, die sich schnell öffnen lässt, die Form eines "
         "Pinsels oder einer gerollten Seite an der Öffnung. Der Steinmetz hat die Hand verborgen, die hineingreift, sodass die "
         "Geste unterbrochen bleibt."),
        ("If K'in remembers her climbers as versions of one another, then Kaya may have been carved not because she is new, but "
         "because she is familiar. Wren is the warning that a careful reader can be absorbed into the very record she reads.",
         "Wenn K'in ihre Kletterer als Versionen voneinander in Erinnerung behält, dann wurde Kaya vielleicht nicht gemeißelt, weil "
         "sie neu ist, sondern weil sie vertraut ist. Wren ist die Warnung, dass eine sorgfältige Leserin von genau der Aufzeichnung "
         "verschluckt werden kann, die sie liest."),
    ],
    facts=[(R, ("Carved Climber, lost to the loop", "Gemeißelte Gestalt, an die Schleife verloren")),
           (SIG, ("A half-open satchel, a hidden hand, Kaya's buckle", "Eine halb offene Tasche, eine verborgene Hand, Kayas Schnalle")),
           (("In life", "Zu Lebzeiten"), ("A slight young scholar bent over an open notebook", "Eine zierliche junge Gelehrte, über ein offenes Notizbuch gebeugt"))],
    quote=(("Same buckle. Same cut, same angle, down to the final stroke.",
            "Dieselbe Schnalle. Derselbe Schnitt, derselbe Winkel, bis zum letzten Strich."), ("Kaya's notebook", "Kayas Notizbuch")),
    design=("Noticeably smaller than the other climbers, on purpose. The sheet includes a side-by-side close-up of Wren's buckle "
            "and the buckle on Kaya's freshly carved likeness.",
            "Bewusst deutlich kleiner als die anderen Kletterer. Das Blatt enthält eine Nahaufnahme, die Wrens Schnalle neben die "
            "Schnalle von Kayas frisch gemeißeltem Abbild stellt."),
    extras=[("TA-WREN", ("In-life turnaround", "Turnaround zu Lebzeiten"))],
)

C["characters/climbers/odalys.html"] = dict(
    name="Odalys", role=("The unfinished carving", "Das unvollendete Relief"), sheet="CS-ODALYS", banner="HOME-KIN", group=CLIMB,
    lede=("The only likeness on the wall that was never finished: the left half polished, the right half still a rough block.",
          "Das einzige Abbild auf der Wand, das nie vollendet wurde: die linke Hälfte poliert, die rechte noch ein grober Block."),
    hook=("Her finished hand is a closed fist, and whatever it holds is hidden inside it.",
          "Ihre vollendete Hand ist eine geschlossene Faust, und was sie hält, bleibt darin verborgen."),
    intro=[
        ("Her cartouche is cut only as far as its first few signs, so even her name is incomplete. The last stroke on the border "
         "ends in a skid instead of a clean lift, and the chips on the ledge below are old and dull.",
         "Ihre Kartusche ist nur bis zu den ersten Zeichen gemeißelt, sodass selbst ihr Name unvollständig ist. Der letzte Strich "
         "am Rand endet in einem Ausrutscher statt in einem sauberen Absetzen, und die Splitter auf dem Sims darunter sind alt und stumpf."),
        ("A carver who was interrupted and a carver who chose to stop look identical in stone. Odalys proves the carving is a "
         "choice made in time, not an automatic effect of the loop.",
         "Ein Steinmetz, der unterbrochen wurde, und einer, der aufhören wollte, sehen in Stein gleich aus. Odalys beweist, dass "
         "das Meißeln eine Entscheidung in der Zeit ist und keine automatische Folge der Schleife."),
    ],
    facts=[(R, ("Carved Climber, fate unsettled", "Gemeißelte Kletterin, Schicksal ungeklärt")),
           (SIG, ("Half carved, half raw stone; a closed fist; a half-cut name", "Halb gemeißelt, halb roher Stein; eine geschlossene Faust; ein halb gemeißelter Name")),
           (("In life", "Zu Lebzeiten"), ("Deliberately not shown", "Bewusst nicht gezeigt"))],
    quote=(("She is...", "Sie ist ..."), ("K'in, before she corrects herself to the past tense", "K'in, bevor sie sich in die Vergangenheit korrigiert")),
    design=("No in-life design, by intention. Her sheet adds a reference strip of the three stages of Maya relief carving: "
            "scribed layout, point-chisel roughing and flat-chisel finish.",
            "Bewusst kein Entwurf zu Lebzeiten. Ihr Blatt ergänzt einen Referenzstreifen mit den drei Stufen der Maya-Reliefkunst: "
            "angerissene Vorzeichnung, Bossieren mit dem Spitzeisen und Feinschliff mit dem Flacheisen."),
    extras=[],
)


# ------------------------------------------------------------------ overview & groups
def overview(ctx):
    t = ctx.t
    living = [
        (ctx.pick("HOME-KAYA", "CS-KAYA"), "Kaya", t("The reader", "Die Leserin"), "characters/kaya.html"),
        (ctx.pick("HOME-KIN", "CS-KIN"), "K'in", t("The spirit guide", "Die Geistführerin"), "characters/kin.html"),
        (ctx.pick("HOME-OXLAHUN", "CS-OXLAHUN"), "Oxlahun", t("The trader", "Der Händler"), "characters/oxlahun.html"),
        (ctx.pick("HOME-ISABEL", "CS-ISABEL"), "Dr. Isabel Kaan", t("The missing mother", "Die verschwundene Mutter"), "characters/isabel-kaan.html"),
    ]
    order = [
        ("CS-GUARDIAN", t("The Risen Guardians", "Die Erweckten Wächter"), t("Five named guardians", "Fünf benannte Wächter"),
         "characters/guardians/index.html"),
        (ctx.pick("HOME-PRIEST", "CS-PRIEST"), t("The Hollow High Priest", "Der Hohle Hohepriester"), t("The summit's keeper", "Der Hüter des Gipfels"),
         "characters/hollow-high-priest.html"),
        ("CS-CLIMBERS", t("The Carved Climbers", "Die gemeißelten Kletterer"), t("Five lost climbers", "Fünf verlorene Kletterer"),
         "characters/climbers/index.html"),
    ]
    more = [
        ("E01", t("Creatures & Bosses", "Kreaturen & Bosse"), t("Everything that fights back", "Alles, was sich wehrt"), "characters/creatures.html"),
        ("CS-LINEUP", t("Cast Lineup", "Größenvergleich"), t("Everyone at true scale", "Alle im echten Maßstab"), "characters/lineup.html"),
    ]
    row = lambda items, cls: f'<div class="cards {cls}">' + "".join(card(ctx, *i) for i in items) + "</div>"
    return f"""
<section class="wrap section narrow-top">
  <div class="prose"><p class="big">{t("Every figure in the temple keeps or bends a record. Kaya records the past, K'in edits it, Oxlahun sells it, "
                                       "and Isabel only ever asked to have hers checked.",
                                       "Jede Figur im Tempel bewahrt oder verbiegt eine Aufzeichnung. Kaya hält die Vergangenheit fest, K'in "
                                       "redigiert sie, Oxlahun verkauft sie, und Isabel bat immer nur darum, dass man ihre überprüft.")}</p></div>
</section>
<section class="band"><div class="wrap section">
  <p class="kicker">{t("The living", "Die Lebenden")}</p><h2>{t("Who Climbers meet", "Wem Kletterer begegnen")}</h2>
  {row(living, "cards-4")}
</div></section>
<section class="wrap section">
  <p class="kicker">{t("The order and the lost", "Der Orden und die Verlorenen")}</p><h2>{t("Who the temple kept", "Wen der Tempel behielt")}</h2>
  {row(order, "cards-3")}
</div></section>
<section class="band"><div class="wrap section">
  <p class="kicker">{t("And more", "Und mehr")}</p><h2>{t("Creatures and scale", "Kreaturen und Maßstab")}</h2>
  {row(more, "cards-2")}
</div></section>
"""


def group_page(intro_fn, sheet, members, extras=()):
    def body(ctx):
        t = ctx.t
        cards = "".join(card(ctx, img, n, T(ctx, r), p) for img, n, r, p in members)
        return f"""
<section class="wrap section narrow-top">
  <div class="prose">{intro_fn(ctx)}</div>
</section>
<section class="band"><div class="wrap section">
  {ctx.figure(sheet, t("In action", "In Aktion") if ctx.has("ACT-" + sheet) else t("Group sheet", "Gruppenblatt"), cls="sheet")}
  {extras_gallery(ctx, list(extras))}
</div></section>
<section class="wrap section">
  <p class="kicker">{t("Named", "Benannt")}</p><h2>{t("Meet each of them", "Lerne jeden von ihnen kennen")}</h2>
  <div class="cards cards-5">{cards}</div>
</section>
"""
    return body


def guardians_intro(ctx):
    t = ctx.t
    return (f'<p class="big">{t("The cursed priests of the Sun Temple still walk its halls, wrapped like funerary bundles, a cold sigil glowing on each chest.", "Die verfluchten Priester des Sonnentempels wandeln noch immer durch seine Hallen, eingewickelt wie Grabbündel, ein kalt leuchtendes Siegel auf jeder Brust.")}</p>'
            f'<p>{t("In play they are the base enemy: they shamble, swing and rise from dust. In the story, the five named guardians are people with a post and a posture. Each held a modest rank in an order that measured rank by scale, and each still holds the pose the curse found them in. Their sigils glow a cold silver-white, never one of the four elemental colours.", "Im Spiel sind sie der Grundgegner: Sie schlurfen, schlagen zu und erheben sich aus dem Staub. In der Geschichte sind die fünf benannten Wächter Menschen mit einem Posten und einer Haltung. Jeder hatte einen bescheidenen Rang in einem Orden, der Rang an der Größe maß, und jeder verharrt noch in der Pose, in der ihn der Fluch fand. Ihre Siegel leuchten kalt silberweiß, nie in einer der vier Elementarfarben.")}</p>'
            f'<p>{t("In the game the five named guardians return as elites: each appears once per tier as the last fight of a floor, with its own sigil and one gift of the curse, a shield, a summons, a leap, a cleave or a curse.", "Im Spiel kehren die fünf benannten Wächter als Elitegegner zurück: Jeder erscheint einmal pro Stufe als letzter Kampf einer Ebene, mit eigenem Siegel und einer Gabe des Fluchs, einem Schild, einer Beschwörung, einem Sprung, einem Rundumschlag oder einem Fluch.")}</p>')


def climbers_intro(ctx):
    t = ctx.t
    return (f'<p class="big">{t("One likeness for every climber K'in has lost, carved into the Spirit Mural so that no one goes unrecorded.", "Ein Abbild für jeden Kletterer, den K'in verloren hat, ins Geisterwandbild gemeißelt, damit niemand unaufgezeichnet bleibt.")}</p>'
            f'<p>{t("They exist only as reliefs, each about the length of a forearm, with dust settled into the grooves. Each sheet shows the carving twice: under flat front light, the way K'in lights it, and under low raking light, the way Kaya learns to read it. The newest figure on the strip is Kaya herself, still pale with fresh dust.", "Es gibt sie nur als Reliefs, jedes etwa so lang wie ein Unterarm, mit Staub in den Rillen. Jedes Blatt zeigt das Relief zweimal: bei flachem Frontlicht, wie K'in es beleuchtet, und bei flachem Streiflicht, wie Kaya es zu lesen lernt. Die neueste Figur im Streifen ist Kaya selbst, noch hell vom frischen Staub.")}</p>'
            f'<p>{t("In the game the wall keeps growing. The first time a player dies in the temple, their Climber is carved here too, with their name in a glyph frame and a sigil of their choice.", "Im Spiel wächst die Wand weiter. Wenn ein Spieler zum ersten Mal im Tempel stirbt, wird auch sein Kletterer hier eingemeißelt, mit seinem Namen in einem Glyphenrahmen und einem Zeichen seiner Wahl.")} '
            f'<a href="{ctx.url("game/climbers-and-co-op.html")}">{t("Climbers &amp; Co-op →", "Kletterer &amp; Koop →")}</a></p>')


GUARDIANS = [("CS-AHKUK", "Ah Kuk", ("Receiver of Offerings", "Empfänger der Opfergaben"), "characters/guardians/ah-kuk.html"),
             ("CS-IXNICTE", "Ix Nicte", ("Keeper of the First Step", "Hüterin der ersten Stufe"), "characters/guardians/ix-nicte.html"),
             ("CS-CHAKTUN", "Chak Tun", ("Warden of the Panels", "Wächter der Tafeln"), "characters/guardians/chak-tun.html"),
             ("CS-AHZAC", "Ah Zac", ("Sweeper of the White Way", "Feger des Weißen Wegs"), "characters/guardians/ah-zac.html"),
             ("CS-KANUK", "Kan Uk", ("The guardian in the niche", "Der Wächter in der Nische"), "characters/guardians/kan-uk.html")]
CLIMBERS = [("CS-MATEO", "Mateo Vance", ("The surveyor", "Der Landvermesser"), "characters/climbers/mateo-vance.html"),
            ("CS-LISBET", "Lisbet", ("Held the line", "Hielt das Seil"), "characters/climbers/lisbet.html"),
            ("CS-JOAQUIN", "Joaquin Reyes", ("Carried his own light", "Trug sein eigenes Licht"), "characters/climbers/joaquin-reyes.html"),
            ("CS-WREN", "Wren", ("Looks like Kaya", "Gleicht Kaya"), "characters/climbers/wren.html"),
            ("CS-ODALYS", "Odalys", ("The unfinished carving", "Das unvollendete Relief"), "characters/climbers/odalys.html")]


# ------------------------------------------------------------------ creatures
ENEMIES = [
    ("E01", ("Risen Guardian", "Erweckter Wächter"), ("Base enemy · from the Shell", "Grundgegner · ab The Shell"),
     ("A cursed priest in paper-brown wrappings with a cracked stone club. Shambles, relentless and without reason.",
      "Ein verfluchter Priester in papierbraunen Bandagen mit einer rissigen Steinkeule. Schlurft heran, unerbittlich und grundlos.")),
    ("E02", ("Elite Guardians", "Elite-Wächter"), ("Temple's Wrath variants · Tier VI", "Varianten des Tempelzorns · Stufe VI"),
     ("Armoured, ember-cursed, drowned and root-bound versions of the same body, each with its own sigil colour.",
      "Gepanzerte, glutverfluchte, ertrunkene und wurzelgebundene Versionen desselben Körpers, jede mit eigener Siegelfarbe.")),
    ("E07", ("Cave Bat", "Höhlenfledermaus"), ("Erratic flyer · Tier I and IV", "Sprunghafter Flieger · Stufe I und IV"),
     ("A crow-sized leaf-nosed bat with glowing amber eyes. A little comical, very annoying.",
      "Eine krähengroße Blattnasenfledermaus mit bernsteinglühenden Augen. Etwas komisch, sehr lästig.")),
    ("E08", ("Temple Leech", "Tempelegel"), ("Water hazard · Tier I", "Wassergefahr · Stufe I"),
     ("Glossy, fat and gross-cute, with teal spots that glow as a warning just under the surface.",
      "Glänzend, dick und eklig-niedlich, mit türkisen Flecken, die knapp unter der Oberfläche warnend leuchten.")),
    ("E09", ("Scarab Swarm", "Skarabäenschwarm"), ("Swarm · Tier II and IV", "Schwarm · Stufe II und IV"),
     ("Jade-and-bronze beetles that flow across the floor like a carpet and rise as a buzzing column.",
      "Käfer aus Jade und Bronze, die wie ein Teppich über den Boden fließen und als summende Säule aufsteigen.")),
    ("E10", ("Husk Archer", "Hülsenschütze"), ("Ranged · from Tier II", "Fernkampf · ab Stufe II"),
     ("A dry skeletal warrior with an obsidian-tipped bow who holds the ledges.",
      "Ein vertrockneter Skelettkrieger mit Obsidianpfeilen, der die Simse besetzt hält.")),
    ("E11", ("Obsidian Panther", "Obsidianpanther"), ("Fast flanker · Tier II and IV", "Schneller Flankenangreifer · Stufe II und IV"),
     ("A black jaguar plated with volcanic glass, rosettes glowing violet-gold from within.",
      "Ein schwarzer Jaguar mit Platten aus vulkanischem Glas, dessen Rosetten von innen violett-golden leuchten.")),
    ("E12", ("Guardian Spirit", "Wächtergeist"), ("Unkillable chaser · Tier II and V", "Unbesiegbarer Verfolger · Stufe II und V"),
     ("A five-metre ghost priest of green spirit light. You cannot fight it. You can only run.",
      "Ein fünf Meter großer Geisterpriester aus grünem Geisterlicht. Man kann ihn nicht bekämpfen, nur vor ihm fliehen.")),
    ("E13", ("Stone Sentry", "Steinwächter"), ("Heavy · from Tier III", "Schwer · ab Stufe III"),
     ("A living statue whose amber eye-slit sweeps the room before it charges.",
      "Eine lebende Statue, deren bernsteinfarbener Augenschlitz den Raum absucht, bevor sie losstürmt.")),
]
BOSSES = [
    ("E14", ("The Gearwarden", "Der Zahnradwächter"), ("Tier III boss", "Boss der Stufe III"),
     ("A nine-metre construct of carved blocks and turning gears around a blazing amber core.",
      "Ein neun Meter hohes Konstrukt aus behauenen Blöcken und drehenden Zahnrädern um einen lodernden Bernsteinkern.")),
    ("E15", ("The Jaguar Priest", "Der Jaguarpriester"), ("Tier V boss", "Boss der Stufe V"),
     ("A shadow-walking priest in a jaguar pelt who phases between carved totems.",
      "Ein schattenwandelnder Priester im Jaguarfell, der zwischen gemeißelten Totems hin und her springt.")),
    ("E16", ("The Priest's Lieutenant", "Der Leutnant des Priesters"), ("Tier VI mini-boss", "Mini-Boss der Stufe VI"),
     ("An armoured warrior-priest with an eagle helmet and an obsidian spear, guarding the Sun Orb vault.",
      "Ein gepanzerter Kriegerpriester mit Adlerhelm und Obsidianspeer, der das Gewölbe der Sonnenkugel bewacht.")),
]
PROPOSED = [
    ("E18", ("Magma Salamander", "Magmasalamander"), ("Proposed · fire floors", "Vorgeschlagen · Feuerebenen"),
     ("Swims through lava, spits molten rock, and hardens when splashed with water.",
      "Schwimmt durch Lava, spuckt geschmolzenes Gestein und erstarrt, wenn man es mit Wasser bespritzt.")),
    ("E19", ("Cenote Serpent", "Cenote-Schlange"), ("Proposed · water floors", "Vorgeschlagen · Wasserebenen"),
     ("A turquoise eel-serpent that strikes from deep water and is stranded when the water parts.",
      "Eine türkise Aalschlange, die aus tiefem Wasser zuschlägt und strandet, wenn sich das Wasser teilt.")),
    ("E20", ("Mirror Shade", "Spiegelschatten"), ("Proposed · illusion floors", "Vorgeschlagen · Täuschungsebenen"),
     ("A faceless obsidian humanoid that splits into copies; only the real one has a gold crack.",
      "Ein gesichtsloser Humanoid aus Obsidian, der sich in Kopien teilt; nur der echte hat einen goldenen Riss.")),
    ("E21", ("Strangler Vine", "Würgeranke"), ("Proposed · root floors", "Vorgeschlagen · Wurzelebenen"),
     ("Looks like ordinary roots until the flower-mouth opens. Burns beautifully.",
      "Sieht aus wie gewöhnliche Wurzeln, bis sich das Blütenmaul öffnet. Brennt wunderbar.")),
]


def creatures(ctx):
    t = ctx.t

    def grid(items):
        return '<div class="items">' + "".join(
            f'<article class="item">{ctx.figure(i, T(ctx, n), show_caption=False)}<div><p class="kicker">{T(ctx, s)}</p>'
            f'<h3>{T(ctx, n)}</h3><p>{T(ctx, d)}</p></div></article>' for i, n, s, d in items) + "</div>"

    named = "".join(card(ctx, img, n, T(ctx, r), p) for img, n, r, p in GUARDIANS[:2] + GUARDIANS[3:])
    return f"""
<section class="wrap section narrow-top">
  <p class="kicker">{t("Enemies", "Gegner")}</p><h2>{t("What waits on the floors", "Was auf den Ebenen wartet")}</h2>
  <p class="lede-sm">{t("Eerie and characterful rather than gory. Every enemy is built to read clearly at third-person range, and their numbers grow with the size of the party.",
                        "Eher unheimlich und charaktervoll als blutig. Jeder Gegner ist so gestaltet, dass er aus der Third-Person-Distanz klar lesbar ist, und ihre Zahl wächst mit der Größe der Gruppe.")}</p>
  {grid(ENEMIES)}
</section>
<section class="band"><div class="wrap section">
  <p class="kicker">{t("Bosses", "Bosse")}</p><h2>{t("Guardians of the tiers", "Hüter der Stufen")}</h2>
  {grid(BOSSES)}
  <p class="lede-sm" style="margin-top:28px">{t("The final boss waits on the summit:", "Der letzte Boss wartet auf dem Gipfel:")}
  <a href="{ctx.url('characters/hollow-high-priest.html')}">{t("The Hollow High Priest →", "Der Hohle Hohepriester →")}</a></p>
</div></section>
<section class="wrap section">
  <p class="kicker">{t("Named guardians", "Benannte Wächter")}</p><h2>{t("The ones with a story", "Die mit einer Geschichte")}</h2>
  <p class="lede-sm">{t("In the game they return as elite enemies, once per tier, each with its own sigil and one gift of the curse.",
                        "Im Spiel kehren sie als Elitegegner zurück, einmal pro Stufe, jeder mit eigenem Siegel und einer Gabe des Fluchs.")}</p>
  <div class="cards cards-4">{named}</div>
</section>
<section class="band"><div class="wrap section">
  <p class="kicker">{t("Ideas for later", "Ideen für später")}</p><h2>{t("Proposed creatures", "Vorgeschlagene Kreaturen")}</h2>
  {grid(PROPOSED)}
</div></section>
"""


def lineup(ctx):
    t = ctx.t
    rows = [
        ("Kaya", t("Tall and slender, about seven heads; K'in hovers at her right shoulder", "Groß und schlank, etwa sieben Kopflängen; K'in schwebt an ihrer rechten Schulter")),
        ("Dr. Isabel Kaan", t("Small and wiry, a little shorter than her daughter", "Klein und drahtig, etwas kleiner als ihre Tochter")),
        ("Oxlahun", t("Medium height, broad and solid", "Mittelgroß, breit und kräftig")),
        ("Ix Nicte", t("About Kaya's height, head bowed", "Etwa so groß wie Kaya, den Kopf geneigt")),
        ("Ah Zac", t("Kaya's height upright; stooped, below her shoulder", "Aufgerichtet so groß wie Kaya; gebückt reicht er ihr nicht bis zur Schulter")),
        ("Kan Uk", t("Lean, slightly stooped, a little shorter than Ah Kuk", "Hager, leicht gebückt, etwas kleiner als Ah Kuk")),
        ("Ah Kuk", t("Very thin, a head taller than Oxlahun", "Sehr hager, einen Kopf größer als Oxlahun")),
        (t("The Hollow High Priest", "Der Hohle Hohepriester"), t("Half again as tall as a tall man, taller still with his headdress", "Anderthalbmal so groß wie ein großer Mann, mit Kopfschmuck noch größer")),
    ]
    row_html = "".join(f"<tr><th scope='row'>{n}</th><td>{d}</td></tr>" for n, d in rows)
    return f"""
<section class="wrap section narrow-top">
  {ctx.figure("CS-LINEUP", t("The cast together in the Threshold", "Alle Figuren gemeinsam in der Schwelle") if ctx.has("ACT-CS-LINEUP")
               else t("The cast at true relative scale", "Die Figuren im echten Größenverhältnis"), cls="sheet")}
</section>
<section class="band"><div class="wrap section">
  <p class="kicker">{t("Left to right", "Von links nach rechts")}</p><h2>{t("Who stands how tall", "Wer wie groß ist")}</h2>
  <div class="table-wrap"><table class="orb-table">
    <thead><tr><th>{t("Character", "Figur")}</th><th>{t("Scale", "Maßstab")}</th></tr></thead><tbody>{row_html}</tbody>
  </table></div>
</div></section>
"""


PAGES = {path: character_page(c) for path, c in C.items()}
PAGES.update({
    "characters/index.html": dict(
        title=("Characters", "Figuren"), kicker=("Characters", "Figuren"), banner="CS-LINEUP",
        lede=("The explorer, her guide, a trader with a smile, a missing mother, the cursed order and the climbers who came before.",
              "Die Entdeckerin, ihre Führerin, ein Händler mit Lächeln, eine verschwundene Mutter, der verfluchte Orden und die Kletterer, die vorher kamen."),
        description=("The cast of Ascent of the Sun Temple.", "Die Figuren von Ascent of the Sun Temple."),
        body=overview, og="CS-LINEUP"),
    "characters/guardians/index.html": dict(
        title=("The Risen Guardians", "Die Erweckten Wächter"), kicker=("Characters", "Figuren"), banner="A-03",
        lede=("The cursed priests of the order: one base enemy, and five guardians with names, posts and stories.",
              "Die verfluchten Priester des Ordens: ein Grundgegner und fünf Wächter mit Namen, Posten und Geschichten."),
        description=("The Risen Guardians of the Sun Temple.", "Die Erweckten Wächter des Sonnentempels."),
        body=group_page(guardians_intro, "CS-GUARDIAN", GUARDIANS, [("E01", ("Enemy sheet", "Gegner-Blatt")),
                                                                    ("TA-GUARDIAN", ("Turnaround", "Turnaround"))]),
        og="CS-GUARDIAN"),
    "characters/climbers/index.html": dict(
        title=("The Carved Climbers", "Die gemeißelten Kletterer"), kicker=("Characters", "Figuren"), banner="HOME-KIN",
        lede=("The faces on the Spirit Mural: climbers who came before Kaya and never left. In the game, every player joins them.",
              "Die Gesichter auf dem Geisterwandbild: Kletterer, die vor Kaya kamen und nie gingen. Im Spiel reiht sich jeder Spieler bei ihnen ein."),
        description=("The Carved Climbers on the Spirit Mural.", "Die gemeißelten Kletterer auf dem Geisterwandbild."),
        body=group_page(climbers_intro, "CS-CLIMBERS", CLIMBERS, [("HUB09", ("The relief panels", "Die Relieftafeln"))]),
        og="CS-CLIMBERS"),
    "characters/creatures.html": dict(
        title=("Creatures & Bosses", "Kreaturen & Bosse"), kicker=("Characters", "Figuren"), banner="B-10",
        lede=("Bats, leeches, scarabs, archers, panthers, sentries, a ghost you can only outrun, and the bosses of the tiers.",
              "Fledermäuse, Egel, Skarabäen, Bogenschützen, Panther, Steinwächter, ein Geist, vor dem man nur fliehen kann, und die Bosse der Stufen."),
        description=("Enemies, creatures and bosses.", "Gegner, Kreaturen und Bosse."),
        body=creatures, og="B-10"),
    "characters/lineup.html": dict(
        title=("Cast Lineup", "Größenvergleich"), kicker=("Characters", "Figuren"),
        lede=("The whole cast side by side on one baseline, at true relative scale.",
              "Alle Figuren nebeneinander auf einer Grundlinie, im echten Größenverhältnis."),
        description=("The cast at true relative scale.", "Die Figuren im echten Größenverhältnis."),
        body=lineup, og="CS-LINEUP"),
})
