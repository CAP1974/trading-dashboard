import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-18'] = {
    'eur': {'saldo': 105.75, 'caixa': 8.23, 'lucro': -3.70, 'positions': [
        P('Allianz', 'EUR', 0.1, 439.60, 443.50, 0.39, 0.89, 44.35, 395.64),
        P('Schneider', 'EUR', 0.079, 304.39, 285.35, -1.50, -6.24, 22.54, 273.95),
        P('BAE Systems', 'EUR', 1.3, 21.738, 20.300, -2.59, -7.80, 30.63, 19.564),
    ]},
    'usd': {'saldo': 253.93, 'caixa': 33.03, 'lucro': -17.39, 'positions': [
        P('Zscaler', 'USD', 0.2, 194.2, 197.17, 0.61, 1.57, 39.43, 174.78),
        P('PayPay', 'USD', 1, 17.98, 17.66, -0.32, -1.78, 17.66, 16.18),
        P('CME', 'USD', 0.2, 286.71, 276.01, -2.14, -3.73, 55.20, 258.04),
        P('SpaceX', 'USD', 0.24, 171.10, 152.28, -4.53, -11.03, 36.54, 153.99),
        P('Amgen', 'USD', 0.12, 434.99, 385.57, -5.93, -11.36, 46.27, 391.49),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 198.39, -5.08, -16.45, 25.80, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-18')
