import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 87.27,
        'caixa': 0.12,
        'lucro': -2.18,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':438.30,'lucro':-0.13,'pct':-0.30,'trust':'r','valor':43.83,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':21.580,'lucro':-1.31,'pct':-6.14,'trust':'r','valor':20.02,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':294.95,'lucro':-0.74,'pct':-3.08,'trust':'r','valor':23.30,'delta':None}
        ]
    },
    'usd': {
        'saldo': 259.47,
        'caixa': 207.53,
        'lucro': -11.13,
        'positions': [
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':483.82, 'lucro':-0.43,'pct':-2.88,'trust':'r','valor':14.51,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':215.58, 'lucro':-4.14,'pct':-21.53,'trust':'r','valor':15.09,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':139.62, 'lucro':-6.56,'pct':-22.70,'trust':'r','valor':22.34,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'BAC','ativo':'Bank of America','mkt':'USD',
         'nota':'SAIDA BAC 1 @ 63.15 -- distribuicao -- +0.82$'},
        {'tipo':'saida','ticker':'AMGN','ativo':'Amgen','mkt':'USD',
         'nota':'SAIDA AMGN 0.15 @ 439.63 -- Esticado -- +2.00$'},
        {'tipo':'diario','nota':'Saidas BAC (distribuicao) e AMGN (esticado), ambas com lucro. Caixa USD subiu para 207.53$. EUR com dia negativo generalizado, BAE -6.14%.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'BAC', 'nome': 'Bank of America', 'mkt': 'USD',
            'lucro': 0.82, 'lucro_pct': 1.32, 'tipo': 'lucro',
            'data_entrada': '2026-08-03', 'data_saida': '2026-08-19',
            'preco_entrada': 62.33, 'preco_saida': 63.15, 'volume': 1.0,
            'dias_holding': 16, 'setup': 'VCP',
            'nota_entrada': 'ENTRADA BAC VCP', 'nota_saida': 'distribuicao',
            'imagem_setup': None, 'rating': 1
        },
        {
            'ticker': 'AMGN', 'nome': 'Amgen', 'mkt': 'USD',
            'lucro': 2.00, 'lucro_pct': 3.14, 'tipo': 'lucro',
            'data_entrada': '2026-08-18', 'data_saida': '2026-08-19',
            'preco_entrada': 426.25, 'preco_saida': 439.63, 'volume': 0.15,
            'dias_holding': 1, 'setup': 'WMS84A',
            'nota_entrada': 'ENTRADA AMGN WMS84A', 'nota_saida': 'Esticado',
            'imagem_setup': None, 'rating': 1
        }
    ]
}

d['2026-08-19'] = entry

# REAL_EUR_AGO: -0.55 (inalterado)
# REAL_USD_AGO: 1.59 + 0.82 + 2.00 = 4.41
d['meses']['2026-08']['realizado_usd'] = 4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-19 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('BAC saida +0.82$ (16 dias) | AMGN saida +2.00$ (1 dia)')
print('caixa: 78.44+63.15+65.94=207.53 checkOK')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41')
print('EUR equity: -2.73 (-39.1% meta) | USD equity: -6.72 (-26.8% meta)')
print('AUM ~517EUR | 95 dias activos')
