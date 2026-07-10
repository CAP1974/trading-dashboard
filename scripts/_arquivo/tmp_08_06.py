import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 72.80,
        'caixa': 0.06,
        'lucro': 9.57,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':78.930, 'lucro':9.87, 'pct':45.46, 'trust':'v','valor':31.58,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':38.760, 'lucro':0.63, 'pct':1.84,  'trust':'v','valor':34.88,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1185.00,'lucro':-0.93,'pct':-12.90,'trust':'r','valor':6.28, 'delta':None}
        ]
    },
    'usd': {
        'saldo': 285.28,
        'caixa': 74.11,
        'lucro': 3.74,
        'positions': [
            {'name':'STMicroelectronics',       'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':74.89,  'lucro':2.80, 'pct':27.78, 'trust':'v','valor':12.88,'delta':None},
            {'name':'SanDisk',                  'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1640.76,'lucro':4.24, 'pct':12.54, 'trust':'v','valor':38.06,'delta':None},
            {'name':'Cadence',                  'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':394.28, 'lucro':1.89, 'pct':11.92, 'trust':'v','valor':17.74,'delta':None},
            {'name':'Eli Lilly',                'mkt':'USD','vol':0.027, 'abertura':1148.55,'atual':1148.16,'lucro':-0.01,'pct':-0.03, 'trust':'r','valor':31.00,'delta':None},
            {'name':'Morgan Stanley',           'mkt':'USD','vol':0.15,  'abertura':214.99, 'atual':212.11, 'lucro':-0.43,'pct':-1.33, 'trust':'r','valor':31.82,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.1,   'abertura':402.76, 'atual':396.15, 'lucro':-0.66,'pct':-1.64, 'trust':'r','valor':39.62,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,     'abertura':5.84,   'atual':5.63,   'lucro':-1.05,'pct':-3.60, 'trust':'r','valor':28.15,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':238.09, 'lucro':-3.04,'pct':-20.35,'trust':'r','valor':11.90,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'AAPL','ativo':'Apple',          'mkt':'USD','nota':'SAIDA AAPL +0.97$ @ 302.80 -- Protocolo V10'},
        {'tipo':'saida','ticker':'DDOG','ativo':'Datadog',        'mkt':'USD','nota':'SAIDA DDOG +2.34$ @ 230.83 -- Protocolo V10'},
        {'tipo':'saida','ticker':'NBIS','ativo':'Nebius Group NV','mkt':'USD','nota':'SAIDA NBIS +1.30$ @ 220.04 -- Protocolo V10'},
        {'tipo':'diario','nota':'Ajuste portfolio para balancear carteira. 3 saidas USD via Protocolo V10.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'AAPL',
            'nome': 'Apple',
            'mkt': 'USD',
            'lucro': 0.97,
            'lucro_pct': 6.81,
            'tipo': 'lucro',
            'data_entrada': '2026-05-01',
            'data_saida': '2026-06-08',
            'preco_entrada': 283.49,
            'preco_saida': 302.80,
            'volume': 0.05,
            'dias_holding': 38,
            'setup': None,
            'nota_entrada': 'Entrada AAPL @ 283.49',
            'nota_saida': 'Protocolo V10',
            'imagem_setup': None,
            'rating': 2
        },
        {
            'ticker': 'DDOG',
            'nome': 'Datadog',
            'mkt': 'USD',
            'lucro': 2.34,
            'lucro_pct': 11.31,
            'tipo': 'lucro',
            'data_entrada': '2026-05-15',
            'data_saida': '2026-06-08',
            'preco_entrada': 207.37,
            'preco_saida': 230.83,
            'volume': 0.1,
            'dias_holding': 24,
            'setup': 'Possivel Breakout',
            'nota_entrada': 'Possivel Breakout',
            'nota_saida': 'Protocolo V10',
            'imagem_setup': None,
            'rating': 3
        },
        {
            'ticker': 'NBIS',
            'nome': 'Nebius Group NV',
            'mkt': 'USD',
            'lucro': 1.30,
            'lucro_pct': 15.08,
            'tipo': 'lucro',
            'data_entrada': '2026-05-18',
            'data_saida': '2026-06-08',
            'preco_entrada': 191.20,
            'preco_saida': 220.04,
            'volume': 0.045,
            'dias_holding': 21,
            'setup': 'Pullback',
            'nota_entrada': 'Pullback reteste EMA',
            'nota_saida': 'Protocolo V10',
            'imagem_setup': None,
            'rating': 3
        }
    ]
}

d['2026-06-08'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-08 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
print(f'Posicoes fechadas: {len(entry["posicoes_fechadas"])} (AAPL +0.97 DDOG +2.34 NBIS +1.30)')
print(f'REAL_USD_JUN novo: +8.22$ (3.61 + 0.97 + 2.34 + 1.30)')
