import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 72.76,
        'caixa': 0.37,
        'lucro': 10.06,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4, 'abertura':54.275,'atual':79.840,'lucro':10.23,'pct':47.12,'trust':'v','valor':31.94,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':1.06,'abertura':37.971,'atual':37.810,'lucro':-0.17,'pct':-0.42,'trust':'r','valor':40.08,'delta':None}
        ]
    },
    'usd': {
        'saldo': 280.24,
        'caixa': 0.27,
        'lucro': -7.33,
        'positions': [
            {'name':'Humana',                   'mkt':'USD','vol':0.1,  'abertura':360.54, 'atual':377.98, 'lucro':1.75, 'pct':4.85,  'trust':'v','valor':37.80,'delta':None},
            {'name':'Morgan Stanley',           'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':214.07, 'lucro':-0.10,'pct':-0.23, 'trust':'r','valor':42.81,'delta':None},
            {'name':'Apple Hospitality',        'mkt':'USD','vol':1.9,  'abertura':16.25,  'atual':16.21,  'lucro':-0.08,'pct':-0.26, 'trust':'r','valor':30.80,'delta':None},
            {'name':'Royalty Pharma',           'mkt':'USD','vol':0.5,  'abertura':55.60,  'atual':54.87,  'lucro':-0.36,'pct':-1.29, 'trust':'r','valor':27.44,'delta':None},
            {'name':'Eli Lilly',                'mkt':'USD','vol':0.027,'abertura':1148.55,'atual':1132.67,'lucro':-0.43,'pct':-1.39, 'trust':'r','valor':30.58,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.13, 'abertura':401.79, 'atual':394.09, 'lucro':-1.01,'pct':-1.93, 'trust':'r','valor':51.23,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,    'abertura':5.84,   'atual':5.58,   'lucro':-1.30,'pct':-4.45, 'trust':'r','valor':27.90,'delta':None},
            {'name':'Rocket Lab',               'mkt':'USD','vol':0.2,  'abertura':110.02, 'atual':102.32, 'lucro':-1.54,'pct':-7.00, 'trust':'r','valor':20.46,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05, 'abertura':298.76, 'atual':213.69, 'lucro':-4.26,'pct':-28.51,'trust':'r','valor':10.68,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'aporte', 'ticker':'DHER','ativo':'Delivery Hero','mkt':'EUR','nota':'APORTE DHER +0.16 @ 37.47 -- reforço pullback -- nova media 37.971 vol 1.06'},
        {'tipo':'entrada','ticker':'APLE','ativo':'Apple Hospitality','mkt':'USD','nota':'ENTRADA APLE 1.9 @ 16.25 -- VCP'},
        {'tipo':'diario','nota':'Aporte DHER (reforço pullback). Entrada APLE Apple Hospitality (VCP).'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-12'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-12 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
print('REAL_EUR_JUN: -0.90EUR (inalterado)')
print('REAL_USD_JUN: +13.98$ (inalterado)')
print('EUR equity: +9.16EUR (125.3% meta)')
print('USD equity: +6.65$ (22.6% meta)')
