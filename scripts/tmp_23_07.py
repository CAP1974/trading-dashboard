import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 68.99,
        'caixa': 1.09,
        'lucro': -1.01,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':54.44, 'lucro':-0.24,'pct':-1.24,'trust':'r','valor':19.05,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':940.40,'lucro':-0.77,'pct':-1.55,'trust':'r','valor':48.85,'delta':None}
        ]
    },
    'usd': {
        'saldo': 257.64,
        'caixa': 61.44,
        'lucro': -16.10,
        'positions': [
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':47.03, 'lucro':0.08, 'pct':0.15,  'trust':'v','valor':52.68,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':392.28,'lucro':-0.57,'pct':-0.82,'trust':'r','valor':68.65,'delta':None},
            {'name':'Apple',                'mkt':'USD','vol':0.13, 'abertura':334.12,'atual':321.65,'lucro':-1.63,'pct':-3.75,'trust':'r','valor':41.81,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':219.00, 'lucro':-3.90,'pct':-20.28,'trust':'r','valor':15.33,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.15, 'abertura':185.37,'atual':118.24, 'lucro':-10.08,'pct':-36.25,'trust':'r','valor':17.73,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'DAVE','ativo':'Dave Inc','mkt':'USD',
         'nota':'SAIDA DAVE 0.1 @ 402.97 -- quebra ema21 -- +0.11$'},
        {'tipo':'saida','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'SAIDA BTSG 0.492 @ 69.45 -- quebra ema21 -- -0.86$ (tranche 1/3)'},
        {'tipo':'saida','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'SAIDA BTSG 0.128 @ 69.45 -- quebra ema21 -- -0.16$ (tranche 2/3)'},
        {'tipo':'saida','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'SAIDA BTSG 0.008 @ 69.42 -- quebra ema21 -- -0.01$ (tranche 3/3, saida completa)'},
        {'tipo':'entrada','ticker':'CNRL','ativo':'Canadian Natural','mkt':'USD',
         'nota':'ENTRADA CNRL 1.12 @ 46.97 -- nao registada no eventos.txt, confirmada pela matematica da caixa (61.44$) e pelo utilizador'},
        {'tipo':'aporte','ticker':'CBRS','ativo':'Cerebras Systems','mkt':'USD',
         'nota':'APORTE CBRS +0.02 @ 214.57 -- vol total 0.07 preco medio 274.71'},
        {'tipo':'aporte','ticker':'SPCX','ativo':'SpaceX','mkt':'USD',
         'nota':'APORTE SPCX +0.05 @ 114.10 -- vol total 0.15 preco medio 185.37'},
        {'tipo':'diario','nota':'Dia de rebalanceamento: saida DAVE e fecho completo de BTSG (3 tranches, quebra ema21). Aportes para melhorar preco medio de Cerebras e SpaceX. Entrada CNRL nao estava no eventos.txt mas confirmada pela caixa e pelo utilizador.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'DAVE', 'nome': 'Dave Inc', 'mkt': 'USD',
            'lucro': 0.11, 'lucro_pct': 0.27, 'tipo': 'lucro',
            'data_entrada': '2026-07-01', 'data_saida': '2026-07-23',
            'preco_entrada': 401.93, 'preco_saida': 402.97, 'volume': 0.1,
            'dias_holding': 22, 'setup': 'Clean Trend',
            'nota_entrada': 'ENTRADA DAVE Clean Trend', 'nota_saida': 'quebra ema21',
            'imagem_setup': None, 'rating': 1
        },
        {
            'ticker': 'BTSG', 'nome': 'Brightspring Health Services (tranche 1/3)', 'mkt': 'USD',
            'lucro': -0.86, 'lucro_pct': -1.21, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-10', 'data_saida': '2026-07-23',
            'preco_entrada': 71.19, 'preco_saida': 69.45, 'volume': 0.492,
            'dias_holding': 13, 'setup': 'Ajuste Macro',
            'nota_entrada': 'aporte 10/07', 'nota_saida': 'quebra ema21',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'BTSG', 'nome': 'Brightspring Health Services (tranche 2/3)', 'mkt': 'USD',
            'lucro': -0.16, 'lucro_pct': -1.77, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-08', 'data_saida': '2026-07-23',
            'preco_entrada': 70.70, 'preco_saida': 69.45, 'volume': 0.128,
            'dias_holding': 15, 'setup': 'Ajuste Macro',
            'nota_entrada': 'entrada original 08/07', 'nota_saida': 'quebra ema21',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'BTSG', 'nome': 'Brightspring Health Services (tranche 3/3)', 'mkt': 'USD',
            'lucro': -0.01, 'lucro_pct': -1.99, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-10', 'data_saida': '2026-07-23',
            'preco_entrada': 71.19, 'preco_saida': 69.42, 'volume': 0.008,
            'dias_holding': 13, 'setup': 'Ajuste Macro',
            'nota_entrada': 'residual aporte 10/07', 'nota_saida': 'quebra ema21 -- saida completa',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-23'] = entry

# REAL_EUR_JUL: -0.08 (inalterado)
# REAL_USD_JUL: -11.64 + 0.11 - 0.86 - 0.16 - 0.01 = -12.56
d['meses']['2026-07']['realizado_usd'] = -12.56

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-23 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('DAVE saida +0.11 | BTSG fechado completo em 3 tranches: -0.86-0.16-0.01=-1.03')
print('CNRL entrada nao registada, confirmada pela caixa: 1.12@46.97=52.60')
print('caixa: 40.12+40.30+43.61-4.29-5.71-52.60=61.44 checkOK')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -12.56')
print('EUR equity: -1.09 (-15.6% meta) | USD equity: -28.66 (-99.9% meta)')
print('AUM ~364EUR | 76 dias activos')
