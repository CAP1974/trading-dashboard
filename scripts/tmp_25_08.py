import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 88.13,
        'caixa': 0.12,
        'lucro': -1.32,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':450.60,'lucro':1.10, 'pct':2.50, 'trust':'v','valor':45.06,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':296.30,'lucro':-0.63,'pct':-2.62,'trust':'v','valor':23.41,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':21.000,'lucro':-1.79,'pct':-8.39,'trust':'r','valor':19.54,'delta':None}
        ]
    },
    'usd': {
        'saldo': 258.85,
        'caixa': 95.22,
        'lucro': -11.74,
        'positions': [
            {'name':'Bio-Rad',              'mkt':'USD','vol':0.1,  'abertura':378.71,'atual':387.80, 'lucro':0.91, 'pct':2.40, 'trust':'v','valor':38.78,'delta':None},
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':442.06, 'lucro':0.85, 'pct':1.63, 'trust':'v','valor':53.05,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':491.57, 'lucro':0.13, 'pct':0.44, 'trust':'v','valor':29.50,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':137.92, 'lucro':-6.83,'pct':-23.63,'trust':'r','valor':22.07,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.11, 'abertura':245.75,'atual':183.88, 'lucro':-6.80,'pct':-25.16,'trust':'r','valor':20.23,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'aporte','ticker':'CBRS','ativo':'Cerebras Systems','mkt':'USD',
         'nota':'APORTE CBRS +0.02 @ 183.52 -- vol total 0.11 preco medio 245.75'},
        {'tipo':'diario','nota':'Aporte Cerebras para melhorar preco medio. CAIXA USD 95.22 confirmado pelo screenshot (eventos.txt indicava 0.00 por erro de preenchimento) - reconcilia com 98.89-3.67. SpaceX -23.63% e Cerebras -25.16% continuam pesados. EUR positivo em Allianz, negativo no total por BAE -8.39%.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-25'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-25 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('CBRS aporte: vol 0.09+0.02=0.11, preco medio (0.09*259.58+0.02*183.52)/0.11=245.75')
print('caixa USD: 98.89-3.67=95.22 -- confirmado pelo utilizador (eventos.txt tinha 0.00 por erro)')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -1.87 (-26.8% meta) | USD equity: -7.33 (-29.3% meta)')
print('AUM correto: 88.13 + 258.85*0.92 = ~326')
