#!/usr/bin/env python3
"""Draw the round-5 front image for news-image-20261125 (1024x1024 PNG).

Form: the atlas spread from rounds 3 and 4. A dark masthead, a world map
band with numbered pins for the six stories, one wide lead picture
(Bangkok refinery fire at night), then five story rows, each with its
own small drawn picture, and a ticker strip at the foot.

Stories: Friday 27 November 2026, none of them used in round 1, 2, 3
or 4 (round 1: Gulf of Finland warship, Riyadh tower, CIA breach,
NATO jets, Hormuz tankers, Gaza toll, Giuliani medal; round 2: Ras
Tanura, Sudan RSF, Australia treaty, Pakistani astronaut, Huawei,
Trump tariffs, Pope/COP31; round 3: Kerch Bridge, Nvidia/Huang,
Abuelouf Gaza, Abrego Garcia, Cuba fuel blockade, Iowa explosives;
round 4: Kyiv missiles, Gaza Abu Nada, FCC SpaceX Starmind, North
Korea expels Swiss diplomat, Ramaphosa impeachment report, DR Congo
Ebola 12,000).

  1. BANGKOK (lead) — Massive fire at a Bangkok oil refinery; several
     people injured, Bangchak Corp shuts all units.
  2. USA — A Thanksgiving storm disrupts the North West; NYC postpones
     the 100th Macy's parade, 500,000+ lose power, flights cancelled.
  3. NEW ZEALAND — Final election results: coalition holds a slim
     67-of-131 majority after ~400,000 special votes counted.
  4. INDONESIA — Rescue teams search for workers trapped in an illegal
     gold mine.
  5. CHESS — World Chess Championship Game 3: Gukesh vs Sindarov, a
     marathon draw, nothing separates them after three games.
  6. CRICKET — India's 17-year-old Vaibhav Sooryavanshi smashes an
     unbeaten 204 off 53 balls vs the UAE in the Asia Cup Rising Stars.

Ticker: Saudi Arabia intercepts two Houthi missiles aimed at Riyadh;
Karachi building collapse kills three; Bank of Korea lifts rates on the
AI chip boom; Flipkart CEO Kalyan Krishnamurthy to step down.

Deterministic: fixed geometry, fixed fonts, no randomness, no network,
no timestamps anywhere in the image.
Run:  python3 compose-r5.py
Writes entry-r5.png next to this file.
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
    # 1 Bangkok, 2 New York, 3 Wellington, 4 Jakarta,
    # 5 India (Gukesh), 6 Doha.
    pin(d, x + 800, y + 60, 1)
    pin(d, x + 150, y + 40, 2)
    pin(d, x + 925, y + 132, 3)
    pin(d, x + 835, y + 88, 4)
    pin(d, x + 700, y + 52, 5)
    pin(d, x + 645, y + 58, 6)
    d.text((x + 8, y + h - 22), "WHERE THE DAY HAPPENED",
           font=fnt(SANSB, 15), fill=NAVY)


def puff(d, cx, cy, r, color=(140, 140, 140)):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color)


def bangkok_hero(d, x, y, w, h):
    """Bangkok refinery at night: storage tanks and distillation columns
    against a dark sky, flames leaping from a ruptured tank, and thick
    black smoke rolling over the plant."""
    d.rectangle([x, y, x + w, y + h], fill=(16, 20, 36))
    for sx, sy in ((x + 60, y + 14), (x + 180, y + 26), (x + 320, y + 10),
                   (x + 470, y + 22), (x + 620, y + 12), (x + 780, y + 24),
                   (x + 900, y + 14), (x + 250, y + 40), (x + 560, y + 38)):
        d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(220, 225, 240))
    # moon
    d.ellipse([x + w - 120, y + 12, x + w - 70, y + 62],
              fill=(240, 232, 200))
    # storage tanks along the ground
    base = y + h - 40
    for tx0, tw in ((x + 10, 110), (x + 140, 96), (x + 256, 120),
                    (x + 640, 110), (x + 770, 100), (x + 886, 88)):
        d.ellipse([tx0, base - 52, tx0 + tw, base - 30], fill=(70, 76, 88))
        d.rectangle([tx0, base - 42, tx0 + tw, base], fill=(52, 58, 70))
        d.rectangle([tx0, base - 42, tx0 + tw, base - 36], fill=(88, 94, 108))
    # distillation columns
    for cx0 in (x + 400, x + 430, x + 460):
        d.rectangle([cx0, base - 96, cx0 + 16, base], fill=(64, 70, 84))
        d.line([(cx0, base - 80), (cx0 + 16, base - 80)], fill=(88, 94, 108),
               width=2)
        d.line([(cx0, base - 60), (cx0 + 16, base - 60)], fill=(88, 94, 108),
               width=2)
    # flames leaping from the ruptured middle tank
    fx = x + 316
    d.polygon([(fx - 34, base), (fx - 18, base - 66), (fx - 4, base - 30),
               (fx + 8, base - 78), (fx + 22, base - 34), (fx + 34, base)],
              fill=(255, 140, 30))
    d.polygon([(fx - 18, base), (fx - 8, base - 44), (fx + 2, base - 18),
               (fx + 12, base - 52), (fx + 20, base)],
              fill=(255, 196, 60))
    # thick black smoke rolling over the plant
    for cx, cy, r in ((fx - 10, base - 88, 16), (fx + 14, base - 104, 13),
                      (fx - 30, base - 100, 10), (fx + 34, base - 86, 9),
                      (fx + 4, base - 120, 8)):
        puff(d, cx, cy, r, color=(38, 38, 44))
    # ground glow and fire-engine lights
    d.rectangle([x, base, x + w, y + h], fill=(28, 26, 30))
    for lx in range(x + 40, x + w, 120):
        d.line([(lx, base + 22), (lx + 40, base + 22)], fill=GOLD, width=3)
    d.rectangle([x + 700, base + 6, x + 760, base + 26], fill=(178, 34, 34))
    d.rectangle([x + 712, base + 12, x + 722, base + 20], fill=(255, 196, 60))


def storm_thumb(d, x, y, w, h):
    """A Thanksgiving storm: black clouds, slanting rain, a bent tree,
    and a fallen power line over a dark house."""
    d.rectangle([x, y, x + w, y + h], fill=(52, 58, 74))
    for cx, cy, r in ((x + 24, y + 12, 14), (x + 52, y + 8, 17),
                      (x + 84, y + 14, 13), (x + 104, y + 10, 9)):
        puff(d, cx, cy, r, color=(30, 34, 46))
    # slanting rain
    for rx in range(x + 6, x + w - 4, 12):
        d.line([(rx, y + 28), (rx - 5, y + 44)], fill=(168, 198, 224),
               width=2)
    # dark house with one lit window
    d.rectangle([x + 8, y + h - 22, x + 44, y + h - 4], fill=(24, 26, 34))
    d.polygon([(x + 6, y + h - 22), (x + 26, y + h - 34),
               (x + 46, y + h - 22)], fill=(18, 20, 28))
    d.rectangle([x + 20, y + h - 16, x + 28, y + h - 8], fill=(250, 196, 90))
    # bent tree and fallen power line
    d.line([(x + 70, y + h - 4), (x + 82, y + h - 30)], fill=(40, 52, 30),
           width=3)
    d.line([(x + 82, y + h - 30), (x + 96, y + h - 22)], fill=(40, 52, 30),
           width=2)
    d.line([(x + 60, y + h - 34), (x + 110, y + h - 26)], fill=(200, 208, 220),
           width=2)
    d.line([(x + 88, y + h - 30), (x + 92, y + h - 8)], fill=(200, 208, 220),
           width=2)


def ballot_thumb(d, x, y, w, h):
    """A ballot box with a paper going in, and a parliament dome behind
    it under a pale sky."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 224, 236))
    # parliament dome
    d.ellipse([x + 74, y + 6, x + 110, y + 34], fill=(120, 128, 140))
    d.rectangle([x + 70, y + 30, x + w - 4, y + h - 8], fill=(148, 156, 168))
    for wx in range(x + 76, x + w - 10, 12):
        d.rectangle([wx, y + 38, wx + 6, y + 48], fill=(40, 48, 60))
    # ballot box
    d.rectangle([x + 8, y + h - 30, x + 56, y + h - 6], fill=(24, 44, 78))
    d.rectangle([x + 6, y + h - 34, x + 58, y + h - 28], fill=(36, 58, 96))
    d.line([(x + 26, y + h - 31), (x + 38, y + h - 31)], fill=(250, 246, 236),
           width=2)
    # paper sliding into the slot, with a tick
    d.polygon([(x + 24, y + 10), (x + 40, y + 8), (x + 38, y + h - 30),
               (x + 26, y + h - 30)], fill=(250, 248, 240))
    d.line([(x + 28, y + 18), (x + 32, y + 22), (x + 38, y + 14)],
           fill=RED, width=2)


