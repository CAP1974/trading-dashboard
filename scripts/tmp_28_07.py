import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.02,
        'caixa': 1.09,
        'lucro': -0.98,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':54.56, 'lucro':-0.24,'pct':-1.24,'trust':'r','valor':19.05,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':943.60,'lucro':-0.74,'pct':-1.49,'trust':'r','valor':48.88,'delta':None}
        ]
    },
    'usd': {
        'saldo': 254.28,
        'caixa': 24.69,
        'lucro': -17.24,
        'positions': [
            {'name':'Travelers',            'mkt':'USD','vol':0.1,  'abertura':387.77,'atual':397.33, 'lucro':0.95, 'pct':2.45, 'trust':'v','valor':39.73,'delta':None},
            {'name':'MetLife',              'mkt':'USD','vol':0.5,  'abertura':95.32, 'atual':97.52,  'lucro':1.10, 'pct':2.31, 'trust':'v','valor':48.76,'delta':None},
            {'name':'J&J',                  'mkt':'USD','vol':0.045,'abertura':262.46,'atual':266.62, 'lucro':0.19, 'pct':1.61, 'trust':'v','valor':12.00,'delta':None},
            {'name':'Eli Lilly',            'mkt':'USD','vol':0.04, 'abertura':1223.54,'atual':1218.99,'lucro':-0.18,'pct':-0.37,'trust':'r','valor':48.76,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':44.20,  'lucro':-3.10,'pct':-5.89,'trust':'r','valor':49.50,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':191.21,  'lucro':-5.85,'pct':-30.42,'trust':'r','valor':13.38,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.15, 'abertura':185.37,'atual':116.38,  'lucro':-10.35,'pct':-37.22,'trust':'r','valor':17.46,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'HUM','ativo':'Humana','mkt':'USD',
         'nota':'SAIDA HUM 0.15 @ 382.05 -- lateralizacao/distribuicao -- -2.02$ (tranche 1/2)'},
        {'tipo':'saida','ticker':'HUM','ativo':'Humana','mkt':'USD',
         'nota':'SAIDA HUM 0.025 @ 382.05 -- lateralizacao/distribuicao -- -0.34$ (tranche 2/2, saida completa)'},
        {'tipo':'entrada','ticker':'LLY','ativo':'Eli Lilly','mkt':'USD',
         'nota':'ENTRADA LLY 0.04 @ 1223.54 -- WMS 84+'},
        {'tipo':'diario','nota':'Humana fechada por completo (2 tranches) por lateralizacao/distribuicao. Entrada Eli Lilly. Cerebras -30.42% e SpaceX -37.22% continuam pesados.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'HUM', 'nome': 'Humana (tranche 1/2)', 'mkt': 'USD',
            'lucro': -2.02, 'lucro_pct': -3.41, 'tipo': 'prejuizo',
            'data_entrada': '2026-06-29', 'data_saida': '2026-07-28',
            'preco_entrada': 395.50, 'preco_saida': 382.05, 'volume': 0.15,
            'dias_holding': 29, 'setup': 'Lateralizacao',
            'nota_entrada': 'entrada anterior (data aproximada)', 'nota_saida': 'lateralizacao/distribuicao',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'HUM', 'nome': 'Humana (tranche 2/2)', 'mkt': 'USD',
            'lucro': -0.34, 'lucro_pct': -3.45, 'tipo': 'prejuizo',
            'data_entrada': '2026-06-29', 'data_saida': '2026-07-28',
            'preco_entrada': 395.69, 'preco_saida': 382.05, 'volume': 0.025,
            'dias_holding': 29, 'setup': 'Lateralizacao',
            'nota_entrada': 'entrada anterior (data aproximada)', 'nota_saida': 'lateralizacao/distribuicao -- saida completa',
            'imagem_setup': None, 'rating': 0
        }
    ]
}

d['2026-07-28'] = entry

# REAL_EUR_JUL: -0.08 (inalterado)
# REAL_USD_JUL: -12.42 - 2.02 - 0.34 = -14.78
d['meses']['2026-07']['realizado_usd'] = -14.78

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-28 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('HUM fechada completa (2 tranches): -2.02-0.34=-2.36 total')
print('LLY entrada: 0.04@1223.54')
print('caixa: 6.77+66.86-48.94=24.69 checkOK')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -14.78')
print('EUR equity: -1.06 (-15.2% meta) | USD equity: -32.02 (-111.6% meta)')
print('AUM ~327EUR | 79 dias activos')
