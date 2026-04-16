#!/usr/bin/env node
/**
 * pipeline.js — extract → deploy
 *
 * Usage:
 *   node scripts/pipeline.js --date 2026-04-15 --eur img.png --usd img.png
 *   npm run pipeline -- --date 2026-04-15 --eur img.png --usd img.png
 */

'use strict';

const { execSync } = require('child_process');
const path         = require('path');
const ROOT         = path.join(__dirname, '..');

function run(cmd, label) {
  console.log(`\n── ${label} ${'─'.repeat(50 - label.length)}`);
  execSync(cmd, { stdio: 'inherit', cwd: ROOT });
}

const args = process.argv.slice(2).map(a => `"${a}"`).join(' ');

run(`node scripts/extract.js ${args}`, '1/2  extract');
run('node scripts/deploy.js',          '2/2  deploy');

console.log('\n✓ Pipeline complete');
