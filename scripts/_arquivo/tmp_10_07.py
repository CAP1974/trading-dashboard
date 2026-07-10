import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.60,
        'caixa': 1.83,
        'lucro': 0.52,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':422.60,'lucro':1.18, 'pct':3.03, 'trust':'v','valor':40.15,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.620,'lucro':-0.66,'pct':-2.25,'trust':'r','valor':28.62,'delta':None}
        ]
    },
    'usd': {
        'saldo': 268.02,
        'caixa': 17.06,
        'lucro': -13.46,
        'positions': [
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':0.00,'lucro':0.18, 'pct':0.40,  'trust':'v','valor':44.83,'delta':None},
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1, 'abertura':401.93,'atual':0.00,'lucro':-0.33,'pct':-0.82,'trust':'r','valor':39.86,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':-0.67,'pct':-0.97,'trust':'r','valor':68.55,'delta':None},
            {'name':'Astrana Health',      'mkt':'USD','vol':1.0, 'abertura':47.09, 'atual':0.00,'lucro':-0.50,'pct':-1.06,'trust':'r','valor':46.59,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':0.62,'abertura':42.30, 'atual':0.00,'lucro':-0.33,'pct':-1.26,'trust':'r','valor':25.90,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-4.24,'pct':-28.38,'trust':'r','valor':10.70,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-7.57,'pct':-34.25,'trust':'r','valor':14.53,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'OXY','ativo':'Occidental','mkt':'USD',
         'nota':'SAIDA OXY 1 @ 52.43 -- Macro -- -1.27$'},
        {'tipo':'saida','ticker':'SDRL','ativo':'Seadrill','mkt':'USD',
         'nota':'SAIDA SDRL 1 @ 40.39 -- Macro -- -0.26$'},
        {'tipo':'entrada','ticker':'DAVE','ativo':'Dave Inc','mkt':'USD',
         'nota':'ENTRADA DAVE 0.1 @ 401.93 -- Clean Trend -- aposta IPO'},
        {'tipo':'aporte','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'APORTE BTSG +0.5 @ 71.19 -- vol total 0.628 preco medio 71.09'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'OXY', 'nome': 'Occidental', 'mkt': 'USD',
            'lucro': -1.27, 'lucro_pct': -2.36, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-08', 'data_saida': '2026-07-10',
            'preco_entrada': 53.70, 'preco_saida': 52.43, 'volume': 1.0,
            'dias_holding': 2, 'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA OXY Ajuste Macro', 'nota_saida': 'Macro',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'SDRL', 'nome': 'Seadrill', 'mkt': 'USD',
            'lucro': -0.26, 'lucro_pct': -0.64, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-08', 'data_saida': '2026-07-10',
            'preco_entrada': 40.65, 'preco_saida': 40.39, 'volume': 1.0,
            'dias_holding': 2, 'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA SDRL Ajuste Macro', 'nota_saida': 'Macro',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-10'] = entry

# REAL_EUR_JUL: +0.00 (sem saidas EUR)
# REAL_USD_JUL: -3.14 - 1.27 - 0.26 = -4.67
d['meses']['2026-07']['realizado_usd'] = -4.67

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-10 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('OXY saida: -1.27$ | SDRL saida: -0.26$ (ambas 2 dias)')
print('DAVE entrada: 0.1@401.93 | BTSG aporte: vol 0.628 preco medio 71.09')
print('caixa: 0.03+52.43+40.39-40.19-35.60=17.06 checkOK')
print('REAL_EUR_JUL: +0.00 (inalterado) | REAL_USD_JUL: -4.67')
print('EUR equity: +0.52 (7.3% meta) | USD equity: -18.13 (-61.7% meta)')
print('AUM ~335EUR | 67 dias activos')
