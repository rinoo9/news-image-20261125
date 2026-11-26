#!/usr/bin/env python3
"""Draw the round-3 front image for news-image-20261125 (1024x1024 PNG).

Form: an atlas spread, not a newspaper grid. A dark masthead, a world
map band with numbered pins for the six stories, one wide lead picture
(the Kerch Bridge road span, destroyed), then five story rows, each with
its own small drawn picture, and a ticker strip at the foot.

Stories: Wednesday 25 November 2026, none of them used in round 1 or
round 2 (round 1: Gulf of Finland warship, Riyadh tower, CIA breach,
NATO jets, Hormuz tankers, Gaza toll, Giuliani medal; round 2: Ras
Tanura, Sudan RSF, Australia treaty, Pakistani astronaut, Huawei,
Trump tariffs, Pope/COP31).

  1. UKRAINE (lead) — Ukraine says it destroyed the road span of the
     Kerch Bridge; Russia says it will rebuild.
  2. TECHNOLOGY — Nvidia reinstates Jensen Huang as chief executive,
     twelve days after he resigned; Trump says he may pardon him.
  3. GAZA — Israel kills Hamas security chief Mohammad Abuelouf, his
     wife and two children, Gaza officials say.
  4. UNITED STATES — Kilmar Abrego Garcia leaves the US for Spain,
     ending a twenty-month legal ordeal.
  5. CUBA — The WHO chief urges the US to end a fuel blockade that
     endangers children in Cuba.
  6. IOWA — The Army detonates its old lead-azide stockpile in a
     controlled blast; early air readings show no lead.

Ticker: Sullivan concedes Alaska race to Peltola; DOJ charges 800 in
a global scam crackdown; Hong Kong marks one year since its deadly
fire; Sinner out after knee surgery.

Deterministic: fixed geometry, fixed fonts, no randomness, no network,
no timestamps anywhere in the image.
Run:  python3 compose-r3.py
Writes entry-r3.png next to this file.
"""
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1024, 1024
PAPER = (250, 246, 236)
INK = (16, 22, 34)
NAVY = (24, 44, 78)
RED = (178, 34, 34)
GOLD = (214, 164, 60)
GREY = (96, 98, 104)
SEA = (168, 198, 224)
LAND = (148, 168, 118)
MARGIN = 20

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANSB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def fnt(path, size):
    return ImageFont.truetype(path, size)


