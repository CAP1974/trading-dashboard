import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 73.12,
        'caixa': 0.37,
        'lucro': 10.42,
        'positions': [
            {'name':'Delivery Hero','mkt':'EUR','vol':1.06,'abertura':37.971,'atual':38.340,'lucro':0.39, 'pct':0.97, 'trust':'v','valor':40.64,'delta':None},
            {'name':'Infineon',     'mkt':'EUR','vol':0.4, 'abertura':54.275,'atual':79.330,'lucro':10.03,'pct':46.20,'trust':'v','valor':31.74,'delta':None}
        ]
    },
    'usd': {
        'saldo': 280.94,
        'caixa': 1.72,
        'lucro': -8.64,
        'positions': [
            {'name':'Morgan Stanley',    'mkt':'USD','vol':0.2,  'abertura':214.56, 'atual':220.69, 'lucro':1.22, 'pct':2.84,  'trust':'v','valor':44.13,'delta':None},
            {'name':'Humana',            'mkt':'USD','vol':0.1,  'abertura':360.54, 'atual':369.51, 'lucro':0.90, 'pct':2.50,  'trust':'v','valor':36.95,'delta':None},
            {'name':'Apple Hospitality', 'mkt':'USD','vol':1.9,  'abertura':16.25,  'atual':16.36,  'lucro':0.20, 'pct':0.65,  'trust':'v','valor':31.08,'delta':None},
            {'name':'Eli Lilly',         'mkt':'USD','vol':0.027,'abertura':1148.55,'atual':1122.08,'lucro':-0.71,'pct':-2.29, 'trust':'r','valor':30.30,'delta':None},
            {'name':'Royalty Pharma',    'mkt':'USD','vol':0.5,  'abertura':55.60,  'atual':54.05,  'lucro':-0.77,'pct':-2.77, 'trust':'r','valor':27.03,'delta':None},
            {'name':'F5 Networks',       'mkt':'USD','vol':0.13, 'abertura':401.79, 'atual':386.78, 'lucro':-1.96,'pct':-3.75, 'trust':'r','valor':50.28,'delta':None},
            {'name':'Astera Labs',       'mkt':'USD','vol':0.075,'abertura':376.18, 'atual':361.36, 'lucro':-1.11,'pct':-3.93, 'trust':'r','valor':27.10,'delta':None},
            {'name':'SpaceX',            'mkt':'USD','vol':0.1,  'abertura':221.00, 'atual':201.90, 'lucro':-1.91,'pct':-8.64, 'trust':'r','valor':20.19,'delta':None},
            {'name':'Cerebras Systems',  'mkt':'USD','vol':0.05, 'abertura':298.76, 'atual':208.76, 'lucro':-4.50,'pct':-30.12,'trust':'r','valor':10.44,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida', 'ticker':'KEEL','ativo':'Keel Infrastructure Corp','mkt':'USD','nota':'SAIDA KEEL +0.55$ @ 5.95 -- Protocolo V10'},
        {'tipo':'entrada','ticker':'ALAB','ativo':'Astera Labs','mkt':'USD','nota':'ENTRADA ALAB 0.075 @ 376.19 -- VCP'},
        {'tipo':'entrada','ticker':'SPCX','ativo':'SpaceX','mkt':'USD','nota':'ENTRADA SPCX 0.1 @ 221 -- IPO Momentum -- aposta IPO'},
        {'tipo':'diario','nota':'Saida KEEL via Protocolo V10. Entradas Astera Labs (VCP) e SpaceX (IPO Momentum).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'KEEL',
            'nome': 'Keel Infrastructure Corp',
            'mkt': 'USD',
            'lucro': 0.55,
            'lucro_pct': 1.88,
            'tipo': 'lucro',
            'data_entrada': '2026-06-01',
            'data_saida': '2026-06-16',
            'preco_entrada': 5.84,
            'preco_saida': 5.95,
            'volume': 5,
            'dias_holding': 15,
            'setup': 'Protocolo V10',
            'nota_entrada': None,
            'nota_saida': None,
            'imagem_setup': None,
            'rating': 1
        }
    ]
}

d['2026-06-16'] = entry

# Actualizar REAL_USD_JUN: 13.99 + 0.55 = 14.54
d['meses']['2026-06']['realizado_usd'] = 14.54

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-16 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('KEEL fechada: +0.55$ | REAL_USD_JUN: +14.54$')
print('REAL_EUR_JUN: -0.90 (inalterado)')
print('EUR equity: +9.52 (130.2% meta)')
print('USD equity: +5.90 (20.1% meta)')
print('AUM aprox 332')
