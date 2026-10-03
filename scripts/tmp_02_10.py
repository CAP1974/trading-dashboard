import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-10-02'] = {
    'eur': {'saldo': 102.83, 'caixa': 0.08, 'lucro': -6.62, 'positions': [
        P('Schneider', 'EUR', 0.079, 304.39, 301.90, -0.19, -0.79, 23.85, 273.95),
        P('Allianz', 'EUR', 0.119, 437.94, 416.40, -2.56, -4.91, 49.55, 395.64),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.285, -3.87, -11.65, 29.35, 19.564),
    ]},
    'usd': {'saldo': 245.85, 'caixa': 7.72, 'lucro': -25.68, 'positions': [
        P('Zscaler', 'USD', 0.2, 198.14, 195.67, -0.50, -1.26, 39.13, 178.33),
        P('Intuitive', 'USD', 0.06, 411.76, 391.83, -1.20, -4.86, 23.51, 370.58),
        P('SpaceX', 'USD', 0.24, 171.10, 158.86, -2.94, -7.16, 38.13, 153.99),
        P('Amgen', 'USD', 0.12, 434.99, 402.80, -3.86, -7.39, 48.34, 391.49),
        P('CME', 'USD', 0.2, 286.71, 262.96, -4.75, -8.28, 52.59, 258.04),
        P('PayPay', 'USD', 1, 17.98, 14.80, -3.18, -17.69, 14.80, 16.18),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 166.25, -9.25, -29.95, 21.63, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-10-02')
