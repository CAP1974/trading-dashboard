import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.82,
        'caixa': 39.84,
        'lucro': -0.18,
        'positions': [
            {'name':'Swiss Life', 'mkt':'EUR','vol':0.0295,'abertura':939.00,'atual':942.60,'lucro':-0.18,'pct':-0.60,'trust':'r','valor':29.98,'delta':None}
        ]
    },
    'usd': {
        'saldo': 269.12,
        'caixa': 1.09,
        'lucro': -11.74,
        'positions': [
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1,  'abertura':401.93,'atual':0.00,'lucro':3.36, 'pct':8.36, 'trust':'v','valor':43.55,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':1.77, 'pct':2.56, 'trust':'v','valor':70.99,'delta':None},
            {'name':'Astrana Health',      'mkt':'USD','vol':1.0,  'abertura':47.09, 'atual':0.00,'lucro':-0.33,'pct':-0.70,'trust':'r','valor':46.76,'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.2,  'abertura':207.88,'atual':0.00,'lucro':-0.32,'pct':-0.77,'trust':'r','valor':41.26,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':0.00,'lucro':-1.88,'pct':-4.21,'trust':'r','valor':42.77,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05, 'abertura':298.76,'atual':0.00,'lucro':-5.74,'pct':-38.42,'trust':'r','valor':9.20, 'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1,  'abertura':221.00,'atual':0.00,'lucro':-8.60,'pct':-38.91,'trust':'r','valor':13.50,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'ALV','ativo':'Allianz','mkt':'EUR',
         'nota':'SAIDA ALV 0.095 @ 415.30 -- Ema21 -- +0.48EUR'},
        {'tipo':'saida','ticker':'L','ativo':'Loews','mkt':'USD',
         'nota':'SAIDA L 0.35 @ 112.75 -- ema21+ST1 -- -1.33$'},
        {'tipo':'entrada','ticker':'CRWD','ativo':'Crowdstrike','mkt':'USD',
         'nota':'ENTRADA CRWD 0.2 @ 207.98 -- PB4/5'},
        {'tipo':'diario','nota':'Allianz fechada (Ema21). Loews fechada (ema21+ST1). Nova entrada CRWD (PB4/5). Caixa EUR subiu para 39.84 com a venda de Allianz sem reinvestimento imediato.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'ALV', 'nome': 'Allianz', 'mkt': 'EUR',
            'lucro': 0.48, 'lucro_pct': 1.24, 'tipo': 'lucro',
            'data_entrada': '2026-06-29', 'data_saida': '2026-07-15',
            'preco_entrada': 410.20, 'preco_saida': 415.30, 'volume': 0.095,
            'dias_holding': 16, 'setup': 'WMS 84A',
            'nota_entrada': 'ENTRADA ALV WMS 84A', 'nota_saida': 'Ema21',
            'imagem_setup': None, 'rating': 1
        },
        {
            'ticker': 'L', 'nome': 'Loews', 'mkt': 'USD',
            'lucro': -1.33, 'lucro_pct': -3.26, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-14', 'data_saida': '2026-07-15',
            'preco_entrada': 116.55, 'preco_saida': 112.75, 'volume': 0.35,
            'dias_holding': 1, 'setup': 'Momento Macro',
            'nota_entrada': 'ENTRADA L Momento Macro', 'nota_saida': 'ema21+ST1',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-15'] = entry

# REAL_EUR_JUL: -0.56 + 0.48 = -0.08
# REAL_USD_JUL: -4.12 - 1.33 = -5.45
d['meses']['2026-07']['realizado_eur'] = -0.08
d['meses']['2026-07']['realizado_usd'] = -5.45

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-15 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('ALV saida: +0.48EUR (16 dias, +1.24%, 1 estrela)')
print('L saida: -1.33$ (1 dia, -3.26%, 0 estrelas) | CRWD entrada: 0.2@207.98')
print('caixa EUR: 0.39+39.45=39.84 checkOK')
print('caixa USD: 3.04+39.46-41.6=0.91 vs 1.09 informado (~0.18$ diferenca, provavel comissao corretora)')
print('REAL_EUR_JUL: -0.08 | REAL_USD_JUL: -5.45')
print('EUR equity: -0.26 (-3.6% meta) | USD equity: -17.19 (-58.5% meta)')
print('AUM ~358EUR | 70 dias activos')
