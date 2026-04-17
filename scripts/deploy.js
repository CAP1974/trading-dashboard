#!/usr/bin/env node
/**
 * deploy.js — valida trading_data.json, depois git add/commit/push
 */

'use strict';

const { execSync } = require('child_process');
const fs   = require('fs');
const path = require('path');
const ROOT = path.join(__dirname, '..');

function run(cmd) {
  execSync(cmd, { stdio: 'inherit', cwd: ROOT });
}

// ── VALIDAÇÃO ──────────────────────────────────────────────────────────────
const DATA_FILE = path.join(ROOT, 'data', 'trading_data.json');

function fail(msg) {
  console.error(`\n❌ VALIDAÇÃO FALHOU: ${msg}`);
  console.error('   Usa: node scripts/restore.js --list  para recuperar backup\n');
  process.exit(1);
}

function validate() {
  if (!fs.existsSync(DATA_FILE)) fail('trading_data.json não encontrado');

  // 1. JSON válido
  let data;
  try { data = JSON.parse(fs.readFileSync(DATA_FILE, 'utf8')); }
  catch (e) { fail(`JSON inválido — ${e.message}`); }

  const days = Object.keys(data).sort();
  if (!days.length) fail('Nenhum dia encontrado no JSON');

  // 2. Nº de dias >= commit anterior
  let prevCount = 0;
  try {
    const prevRaw = execSync('git show HEAD:data/trading_data.json 2>/dev/null', { cwd: ROOT }).toString();
    prevCount = Object.keys(JSON.parse(prevRaw)).length;
  } catch (_) { /* ficheiro novo ou primeiro commit — ok */ }
  if (days.length < prevCount) {
    fail(`Regressão de dados: ${days.length} dias agora vs ${prevCount} no commit anterior`);
  }

  // 3+4. Estrutura de cada dia e posições
  const REQ_POS = ['name','mkt','pct','lucro','vol','valor','atual','abertura','trust'];
  let totalPos = 0;
  for (const d of days) {
    const day = data[d];
    if (!day.date)                      fail(`${d}: campo 'date' em falta`);
    for (const side of ['eur','usd']) {
      const s = day[side];
      if (!s)                           fail(`${d}: secção '${side}' em falta`);
      if (typeof s.lucro !== 'number')  fail(`${d}.${side}: 'lucro' deve ser número`);
      if (!Array.isArray(s.positions))  fail(`${d}.${side}: 'positions' deve ser array`);
      for (const [i, p] of s.positions.entries()) {
        for (const f of REQ_POS) {
          if (p[f] === undefined) fail(`${d}.${side}.positions[${i}] (${p.name||'?'}): campo '${f}' em falta`);
        }
        totalPos++;
      }
    }
  }

  console.log(`\n✅ Validação OK — ${days.length} dias, ${totalPos} posições\n`);
  return { days, totalPos };
}

// Copia dashboard/data.js para raiz (se existir)
const src = path.join(ROOT, 'dashboard', 'data.js');
const dst = path.join(ROOT, 'data.js');
if (fs.existsSync(src)) {
  fs.copyFileSync(src, dst);
  console.log('Copiado dashboard/data.js → ./data.js');
}

// Validar antes de qualquer git
validate();

try {
  run('git add .');
  const status = execSync('git status --porcelain', { cwd: ROOT }).toString().trim();
  if (!status) {
    console.log('Nothing to commit — working tree clean.');
  } else {
    run('git commit -m "update data"');
    console.log('Committed.');
  }
  run('git push origin main');
  console.log('Pushed to origin/main.');
} catch (e) {
  console.error('Deploy failed:', e.message);
  process.exit(1);
}
