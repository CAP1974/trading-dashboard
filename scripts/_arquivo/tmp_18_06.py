import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 71.90,
        'caixa': 1.86,
        'lucro': -1.35,
        'positions': [
            {'name':'Poste Italiane', 'mkt':'EUR','vol':1.0, 'abertura':29.280,'atual':28.720,'lucro':-0.56,'pct':-1.91,'trust':'r','valor':28.72,'delta':None},
            {'name':'Delivery Hero',  'mkt':'EUR','vol':1.06,'abertura':37.971,'atual':37.220,'lucro':-0.79,'pct':-1.96,'trust':'r','valor':39.46,'delta':None}
        ]
    },
    'usd': {
        'saldo': 395.92,
        'caixa': 106.80,
        'lucro': 4.17,
        'positions': [
            {'name':'Astera Labs',    'mkt':'USD','vol':0.075,'abertura':376.18,'atual':416.50,'lucro':3.03, 'pct':10.74, 'trust':'v','valor':31.24,'delta':None},
            {'name':'SanDisk',        'mkt':'USD','vol':0.035,'abertura':1999.66,'atual':2177.20,'lucro':6.21,'pct':8.87,  'trust':'v','valor':76.20,'delta':None},
            {'name':'Morgan Stanley', 'mkt':'USD','vol':0.2,  'abertura':214.56,'atual':223.35, 'lucro':1.76, 'pct':4.10,  'trust':'v','valor':44.67,'delta':None},
            {'name':'SpaceX',         'mkt':'USD','vol':0.1,  'abertura':221.00, 'atual':185.12, 'lucro':-3.59,'pct':-16.24,'trust':'r','valor':18.51,'delta':None},
            {'name':'Cerebras Systems','mkt':'USD','vol':0.05,'abertura':298.76, 'atual':234.00, 'lucro':-3.24,'pct':-21.69,'trust':'r','valor':11.70,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'APLE','ativo':'Apple Hospitality','mkt':'USD','nota':'SAIDA APLE +0.57$ @ 16.55 -- Quebra WMS'},
        {'tipo':'saida','ticker':'HUM', 'ativo':'Humana',           'mkt':'USD','nota':'SAIDA HUM +0.06$ @ 361.06 -- Quebra WMS'},
        {'tipo':'diario','nota':'Saidas APLE e HUM por Quebra WMS. ALAB e SNDK em forte alta.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'APLE',
            'nome': 'Apple Hospitality',
            'mkt': 'USD',
            'lucro': 0.57,
            'lucro_pct': 1.85,
            'tipo': 'lucro',
            'data_entrada': '2026-06-12',
            'data_saida': '2026-06-18',
            'preco_entrada': 16.25,
            'preco_saida': 16.55,
            'volume': 1.9,
            'dias_holding': 6,
            'setup': 'Quebra WMS',
            'nota_entrada': None,
            'nota_saida': None,
            'imagem_setup': None,
            'rating': 1
        },
        {
            'ticker': 'HUM',
            'nome': 'Humana',
            'mkt': 'USD',
            'lucro': 0.06,
            'lucro_pct': 0.14,
            'tipo': 'lucro',
            'data_entrada': '2026-06-10',
            'data_saida': '2026-06-18',
            'preco_entrada': 360.54,
            'preco_saida': 361.06,
            'volume': 0.1,
            'dias_holding': 8,
            'setup': 'Quebra WMS',
            'nota_entrada': None,
            'nota_saida': None,
            'imagem_setup': None,
            'rating': 1
        }
    ]
}

d['2026-06-18'] = entry

d['meses']['2026-06']['realizado_usd'] = 11.64

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-18 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('REAL_EUR_JUN: +8.19 (inalterado) | REAL_USD_JUN: +11.64')
print('EUR equity: +6.84 (93.6% meta) | USD equity: +15.81 (53.8% meta)')
print('AUM aprox 436')
