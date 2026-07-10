import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 77.03,
        'caixa': 0.06,
        'lucro': 13.80,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':88.360, 'lucro':13.63,'pct':62.78,'trust':'v','valor':35.34,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':38.220, 'lucro':0.15, 'pct':0.44, 'trust':'v','valor':34.40,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1365.00,'lucro':0.02, 'pct':0.28, 'trust':'v','valor':7.23, 'delta':None}
        ]
    },
    'usd': {
        'saldo': 299.68,
        'caixa': 89.66,
        'lucro': 22.30,
        'positions': [
            {'name':'Nebius Group NV',          'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':260.00, 'lucro':3.10, 'pct':36.05, 'trust':'v','valor':11.70,'delta':None},
            {'name':'STMicroelectronics',       'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':79.58,  'lucro':3.61, 'pct':35.81, 'trust':'v','valor':13.69,'delta':None},
            {'name':'Datadog',                  'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':269.00, 'lucro':6.16, 'pct':29.70, 'trust':'v','valor':26.90,'delta':None},
            {'name':'Cadence',                  'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':416.61, 'lucro':2.90, 'pct':18.30, 'trust':'v','valor':18.75,'delta':None},
            {'name':'SanDisk',                  'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1716.14,'lucro':6.00, 'pct':17.74, 'trust':'v','valor':39.82,'delta':None},
            {'name':'Apple',                    'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':315.32, 'lucro':1.60, 'pct':11.29, 'trust':'v','valor':15.77,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,     'abertura':5.84,   'atual':6.13,   'lucro':1.45, 'pct':4.97,  'trust':'v','valor':30.65,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.1,   'abertura':402.76, 'atual':408.99, 'lucro':0.62, 'pct':1.54,  'trust':'v','valor':40.90,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':236.00, 'lucro':-3.14,'pct':-21.02,'trust':'r','valor':11.80,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'FFIV','ativo':'F5 Networks','mkt':'USD','nota':'Entrada FFIV 0.1 @ 402.76$ -- Clean Trend'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-02'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-02 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} lucro:{entry["usd"]["lucro"]}')
