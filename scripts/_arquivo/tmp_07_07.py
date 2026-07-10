import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.91,
        'caixa': 1.83,
        'lucro': 0.83,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':423.90,'lucro':1.30, 'pct':3.34, 'trust':'v','valor':40.27,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.810,'lucro':-0.47,'pct':-1.61,'trust':'r','valor':28.81,'delta':None}
        ]
    },
    'usd': {
        'saldo': 273.98,
        'caixa': 0.98,
        'lucro': -15.12,
        'positions': [
            {'name':'JFrog',                'mkt':'USD','vol':1.0, 'abertura':95.40,  'atual':0.00,'lucro':0.39, 'pct':0.41,  'trust':'v','valor':95.79,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':-0.46,'pct':-0.66,'trust':'r','valor':68.76,'delta':None},
            {'name':'Axos Financial',      'mkt':'USD','vol':0.088,'abertura':99.09, 'atual':0.00,'lucro':-0.09,'pct':-1.03,'trust':'r','valor':8.63, 'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.14,'abertura':198.25,'atual':0.00,'lucro':-0.55,'pct':-1.98,'trust':'r','valor':27.21,'delta':None},
            {'name':'Okta',                 'mkt':'USD','vol':0.33,'abertura':151.44,'atual':0.00,'lucro':-1.13,'pct':-2.26,'trust':'r','valor':48.85,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-7.17,'pct':-32.44,'trust':'r','valor':14.93,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-6.11,'pct':-40.90,'trust':'r','valor':8.83, 'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'APLE','ativo':'Apple Hospitality','mkt':'USD',
         'nota':'SAIDA APLE 3 @ 16.51 -- Quebra WMS -- -1.17$'},
        {'tipo':'entrada','ticker':'OKTA','ativo':'Okta','mkt':'USD',
         'nota':'ENTRADA OKTA 0.33 @ 151.44 -- WMS 90A+'},
        {'tipo':'diario','nota':'Saida APLE por Quebra WMS. Entrada OKTA WMS 90A+. SpaceX e Cerebras seguem a piorar (-32.4% e -40.9%).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'APLE',
            'nome': 'Apple Hospitality',
            'mkt': 'USD',
            'lucro': -1.17,
            'lucro_pct': -2.31,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-29',
            'data_saida': '2026-07-07',
            'preco_entrada': 16.90,
            'preco_saida': 16.51,
            'volume': 3.0,
            'dias_holding': 8,
            'setup': 'WMS 83A',
            'nota_entrada': 'ENTRADA APLE WMS 83A',
            'nota_saida': 'Quebra WMS',
            'imagem_setup': None,
            'rating': 0
        }
    ]
}

d['2026-07-07'] = entry

# REAL_EUR_JUL: +0.00 (sem saidas EUR)
# REAL_USD_JUL: 4.12 - 1.17 = +2.95
d['meses']['2026-07']['realizado_usd'] = 2.95

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-07 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('APLE saida: -1.17$ @ 16.51 (8 dias, -2.31%, 0 estrelas)')
print('OKTA entrada: 0.33@151.44 = 49.98$')
print('caixa: 1.43+49.53-49.98=0.98 checkOK')
print('REAL_EUR_JUL: +0.00 (inalterado) | REAL_USD_JUL: +2.95')
print('EUR equity: +0.83 (11.6% meta) | USD equity: -12.17 (-41.4% meta)')
print('AUM ~326EUR | 64 dias activos')
