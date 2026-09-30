import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-30'] = {
    'eur': {'saldo': 102.20, 'caixa': 0.08, 'lucro': -7.25, 'positions': [
        P('Schneider', 'EUR', 0.079, 304.39, 291.30, -1.03, -4.28, 23.01, 273.95),
        P('Allianz', 'EUR', 0.119, 437.94, 415.30, -2.69, -5.16, 49.42, 395.64),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.610, -3.53, -10.63, 29.69, 19.564),
    ]},
    'usd': {'saldo': 249.86, 'caixa': 7.72, 'lucro': -21.67, 'positions': [
        P('Zscaler', 'USD', 0.2, 198.14, 199.24, 0.22, 0.56, 39.85, 178.33),
        P('Intuitive', 'USD', 0.06, 411.76, 406.65, -0.31, -1.25, 24.40, 370.58),
        P('Amgen', 'USD', 0.12, 434.99, 421.48, -1.62, -3.10, 50.58, 391.49),
        P('CME', 'USD', 0.2, 286.71, 261.93, -4.95, -8.63, 52.39, 258.04),
        P('SpaceX', 'USD', 0.24, 171.10, 150.78, -4.88, -11.88, 36.19, 153.99),
        P('PayPay', 'USD', 1, 17.98, 15.64, -2.34, -13.01, 15.64, 16.18),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 177.72, -7.79, -25.23, 23.09, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-30')