def mine_thumb(d, x, y, w, h):
    """A mine headframe tower over a dark shaft mouth, with a rescuer's
    lamp glowing at the entrance."""
    d.rectangle([x, y, x + w, y + h], fill=(222, 210, 180))
    d.rectangle([x, y + h - 10, x + w, y + h], fill=(96, 84, 66))
    # headframe: two legs and a crossbeam with a wheel on top
    d.line([(x + 44, y + h - 10), (x + 54, y + 8)], fill=(60, 52, 44),
           width=4)
    d.line([(x + 74, y + h - 10), (x + 64, y + 8)], fill=(60, 52, 44),
           width=4)
    d.line([(x + 46, y + 20), (x + 72, y + 20)], fill=(60, 52, 44), width=3)
    d.ellipse([x + 52, y + 2, x + 66, y + 16], fill=(40, 36, 30))
    d.line([(x + 59, y + 9), (x + 59, y + h - 10)], fill=(40, 36, 30),
           width=2)
    # shaft mouth: a black arch in the hillside
    d.pieslice([x + 82, y + h - 34, x + 112, y + h - 4], 180, 360,
               fill=(16, 14, 12))
    d.rectangle([x + 82, y + h - 20, x + 112, y + h - 10], fill=(16, 14, 12))
    # rescuer's lamp glowing at the entrance
    d.ellipse([x + 92, y + h - 16, x + 102, y + h - 6], fill=(255, 196, 60))
    d.ellipse([x + 95, y + h - 13, x + 99, y + h - 9], fill=(255, 240, 180))


