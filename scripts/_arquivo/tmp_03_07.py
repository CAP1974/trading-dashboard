import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.98,
        'caixa': 1.83,
        'lucro': 0.90,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':420.70,'lucro':1.00, 'pct':2.57, 'trust':'v','valor':39.97,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':29.180,'lucro':-0.10,'pct':-0.34,'trust':'r','valor':29.18,'delta':None}
        ]
    },
    'usd': {
        # Mercado USD fechado (4 de Julho - Independence Day) -- identico a 02/07
        'saldo': 277.56,
        'caixa': 1.38,
        'lucro': -12.66,
        'positions': [
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':0.10, 'pct':0.14,  'trust':'v','valor':69.32,'delta':None},
            {'name':'JFrog',                'mkt':'USD','vol':1.0, 'abertura':95.40,  'atual':0.00,'lucro':-0.62,'pct':-0.65,'trust':'r','valor':94.78,'delta':None},
            {'name':'Apple Hospitality',   'mkt':'USD','vol':3.0, 'abertura':16.90,  'atual':0.00,'lucro':-0.78,'pct':-1.54,'trust':'r','valor':49.92,'delta':None},
            {'name':'Axos Financial',      'mkt':'USD','vol':0.088,'abertura':99.09, 'atual':0.00,'lucro':-0.15,'pct':-1.72,'trust':'r','valor':8.57, 'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.14,'abertura':198.25,'atual':0.00,'lucro':-0.60,'pct':-2.16,'trust':'r','valor':27.16,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-5.91,'pct':-26.74,'trust':'r','valor':16.19,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-4.70,'pct':-31.46,'trust':'r','valor':10.24,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Mercado USD fechado (4 de Julho - Independence Day). EUR: Allianz +2.57%, Poste Italiane -0.34%. Caixa EUR 1.83EUR inalterada.'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-03'] = entry

# Realizados inalterados (sem saidas hoje, USD fechado)
# REAL_EUR_JUL: +0.00 | REAL_USD_JUL: +4.12

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-03 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], '(mercado fechado - Independence Day)')
print('EUR equity: +0.90 (12.6% meta) | USD equity: -8.54 (inalterado, -29.0% meta)')
print('AUM ~329EUR | 62 dias activos')
