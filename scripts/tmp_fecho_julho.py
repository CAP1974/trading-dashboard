import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

jul = d['meses']['2026-07']
ultimo_dia = d['2026-07-31']

# saldo do dia ja e capital total (caixa + Sigma valor posicoes) -- confirmado empiricamente
jul['saldo_fim_eur'] = ultimo_dia['eur']['saldo']
jul['saldo_fim_usd'] = ultimo_dia['usd']['saldo']
jul['flutuante_fim_eur'] = ultimo_dia['eur']['lucro']
jul['flutuante_fim_usd'] = ultimo_dia['usd']['lucro']

equity_eur = round(jul['realizado_eur'] + jul['flutuante_fim_eur'], 2)
equity_usd = round(jul['realizado_usd'] + jul['flutuante_fim_usd'], 2)
jul['equity_eur'] = equity_eur
jul['equity_usd'] = equity_usd
jul['retorno_meta_eur_pct'] = round(equity_eur / jul['meta_eur'] * 100, 1)
jul['retorno_meta_usd_pct'] = round(equity_usd / jul['meta_usd'] * 100, 1)

jul['trades_total'] = 26
jul['trades_eur'] = 2
jul['trades_usd'] = 24
jul['win_rate_pct'] = 23.1
jul['profit_factor'] = 0.27
jul['status'] = 'FECHADO'
jul['fim'] = '2026-07-31'

# Abertura de Agosto -- juro composto: base = saldo_fim do mes anterior
base_eur_ago = jul['saldo_fim_eur']
base_usd_ago = jul['saldo_fim_usd']

d['meses']['2026-08'] = {
    'inicio': '2026-08-01',
    'status': 'EM CURSO',
    'base_eur': base_eur_ago,
    'base_usd': base_usd_ago,
    'base_ajustada_eur': base_eur_ago,
    'base_ajustada_usd': base_usd_ago,
    'meta_eur': round(base_eur_ago * 0.10, 3),
    'meta_usd': round(base_usd_ago * 0.10, 3),
    'ajustes_eur': 0,
    'ajustes_usd': 0,
    'realizado_eur': 0,
    'realizado_usd': 0,
    'flutuante_fim_eur': None,
    'flutuante_fim_usd': None,
    'saldo_fim_eur': None,
    'saldo_fim_usd': None
}

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('=== FECHO JULHO 2026 ===')
print('saldo_fim_eur:', jul['saldo_fim_eur'], '| saldo_fim_usd:', jul['saldo_fim_usd'])
print('flutuante_fim_eur:', jul['flutuante_fim_eur'], '| flutuante_fim_usd:', jul['flutuante_fim_usd'])
print('realizado_eur:', jul['realizado_eur'], '| realizado_usd:', jul['realizado_usd'])
print('equity_eur:', equity_eur, '(', jul['retorno_meta_eur_pct'], '% meta)')
print('equity_usd:', equity_usd, '(', jul['retorno_meta_usd_pct'], '% meta)')
print('trades_total:', jul['trades_total'], '| win_rate:', jul['win_rate_pct'], '% | profit_factor:', jul['profit_factor'])
print()
print('=== ABERTURA AGOSTO 2026 (juro composto) ===')
print('base_eur:', base_eur_ago, '| base_usd:', base_usd_ago)
print('meta_eur:', d['meses']['2026-08']['meta_eur'], '| meta_usd:', d['meses']['2026-08']['meta_usd'])
