import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.75,
        'caixa': 1.83,
        'lucro': 0.67,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':420.50,'lucro':0.98, 'pct':2.51, 'trust':'v','valor':39.95,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.970,'lucro':-0.31,'pct':-1.06,'trust':'r','valor':28.97,'delta':None}
        ]
    },
    'usd': {
        'saldo': 279.58,
        'caixa': 1.43,
        'lucro': -10.69,
        'positions': [
            {'name':'JFrog',                'mkt':'USD','vol':1.0, 'abertura':95.40,  'atual':0.00,'lucro':2.19, 'pct':2.30,  'trust':'v','valor':97.59,'delta':None},
            {'name':'Axos Financial',      'mkt':'USD','vol':0.088,'abertura':99.09, 'atual':0.00,'lucro':0.13, 'pct':1.49,  'trust':'v','valor':8.85, 'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.14,'abertura':198.25,'atual':0.00,'lucro':0.14, 'pct':0.50,  'trust':'v','valor':27.90,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':-0.76,'pct':-1.10,'trust':'r','valor':68.46,'delta':None},
            {'name':'Apple Hospitality',   'mkt':'USD','vol':3.0, 'abertura':16.90,  'atual':0.00,'lucro':-0.99,'pct':-1.95,'trust':'r','valor':49.71,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-6.03,'pct':-27.29,'trust':'r','valor':16.07,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-5.37,'pct':-35.94,'trust':'r','valor':9.57, 'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem entradas/saidas hoje. EUR: Allianz +2.51%, Poste Italiane -1.06%. USD: JFrog, Axos e Crowdstrike positivos; Humana, APLE, SpaceX e Cerebras negativos.'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-06'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: +0.00 | REAL_USD_JUL: +4.12

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-06 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades hoje. Caixa confirmada: EUR 1.83 (igual) | USD 1.43 (era 1.38)')
print('EUR equity: +0.67 (9.4% meta) | USD equity: -6.57 (-22.4% meta)')
print('AUM ~331EUR | 63 dias activos')
