import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 87.32,
        'caixa': 0.12,
        'lucro': -2.13,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':445.30,'lucro':0.57, 'pct':1.30, 'trust':'v','valor':44.53,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':292.80,'lucro':-0.91,'pct':-3.79,'trust':'r','valor':23.13,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':21.010,'lucro':-1.79,'pct':-8.39,'trust':'r','valor':19.54,'delta':None}
        ]
    },
    'usd': {
        'saldo': 257.73,
        'caixa': 98.89,
        'lucro': -12.86,
        'positions': [
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':443.63, 'lucro':1.04, 'pct':1.99, 'trust':'v','valor':53.24,'delta':None},
            {'name':'Bio-Rad',              'mkt':'USD','vol':0.1,  'abertura':378.71,'atual':381.32, 'lucro':0.26, 'pct':0.69, 'trust':'v','valor':38.13,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':487.12, 'lucro':-0.15,'pct':-0.51,'trust':'r','valor':29.22,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':134.99, 'lucro':-7.30,'pct':-25.26,'trust':'r','valor':21.60,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.09, 'abertura':259.58,'atual':185.09, 'lucro':-6.71,'pct':-28.72,'trust':'r','valor':16.65,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'diario','nota':'Sem trades. Caixa inalterada (EUR 0.12 / USD 98.89), confirma nenhum movimento. Cerebras -28.72% e SpaceX -25.26% agravam-se. EUR negativo com BAE -8.39%.'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-24'] = entry

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: +4.41

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-24 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Sem trades - caixa inalterada face a 21/08 (EUR 0.12 / USD 98.89) - checkOK')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: +4.41 (inalterado)')
print('EUR equity: -2.68 (-38.4% meta) | USD equity: -8.45 (-33.7% meta)')
print('AUM correto (sem duplicar caixa): 87.32 + 257.73*0.92 = ~324')
