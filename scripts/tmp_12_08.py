import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

entry = {
    'eur': {
        'saldo': 89.62,
        'caixa': 0.12,
        'lucro': 0.17,
        'positions': [
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':310.25,'lucro':0.46, 'pct':1.91, 'trust':'v','valor':24.50,'delta':None},
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':438.70,'lucro':-0.09,'pct':-0.20,'trust':'r','valor':43.87,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':22.680,'lucro':-0.20,'pct':-0.94,'trust':'r','valor':21.13,'delta':None}
        ]
    },
    'usd': {
        'saldo': 268.64,
        'caixa': 0.36,
        'lucro': 3.28,
        'positions': [
            {'name':'Palo Alto',           'mkt':'USD','vol':0.38, 'abertura':367.35,'atual':386.93, 'lucro':7.44, 'pct':5.33, 'trust':'v','valor':147.04,'delta':None},
            {'name':'Bank of America',    'mkt':'USD','vol':1.0,  'abertura':62.33, 'atual':64.80,  'lucro':2.47, 'pct':3.96, 'trust':'v','valor':64.80,'delta':None},
            {'name':'Microsoft',           'mkt':'USD','vol':0.03, 'abertura':497.97,'atual':492.52, 'lucro':-0.16,'pct':-1.07,'trust':'r','valor':14.78,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.07, 'abertura':274.71,'atual':262.07, 'lucro':-0.89,'pct':-4.63,'trust':'r','valor':18.34,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':145.71, 'lucro':-5.58,'pct':-19.31,'trust':'r','valor':23.32,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'entrada','ticker':'BA.L','ativo':'BAE Systems','mkt':'EUR',
         'nota':'ENTRADA BA.L 0.8 @ 22.65 -- financiada por deposito externo de 20EUR (registado em fund_metrics). Cotacao GBX, cambio diario -- P&L nao bate com formula simples preco x volume.'},
        {'tipo':'diario','nota':'Deposito Carlos de 20EUR na conta EUR, usado para abrir posicao BAE Systems (LSE, GBX). Sem trades USD hoje -- boa recuperacao geral (Palo Alto +5.33%, BofA +3.96%).'}
    ],
    'posicoes_fechadas': []
}

d['2026-08-12'] = entry

# Registar deposito externo em fund_metrics (fluxo externo -- NAV nao deve contar como retorno)
d['fund_metrics']['eur']['transferencias'].append({
    'data': '2026-08-12',
    'valor': 20.00,
    'nota': 'Deposito Carlos - financiou entrada BAE Systems'
})

# Realizados inalterados (sem saidas hoje)
# REAL_EUR_AGO: -0.55 | REAL_USD_AGO: -0.83

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-08-12 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('BAE Systems entrada: 0.8@22.65 (GBX) -- deposito 20EUR registado em fund_metrics')
print('REAL_EUR_AGO: -0.55 (inalterado) | REAL_USD_AGO: -0.83 (inalterado)')
print('EUR equity: -0.38 (-5.4% meta) | USD equity: +2.45 (9.8% meta)')
print('AUM ~337EUR | 90 dias activos')
