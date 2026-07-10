import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 74.81,
        'caixa': 7.27,
        'lucro': 11.58,
        'positions': [
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,  'abertura':38.060,'atual':39.380,'lucro':1.19, 'pct':3.47, 'trust':'v','valor':35.44,'delta':None},
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,  'abertura':54.275,'atual':80.260,'lucro':10.39,'pct':47.86,'trust':'v','valor':32.10,'delta':None}
        ]
    },
    'usd': {
        'saldo': 293.12,
        'caixa': 94.44,
        'lucro': 19.37,
        'positions': [
            {'name':'Navitas Semiconductor Corp','mkt':'USD','vol':0.915, 'abertura':23.00,  'atual':28.44,  'lucro':4.97, 'pct':23.61, 'trust':'v','valor':26.02,'delta':None},
            {'name':'Nebius Group NV',           'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':226.39, 'lucro':1.59, 'pct':18.49, 'trust':'v','valor':10.19,'delta':None},
            {'name':'STMicroelectronics',        'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':69.34,  'lucro':1.85, 'pct':18.35, 'trust':'v','valor':11.93,'delta':None},
            {'name':'Astera Labs',               'mkt':'USD','vol':0.13,  'abertura':307.93, 'atual':349.07, 'lucro':5.33, 'pct':13.31, 'trust':'v','valor':45.37,'delta':None},
            {'name':'SanDisk',                   'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1642.13,'lucro':4.28, 'pct':12.66, 'trust':'v','valor':38.10,'delta':None},
            {'name':'Apple',                     'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':312.35, 'lucro':1.45, 'pct':10.23, 'trust':'v','valor':15.62,'delta':None},
            {'name':'Datadog',                   'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':225.10, 'lucro':1.77, 'pct':8.53,  'trust':'v','valor':22.51,'delta':None},
            {'name':'Cadence',                   'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':373.74, 'lucro':0.97, 'pct':6.12,  'trust':'v','valor':16.82,'delta':None},
            {'name':'Cerebras Systems',          'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':241.96, 'lucro':-2.84,'pct':-19.01,'trust':'r','valor':12.10,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'DHER','ativo':'Delivery Hero',  'mkt':'EUR','nota':'Entrada DHER 0.9 @ 38.06EUR -- Clean Trend'},
        {'tipo':'saida',  'ticker':'KGS', 'ativo':'Kodiak Gas Services','mkt':'USD','nota':'Saida KGS -3.58$ @ 68.49$ -- quebra ema21 e st2'},
        {'tipo':'saida',  'ticker':'SNPS','ativo':'Synopsys',        'mkt':'USD','nota':'Saida SNPS -1.06$ @ 474.68$ -- quebra ema21 e st2'}
    ],
    'posicoes_fechadas': [
        {
            'ticker':'KGS','nome':'Kodiak Gas Services','mkt':'USD',
            'lucro':-3.58,'lucro_pct':-8.84,'tipo':'prejuizo',
            'data_entrada':'2026-05-19','data_saida':'2026-05-28',
            'preco_entrada':75.13,'preco_saida':68.49,'volume':0.54,
            'dias_holding':9,'setup':'Quebra EMA21 e ST2',
            'nota_entrada':'Reentrada KGS aumento posicao','nota_saida':'quebra conceito',
            'imagem_setup':None,'rating':0
        },
        {
            'ticker':'SNPS','nome':'Synopsys','mkt':'USD',
            'lucro':-1.06,'lucro_pct':-6.92,'tipo':'prejuizo',
            'data_entrada':'2026-05-08','data_saida':'2026-05-28',
            'preco_entrada':509.99,'preco_saida':474.68,'volume':0.03,
            'dias_holding':20,'setup':'Quebra EMA21 e ST2',
            'nota_entrada':'Entrada SNPS VCP','nota_saida':'quebra conceito',
            'imagem_setup':None,'rating':0
        }
    ]
}

d['2026-05-28'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-05-28 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
