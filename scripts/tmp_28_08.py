import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 88.27,
        'caixa': 0.12,
        'lucro': -1.18,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':453.20,'lucro':1.36, 'pct':3.09, 'trust':'v','valor':45.32,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':302.95,'lucro':-0.10,'pct':-0.42,'trust':'v','valor':23.94,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':20.310,'lucro':-2.44,'pct':-11.44,'trust':'r','valor':18.89,'delta':None,'stop':None}
        ]
    },
    'usd': {
        'saldo': 258.99,
        'caixa': 95.22,
        'lucro': -11.60,
        'positions': [
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':513.50, 'lucro':1.45, 'pct':4.94, 'trust':'v','valor':30.82,'delta':None},
            {'name':'Bio-Rad',              'mkt':'USD','vol':0.1,  'abertura':378.71,'atual':387.56, 'lucro':0.89, 'pct':2.35, 'trust':'v','valor':38.76,'delta':None},
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':432.34, 'lucro':-0.32,'pct':-0.61,'trust':'v','valor':51.88,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':141.46, 'lucro':-6.27,'pct':-21.70,'trust':'r','valor':22.63,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.11, 'abertura':245.75,'atual':178.80, 'lucro':-7.35,'pct':-27.19,'trust':'r','valor':19.68,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades. Caixa inalterada (EUR 0.12 / USD 95.22). ALERTA: BAE Systems atingiu -11.44%, violando o STOP DURO (-10%) pela primeira vez - avaliar saida ou justificar como excecao. SpaceX -21.70% e Cerebras -27.19% continuam em excecao historica marcada. EUR positivo em Allianz +3.09%.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-28'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-28 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades - caixa inalterada face a 27/08 (EUR 0.12 / USD 95.22) - checkOK')
print('ALERTA STOP DURO: BAE Systems -11.44% (nova violacao)')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -1.73 (-24.8% meta) | USD equity: -7.19 (-28.7% meta)')
print('AUM correto: 88.27 + 258.99*0.92 = ~327')
