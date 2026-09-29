import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-29'] = {
    'eur': {'saldo': 102.99, 'caixa': 0.08, 'lucro': -6.46, 'positions': [
        P('Schneider', 'EUR', 0.079, 304.39, 295.90, -0.67, -2.79, 23.37, 273.95),
        P('Allianz', 'EUR', 0.119, 437.94, 422.20, -1.87, -3.59, 50.24, 395.64),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.435, -3.92, -11.80, 29.30, 19.564),
    ]},
    'usd': {'saldo': 252.45, 'caixa': 7.72, 'lucro': -19.08, 'positions': [
        P('Intuitive', 'USD', 0.06, 411.76, 411.97, 0.01, 0.04, 24.72, 370.58),
        P('Zscaler', 'USD', 0.2, 198.14, 198.22, 0.01, 0.03, 39.64, 178.33),
        P('Amgen', 'USD', 0.12, 434.99, 423.32, -1.40, -2.68, 50.80, 391.49),
        P('CME', 'USD', 0.2, 286.71, 263.09, -4.72, -8.23, 52.62, 258.04),
        P('PayPay', 'USD', 1, 17.98, 15.80, -2.18, -12.12, 15.80, 16.18),
        P('SpaceX', 'USD', 0.24, 171.10, 149.24, -5.26, -12.81, 35.81, 153.99),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 194.88, -5.54, -17.94, 25.34, 213.80),
    ]},
    'eventos': [
        {'tipo': 'entrada', 'conta': 'usd', 'ticker': 'ZS', 'nome': 'Zscaler', 'entrada': 198.14, 'vol': 0.2, 'setup': 'WMS62', 'nota': ''},
        {'tipo': 'entrada', 'conta': 'usd', 'ticker': 'IRSG', 'nome': 'Intuitive', 'entrada': 411.76, 'vol': 0.06, 'setup': 'WMS90', 'nota': 'Retoma'},
        {'tipo': 'diario', 'nota': ''},
    ],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-29')
