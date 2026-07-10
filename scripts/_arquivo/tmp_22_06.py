import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.99,
        'caixa': 0.26,
        'lucro': -0.58,
        'positions': [
            {'name':'ASML Holding',  'mkt':'EUR','vol':0.025,'abertura':1641.00,'atual':1674.00,'lucro':0.82, 'pct':2.00, 'trust':'v','valor':41.85,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0, 'abertura':29.280, 'atual':27.880, 'lucro':-1.40,'pct':-4.78,'trust':'r','valor':27.88,'delta':None}
        ]
    },
    'usd': {
        'saldo': 290.51,
        'caixa': 16.18,
        'lucro': 5.56,
        'positions': [
            {'name':'Astera Labs',    'mkt':'USD','vol':0.075,'abertura':376.18, 'atual':439.47,'lucro':4.75, 'pct':16.84,'trust':'v','valor':32.96,'delta':None},
            {'name':'SanDisk',        'mkt':'USD','vol':0.035,'abertura':1999.66,'atual':2273.00,'lucro':9.57, 'pct':13.67,'trust':'v','valor':79.56,'delta':None},
            {'name':'Morgan Stanley', 'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':227.17,'lucro':2.53, 'pct':5.90, 'trust':'v','valor':45.44,'delta':None},
            {'name':'Veracyte',       'mkt':'USD','vol':1.7,  'abertura':53.31,  'atual':52.83, 'lucro':-0.80,'pct':-0.88,'trust':'r','valor':89.82,'delta':None},
            {'name':'Cerebras Systems','mkt':'USD','vol':0.05,'abertura':298.76, 'atual':222.22,'lucro':-3.83,'pct':-25.64,'trust':'r','valor':11.11,'delta':None},
            {'name':'SpaceX',         'mkt':'USD','vol':0.1,  'abertura':221.00, 'atual':154.43,'lucro':-6.66,'pct':-30.14,'trust':'r','valor':15.44,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'VCYT','ativo':'Veracyte','mkt':'USD',
         'nota':'ENTRADA VCYT 1.70 @ 53.31 -- WMS 87'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-22'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUN: +7.32 | REAL_USD_JUN: +11.64

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-22 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('VCYT entrada: 1.70 vol @ 53.31 -- WMS 87 | caixa 106.80 - 90.63 = 16.17 ~ 16.18 checkOK')
print('EUR equity: +6.74 (92.2% meta) | USD equity: +17.20 (58.5% meta)')
print('AUM ~337EUR | 53 dias activos')
print('REAL_EUR_JUN: +7.32 (inalterado) | REAL_USD_JUN: +11.64 (inalterado)')
