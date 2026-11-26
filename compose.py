#!/usr/bin/env python3
"""Compose the round-2 front page for news-image-20261125 (1024x1024 PNG).

A fresh take on Wednesday 25 November 2026: all-new stories, all-new
drawn panels, same newspaper front-page form as round 1. Lead: the
Houthi strike on Saudi Arabia's Ras Tanura refinery. The hero is drawn
with Pillow (no generated photo), so the whole image is produced by
this one deterministic script.

Deterministic: fixed layout, fixed fonts, fixed seeded decoration, no
randomness in the output, no network, no timestamps in the image.
Run: python3 compose-r2.py
Writes entry.png next to this file.
"""
import math
import os
import random
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024
PAPER = (247, 243, 233)
INK = (18, 24, 38)
RED = (178, 34, 34)
NAVY = (28, 52, 92)
GREY = (90, 92, 96)
RULE = (18, 24, 38)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, x, y, text, fnt, color, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x0, y, x1, width=2):
    draw.line([(x0, y), (x1, y)], fill=RULE, width=width)


def flame(d, cx, base_y, w, h):
    """A stylised flame: orange outer, yellow inner."""
    d.polygon([(cx - w, base_y), (cx - w // 2, base_y - h),
               (cx, base_y - h - 10), (cx + w // 2, base_y - h),
               (cx + w, base_y)], fill=(255, 140, 40))
    d.polygon([(cx - w // 2, base_y), (cx - w // 4, base_y - h // 2),
               (cx, base_y - h // 2 - 6), (cx + w // 4, base_y - h // 2),
               (cx + w // 2, base_y)], fill=(255, 196, 60))


def smoke(d, cx, cy, r, color=(150, 150, 150)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def hero_refinery(d, x, y, w, h):
    """Ras Tanura refinery at dusk: columns, flare stacks, fire, smoke."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 178, 120))
    d.ellipse([x + w - 90, y + 8, x + w - 30, y + 68], fill=(250, 220, 150))
    d.rectangle([x, y + h - 34, x + w, y + h], fill=(70, 60, 54))
    # distillation columns
    for cx, cw, ch in ((x + 90, 46, 96), (x + 170, 38, 78), (x + 250, 52, 108)):
        d.rectangle([cx, y + h - 34 - ch, cx + cw, y + h - 34],
                    fill=(96, 104, 118))
        d.rectangle([cx - 6, y + h - 34 - ch, cx + cw + 6,
                     y + h - 34 - ch + 8], fill=(70, 78, 92))
        d.rectangle([cx + cw // 2 - 3, y + h - 34 - ch - 16,
                     cx + cw // 2 + 3, y + h - 34 - ch], fill=(70, 78, 92))
    # flare stacks with flames
    for fx in (x + 380, x + 450):
        d.rectangle([fx - 5, y + 44, fx + 5, y + h - 34], fill=(52, 58, 66))
        flame(d, fx, y + 46, 16, 30)
    # storage tanks
    for tx in (x + 330, x + 500):
        d.ellipse([tx, y + h - 84, tx + 64, y + h - 34], fill=(214, 222, 235))
        d.rectangle([tx, y + h - 68, tx + 64, y + h - 34],
                    fill=(214, 222, 235))
    # fire at the base of the first column + smoke rising
    flame(d, x + 113, y + h - 30, 26, 44)
    flame(d, x + 200, y + h - 30, 18, 30)
    for cx, cy, r in ((x + 113, y + 34, 14), (x + 126, y + 20, 10),
                      (x + 100, y + 18, 8), (x + 200, y + 44, 11)):
        smoke(d, cx, cy, r)


def drone_panel(d, x, y, w, h):
    """A drone over a city skyline at dusk, smoke rising."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 150, 110))
    d.rectangle([x, y + h - 30, x + w, y + h], fill=(60, 52, 48))
    for bx, bw, bh in ((x + 14, 52, 46), (x + 78, 40, 66), (x + 130, 58, 38),
                       (x + 200, 44, 58), (x + 256, 50, 44)):
        d.rectangle([bx, y + h - 30 - bh, bx + bw, y + h - 30],
                    fill=(90, 78, 72))
        for wy in range(y + h - 30 - bh + 8, y + h - 36, 12):
            d.rectangle([bx + 8, wy, bx + 16, wy + 6], fill=(250, 196, 90))
    # quadcopter drone
    cx, cy = x + w // 2, y + 34
    d.rectangle([cx - 26, cy - 3, cx + 26, cy + 3], fill=(30, 34, 40))
    d.rectangle([cx - 6, cy + 3, cx + 6, cy + 12], fill=(30, 34, 40))
    for px in (cx - 30, cx + 30):
        d.ellipse([px - 12, cy - 8, px + 12, cy + 2], outline=(30, 34, 40),
                  width=2)
    for sx, sy, r in ((x + 240, y + 26, 12), (x + 252, y + 14, 8),
                      (x + 228, y + 12, 7)):
        smoke(d, sx, sy, r)


def treaty_panel(d, x, y, w, h):
    """A Pacific island with two flagpoles: Australia and Solomon Islands."""
    d.rectangle([x, y, x + w, y + h], fill=(178, 205, 228))
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(44, 92, 128))
    for wx in range(x, x + w, 24):
        d.arc([wx, y + h - 36, wx + 24, y + h - 20], 180, 360,
              fill=(44, 92, 128), width=2)
    # island
    d.polygon([(x + 60, y + h - 26), (x + 120, y + h - 66),
               (x + 200, y + h - 66), (x + 260, y + h - 26)],
              fill=(96, 122, 90))
    d.polygon([(x + 150, y + h - 66), (x + 160, y + h - 96),
               (x + 170, y + h - 66)], fill=(70, 96, 66))
    # flagpoles: blue ensign left, blue field with stars right
    for fx, col in ((x + 96, (36, 68, 140)), (x + 216, (36, 68, 140))):
        d.line([(fx, y + 22), (fx, y + h - 66)], fill=(52, 58, 66), width=3)
        d.polygon([(fx, y + 22), (fx + 44, y + 32), (fx, y + 42)],
                  fill=col)
    d.polygon([(x + 216, y + 22), (x + 260, y + 32), (x + 216, y + 42)],
              fill=(36, 120, 70))
    for sx, sy in ((x + 236, y + 30), (x + 246, y + 26), (x + 246, y + 36)):
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 240, 180))


def space_panel(d, x, y, w, h):
    """A space station over Earth's curve, capsule docking."""
    d.rectangle([x, y, x + w, y + h], fill=(16, 22, 40))
    rng = random.Random(11)
    for _ in range(26):
        sx = x + rng.randint(6, w - 6)
        sy = y + rng.randint(6, h - 40)
        d.ellipse([sx, sy, sx + 2, sy + 2], fill=(235, 240, 250))
    # Earth curve
    d.ellipse([x - 60, y + h - 26, x + w + 60, y + h + 60],
              fill=(44, 92, 160))
    d.ellipse([x - 60, y + h - 26, x + w + 60, y + h + 60],
              outline=(120, 170, 220), width=2)
    # station: core module + solar wings
    cx, cy = x + w // 2, y + h // 2 - 6
    d.rectangle([cx - 70, cy - 12, cx + 70, cy + 12], fill=(200, 208, 220))
    d.rectangle([cx - 70, cy - 12, cx - 46, cy + 12], fill=(150, 158, 172))
    d.rectangle([cx - 118, cy - 20, cx - 72, cy + 20], fill=(36, 68, 140))
    d.rectangle([cx + 72, cy - 20, cx + 118, cy + 20], fill=(36, 68, 140))
    for gx in range(cx - 116, cx - 74, 10):
        d.line([(gx, cy - 20), (gx, cy + 20)], fill=(90, 120, 180), width=1)
    for gx in range(cx + 74, cx + 118, 10):
        d.line([(gx, cy - 20), (gx, cy + 20)], fill=(90, 120, 180), width=1)
    # docking capsule
    d.ellipse([cx + 78, cy - 8, cx + 98, cy + 8], fill=(232, 182, 60))


def court_panel(d, x, y, w, h):
    """A courthouse front with columns and a gavel."""
    d.rectangle([x, y, x + w, y + h], fill=(58, 74, 102))
    d.polygon([(x + 40, y + 18), (x + w - 40, y + 18), (x + w // 2, y + 44)],
              fill=(214, 222, 235))
    for cx in (x + 70, x + 140, x + 210, x + 280):
        d.rectangle([cx - 12, y + 46, cx + 12, y + h - 18],
                    fill=(214, 222, 235))
    d.rectangle([x + 40, y + h - 18, x + w - 40, y + h - 8],
                fill=(214, 222, 235))
    # gavel, head horizontal, handle diagonal down to the right
    gx, gy = x + w - 78, y + h - 52
    d.rectangle([gx - 22, gy - 8, gx + 22, gy + 8], fill=(120, 82, 40))
    d.ellipse([gx - 22, gy - 8, gx - 12, gy + 8], fill=(90, 60, 28))
    d.ellipse([gx + 12, gy - 8, gx + 22, gy + 8], fill=(90, 60, 28))
    d.line([(gx + 8, gy + 6), (gx + 30, gy + 30)], fill=(120, 82, 40),
           width=6)
    d.rectangle([x + 40, y + h - 18, x + w - 40, y + h - 8],
                fill=(214, 222, 235))


def tariff_panel(d, x, y, w, h):
    """Stacked shipping containers under a big percent sign."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 214, 170))
    cols = ((178, 60, 50), (60, 96, 140), (196, 160, 60), (70, 120, 80))
    for row in range(2):
        for col in range(4):
            bx = x + 12 + col * 76
            by = y + h - 34 - (row + 1) * 30
            d.rectangle([bx, by, bx + 70, by + 28], fill=cols[col])
            for vx in range(bx + 8, bx + 66, 10):
                d.line([(vx, by + 3), (vx, by + 25)], fill=(0, 0, 0), width=1)
    d.text((x + w - 66, y + 6), "%", font=font(SANS_B, 44), fill=RED)


def climate_panel(d, x, y, w, h):
    """A warming globe under a pale sun: the climate talks."""
    d.rectangle([x, y, x + w, y + h], fill=(196, 214, 226))
    d.ellipse([x + w - 66, y + 8, x + w - 26, y + 48], fill=(250, 196, 90))
    cx, cy = x + w // 2, y + h // 2 + 8
    d.ellipse([cx - 46, cy - 46, cx + 46, cy + 46], fill=(44, 92, 160))
    d.ellipse([cx - 30, cy - 30, cx + 6, cy - 6], fill=(70, 120, 80))
    d.ellipse([cx + 2, cy + 10, cx + 34, cy + 38], fill=(70, 120, 80))
    d.arc([cx - 46, cy - 46, cx + 46, cy + 46], 200, 340,
          fill=(120, 170, 220), width=3)
    d.line([(cx + 52, cy - 52), (cx + 62, cy - 62)], fill=(178, 34, 34),
           width=4)
    d.polygon([(cx + 62, cy - 62), (cx + 62, cy - 48), (cx + 48, cy - 62)],
              fill=(178, 34, 34))


PANELS = [
    ("SUDAN", "RSF drone strikes kill 19 civilians in two cities",
     "Rights group says 20 more wounded in the attacks.", drone_panel),
    ("PACIFIC", "Australia signs treaty barring foreign bases",
     "Solomon Islands pact shuts out any foreign military base.",
     treaty_panel),
    ("SPACE", "Pakistani astronaut boards China's space station",
     "First foreigner aboard Tiangong as Shenzhou-24 docks.",
     space_panel),
    ("WASHINGTON", "Huawei guilty of stealing trade secrets",
     "US jury convicts on trade secrets and bank fraud.", court_panel),
    ("WASHINGTON", "Trump proposes new tariffs on 14 partners",
     "Duties target excess factory capacity, China hardest hit.",
     tariff_panel),
    ("VATICAN", "Pope warns as COP31 climate talks fail",
     "No deal reached; extreme weather grows more frequent.",
     climate_panel),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.text((W // 2, 12), "THE WORLD IN ONE DAY", font=font(SERIF_B, 58),
           fill=INK, anchor="ma")
    d.text((W // 2, 76), "WEDNESDAY, 25 NOVEMBER 2026",
           font=font(SANS_B, 26), fill=RED, anchor="ma")
    rule(d, 20, 108, W - 20, 3)

    # Lead
    y = 122
    d.text((20, y), "RAS TANURA HIT", font=font(SANS_B, 20), fill=RED)
    y += 30
    y = text_block(d, 20, y,
                   "Houthis strike Saudi Arabia's biggest oil refinery "
                   "\u2014 fires at Ras Tanura",
                   font(SANS_B, 32), INK, W - 40, 40)
    y += 8
    hero_panel = Image.new("RGB", (560, 170), PAPER)
    hd = ImageDraw.Draw(hero_panel)
    hero_refinery(hd, 0, 0, 560, 170)
    img.paste(hero_panel, (20, y))
    d.rectangle([20, y, 20 + 560, y + 170], outline=INK, width=2)
    yy = text_block(d, 596, y,
                    "Yemen's Houthis say they attacked the Ras Tanura "
                    "refinery, Saudi Arabia's largest, and caused fires.",
                    font(SANS, 20), INK, 408, 26)
    text_block(d, 596, yy + 10,
               "Oil prices climb; Brent nears $95 a barrel.",
               font(SANS_B, 20), INK, 408, 26)
    y = y + 170 + 12
    rule(d, 20, y, W - 20, 2)
    y += 10

    # Two rows of three story panels. Each panel is drawn on its own
    # temporary image so no drawing can spill past the panel border
    # (e.g. the Earth curve in the space panel) into the captions below.
    col_w, gap = 320, 12
    x0 = 20
    panel_h = 96
    for row in range(2):
        row_y = y
        row_bottom = row_y
        for col in range(3):
            p = PANELS[row * 3 + col]
            px = x0 + col * (col_w + gap)
            panel_img = Image.new("RGB", (col_w, panel_h), PAPER)
            pd = ImageDraw.Draw(panel_img)
            p[3](pd, 0, 0, col_w, panel_h)
            img.paste(panel_img, (px, row_y))
            d.rectangle([px, row_y, px + col_w, row_y + panel_h],
                        outline=INK, width=2)
            ty = row_y + panel_h + 8
            d.text((px, ty), p[0], font=font(SANS_B, 16), fill=RED)
            ty += 21
            ty = text_block(d, px, ty, p[1], font(SANS_B, 21), INK,
                            col_w, 25)
            ty = text_block(d, px, ty + 3, p[2], font(SANS, 17), GREY,
                            col_w, 21)
            row_bottom = max(row_bottom, ty)
        y = row_bottom + 10
        if row == 0:
            rule(d, 20, y, W - 20, 1)
            y += 10

    # Ticker footer
    rule(d, 20, y, W - 20, 2)
    y += 10
    d.text((20, y), "ALSO TODAY", font=font(SANS_B, 17), fill=RED)
    text_block(d, 20, y + 24,
               "Bangladesh raises garment wage 36% to $139 \u00b7 Cairo "
               "tanker fire kills 31 \u00b7 Nasdaq down 2%, near bear "
               "market \u00b7 Macy's parade postponed by storm",
               font(SANS, 17), INK, W - 40, 22)
    print("layout ends near y =", y + 24 + 44, "of", H)

    out = os.path.join(HERE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
