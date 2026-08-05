import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.96,
        'caixa': 1.09,
        'lucro': -0.04,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':57.55, 'lucro':0.55, 'pct':2.85, 'trust':'v','valor':19.84,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':947.20,'lucro':-0.59,'pct':-1.19,'trust':'r','valor':49.03,'delta':None}
        ]
    },
    'usd': {
        'saldo': 247.12,
        'caixa': 50.52,
        'lucro': -18.24,
        'positions': [
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':63.22, 'lucro':0.89, 'pct':1.43, 'trust':'v','valor':63.22,'delta':None},
            {'name':'Palo Alto',           'mkt':'USD','vol':0.28, 'abertura':372.77,'atual':361.34, 'lucro':-3.21,'pct':-3.08,'trust':'r','valor':101.17,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':212.70, 'lucro':-4.34,'pct':-22.57,'trust':'r','valor':14.89,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':108.26, 'lucro':-11.58,'pct':-40.07,'trust':'r','valor':17.32,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'ENTRADA PANW 0.2 @ 376.18 -- Clean Trend (tranche 1/3)'},
        {'tipo':'entrada','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'ENTRADA PANW 0.04 @ 364.48 -- Clean Trend (tranche 2/3)'},
        {'tipo':'entrada','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'ENTRADA PANW 0.04 @ 363.98 -- Clean Trend (tranche 3/3) -- vol total 0.28 preco medio 372.77'},
        {'tipo':'diario','nota':'Entrada Palo Alto em 3 tranches (Clean Trend). Cerebras -22.57% e SpaceX -40.07% continuam a pesar.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-05'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: 0.00 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-05 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('PANW entrada 3 tranches: vol total 0.28 preco medio 372.77')
print('caixa: 154.91-104.37=50.54 vs 50.52 informado (diferenca minima)')
print('REAL_EUR_AGO: +0.00 (inalterado) | REAL_USD_AGO: -0.83 (inalterado)')
print('EUR equity: -0.04 (-0.6% meta) | USD equity: -19.07 (-76.2% meta)')
print('AUM ~345EUR | 85 dias activos')
