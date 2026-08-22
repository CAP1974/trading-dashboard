import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 87.39,
        'caixa': 0.12,
        'lucro': -2.06,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':441.10,'lucro':0.15, 'pct':0.34, 'trust':'v','valor':44.11,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':21.260,'lucro':-1.58,'pct':-7.41,'trust':'r','valor':19.75,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':296.35,'lucro':-0.63,'pct':-2.62,'trust':'r','valor':23.41,'delta':None}
        ]
    },
    'usd': {
        'saldo': 257.91,
        'caixa': 98.89,
        'lucro': -12.68,
        'positions': [
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':439.00, 'lucro':0.48, 'pct':0.92, 'trust':'v','valor':52.68,'delta':None},
            {'name':'Bio-Rad',              'mkt':'USD','vol':0.1,  'abertura':378.71,'atual':378.59, 'lucro':-0.01,'pct':-0.03,'trust':'r','valor':37.86,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':482.99, 'lucro':-0.39,'pct':-1.33,'trust':'r','valor':28.98,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':136.88, 'lucro':-7.00,'pct':-24.22,'trust':'r','valor':21.90,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.09, 'abertura':259.58,'atual':195.63, 'lucro':-5.76,'pct':-24.66,'trust':'r','valor':17.60,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'BIO','ativo':'Bio-Rad','mkt':'USD',
         'nota':'ENTRADA BIO 0.1 @ 378.71 -- VCP'},
        {'tipo':'diario','nota':'Nova entrada Bio-Rad (VCP). Cerebras -24.66% e SpaceX -24.22% continuam pesados. EUR com dia negativo, BAE -7.41%.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-21'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-21 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('BIO entrada: 0.1@378.71')
print('caixa: 136.76-37.87=98.89 checkOK')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -2.61 (-37.4% meta) | USD equity: -8.27 (-33.0% meta)')
print('AUM ~416EUR | 97 dias activos')
