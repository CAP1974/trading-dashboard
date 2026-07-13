// Patch pontual do dia 2026-07-13 (reconciliação manual):
//  (a) entrada em falta: Swiss Life (EUR) — evento não detetado porque o "ontem" não carregou no fecho.
//  (b) caixa EUR corrigida para 0.39 (a leitura tinha 2.45; saldo estava sobre-lido).
// Idempotente: se já aplicado, não repete. Faz backup antes de escrever.
// Correr: node scripts/patch_2026-07-13.js   (o CORRIGIR_DIA13.bat faz isto + regen + nav + validate + publica)
const fs = require('fs');
const path = require('path');
const ROOT = path.join(__dirname, '..');
const FILE = path.join(ROOT, 'data', 'trading_data.json');
const DATE = '2026-07-13';

const d = JSON.parse(fs.readFileSync(FILE, 'utf8'));
const day = d[DATE];
if (!day) { console.error('Dia ' + DATE + ' não existe — abortar.'); process.exit(1); }

// backup
const bkp = path.join(ROOT, 'data', 'backups', 'trading_data_pre_patch_' + DATE + '.json');
fs.mkdirSync(path.dirname(bkp), { recursive: true });
fs.writeFileSync(bkp, JSON.stringify(d, null, 2));

let mudou = false;
const eur = day.eur;
const somaPos = (eur.positions || []).reduce((s, p) => s + (p.valor || 0), 0);

// (b) caixa + saldo (mantém as posições; saldo = caixa + Σposições)
const CAIXA = 0.39;
const novoSaldo = Math.round((CAIXA + somaPos) * 100) / 100;
if (eur.caixa !== CAIXA || eur.saldo !== novoSaldo) {
  console.log(`EUR caixa ${eur.caixa} → ${CAIXA} · saldo ${eur.saldo} → ${novoSaldo} (Σpos ${Math.round(somaPos * 100) / 100})`);
  eur.caixa = CAIXA;
  eur.saldo = novoSaldo;
  mudou = true;
}

// (a) evento de entrada Swiss Life (se ainda não existir)
day.eventos = day.eventos || [];
const jaTem = day.eventos.some(e => e.tipo === 'entrada' && /swiss/i.test(e.ativo || e.nota || ''));
const sl = (eur.positions || []).find(p => /swiss/i.test(p.name || ''));
if (!jaTem && sl) {
  day.eventos.push({ tipo: 'entrada', ativo: sl.name, mkt: 'EUR', nota: `ENTRADA ${sl.name} ${sl.vol} @ ${sl.abertura} (reconciliação — não detetada no fecho)` });
  console.log(`Evento de entrada adicionado: ${sl.name} ${sl.vol} @ ${sl.abertura}`);
  mudou = true;
}

// (c) backfill dos campos em falta nas posições fechadas (o fecho-dia não os gravava → "undefined"/sem dias/partia gráficos)
(day.posicoes_fechadas || []).forEach((pf) => {
  if (!pf.data_saida) { pf.data_saida = DATE; mudou = true; }
  // PST (Poste Italiane): entrada 2026-06-17 (histórico do dashboard)
  if (/^PST$/i.test(pf.ticker || '')) {
    if (!pf.nome) { pf.nome = 'Poste Italiane'; mudou = true; }
    if (!pf.data_entrada) { pf.data_entrada = '2026-06-17'; mudou = true; }
    if (pf.dias_holding == null) { pf.dias_holding = Math.round((new Date(pf.data_saida) - new Date('2026-06-17')) / 86400000); mudou = true; }
  }
  // qualquer outra sem nome → usa o ticker (evita "undefined")
  if (!pf.nome) { pf.nome = pf.ticker; mudou = true; }
  if (mudou) console.log('backfill ' + pf.ticker + ': nome=' + pf.nome + ' entrada=' + (pf.data_entrada || '?') + ' dias=' + (pf.dias_holding == null ? '?' : pf.dias_holding));
});

if (!mudou) { console.log('Nada a alterar (já aplicado).'); process.exit(0); }
fs.writeFileSync(FILE, JSON.stringify(d, null, 2));
console.log('✓ Patch aplicado. Backup em ' + path.relative(ROOT, bkp));
