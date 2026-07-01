import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.15,
        'caixa': 1.83,
        'lucro': 0.07,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':414.20,'lucro':0.38, 'pct':0.98, 'trust':'v','valor':39.35,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.970,'lucro':-0.31,'pct':-1.06,'trust':'r','valor':28.97,'delta':None}
        ]
    },
    'usd': {
        'saldo': 285.68,
        'caixa': 0.14,
        'lucro': -0.42,
        'positions': [
            {'name':'Veracyte',            'mkt':'USD','vol':1.7, 'abertura':53.31, 'atual':0.00,'lucro':10.65,'pct':11.75, 'trust':'v','valor':101.27,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':2.11,'pct':3.05,  'trust':'v','valor':71.33,'delta':None},
            {'name':'Axos Financial',      'mkt':'USD','vol':0.07,'abertura':99.10, 'atual':0.00,'lucro':-0.02,'pct':-0.29,'trust':'r','valor':6.92, 'delta':None},
            {'name':'Apple Hospitality',   'mkt':'USD','vol':3.0, 'abertura':16.90, 'atual':0.00,'lucro':-1.23,'pct':-2.43,'trust':'r','valor':49.47,'delta':None},
            {'name':'Caterpillar',         'mkt':'USD','vol':0.03,'abertura':1048.01,'atual':0.00,'lucro':-1.69,'pct':-5.38,'trust':'r','valor':29.75,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-3.89,'pct':-26.04,'trust':'r','valor':11.05,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-6.35,'pct':-28.73,'trust':'r','valor':15.75,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'AX','ativo':'Axos Financial','mkt':'USD',
         'nota':'ENTRADA AX 0.07 @ 99.10 -- Clean Trend'},
        {'tipo':'diario','nota':'Primeiro dia de Julho 2026. Entrada AX (Axos Financial) Clean Trend. Sem saidas hoje.'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-01'] = entry

# Realizado Julho: sem saidas hoje, mantem 0
# REAL_EUR_JUL: 0 | REAL_USD_JUL: 0

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-01 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('AX entrada: 0.07@99.10 = 6.94$ | caixa: 7.08-6.94=0.14 checkOK')
print('REAL_EUR_JUL: 0.00 | REAL_USD_JUL: 0.00')
print('EUR equity: +0.07 (1.0% meta) | USD equity: -0.42 (-1.4% meta)')
print('AUM ~335EUR | 60 dias activos')