def wrap_lines(d, text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(d, x, y, text, font, color, max_w, leading):
    for line in wrap_lines(d, text, font, max_w):
        d.text((x, y), line, font=font, fill=color)
        y += leading
    return y


def hline(d, x0, y, x1, width=2, color=INK):
    d.line([(x0, y), (x1, y)], fill=color, width=width)


def pin(d, x, y, num):
    d.ellipse([x - 13, y - 13, x + 13, y + 13], fill=RED,
              outline=(255, 255, 255), width=2)
    d.text((x, y), str(num), font=fnt(SANSB, 17), fill=(255, 255, 255),
           anchor="mm")


def draw_map(d, x, y, w, h):
    """A simplified world map: sea, rough continents, numbered pins."""
    d.rectangle([x, y, x + w, y + h], fill=SEA)
    # North America
    d.polygon([(x + 30, y + 14), (x + 190, y + 8), (x + 235, y + 26),
               (x + 215, y + 52), (x + 160, y + 66), (x + 120, y + 82),
               (x + 70, y + 68), (x + 38, y + 40)], fill=LAND)
    # Central America narrows toward South America
    d.polygon([(x + 120, y + 82), (x + 165, y + 86), (x + 175, y + 100),
               (x + 140, y + 104), (x + 118, y + 96)], fill=LAND)
    # South America
    d.polygon([(x + 175, y + 104), (x + 250, y + 100), (x + 285, y + 118),
               (x + 262, y + 136), (x + 225, y + 140), (x + 200, y + 124),
               (x + 178, y + 112)], fill=LAND)
    # Europe
    d.polygon([(x + 470, y + 18), (x + 545, y + 12), (x + 565, y + 34),
               (x + 540, y + 52), (x + 495, y + 50), (x + 472, y + 34)],
              fill=LAND)
    # Africa
    d.polygon([(x + 480, y + 56), (x + 560, y + 52), (x + 590, y + 78),
               (x + 575, y + 112), (x + 540, y + 124), (x + 505, y + 100),
               (x + 478, y + 78)], fill=LAND)
    # Asia
    d.polygon([(x + 570, y + 10), (x + 880, y + 6), (x + 940, y + 28),
               (x + 905, y + 58), (x + 830, y + 76), (x + 760, y + 72),
               (x + 700, y + 56), (x + 620, y + 48), (x + 575, y + 32)],
              fill=LAND)
    # Australia
    d.polygon([(x + 810, y + 126), (x + 890, y + 122), (x + 905, y + 136),
               (x + 870, y + 142), (x + 825, y + 138)], fill=LAND)
    # Story pins, numbered in story order:
    # 1 Kerch Bridge (Black Sea), 2 California (Nvidia),
    # 3 Gaza, 4 Madrid (Abrego Garcia to Spain),
    # 5 Havana (Cuba), 6 Iowa.
    pin(d, x + 585, y + 44, 1)
    pin(d, x + 92, y + 56, 2)
    pin(d, x + 556, y + 62, 3)
    pin(d, x + 478, y + 44, 4)
    pin(d, x + 168, y + 78, 5)
    pin(d, x + 168, y + 44, 6)
    d.text((x + 8, y + h - 22), "WHERE THE DAY HAPPENED",
           font=fnt(SANSB, 15), fill=NAVY)


def puff(d, cx, cy, r, color=(140, 140, 140)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def bridge_hero(d, x, y, w, h):
    """The Kerch Bridge over the strait, its road span broken open."""
    d.rectangle([x, y, x + w, y + h], fill=(196, 214, 232))
    d.ellipse([x + w - 110, y + 10, x + w - 40, y + 80],
              fill=(250, 224, 150))
    # sea
    d.rectangle([x, y + h - 46, x + w, y + h], fill=(44, 92, 160))
    for wx in range(x + 10, x + w, 46):
        d.arc([wx, y + h - 34, wx + 34, y + h - 20], 180, 360,
              fill=(120, 170, 220), width=2)
    # two towers
    for tx in (x + 250, x + 660):
        d.rectangle([tx - 8, y + 30, tx + 8, y + h - 46], fill=(96, 104, 118))
        d.line([(tx, y + 30), (tx - 120, y + h - 46)], fill=(70, 78, 92),
               width=2)
        d.line([(tx, y + 30), (tx + 120, y + h - 46)], fill=(70, 78, 92),
               width=2)
    # deck, left half and right half, with the middle span gone
    d.rectangle([x, y + h - 66, x + 430, y + h - 46], fill=(214, 222, 235))
    d.rectangle([x + 560, y + h - 66, x + w, y + h - 46],
                fill=(214, 222, 235))
    # the fallen span, tilted into the water
    d.polygon([(x + 440, y + h - 62), (x + 545, y + h - 58),
               (x + 530, y + h - 30), (x + 455, y + h - 26)],
              fill=(150, 158, 172))
    # fire and smoke where the span broke
    d.polygon([(x + 478, y + h - 58), (x + 488, y + h - 96),
               (x + 498, y + h - 58)], fill=(255, 140, 40))
    d.polygon([(x + 488, y + h - 58), (x + 494, y + h - 84),
               (x + 500, y + h - 58)], fill=(255, 196, 60))
    for cx, cy, r in ((x + 492, y + 34, 15), (x + 508, y + 18, 11),
                      (x + 476, y + 16, 9), (x + 520, y + 36, 8)):
        puff(d, cx, cy, r)


def chip_thumb(d, x, y, w, h):
    """A green circuit board with a chip at its centre."""
    d.rectangle([x, y, x + w, y + h], fill=(24, 96, 60))
    for gx in range(x + 8, x + w - 8, 18):
        d.line([(gx, y + 6), (gx, y + h - 6)], fill=(60, 160, 100), width=1)
    for gy in range(y + 8, y + h - 8, 18):
        d.line([(x + 6, gy), (x + w - 6, gy)], fill=(60, 160, 100), width=1)
    cx, cy = x + w // 2, y + h // 2
    d.rectangle([cx - 26, cy - 18, cx + 26, cy + 18], fill=(30, 34, 40))
    d.rectangle([cx - 16, cy - 10, cx + 16, cy + 10], fill=(214, 164, 60))
    for px in range(cx - 20, cx + 21, 10):
        d.line([(px, cy - 24), (px, cy - 18)], fill=(200, 208, 220), width=2)
        d.line([(px, cy + 18), (px, cy + 24)], fill=(200, 208, 220), width=2)


def skyline_thumb(d, x, y, w, h):
    """A city skyline at dusk, one building damaged, smoke rising."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 150, 110))
    d.rectangle([x, y + h - 12, x + w, y + h], fill=(60, 52, 48))
    for bx, bw, bh in ((x + 6, 26, 34), (x + 36, 22, 48), (x + 62, 26, 30),
                       (x + 92, 22, 42)):
        d.rectangle([bx, y + h - 12 - bh, bx + bw, y + h - 12],
                    fill=(90, 78, 72))
        for wy in range(y + h - 12 - bh + 6, y + h - 16, 10):
            d.rectangle([bx + 5, wy, bx + 11, wy + 5], fill=(250, 196, 90))
    # damaged building: top corner missing, smoke above it
    d.polygon([(x + 62, y + h - 12 - 30), (x + 74, y + h - 12 - 30),
               (x + 88, y + h - 12 - 18), (x + 88, y + h - 12),
               (x + 62, y + h - 12)], fill=(70, 60, 54))
    for cx, cy, r in ((x + 76, y + 12, 8), (x + 84, y + 6, 6)):
        puff(d, cx, cy, r)


def plane_thumb(d, x, y, w, h):
    """An airliner crossing a sunset sky over the sea."""
    d.rectangle([x, y, x + w, y + h], fill=(250, 196, 120))
    d.ellipse([x + w - 34, y + 6, x + w - 10, y + 30], fill=(250, 240, 200))
    d.rectangle([x, y + h - 16, x + w, y + h], fill=(44, 92, 160))
    cx, cy = x + w // 2, y + h // 2
    d.ellipse([cx - 34, cy - 7, cx + 34, cy + 7], fill=(240, 244, 250))
    d.polygon([(cx + 26, cy - 6), (cx + 44, cy - 16), (cx + 40, cy - 2)],
              fill=(200, 208, 220))
    d.polygon([(cx - 4, cy + 6), (cx + 10, cy + 18), (cx + 16, cy + 6)],
              fill=(200, 208, 220))
    d.line([(cx - 40, cy), (cx - 52, cy)], fill=(200, 208, 220), width=3)


def island_thumb(d, x, y, w, h):
    """A Caribbean island: palm, beach, and a fuel drum on the shore."""
    d.rectangle([x, y, x + w, y + h], fill=(178, 205, 228))
    d.rectangle([x, y + h - 18, x + w, y + h], fill=(44, 92, 160))
    for wx in range(x, x + w, 22):
        d.arc([wx, y + h - 26, wx + 22, y + h - 12], 180, 360,
              fill=(44, 92, 128), width=2)
    d.polygon([(x + 18, y + h - 18), (x + 44, y + h - 40),
               (x + 78, y + h - 40), (x + 100, y + h - 18)],
              fill=(220, 200, 140))
    # palm
    d.line([(x + 52, y + h - 40), (x + 52, y + 14)], fill=(96, 72, 40),
           width=3)
    for dx, dy in ((-16, -6), (-12, 4), (16, -6), (12, 4)):
        d.arc([x + 52 + dx - 10, y + 14 + dy - 6, x + 52 + dx + 10,
               y + 14 + dy + 6], 0, 180, fill=(60, 120, 60), width=2)
    # red fuel drum
    d.rectangle([x + 82, y + h - 34, x + 98, y + h - 18], fill=RED)
    d.line([(x + 82, y + h - 29), (x + 98, y + h - 29)], fill=(120, 20, 20),
           width=1)


def field_thumb(d, x, y, w, h):
    """An Iowa field at dawn: fence posts and a blast cloud on the
    horizon."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 214, 170))
    d.ellipse([x + 8, y + 6, x + 32, y + 30], fill=(250, 196, 90))
    d.rectangle([x, y + h - 26, x + w, y + h], fill=(120, 140, 70))
    for fx in range(x + 10, x + w - 6, 26):
        d.rectangle([fx, y + h - 40, fx + 3, y + h - 24], fill=(96, 72, 40))
    d.line([(x, y + h - 34), (x + w, y + h - 34)], fill=(96, 72, 40),
           width=2)
    # blast cloud rising over the far field
    for cx, cy, r in ((x + w - 30, y + 22, 12), (x + w - 18, y + 14, 9),
                      (x + w - 42, y + 14, 8)):
        puff(d, cx, cy, r, color=(200, 200, 200))
    d.polygon([(x + w - 38, y + 30), (x + w - 30, y + 18),
               (x + w - 22, y + 30)], fill=(255, 140, 40))


ROWS = [
    ("2 · TECHNOLOGY", "Nvidia brings back Jensen Huang as chief executive",
     "Twelve days after he resigned; Trump says he may pardon him.",
     chip_thumb),
    ("3 · GAZA", "Israel kills Hamas security chief in Gaza",
     "Mohammad Abuelouf, his wife and two children killed, officials say.",
     skyline_thumb),
    ("4 · UNITED STATES", "Abrego Garcia leaves the US for Spain",
     "A Salvadoran man wrongly deported ends a 20-month legal ordeal.",
     plane_thumb),
    ("5 · CUBA", "WHO chief: end the fuel blockade endangering children",
     "Tedros urges the US to lift a blockade that starves Cuba of fuel.",
     island_thumb),
    ("6 · IOWA", "Army detonates its old explosives stockpile",
     "A controlled blast in Iowa; early air readings show no lead.",
     field_thumb),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead band
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.text((W // 2, 10), "A DAY AROUND THE WORLD", font=fnt(SERIF, 44),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 62), "WEDNESDAY, 25 NOVEMBER 2026  ·  SIX STORIES, ONE DAY",
           font=fnt(SANSB, 19), fill=GOLD, anchor="ma")

    # Map band
    draw_map(d, MARGIN, 108, W - 2 * MARGIN, 148)
    d.rectangle([MARGIN, 108, W - MARGIN, 256], outline=INK, width=2)

    # Lead story
    y = 272
    d.text((MARGIN, y), "1 · UKRAINE — THE LEAD", font=fnt(SANSB, 19),
           fill=RED)
    y += 28
    y = para(d, MARGIN, y,
             "Ukraine says it destroyed the road span of the Kerch Bridge",
             fnt(SANSB, 31), INK, W - 2 * MARGIN, 34)
    y += 4
    hero = Image.new("RGB", (W - 2 * MARGIN, 150), PAPER)
    hd = ImageDraw.Draw(hero)
    bridge_hero(hd, 0, 0, W - 2 * MARGIN, 150)
    img.paste(hero, (MARGIN, y))
    d.rectangle([MARGIN, y, W - MARGIN, y + 150], outline=INK, width=2)
    y += 150 + 8
    y = para(d, MARGIN, y,
             "Kyiv says its forces brought down the road deck of the bridge "
             "linking Russia to occupied Crimea; Moscow says it will rebuild.",
             fnt(SANS, 19), INK, W - 2 * MARGIN, 25)
    y += 6
    hline(d, MARGIN, y, W - MARGIN, 2)
    y += 12

    # Five story rows, each with its own drawn picture
    thumb_w, thumb_h = 118, 62
    for kicker, headline, summary, draw_fn in ROWS:
        thumb = Image.new("RGB", (thumb_w, thumb_h), PAPER)
        td = ImageDraw.Draw(thumb)
        draw_fn(td, 0, 0, thumb_w, thumb_h)
        img.paste(thumb, (MARGIN, y))
        d.rectangle([MARGIN, y, MARGIN + thumb_w, y + thumb_h],
                    outline=INK, width=2)
        tx = MARGIN + thumb_w + 14
        d.text((tx, y - 2), kicker, font=fnt(SANSB, 15), fill=RED)
        ty = para(d, tx, y + 18, headline, fnt(SANSB, 20), INK,
                  W - MARGIN - tx, 24)
        para(d, tx, ty + 2, summary, fnt(SANS, 16), GREY,
             W - MARGIN - tx, 20)
        y += 72
        if kicker != ROWS[-1][0]:
            hline(d, MARGIN, y - 6, W - MARGIN, 1, color=(180, 180, 175))

    # Ticker strip
    d.rectangle([0, 966, W, H], fill=NAVY)
    d.text((MARGIN, 976), "ALSO TODAY", font=fnt(SANSB, 16), fill=GOLD)
    para(d, 150, 976,
         "Sullivan concedes Alaska race to Peltola · DOJ charges 800 in a "
         "global scam crackdown · Hong Kong marks one year since its deadly "
         "fire · Sinner out after knee surgery",
         fnt(SANS, 16), (255, 255, 255), W - MARGIN - 150, 20)
    print("story rows end near y =", y, "of", H)

    out = os.path.join(HERE, "entry-r3.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
