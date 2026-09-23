import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-23'] = {
    'eur': {'saldo': 102.53, 'caixa': 0.08, 'lucro': -6.92, 'positions': [
        P('Schneider', 'EUR', 0.079, 304.39, 292.80, -0.91, -3.79, 23.13, 273.95),
        P('Allianz', 'EUR', 0.119, 437.94, 410.00, -3.32, -6.37, 48.79, 395.64),
        P('BAE Systems', 'EUR', 1.3, 21.738, 20.290, -2.69, -8.10, 30.53, 19.564),
    ]},
    'usd': {'saldo': 257.26, 'caixa': 33.03, 'lucro': -14.06, 'positions': [
        P('Zscaler', 'USD', 0.2, 194.2, 213.67, 3.91, 10.07, 42.73, 174.78),
        P('CME', 'USD', 0.2, 286.71, 270.77, -3.19, -5.56, 54.15, 258.04),
        P('Amgen', 'USD', 0.12, 434.99, 405.74, -3.51, -6.72, 48.69, 391.49),
        P('PayPay', 'USD', 1, 17.98, 16.43, -1.55, -8.62, 16.43, 16.18),
        P('SpaceX', 'USD', 0.24, 171.10, 148.29, -5.49, -13.37, 35.58, 153.99),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 204.94, -4.23, -13.70, 26.65, 213.80),
    ]},
    'eventos': [
        {'tipo': 'aporte', 'ticker': 'ALV', 'ativo': 'Allianz', 'mkt': 'EUR',
         'nota': 'APORTE ALV +0.019 @ 429.20 -- vol total 0.119 preco medio 437.94 (melhorar preco medio)'},
        {'tipo': 'diario', 'nota': ''},
    ],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-23')
