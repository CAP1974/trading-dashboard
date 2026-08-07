import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 68.98,
        'caixa': 1.45,
        'lucro': -0.47,
        'positions': [
            {'name':'Schneider', 'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':304.55,'lucro':0.02, 'pct':0.08, 'trust':'v','valor':24.06,'delta':None},
            {'name':'Allianz',   'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':434.70,'lucro':-0.49,'pct':-1.11,'trust':'r','valor':43.47,'delta':None}
        ]
    },
    'usd': {
        'saldo': 253.75,
        'caixa': 0.36,
        'lucro': -11.61,
        'positions': [
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':63.15, 'lucro':0.82, 'pct':1.32, 'trust':'v','valor':63.15,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':499.78, 'lucro':0.05, 'pct':0.33, 'trust':'v','valor':14.99,'delta':None},
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':363.71, 'lucro':-1.39,'pct':-1.00,'trust':'r','valor':138.21,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':224.75, 'lucro':-3.49,'pct':-18.15,'trust':'r','valor':15.74,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':133.11, 'lucro':-7.60,'pct':-26.30,'trust':'r','valor':21.30,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'SLHN','ativo':'Swiss Life','mkt':'EUR',
         'nota':'SAIDA SLHN 0.019 @ 945.00 -- EMA21 -- -0.34EUR (tranche 1/2, cotacao CHF)'},
        {'tipo':'saida','ticker':'SLHN','ativo':'Swiss Life','mkt':'EUR',
         'nota':'SAIDA SLHN 0.0295 @ 945.00 -- EMA21 -- -0.48EUR (tranche 2/2, saida completa, cotacao CHF)'},
        {'tipo':'saida','ticker':'COPA','ativo':'Copper (WisdomTree)','mkt':'EUR',
         'nota':'SAIDA COPA 0.4 @ 56.83 -- WMS65C -- +0.27EUR (cotacao moeda estrangeira, saida completa)'},
        {'tipo':'entrada','ticker':'ALV','ativo':'Allianz','mkt':'EUR',
         'nota':'ENTRADA ALV 0.1 @ 439.60 -- VCP'},
        {'tipo':'entrada','ticker':'SU','ativo':'Schneider','mkt':'EUR',
         'nota':'ENTRADA SU 0.019 @ 303.40 -- Clean Trend (tranche 1/2)'},
        {'tipo':'entrada','ticker':'SU','ativo':'Schneider','mkt':'EUR',
         'nota':'ENTRADA SU 0.06 @ 304.70 -- Clean Trend (tranche 2/2) -- vol total 0.079 preco medio 304.39'},
        {'tipo':'diario','nota':'Dia de rebalanceamento EUR: Swiss Life e Copper fechadas por completo. Novas entradas Allianz e Schneider. Nota: Swiss Life (CHF) e Copper (moeda estrangeira) tem P&L calculado pela XTB apos conversao cambial -- nao bate com formula simples preco x volume, usado o resultado literal informado.'}
    ],
    'posicoes_fechadas': [
        {
            'ticker': 'SLHN', 'nome': 'Swiss Life (tranche aporte)', 'mkt': 'EUR',
            'lucro': -0.34, 'lucro_pct': -1.90, 'tipo': 'prejuizo',
            'data_entrada': '2026-07-16', 'data_saida': '2026-08-07',
            'preco_entrada': 942.40, 'preco_saida': 945.00, 'volume': 0.019,
            'dias_holding': 22, 'setup': 'Ajuste Portfolio',
            'nota_entrada': 'aporte 16/07', 'nota_saida': 'EMA21 (cotacao CHF)',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'SLHN', 'nome': 'Swiss Life (tranche original)', 'mkt': 'EUR',
            'lucro': -0.48, 'lucro_pct': -1.73, 'tipo': 'prejuizo',
            'data_entrada': '2026-06-13', 'data_saida': '2026-08-07',
            'preco_entrada': 939.00, 'preco_saida': 945.00, 'volume': 0.0295,
            'dias_holding': 55, 'setup': 'Ajuste Portfolio',
            'nota_entrada': 'entrada original (correcao dia 13)', 'nota_saida': 'EMA21 -- saida completa (cotacao CHF)',
            'imagem_setup': None, 'rating': 0
        },
        {
            'ticker': 'COPA', 'nome': 'Copper (WisdomTree)', 'mkt': 'EUR',
            'lucro': 0.27, 'lucro_pct': 1.23, 'tipo': 'lucro',
            'data_entrada': '2026-07-16', 'data_saida': '2026-08-07',
            'preco_entrada': 55.00, 'preco_saida': 56.83, 'volume': 0.4,
            'dias_holding': 22, 'setup': 'Ajuste Portfolio Balanca',
            'nota_entrada': 'ENTRADA COPA Ajuste Portfolio', 'nota_saida': 'WMS65C -- saida completa (cotacao moeda estrangeira)',
            'imagem_setup': None, 'rating': 1
        }
    ]
}

d['2026-08-07'] = entry

# REAL_EUR_AGO: 0.00 - 0.34 - 0.48 + 0.27 = -0.55
# REAL_USD_AGO: -0.83 (inalterado, sem saidas USD)
d['meses']['2026-08']['realizado_eur'] = -0.55

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-07 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('Swiss Life fechada completa (2 tranches, CHF): -0.34-0.48=-0.82')
print('Copper fechada completa (moeda estrangeira): +0.27')
print('ALV entrada 0.1@439.60 | SU Schneider 2 tranches vol total 0.079 preco medio 304.39')
print('REAL_EUR_AGO: -0.55 | REAL_USD_AGO: -0.83 (inalterado)')
print('EUR equity: -1.02 (-14.6% meta) | USD equity: -12.44 (-49.7% meta)')
print('AUM ~304EUR | 87 dias activos')
