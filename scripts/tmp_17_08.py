import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 89.23,
        'caixa': 0.12,
        'lucro': -0.22,
        'positions': [
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':308.55,'lucro':0.33, 'pct':1.37, 'trust':'v','valor':24.37,'delta':None},
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':438.90,'lucro':-0.07,'pct':-0.16,'trust':'r','valor':43.89,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':22.400,'lucro':-0.48,'pct':-2.25,'trust':'r','valor':20.85,'delta':None}
        ]
    },
    'usd': {
        'saldo': 262.44,
        'caixa': 0.36,
        'lucro': -2.92,
        'positions': [
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':63.88,  'lucro':1.55, 'pct':2.49, 'trust':'v','valor':63.88,'delta':None},
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':375.71, 'lucro':3.17, 'pct':2.27, 'trust':'v','valor':142.77,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':480.35, 'lucro':-0.53,'pct':-3.55,'trust':'r','valor':14.41,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':251.82, 'lucro':-1.60,'pct':-8.32,'trust':'r','valor':17.63,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':146.18, 'lucro':-5.51,'pct':-19.07,'trust':'r','valor':23.39,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Schneider +1.37%, Allianz -0.16%, BAE -2.25%. USD: Bank of America +2.49%, Palo Alto +2.27%, mas Microsoft -3.55%, Cerebras -8.32% e SpaceX -19.07% negativos.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-17'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-17 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual ao dia anterior (EUR 0.12 | USD 0.36)')
print('EUR equity: -0.77 (-11.0% meta) | USD equity: -3.75 (-15.0% meta)')
print('AUM ~331EUR | 93 dias activos')
