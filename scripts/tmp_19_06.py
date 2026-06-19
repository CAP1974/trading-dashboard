import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 71.34,
        'caixa': 0.26,
        'lucro': 0.51,
        'positions': [
            {'name':'ASML Holding',  'mkt':'EUR','vol':0.025,'abertura':1641.00,'atual':1662.40,'lucro':0.53, 'pct':1.29, 'trust':'v','valor':41.56,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0, 'abertura':29.280, 'atual':29.260, 'lucro':-0.02,'pct':-0.07,'trust':'r','valor':29.26,'delta':None}
        ]
    },
    'usd': {
        # Mercado USD fechado (Juneteenth) — identico a 18/06
        'saldo': 395.92,
        'caixa': 106.80,
        'lucro': 4.17,
        'positions': [
            {'name':'Astera Labs',    'mkt':'USD','vol':0.075,'abertura':376.18, 'atual':416.50,'lucro':3.03, 'pct':10.74, 'trust':'v','valor':31.24,'delta':None},
            {'name':'SanDisk',        'mkt':'USD','vol':0.035,'abertura':1999.66,'atual':2177.20,'lucro':6.21,'pct':8.87,  'trust':'v','valor':76.20,'delta':None},
            {'name':'Morgan Stanley', 'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':223.35,'lucro':1.76, 'pct':4.10,  'trust':'v','valor':44.67,'delta':None},
            {'name':'SpaceX',         'mkt':'USD','vol':0.1,  'abertura':221.00, 'atual':185.12,'lucro':-3.59,'pct':-16.24,'trust':'r','valor':18.51,'delta':None},
            {'name':'Cerebras Systems','mkt':'USD','vol':0.05,'abertura':298.76, 'atual':234.00,'lucro':-3.24,'pct':-21.69,'trust':'r','valor':11.70,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'DHER','ativo':'Delivery Hero','mkt':'EUR',
         'nota':'SAIDA DHER 1.06 vol total @ 37.21 -- Lateralizacao -- aporte(-0.10EUR) + original(-0.77EUR)'},
        {'tipo':'entrada','ticker':'ASML','ativo':'ASML Holding','mkt':'EUR',
         'nota':'ENTRADA ASML 0.025 @ 1641 -- Clean Trend'},
        {'tipo':'diario','nota':'Mercado USD fechado (Juneteenth). DHER fechada totalmente. ASML nova entrada Clean Trend. Caixa: 0.26EUR verificado por calculo.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'DHER',
            'nome': 'Delivery Hero (tranche aporte)',
            'mkt': 'EUR',
            'lucro': -0.10,
            'lucro_pct': -0.69,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-12',
            'data_saida': '2026-06-19',
            'preco_entrada': 37.47,
            'preco_saida': 37.21,
            'volume': 0.16,
            'dias_holding': 7,
            'setup': 'Lateralizacao',
            'nota_entrada': 'aporte 12/06',
            'nota_saida': 'saida completa da posicao',
            'imagem_setup': None,
            'rating': 0
        },
        {
            'ticker': 'DHER',
            'nome': 'Delivery Hero (tranche original)',
            'mkt': 'EUR',
            'lucro': -0.77,
            'lucro_pct': -2.23,
            'tipo': 'prejuizo',
            'data_entrada': '2026-05-28',
            'data_saida': '2026-06-19',
            'preco_entrada': 38.060,
            'preco_saida': 37.21,
            'volume': 0.90,
            'dias_holding': 22,
            'setup': 'Lateralizacao',
            'nota_entrada': None,
            'nota_saida': 'saida completa da posicao',
            'imagem_setup': None,
            'rating': 0
        }
    ]
}

d['2026-06-19'] = entry

# REAL_EUR_JUN: +8.19 - 0.10 - 0.77 = +7.32
d['meses']['2026-06']['realizado_eur'] = 7.32

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-19 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], '(mercado fechado)')
print('DHER fechada total: -0.10 (aporte) + -0.77 (original) = -0.87EUR')
print('REAL_EUR_JUN: +7.32 | REAL_USD_JUN: +11.64 (inalterado)')
print('EUR equity: +7.83 (107.1% meta) | USD equity: +15.81 (53.8% meta)')
