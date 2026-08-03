import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.78,
        'caixa': 1.09,
        'lucro': -0.22,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':55.94, 'lucro':0.06, 'pct':0.31, 'trust':'v','valor':19.35,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':954.00,'lucro':-0.28,'pct':-0.56,'trust':'r','valor':49.34,'delta':None}
        ]
    },
    'usd': {
        'saldo': 251.60,
        'caixa': 103.53,
        'lucro': -14.99,
        'positions': [
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':62.48,  'lucro':0.15, 'pct':0.24, 'trust':'v','valor':62.48,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':46.38,  'lucro':-0.65,'pct':-1.24,'trust':'r','valor':51.95,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':218.64, 'lucro':-3.93,'pct':-20.44,'trust':'r','valor':15.30,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':114.61, 'lucro':-10.56,'pct':-36.54,'trust':'r','valor':18.34,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'MET','ativo':'MetLife','mkt':'USD',
         'nota':'SAIDA MET 0.5 @ 96.11 -- Earnings 3 Sessoes -- +0.40$'},
        {'tipo':'entrada','ticker':'BAC','ativo':'Bank of America','mkt':'USD',
         'nota':'ENTRADA BAC 1 @ 62.33 -- VCP'},
        {'tipo':'diario','nota':'Primeira sessao de Agosto. Saida MetLife apos earnings (+0.40$). Entrada Bank of America (VCP). Cerebras -20.44% e SpaceX -36.54% continuam pesados.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'MET', 'nome': 'MetLife', 'mkt': 'USD',
            'lucro': 0.40, 'lucro_pct': 0.84, 'tipo': 'lucro',
            'data_entrada': '2026-07-27', 'data_saida': '2026-08-03',
            'preco_entrada': 95.32, 'preco_saida': 96.11, 'volume': 0.5,
            'dias_holding': 7, 'setup': 'WMS A+',
            'nota_entrada': 'ENTRADA MET WMS A+', 'nota_saida': 'Earnings 3 Sessoes',
            'imagem_setup': None, 'rating': 1
        }
    ]
}

d['2026-08-03'] = entry

# REAL_EUR_AGO: 0.00 (sem saidas EUR)
# REAL_USD_AGO: 0.00 + 0.40 = 0.40
d['meses']['2026-08']['realizado_usd'] = 0.40

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-03 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('MET saida: +0.40$ @ 96.11 (7 dias, +0.84%, 1 estrela)')
print('BAC entrada: 1@62.33')
print('caixa: 117.80+48.06-62.33=103.53 checkOK')
print('REAL_EUR_AGO: +0.00 | REAL_USD_AGO: +0.40')
print('EUR equity: -0.22 (-3.1% meta) | USD equity: -14.59 (-58.3% meta)')
print('AUM ~398EUR | 83 dias activos')
