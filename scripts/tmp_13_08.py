import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 89.19,
        'caixa': 0.12,
        'lucro': -0.26,
        'positions': [
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':309.15,'lucro':0.38, 'pct':1.58, 'trust':'v','valor':24.42,'delta':None},
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':438.10,'lucro':-0.15,'pct':-0.34,'trust':'r','valor':43.81,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':22.380,'lucro':-0.49,'pct':-2.30,'trust':'r','valor':20.84,'delta':None}
        ]
    },
    'usd': {
        'saldo': 268.15,
        'caixa': 0.36,
        'lucro': 2.79,
        'positions': [
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':394.76, 'lucro':10.41,'pct':7.46, 'trust':'v','valor':150.01,'delta':None},
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':64.10,  'lucro':1.77, 'pct':2.84, 'trust':'v','valor':64.10,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':496.42, 'lucro':-0.05,'pct':-0.33,'trust':'r','valor':14.89,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':231.30, 'lucro':-3.03,'pct':-15.76,'trust':'r','valor':16.20,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':141.24, 'lucro':-6.31,'pct':-21.83,'trust':'r','valor':22.59,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades hoje. EUR: Schneider +1.58%, Allianz -0.34%, BAE -2.30%. USD: Palo Alto muito forte +7.46%, Bank of America +2.84%, mas Cerebras -15.76% e SpaceX -21.83% ainda pesam.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-13'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-13 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades. Caixa confirmada igual a ontem (EUR 0.12 | USD 0.36)')
print('EUR equity: -0.81 (-11.6% meta) | USD equity: +1.96 (7.8% meta)')
print('AUM ~336EUR | 91 dias activos')
