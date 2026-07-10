import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 68.97,
        'caixa': 0.89,
        'lucro': -2.23,
        'positions': [
            {'name':'ASML Holding',  'mkt':'EUR','vol':0.025,'abertura':1641.00,'atual':1593.00,'lucro':-1.20,'pct':-2.92,'trust':'r','valor':39.83,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0, 'abertura':29.280, 'atual':28.250, 'lucro':-1.03,'pct':-3.52,'trust':'r','valor':28.25,'delta':None}
        ]
    },
    'usd': {
        'saldo': 282.97,
        'caixa': 12.84,
        'lucro': -3.60,
        'positions': [
            {'name':'Veracyte',             'mkt':'USD','vol':1.7, 'abertura':53.31, 'atual':0.00,'lucro':8.39, 'pct':9.26, 'trust':'v','valor':99.01,'delta':None},
            {'name':'Brightspring Health',  'mkt':'USD','vol':0.94,'abertura':68.74, 'atual':0.00,'lucro':0.88, 'pct':1.36, 'trust':'v','valor':65.49,'delta':None},
            {'name':'Caterpillar',          'mkt':'USD','vol':0.03,'abertura':1048.01,'atual':0.00,'lucro':0.23,'pct':0.73, 'trust':'v','valor':31.67,'delta':None},
            {'name':'JPMorgan Chase',       'mkt':'USD','vol':0.15,'abertura':333.45,'atual':0.00,'lucro':0.23, 'pct':0.46, 'trust':'v','valor':50.25,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-6.83,'pct':-30.90,'trust':'r','valor':15.27,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-6.50,'pct':-43.51,'trust':'r','valor':8.44, 'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'MS','ativo':'Morgan Stanley','mkt':'USD',
         'nota':'SAIDA MS 0.2 @ 220.89 -- WMS 46C -- +1.26$'},
        {'tipo':'entrada','ticker':'CAT','ativo':'Caterpillar','mkt':'USD',
         'nota':'ENTRADA CAT 0.03 @ 1048.01 -- Macro Detector'},
        {'tipo':'aporte','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'APORTE BTSG +0.44 @ 68.92 -- WMS 87 -- vol total 0.94 preco medio 68.74'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'MS',
            'nome': 'Morgan Stanley',
            'mkt': 'USD',
            'lucro': 1.26,
            'lucro_pct': 2.95,
            'tipo': 'lucro',
            'data_entrada': '2026-06-05',
            'data_saida': '2026-06-25',
            'preco_entrada': 214.56,
            'preco_saida': 220.89,
            'volume': 0.2,
            'dias_holding': 20,
            'setup': 'WMS 87',
            'nota_entrada': None,
            'nota_saida': 'saida WMS 46C',
            'imagem_setup': None,
            'rating': 1
        }
    ]
}

d['2026-06-25'] = entry

# REAL_EUR_JUN: +7.32 (sem saidas EUR)
# REAL_USD_JUN: 12.00 + 1.26 = +13.26
d['meses']['2026-06']['realizado_usd'] = 13.26

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-25 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('MS saida: +1.26$ @ 220.89 (20 dias, 2.95%, 1 estrela)')
print('CAT entrada: 0.03 @ 1048.01 = 31.44$ | BTSG aporte: 0.44 @ 68.92 = 30.32$')
print('caixa: 30.43 + 44.178 - 31.44 - 30.325 = 12.84 checkOK')
print('REAL_EUR_JUN: +7.32 (inalterado) | REAL_USD_JUN: +13.26')
print('EUR equity: +5.09 (69.6% meta) | USD equity: +9.66 (32.9% meta)')
print('AUM ~329EUR | 56 dias activos')
