"""The game's title lockup: the main logo with the "Ascent of the Sun Temple" plate tucked under it.

Usage (from the repo root):  python _builder/compose_logo.py [plate_width] [overlap]
Reads   _builder/images/originals/TITLE-LOGO.*  (main logo, transparent)
        _builder/images/originals/SUB-ASCENT.*  (subtitle plate, transparent)
Writes  _builder/images/originals/TITLE-LOCKUP.webp  (transparent; the home page hero shows it)

plate_width is a share of the logo's width (default 0.94), overlap a share of the logo's height (default 0.05).
"""
import sys
from pathlib import Path

from PIL import Image

ORIGINALS = Path(__file__).resolve().parent / "images" / "originals"


def trimmed(stem):
    path = next(p for p in ORIGINALS.glob(f"{stem}.*") if p.suffix.lower() in (".png", ".webp"))
    im = Image.open(path).convert("RGBA")
    return im.crop(im.split()[3].point(lambda v: 255 if v > 10 else 0).getbbox())


def main():
    plate_share = float(sys.argv[1]) if len(sys.argv) > 1 else 0.94
    overlap = float(sys.argv[2]) if len(sys.argv) > 2 else 0.05
    logo, plate = trimmed("TITLE-LOGO"), trimmed("SUB-ASCENT")
    pw = round(logo.width * plate_share)
    plate = plate.resize((pw, round(plate.height * pw / plate.width)), Image.LANCZOS)
    py = logo.height - round(logo.height * overlap)
    out = Image.new("RGBA", (logo.width, py + plate.height))
    out.alpha_composite(logo, (0, 0))
    out.alpha_composite(plate, ((logo.width - pw) // 2, py))
    path = ORIGINALS / "TITLE-LOCKUP.webp"
    out.save(path, "WEBP", lossless=True)
    print(f"{path}  {out.size}")


if __name__ == "__main__":
    main()
