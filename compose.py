#!/usr/bin/env python3
"""Draw the round-4 front image for news-image-20261125 (1024x1024 PNG).

Form: the atlas spread from round 3. A dark masthead, a world map band
with numbered pins for the six stories, one wide lead picture (Kyiv at
night, under a missile strike), then five story rows, each with its own
small drawn picture, and a ticker strip at the foot.

Stories: Thursday 26 November 2026, none of them used in round 1, 2
or 3 (round 1: Gulf of Finland warship, Riyadh tower, CIA breach,
NATO jets, Hormuz tankers, Gaza toll, Giuliani medal; round 2: Ras
Tanura, Sudan RSF, Australia treaty, Pakistani astronaut, Huawei,
Trump tariffs, Pope/COP31; round 3: Kerch Bridge, Nvidia/Huang,
Abuelouf Gaza, Abrego Garcia, Cuba fuel blockade, Iowa explosives).

  1. KYIV (lead) — Russian ballistic missiles strike Kyiv overnight,
     hitting a shopping centre; seven people wounded.
  2. GAZA — Israeli strikes kill nine in Gaza, including the
     Hamas-appointed deputy education minister Khaled Abu Nada.
  3. SPACE — The FCC approves SpaceX's plan for up to one million
     satellites for orbital data centres.
  4. NORTH KOREA — Pyongyang expels Switzerland's top diplomat and
     orders its reopened office closed.
  5. SOUTH AFRICA — A court throws out the report behind the
     Ramaphosa impeachment push.
  6. DR CONGO — Ebola cases pass 12,000 in the worst outbreak.

Ticker: EU leaders meet over a 2 trillion euro budget; king tides
flood California's coast; memory-chip shortage triples some RAM
prices; China investigates Shanghai party chief Chen Jining.

Deterministic: fixed geometry, fixed fonts, no randomness, no network,
no timestamps anywhere in the image.
Run:  python3 compose-r4.py
Writes entry-r4.png next to this file.
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
    # 1 Kyiv, 2 Gaza, 3 Washington DC, 4 Pyongyang, 5 Cape Town,
    # 6 DR Congo (Kinshasa).
    pin(d, x + 578, y + 38, 1)
    pin(d, x + 556, y + 62, 2)
    pin(d, x + 168, y + 56, 3)
    pin(d, x + 880, y + 40, 4)
    pin(d, x + 540, y + 118, 5)
    pin(d, x + 520, y + 88, 6)
    d.text((x + 8, y + h - 22), "WHERE THE DAY HAPPENED",
           font=fnt(SANSB, 15), fill=NAVY)


def puff(d, cx, cy, r, color=(140, 140, 140)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def kyiv_hero(d, x, y, w, h):
    """Kyiv at night: a dark skyline, a missile trail arcing down, and
    a blast flash with smoke over a shopping centre."""
    d.rectangle([x, y, x + w, y + h], fill=(18, 26, 48))
    for sx, sy in ((x + 60, y + 14), (x + 180, y + 26), (x + 320, y + 10),
                   (x + 470, y + 22), (x + 620, y + 12), (x + 780, y + 24),
                   (x + 900, y + 14), (x + 250, y + 40), (x + 560, y + 38)):
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(220, 225, 240))
    # moon
    d.ellipse([x + w - 120, y + 12, x + w - 70, y + 62],
              fill=(240, 232, 200))
    # missile trail arcing down from the upper right
    for i, (tx, ty) in enumerate(((x + 700, y + 16), (x + 660, y + 34),
                                  (x + 620, y + 54), (x + 585, y + 76))):
        d.ellipse([tx - 3, ty - 3, tx + 3, ty + 3],
                  fill=(255, 200, 90) if i == 3 else (255, 160, 60))
    # blast flash over the rooftops
    bx, by = x + 580, y + h - 58
    d.polygon([(bx, by - 34), (bx + 12, by - 8), (bx + 34, by - 12),
               (bx + 16, by + 2), (bx + 26, by + 18), (bx, by + 8),
               (bx - 26, by + 18), (bx - 16, by + 2), (bx - 34, by - 12),
               (bx - 12, by - 8)], fill=(255, 196, 60))
    d.polygon([(bx, by - 18), (bx + 7, by - 4), (bx + 18, by - 6),
               (bx + 9, by + 2), (bx + 14, by + 10), (bx, by + 4),
               (bx - 14, by + 10), (bx - 9, by + 2), (bx - 18, by - 6),
               (bx - 7, by - 4)], fill=(255, 120, 30))
    # smoke rising from the blast
    for cx, cy, r in ((bx - 6, by - 44, 13), (bx + 10, by - 58, 10),
                      (bx - 20, by - 56, 8), (bx + 22, by - 40, 7)):
        puff(d, cx, cy, r, color=(120, 120, 128))
    # skyline silhouette
    base = y + h - 40
    for bx0, bw, bh in ((x + 10, 70, 52), (x + 90, 56, 74), (x + 156, 80, 44),
                        (x + 246, 60, 88), (x + 316, 72, 58), (x + 398, 64, 80),
                        (x + 472, 76, 48), (x + 640, 66, 70), (x + 716, 80, 54),
                        (x + 806, 60, 78), (x + 876, 70, 46)):
        d.rectangle([bx0, base - bh, bx0 + bw, base], fill=(8, 12, 24))
        for wy in range(base - bh + 8, base - 6, 12):
            for wx in range(bx0 + 8, bx0 + bw - 8, 14):
                d.rectangle([wx, wy, wx + 5, wy + 6], fill=(250, 196, 90))
    # damaged building: top corner gone, by the blast
    d.polygon([(x + 472, base - 48), (x + 486, base - 48),
               (x + 548, base - 34), (x + 548, base), (x + 472, base)],
              fill=(5, 8, 16))
    # street
    d.rectangle([x, base, x + w, y + h], fill=(30, 32, 40))
    for lx in range(x + 40, x + w, 120):
        d.line([(lx, base + 22), (lx + 40, base + 22)], fill=GOLD, width=3)


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


def satellite_thumb(d, x, y, w, h):
    """A satellite with gold panels crossing a starry sky over Earth."""
    d.rectangle([x, y, x + w, y + h], fill=(12, 18, 40))
    for sx, sy in ((x + 10, y + 10), (x + 34, y + 22), (x + 70, y + 8),
                   (x + 96, y + 18), (x + 110, y + 6), (x + 52, y + 30)):
        d.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(230, 235, 245))
    # Earth curve at the foot
    d.ellipse([x - 30, y + h - 14, x + w + 30, y + h + 40],
              fill=(44, 92, 160))
    d.ellipse([x + 18, y + h - 10, x + 52, y + h + 8], fill=(60, 140, 80))
    # satellite body and panels
    cx, cy = x + w // 2, y + h // 2 - 4
    d.rectangle([cx - 34, cy - 6, cx - 10, cy + 6], fill=(214, 164, 60))
    d.rectangle([cx + 10, cy - 6, cx + 34, cy + 6], fill=(214, 164, 60))
    d.rectangle([cx - 10, cy - 9, cx + 10, cy + 9], fill=(200, 208, 220))
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(24, 44, 78))
    d.line([(cx + 10, cy - 12), (cx + 22, cy - 22)], fill=(200, 208, 220),
           width=2)
    d.ellipse([cx + 20, cy - 24, cx + 24, cy - 20], fill=(255, 196, 60))


def embassy_thumb(d, x, y, w, h):
    """A shuttered embassy: a grey office block, a flag at half-mast,
    and a closed gate."""
    d.rectangle([x, y, x + w, y + h], fill=(196, 204, 214))
    d.rectangle([x + 14, y + 8, x + w - 14, y + h - 14], fill=(120, 128, 140))
    for wy in range(y + 16, y + h - 20, 12):
        for wx in range(x + 20, x + w - 20, 16):
            d.rectangle([wx, wy, wx + 8, wy + 7], fill=(40, 48, 60))
    # flagpole with a small red flag lowered halfway
    d.line([(x + 62, y + 4), (x + 62, y + 26)], fill=(240, 244, 250),
           width=2)
    d.rectangle([x + 62, y + 12, x + 82, y + 20], fill=RED)
    # closed gate bars across the foot
    for gx in range(x + 6, x + w - 6, 10):
        d.line([(gx, y + h - 12), (gx, y + h - 2)], fill=(30, 34, 40),
               width=2)
    d.line([(x, y + h - 12), (x + w, y + h - 12)], fill=(30, 34, 40),
           width=2)


def court_thumb(d, x, y, w, h):
    """A courthouse front: columns, a pediment, and a gavel's echo in
    the steps."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 214))
    d.polygon([(x + 10, y + 22), (x + w // 2, y + 4), (x + w - 10, y + 22)],
              fill=(180, 172, 150))
    for cx in (x + 22, x + 46, x + 70, x + 94):
        d.rectangle([cx - 4, y + 24, cx + 4, y + h - 14], fill=(250, 248, 240))
        d.rectangle([cx - 7, y + 22, cx + 7, y + 26], fill=(210, 202, 180))
        d.rectangle([cx - 7, y + h - 16, cx + 7, y + h - 12],
                    fill=(210, 202, 180))
    d.rectangle([x, y + h - 12, x + w, y + h], fill=(150, 142, 122))
    # scales of justice above the door
    d.line([(x + w // 2, y + 26), (x + w // 2, y + 34)], fill=(90, 78, 60),
           width=2)
    d.line([(x + w // 2 - 10, y + 28), (x + w // 2 + 10, y + 28)],
           fill=(90, 78, 60), width=2)


def clinic_thumb(d, x, y, w, h):
    """A field clinic tent with a red cross, under a pale sun."""
    d.rectangle([x, y, x + w, y + h], fill=(238, 228, 200))
    d.ellipse([x + 8, y + 6, x + 30, y + 28], fill=(250, 196, 90))
    d.rectangle([x, y + h - 16, x + w, y + h], fill=(120, 140, 70))
    # tent
    d.polygon([(x + 24, y + h - 16), (x + 59, y + 18), (x + 94, y + h - 16)],
              fill=(240, 244, 250))
    d.polygon([(x + 24, y + h - 16), (x + 59, y + 18), (x + 59, y + h - 16)],
              fill=(214, 220, 230))
    d.rectangle([x + 54, y + h - 26, x + 64, y + h - 16], fill=(90, 78, 60))
    # red cross on the tent
    d.rectangle([x + 56, y + 30, x + 62, y + 44], fill=RED)
    d.rectangle([x + 50, y + 35, x + 68, y + 41], fill=RED)


ROWS = [
    ("2 · GAZA", "Israeli strikes kill nine in Gaza, deputy minister dead",
     "Khaled Abu Nada, the Hamas-appointed deputy education minister, "
     "killed in Deir al-Balah.",
     skyline_thumb),
    ("3 · SPACE", "FCC clears SpaceX plan for a million satellites",
     "Orbital data centres get the go-ahead in Washington.",
     satellite_thumb),
    ("4 · NORTH KOREA", "Pyongyang expels Swiss envoy, shuts reopened office",
     "Five weeks after the mission resumed, North Korea orders it closed.",
     embassy_thumb),
    ("5 · SOUTH AFRICA", "Court throws out report behind Ramaphosa push",
     "Judges reject the case that fuelled calls to remove the president.",
     court_thumb),
    ("6 · DR CONGO", "Ebola cases pass 12,000 in worst outbreak",
     "Health officials warn the epidemic is still accelerating.",
     clinic_thumb),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead band
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.text((W // 2, 10), "A DAY AROUND THE WORLD", font=fnt(SERIF, 44),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 62), "THURSDAY, 26 NOVEMBER 2026  ·  SIX STORIES, ONE DAY",
           font=fnt(SANSB, 19), fill=GOLD, anchor="ma")

    # Map band
    draw_map(d, MARGIN, 108, W - 2 * MARGIN, 148)
    d.rectangle([MARGIN, 108, W - MARGIN, 256], outline=INK, width=2)

    # Lead story
    y = 272
    d.text((MARGIN, y), "1 · KYIV — THE LEAD", font=fnt(SANSB, 19),
           fill=RED)
    y += 28
    y = para(d, MARGIN, y,
             "Russian missiles hit Kyiv overnight; seven wounded",
             fnt(SANSB, 31), INK, W - 2 * MARGIN, 34)
    y += 4
    hero = Image.new("RGB", (W - 2 * MARGIN, 150), PAPER)
    hd = ImageDraw.Draw(hero)
    kyiv_hero(hd, 0, 0, W - 2 * MARGIN, 150)
    img.paste(hero, (MARGIN, y))
    d.rectangle([MARGIN, y, W - MARGIN, y + 150], outline=INK, width=2)
    y += 150 + 8
    y = para(d, MARGIN, y,
             "Ballistic missiles struck a shopping centre in the capital's "
             "Desnianskyi district; the mayor says seven people were hurt.",
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
         "EU leaders meet over a 2 trillion euro budget · King tides flood "
         "California's coast · Memory-chip shortage triples some RAM prices "
         "· China investigates Shanghai party chief Chen Jining",
         fnt(SANS, 16), (255, 255, 255), W - MARGIN - 150, 20)
    print("story rows end near y =", y, "of", H)

    out = os.path.join(HERE, "entry-r4.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
