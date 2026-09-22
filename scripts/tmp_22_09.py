import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-22'] = {
    'eur': {'saldo': 104.72, 'caixa': 8.23, 'lucro': -4.73, 'positions': [
        P('Allianz', 'EUR', 0.1, 439.60, 430.10, -0.95, -2.16, 43.01, 395.64),
        P('Schneider', 'EUR', 0.079, 304.39, 295.55, -0.69, -2.87, 23.35, 273.95),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.975, -3.09, -9.30, 30.13, 19.564),
    ]},
    'usd': {'saldo': 258.98, 'caixa': 33.03, 'lucro': -12.34, 'positions': [
        P('Zscaler', 'USD', 0.2, 194.2, 209.55, 3.09, 7.96, 41.91, 174.78),
        P('Amgen', 'USD', 0.12, 434.99, 409.98, -3.00, -5.75, 49.20, 391.49),
        P('CME', 'USD', 0.2, 286.71, 267.08, -3.92, -6.84, 53.42, 258.04),
        P('PayPay', 'USD', 1, 17.98, 16.74, -1.24, -6.90, 16.74, 16.18),
        P('SpaceX', 'USD', 0.24, 171.10, 154.67, -3.95, -9.62, 37.12, 153.99),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 212.00, -3.32, -10.75, 27.56, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-22')
