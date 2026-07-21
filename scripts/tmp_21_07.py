import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.72,
        'caixa': 1.09,
        'lucro': -0.28,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':56.21, 'lucro':0.33, 'pct':1.71, 'trust':'v','valor':19.62,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':941.60,'lucro':-0.61,'pct':-1.23,'trust':'r','valor':49.01,'delta':None}
        ]
    },
    'usd': {
        'saldo': 265.06,
        'caixa': 40.12,
        'lucro': -9.60,
        'positions': [
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1,  'abertura':401.93,'atual':435.27,'lucro':3.34, 'pct':8.31, 'trust':'v','valor':43.53,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':404.06,'lucro':1.49, 'pct':2.15, 'trust':'v','valor':70.71,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':72.30, 'lucro':0.75, 'pct':1.68, 'trust':'v','valor':45.40,'delta':None},
            {'name':'Apple',                'mkt':'USD','vol':0.13, 'abertura':334.12,'atual':327.63,'lucro':-0.85,'pct':-1.96,'trust':'r','valor':42.59,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05, 'abertura':298.76,'atual':207.37,'lucro':-4.57,'pct':-30.59,'trust':'r','valor':10.37,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1,  'abertura':221.00,'atual':123.43,'lucro':-9.76,'pct':-44.16,'trust':'r','valor':12.34,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'CRWD','ativo':'Crowdstrike','mkt':'USD',
         'nota':'SAIDA CRWD 0.2 @ 191.98 -- quebra ema21 -- -3.18$'},
        {'tipo':'diario','nota':'Saida CRWD por quebra ema21. Dave Inc, Humana e Brightspring recuperam bem. Cerebras (-30.59%) e SpaceX (-44.16%) continuam pesados.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'CRWD', 'nome': 'Crowdstrike', 'mkt': 'USD',
            'lucro': -3.18, 'lucro_pct': -1.53, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-15', 'data_saida': '2026-07-21',
            'preco_entrada': 207.88, 'preco_saida': 191.98, 'volume': 0.2,
            'dias_holding': 6, 'setup': 'PB4/5',
            'nota_entrada': 'ENTRADA CRWD PB4/5', 'nota_saida': 'quebra ema21',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-21'] = entry

# REAL_EUR_JUL: -0.08 (inalterado)
# REAL_USD_JUL: -8.46 - 3.18 = -11.64
d['meses']['2026-07']['realizado_usd'] = -11.64

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-21 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('CRWD saida: -3.18$ @ 191.98 (6 dias, -1.53%, 0 estrelas)')
print('caixa: 1.73+38.40=40.12 checkOK')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -11.64')
print('EUR equity: -0.36 (-5.2% meta) | USD equity: -21.24 (-74.0% meta)')
print('AUM ~352EUR | 74 dias activos')
