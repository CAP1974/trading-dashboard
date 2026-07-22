import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.06,
        'caixa': 1.09,
        'lucro': 0.06,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':56.00, 'lucro':0.24, 'pct':1.24, 'trust':'v','valor':19.53,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':951.60,'lucro':-0.18,'pct':-0.36,'trust':'r','valor':49.44,'delta':None}
        ]
    },
    'usd': {
        'saldo': 259.80,
        'caixa': 40.12,
        'lucro': -14.86,
        'positions': [
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1,  'abertura':401.93,'atual':423.26,'lucro':2.14, 'pct':5.32, 'trust':'v','valor':42.33,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':396.35,'lucro':0.14, 'pct':0.20, 'trust':'v','valor':69.36,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':69.49, 'lucro':-1.02,'pct':-2.28,'trust':'r','valor':43.63,'delta':None},
            {'name':'Apple',                'mkt':'USD','vol':0.13, 'abertura':334.12,'atual':326.31,'lucro':-1.02,'pct':-2.35,'trust':'r','valor':42.42,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05, 'abertura':298.76,'atual':208.18,'lucro':-4.53,'pct':-30.32,'trust':'r','valor':10.41,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1,  'abertura':221.00,'atual':115.28,'lucro':-10.57,'pct':-47.83,'trust':'r','valor':11.53,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Copper +1.24%, Swiss Life -0.36%. USD: Dave Inc e Humana positivos, mas Cerebras -30.32% e SpaceX -47.83% continuam a dominar o floating negativo.'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-22'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: -0.08 | REAL_USD_JUL: -11.64

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-22 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 1.09 | USD 40.12)')
print('EUR equity: -0.02 (-0.3% meta) | USD equity: -26.50 (-92.4% meta)')
print('AUM ~347EUR | 75 dias activos')
