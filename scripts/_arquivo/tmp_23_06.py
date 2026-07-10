import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 67.18,
        'caixa': 0.26,
        'lucro': -3.39,
        'positions': [
            {'name':'ASML Holding',  'mkt':'EUR','vol':0.025,'abertura':1641.00,'atual':1562.00,'lucro':-1.98,'pct':-4.83,'trust':'r','valor':39.05,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0, 'abertura':29.280, 'atual':27.870, 'lucro':-1.41,'pct':-4.82,'trust':'r','valor':27.87,'delta':None}
        ]
    },
    'usd': {
        'saldo': 277.79,
        'caixa': 114.74,
        'lucro': -7.52,
        'positions': [
            {'name':'Morgan Stanley', 'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':226.20,'lucro':2.33, 'pct':5.43, 'trust':'v','valor':45.24,'delta':None},
            {'name':'Veracyte',       'mkt':'USD','vol':1.7,  'abertura':53.31,  'atual':53.41, 'lucro':0.18, 'pct':0.20, 'trust':'v','valor':90.80,'delta':None},
            {'name':'Cerebras Systems','mkt':'USD','vol':0.05,'abertura':298.76, 'atual':227.25,'lucro':-3.58,'pct':-23.96,'trust':'r','valor':11.36,'delta':None},
            {'name':'SpaceX',         'mkt':'USD','vol':0.1,  'abertura':221.00, 'atual':156.54,'lucro':-6.45,'pct':-29.19,'trust':'r','valor':15.65,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'SNDK','ativo':'SanDisk','mkt':'USD',
         'nota':'SAIDA SNDK 0.035 @ 1956 -- WMS 87 -- -1.53$'},
        {'tipo':'saida','ticker':'ALAB','ativo':'Astera Labs','mkt':'USD',
         'nota':'SAIDA ALAB 0.075 @ 401.27 -- Earnings MU -- +1.89$'},
        {'tipo':'diario','nota':'Saidas SNDK (-1.53$) e ALAB (+1.89$). EUR em forte queda: ASML -4.83%, PST -4.82%. USD flutuante negativo por CBRS e SpaceX.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'SNDK',
            'nome': 'SanDisk',
            'mkt': 'USD',
            'lucro': -1.53,
            'lucro_pct': -2.18,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-17',
            'data_saida': '2026-06-23',
            'preco_entrada': 1999.66,
            'preco_saida': 1956.00,
            'volume': 0.035,
            'dias_holding': 6,
            'setup': 'WMS 87',
            'nota_entrada': 'ENTRADA SNDK WMS 87',
            'nota_saida': 'saida WMS',
            'imagem_setup': None,
            'rating': 0
        },
        {
            'ticker': 'ALAB',
            'nome': 'Astera Labs',
            'mkt': 'USD',
            'lucro': 1.89,
            'lucro_pct': 6.67,
            'tipo': 'lucro',
            'data_entrada': '2026-06-16',
            'data_saida': '2026-06-23',
            'preco_entrada': 376.18,
            'preco_saida': 401.27,
            'volume': 0.075,
            'dias_holding': 7,
            'setup': 'VCP',
            'nota_entrada': 'ENTRADA ALAB VCP',
            'nota_saida': 'saida por Earnings MU',
            'imagem_setup': None,
            'rating': 2
        }
    ]
}

d['2026-06-23'] = entry

# REAL_EUR_JUN: +7.32 (sem saidas EUR hoje)
# REAL_USD_JUN: 11.64 - 1.53 + 1.89 = +12.00
d['meses']['2026-06']['realizado_usd'] = 12.00

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-23 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('SNDK saida: -1.53$ | ALAB saida: +1.89$ | liquido: +0.36$')
print('caixa: 16.18 + 1956*0.035 + 401.27*0.075 = 16.18 + 68.46 + 30.10 = 114.74 checkOK')
print('REAL_EUR_JUN: +7.32 (inalterado) | REAL_USD_JUN: +12.00')
print('EUR equity: +3.93 (53.8% meta) | USD equity: +4.48 (15.2% meta)')
print('AUM ~323EUR | 54 dias activos')
