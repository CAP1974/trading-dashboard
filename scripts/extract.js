#!/usr/bin/env node
/**
 * extract.js — eToro screenshot → Claude Vision → trading_data.json + data.js
 *
 * Estrutura real do trading_data.json (flat por data):
 *   { "2025-04-09": { date, eventos, eur: { lucro, positions[] }, usd: { lucro, positions[] } }, ... }
 *
 * Usage:
 *   node scripts/extract.js --date 2025-04-16 --eur path/eur.png --usd path/usd.png
 *   node scripts/extract.js --date 2025-04-16 --eur path/eur.png
 *
 * Env:  ANTHROPIC_API_KEY  (required)
 */

'use strict';

const fs        = require('fs');
const path      = require('path');
const Anthropic = require('@anthropic-ai/sdk');

// ── carrega API key do ficheiro .env ───────────────────────────────────────
(function loadEnv() {
  const root     = path.join(__dirname, '..');
  const envFiles = ['ANTHROPIC_API_KEY.env', '.env'];
  for (const name of envFiles) {
    const p = path.join(root, name);
    if (fs.existsSync(p)) {
      fs.readFileSync(p, 'utf8').split('\n').forEach(line => {
        const m = line.trim().match(/^([^#=]+)=(.*)$/);
        if (m && !process.env[m[1].trim()]) {
          process.env[m[1].trim()] = m[2].trim();
        }
      });
      console.log(`Env carregado: ${name}`);
      break;
    }
  }
})();

// ── args ───────────────────────────────────────────────────────────────────
const args    = process.argv.slice(2);
const get     = flag => { const i = args.indexOf(flag); return i !== -1 ? args[i + 1] : null; };

const date    = get('--date') || new Date().toISOString().slice(0, 10);
const eurPath = get('--eur');
const usdPath = get('--usd');

if (!eurPath && !usdPath) {
  console.error('Usage: node scripts/extract.js --date YYYY-MM-DD [--eur <img>] [--usd <img>]');
  process.exit(1);
}

const DATA_FILE    = path.join(__dirname, '..', 'data', 'trading_data.json');
const DATA_JS      = path.join(__dirname, '..', 'data.js');
const BACKUP_DIR   = path.join(__dirname, '..', 'data', 'backups');
const MAX_BACKUPS  = 30;

function makeBackup() {
  if (!fs.existsSync(DATA_FILE)) return;
  if (!fs.existsSync(BACKUP_DIR)) fs.mkdirSync(BACKUP_DIR, { recursive: true });
  const now  = new Date();
  const pad  = n => String(n).padStart(2, '0');
  const stamp = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())}_${pad(now.getHours())}${pad(now.getMinutes())}`;
  const dest = path.join(BACKUP_DIR, `trading_data_${stamp}.json`);
  fs.copyFileSync(DATA_FILE, dest);
  console.log(`Backup → ${path.basename(dest)}`);
  // keep only last MAX_BACKUPS
  const files = fs.readdirSync(BACKUP_DIR)
    .filter(f => f.startsWith('trading_data_') && f.endsWith('.json'))
    .sort();
  if (files.length > MAX_BACKUPS) {
    files.slice(0, files.length - MAX_BACKUPS).forEach(f => {
      fs.unlinkSync(path.join(BACKUP_DIR, f));
      console.log(`Backup antigo removido: ${f}`);
    });
  }
}

const client = new Anthropic();

// ── Claude Vision ──────────────────────────────────────────────────────────
async function extractPositions(imagePath, currency) {
  const buf       = fs.readFileSync(imagePath);
  const base64    = buf.toString('base64');
  const ext       = path.extname(imagePath).toLowerCase();
  const mediaType = (ext === '.jpg' || ext === '.jpeg') ? 'image/jpeg'
                  : ext === '.webp'                     ? 'image/webp'
                  : ext === '.gif'                      ? 'image/gif'
                  :                                       'image/png';

  const prompt = `This is an eToro trading screenshot showing ${currency} positions.

Extract ALL visible positions as a JSON array. For each position use these exact fields:
{
  "name":      instrument/stock name as shown (e.g. "Ericsson", "Samsung", "Micron"),
  "mkt":       "${currency}",
  "pct":       P&L percentage as number (e.g. 2.35 or -4.10),
  "lucro":     P&L amount as number (positive = profit, negative = loss),
  "vol":       volume/units as number,
  "valor":     current invested value as number,
  "atual":     current price as number,
  "abertura":  open/entry price as number,
  "trust":     "v" (green/good), "a" (yellow/neutral), or "r" (red/bad) based on performance,
  "delta":     { "pct": day_change_pct, "val": day_change_value } or null if not shown
}

Also extract the total P&L shown for the ${currency} section as a separate number.

Return ONLY this JSON object, no markdown, no explanation:
{
  "lucro": <total pnl number>,
  "positions": [ <array of positions> ]
}`;

  const response = await client.messages.create({
    model:      'claude-opus-4-5',
    max_tokens: 4096,
    messages: [{
      role:    'user',
      content: [
        { type: 'image', source: { type: 'base64', media_type: mediaType, data: base64 } },
        { type: 'text',  text: prompt }
      ]
    }]
  });

  const text    = response.content[0].text.trim();
  const cleaned = text.replace(/^```json?\s*/i, '').replace(/\s*```$/, '').trim();

  try {
    return JSON.parse(cleaned);
  } catch (e) {
    console.error(`  Falha a parsear resposta Claude para ${currency}:`);
    console.error('  Raw:', text.slice(0, 400));
    throw new Error(`JSON parse error (${currency}): ${e.message}`);
  }
}

// ── write data.js (raiz) ───────────────────────────────────────────────────
function writeDataJs(data) {
  const meses     = data.meses || {};
  const dateData  = {};
  Object.keys(data).filter(k => k !== 'meses').sort().forEach(k => dateData[k] = data[k]);
  const sorted = Object.keys(dateData);
  const latest = sorted[sorted.length - 1];
  const last7  = sorted.slice(-7);

  const js = `// AUTO-GENERATED by scripts/extract.js — DO NOT EDIT MANUALLY
// Updated: ${new Date().toISOString()}
const TRADING_DATA = ${JSON.stringify(dateData, null, 2)};
const DATA_DATES   = ${JSON.stringify(last7)};
const LATEST_DATE  = "${latest}";
const MESES_DATA   = ${JSON.stringify(meses, null, 2)};
`;
  fs.writeFileSync(DATA_JS, js);
  console.log(`Gerado → data.js  (${sorted.length} dias, ${Object.keys(meses).length} meses, último: ${latest})`);
}

// ── main ───────────────────────────────────────────────────────────────────
async function run() {
  // Backup antes de qualquer escrita
  makeBackup();

  // Carrega dados existentes (estrutura flat)
  let data = {};
  if (fs.existsSync(DATA_FILE)) {
    data = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
    console.log(`Dados carregados: ${Object.keys(data).length} dias`);
  }

  // Dia actual — preserva eventos manuais já existentes
  const existing = data[date] || {};
  const day = {
    date,
    eventos:  existing.eventos || [],
    eur:      existing.eur     || { lucro: 0, positions: [] },
    usd:      existing.usd     || { lucro: 0, positions: [] },
  };

  // Extrai EUR
  if (eurPath) {
    console.log(`\nA extrair EUR de: ${eurPath}`);
    const result = await extractPositions(eurPath, 'EUR');
    day.eur = {
      lucro:     result.lucro     ?? 0,
      positions: result.positions ?? [],
    };
    console.log(`  → ${day.eur.positions.length} posições EUR | lucro: ${day.eur.lucro}`);
  }

  // Extrai USD
  if (usdPath) {
    console.log(`\nA extrair USD de: ${usdPath}`);
    const result = await extractPositions(usdPath, 'USD');
    day.usd = {
      lucro:     result.lucro     ?? 0,
      positions: result.positions ?? [],
    };
    console.log(`  → ${day.usd.positions.length} posições USD | lucro: ${day.usd.lucro}`);
  }

  // Guarda o dia
  data[date] = day;

  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
  console.log(`\nGravado → data/trading_data.json`);
  console.log(`  EUR: ${day.eur.lucro} | USD: ${day.usd.lucro} | Total: ${Math.round((day.eur.lucro + day.usd.lucro) * 100) / 100}`);

  writeDataJs(data);
}

run().catch(e => { console.error('\nExtract failed:', e.message); process.exit(1); });
