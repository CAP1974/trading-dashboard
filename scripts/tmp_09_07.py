import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 70.68,
        'caixa': 1.83,
        # eventos_09_07.txt reportou CAIXA 0.60EUR, mas screenshot mostra 1.83EUR (sem eventos EUR hoje, valor deve manter-se)
        # confirmado com o utilizador: usar 1.83EUR
        'lucro': 0.60,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':421.90,'lucro':1.11, 'pct':2.85, 'trust':'v','valor':40.08,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.770,'lucro':-0.51,'pct':-1.74,'trust':'r','valor':28.77,'delta':None}
        ]
    },
    'usd': {
        'saldo': 268.22,
        'caixa': 0.03,
        'lucro': -14.79,
        'positions': [
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.128,'abertura':70.70, 'atual':71.60, 'lucro':0.11, 'pct':1.22, 'trust':'v','valor':9.16, 'delta':None},
            {'name':'Humana',              'mkt':'USD','vol':0.175,'abertura':395.53,'atual':396.77,'lucro':0.22, 'pct':0.32, 'trust':'v','valor':69.44,'delta':None},
            {'name':'Canadian Natural',    'mkt':'USD','vol':0.62,'abertura':42.30, 'atual':41.88, 'lucro':-0.26,'pct':-0.99,'trust':'r','valor':25.97,'delta':None},
            {'name':'Astrana Health',      'mkt':'USD','vol':1.0, 'abertura':47.09, 'atual':46.48, 'lucro':-0.61,'pct':-1.30,'trust':'r','valor':46.48,'delta':None},
            {'name':'Seadrill',            'mkt':'USD','vol':1.0, 'abertura':40.65, 'atual':39.74, 'lucro':-0.91,'pct':-2.24,'trust':'r','valor':39.74,'delta':None},
            {'name':'Occidental',          'mkt':'USD','vol':1.0, 'abertura':53.70, 'atual':52.26, 'lucro':-1.44,'pct':-2.68,'trust':'r','valor':52.26,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':152.15,'lucro':-6.88,'pct':-31.13,'trust':'r','valor':15.22,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':198.40,'lucro':-5.02,'pct':-33.60,'trust':'r','valor':9.92, 'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem entradas/saidas hoje. EUR: Allianz +2.85%, Poste Italiane -1.74%. USD: BTSG e Humana positivos, resto negativo. Caixa EUR confirmada em 1.83EUR (eventos reportou 0.60 por erro).'}
    ],
    'posicoes_fechadas': []
}

d['2026-07-09'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUL: +0.00 | REAL_USD_JUL: -3.14

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-07-09 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Caixa EUR: confirmado 1.83 (eventos reportou 0.60 por erro de transcricao)')
print('EUR equity: +0.60 (8.4% meta) | USD equity: -17.93 (-61.0% meta)')
print('AUM ~319EUR | 66 dias activos')
