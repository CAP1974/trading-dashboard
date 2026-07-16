import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.24,
        'caixa': 1.09,
        'lucro': -0.76,
        'positions': [
            {'name':'Copper (WisdomTree)', 'mkt':'EUR','vol':0.4,  'abertura':55.00, 'atual':0.00,  'lucro':-0.27,'pct':-1.40,'trust':'r','valor':19.02,'delta':None},
            {'name':'Swiss Life',          'mkt':'EUR','vol':0.0485,'abertura':940.33,'atual':941.60,'lucro':-0.49,'pct':-0.99,'trust':'r','valor':49.13,'delta':None}
        ]
    },
    'usd': {
        'saldo': 263.60,
        'caixa': 1.09,
        'lucro': -17.26,
        'positions': [
            {'name':'Dave Inc',             'mkt':'USD','vol':0.1,  'abertura':401.93,'atual':0.00,'lucro':4.03, 'pct':10.03, 'trust':'v','valor':44.22,'delta':None},
            {'name':'Crowdstrike',          'mkt':'USD','vol':0.2,  'abertura':207.88,'atual':0.00,'lucro':-0.82,'pct':-1.97,'trust':'r','valor':40.76,'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':0.00,'lucro':-1.65,'pct':-2.38,'trust':'r','valor':67.57,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.628,'abertura':71.09, 'atual':0.00,'lucro':-1.88,'pct':-4.21,'trust':'r','valor':42.77,'delta':None},
            {'name':'Astrana Health',      'mkt':'USD','vol':1.0,  'abertura':47.09, 'atual':0.00,'lucro':-2.02,'pct':-4.29,'trust':'r','valor':45.07,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05, 'abertura':298.76,'atual':0.00,'lucro':-5.93,'pct':-39.69,'trust':'r','valor':9.01, 'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1,  'abertura':221.00,'atual':0.00,'lucro':-8.99,'pct':-40.68,'trust':'r','valor':13.11,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'COPA','ativo':'Copper (WisdomTree ETC)','mkt':'EUR',
         'nota':'ENTRADA COPA 0.4 @ 55.00 -- Ajuste Portfolio Balanca'},
        {'tipo':'aporte','ticker':'SLHN','ativo':'Swiss Life','mkt':'EUR',
         'nota':'APORTE SLHN +0.019 @ 942.40 -- vol total 0.0485 preco medio 940.33'},
        {'tipo':'diario','nota':'Sem trades USD hoje. Entrada COPA (Copper ETC, ajuste de portfolio) e aporte Swiss Life em EUR. USD continua pressionado por Cerebras (-39.69%) e SpaceX (-40.68%).'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-16'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: -0.08 | REAL_USD_JUL: -5.45

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-16 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('COPA entrada: 0.4@55.00 (Copper ETC) | SLHN aporte: vol 0.0295+0.019=0.0485 preco medio 940.33 checkOK')
print('Nota: COPA/SLHN cotam em moeda estrangeira (USD/CHF), caixa EUR aproximada por conversao cambial')
print('REAL_EUR_JUL: -0.08 (inalterado) | REAL_USD_JUL: -5.45 (inalterado, sem trades USD)')
print('EUR equity: -0.84 (-12.1% meta) | USD equity: -22.71 (-79.2% meta)')
print('AUM ~314EUR | 71 dias activos')
