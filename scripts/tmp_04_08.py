import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.39,
        'caixa': 1.09,
        'lucro': 0.39,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':57.16, 'lucro':0.46, 'pct':2.38, 'trust':'v','valor':19.75,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':957.60,'lucro':-0.07,'pct':-0.14,'trust':'r','valor':49.55,'delta':None}
        ]
    },
    'usd': {
        'saldo': 253.71,
        'caixa': 154.91,
        'lucro': -11.66,
        'positions': [
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':62.91, 'lucro':0.58, 'pct':0.93, 'trust':'v','valor':62.91,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':225.04, 'lucro':-3.48,'pct':-18.10,'trust':'r','valor':15.75,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':125.87, 'lucro':-8.76,'pct':-30.31,'trust':'r','valor':20.14,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'CNQ','ativo':'Canadian Natural','mkt':'USD',
         'nota':'SAIDA CNQ 0.5 @ 45.85 -- Earnings 3 sessoes -- -0.54$ (tranche 1/3)'},
        {'tipo':'saida','ticker':'CNQ','ativo':'Canadian Natural','mkt':'USD',
         'nota':'SAIDA CNQ 0.5 @ 45.85 -- Earnings 3 sessoes -- -0.56$ (tranche 2/3)'},
        {'tipo':'saida','ticker':'CNQ','ativo':'Canadian Natural','mkt':'USD',
         'nota':'SAIDA CNQ 0.12 @ 45.91 -- Earnings 3 sessoes -- -0.13$ (tranche 3/3, saida completa)'},
        {'tipo':'diario','nota':'Canadian Natural fechada por completo (3 tranches, earnings 3 sessoes). Cerebras -18.10% e SpaceX -30.31% continuam a pesar.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'CNQ', 'nome': 'Canadian Natural (tranche 1/3)', 'mkt': 'USD',
            'lucro': -0.54, 'lucro_pct': -2.32, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-23', 'data_saida': '2026-08-04',
            'preco_entrada': 46.94, 'preco_saida': 45.85, 'volume': 0.5,
            'dias_holding': 12, 'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA CNRL nao registada, confirmada pela caixa (23/07)', 'nota_saida': 'Earnings 3 sessoes',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'CNQ', 'nome': 'Canadian Natural (tranche 2/3)', 'mkt': 'USD',
            'lucro': -0.56, 'lucro_pct': -1.19, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-23', 'data_saida': '2026-08-04',
            'preco_entrada': 46.99, 'preco_saida': 45.85, 'volume': 0.5,
            'dias_holding': 12, 'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA CNRL nao registada, confirmada pela caixa (23/07)', 'nota_saida': 'Earnings 3 sessoes',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'CNQ', 'nome': 'Canadian Natural (tranche 3/3)', 'mkt': 'USD',
            'lucro': -0.13, 'lucro_pct': -2.30, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-23', 'data_saida': '2026-08-04',
            'preco_entrada': 46.99, 'preco_saida': 45.91, 'volume': 0.12,
            'dias_holding': 12, 'setup': 'Ajuste Macro',
            'nota_entrada': 'ENTRADA CNRL nao registada, confirmada pela caixa (23/07)', 'nota_saida': 'Earnings 3 sessoes -- saida completa',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-08-04'] = entry

# REAL_EUR_AGO: 0.00 (inalterado)
# REAL_USD_AGO: 0.40 - 0.54 - 0.56 - 0.13 = -0.83
d['meses']['2026-08']['realizado_usd'] = -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-04 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('CNQ fechada completa (3 tranches): -0.54-0.56-0.13=-1.23 total')
print('caixa: 103.53+51.36=154.89 vs 154.91 informado (diferenca minima)')
print('REAL_EUR_AGO: +0.00 (inalterado) | REAL_USD_AGO: -0.83')
print('EUR equity: +0.39 (5.6% meta) | USD equity: -12.49 (-49.9% meta)')
print('AUM ~447EUR | 84 dias activos')
