import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 68.58,
        'caixa': 0.89,
        'lucro': -2.62,
        'positions': [
            {'name':'ASML Holding',  'mkt':'EUR','vol':0.025,'abertura':1641.00,'atual':0.00,'lucro':-1.72,'pct':-4.19,'trust':'r','valor':39.31,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0, 'abertura':29.280, 'atual':0.00, 'lucro':-0.90,'pct':-3.07,'trust':'r','valor':28.38,'delta':None}
        ]
    },
    'usd': {
        'saldo': 283.19,
        'caixa': 62.03,
        'lucro': -2.55,
        'positions': [
            {'name':'Veracyte',            'mkt':'USD','vol':1.7, 'abertura':53.31, 'atual':0.00,'lucro':11.61,'pct':12.81, 'trust':'v','valor':102.23,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.94,'abertura':68.74, 'atual':0.00,'lucro':0.16, 'pct':0.25,  'trust':'v','valor':64.77, 'delta':None},
            {'name':'Caterpillar',         'mkt':'USD','vol':0.03,'abertura':1048.01,'atual':0.00,'lucro':-1.68,'pct':-5.34,'trust':'r','valor':29.76, 'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-6.79,'pct':-30.72,'trust':'r','valor':15.31, 'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-5.85,'pct':-39.16,'trust':'r','valor':9.09,  'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'JPM','ativo':'JPMorgan Chase','mkt':'USD',
         'nota':'SAIDA JPM 0.15 @ 327.94 -- WMS 53C -- -0.83$'},
        {'tipo':'diario','nota':'Macro detector virou para defensivos e industrial. JPM saida -0.83$. VCYT forte +12.81%.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'JPM',
            'nome': 'JPMorgan Chase',
            'mkt': 'USD',
            'lucro': -0.83,
            'lucro_pct': -1.65,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-24',
            'data_saida': '2026-06-26',
            'preco_entrada': 333.45,
            'preco_saida': 327.94,
            'volume': 0.15,
            'dias_holding': 2,
            'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA JPM Ajuste Macro',
            'nota_saida': 'saida WMS 53C',
            'imagem_setup': None,
            'rating': 0
        }
    ]
}

d['2026-06-26'] = entry

# REAL_EUR_JUN: +7.32 (sem saidas EUR)
# REAL_USD_JUN: 13.26 - 0.83 = +12.43
d['meses']['2026-06']['realizado_usd'] = 12.43

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-26 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('JPM saida: -0.83$ @ 327.94 (2 dias, -1.65%, 0 estrelas)')
print('caixa: 12.84 + 327.94*0.15 = 12.84 + 49.19 = 62.03 checkOK')
print('REAL_EUR_JUN: +7.32 (inalterado) | REAL_USD_JUN: +12.43')
print('EUR equity: +4.70 (64.3% meta) | USD equity: +9.88 (33.6% meta)')
print('AUM ~329EUR | 57 dias activos')
