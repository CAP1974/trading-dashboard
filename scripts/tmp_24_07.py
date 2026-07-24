import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.21,
        'caixa': 1.09,
        'lucro': -0.79,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':54.75, 'lucro':-0.15,'pct':-0.78,'trust':'r','valor':19.14,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':944.00,'lucro':-0.64,'pct':-1.29,'trust':'r','valor':48.98,'delta':None}
        ]
    },
    'usd': {
        'saldo': 255.93,
        'caixa': 0.86,
        'lucro': -17.81,
        'positions': [
            {'name':'J&J',                  'mkt':'USD','vol':0.045,'abertura':262.46,'atual':263.41,'lucro':0.04, 'pct':0.34, 'trust':'v','valor':11.85,'delta':None},
            {'name':'Travelers',            'mkt':'USD','vol':0.1,  'abertura':387.77,'atual':387.24,'lucro':-0.06,'pct':-0.15,'trust':'r','valor':38.72,'delta':None},
            {'name':'Apple',                'mkt':'USD','vol':0.16, 'abertura':333.90,'atual':333.02,'lucro':-0.15,'pct':-0.28,'trust':'r','valor':53.28,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':46.45, 'lucro':-0.57,'pct':-1.08,'trust':'r','valor':52.03,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':388.65,'lucro':-1.20,'pct':-1.73,'trust':'r','valor':68.02,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':199.00, 'lucro':-5.30,'pct':-27.56,'trust':'r','valor':13.93,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.15, 'abertura':185.37,'atual':114.90, 'lucro':-10.57,'pct':-38.01,'trust':'r','valor':17.24,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'TRV','ativo':'Travelers','mkt':'USD',
         'nota':'ENTRADA TRV 0.1 @ 387.77 -- Clean Trend'},
        {'tipo':'entrada','ticker':'JNJ','ativo':'J&J','mkt':'USD',
         'nota':'ENTRADA JNJ 0.045 @ 262.46 -- Pullback 4/5'},
        {'tipo':'aporte','ticker':'AAPL','ativo':'Apple','mkt':'USD',
         'nota':'APORTE AAPL +0.03 @ 332.97 -- vol total 0.16 preco medio 333.90'},
        {'tipo':'diario','nota':'Entradas TRV (Clean Trend) e J&J (Pullback 4/5). Aporte AAPL para melhorar preco medio. Cerebras -27.56% e SpaceX -38.01% seguem a pesar.'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-24'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: -0.08 | REAL_USD_JUL: -12.56

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-24 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('TRV entrada 0.1@387.77 | J&J entrada 0.045@262.46 | AAPL aporte vol 0.13+0.03=0.16 preco medio 333.90')
print('caixa: 61.44-38.78-11.81-9.99=0.86 checkOK')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -12.56 (inalterado)')
print('EUR equity: -0.87 (-12.5% meta) | USD equity: -30.37 (-105.9% meta)')
print('AUM ~307EUR | 77 dias activos')
