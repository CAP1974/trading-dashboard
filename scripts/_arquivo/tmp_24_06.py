import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 68.00,
        'caixa': 0.89,
        'lucro': -3.20,
        'positions': [
            {'name':'ASML Holding',  'mkt':'EUR','vol':0.025,'abertura':1641.00,'atual':1554.00,'lucro':-2.18,'pct':-5.31,'trust':'r','valor':38.85,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0, 'abertura':29.280, 'atual':28.260, 'lucro':-1.02,'pct':-3.48,'trust':'r','valor':28.26,'delta':None}
        ]
    },
    'usd': {
        'saldo': 278.64,
        'caixa': 30.43,
        'lucro': -6.67,
        'positions': [
            {'name':'Veracyte',              'mkt':'USD','vol':1.7, 'abertura':53.31, 'atual':56.43, 'lucro':5.32, 'pct':5.87,  'trust':'v','valor':95.94,'delta':None},
            {'name':'Morgan Stanley',        'mkt':'USD','vol':0.2, 'abertura':214.56,'atual':220.04,'lucro':1.10, 'pct':2.56,  'trust':'v','valor':44.01,'delta':None},
            {'name':'JPMorgan Chase',        'mkt':'USD','vol':0.15,'abertura':333.45,'atual':333.40,'lucro':-0.01,'pct':-0.02, 'trust':'r','valor':50.01,'delta':None},
            {'name':'Brightspring Health',   'mkt':'USD','vol':0.5, 'abertura':68.58, 'atual':67.37, 'lucro':-0.60,'pct':-1.75, 'trust':'r','valor':33.69,'delta':None},
            {'name':'SpaceX',               'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':154.43,'lucro':-6.66,'pct':-30.14,'trust':'r','valor':15.44,'delta':None},
            {'name':'Cerebras Systems',     'mkt':'USD','vol':0.05,'abertura':298.76,'atual':182.48,'lucro':-5.82,'pct':-38.96,'trust':'r','valor':9.12, 'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'JPM','ativo':'JPMorgan Chase','mkt':'USD',
         'nota':'ENTRADA JPM 0.15 @ 333.45 -- Ajuste Macro'},
        {'tipo':'entrada','ticker':'BTSG','ativo':'Brightspring Health Services','mkt':'USD',
         'nota':'ENTRADA BTSG 0.5 @ 68.58 -- Ajuste Macro'},
        {'tipo':'diario','nota':'Ajuste carteira para mudanca macro. EUR continua em queda (ASML -5.31%). Entradas JPM e BTSG. Caixa EUR subiu para 0.89 (possivel dividendo/juro).'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-24'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_JUN: +7.32 | REAL_USD_JUN: +12.00

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-24 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('JPM entrada: 0.15@333.45 = 50.02$ | BTSG entrada: 0.5@68.58 = 34.29$')
print('caixa: 114.74 - 50.02 - 34.29 = 30.43 checkOK')
print('EUR equity: +4.12 (56.4% meta) | USD equity: +5.33 (18.1% meta)')
print('AUM ~324EUR | 55 dias activos')
print('REAL_EUR_JUN: +7.32 (inalterado) | REAL_USD_JUN: +12.00 (inalterado)')
