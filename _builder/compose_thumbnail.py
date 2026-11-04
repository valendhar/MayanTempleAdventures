"""Island thumbnail: the island's painting + the main title logo + the island's subtitle plate, at 1920x1080.

Usage (from the repo root):  python _builder/compose_thumbnail.py TRAPS [logo_width] [top] [plate_scale]
Reads   _builder/images/originals/ISL-<KEY>.*  (painting without any logo)
        _builder/images/originals/SUB-<KEY>.*  (subtitle plate, transparent)
        _builder/images/originals/TITLE-LOGO.* (main logo, transparent)
Writes  _builder/images/originals/THUMB-<KEY>.png  (the Fortnite island thumbnail; the site shows it as the page header)

logo_width is a share of the image width (default 0.38), top a share of its height (default 0.02).
plate_scale enlarges a short plate (default 1; it never grows wider than the logo allows).
"""
import sys
from pathlib import Path

from PIL import Image, ImageFilter

ORIGINALS = Path(__file__).resolve().parent / "images" / "originals"
W, H = 1920, 1080
PLATE_ASPECT = 4.68  # width/height of a full-length plate (SUB-TRAPS); sets the shared plate height


def find(stem):
    hits = [p for p in ORIGINALS.glob(f"{stem}.*") if p.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")]
    if not hits:
        sys.exit(f"missing: {ORIGINALS / stem}.*")
    return hits[0]


def trimmed(path):
    im = Image.open(path).convert("RGBA")
    return im.crop(im.split()[3].point(lambda v: 255 if v > 10 else 0).getbbox())


def main():
    key = sys.argv[1].upper()
    logo_w = float(sys.argv[2]) if len(sys.argv) > 2 else 0.38
    top = float(sys.argv[3]) if len(sys.argv) > 3 else 0.02
    plate_scale = float(sys.argv[4]) if len(sys.argv) > 4 else 1.0

    bg = Image.open(find(f"ISL-{key}")).convert("RGBA").resize((W, H), Image.LANCZOS)
    logo, plate = trimmed(find("TITLE-LOGO")), trimmed(find(f"SUB-{key}"))

    lw = int(W * logo_w)
    logo = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
    # the plate tucks under the logo, a little narrower than it. Every plate gets the same height, so a short title
    # (a shorter plate) keeps the same letter size instead of being stretched to the full width.
    ph = round(lw * 0.86 / PLATE_ASPECT * plate_scale)
    pw = min(int(lw * 0.86), round(plate.width * ph / plate.height))
    plate = plate.resize((pw, round(plate.height * pw / plate.width)), Image.LANCZOS)

    lx, ly = (W - lw) // 2, int(H * top)
    px, py = (W - pw) // 2, ly + logo.height - int(logo.height * 0.10)
    group = Image.new("RGBA", (W, H))
    group.alpha_composite(logo, (lx, ly))
    group.alpha_composite(plate, (px, py))

    # a soft dark shadow lifts the lockup off a busy painting
    shadow = Image.new("RGBA", (W, H), (7, 22, 18, 0))
    shadow.putalpha(group.split()[3].point(lambda v: int(v * .55)))
    bg.alpha_composite(shadow.filter(ImageFilter.GaussianBlur(14)), (0, 10))
    bg.alpha_composite(group)

    out = ORIGINALS / f"THUMB-{key}.png"
    bg.convert("RGB").save(out)
    print(f"{out}  (logo {lw}px wide, plate ends at y={py + plate.height})")


if __name__ == "__main__":
    main()