def chess_thumb(d, x, y, w, h):
    """A chessboard mid-game: a white king and a black queen facing off,
    with a clock ticking at the side."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 222, 196))
    # 4x4 board
    sq = 12
    ox, oy = x + 6, y + 8
    for r in range(4):
        for c in range(4):
            fill = (250, 246, 236) if (r + c) % 2 == 0 else (60, 52, 44)
            d.rectangle([ox + c * sq, oy + r * sq,
                         ox + (c + 1) * sq, oy + (r + 1) * sq], fill=fill)
    # white king on the light square
    kx, ky = ox + 6, oy + 6
    d.rectangle([kx + 3, ky + 8, kx + 9, ky + 16], fill=(250, 248, 240))
    d.ellipse([kx + 2, ky + 1, kx + 10, ky + 9], fill=(250, 248, 240))
    d.rectangle([kx + 5, ky - 1, kx + 7, ky + 3], fill=(250, 248, 240))
    # black queen opposite
    qx, qy = ox + 30, oy + 30
    d.rectangle([qx + 3, qy + 8, qx + 9, qy + 16], fill=(24, 22, 20))
    d.ellipse([qx + 2, qy + 1, qx + 10, qy + 9], fill=(24, 22, 20))
    d.polygon([(qx + 2, qy + 2), (qx + 6, qy - 3), (qx + 10, qy + 2)],
              fill=(24, 22, 20))
    # clock at the side
    d.ellipse([x + w - 26, y + 8, x + w - 6, y + 28], fill=(250, 248, 240))
    d.ellipse([x + w - 24, y + 10, x + w - 8, y + 26], fill=(24, 44, 78))
    d.line([(x + w - 16, y + 18), (x + w - 16, y + 12)], fill=GOLD, width=2)
    d.line([(x + w - 16, y + 18), (x + w - 11, y + 18)], fill=GOLD, width=2)


def cricket_thumb(d, x, y, w, h):
    """A cricket pitch at dusk: a batsman mid-swing, the stumps behind
    him, and a red ball flying to the boundary."""
    d.rectangle([x, y, x + w, y + h], fill=(120, 168, 90))
    d.rectangle([x, y + h - 14, x + w, y + h], fill=(96, 140, 70))
    # the pitch strip
    d.rectangle([x + 20, y + 8, x + w - 20, y + h - 14], fill=(214, 196, 150))
    # stumps at the far end
    for sx in (x + 52, x + 58, x + 64):
        d.line([(sx, y + 12), (sx, y + 26)], fill=(250, 240, 200), width=2)
    d.line([(x + 52, y + 12), (x + 66, y + 12)], fill=(250, 240, 200),
           width=2)
    # batsman mid-swing: body, bat, and helmet
    d.ellipse([x + 78, y + 22, x + 90, y + 34], fill=(24, 44, 78))
    d.rectangle([x + 78, y + 34, x + 90, y + h - 14], fill=(250, 248, 240))
    d.line([(x + 88, y + 30), (x + 104, y + 16)], fill=(150, 110, 60),
           width=4)
    d.line([(x + 80, y + 44), (x + 66, y + h - 14)], fill=(24, 44, 78),
           width=3)
    d.line([(x + 88, y + 44), (x + 98, y + h - 14)], fill=(24, 44, 78),
           width=3)
    # red ball flying to the boundary
    d.ellipse([x + w - 16, y + 8, x + w - 6, y + 18], fill=RED)
    d.arc([x + w - 24, y + 2, x + w - 2, y + 24], 300, 60, fill=RED,
          width=2)


ROWS = [
    ("2 · USA", "Thanksgiving storm halts the parade, cuts power to 500,000+",
     "New York postpones its 100th parade for the first time as a huge "
     "storm cancels hundreds of flights.",
     storm_thumb),
    ("3 · NEW ZEALAND", "Final count gives coalition a slim 67-of-131 majority",
     "Roughly 400,000 special votes are counted; a hung parliament is "
     "still possible.",
     ballot_thumb),
    ("4 · INDONESIA", "Rescue search for workers trapped in illegal gold mine",
     "Teams work around the clock at the collapsed mine site.",
     mine_thumb),
    ("5 · CHESS", "Gukesh vs Sindarov: marathon draw in Game 3",
     "The longest game of the series so far leaves nothing between "
     "them after three games.",
     chess_thumb),
    ("6 · CRICKET", "Teen Sooryavanshi smashes unbeaten 204 off 53 balls",
     "The 17-year-old's record knock powers India past the UAE.",
     cricket_thumb),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead band
    d.rectangle([0, 0, W, 96], fill=NAVY)
    d.text((W // 2, 10), "A DAY AROUND THE WORLD", font=fnt(SERIF, 44),
           fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 62), "FRIDAY, 27 NOVEMBER 2026  ·  SIX STORIES, ONE DAY",
           font=fnt(SANSB, 19), fill=GOLD, anchor="ma")

    # Map band
    draw_map(d, MARGIN, 108, W - 2 * MARGIN, 148)
    d.rectangle([MARGIN, 108, W - MARGIN, 256], outline=INK, width=2)

    # Lead story
    y = 272
    d.text((MARGIN, y), "1 · BANGKOK — THE LEAD", font=fnt(SANSB, 19),
           fill=RED)
    y += 28
    y = para(d, MARGIN, y,
             "Massive fire at Bangkok oil refinery; several injured",
             fnt(SANSB, 31), INK, W - 2 * MARGIN, 34)
    y += 4
    hero = Image.new("RGB", (W - 2 * MARGIN, 150), PAPER)
    hd = ImageDraw.Draw(hero)
    bangkok_hero(hd, 0, 0, W - 2 * MARGIN, 150)
    img.paste(hero, (MARGIN, y))
    d.rectangle([MARGIN, y, W - MARGIN, y + 150], outline=INK, width=2)
    y += 150 + 8
    y = para(d, MARGIN, y,
             "Flames leapt from a ruptured tank at the Bangchak plant; "
             "the company shut every unit as crews fought the blaze.",
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
         "Saudi Arabia intercepts two Houthi missiles aimed at Riyadh · "
         "Karachi building collapse kills three · Bank of Korea lifts rates "
         "on the AI chip boom · Flipkart CEO to step down next month",
         fnt(SANS, 16), (255, 255, 255), W - MARGIN - 150, 20)
    print("story rows end near y =", y, "of", H)

    out = os.path.join(HERE, "entry-r5.png")
    img.save(out, "PNG", optimize=True)
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
