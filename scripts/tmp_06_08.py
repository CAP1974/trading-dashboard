import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.23,
        'caixa': 1.09,
        'lucro': 0.23,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':57.84, 'lucro':0.69, 'pct':3.58, 'trust':'v','valor':19.98,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':953.40,'lucro':-0.46,'pct':-0.93,'trust':'r','valor':49.16,'delta':None}
        ]
    },
    'usd': {
        'saldo': 247.12,
        'caixa': 0.36,
        'lucro': -18.24,
        'positions': [
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':62.97, 'lucro':0.64, 'pct':1.03, 'trust':'v','valor':62.97,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':499.62, 'lucro':0.05, 'pct':0.33, 'trust':'v','valor':14.99,'delta':None},
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':357.65, 'lucro':-3.68,'pct':-2.64,'trust':'r','valor':135.92,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':207.43, 'lucro':-4.71,'pct':-24.49,'trust':'r','valor':14.52,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':114.72, 'lucro':-10.54,'pct':-36.47,'trust':'r','valor':18.36,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'MSFT','ativo':'Microsoft','mkt':'USD',
         'nota':'ENTRADA MSFT 0.03 @ 497.97'},
        {'tipo':'aporte','ticker':'PANW','ativo':'Palo Alto','mkt':'USD',
         'nota':'APORTE PANW +0.10 @ 352.18 -- vol total 0.38 preco medio 367.35 (eventos.txt tinha vol:0.01, corrigido para 0.10 -- caixa e preco medio so batem certo com 0.10)'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-06'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: 0.00 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-06 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('MSFT entrada 0.03@497.97 | PANW aporte corrigido 0.10@352.18 (nao 0.01) -> vol total 0.38 preco medio 367.35')
print('caixa: 50.52-14.94-35.22=0.36 checkOK (so bate com vol 0.10)')
print('REAL_EUR_AGO: +0.00 (inalterado) | REAL_USD_AGO: -0.83 (inalterado)')
print('EUR equity: +0.23 (3.3% meta) | USD equity: -19.07 (-76.2% meta)')
print('AUM ~299EUR | 86 dias activos')
