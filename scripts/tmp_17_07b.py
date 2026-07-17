import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.42,
        'caixa': 1.09,
        'lucro': -0.58,
        'positions': [
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':948.40,'lucro':-0.02,'pct':-0.04,'trust':'r','valor':49.60,'delta':None},
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':53.85,  'lucro':-0.56,'pct':-2.90,'trust':'r','valor':18.73,'delta':None}
        ]
    },
    'usd': {
        'saldo': 264.86,
        'caixa': 1.73,
        'lucro': -12.99,
        'positions': [
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1,  'abertura':401.93,'atual':0.00,'lucro':3.58, 'pct':8.91, 'trust':'v','valor':43.77,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':0.76, 'pct':1.10, 'trust':'v','valor':69.98,'delta':None},
            {'name':'Apple',                'mkt':'USD','vol':0.13, 'abertura':334.12,'atual':0.00,'lucro':-0.06,'pct':-0.14,'trust':'r','valor':43.38,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':0.00,'lucro':-0.30,'pct':-0.67,'trust':'r','valor':44.35,'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.2,  'abertura':207.88,'atual':0.00,'lucro':-0.98,'pct':-2.36,'trust':'r','valor':40.60,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05, 'abertura':298.76,'atual':0.00,'lucro':-6.28,'pct':-42.03,'trust':'r','valor':8.66, 'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1,  'abertura':221.00,'atual':0.00,'lucro':-9.71,'pct':-43.94,'trust':'r','valor':12.39,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'ASTH','ativo':'Astrana Health','mkt':'USD',
         'nota':'SAIDA ASTH 1 @ 44.08 -- EMA21+ST1 -- -3.01$'},
        {'tipo':'entrada','ticker':'AAPL','ativo':'Apple','mkt':'USD',
         'nota':'ENTRADA AAPL 0.13 @ 334.12 -- VCP'},
        {'tipo':'diario','nota':'Saida ASTH por EMA21+ST1. Entrada AAPL (VCP). Cerebras e SpaceX seguem a piorar (-42.03%% e -43.94%%).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'ASTH', 'nome': 'Astrana Health', 'mkt': 'USD',
            'lucro': -3.01, 'lucro_pct': -6.39, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-08', 'data_saida': '2026-07-17',
            'preco_entrada': 47.09, 'preco_saida': 44.08, 'volume': 1.0,
            'dias_holding': 9, 'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA ASTH Ajuste Macro', 'nota_saida': 'EMA21+ST1',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-17'] = entry

# REAL_EUR_JUL: -0.08 (inalterado)
# REAL_USD_JUL: -5.45 - 3.01 = -8.46
d['meses']['2026-07']['realizado_usd'] = -8.46

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-17 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('ASTH saida: -3.01$ @ 44.08 (9 dias, -6.39%, 0 estrelas)')
print('AAPL entrada: 0.13@334.12')
print('caixa: 1.09+44.08-43.44=1.73 checkOK')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -8.46')
print('EUR equity: -0.66 (-9.5% meta) | USD equity: -21.45 (-74.8% meta)')
print('AUM ~316EUR | 72 dias activos')
