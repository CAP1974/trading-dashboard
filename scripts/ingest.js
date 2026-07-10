#!/usr/bin/env node
'use strict';
// ═══════════════════════════════════════════════════════════════
// INGEST — aplica o fecho_DATA.json (gerado pela página Fecho do Dia
// da app CTM PRO) ao trading_data.json. ZERO tokens, determinístico.
//   node scripts/ingest.js               → procura watched/fecho_*.json
//   node scripts/ingest.js --force      → substitui dia já existente
// Fluxo: backup → merge dia → saídas→posicoes_fechadas + realizado mensal
// → depósitos→fund_metrics → validate → nav → _regen → move p/ processados.
// NUNCA substitui um dia existente sem --force. Commit/push ficam para ti.
// ═══════════════════════════════════════════════════════════════
const fs = require('fs'); const path = require('path'); const { execSync } = require('child_process');
const ROOT = path.join(__dirname, '..');
const DATA = path.join(ROOT, 'data/trading_data.json');
const force = process.argv.includes('--force');

// [sem-terminal] se o fecho estiver nos Downloads (a página faz download para lá), move-o para watched/
try {
  const dl = path.join(require('os').homedir(), 'Downloads');
  const dlf = fs.readdirSync(dl).filter(f => /^fecho_\d{4}-\d{2}-\d{2}(\s*\(\d+\))?\.json$/.test(f))
    .map(f => ({ f, t: fs.statSync(path.join(dl, f)).mtimeMs })).sort((a, b) => b.t - a.t);
  if (dlf.length) {
    const src = path.join(dl, dlf[0].f);
    const clean = dlf[0].f.replace(/\s*\(\d+\)/, '');
    fs.copyFileSync(src, path.join(ROOT, 'watched', clean));
    fs.unlinkSync(src);
    console.log('Fecho encontrado nos Downloads → movido para watched/: ' + clean);
  }
} catch (e) { /* Downloads inacessível — segue com watched/ */ }

const files = fs.readdirSync(path.join(ROOT, 'watched')).filter(f => /^fecho_\d{4}-\d{2}-\d{2}\.json$/.test(f)).sort();
if (!files.length) { console.error('Nenhum fecho_*.json encontrado (nem em watched/ nem nos Downloads).'); process.exit(1); }
const fname = files[files.length - 1];
const F = JSON.parse(fs.readFileSync(path.join(ROOT, 'watched', fname), 'utf8'));
const date = F.date; const mes = date.slice(0, 7);
console.log('A ingerir', fname, '→ dia', date);

const d = JSON.parse(fs.readFileSync(DATA, 'utf8'));
if (d[date] && !force) { console.error(`Dia ${date} já existe — usa --force para substituir (NUNCA por engano).`); process.exit(1); }

// backup
const bdir = path.join(ROOT, 'data/backups');
fs.mkdirSync(bdir, { recursive: true });
fs.copyFileSync(DATA, path.join(bdir, `trading_data_pre_ingest_${date}.json`));

// ── posições no formato do dashboard ──
function conv(pos, mkt) {
  return (pos || []).map(p => ({
    name: p.name, mkt, vol: p.vol, abertura: p.abertura, atual: p.atual,
    lucro: p.lucro, pct: p.pct != null ? p.pct : (p.abertura > 0 ? Math.round((p.atual / p.abertura - 1) * 10000) / 100 : null),
    trust: 'v', valor: p.valor != null ? p.valor : Math.round(p.vol * p.atual * 100) / 100, delta: null,
  }));
}
const day = {
  date,
  eur: { saldo: F.eur.saldo, caixa: F.eur.caixa, lucro: F.eur.lucro, positions: conv(F.eur.positions, 'EUR') },
  usd: { saldo: F.usd.saldo, caixa: F.usd.caixa, lucro: F.usd.lucro, positions: conv(F.usd.positions, 'USD') },
  eventos: [], posicoes_fechadas: [],
};
if (F.fx) day.fx = F.fx;
if (F.diario) day.diario = { nota: F.diario };

// eventos automáticos (entradas/aportes vindos do diff da página)
for (const e of (F.entradas || [])) day.eventos.push({ tipo: 'entrada', ativo: e.name, mkt: e.mkt, nota: `ENTRADA ${e.name} ${e.vol} @ ${e.entrada} (auto-detetada)` });
for (const a of (F.aportes || [])) day.eventos.push({ tipo: 'aporte', ativo: a.name, mkt: a.mkt, nota: `APORTE ${a.name} vol ${a.volAntes}→${a.volDepois} @ ${a.preco} (auto-detetado)` });

