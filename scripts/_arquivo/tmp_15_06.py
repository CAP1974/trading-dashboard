import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 73.11,
        'caixa': 0.37,
        'lucro': 10.41,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4, 'abertura':54.275,'atual':80.990,'lucro':10.69,'pct':49.24,'trust':'v','valor':32.40,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':1.06,'abertura':37.971,'atual':37.710,'lucro':-0.28,'pct':-0.70,'trust':'r','valor':39.97,'delta':None}
        ]
    },
    'usd': {
        'saldo': 304.78,
        'caixa': 22.28,
        'lucro': -4.81,
        'positions': [
            {'name':'Humana',                   'mkt':'USD','vol':0.1,  'abertura':360.54, 'atual':379.92, 'lucro':1.94, 'pct':5.38,  'trust':'v','valor':37.99,'delta':None},
            {'name':'Morgan Stanley',           'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':217.95, 'lucro':0.68, 'pct':1.58,  'trust':'v','valor':43.59,'delta':None},
            {'name':'Apple Hospitality',        'mkt':'USD','vol':1.9,  'abertura':16.25,  'atual':16.14,  'lucro':-0.21,'pct':-0.68, 'trust':'r','valor':30.67,'delta':None},
            {'name':'Eli Lilly',                'mkt':'USD','vol':0.027,'abertura':1148.55,'atual':1129.17,'lucro':-0.52,'pct':-1.68, 'trust':'r','valor':30.49,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.13, 'abertura':401.79, 'atual':394.47, 'lucro':-0.96,'pct':-1.84, 'trust':'r','valor':51.28,'delta':None},
            {'name':'Royalty Pharma',           'mkt':'USD','vol':0.5,  'abertura':55.60,  'atual':54.12,  'lucro':-0.74,'pct':-2.66, 'trust':'r','valor':27.06,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,    'abertura':5.84,   'atual':5.65,   'lucro':-0.95,'pct':-3.25, 'trust':'r','valor':28.25,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05, 'abertura':298.76, 'atual':217.76, 'lucro':-4.05,'pct':-27.11,'trust':'r','valor':10.89,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida', 'ticker':'RKLB','ativo':'Rocket Lab','mkt':'USD','nota':'SAIDA RKLB +0.01$ @ 110.04 -- Teste IPO Spacex -- break-even'},
        {'tipo':'diario','nota':'Saida RKLB break-even. Humana e Morgan Stanley em positivo. Semana começa com USD equity positiva.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'RKLB',
            'nome': 'Rocket Lab',
            'mkt': 'USD',
            'lucro': 0.01,
            'lucro_pct': 0.02,
            'tipo': 'lucro',
            'data_entrada': '2026-06-11',
            'data_saida': '2026-06-15',
            'preco_entrada': 110.02,
            'preco_saida': 110.04,
            'volume': 0.20,
            'dias_holding': 4,
            'setup': 'Teste IPO Spacex',
            'nota_entrada': 'IPO Momentum SpaceX',
            'nota_saida': 'break-even',
            'imagem_setup': None,
            'rating': 1
        }
    ]
}

d['2026-06-15'] = entry

# Actualizar REAL_USD_JUN: 13.98 + 0.01 = 13.99
d['meses']['2026-06']['realizado_usd'] = 13.99

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-15 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
print('RKLB fechada: +0.01$ | REAL_USD_JUN: +13.99$')
print('REAL_EUR_JUN: -0.90€ (inalterado)')
print('EUR equity: +9.51€ (130.1% meta)')
print('USD equity: +9.18$ (31.2% meta)')
print('AUM ≈354€')
