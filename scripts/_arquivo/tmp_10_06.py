import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.89,
        'caixa': 0.06,
        'lucro': 6.66,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':75.330, 'lucro':8.43, 'pct':38.83, 'trust':'v','valor':30.14,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':37.300, 'lucro':-0.68,'pct':-1.99, 'trust':'r','valor':33.57,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1155.00,'lucro':-1.09,'pct':-15.12,'trust':'r','valor':6.12, 'delta':None}
        ]
    },
    'usd': {
        'saldo': 277.76,
        'caixa': 53.15,
        'lucro': -9.54,
        'positions': [
            {'name':'Humana',                   'mkt':'USD','vol':0.1,  'abertura':360.54, 'atual':364.89, 'lucro':0.44, 'pct':1.22,  'trust':'v','valor':36.49,'delta':None},
            {'name':'Eli Lilly',                'mkt':'USD','vol':0.027,'abertura':1148.55,'atual':1137.00,'lucro':-0.31,'pct':-1.00, 'trust':'r','valor':30.70,'delta':None},
            {'name':'Royalty Pharma',           'mkt':'USD','vol':0.5,  'abertura':55.60,  'atual':54.49,  'lucro':-0.55,'pct':-1.98, 'trust':'r','valor':27.25,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.13, 'abertura':401.79, 'atual':390.82, 'lucro':-1.44,'pct':-2.76, 'trust':'r','valor':50.80,'delta':None},
            {'name':'Morgan Stanley',           'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':206.81, 'lucro':-1.55,'pct':-3.61, 'trust':'r','valor':41.36,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,    'abertura':5.84,   'atual':5.23,   'lucro':-3.05,'pct':-10.45,'trust':'r','valor':26.15,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05, 'abertura':298.76, 'atual':237.24, 'lucro':-3.08,'pct':-20.62,'trust':'r','valor':11.86,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'HUM','ativo':'Humana','mkt':'USD','nota':'ENTRADA HUM 0.1 @ 360.54 -- Clean Trend'},
        {'tipo':'diario','nota':'Entrada Humana. Fim do balanceamento com reducao de IA no portfolio.'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-10'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-10 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
