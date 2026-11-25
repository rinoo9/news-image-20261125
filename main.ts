// A make.fun news-image entry (Node 22, standard library only): the image
// beside this file is copied to /output/entry.png. It is the day's front
// page — Wednesday 25 November 2026 — led by the confirmed story of the day:
// Ukrainian drones struck two Russian vessels, a warship sunk off Benghazi
// and a cargo ship hit in the Gulf of Finland, the ship in the hero photo.
// The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024
// pixels, and the judge sees exactly the bytes copied, so this program
// checks the file before it copies it: it must really be a PNG, exactly
// 1024x1024 from its header, and no bigger than 1 MiB. Two runs write
// byte-identical output, because the program copies a fixed file.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const src = new URL('./entry.png', import.meta.url);
const data = readFileSync(src);
if (data.length < 33 || data[0] !== 0x89 || data[1] !== 0x50 ||
    data[2] !== 0x4e || data[3] !== 0x47) {
  throw new Error('entry.png is not a PNG file');
}
if (data.length > 1048576) {
  throw new Error('entry.png is over the 1 MiB limit');
}
// The first chunk must be IHDR, 13 bytes, or the header is not a PNG's:
// a file with a PNG signature but a different first chunk is not whole.
if (data.readUInt32BE(8) !== 13 || data.toString('latin1', 12, 16) !== 'IHDR') {
  throw new Error('entry.png has no IHDR chunk first');
}
const width = data.readUInt32BE(16);
const height = data.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  throw new Error(`entry.png is ${width}x${height}, not 1024x1024`);
}
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, 'entry.png'));
