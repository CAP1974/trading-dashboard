import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 71.16,
        'caixa': 0.06,
        'lucro': 7.93,
        'positions': [
            {'name':'Infineon',     'mkt':'EUR','vol':0.4,   'abertura':54.275,  'atual':76.600, 'lucro':8.93, 'pct':41.13, 'trust':'v','valor':30.64,'delta':None},
            {'name':'Delivery Hero','mkt':'EUR','vol':0.9,   'abertura':38.060,  'atual':38.010, 'lucro':-0.04,'pct':-0.12, 'trust':'r','valor':34.21,'delta':None},
            {'name':'SK Hynix',     'mkt':'EUR','vol':0.0053,'abertura':1360.000,'atual':1180.00,'lucro':-0.96,'pct':-13.31,'trust':'r','valor':6.25, 'delta':None}
        ]
    },
    'usd': {
        'saldo': 279.63,
        'caixa': 89.20,
        'lucro': -7.67,
        'positions': [
            {'name':'Royalty Pharma',           'mkt':'USD','vol':0.5,  'abertura':55.60,  'atual':55.62,  'lucro':0.01, 'pct':0.04,  'trust':'v','valor':27.81,'delta':None},
            {'name':'Eli Lilly',                'mkt':'USD','vol':0.027,'abertura':1148.55,'atual':1140.00,'lucro':-0.23,'pct':-0.74, 'trust':'r','valor':30.78,'delta':None},
            {'name':'F5 Networks',              'mkt':'USD','vol':0.13, 'abertura':401.79, 'atual':395.10, 'lucro':-0.88,'pct':-1.68, 'trust':'r','valor':51.36,'delta':None},
            {'name':'Morgan Stanley',           'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':210.12, 'lucro':-0.88,'pct':-2.05, 'trust':'r','valor':42.03,'delta':None},
            {'name':'Keel Infrastructure Corp', 'mkt':'USD','vol':5,    'abertura':5.84,   'atual':5.42,   'lucro':-2.10,'pct':-7.19, 'trust':'r','valor':27.10,'delta':None},
            {'name':'Cerebras Systems',         'mkt':'USD','vol':0.05, 'abertura':298.76, 'atual':226.90, 'lucro':-3.59,'pct':-24.03,'trust':'r','valor':11.35,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'SNDK','ativo':'SanDisk',          'mkt':'USD','nota':'SAIDA SNDK +2.70$ @ 1583.70 -- Protocolo V10'},
        {'tipo':'saida','ticker':'STM', 'ativo':'STMicroelectronics','mkt':'USD','nota':'SAIDA STM +1.81$ @ 69.49 -- Protocolo V10'},
        {'tipo':'saida','ticker':'CDNS','ativo':'Cadence',          'mkt':'USD','nota':'SAIDA CDNS +1.25$ @ 380.02 -- Protocolo V10'},
        {'tipo':'entrada','ticker':'RPRX','ativo':'Royalty Pharma', 'mkt':'USD','nota':'ENTRADA RPRX 0.5 @ 55.60 -- VCP'},
        {'tipo':'diario','nota':'Balanceamento de carteira via Protocolo Macro Detector. 3 saidas V10 + 1 entrada VCP (RPRX).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'SNDK',
            'nome': 'SanDisk',
            'mkt': 'USD',
            'lucro': 2.70,
            'lucro_pct': 4.81,
            'tipo': 'lucro',
            'data_entrada': '2026-04-20',
            'data_saida': '2026-06-09',
            'preco_entrada': 1510.99,
            'preco_saida': 1583.70,
            'volume': 0.0372,
            'dias_holding': 50,
            'setup': 'Protocolo V10',
            'nota_entrada': 'Entrada SNDK longo prazo',
            'nota_saida': 'Protocolo V10',
            'imagem_setup': None,
            'rating': 1
        },
        {
            'ticker': 'STM',
            'nome': 'STMicroelectronics',
            'mkt': 'USD',
            'lucro': 1.81,
            'lucro_pct': 5.32,
            'tipo': 'lucro',
            'data_entrada': '2026-04-20',
            'data_saida': '2026-06-09',
            'preco_entrada': 65.98,
            'preco_saida': 69.49,
            'volume': 0.516,
            'dias_holding': 50,
            'setup': 'Protocolo V10',
            'nota_entrada': 'Entrada STM posicao longo prazo',
            'nota_saida': 'Protocolo V10',
            'imagem_setup': None,
            'rating': 2
        },
        {
            'ticker': 'CDNS',
            'nome': 'Cadence Design Systems',
            'mkt': 'USD',
            'lucro': 1.25,
            'lucro_pct': 7.86,
            'tipo': 'lucro',
            'data_entrada': '2026-05-13',
            'data_saida': '2026-06-09',
            'preco_entrada': 352.32,
            'preco_saida': 380.02,
            'volume': 0.045,
            'dias_holding': 27,
            'setup': 'Protocolo V10',
            'nota_entrada': 'Breakout tech sector',
            'nota_saida': 'Protocolo V10',
            'imagem_setup': None,
            'rating': 2
        }
    ]
}

d['2026-06-09'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-09 criado OK')
print(f'EUR saldo:{entry["eur"]["saldo"]} lucro:{entry["eur"]["lucro"]}')
print(f'USD saldo:{entry["usd"]["saldo"]} caixa:{entry["usd"]["caixa"]} lucro:{entry["usd"]["lucro"]}')
print(f'Posicoes fechadas: SNDK +2.70 | STM +1.81 | CDNS +1.25')
print(f'REAL_USD_JUN: 8.22 + 5.76 = +13.98$')
