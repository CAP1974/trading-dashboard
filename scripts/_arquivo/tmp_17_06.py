import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 73.29,
        'caixa': 1.89,
        'lucro': -0.02,
        'positions': [
            {'name':'Delivery Hero', 'mkt':'EUR','vol':1.06,'abertura':37.971,'atual':37.970,'lucro':0.00, 'pct':0.00, 'trust':'v','valor':40.25,'delta':None},
            {'name':'Poste Italiane', 'mkt':'EUR','vol':1.0, 'abertura':29.280,'atual':29.260,'lucro':-0.02,'pct':-0.07,'trust':'r','valor':29.26,'delta':None}
        ]
    },
    'usd': {
        'saldo': 317.06,
        'caixa': 39.24,
        'lucro': -6.50,
        'positions': [
            {'name':'Morgan Stanley',  'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':225.08, 'lucro':2.10, 'pct':4.89,  'trust':'v','valor':45.01,'delta':None},
            {'name':'Humana',          'mkt':'USD','vol':0.1,  'abertura':360.54, 'atual':361.58, 'lucro':0.11, 'pct':0.31,  'trust':'v','valor':36.16,'delta':None},
            {'name':'Apple Hospitality','mkt':'USD','vol':1.9, 'abertura':16.25,  'atual':16.24,  'lucro':-0.02,'pct':-0.06, 'trust':'r','valor':30.86,'delta':None},
            {'name':'Astera Labs',     'mkt':'USD','vol':0.075,'abertura':376.18, 'atual':374.40, 'lucro':-0.13,'pct':-0.46, 'trust':'r','valor':28.08,'delta':None},
            {'name':'SanDisk',         'mkt':'USD','vol':0.035,'abertura':1999.66,'atual':1960.00,'lucro':-1.39,'pct':-1.99, 'trust':'r','valor':68.60,'delta':None},
            {'name':'SpaceX',          'mkt':'USD','vol':0.1,  'abertura':221.00, 'atual':191.75, 'lucro':-2.92,'pct':-13.21,'trust':'r','valor':19.18,'delta':None},
            {'name':'Cerebras Systems','mkt':'USD','vol':0.05, 'abertura':298.76, 'atual':213.71, 'lucro':-4.25,'pct':-28.45,'trust':'r','valor':10.69,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida', 'ticker':'IFX', 'ativo':'Infineon',          'mkt':'EUR','nota':'SAIDA IFX +9.09EUR @ 77.01 -- Lateralizacao -- 54 dias'},
        {'tipo':'entrada','ticker':'PST', 'ativo':'Poste Italiane',   'mkt':'EUR','nota':'ENTRADA PST 1 @ 29.28 -- WMS 87'},
        {'tipo':'saida', 'ticker':'RPRX','ativo':'Royalty Pharma',    'mkt':'USD','nota':'SAIDA RPRX -0.85$ @ 53.89 -- Exaustao IEC'},
        {'tipo':'saida', 'ticker':'LLY', 'ativo':'Eli Lilly',         'mkt':'USD','nota':'SAIDA LLY -0.90$ @ 1115.10 -- Exaustao IEC'},
        {'tipo':'saida', 'ticker':'FFIV','ativo':'F5 Networks',       'mkt':'USD','nota':'SAIDA FFIV -1.78$ @ 388.07 -- Exaustao IEC'},
        {'tipo':'entrada','ticker':'SNDK','ativo':'SanDisk',          'mkt':'USD','nota':'ENTRADA SNDK 0.035 @ 1999.66 -- WMS 87'},
        {'tipo':'diario','nota':'Entrada em pratica novos processos no projeto com introducao criterio WMS. Saida IFX (Lateralizacao). 3 saidas USD por Exaustao IEC. Entradas PST e SNDK (WMS 87).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'IFX',
            'nome': 'Infineon',
            'mkt': 'EUR',
            'lucro': 9.09,
            'lucro_pct': 41.89,
            'tipo': 'lucro',
            'data_entrada': '2026-04-24',
            'data_saida': '2026-06-17',
            'preco_entrada': 54.275,
            'preco_saida': 77.01,
            'volume': 0.4,
            'dias_holding': 54,
            'setup': 'Lateralizacao',
            'nota_entrada': None,
            'nota_saida': None,
            'imagem_setup': None,
            'rating': 5
        },
        {
            'ticker': 'RPRX',
            'nome': 'Royalty Pharma',
            'mkt': 'USD',
            'lucro': -0.85,
            'lucro_pct': -3.08,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-09',
            'data_saida': '2026-06-17',
            'preco_entrada': 55.60,
            'preco_saida': 53.89,
            'volume': 0.5,
            'dias_holding': 8,
            'setup': 'Exaustao IEC',
            'nota_entrada': None,
            'nota_saida': None,
            'imagem_setup': None,
            'rating': 0
        },
        {
            'ticker': 'LLY',
            'nome': 'Eli Lilly',
            'mkt': 'USD',
            'lucro': -0.90,
            'lucro_pct': -2.91,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-05',
            'data_saida': '2026-06-17',
            'preco_entrada': 1148.55,
            'preco_saida': 1115.10,
            'volume': 0.027,
            'dias_holding': 12,
            'setup': 'Exaustao IEC',
            'nota_entrada': None,
            'nota_saida': None,
            'imagem_setup': None,
            'rating': 0
        },
        {
            'ticker': 'FFIV',
            'nome': 'F5 Networks',
            'mkt': 'USD',
            'lucro': -1.78,
            'lucro_pct': -3.41,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-02',
            'data_saida': '2026-06-17',
            'preco_entrada': 401.79,
            'preco_saida': 388.07,
            'volume': 0.13,
            'dias_holding': 15,
            'setup': 'Exaustao IEC',
            'nota_entrada': None,
            'nota_saida': None,
            'imagem_setup': None,
            'rating': 0
        }
    ]
}

d['2026-06-17'] = entry

d['meses']['2026-06']['realizado_eur'] = 8.19
d['meses']['2026-06']['realizado_usd'] = 11.01

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-17 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('REAL_EUR_JUN: +8.19 | REAL_USD_JUN: +11.01')
print('EUR equity: +8.17 (111.8% meta) | USD equity: +4.51 (15.3% meta)')
print('AUM aprox 365')
