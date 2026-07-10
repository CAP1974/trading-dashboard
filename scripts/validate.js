#!/usr/bin/env node
'use strict';
// ═══════════════════════════════════════════════════════════════
// VALIDADOR DE DADOS — correr SEMPRE depois de escrever trading_data.json
// e ANTES de regenerar/commitar.  node scripts/validate.js  (exit 1 = abortar)
// Regras (auditoria Fable 2026-07-10 — teria apanhado os bugs 2025-04 e 15-19/06):
//  R1 chaves/datas validas e ano >= 2026
//  R2 saldo = caixa + Σposicoes (±0.05) por conta
//  R3 variacao diaria combinada > 8% exige evento aporte/deposito/transfer no dia
//  R4 posicoes: valor ≈ vol×atual (±1.5%), atual > 0, pct em faixa sana
//  R5 fund_metrics: capital_ajustado = capital_inicial + Σaportes
//  R6 (aviso) realizado mensal ≈ Σ lucros das posicoes_fechadas do mes
// ═══════════════════════════════════════════════════════════════
const fs = require('fs'); const path = require('path');
const d = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'data/trading_data.json'), 'utf8'));
let errs = [], warns = [];
const days = Object.keys(d).filter(k => /^\d{4}-\d{2}-\d{2}$/.test(k)).sort();

// R1
for (const k of days) {
  if (parseInt(k.slice(0, 4)) < 2026) errs.push(`R1 ano invalido: ${k}`);
  if (d[k].date && d[k].date !== k) errs.push(`R1 campo date (${d[k].date}) != chave ${k}`);
}
// R2 + R4
for (const k of days) for (const acc of ['eur', 'usd']) {
  const a = d[k][acc]; if (!a || a.saldo == null || a.caixa == null || !Array.isArray(a.positions) || !a.positions.length) continue;
  const calc = a.caixa + a.positions.reduce((s, p) => s + (p.valor || 0), 0);
  if (Math.abs(a.saldo - calc) > 0.05) errs.push(`R2 ${k} ${acc}: saldo ${a.saldo} != caixa+pos ${calc.toFixed(2)}`);
  for (const p of a.positions) {
    if (!p.vol || !p.valor) continue;
    if (!p.atual) { errs.push(`R4 ${k} ${acc} ${p.name}: atual em falta/0`); continue; }
    if (Math.abs(p.vol * p.atual - p.valor) / p.valor > 0.015) errs.push(`R4 ${k} ${acc} ${p.name}: valor ${p.valor} != vol×atual ${(p.vol * p.atual).toFixed(2)}`);
    if (p.pct != null && (p.pct < -90 || p.pct > 300)) errs.push(`R4 ${k} ${acc} ${p.name}: pct suspeito ${p.pct}`);
  }
}
// R3
let prev = null;
for (const k of days) {
  const e = d[k].eur && d[k].eur.saldo, u = d[k].usd && d[k].usd.saldo;
  if (e == null || u == null) { continue; }
  const v = e + u;
  if (prev) {
    const ch = (v / prev.v - 1) * 100;
    if (Math.abs(ch) > 8) {
      const evs = (d[k].eventos || []).map(x => ((x.tipo || '') + ' ' + (x.nota || '')).toLowerCase()).join(' ');
      if (!/aporte|deposito|depósito|transfer/.test(evs)) errs.push(`R3 ${prev.k}->${k}: variacao ${ch.toFixed(1)}% sem aporte/deposito registado`);
    }
  }
  prev = { k, v };
}
// R5
const fm = d.fund_metrics || {};
if (fm.usd) {
  const cap = (fm.usd.capital_inicial || 0) + (fm.usd.aportes || []).reduce((s, a) => s + a.valor, 0);
  if (Math.abs(cap - (fm.usd.capital_ajustado || 0)) > 0.02) errs.push(`R5 usd capital_ajustado ${fm.usd.capital_ajustado} != ${cap.toFixed(2)}`);
}
// R6 (aviso)
const porMes = {};
for (const k of days) for (const p of (d[k].posicoes_fechadas || [])) { const m = k.slice(0, 7); porMes[m] = (porMes[m] || 0) + (p.lucro || 0); }
for (const [m, v] of Object.entries(d.meses || {})) {
  if (v.realizado_eur == null && v.realizado_usd == null) continue;
  const led = (v.realizado_eur || 0) + (v.realizado_usd || 0);
  if (porMes[m] != null && Math.abs(led - porMes[m]) > 0.8) warns.push(`R6 ${m}: ledger ${led.toFixed(2)} vs Σfechadas ${porMes[m].toFixed(2)}`);
}

warns.forEach(w => console.log('⚠  ' + w));
if (errs.length) { errs.forEach(e => console.error('✗ ' + e)); console.error(`\n✗ ${errs.length} erro(s) — NAO commitar. Corrigir primeiro.`); process.exit(1); }
console.log(`✓ validacao OK (${days.length} dias, ${warns.length} avisos)`);
