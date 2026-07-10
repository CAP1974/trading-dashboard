import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 77.16,
        'caixa': 0.06,
        'lucro': 13.93,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':87.990, 'lucro':13.49,'pct':62.14,'trust':'v','valor':35.20,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1385.00,'lucro':0.13, 'pct':1.80, 'trust':'v','valor':7.34, 'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':38.400, 'lucro':0.31, 'pct':0.91, 'trust':'v','valor':34.56,'delta':None}
        ]
    },
    'usd': {
        'saldo': 298.26,
        'caixa': 89.68,
        'lucro': 20.85,
        'positions': [
            {'name':'STMicroelectronics',       'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':79.84,  'lucro':3.65, 'pct':36.21, 'trust':'v','valor':13.73,'delta':None},
            {'name':'Nebius Group NV',          'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':251.53, 'lucro':2.72, 'pct':31.63, 'trust':'v','valor':11.32,'delta':None},
            {'name':'SanDisk',                  'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1832.22,'lucro':8.69, 'pct':25.69, 'trust':'v','valor':42.51,'delta':None},
            {'name':'Datadog',                  'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':250.42, 'lucro':4.30, 'pct':20.73, 'trust':'v','valor':25.04,'delta':None},
            {'name':'Cadence',                  'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':408.07, 'lucro':2.51, 'pct':15.84, 'trust':'v','valor':18.36,'delta':None},
            {'name':'Apple',                    'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':310.06, 'lucro':1.33, 'pct':9.39,  'trust':'v','valor':15.50,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,     'abertura':5.84,   'atual':6.15,   'lucro':1.55, 'pct':5.31,  'trust':'v','valor':30.75,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.1,   'abertura':402.76, 'atual':405.87, 'lucro':0.31, 'pct':0.77,  'trust':'v','valor':40.59,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':214.67, 'lucro':-4.21,'pct':-28.18,'trust':'r','valor':10.73,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Mercado USD em baixa'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-03'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-03 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} lucro:{entry["usd"]["lucro"]}')
