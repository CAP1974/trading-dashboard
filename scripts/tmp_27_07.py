import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.32,
        'caixa': 1.09,
        'lucro': -0.68,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':54.93, 'lucro':-0.07,'pct':-0.36,'trust':'r','valor':19.22,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':945.60,'lucro':-0.61,'pct':-1.23,'trust':'r','valor':49.01,'delta':None}
        ]
    },
    'usd': {
        'saldo': 252.32,
        'caixa': 6.77,
        'lucro': -21.56,
        'positions': [
            {'name':'J&J',                  'mkt':'USD','vol':0.045,'abertura':262.46,'atual':265.88,'lucro':0.15, 'pct':1.27, 'trust':'v','valor':11.96,'delta':None},
            {'name':'Travelers',            'mkt':'USD','vol':0.1,  'abertura':387.77,'atual':390.39,'lucro':0.26, 'pct':0.67, 'trust':'v','valor':39.04,'delta':None},
            {'name':'MetLife',              'mkt':'USD','vol':0.5,  'abertura':95.32, 'atual':95.03, 'lucro':-0.14,'pct':-0.29,'trust':'r','valor':47.52,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':380.91,'lucro':-2.56,'pct':-3.70,'trust':'r','valor':66.66,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':44.79, 'lucro':-2.43,'pct':-4.62,'trust':'r','valor':50.17,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':188.35, 'lucro':-6.04,'pct':-31.41,'trust':'r','valor':13.19,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.15, 'abertura':185.37,'atual':113.37, 'lucro':-10.80,'pct':-38.83,'trust':'r','valor':17.01,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'AAPL','ativo':'Apple','mkt':'USD',
         'nota':'SAIDA AAPL 0.03 @ 334.81 -- earnings proximo -- +0.05$ (tranche aporte)'},
        {'tipo':'saida','ticker':'AAPL','ativo':'Apple','mkt':'USD',
         'nota':'SAIDA AAPL 0.13 @ 334.81 -- earnings proximo -- +0.09$ (tranche original, saida completa)'},
        {'tipo':'entrada','ticker':'MET','ativo':'MetLife','mkt':'USD',
         'nota':'ENTRADA MET 0.5 @ 95.32 -- WMS A+'},
        {'tipo':'diario','nota':'Apple fechada por completo (2 tranches) antes dos earnings. Entrada MetLife. Cerebras -31.41% e SpaceX -38.83% continuam pesados.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'AAPL', 'nome': 'Apple (tranche aporte)', 'mkt': 'USD',
            'lucro': 0.05, 'lucro_pct': 0.55, 'tipo': 'lucro',
            'data_entrada': '2026-07-24', 'data_saida': '2026-07-27',
            'preco_entrada': 332.97, 'preco_saida': 334.81, 'volume': 0.03,
            'dias_holding': 3, 'setup': 'VCP',
            'nota_entrada': 'aporte 24/07', 'nota_saida': 'earnings proximo',
            'imagem_setup': None, 'rating': 1
        },
        {
            'ticker': 'AAPL', 'nome': 'Apple (tranche original)', 'mkt': 'USD',
            'lucro': 0.09, 'lucro_pct': 0.21, 'tipo': 'lucro',
            'data_entrada': '2026-07-17', 'data_saida': '2026-07-27',
            'preco_entrada': 334.12, 'preco_saida': 334.81, 'volume': 0.13,
            'dias_holding': 10, 'setup': 'VCP',
            'nota_entrada': 'ENTRADA AAPL VCP', 'nota_saida': 'earnings proximo -- saida completa',
            'imagem_setup': None, 'rating': 1
        }
    ]
}

d['2026-07-27'] = entry

# REAL_EUR_JUL: -0.08 (inalterado)
# REAL_USD_JUL: -12.56 + 0.05 + 0.09 = -12.42
d['meses']['2026-07']['realizado_usd'] = -12.42

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-27 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('AAPL fechada completa (2 tranches): +0.05 + +0.09 = +0.14 total, antes dos earnings')
print('MET entrada: 0.5@95.32')
print('caixa: 0.86+53.57-47.66=6.77 checkOK')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -12.42')
print('EUR equity: -0.76 (-10.9% meta) | USD equity: -33.98 (-118.4% meta)')
print('AUM ~309EUR | 78 dias activos')
