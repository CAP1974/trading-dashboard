import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 74.89,
        'caixa': 0.06,
        'lucro': 11.66,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':84.860, 'lucro':12.23,'pct':56.33, 'trust':'v','valor':33.94,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':38.010, 'lucro':-0.04,'pct':-0.12, 'trust':'r','valor':34.21,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1260.00,'lucro':-0.53,'pct':-7.35, 'trust':'r','valor':6.68, 'delta':None}
        ]
    },
    'usd': {
        'saldo': 295.16,
        'caixa': 89.68,
        'lucro': 17.75,
        'positions': [
            {'name':'Nebius Group NV',          'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':259.55, 'lucro':3.08, 'pct':35.81, 'trust':'v','valor':11.68,'delta':None},
            {'name':'STMicroelectronics',       'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':78.27,  'lucro':3.38, 'pct':33.53, 'trust':'v','valor':13.46,'delta':None},
            {'name':'SanDisk',                  'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1756.00,'lucro':6.92, 'pct':20.46, 'trust':'v','valor':40.74,'delta':None},
            {'name':'Datadog',                  'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':243.65, 'lucro':3.63, 'pct':17.50, 'trust':'v','valor':24.37,'delta':None},
            {'name':'Cadence',                  'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':410.61, 'lucro':2.63, 'pct':16.59, 'trust':'v','valor':18.48,'delta':None},
            {'name':'Apple',                    'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':311.29, 'lucro':1.39, 'pct':9.81,  'trust':'v','valor':15.56,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,     'abertura':5.84,   'atual':5.93,   'lucro':0.45, 'pct':1.54,  'trust':'v','valor':29.65,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.1,   'abertura':402.76, 'atual':407.22, 'lucro':0.44, 'pct':1.09,  'trust':'v','valor':40.72,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':215.36, 'lucro':-4.17,'pct':-27.91,'trust':'r','valor':10.77,'delta':None}
        ]
    },
    'eventos': [],
    'posicoes_fechadas': []
}

d['2026-06-04'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-04 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} lucro:{entry["usd"]["lucro"]}')
