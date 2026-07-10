import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

jun = d['meses']['2026-06']
ultimo_dia = d['2026-06-30']

# Fecho de Junho -- saldo_fim = saldo do ultimo dia (posicoes + caixa), flutuante_fim = lucro flutuante do ultimo dia
jun['saldo_fim_eur'] = ultimo_dia['eur']['saldo']
jun['saldo_fim_usd'] = ultimo_dia['usd']['saldo']
jun['flutuante_fim_eur'] = ultimo_dia['eur']['lucro']
jun['flutuante_fim_usd'] = ultimo_dia['usd']['lucro']

equity_eur = round(jun['realizado_eur'] + jun['flutuante_fim_eur'], 2)
equity_usd = round(jun['realizado_usd'] + jun['flutuante_fim_usd'], 2)
jun['equity_eur'] = equity_eur
jun['equity_usd'] = equity_usd
jun['retorno_meta_eur_pct'] = round(equity_eur / jun['meta_eur'] * 100, 1)
jun['retorno_meta_usd_pct'] = round(equity_usd / jun['meta_usd'] * 100, 1)

jun['trades_total'] = 25
jun['trades_eur'] = 5
jun['trades_usd'] = 20
jun['win_rate_pct'] = 64.0
jun['profit_factor'] = 3.16
jun['status'] = 'FECHADO'
jun['fim'] = '2026-06-30'

# Abertura de Julho -- juro composto: base = saldo_fim do mes anterior
base_eur_jul = jun['saldo_fim_eur']
base_usd_jul = jun['saldo_fim_usd']

d['meses']['2026-07'] = {
    'inicio': '2026-07-01',
    'status': 'EM CURSO',
    'base_eur': base_eur_jul,
    'base_usd': base_usd_jul,
    'base_ajustada_eur': base_eur_jul,
    'base_ajustada_usd': base_usd_jul,
    'meta_eur': round(base_eur_jul * 0.10, 3),
    'meta_usd': round(base_usd_jul * 0.10, 3),
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

print('=== FECHO JUNHO 2026 ===')
print('saldo_fim_eur:', jun['saldo_fim_eur'], '| saldo_fim_usd:', jun['saldo_fim_usd'])
print('flutuante_fim_eur:', jun['flutuante_fim_eur'], '| flutuante_fim_usd:', jun['flutuante_fim_usd'])
print('realizado_eur:', jun['realizado_eur'], '| realizado_usd:', jun['realizado_usd'])
print('equity_eur:', equity_eur, '(', jun['retorno_meta_eur_pct'], '% meta)')
print('equity_usd:', equity_usd, '(', jun['retorno_meta_usd_pct'], '% meta)')
print('trades_total:', jun['trades_total'], '| win_rate:', jun['win_rate_pct'], '% | profit_factor:', jun['profit_factor'])
print()
print('=== ABERTURA JULHO 2026 (juro composto) ===')
print('base_eur:', base_eur_jul, '| base_usd:', base_usd_jul)
print('meta_eur:', d['meses']['2026-07']['meta_eur'], '| meta_usd:', d['meses']['2026-07']['meta_usd'])
