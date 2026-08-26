import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 88.39,
        'caixa': 0.12,
        'lucro': -1.06,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':451.90,'lucro':1.23, 'pct':2.80, 'trust':'v','valor':45.19,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':299.25,'lucro':-0.39,'pct':-1.62,'trust':'v','valor':23.65,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':20.930,'lucro':-1.90,'pct':-8.91,'trust':'r','valor':19.43,'delta':None}
        ]
    },
    'usd': {
        'saldo': 259.04,
        'caixa': 95.22,
        'lucro': -11.55,
        'positions': [
            {'name':'Bio-Rad',              'mkt':'USD','vol':0.1,  'abertura':378.71,'atual':388.69, 'lucro':1.00, 'pct':2.64, 'trust':'v','valor':38.87,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':496.19, 'lucro':0.41, 'pct':1.40, 'trust':'v','valor':29.78,'delta':None},
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':440.14, 'lucro':0.62, 'pct':1.19, 'trust':'v','valor':52.82,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':139.53, 'lucro':-6.57,'pct':-22.73,'trust':'r','valor':22.33,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.11, 'abertura':245.75,'atual':182.04, 'lucro':-7.01,'pct':-25.93,'trust':'r','valor':20.02,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades. Caixa inalterada (EUR 0.12 / USD 95.22). EUR positivo em Allianz +2.80%, negativo no total por BAE -8.91%. SpaceX -22.73% e Cerebras -25.93% continuam pesados.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-26'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-26 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades - caixa inalterada face a 25/08 (EUR 0.12 / USD 95.22) - checkOK')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -1.61 (-23.0% meta) | USD equity: -7.14 (-28.5% meta)')
print('AUM correto: 88.39 + 259.04*0.92 = ~327')
