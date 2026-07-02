import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.90,
        'caixa': 1.83,
        'lucro': 0.82,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':419.70,'lucro':0.90, 'pct':2.31, 'trust':'v','valor':39.87,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':29.200,'lucro':-0.08,'pct':-0.27,'trust':'r','valor':29.20,'delta':None}
        ]
    },
    'usd': {
        'saldo': 277.56,
        'caixa': 1.38,
        'lucro': -12.66,
        'positions': [
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':0.10, 'pct':0.14,  'trust':'v','valor':69.32,'delta':None},
            {'name':'JFrog',                'mkt':'USD','vol':1.0, 'abertura':95.40,  'atual':0.00,'lucro':-0.62,'pct':-0.65,'trust':'r','valor':94.78,'delta':None},
            {'name':'Apple Hospitality',   'mkt':'USD','vol':3.0, 'abertura':16.90,  'atual':0.00,'lucro':-0.78,'pct':-1.54,'trust':'r','valor':49.92,'delta':None},
            {'name':'Axos Financial',      'mkt':'USD','vol':0.088,'abertura':99.09, 'atual':0.00,'lucro':-0.15,'pct':-1.72,'trust':'r','valor':8.57, 'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.14,'abertura':198.25,'atual':0.00,'lucro':-0.60,'pct':-2.16,'trust':'r','valor':27.16,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-5.91,'pct':-26.74,'trust':'r','valor':16.19,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-4.70,'pct':-31.46,'trust':'r','valor':10.24,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'CAT','ativo':'Caterpillar','mkt':'USD',
         'nota':'SAIDA CAT 0.03 @ 981.52 -- quebra ema21 e st1 -- -1.99$'},
        {'tipo':'saida','ticker':'VCYT','ativo':'Veracyte','mkt':'USD',
         'nota':'SAIDA VCYT 1.7 @ 56.90 -- Quebra WMS -- +6.11$'},
        {'tipo':'entrada','ticker':'CRWD','ativo':'Crowdstrike','mkt':'USD',
         'nota':'ENTRADA CRWD 0.14 @ 198.25 -- Clean Trend'},
        {'tipo':'entrada','ticker':'FROG','ativo':'JFrog','mkt':'USD',
         'nota':'ENTRADA FROG 1 @ 95.40 -- Clean Trend'},
        {'tipo':'aporte','ticker':'AX','ativo':'Axos Financial','mkt':'USD',
         'nota':'APORTE AX +0.018 @ 99.03 -- vol total 0.088 preco medio 99.09'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'CAT',
            'nome': 'Caterpillar',
            'mkt': 'USD',
            'lucro': -1.99,
            'lucro_pct': -6.35,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-25',
            'data_saida': '2026-07-02',
            'preco_entrada': 1048.01,
            'preco_saida': 981.52,
            'volume': 0.03,
            'dias_holding': 7,
            'setup': 'Macro Detector',
            'nota_entrada': 'ENTRADA CAT Macro Detector',
            'nota_saida': 'quebra ema21 e st1',
            'imagem_setup': None,
            'rating': 0
        },
        {
            'ticker': 'VCYT',
            'nome': 'Veracyte',
            'mkt': 'USD',
            'lucro': 6.11,
            'lucro_pct': 6.73,
            'tipo': 'lucro',
            'data_entrada': '2026-06-22',
            'data_saida': '2026-07-02',
            'preco_entrada': 53.31,
            'preco_saida': 56.90,
            'volume': 1.7,
            'dias_holding': 10,
            'setup': 'WMS 87',
            'nota_entrada': 'ENTRADA VCYT WMS 87',
            'nota_saida': 'Quebra WMS',
            'imagem_setup': None,
            'rating': 2
        }
    ]
}

d['2026-07-02'] = entry

# REAL_EUR_JUL: +0.00 (sem saidas EUR)
# REAL_USD_JUL: 0.00 - 1.99 + 6.11 = +4.12
d['meses']['2026-07']['realizado_usd'] = 4.12

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-02 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('CAT saida: -1.99$ (7 dias) | VCYT saida: +6.11$ (10 dias)')
print('AX aporte: vol 0.07+0.018=0.088 preco medio 99.09 checkOK')
print('caixa: 0.14+29.45+96.73-27.76-95.40-1.78=1.38 checkOK')
print('REAL_EUR_JUL: +0.00 | REAL_USD_JUL: +4.12')
print('EUR equity: +0.82 (11.5% meta) | USD equity: -8.54 (-29.0% meta)')
print('AUM ~329EUR | 61 dias activos')
