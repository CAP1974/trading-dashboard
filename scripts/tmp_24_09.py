import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-24'] = {
    'eur': {'saldo': 102.78, 'caixa': 0.08, 'lucro': -6.67, 'positions': [
        P('Allianz', 'EUR', 0.119, 437.94, 419.30, -2.21, -4.24, 49.90, 395.64),
        P('Schneider', 'EUR', 0.079, 304.39, 289.75, -1.14, -4.74, 22.90, 273.95),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.900, -3.32, -9.99, 29.90, 19.564),
    ]},
    'usd': {'saldo': 256.88, 'caixa': 33.03, 'lucro': -14.44, 'positions': [
        P('Zscaler', 'USD', 0.2, 194.2, 213.71, 3.92, 10.10, 42.74, 174.78),
        P('CME', 'USD', 0.2, 286.71, 268.90, -3.56, -6.21, 53.78, 258.04),
        P('Amgen', 'USD', 0.12, 434.99, 405.90, -3.49, -6.69, 48.71, 391.49),
        P('PayPay', 'USD', 1, 17.98, 16.39, -1.59, -8.84, 16.39, 16.18),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 205.46, -4.17, -13.50, 26.71, 213.80),
        P('SpaceX', 'USD', 0.24, 171.10, 148.03, -5.55, -13.51, 35.52, 153.99),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-24')
