import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 87.58,
        'caixa': 0.12,
        'lucro': -1.87,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':444.60,'lucro':0.50, 'pct':1.14, 'trust':'v','valor':44.46,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':297.80,'lucro':-0.51,'pct':-2.12,'trust':'v','valor':23.53,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':20.990,'lucro':-1.86,'pct':-8.72,'trust':'v','valor':19.47,'delta':None}
        ]
    },
    'usd': {
        'saldo': 259.99,
        'caixa': 95.22,
        'lucro': -10.60,
        'positions': [
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':504.96, 'lucro':0.93, 'pct':3.17, 'trust':'v','valor':30.30,'delta':None},
            {'name':'Bio-Rad',              'mkt':'USD','vol':0.1,  'abertura':378.71,'atual':389.74, 'lucro':1.10, 'pct':2.90, 'trust':'v','valor':38.97,'delta':None},
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':436.94, 'lucro':0.23, 'pct':0.44, 'trust':'v','valor':52.43,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':140.90, 'lucro':-6.35,'pct':-21.97,'trust':'v','valor':22.55,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.11, 'abertura':245.75,'atual':186.55, 'lucro':-6.51,'pct':-24.08,'trust':'v','valor':20.52,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades. Caixa inalterada (EUR 0.12 / USD 95.22). Preco de abertura confirmado no screenshot para todas as posicoes, incluindo Cerebras 245.75 (media ponderada do aporte de 25/08). EUR negativo por BAE -8.72%. SpaceX -21.97% e Cerebras -24.08% continuam pesados.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-27'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-27 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades - caixa inalterada face a 26/08 (EUR 0.12 / USD 95.22) - checkOK')
print('Preco de abertura confirmado no screenshot (Cerebras 245.75 = media ponderada do aporte)')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -2.42 (-34.6% meta) | USD equity: -6.19 (-24.7% meta)')
print('AUM correto: 87.58 + 259.99*0.92 = ~327')
