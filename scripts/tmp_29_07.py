import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 68.45,
        'caixa': 1.09,
        'lucro': -1.55,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':54.25, 'lucro':-0.43,'pct':-2.23,'trust':'r','valor':18.86,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':938.20,'lucro':-1.12,'pct':-2.26,'trust':'r','valor':48.50,'delta':None}
        ]
    },
    'usd': {
        'saldo': 253.27,
        'caixa': 24.69,
        'lucro': -18.25,
        'positions': [
            {'name':'MetLife',              'mkt':'USD','vol':0.5,  'abertura':95.32, 'atual':96.99,  'lucro':0.84, 'pct':1.76, 'trust':'v','valor':48.50,'delta':None},
            {'name':'J&J',                  'mkt':'USD','vol':0.045,'abertura':262.46,'atual':265.73, 'lucro':0.15, 'pct':1.27, 'trust':'v','valor':11.96,'delta':None},
            {'name':'Travelers',            'mkt':'USD','vol':0.1,  'abertura':387.77,'atual':389.34, 'lucro':0.15, 'pct':0.39, 'trust':'v','valor':38.93,'delta':None},
            {'name':'Eli Lilly',            'mkt':'USD','vol':0.04, 'abertura':1223.54,'atual':1210.90,'lucro':-0.50,'pct':-1.02,'trust':'r','valor':48.44,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':46.48,  'lucro':-0.54,'pct':-1.03,'trust':'r','valor':52.06,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':169.16,  'lucro':-7.39,'pct':-38.43,'trust':'r','valor':11.84,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.15, 'abertura':185.37,'atual':112.34,  'lucro':-10.96,'pct':-39.41,'trust':'r','valor':16.85,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Copper e Swiss Life ambas negativas. USD: MetLife, J&J e Travelers positivos, mas Cerebras -38.43% e SpaceX -39.41% dominam o floating negativo.'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-29'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: -0.08 | REAL_USD_JUL: -14.78

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-29 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 1.09 | USD 24.69)')
print('EUR equity: -1.63 (-23.4% meta) | USD equity: -33.03 (-115.1% meta)')
print('AUM ~325EUR | 80 dias activos')
