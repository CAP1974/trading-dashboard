import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.64,
        'caixa': 1.83,
        'lucro': -0.44,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':413.00,'lucro':0.27, 'pct':0.69, 'trust':'v','valor':39.24,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.570,'lucro':-0.71,'pct':-2.42,'trust':'r','valor':28.57,'delta':None}
        ]
    },
    'usd': {
        'saldo': 286.87,
        'caixa': 7.08,
        # CAIXA confirmada via screenshot/eventos pelo utilizador; calculo manual (-2.31) nao reconciliou -- aceite 7.08 sem explicacao adicional
        'lucro': 0.77,
        'positions': [
            {'name':'Veracyte',            'mkt':'USD','vol':1.7, 'abertura':53.31, 'atual':0.00,'lucro':9.17, 'pct':10.12, 'trust':'v','valor':99.79,'delta':None},
            {'name':'Caterpillar',         'mkt':'USD','vol':0.03,'abertura':1048.01,'atual':0.00,'lucro':0.42,'pct':1.34,  'trust':'v','valor':31.86,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':0.34,'pct':0.49, 'trust':'v','valor':69.56,'delta':None},
            {'name':'Apple Hospitality',   'mkt':'USD','vol':3.0, 'abertura':16.90, 'atual':0.00,'lucro':-0.24,'pct':-0.47,'trust':'r','valor':50.46,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-5.01,'pct':-22.67,'trust':'r','valor':17.09,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-3.91,'pct':-26.17,'trust':'r','valor':11.03,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'SAIDA BTSG 0.94 @ 59.12 -- Lateralizacao -- +0.36$'},
        {'tipo':'entrada','ticker':'HUM','ativo':'Humana','mkt':'USD',
         'nota':'ENTRADA HUM 0.175 @ 395.53 -- Clean Trend'},
        {'tipo':'diario','nota':'Saida BTSG (+0.36$) e entrada HUM (Clean Trend). Caixa USD 7.08$ confirmada pelo utilizador (calculo manual nao reconciliou).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'BTSG',
            'nome': 'Brightspring Health Services',
            'mkt': 'USD',
            'lucro': 0.36,
            'lucro_pct': 0.55,
            'tipo': 'lucro',
            'data_entrada': '2026-06-24',
            'data_saida': '2026-06-30',
            'preco_entrada': 68.74,
            'preco_saida': 59.12,
            'volume': 0.94,
            'dias_holding': 6,
            'setup': 'Ajuste Macro',
            'nota_entrada': 'entrada 0.5 + aporte 0.44 (preco medio 68.74)',
            'nota_saida': 'saida Lateralizacao',
            'imagem_setup': None,
            'rating': 1
        }
    ]
}

d['2026-06-30'] = entry

# REAL_EUR_JUN: +6.20 (sem saidas EUR)
# REAL_USD_JUN: 12.43 + 0.36 = +12.79
d['meses']['2026-06']['realizado_usd'] = 12.79

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-30 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('BTSG saida: +0.36$ @ 59.12 (6 dias, 0.55%, 1 estrela)')
print('CAIXA USD nao reconciliou pelo calculo (-2.31 vs 7.08) -- aceite por confirmacao do utilizador')
print('REAL_EUR_JUN: +6.20 (inalterado) | REAL_USD_JUN: +12.79')
print('EUR equity: +5.76 (78.8% meta) | USD equity: +13.56 (46.1% meta)')
print('AUM ~334EUR | 59 dias activos')
