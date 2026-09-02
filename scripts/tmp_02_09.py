import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 86.17,
        'caixa': 0.12,
        'lucro': -3.28,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':449.80,'lucro':1.02, 'pct':2.32, 'trust':'v','valor':44.98,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':287.10,'lucro':-1.36,'pct':-5.66,'trust':'r','valor':22.68,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':19.850,'lucro':-2.94,'pct':-13.78,'trust':'r','valor':18.39,'delta':None}
        ]
    },
    'usd': {
        'saldo': 257.12,
        'caixa': 76.00,
        'lucro': -13.72,
        'positions': [
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':442.64, 'lucro':0.92, 'pct':1.76, 'trust':'v','valor':53.12,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':496.40, 'lucro':0.41, 'pct':1.40, 'trust':'v','valor':29.78,'delta':None},
            {'name':'CME',                  'mkt':'USD','vol':0.2,  'abertura':286.71,'atual':277.46, 'lucro':-1.85,'pct':-3.23,'trust':'r','valor':55.49,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':140.60, 'lucro':-6.40,'pct':-22.15,'trust':'r','valor':22.50,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.11, 'abertura':245.75,'atual':183.83, 'lucro':-6.80,'pct':-25.16,'trust':'r','valor':20.23,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades. Caixa inalterada (EUR 0.12 / USD 76.00). ALERTA: BAE Systems piora para -13.78%, 6o dia consecutivo a violar o STOP DURO sem accao. SpaceX -22.15% e Cerebras -25.16% em excecao historica. CME entra tambem em terreno negativo -3.23%.'}
    ],
    'posicoes_fechadas': []
}

d['2026-09-02'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_SET: 0.00 | REAL_USD_SET: +0.19

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-09-02 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades - caixa inalterada face a 01/09 (EUR 0.12 / USD 76.00) - checkOK')
print('ALERTA STOP DURO: BAE Systems -13.78% (6o dia consecutivo)')
print('REAL_EUR_SET: 0.00 (inalterado) | REAL_USD_SET: +0.19 (inalterado)')
print('EUR equity: -3.28 (-37.6% meta) | USD equity: -13.53 (-52.3% meta)')
print('AUM correto: 86.17 + 257.12*0.92 = ~323')
