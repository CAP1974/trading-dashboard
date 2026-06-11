import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 71.18,
        'caixa': 6.37,
        'lucro': 8.85,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,'abertura':54.275,'atual':77.150,'lucro':9.15, 'pct':42.15,'trust':'v','valor':30.86,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,'abertura':38.060,'atual':37.720,'lucro':-0.30,'pct':-0.88,'trust':'r','valor':33.95,'delta':None}
        ]
    },
    'usd': {
        'saldo': 282.41,
        'caixa': 31.15,
        'lucro': -4.89,
        'positions': [
            {'name':'Rocket Lab',               'mkt':'USD','vol':0.2,  'abertura':110.02, 'atual':114.75, 'lucro':0.95, 'pct':4.32,  'trust':'v','valor':22.95,'delta':None},
            {'name':'Humana',                   'mkt':'USD','vol':0.1,  'abertura':360.54, 'atual':369.13, 'lucro':0.86, 'pct':2.39,  'trust':'v','valor':36.91,'delta':None},
            {'name':'Eli Lilly',                'mkt':'USD','vol':0.027,'abertura':1148.55,'atual':1160.17,'lucro':0.31, 'pct':1.00,  'trust':'v','valor':31.32,'delta':None},
            {'name':'Royalty Pharma',           'mkt':'USD','vol':0.5,  'abertura':55.60,  'atual':55.10,  'lucro':-0.25,'pct':-0.90, 'trust':'r','valor':27.55,'delta':None},
            {'name':'Morgan Stanley',           'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':212.57, 'lucro':-0.39,'pct':-0.91, 'trust':'r','valor':42.52,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.13, 'abertura':401.79, 'atual':393.36, 'lucro':-1.10,'pct':-2.11, 'trust':'r','valor':51.14,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,    'abertura':5.84,   'atual':5.51,   'lucro':-1.65,'pct':-5.65, 'trust':'r','valor':27.55,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05, 'abertura':298.76, 'atual':226.42, 'lucro':-3.62,'pct':-24.23,'trust':'r','valor':11.32,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida', 'ticker':'HY9H','ativo':'SK Hynix',   'mkt':'EUR','nota':'SAIDA HY9H -0.90EUR @ 1190 -- Circuit Breaker -- distribuicao disfarçada'},
        {'tipo':'entrada','ticker':'RKLB','ativo':'Rocket Lab', 'mkt':'USD','nota':'ENTRADA RKLB 0.2 @ 110.02 -- IPO Momentum SpaceX'},
        {'tipo':'diario','nota':'Saida HY9H EUR (Circuit Breaker). Entrada RKLB (Rocket Lab) IPO Momentum.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'HY9H',
            'nome': 'SK Hynix',
            'mkt': 'EUR',
            'lucro': -0.90,
            'lucro_pct': -12.50,
            'tipo': 'prejuizo',
            'data_entrada': '2026-05-29',
            'data_saida': '2026-06-11',
            'preco_entrada': 1360.0,
            'preco_saida': 1190.0,
            'volume': 0.0053,
            'dias_holding': 13,
            'setup': 'Circuit Breaker',
            'nota_entrada': 'Entrada SK Hynix sector semicondutores',
            'nota_saida': 'distribuicao disfarçada',
            'imagem_setup': None,
            'rating': 0
        }
    ]
}

d['2026-06-11'] = entry

# Actualizar meses realizados Jun 2026
d['meses']['2026-06']['realizado_eur'] = -0.90
d['meses']['2026-06']['realizado_usd'] = 13.98

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-11 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
print(f'HY9H fechada: -0.90EUR | REAL_EUR_JUN: -0.90EUR')
print(f'REAL_USD_JUN: +13.98$ (inalterado)')
