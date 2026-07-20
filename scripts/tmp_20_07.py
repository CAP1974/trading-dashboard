import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.24,
        'caixa': 1.09,
        'lucro': -0.76,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':54.54, 'lucro':-0.28,'pct':-1.45,'trust':'r','valor':19.01,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':941.60,'lucro':-0.48,'pct':-0.97,'trust':'r','valor':49.14,'delta':None}
        ]
    },
    'usd': {
        'saldo': 261.56,
        'caixa': 1.73,
        'lucro': -16.29,
        'positions': [
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1,  'abertura':401.93,'atual':435.77,'lucro':3.39, 'pct':8.43, 'trust':'v','valor':43.58,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':396.25,'lucro':0.13, 'pct':0.19, 'trust':'v','valor':69.35,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':70.16, 'lucro':-0.59,'pct':-1.32,'trust':'r','valor':44.06,'delta':None},
            {'name':'Apple',                'mkt':'USD','vol':0.13, 'abertura':334.12,'atual':326.50,'lucro':-0.99,'pct':-2.28,'trust':'r','valor':42.45,'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.2,  'abertura':207.88,'atual':198.28,'lucro':-1.92,'pct':-4.62,'trust':'r','valor':39.66,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05, 'abertura':298.76,'atual':175.29,'lucro':-6.18,'pct':-41.37,'trust':'r','valor':8.76, 'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1,  'abertura':221.00,'atual':119.65,'lucro':-10.13,'pct':-45.84,'trust':'r','valor':11.97,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Copper e Swiss Life ambas ligeiramente negativas. USD: Dave Inc forte (+8.43%), Cerebras e SpaceX continuam a piorar (-41.37% e -45.84%).'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-20'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: -0.08 | REAL_USD_JUL: -8.46

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-20 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 1.09 | USD 1.73)')
print('EUR equity: -0.84 (-12.1% meta) | USD equity: -24.75 (-86.3% meta)')
print('AUM ~313EUR | 73 dias activos')
