import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 88.26,
        'caixa': 0.12,
        'lucro': -1.19,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':441.90, 'lucro':0.23, 'pct':0.52, 'trust':'v','valor':44.19,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':22.200,'lucro':-0.67,'pct':-3.14,'trust':'r','valor':20.66,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':294.85,'lucro':-0.75,'pct':-3.12,'trust':'r','valor':23.29,'delta':None}
        ]
    },
    'usd': {
        'saldo': 259.06,
        'caixa': 78.44,
        'lucro': -8.72,
        'positions': [
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':64.19,  'lucro':1.86, 'pct':2.98, 'trust':'v','valor':64.19,'delta':None},
            {'name':'Amgen',                'mkt':'USD','vol':0.15, 'abertura':426.25,'atual':424.91, 'lucro':-0.20,'pct':-0.31,'trust':'r','valor':63.74,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':481.25, 'lucro':-0.50,'pct':-3.35,'trust':'r','valor':14.44,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':218.68, 'lucro':-3.93,'pct':-20.44,'trust':'r','valor':15.30,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':143.46, 'lucro':-5.95,'pct':-20.59,'trust':'r','valor':22.95,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'SAIDA PANW 0.1 @ 373.74 -- st1/distribuicao -- +2.15$ (tranche 1/4)'},
        {'tipo':'saida','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'SAIDA PANW 0.04 @ 373.74 -- st1/distribuicao -- +0.39$ (tranche 2/4)'},
        {'tipo':'saida','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'SAIDA PANW 0.04 @ 373.74 -- st1/distribuicao -- +0.37$ (tranche 3/4)'},
        {'tipo':'saida','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'SAIDA PANW 0.2 @ 373.74 -- st1/distribuicao -- -0.49$ (tranche 4/4, saida completa)'},
        {'tipo':'entrada','ticker':'AMGN','ativo':'Amgen','mkt':'USD',
         'nota':'ENTRADA AMGN 0.15 @ 426.25 -- WMS84A'},
        {'tipo':'diario','nota':'Palo Alto fechada por completo (4 tranches, st1/distribuicao): +2.15+0.39+0.37-0.49=+2.42 total. Entrada Amgen. EUR sem trades, dia negativo generalizado (Schneider -3.12%, BAE -3.14%).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'PANW', 'nome': 'Palo Alto (tranche 1/4)', 'mkt': 'USD',
            'lucro': 2.15, 'lucro_pct': 6.12, 'tipo': 'lucro',
            'data_entrada': '2026-08-06', 'data_saida': '2026-08-18',
            'preco_entrada': 352.18, 'preco_saida': 373.74, 'volume': 0.1,
            'dias_holding': 12, 'setup': 'Clean Trend',
            'nota_entrada': 'aporte 06/08', 'nota_saida': 'st1/distribuicao',
            'imagem_setup': None, 'rating': 2
        },
        {
            'ticker': 'PANW', 'nome': 'Palo Alto (tranche 2/4)', 'mkt': 'USD',
            'lucro': 0.39, 'lucro_pct': 2.68, 'tipo': 'lucro',
            'data_entrada': '2026-08-05', 'data_saida': '2026-08-18',
            'preco_entrada': 363.98, 'preco_saida': 373.74, 'volume': 0.04,
            'dias_holding': 13, 'setup': 'Clean Trend',
            'nota_entrada': 'ENTRADA PANW Clean Trend (tranche 3/3 original)', 'nota_saida': 'st1/distribuicao',
            'imagem_setup': None, 'rating': 1
        },
        {
            'ticker': 'PANW', 'nome': 'Palo Alto (tranche 3/4)', 'mkt': 'USD',
            'lucro': 0.37, 'lucro_pct': 2.54, 'tipo': 'lucro',
            'data_entrada': '2026-08-05', 'data_saida': '2026-08-18',
            'preco_entrada': 364.48, 'preco_saida': 373.74, 'volume': 0.04,
            'dias_holding': 13, 'setup': 'Clean Trend',
            'nota_entrada': 'ENTRADA PANW Clean Trend (tranche 2/3 original)', 'nota_saida': 'st1/distribuicao',
            'imagem_setup': None, 'rating': 1
        },
        {
            'ticker': 'PANW', 'nome': 'Palo Alto (tranche 4/4)', 'mkt': 'USD',
            'lucro': -0.49, 'lucro_pct': -0.65, 'tipo': 'prejuizo',
            'data_entrada': '2026-08-05', 'data_saida': '2026-08-18',
            'preco_entrada': 376.18, 'preco_saida': 373.74, 'volume': 0.2,
            'dias_holding': 13, 'setup': 'Clean Trend',
            'nota_entrada': 'ENTRADA PANW Clean Trend (tranche 1/3 original)', 'nota_saida': 'st1/distribuicao -- saida completa',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-08-18'] = entry

# REAL_EUR_AGO: -0.55 (inalterado)
# REAL_USD_AGO: -0.83 + 2.15 + 0.39 + 0.37 - 0.49 = 1.59
d['meses']['2026-08']['realizado_usd'] = 1.59

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-18 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('PANW fechada completa (4 tranches): +2.15+0.39+0.37-0.49=+2.42 total')
print('caixa: 0.36+142.02-63.94=78.44 checkOK')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +1.59')
print('EUR equity: -1.74 (-24.9% meta) | USD equity: -7.13 (-28.5% meta)')
print('AUM ~399EUR | 94 dias activos')
