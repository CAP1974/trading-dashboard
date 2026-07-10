import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 73.10,
        'caixa': 0.06,
        'lucro': 9.87,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':81.230,  'lucro':10.79,'pct':49.70, 'trust':'v','valor':32.50,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1345.000,'lucro':-0.08,'pct':-1.11, 'trust':'r','valor':7.13, 'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':37.120,  'lucro':-0.84,'pct':-2.45, 'trust':'r','valor':33.41,'delta':None}
        ]
    },
    'usd': {
        'saldo': 294.09,
        'caixa': 94.44,
        'lucro': 20.34,
        'positions': [
            {'name':'Nebius Group NV',           'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':230.94, 'lucro':1.79, 'pct':20.81, 'trust':'v','valor':10.39,'delta':None},
            {'name':'Datadog',                   'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':247.70, 'lucro':4.03, 'pct':19.43, 'trust':'v','valor':24.77,'delta':None},
            {'name':'STMicroelectronics',        'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':69.23,  'lucro':1.83, 'pct':18.15, 'trust':'v','valor':11.91,'delta':None},
            {'name':'SanDisk',                   'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1696.95,'lucro':5.55, 'pct':16.41, 'trust':'v','valor':39.37,'delta':None},
            {'name':'Navitas Semiconductor Corp','mkt':'USD','vol':0.915, 'abertura':23.00,  'atual':26.59,  'lucro':3.28, 'pct':15.58, 'trust':'v','valor':24.33,'delta':None},
            {'name':'Astera Labs',               'mkt':'USD','vol':0.13,  'abertura':307.93, 'atual':342.59, 'lucro':4.50, 'pct':11.24, 'trust':'v','valor':44.54,'delta':None},
            {'name':'Apple',                     'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':312.05, 'lucro':1.43, 'pct':10.09, 'trust':'v','valor':15.60,'delta':None},
            {'name':'Cadence',                   'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':374.76, 'lucro':1.01, 'pct':6.37,  'trust':'v','valor':16.86,'delta':None},
            {'name':'Cerebras Systems',          'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':237.28, 'lucro':-3.08,'pct':-20.62,'trust':'r','valor':11.86,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'HY9H','ativo':'SK Hynix','mkt':'EUR','nota':'Entrada HY9H 0.0053 @ 1360 EUR -- Clean Trend'}
    ],
    'posicoes_fechadas': []
}

d['2026-05-29'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-05-29 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
