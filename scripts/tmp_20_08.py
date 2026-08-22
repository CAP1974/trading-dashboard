import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 87.29,
        'caixa': 0.12,
        'lucro': -2.16,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':439.10,'lucro':-0.05,'pct':-0.11,'trust':'r','valor':43.91,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':295.05,'lucro':-0.73,'pct':-3.04,'trust':'r','valor':23.31,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':21.470,'lucro':-1.38,'pct':-6.47,'trust':'r','valor':19.95,'delta':None}
        ]
    },
    'usd': {
        'saldo': 257.94,
        'caixa': 136.76,
        'lucro': -12.65,
        'positions': [
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':433.73, 'lucro':-0.15,'pct':-0.29,'trust':'r','valor':52.05,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':480.71, 'lucro':-0.53,'pct':-1.80,'trust':'r','valor':28.84,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.09, 'abertura':259.58,'atual':209.64, 'lucro':-4.50,'pct':-19.26,'trust':'r','valor':18.86,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':133.94, 'lucro':-7.47,'pct':-25.85,'trust':'r','valor':21.43,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'AMGN','ativo':'Amgen','mkt':'USD',
         'nota':'ENTRADA AMGN 0.12 @ 434.99 -- VCP'},
        {'tipo':'aporte','ticker':'CBRS','ativo':'Cerebras Systems','mkt':'USD',
         'nota':'APORTE CBRS +0.02 @ 206.62 -- vol total 0.09 preco medio 259.58'},
        {'tipo':'aporte','ticker':'MSFT','ativo':'Microsoft','mkt':'USD',
         'nota':'APORTE MSFT +0.03 @ 481.05 -- vol total 0.06 preco medio 489.51'},
        {'tipo':'diario','nota':'Nova entrada AMGN (VCP). Aportes para melhorar preco medio de Cerebras e Microsoft. Cerebras -19.26% e SpaceX -25.85% continuam pesados. EUR com dia negativo, BAE -6.47%.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-20'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-20 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('AMGN entrada 0.12@434.99 | CBRS aporte vol 0.07+0.02=0.09 preco medio 259.58')
print('MSFT aporte vol 0.03+0.03=0.06 preco medio 489.51')
print('caixa: 207.53-52.20-4.13-14.43=136.77 vs 136.76 informado (diferenca minima)')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -2.71 (-38.8% meta) | USD equity: -8.24 (-32.9% meta)')
print('AUM ~451EUR | 96 dias activos')
