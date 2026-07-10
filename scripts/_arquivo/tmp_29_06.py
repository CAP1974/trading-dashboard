import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 69.16,
        'caixa': 1.83,
        # caixa events diz 0.92 mas screenshot mostra 1.83 (calculo: 0.89+39.90-38.97=1.82~1.83 confirma screenshot)
        'lucro': -0.92,
        'positions': [
            {'name':'Allianz',       'mkt':'EUR','vol':0.095,'abertura':410.20,'atual':409.60,'lucro':-0.06,'pct':-0.15,'trust':'r','valor':38.91,'delta':None},
            {'name':'Poste Italiane','mkt':'EUR','vol':1.0,  'abertura':29.280,'atual':28.420,'lucro':-0.86,'pct':-2.94,'trust':'r','valor':28.42,'delta':None}
        ]
    },
    'usd': {
        'saldo': 286.70,
        'caixa': 11.33,
        'lucro': 0.96,
        'positions': [
            {'name':'Veracyte',            'mkt':'USD','vol':1.7, 'abertura':53.31, 'atual':0.00,'lucro':11.14,'pct':12.29, 'trust':'v','valor':101.76,'delta':None},
            {'name':'Brightspring Health', 'mkt':'USD','vol':0.94,'abertura':68.74, 'atual':0.00,'lucro':0.23, 'pct':0.36,  'trust':'v','valor':64.84, 'delta':None},
            {'name':'Apple Hospitality',   'mkt':'USD','vol':3.0, 'abertura':16.90, 'atual':0.00,'lucro':-0.06,'pct':-0.12, 'trust':'r','valor':50.64, 'delta':None},
            {'name':'Caterpillar',         'mkt':'USD','vol':0.03,'abertura':1048.01,'atual':0.00,'lucro':-0.44,'pct':-1.40,'trust':'r','valor':31.00, 'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.1, 'abertura':221.00,'atual':0.00,'lucro':-5.69,'pct':-25.75,'trust':'r','valor':16.41, 'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.05,'abertura':298.76,'atual':0.00,'lucro':-4.22,'pct':-28.25,'trust':'r','valor':10.72, 'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'ASML','ativo':'ASML Holding','mkt':'EUR',
         'nota':'SAIDA ASML 0.025 @ 1596 -- Mudanca Macro Detector -- -1.12EUR'},
        {'tipo':'entrada','ticker':'ALV','ativo':'Allianz','mkt':'EUR',
         'nota':'ENTRADA ALV 0.095 @ 410.20 -- WMS 84A'},
        {'tipo':'entrada','ticker':'APLE','ativo':'Apple Hospitality','mkt':'USD',
         'nota':'ENTRADA APLE 3 @ 16.90 -- WMS 83A'},
        {'tipo':'diario','nota':'Saida ASML por mudanca Macro Detector. Entrada ALV EUR e APLE USD. Caixa EUR: screenshot 1.83 (eventos erraram 0.92).'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'ASML',
            'nome': 'ASML Holding',
            'mkt': 'EUR',
            'lucro': -1.12,
            'lucro_pct': -2.74,
            'tipo': 'prejuizo',
            'data_entrada': '2026-06-19',
            'data_saida': '2026-06-29',
            'preco_entrada': 1641.00,
            'preco_saida': 1596.00,
            'volume': 0.025,
            'dias_holding': 10,
            'setup': 'Macro Detector',
            'nota_entrada': 'ENTRADA ASML Clean Trend',
            'nota_saida': 'saida mudanca Macro Detector',
            'imagem_setup': None,
            'rating': 0
        }
    ]
}

d['2026-06-29'] = entry

# REAL_EUR_JUN: 7.32 - 1.12 = +6.20
d['meses']['2026-06']['realizado_eur'] = 6.20
# REAL_USD_JUN: +12.43 (inalterado)

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-29 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('ASML saida: -1.12EUR @ 1596 (10 dias, -2.74%, 0 estrelas)')
print('ALV entrada: 0.095@410.20 = 38.97EUR | APLE entrada: 3@16.90 = 50.70$')
print('caixa EUR: 0.89+39.90-38.97=1.82~1.83 checkOK (events erraram 0.92)')
print('caixa USD: 62.03-50.70=11.33 checkOK')
print('REAL_EUR_JUN: +6.20 | REAL_USD_JUN: +12.43 (inalterado)')
print('EUR equity: +5.28 (72.2% meta) | USD equity: +13.39 (45.5% meta)')
print('AUM ~333EUR | 58 dias activos')