// saídas → posicoes_fechadas + realizado mensal (ACUMULAR, nunca substituir)
d.meses = d.meses || {}; d.meses[mes] = d.meses[mes] || {};
for (const s of (F.saidas || [])) {
  if (s.lucro == null) { console.error(`Saída ${s.name} sem lucro exato — abortar.`); process.exit(1); }
  const pctL = (s.entrada > 0 && s.saida > 0) ? Math.round((s.saida / s.entrada - 1) * 10000) / 100 : null;
  day.posicoes_fechadas.push({ ticker: s.name, mkt: s.mkt, lucro: s.lucro, lucro_pct: pctL, entrada: s.entrada, saida: s.saida, vol: s.vol, setup: s.setup || null, nota: 'via fecho-dia' });
  day.eventos.push({ tipo: 'saida', ativo: s.name, mkt: s.mkt, nota: `SAIDA ${s.name} ${s.lucro > 0 ? '+' : ''}${s.lucro} (saida ${s.saida} / entrada ${s.entrada})` });
  const k = s.mkt === 'EUR' ? 'realizado_eur' : 'realizado_usd';
  d.meses[mes][k] = Math.round(((d.meses[mes][k] || 0) + s.lucro) * 100) / 100;
}

// depósitos EXTERNOS → fund_metrics (o NAV lê daqui) + evento
for (const dep of (F.depositos || [])) {
  day.eventos.push({ tipo: 'aporte', mkt: dep.mkt, nota: `DEPOSITO EXTERNO ${dep.valor > 0 ? '+' : ''}${dep.valor} ${dep.mkt} — ${dep.nota || ''}` });
  if (dep.mkt === 'USD') {
    d.fund_metrics.usd.aportes.push({ data: date, valor: dep.valor, nota: dep.nota || 'via fecho-dia' });
    d.fund_metrics.usd.capital_ajustado = Math.round((d.fund_metrics.usd.capital_inicial + d.fund_metrics.usd.aportes.reduce((s, a) => s + a.valor, 0)) * 100) / 100;
  } else {
    d.fund_metrics.eur.transferencias.push({ data: date, valor: dep.valor, nota: dep.nota || 'via fecho-dia' });
    d.fund_metrics.eur.capital_ajustado = Math.round((d.fund_metrics.eur.capital_inicial + d.fund_metrics.eur.transferencias.reduce((s, a) => s + a.valor, 0)) * 100) / 100;
  }
}

d[date] = day;
fs.writeFileSync(DATA, JSON.stringify(d, null, 2));
console.log(`Dia ${date} escrito: ${day.eur.positions.length} pos EUR, ${day.usd.positions.length} pos USD, ${day.posicoes_fechadas.length} saídas, ${(F.depositos || []).length} depósitos.`);

// ── validação + nav + regen (a rede de segurança) ──
try { execSync('node ' + path.join(__dirname, 'validate.js'), { stdio: 'inherit' }); }
catch (e) { console.error('\n✗ VALIDAÇÃO FALHOU — dia escrito mas NÃO commitar. Backup em data/backups/. Corrige e revalida.'); process.exit(1); }
try { execSync('node ' + path.join(__dirname, 'nav.mjs'), { stdio: 'inherit' }); } catch (e) { console.error('nav.mjs falhou:', e.message); }
try { execSync('node ' + path.join(__dirname, '_regen.js'), { stdio: 'inherit' }); } catch (e) { console.error('_regen falhou:', e.message); process.exit(1); }

// arquivar o fecho
const pdir = path.join(ROOT, 'watched/processados', date);
fs.mkdirSync(pdir, { recursive: true });
fs.renameSync(path.join(ROOT, 'watched', fname), path.join(pdir, fname));
console.log(`\n✓ TUDO OK. Rever e commitar: git add -A && git commit -m "diario ${date} (fecho-dia)" && git push`);

// alerta stop duro (informativo)
const viol = [...day.eur.positions, ...day.usd.positions].filter(p => (p.pct || 0) <= -10);
if (viol.length) console.log('⚠ STOP DURO −10% violado: ' + viol.map(p => `${p.name} ${p.pct}%`).join(' · '));
