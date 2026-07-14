import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.05,
        'caixa': 0.39,
        'lucro': 0.53,
        'positions': [
            {'name':'Allianz',    'mkt':'EUR','vol':0.095, 'abertura':410.20,'atual':421.20,'lucro':1.04, 'pct':2.67, 'trust':'v','valor':40.01,'delta':None},
            {'name':'Swiss Life', 'mkt':'EUR','vol':0.0295,'abertura':939.00,'atual':933.80,'lucro':-0.51,'pct':-1.69,'trust':'r','valor':29.65,'delta':None}
        ]
    },
    'usd': {
        'saldo': 271.91,
        'caixa': 3.04,
        'lucro': -10.11,
        'positions': [
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1,  'abertura':401.93,'atual':0.00,'lucro':1.49, 'pct':3.71, 'trust':'v','valor':41.68,'delta':None},
            {'name':'Astrana Health',      'mkt':'USD','vol':1.0,  'abertura':47.09, 'atual':0.00,'lucro':1.65, 'pct':3.50, 'trust':'v','valor':48.74,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':1.72, 'pct':2.48, 'trust':'v','valor':70.94,'delta':None},
            {'name':'Loews',                'mkt':'USD','vol':0.35, 'abertura':116.55,'atual':0.00,'lucro':-0.75,'pct':-1.84,'trust':'r','valor':40.04,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':0.00,'lucro':-0.92,'pct':-2.06,'trust':'r','valor':43.73,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05, 'abertura':298.76,'atual':0.00,'lucro':-4.81,'pct':-32.20,'trust':'r','valor':10.13,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1,  'abertura':221.00,'atual':0.00,'lucro':-8.49,'pct':-38.42,'trust':'r','valor':13.61,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'CNQ','ativo':'Canadian Natural','mkt':'USD',
         'nota':'SAIDA CNQ 0.62 @ 43.18 -- mudanca macro -- +0.55$'},
        {'tipo':'entrada','ticker':'L','ativo':'Loews','mkt':'USD',
         'nota':'ENTRADA L 0.35 @ 116.55 -- Momento Macro'},
        {'tipo':'diario','nota':'Nota: dias 11,12,14,15,16/07 sem screenshot/registo individual (gap no pipeline). Composicao da carteira entre o fecho do dia 13 (ultimo commit valido) e hoje manteve-se identica, excepto as 2 operacoes de hoje (CNQ saida, Loews entrada) -- sem impacto nos realizados desses dias.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'CNQ', 'nome': 'Canadian Natural', 'mkt': 'USD',
            'lucro': 0.55, 'lucro_pct': 2.08, 'tipo': 'lucro',
            'data_entrada': '2026-07-08', 'data_saida': '2026-07-17',
            'preco_entrada': 42.30, 'preco_saida': 43.18, 'volume': 0.62,
            'dias_holding': 9, 'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA CNQ Ajuste Macro', 'nota_saida': 'mudanca macro',
            'imagem_setup': None, 'rating': 1
        }
    ]
}

d['2026-07-17'] = entry

# REAL_EUR_JUL: -0.56 (inalterado, sem saidas EUR desde dia 13)
# REAL_USD_JUL: -4.67 + 0.55 = -4.12
d['meses']['2026-07']['realizado_usd'] = -4.12

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-17 criado OK (construido sobre o ultimo dia commitado: 2026-07-13)')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('CNQ saida: +0.55$ @ 43.18 (9 dias, +2.08%, 1 estrela) | Loews entrada: 0.35@116.55')
print('caixa USD: 17.06+26.77-40.79=3.04 checkOK')
print('REAL_EUR_JUL: -0.56 (inalterado desde dia 13) | REAL_USD_JUL: -4.12')
print('EUR equity: -0.03 (-0.4% meta) | USD equity: -14.23 (-48.4% meta)')
print('Gap dias 11,12,14,15,16 sem registo individual -- sem impacto nos realizados (carteira identica)')
