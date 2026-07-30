import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.51,
        'caixa': 1.09,
        'lucro': -0.49,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':55.46, 'lucro':-0.14,'pct':-0.73,'trust':'r','valor':19.15,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':947.60,'lucro':-0.35,'pct':-0.71,'trust':'r','valor':49.27,'delta':None}
        ]
    },
    'usd': {
        'saldo': 252.43,
        'caixa': 24.69,
        'lucro': -19.09,
        'positions': [
            {'name':'MetLife',              'mkt':'USD','vol':0.5,  'abertura':95.32, 'atual':97.08,  'lucro':0.88, 'pct':1.85, 'trust':'v','valor':48.54,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':1.12, 'abertura':46.97, 'atual':47.26,  'lucro':0.33, 'pct':0.63, 'trust':'v','valor':52.93,'delta':None},
            {'name':'J&J',                  'mkt':'USD','vol':0.045,'abertura':262.46,'atual':255.77, 'lucro':-0.30,'pct':-2.54,'trust':'r','valor':11.51,'delta':None},
            {'name':'Travelers',            'mkt':'USD','vol':0.1,  'abertura':387.77,'atual':375.94, 'lucro':-1.19,'pct':-3.07,'trust':'r','valor':37.59,'delta':None},
            {'name':'Eli Lilly',            'mkt':'USD','vol':0.04, 'abertura':1223.54,'atual':1155.62,'lucro':-2.72,'pct':-5.56,'trust':'r','valor':46.22,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':201.56,  'lucro':-5.12,'pct':-26.63,'trust':'r','valor':14.11,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.15, 'abertura':185.37,'atual':112.29,  'lucro':-10.97,'pct':-39.45,'trust':'r','valor':16.84,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Copper e Swiss Life ambas ligeiramente negativas. USD: MetLife e CNRL positivos, mas Cerebras -26.63% e SpaceX -39.45% continuam a pesar.'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-30'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: -0.08 | REAL_USD_JUL: -14.78

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-30 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 1.09 | USD 24.69)')
print('EUR equity: -0.57 (-8.2% meta) | USD equity: -33.87 (-118.1% meta)')
print('AUM ~326EUR | 81 dias activos')
