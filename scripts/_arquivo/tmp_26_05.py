import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 73.34,
        'caixa': 18.50,
        'lucro': 12.36,
        'positions': [
            {'name':'IG Group',  'mkt':'EUR','vol':0.5,    'abertura':18.490,'atual':18.440,'lucro':-0.14,'pct':-1.30,'trust':'r','valor':10.61,'delta':None},
            {'name':'Infineon',  'mkt':'EUR','vol':0.4,    'abertura':54.275,'atual':77.260,'lucro':9.19, 'pct':42.33,'trust':'v','valor':30.90,'delta':None},
            {'name':'Prysmian',  'mkt':'EUR','vol':0.0881, 'abertura':113.75,'atual':151.25,'lucro':3.31, 'pct':33.03,'trust':'v','valor':13.33,'delta':None}
        ]
    },
    'usd': {
        'saldo': 294.62,
        'caixa': 43.11,
        'lucro': 16.33,
        'positions': [
            {'name':'Navitas Semiconductor Corp','mkt':'USD','vol':0.915, 'abertura':23.00,   'atual':31.82,  'lucro':8.07, 'pct':38.34,'trust':'v','valor':29.12,'delta':None},
            {'name':'STMicroelectronics',        'mkt':'USD','vol':0.172, 'abertura':58.62,   'atual':70.68,  'lucro':2.08, 'pct':20.63,'trust':'v','valor':12.16,'delta':None},
            {'name':'SanDisk',                   'mkt':'USD','vol':0.0232,'abertura':1457.66, 'atual':1586.00,'lucro':2.97, 'pct':8.78, 'trust':'v','valor':36.79,'delta':None},
            {'name':'Apple',                     'mkt':'USD','vol':0.05,  'abertura':283.49,  'atual':308.17, 'lucro':1.24, 'pct':8.75, 'trust':'v','valor':15.41,'delta':None},
            {'name':'Nebius Group NV',           'mkt':'USD','vol':0.045, 'abertura':191.20,  'atual':207.63, 'lucro':0.74, 'pct':8.60, 'trust':'v','valor':9.34, 'delta':None},
            {'name':'Cadence',                   'mkt':'USD','vol':0.045, 'abertura':352.32,  'atual':381.66, 'lucro':1.32, 'pct':8.33, 'trust':'v','valor':17.17,'delta':None},
            {'name':'Datadog',                   'mkt':'USD','vol':0.1,   'abertura':207.37,  'atual':223.57, 'lucro':1.62, 'pct':7.81, 'trust':'v','valor':22.36,'delta':None},
            {'name':'Synopsys',                  'mkt':'USD','vol':0.03,  'abertura':509.99,  'atual':534.40, 'lucro':0.73, 'pct':4.77, 'trust':'v','valor':16.03,'delta':None},
            {'name':'Astera Labs',               'mkt':'USD','vol':0.13,  'abertura':307.93,  'atual':318.73, 'lucro':1.39, 'pct':3.47, 'trust':'v','valor':41.43,'delta':None},
            {'name':'Kodiak Gas Services',       'mkt':'USD','vol':0.54,  'abertura':75.13,   'atual':73.34,  'lucro':-0.96,'pct':-2.37,'trust':'r','valor':39.61,'delta':None},
            {'name':'Cerebras Systems',          'mkt':'USD','vol':0.05,  'abertura':298.76,  'atual':241.47, 'lucro':-2.87,'pct':-19.21,'trust':'r','valor':12.07,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'TEP','ativo':'Teleperformance','mkt':'EUR','nota':'Saida TEP -2.34 EUR @ 68.20 -- quebra ema21, st1 e st2'},
        {'tipo':'saida','ticker':'VRT','ativo':'Vertiv',         'mkt':'USD','nota':'Saida VRT -0.49$ @ 324.02$ -- quebra ema21, st1 e st2'},
        {'tipo':'saida','ticker':'CVX','ativo':'Chevron',        'mkt':'USD','nota':'Saida CVX -1.14$ @ 184.32$ -- quebra ema21, st1 e st2'},
        {'tipo':'saida','ticker':'MU', 'ativo':'Micron',         'mkt':'USD','nota':'Saida MU +4.01$ @ 910.49$ -- novo conceito CTM +41.6%'}
    ],
    'posicoes_fechadas': [
        {
            'ticker':'TEP','nome':'Teleperformance','mkt':'EUR',
            'lucro':-2.34,'lucro_pct':-11.24,'tipo':'prejuizo',
            'data_entrada':'2026-05-19','data_saida':'2026-05-26',
            'preco_entrada':76.84,'preco_saida':68.20,'volume':0.27,
            'dias_holding':7,'setup':'Quebra EMA21, ST1 e ST2',
            'nota_entrada':'Entrada TEP Clean Trend','nota_saida':'quebra ema21, st1 e st2',
            'imagem_setup':None,'rating':0
        },
        {
            'ticker':'VRT','nome':'Vertiv','mkt':'USD',
            'lucro':-0.49,'lucro_pct':-4.78,'tipo':'prejuizo',
            'data_entrada':'2026-05-05','data_saida':'2026-05-26',
            'preco_entrada':340.29,'preco_saida':324.02,'volume':0.03,
            'dias_holding':21,'setup':'Quebra EMA21, ST1 e ST2',
            'nota_entrada':'Entrada VRT','nota_saida':'quebra ema21, st1 e st2',
            'imagem_setup':None,'rating':0
        },
        {
            'ticker':'CVX','nome':'Chevron','mkt':'USD',
            'lucro':-1.14,'lucro_pct':-5.81,'tipo':'prejuizo',
            'data_entrada':'2026-05-19','data_saida':'2026-05-26',
            'preco_entrada':195.68,'preco_saida':184.32,'volume':0.1,
            'dias_holding':7,'setup':'Quebra EMA21, ST1 e ST2',
            'nota_entrada':'Entrada CVX','nota_saida':'quebra ema21, st1 e st2',
            'imagem_setup':None,'rating':0
        },
        {
            'ticker':'MU','nome':'Micron','mkt':'USD',
            'lucro':4.01,'lucro_pct':41.60,'tipo':'lucro',
            'data_entrada':'2026-05-07','data_saida':'2026-05-26',
            'preco_entrada':643.00,'preco_saida':910.49,'volume':0.015,
            'dias_holding':19,'setup':'Novo Conceito CTM',
            'nota_entrada':'Entrada MU breakout Nasdaq','nota_saida':'novo conceito CTM',
            'imagem_setup':None,'rating':5
        }
    ]
}

d['2026-05-26'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-05-26 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
