import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.17,
        'caixa': 1.83,
        'lucro': 0.09,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':418.10,'lucro':0.75, 'pct':1.92, 'trust':'v','valor':39.72,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.620,'lucro':-0.66,'pct':-2.25,'trust':'r','valor':28.62,'delta':None}
        ]
    },
    'usd': {
        'saldo': 268.79,
        'caixa': 0.03,
        'lucro': -14.22,
        'positions': [
            {'name':'Canadian Natural',    'mkt':'USD','vol':0.62,'abertura':42.30,'atual':0.00,'lucro':0.08, 'pct':0.30, 'trust':'v','valor':26.31,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':0.11,'pct':0.16, 'trust':'v','valor':69.33,'delta':None},
            {'name':'Occidental',          'mkt':'USD','vol':1.0, 'abertura':53.70, 'atual':0.00,'lucro':-0.10,'pct':-0.19,'trust':'r','valor':53.60,'delta':None},
            {'name':'Seadrill',            'mkt':'USD','vol':1.0, 'abertura':40.65, 'atual':0.00,'lucro':-0.11,'pct':-0.27,'trust':'r','valor':40.54,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.128,'abertura':70.70, 'atual':0.00,'lucro':-0.06,'pct':-0.66,'trust':'r','valor':8.99, 'delta':None},
            {'name':'Astrana Health',      'mkt':'USD','vol':1.0, 'abertura':47.09, 'atual':0.00,'lucro':-0.99,'pct':-2.10,'trust':'r','valor':46.10,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-7.29,'pct':-32.99,'trust':'r','valor':14.81,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-5.86,'pct':-39.22,'trust':'r','valor':9.08, 'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'AX','ativo':'Axos Financial','mkt':'USD',
         'nota':'SAIDA AX 0.088 @ 95.78 -- Decisao Mudanca Macro -- -0.30$'},
        {'tipo':'saida','ticker':'OKTA','ativo':'Okta','mkt':'USD',
         'nota':'SAIDA OKTA 0.33 @ 145.78 -- Decisao Mudanca Macro -- -1.87$'},
        {'tipo':'saida','ticker':'FROG','ativo':'JFrog','mkt':'USD',
         'nota':'SAIDA FROG 1 @ 92.76 -- Decisao Mudanca Macro -- -2.64$'},
        {'tipo':'saida','ticker':'CRWD','ativo':'Crowdstrike','mkt':'USD',
         'nota':'SAIDA CRWD 0.14 @ 189.15 -- Decisao Mudanca Macro -- -1.28$'},
        {'tipo':'entrada','ticker':'ASTH','ativo':'Astrana Health','mkt':'USD',
         'nota':'ENTRADA ASTH 1 @ 47.09 -- Ajuste Macro'},
        {'tipo':'entrada','ticker':'SDRL','ativo':'Seadrill','mkt':'USD',
         'nota':'ENTRADA SDRL 1 @ 40.65 -- Ajuste Macro'},
        {'tipo':'entrada','ticker':'OXY','ativo':'Occidental','mkt':'USD',
         'nota':'ENTRADA OXY 1 @ 53.70 -- Ajuste Macro'},
        {'tipo':'entrada','ticker':'CNQ','ativo':'Canadian Natural','mkt':'USD',
         'nota':'ENTRADA CNQ 0.62 @ 42.30 -- Ajuste Macro'},
        {'tipo':'entrada','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'ENTRADA BTSG 0.128 @ 70.70 -- Ajuste Macro'},
        {'tipo':'diario','nota':'Mudanca da carteira para ajuste macro e indecisao geo-politica com retorno conflito EUA-Irao. 4 saidas (AX, OKTA, FROG, CRWD) e 5 entradas defensivas/energia (ASTH, SDRL, OXY, CNQ, BTSG).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'AX', 'nome': 'Axos Financial', 'mkt': 'USD',
            'lucro': -0.30, 'lucro_pct': -3.44, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-01', 'data_saida': '2026-07-08',
            'preco_entrada': 99.19, 'preco_saida': 95.78, 'volume': 0.088,
            'dias_holding': 7, 'setup': 'Clean Trend',
            'nota_entrada': 'entrada 0.07 + aporte 0.018 (preco medio 99.19)',
            'nota_saida': 'Decisao Mudanca Macro', 'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'OKTA', 'nome': 'Okta', 'mkt': 'USD',
            'lucro': -1.87, 'lucro_pct': -3.74, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-07', 'data_saida': '2026-07-08',
            'preco_entrada': 151.44, 'preco_saida': 145.78, 'volume': 0.33,
            'dias_holding': 1, 'setup': 'WMS 90A+',
            'nota_entrada': 'ENTRADA OKTA WMS 90A+', 'nota_saida': 'Decisao Mudanca Macro',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'FROG', 'nome': 'JFrog', 'mkt': 'USD',
            'lucro': -2.64, 'lucro_pct': -2.77, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-02', 'data_saida': '2026-07-08',
            'preco_entrada': 95.40, 'preco_saida': 92.76, 'volume': 1.0,
            'dias_holding': 6, 'setup': 'Clean Trend',
            'nota_entrada': 'ENTRADA FROG Clean Trend', 'nota_saida': 'Decisao Mudanca Macro',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'CRWD', 'nome': 'Crowdstrike', 'mkt': 'USD',
            'lucro': -1.28, 'lucro_pct': -4.59, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-02', 'data_saida': '2026-07-08',
            'preco_entrada': 198.25, 'preco_saida': 189.15, 'volume': 0.14,
            'dias_holding': 6, 'setup': 'Clean Trend',
            'nota_entrada': 'ENTRADA CRWD Clean Trend', 'nota_saida': 'Decisao Mudanca Macro',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-08'] = entry

# REAL_EUR_JUL: +0.00 (sem saidas EUR)
# REAL_USD_JUL: 2.95 - 0.30 - 1.87 - 2.64 - 1.28 = -3.14
d['meses']['2026-07']['realizado_usd'] = -3.14

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-08 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('4 saidas: AX -0.30 | OKTA -1.87 | FROG -2.64 | CRWD -1.28 = -6.09 total')
print('5 entradas: ASTH, SDRL, OXY, CNQ, BTSG (Ajuste Macro)')
print('caixa: 0.98+175.78-176.72=0.03 checkOK (rebalanceamento por conflito EUA-Irao)')
print('REAL_EUR_JUL: +0.00 (inalterado) | REAL_USD_JUL: -3.14')
print('EUR equity: +0.09 (1.3% meta) | USD equity: -17.36 (-59.1% meta)')
print('AUM ~319EUR | 65 dias activos')
