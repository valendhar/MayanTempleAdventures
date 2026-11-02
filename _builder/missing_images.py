#!/usr/bin/env python3
"""Write _builder/MISSING_IMAGES.md: every image ID the built site still shows as a placeholder, grouped by page.
Codex pages (CX-…) are listed last, in one group, so they can be made after everything else.

Usage:  python _builder/missing_images.py      (run after build.py, or while dev.py is running)
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
from site_map import all_paths  # noqa: E402

OPTIONAL = ("Optional extras such as the turnarounds (`TA-KAYA`, `TA-OXLAHUN`, …), the named guardian sheets (`E03`–`E06`) "
            "and the boss sheets (`E15`–`E17`) are not listed: they stay hidden until uploaded, then appear on their pages.")


def main():
    seen, sections, codex = set(), [], []
    for path, trail in all_paths():
        page = ROOT / path
        if not page.exists():
            continue
        ids = list(dict.fromkeys(re.findall(r'class="ph-id">([^<]+)<', page.read_text(encoding="utf-8"))))
        new = [i for i in ids if i not in seen]
        seen.update(new)
        codex += [i for i in new if i.startswith("CX-")]
        new = [i for i in new if not i.startswith("CX-")]
        if new:
            label = trail[-1][0] if isinstance(trail[-1], (tuple, list)) else trail[-1]
            sections.append(f"### {label} (`{path}`)\n\n" + " ".join(f"`{i}`" for i in new) + "\n")
    rest = len(seen) - len(codex)
    out = ["# Missing images", "",
           f"**{len(seen)} images still show as placeholders:** {rest} scenes, maps and sheets, then {len(codex)} codex pages.", "",
           "Save an image as `_builder/images/originals/<ID>.png` (or `.jpg` / `.webp`), using the ID exactly as shown. "
           "The next build (or the running dev server) turns the placeholder into the picture everywhere that ID is used.", "",
           OPTIONAL, "", "Regenerate this list with `python _builder/missing_images.py`.", "",
           f"## Scenes, maps and sheets ({rest})", "", *sections,
           f"## Codex pages ({len(codex)}), last", "", " ".join(f"`{i}`" for i in codex) + "\n"]
    (HERE / "MISSING_IMAGES.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(seen)} missing ({rest} + {len(codex)} codex) -> {HERE / 'MISSING_IMAGES.md'}")


if __name__ == "__main__":
    main()
