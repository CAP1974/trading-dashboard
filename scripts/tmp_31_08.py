import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 87.28,
        'caixa': 0.12,
        'lucro': -2.17,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':449.00,'lucro':0.94, 'pct':2.14, 'trust':'v','valor':44.90,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':296.10,'lucro':-0.64,'pct':-2.66,'trust':'v','valor':23.40,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':20.310,'lucro':-2.47,'pct':-11.58,'trust':'r','valor':18.86,'delta':None}
        ]
    },
    'usd': {
        'saldo': 258.51,
        'caixa': 37.88,
        'lucro': -12.08,
        'positions': [
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':507.32, 'lucro':1.07, 'pct':3.64, 'trust':'v','valor':30.44,'delta':None},
            {'name':'Bio-Rad',              'mkt':'USD','vol':0.1,  'abertura':378.71,'atual':384.23, 'lucro':0.55, 'pct':1.45, 'trust':'v','valor':38.42,'delta':None},
            {'name':'CME',                  'mkt':'USD','vol':0.2,  'abertura':286.71,'atual':285.46, 'lucro':-0.25,'pct':-0.44,'trust':'v','valor':57.09,'delta':None},
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':429.64, 'lucro':-0.64,'pct':-1.23,'trust':'r','valor':51.56,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':143.66, 'lucro':-5.91,'pct':-20.45,'trust':'r','valor':22.99,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.11, 'abertura':245.75,'atual':182.92, 'lucro':-6.90,'pct':-25.53,'trust':'r','valor':20.13,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'CME','ativo':'Cme','mkt':'USD',
         'nota':'ENTRADA CME 0.2 @ 286.71'},
        {'tipo':'diario','nota':'Nova entrada CME. Caixa USD confere: 95.22-0.2*286.71=37.88. BAE Systems continua a violar STOP DURO (-11.58%, sem accao desde 28/08). SpaceX -20.45% e Cerebras -25.53% em excecao historica. EUR positivo em Allianz +2.14%.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-31'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-31 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('CME entrada: vol 0.2@286.71 -- caixa 95.22-57.34=37.88 checkOK')
print('ALERTA STOP DURO: BAE Systems -11.58% (ainda por resolver desde 28/08)')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -2.72 (-38.9% meta) | USD equity: -7.67 (-30.6% meta)')
print('AUM correto: 87.28 + 258.51*0.92 = ~325')
