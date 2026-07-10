import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 72.05,
        'caixa': 0.06,
        'lucro': 8.82,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':77.590, 'lucro':9.33, 'pct':42.98, 'trust':'v','valor':31.04,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':38.880, 'lucro':0.74, 'pct':2.16,  'trust':'v','valor':34.99,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1125.00,'lucro':-1.25,'pct':-17.34,'trust':'r','valor':5.96, 'delta':None}
        ]
    },
    'usd': {
        'saldo': 277.30,
        'caixa': 25.99,
        'lucro': 0.32,
        'positions': [
            {'name':'STMicroelectronics',       'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':70.70,  'lucro':2.08, 'pct':20.63, 'trust':'v','valor':12.16,'delta':None},
            {'name':'Nebius Group NV',          'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':227.80, 'lucro':1.65, 'pct':19.19, 'trust':'v','valor':10.25,'delta':None},
            {'name':'Datadog',                  'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':233.11, 'lucro':2.57, 'pct':12.39, 'trust':'v','valor':23.31,'delta':None},
            {'name':'Apple',                    'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':307.50, 'lucro':1.21, 'pct':8.54,  'trust':'v','valor':15.38,'delta':None},
            {'name':'Cadence',                  'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':376.26, 'lucro':1.08, 'pct':6.81,  'trust':'v','valor':16.93,'delta':None},
            {'name':'SanDisk',                  'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1554.92,'lucro':2.26, 'pct':6.68,  'trust':'v','valor':36.08,'delta':None},
            {'name':'Morgan Stanley',           'mkt':'USD','vol':0.15,  'abertura':214.99, 'atual':211.89, 'lucro':-0.47,'pct':-1.46, 'trust':'r','valor':31.78,'delta':None},
            {'name':'Eli Lilly',                'mkt':'USD','vol':0.027, 'abertura':1148.55,'atual':1130.00,'lucro':-0.50,'pct':-1.61, 'trust':'r','valor':30.51,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.1,   'abertura':402.76, 'atual':393.03, 'lucro':-0.98,'pct':-2.43, 'trust':'r','valor':39.30,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,     'abertura':5.84,   'atual':5.11,   'lucro':-3.65,'pct':-12.50,'trust':'r','valor':25.55,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':200.20, 'lucro':-4.93,'pct':-33.00,'trust':'r','valor':10.01,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'MS', 'ativo':'Morgan Stanley',          'mkt':'USD','nota':'Entrada MS 0.15 @ 214.99$ -- Clean Trend'},
        {'tipo':'entrada','ticker':'LLY','ativo':'Eli Lilly',               'mkt':'USD','nota':'Entrada LLY 0.027 @ 1148.55$ -- Clean Trend'},
        {'tipo':'diario', 'nota':'Forte quedas no setor tech e IA. Taxas USD: -0.39EUR'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-05'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-05 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} lucro:{entry["usd"]["lucro"]}')
