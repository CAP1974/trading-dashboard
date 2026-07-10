import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

# Remove stub 2026-06-02 (substituído por dado real de 01/06)
if '2026-06-02' in d:
    del d['2026-06-02']

entry = {
    'eur': {
        'saldo': 73.68,
        'caixa': 0.06,
        'lucro': 10.45,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':80.630, 'lucro':10.55,'pct':48.60,'trust':'v','valor':32.26,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1390.00,'lucro':0.16, 'pct':2.22, 'trust':'v','valor':7.37, 'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':37.770, 'lucro':-0.26,'pct':-0.76,'trust':'r','valor':33.99,'delta':None}
        ]
    },
    'usd': {
        'saldo': 297.23,
        'caixa': 129.94,
        'lucro': 19.85,
        'positions': [
            {'name':'Nebius Group NV',            'mkt':'USD','vol':0.045, 'abertura':191.20, 'atual':264.42, 'lucro':3.30, 'pct':38.37, 'trust':'v','valor':11.90,'delta':None},
            {'name':'Datadog',                    'mkt':'USD','vol':0.1,   'abertura':207.37, 'atual':276.37, 'lucro':6.90, 'pct':33.27, 'trust':'v','valor':27.64,'delta':None},
            {'name':'SanDisk',                    'mkt':'USD','vol':0.0232,'abertura':1457.66,'atual':1759.55,'lucro':7.00, 'pct':20.70, 'trust':'v','valor':40.82,'delta':None},
            {'name':'STMicroelectronics',         'mkt':'USD','vol':0.172, 'abertura':58.62,  'atual':69.01,  'lucro':1.79, 'pct':17.76, 'trust':'v','valor':11.87,'delta':None},
            {'name':'Cadence',                    'mkt':'USD','vol':0.045, 'abertura':352.32, 'atual':412.70, 'lucro':2.72, 'pct':17.16, 'trust':'v','valor':18.57,'delta':None},
            {'name':'Apple',                      'mkt':'USD','vol':0.05,  'abertura':283.49, 'atual':306.34, 'lucro':1.15, 'pct':8.12,  'trust':'v','valor':15.32,'delta':None},
            {'name':'Keel Infrastructure Corp',   'mkt':'USD','vol':5,     'abertura':5.84,   'atual':6.10,   'lucro':1.30, 'pct':4.45,  'trust':'v','valor':30.50,'delta':None},
            {'name':'Cerebras Systems',           'mkt':'USD','vol':0.05,  'abertura':298.76, 'atual':212.61, 'lucro':-4.31,'pct':-28.85,'trust':'r','valor':10.63,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida',  'ticker':'NVTS','ativo':'Navitas Semiconductor Corp','mkt':'USD','nota':'Saida NVTS +1.63$ @ 24.79$ -- quebra ema21 e ST1'},
        {'tipo':'saida',  'ticker':'ALAB','ativo':'Astera Labs',               'mkt':'USD','nota':'Saida ALAB +1.98$ @ 323.19$ -- quebra ema21 e ST1'},
        {'tipo':'entrada','ticker':'KEEL','ativo':'Keel Infrastructure Corp',  'mkt':'USD','nota':'Entrada KEEL 5 @ 5.84$ -- Clean Trend'},
        {'tipo':'diario', 'nota':'2 saidas por quebra conceito e 1 entrada aprovada pelo protocolo'}
    ],
    'posicoes_fechadas': [
        {
            'ticker':'NVTS','nome':'Navitas Semiconductor Corp','mkt':'USD',
            'lucro':1.63,'lucro_pct':7.78,'tipo':'lucro',
            'data_entrada':'2026-05-11','data_saida':'2026-06-01',
            'preco_entrada':23.00,'preco_saida':24.79,'volume':0.915,
            'dias_holding':21,'setup':'Quebra EMA21 e ST1',
            'nota_entrada':'Entrada NVTS VCP','nota_saida':'quebra conceito',
            'imagem_setup':None,'rating':2
        },
        {
            'ticker':'ALAB','nome':'Astera Labs','mkt':'USD',
            'lucro':1.98,'lucro_pct':4.96,'tipo':'lucro',
            'data_entrada':'2026-05-22','data_saida':'2026-06-01',
            'preco_entrada':307.93,'preco_saida':323.19,'volume':0.13,
            'dias_holding':10,'setup':'Quebra EMA21 e ST1',
            'nota_entrada':'Entrada ALAB Clean Trend','nota_saida':'quebra conceito',
            'imagem_setup':None,'rating':1
        }
    ]
}

d['2026-06-01'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-01 criado OK | stub 2026-06-02 removido')
print(f'EUR saldo:{entry["eur"]["saldo"]} caixa:{entry["eur"]["caixa"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
