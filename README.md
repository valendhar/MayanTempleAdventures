# Mayan Temple Adventures — design site

A visual design document for *Mayan Temple Adventures*: five Fortnite islands set in and around one living Mayan pyramid, planned in Unreal Editor for Fortnite (UEFN). The flagship, *Ascent of the Sun Temple: Climbers*, is a co-op climb for up to four players.

The site is plain HTML, CSS and JavaScript. It needs no build step on GitHub and works by opening `index.html` in a browser.

## Languages

The site is in English and German. English pages live at the top level, the German copies of every page live in `de/` with the same file names. The flags in the top-right corner of the menu bar switch to the same page in the other language. Images are shared by both languages.

Live addresses: `https://valendhar.github.io/MayanTempleAdventures/` (English) and `https://valendhar.github.io/MayanTempleAdventures/de/` (German).

## Putting it online with GitHub Pages

### First time

1. Sign in at github.com (or create a free account).
2. Install **GitHub Desktop** from desktop.github.com and sign in with the same account.
3. In GitHub Desktop choose **File → New repository**. Name it `sun-temple`, pick a folder on your computer, and click **Create repository**.
4. Unzip the site zip and copy **everything inside it** (the `index.html`, the `assets` folder, `_builder` and the rest) into that new repository folder.
5. Back in GitHub Desktop, type a summary such as `First version of the site`, click **Commit to main**, then **Publish repository**. Untick **Keep this code private** (free GitHub Pages needs a public repository) and confirm.
6. On github.com, open the repository, go to **Settings → Pages**. Under **Build and deployment**, set **Source** to **Deploy from a branch**, choose **main** and **/ (root)**, and click **Save**.
7. After a minute or two the page shows your address: `https://<your-username>.github.io/sun-temple/`.

### Every update after that

1. Unzip the new version and copy everything into the same repository folder, replacing the old files.
2. In GitHub Desktop: write a short summary, **Commit to main**, then **Push origin**.
3. The live site updates within a minute or two.

## Working on the site locally

Edit the page sources in `_builder/` (never the generated `.html` files or `assets/css`, `assets/js`: the builder overwrites them). To see changes as you work:

1. Once: `pip install -r _builder/requirements.txt`
2. Run `python _builder/dev.py` and open http://127.0.0.1:8765/

Every time you save a file in `_builder/`, the site rebuilds in under a second and open pages reload themselves. If a change breaks the build, the error shows in the terminal and in a red banner on the page until you fix it. Commit the rebuilt files together with your source changes.

## Folder guide

| Folder | What is in it |
|---|---|
| `index.html`, `game/`, `world/`, `characters/`, `climb/`, `art/` | The English pages |
| `de/` | The German pages |
| `assets/css`, `assets/js` | Styles, menus and the image viewer |
| `assets/img/full`, `assets/img/thumb` | Web-sized images, made automatically |
| `_builder/` | The page source and the builder script used to regenerate the site |
| `_builder/IMAGE_LIST.md` | Which image goes where, by file name |

## License

Copyright © 2026 Mike Stevanovic. All rights reserved.

This project is proprietary and is not open source. Its art, characters, story, world, designs, text and code may not be copied, adapted, redistributed, used commercially or used to train AI without written permission. See [LICENSE](LICENSE) for the full terms.
