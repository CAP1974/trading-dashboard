import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 89.60,
        'caixa': 0.12,
        'lucro': 0.15,
        'positions': [
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':307.30,'lucro':0.24, 'pct':1.00, 'trust':'v','valor':24.28,'delta':None},
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':442.00,'lucro':0.24, 'pct':0.55, 'trust':'v','valor':44.20,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':22.550,'lucro':-0.33,'pct':-1.55,'trust':'r','valor':21.00,'delta':None}
        ]
    },
    'usd': {
        'saldo': 263.37,
        'caixa': 0.36,
        'lucro': -1.99,
        'positions': [
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':384.33, 'lucro':6.44, 'pct':4.61, 'trust':'v','valor':146.04,'delta':None},
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':64.46,  'lucro':2.13, 'pct':3.42, 'trust':'v','valor':64.46,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':495.01, 'lucro':-0.09,'pct':-0.60,'trust':'r','valor':14.85,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':218.00, 'lucro':-3.97,'pct':-20.64,'trust':'r','valor':15.26,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':139.96, 'lucro':-6.50,'pct':-22.49,'trust':'r','valor':22.40,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Schneider +1.00%, Allianz +0.55%, BAE -1.55%. USD: Palo Alto +4.61%, Bank of America +3.42%, mas Cerebras -20.64% e SpaceX -22.49% ainda pesam.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-14'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-14 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 0.12 | USD 0.36)')
print('EUR equity: -0.40 (-5.7% meta) | USD equity: -2.82 (-11.3% meta)')
print('AUM ~332EUR | 92 dias activos')
