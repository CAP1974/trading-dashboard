import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.30,
        'caixa': 1.45,
        'lucro': -0.15,
        'positions': [
            {'name':'Allianz',   'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':438.90,'lucro':-0.07,'pct':-0.16,'trust':'r','valor':43.89,'delta':None},
            {'name':'Schneider', 'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':303.30,'lucro':-0.08,'pct':-0.33,'trust':'r','valor':23.96,'delta':None}
        ]
    },
    'usd': {
        'saldo': 263.68,
        'caixa': 0.36,
        'lucro': -1.68,
        'positions': [
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':384.15, 'lucro':6.39, 'pct':4.58, 'trust':'v','valor':145.99,'delta':None},
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':63.87,  'lucro':1.54, 'pct':2.47, 'trust':'v','valor':63.87,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':506.04, 'lucro':0.24, 'pct':1.61, 'trust':'v','valor':15.18,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':230.00, 'lucro':-3.13,'pct':-16.28,'trust':'r','valor':16.10,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':138.58, 'lucro':-6.72,'pct':-23.25,'trust':'r','valor':22.18,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Allianz e Schneider ambas ligeiramente negativas. USD: Palo Alto forte +4.58%, Bank of America +2.47% e Microsoft +1.61%, mas Cerebras -16.28% e SpaceX -23.25% ainda pesam.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-10'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-10 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 1.45 | USD 0.36)')
print('EUR equity: -0.70 (-10.0% meta) | USD equity: -2.51 (-10.0% meta)')
print('AUM ~314EUR | 88 dias activos')
