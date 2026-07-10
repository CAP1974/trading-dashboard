import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 72.53,
        'caixa': 41.81,
        'lucro': 9.01,
        'positions': [
            {'name':'Infineon','mkt':'EUR','vol':0.4,'abertura':54.275,'atual':76.810,'lucro':9.01,'pct':41.50,'trust':'v','valor':30.72,'delta':None}
        ]
    },
    'usd': {
        'saldo': 291.22,
        'caixa': 43.11,
        'lucro': 12.93,
        'positions': [
            {'name':'Navitas Semiconductor Corp','mkt':'USD','vol':0.915, 'abertura':23.00,  'atual':28.78,  'lucro':5.28, 'pct':25.08,'trust':'v','valor':26.33,'delta':None},
            {'name':'STMicroelectronics',        'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':67.75,  'lucro':1.57, 'pct':15.58,'trust':'v','valor':11.65,'delta':None},
            {'name':'Apple',                     'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':310.81, 'lucro':1.37, 'pct':9.67, 'trust':'v','valor':15.54,'delta':None},
            {'name':'SanDisk',                   'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1590.80,'lucro':3.09, 'pct':9.14, 'trust':'v','valor':36.91,'delta':None},
            {'name':'Nebius Group NV',           'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':208.40, 'lucro':0.78, 'pct':9.07, 'trust':'v','valor':9.38, 'delta':None},
            {'name':'Datadog',                   'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':221.89, 'lucro':1.45, 'pct':6.99, 'trust':'v','valor':22.19,'delta':None},
            {'name':'Cadence',                   'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':374.11, 'lucro':0.98, 'pct':6.18, 'trust':'v','valor':16.83,'delta':None},
            {'name':'Astera Labs',               'mkt':'USD','vol':0.13,  'abertura':307.93, 'atual':323.93, 'lucro':2.08, 'pct':5.19, 'trust':'v','valor':42.12,'delta':None},
            {'name':'Synopsys',                  'mkt':'USD','vol':0.03,  'abertura':509.99, 'atual':525.63, 'lucro':0.47, 'pct':3.07, 'trust':'v','valor':15.77,'delta':None},
            {'name':'Kodiak Gas Services',       'mkt':'USD','vol':0.54,  'abertura':75.13,  'atual':70.45,  'lucro':-2.53,'pct':-6.24,'trust':'r','valor':38.04,'delta':None},
            {'name':'Cerebras Systems',          'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':266.51, 'lucro':-1.61,'pct':-10.78,'trust':'r','valor':13.33,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'IGG', 'ativo':'IG Group',     'mkt':'EUR','nota':'Saida IGG -0.38EUR @ 180.60 -- falha breakout'},
        {'tipo':'saida','ticker':'PRYS','ativo':'Prysmian',     'mkt':'EUR','nota':'Saida PRYS +2.92EUR @ 146.85 -- lateralizacao, objetivo alcancado'}
    ],
    'posicoes_fechadas': [
        {
            'ticker':'IGG','nome':'IG Group','mkt':'EUR',
            'lucro':-0.38,'lucro_pct':-2.17,'tipo':'prejuizo',
            'data_entrada':'2026-05-21','data_saida':'2026-05-27',
            'preco_entrada':184.60,'preco_saida':180.60,'volume':0.5,
            'dias_holding':6,'setup':'Falha Breakout',
            'nota_entrada':'Entrada IGG Clean Trend','nota_saida':'falha breakout',
            'imagem_setup':None,'rating':0
        },
        {
            'ticker':'PRYS','nome':'Prysmian','mkt':'EUR',
            'lucro':2.92,'lucro_pct':29.10,'tipo':'lucro',
            'data_entrada':'2025-04-09','data_saida':'2026-05-27',
            'preco_entrada':113.75,'preco_saida':146.85,'volume':0.0881,
            'dias_holding':413,'setup':'Lateralizacao',
            'nota_entrada':'Posicao desde o inicio do fundo','nota_saida':'objetivo alcancado',
            'imagem_setup':None,'rating':4
        }
    ]
}

d['2026-05-27'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-05-27 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
