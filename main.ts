// A make.fun news-image entry (Node 22, standard library only) for
// round 3 of news-image-20261125.
//
// The entry image lives beside this file as entry.png. This program
// copies it to /output/entry.png and nothing else. Before the copy it
// proves the file is a whole PNG of the size the bounty allows: the
// eight PNG magic bytes, a 1024 by 1024 header, and at most 1 MiB.
// The grader runs the program twice; both runs write the same bytes
// because the source file never changes between runs.
//
// Round 3: the image is "A Day Around the World" — a world map with
// numbered pins, the Kerch Bridge as the lead picture, and five story
// rows. It was drawn by compose.py (Pillow) and saved as entry.png.
// The program writes exactly one file, /output/entry.png, and reads
// exactly one file, the entry.png beside it.
// At push time this file is renamed to main.ts and entry-r3.png to
// entry.png.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
// /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main-r3.ts

import { copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

const MAX_BYTES = 1048576;
const WANT_WIDTH = 1024;
const WANT_HEIGHT = 1024;

const PNG_MAGIC = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

function checkPng(data: Buffer): void {
  if (data.length < 33) {
    throw new Error('entry.png is too short to be a PNG file');
  }
  for (let i = 0; i < PNG_MAGIC.length; i += 1) {
    if (data[i] !== PNG_MAGIC[i]) {
      throw new Error('entry.png does not start with the PNG magic bytes');
    }
  }
  if (data.length > MAX_BYTES) {
    throw new Error(`entry.png is ${data.length} bytes, over the 1 MiB limit`);
  }
  const width = data.readUInt32BE(16);
  const height = data.readUInt32BE(20);
  if (width !== WANT_WIDTH || height !== WANT_HEIGHT) {
    throw new Error(
      `entry.png is ${width}x${height}, not ${WANT_WIDTH}x${WANT_HEIGHT}`,
    );
  }
}

const src = new URL('./entry.png', import.meta.url);
const data = readFileSync(src);
checkPng(data);

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, 'entry.png'));
