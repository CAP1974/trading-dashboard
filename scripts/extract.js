#!/usr/bin/env node
/**
 * extract.js — eToro screenshot → Claude Vision → trading_data.json + dashboard/data.js
 *
 * Usage:
 *   node scripts/extract.js --date 2026-04-15 --eur path/to/eur.png --usd path/to/usd.png
 *   node scripts/extract.js --date 2026-04-15 --eur path/to/eur.png
 *   node scripts/extract.js --date 2026-04-15 --usd path/to/usd.png
 *
 * Env:
 *   ANTHROPIC_API_KEY  (required)
 */

'use strict';

const fs        = require('fs');
const path      = require('path');
const Anthropic = require('@anthropic-ai/sdk');

// ── arg parsing ────────────────────────────────────────────────────────────
const args  = process.argv.slice(2);
const get   = flag => { const i = args.indexOf(flag); return i !== -1 ? args[i + 1] : null; };

const date    = get('--date') || new Date().toISOString().slice(0, 10);
const eurPath = get('--eur');
const usdPath = get('--usd');

if (!eurPath && !usdPath) {
  console.error('Usage: node scripts/extract.js --date YYYY-MM-DD [--eur <img>] [--usd <img>]');
  process.exit(1);
}

const DATA_FILE = path.join(__dirname, '..', 'data', 'trading_data.json');
const DATA_JS   = path.join(__dirname, '..', 'dashboard', 'data.js');

const client = new Anthropic();

// ── vision extraction ──────────────────────────────────────────────────────
async function extractPositions(imagePath, currency) {
  const buf       = fs.readFileSync(imagePath);
  const base64    = buf.toString('base64');
  const ext       = path.extname(imagePath).toLowerCase();
  const mediaType = (ext === '.jpg' || ext === '.jpeg') ? 'image/jpeg'
                  : ext === '.webp'                     ? 'image/webp'
                  : ext === '.gif'                      ? 'image/gif'
                  :                                       'image/png';

  const prompt = `This is an eToro trading platform screenshot showing ${currency} positions.

Extract ALL positions visible in the table as a JSON array.
For each row include these exact fields:
{
  "id":         position ID string visible on screen (if not visible use sequential "P001", "P002", ...),
  "asset":      instrument name exactly as shown (e.g. "EUR/USD", "GBP/USD", "USD/JPY"),
  "direction":  "buy" or "sell",
  "amount":     invested amount as a number (no currency symbols),
  "open_rate":  open/entry price as a number,
  "close_rate": close price as a number, or null if position is still open,
  "pnl":        profit/loss as a number (positive = profit, negative = loss),
  "pnl_pct":    P&L percentage as a number (e.g. 4.5 for 4.5%),
  "status":     "open" or "closed",
  "open_time":  time or datetime string exactly as shown,
  "close_time": close time string or null if open
}

Return ONLY a valid JSON array with no explanation, no markdown fences, no extra text.
If no positions are visible return an empty array [].`;

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
    console.error(`  Failed to parse Claude response for ${currency}:`);
    console.error('  Raw:', text.slice(0, 300));
    throw new Error(`JSON parse error for ${currency} positions: ${e.message}`);
  }
}

// ── summarise positions ────────────────────────────────────────────────────
function summarise(positions) {
  const pnl  = positions.reduce((s, p) => s + (p.pnl || 0), 0);
  const pos  = positions.filter(p => (p.pnl || 0) > 0);
  const neg  = positions.filter(p => (p.pnl || 0) < 0);
  return {
    total_pnl: Math.round(pnl * 100) / 100,
    positions: positions.length,
    positive:  pos.length,
    negative:  neg.length,
    best:      pos.length ? Math.max(...pos.map(p => p.pnl)) : 0,
    worst:     neg.length ? Math.min(...neg.map(p => p.pnl)) : 0,
  };
}

