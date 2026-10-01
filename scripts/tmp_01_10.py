import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-10-01'] = {
    'eur': {'saldo': 101.63, 'caixa': 0.08, 'lucro': -7.82, 'positions': [
        P('Schneider', 'EUR', 0.079, 304.39, 292.70, -0.92, -3.83, 23.12, 273.95),
        P('Allianz', 'EUR', 0.119, 437.94, 411.30, -3.17, -6.08, 48.94, 395.64),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.420, -3.73, -11.23, 29.49, 19.564),
    ]},
    'usd': {'saldo': 245.86, 'caixa': 7.72, 'lucro': -25.67, 'positions': [
        P('Zscaler', 'USD', 0.2, 198.14, 198.29, 0.03, 0.08, 39.66, 178.33),
        P('Intuitive', 'USD', 0.06, 411.76, 400.96, -0.65, -2.63, 24.06, 370.58),
        P('Amgen', 'USD', 0.12, 434.99, 407.11, -3.35, -6.42, 48.85, 391.49),
        P('CME', 'USD', 0.2, 286.71, 265.03, -4.33, -7.55, 53.01, 258.04),
        P('SpaceX', 'USD', 0.24, 171.10, 147.94, -5.56, -13.54, 35.51, 153.99),
        P('PayPay', 'USD', 1, 17.98, 15.01, -2.97, -16.52, 15.01, 16.18),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 169.51, -8.84, -28.63, 22.04, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-10-01')
