import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-28'] = {
    'eur': {'saldo': 103.60, 'caixa': 0.08, 'lucro': -5.85, 'positions': [
        P('Allianz', 'EUR', 0.119, 437.94, 427.30, -1.26, -2.42, 50.85, 395.64),
        P('Schneider', 'EUR', 0.079, 304.39, 290.85, -1.06, -4.41, 22.98, 273.95),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.680, -3.53, -10.63, 29.69, 19.564),
    ]},
    'usd': {'saldo': 251.17, 'caixa': 72.06, 'lucro': -20.36, 'positions': [
        P('Amgen', 'USD', 0.12, 434.99, 418.21, -2.01, -3.85, 50.19, 391.49),
        P('CME', 'USD', 0.2, 286.71, 263.22, -4.70, -8.20, 52.64, 258.04),
        P('PayPay', 'USD', 1, 17.98, 15.84, -2.14, -11.90, 15.84, 16.18),
        P('SpaceX', 'USD', 0.24, 171.10, 145.41, -6.18, -15.05, 34.89, 153.99),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 196.60, -5.33, -17.26, 25.55, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-28')
