#!/usr/bin/env node
// ═══════════════════════════════════════════════════════════════
// NAV UNITIZADO (quotas) — padrão de fundo. node scripts/nav.mjs
// Dia 0: NAV=100, quotas=saldo/100. Aporte compra quotas ao NAV do dia
// (NAV_pre = (saldo_fim − fluxo)/quotas_antigas); levantamento vende.
// Retorno oficial = variação do NAV (TWR — imune a aportes/levantamentos).
// Escreve d.nav em trading_data.json. Fluxos = fund_metrics (fonte única).
// ═══════════════════════════════════════════════════════════════
import fs from 'fs';
const F = new URL('../data/trading_data.json', import.meta.url);
const d = JSON.parse(fs.readFileSync(F, 'utf8'));
const days = Object.keys(d).filter(k => /^\d{4}-\d{2}-\d{2}$/.test(k)).sort();
const fm = d.fund_metrics;

const flows = { eur: {}, usd: {} };
for (const t of (fm.eur.transferencias || [])) flows.eur[t.data] = (flows.eur[t.data] || 0) + t.valor;
for (const a of (fm.usd.aportes || []))       flows.usd[a.data] = (flows.usd[a.data] || 0) + a.valor;

const nav = { gerado: new Date().toISOString().slice(0, 10), metodo: 'unitizacao (TWR)', inicio_serie: '2026-05-26 (primeiro dia com saldo diario)', eur: [], usd: [], twr_mensal: {} };
for (const acc of ['eur', 'usd']) {
  let units = null, out = [];
  for (const k of days) {
    const s = d[k] && d[k][acc] ? d[k][acc].saldo : null;
    if (s == null) continue;
    const fl = flows[acc][k] || 0;
    if (units == null) { units = (s - fl) > 0 ? (s - fl) / 100 : s / 100; if (fl) units += fl / (s / ((s - fl) / 100 > 0 ? (s - fl) / ((s - fl) / 100) : 100)); }
    else if (fl) { const navPre = (s - fl) / units; if (navPre > 0) units += fl / navPre; }
    out.push([k, Math.round(s / units * 100) / 100]);
  }
  nav[acc] = out;
  // TWR mensal
  const byM = {};
  for (const [k, v] of out) { const m = k.slice(0, 7); (byM[m] = byM[m] || []).push(v); }
  let prevEnd = null;
  for (const m of Object.keys(byM).sort()) {
    const start = prevEnd != null ? prevEnd : byM[m][0];
    const end = byM[m][byM[m].length - 1];
    nav.twr_mensal[m] = nav.twr_mensal[m] || {};
    nav.twr_mensal[m][acc] = Math.round((end / start - 1) * 1000) / 10;
    prevEnd = end;
  }
}
d.nav = nav;
fs.writeFileSync(F, JSON.stringify(d, null, 2));
const le = nav.eur[nav.eur.length - 1], lu = nav.usd[nav.usd.length - 1];
console.log(`NAV EUR: ${le[1]} (${le[0]}) — desde 26/05 ${(le[1] - 100).toFixed(1)}%`);
console.log(`NAV USD: ${lu[1]} (${lu[0]}) — desde 26/05 ${(lu[1] - 100).toFixed(1)}%`);
console.log('TWR mensal:', JSON.stringify(nav.twr_mensal));
