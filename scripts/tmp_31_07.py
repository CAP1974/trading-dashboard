import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.87,
        'caixa': 1.09,
        'lucro': -0.13,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':55.82, 'lucro':0.02, 'pct':0.10, 'trust':'v','valor':19.31,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':953.80,'lucro':-0.15,'pct':-0.30,'trust':'r','valor':49.47,'delta':None}
        ]
    },
    'usd': {
        'saldo': 250.40,
        'caixa': 117.80,
        'lucro': -15.79,
        'positions': [
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':47.65, 'lucro':0.77, 'pct':1.46, 'trust':'v','valor':53.37,'delta':None},
            {'name':'MetLife',              'mkt':'USD','vol':0.5,  'abertura':95.32, 'atual':96.10, 'lucro':0.39, 'pct':0.82, 'trust':'v','valor':48.05,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':198.20, 'lucro':-5.36,'pct':-27.87,'trust':'r','valor':13.87,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':108.23, 'lucro':-11.59,'pct':-40.10,'trust':'r','valor':17.31,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'JNJ','ativo':'J&J','mkt':'USD',
         'nota':'SAIDA JNJ 0.045 @ 257.66 -- quebra ema21 -- -0.22$'},
        {'tipo':'saida','ticker':'LLY','ativo':'Eli Lilly','mkt':'USD',
         'nota':'SAIDA LLY 0.04 @ 1124.13 -- quebra ema21 -- -3.97$'},
        {'tipo':'saida','ticker':'TRV','ativo':'Travelers','mkt':'USD',
         'nota':'SAIDA TRV 0.1 @ 376.42 -- quebra WMS -- -1.14$'},
        {'tipo':'aporte','ticker':'SPCX','ativo':'SpaceX','mkt':'USD',
         'nota':'APORTE SPCX +0.01 @ 108.96 -- vol total 0.16 preco medio 180.59'},
        {'tipo':'diario','nota':'Fecho do mes. Ajustes de metricas na app (novos pines, ajustes na base WMS). Fora os 2 ativos IPO (Cerebras/SpaceX), os ajustes estao a resultar num mes de forte quebra do mercado USA. Saidas JNJ, LLY e TRV por quebra ema21/WMS.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'JNJ', 'nome': 'J&J', 'mkt': 'USD',
            'lucro': -0.22, 'lucro_pct': -1.83, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-24', 'data_saida': '2026-07-31',
            'preco_entrada': 262.46, 'preco_saida': 257.66, 'volume': 0.045,
            'dias_holding': 7, 'setup': 'Pullback 4/5',
            'nota_entrada': 'ENTRADA JNJ Pullback 4/5', 'nota_saida': 'quebra ema21',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'LLY', 'nome': 'Eli Lilly', 'mkt': 'USD',
            'lucro': -3.97, 'lucro_pct': -8.12, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-28', 'data_saida': '2026-07-31',
            'preco_entrada': 1223.54, 'preco_saida': 1124.13, 'volume': 0.04,
            'dias_holding': 3, 'setup': 'WMS 84+',
            'nota_entrada': 'ENTRADA LLY WMS 84+', 'nota_saida': 'quebra ema21',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'TRV', 'nome': 'Travelers', 'mkt': 'USD',
            'lucro': -1.14, 'lucro_pct': -2.94, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-24', 'data_saida': '2026-07-31',
            'preco_entrada': 387.77, 'preco_saida': 376.42, 'volume': 0.1,
            'dias_holding': 7, 'setup': 'Clean Trend',
            'nota_entrada': 'ENTRADA TRV Clean Trend', 'nota_saida': 'quebra WMS',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-31'] = entry

# REAL_EUR_JUL: -0.08 (inalterado)
# REAL_USD_JUL: -14.78 - 0.22 - 3.97 - 1.14 = -20.11
d['meses']['2026-07']['realizado_usd'] = -20.11

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-31 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('JNJ -0.22 | LLY -3.97 | TRV -1.14 = -5.33 total | SPCX aporte 0.01@108.96')
print('caixa: 24.69+94.20-1.09=117.80 checkOK')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -20.11')
print('EUR equity: -0.21 (-3.0% meta) | USD equity: -35.90 (-125.1% meta)')
print('AUM ~410EUR | 82 dias activos')