// ── generate events from positions ────────────────────────────────────────
function deriveEvents(eurPositions, usdPositions) {
  const events = [];
  const all    = [
    ...eurPositions.map(p => ({ ...p, _ccy: 'EUR' })),
    ...usdPositions.map(p => ({ ...p, _ccy: 'USD' })),
  ];

  for (const p of all) {
    const sym = p._ccy === 'EUR' ? '€' : '$';
    if (p.open_time) {
      events.push({
        time:        p.open_time,
        type:        'open',
        description: `Abriu ${p.asset} ${p.direction === 'buy' ? 'Buy' : 'Sell'} ${sym}${p.amount}${p.status === 'open' ? ' (aberta)' : ''}`,
      });
    }
    if (p.close_time) {
      const sign = p.pnl >= 0 ? '+' : '';
      events.push({
        time:        p.close_time,
        type:        p.pnl >= 0 ? 'close' : 'loss',
        description: `Fechou ${p.asset} ${sign}${sym}${Math.abs(p.pnl).toFixed(2)} (${sign}${p.pnl_pct}%)`,
      });
    }
  }

  return events.sort((a, b) => a.time.localeCompare(b.time));
}

// ── write dashboard/data.js ────────────────────────────────────────────────
function writeDataJs(data) {
  const sorted     = Object.keys(data.days).sort();
  const latest     = sorted[sorted.length - 1];
  const last7      = sorted.slice(-7);

  const js = `// AUTO-GENERATED by scripts/extract.js — DO NOT EDIT MANUALLY
// Updated: ${data.meta.updated}
const TRADING_DATA = ${JSON.stringify(data, null, 2)};
const DATA_DATES   = ${JSON.stringify(last7)};
const LATEST_DATE  = "${latest}";
`;
  fs.writeFileSync(DATA_JS, js);
  console.log(`Generated → dashboard/data.js  (${sorted.length} days, latest: ${latest})`);
}

// ── main ───────────────────────────────────────────────────────────────────
async function run() {
  let data = { meta: { trader: 'Carlos', updated: '' }, days: {} };
  if (fs.existsSync(DATA_FILE)) {
    data = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8'));
    console.log(`Loaded existing data (${Object.keys(data.days).length} days)`);
  }

  const day = data.days[date] || { date, eur: [], usd: [], events: [] };

  if (eurPath) {
    console.log(`\nExtracting EUR positions from: ${eurPath}`);
    day.eur = await extractPositions(eurPath, 'EUR');
    console.log(`  → ${day.eur.length} EUR positions extracted`);
  }

  if (usdPath) {
    console.log(`\nExtracting USD positions from: ${usdPath}`);
    day.usd = await extractPositions(usdPath, 'USD');
    console.log(`  → ${day.usd.length} USD positions extracted`);
  }

  const eurPnl = (day.eur || []).reduce((s, p) => s + (p.pnl || 0), 0);
  const usdPnl = (day.usd || []).reduce((s, p) => s + (p.pnl || 0), 0);

  day.events  = deriveEvents(day.eur || [], day.usd || []);
  day.summary = {
    eur:       summarise(day.eur || []),
    usd:       summarise(day.usd || []),
    total_pnl: Math.round((eurPnl + usdPnl) * 100) / 100,
  };

  data.days[date]  = day;
  data.meta.updated = new Date().toISOString();

  fs.writeFileSync(DATA_FILE, JSON.stringify(data, null, 2));
  console.log(`\nSaved → data/trading_data.json`);
  console.log(`  EUR: ${day.summary.eur.total_pnl >= 0 ? '+' : ''}${day.summary.eur.total_pnl} | USD: ${day.summary.usd.total_pnl >= 0 ? '+' : ''}${day.summary.usd.total_pnl} | Total: ${day.summary.total_pnl >= 0 ? '+' : ''}${day.summary.total_pnl}`);

  writeDataJs(data);
}

run().catch(e => { console.error('\nExtract failed:', e.message); process.exit(1); });
