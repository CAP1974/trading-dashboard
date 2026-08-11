import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.18,
        'caixa': 1.45,
        'lucro': -0.27,
        'positions': [
            {'name':'Schneider', 'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':305.20,'lucro':0.07, 'pct':0.29, 'trust':'v','valor':24.11,'delta':None},
            {'name':'Allianz',   'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':436.20,'lucro':-0.34,'pct':-0.77,'trust':'r','valor':43.62,'delta':None}
        ]
    },
    'usd': {
        'saldo': 263.12,
        'caixa': 0.36,
        'lucro': -2.24,
        'positions': [
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':383.88, 'lucro':6.29, 'pct':4.51, 'trust':'v','valor':145.89,'delta':None},
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':63.98,  'lucro':1.65, 'pct':2.65, 'trust':'v','valor':63.98,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':503.37, 'lucro':0.16, 'pct':1.07, 'trust':'v','valor':15.10,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':235.00, 'lucro':-2.78,'pct':-14.46,'trust':'r','valor':16.45,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':133.39, 'lucro':-7.56,'pct':-26.16,'trust':'r','valor':21.34,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Schneider +0.29%, Allianz -0.77%. USD: Palo Alto, Bank of America e Microsoft positivos, mas Cerebras -14.46% e SpaceX -26.16% ainda pesam.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-11'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-11 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 1.45 | USD 0.36)')
print('EUR equity: -0.82 (-11.7% meta) | USD equity: -3.07 (-12.3% meta)')
print('AUM ~313EUR | 89 dias activos')
