import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-21'] = {
    'eur': {'saldo': 106.80, 'caixa': 8.23, 'lucro': -2.65, 'positions': [
        P('Allianz', 'EUR', 0.1, 439.60, 444.10, 0.45, 1.02, 44.41, 395.64),
        P('Schneider', 'EUR', 0.079, 304.39, 295.30, -0.71, -2.95, 23.33, 273.95),
        P('BAE Systems', 'EUR', 1.3, 21.738, 20.440, -2.39, -7.19, 30.83, 19.564),
    ]},
    'usd': {'saldo': 257.72, 'caixa': 33.03, 'lucro': -13.60, 'positions': [
        P('Zscaler', 'USD', 0.2, 194.2, 207.18, 2.62, 6.75, 41.44, 174.78),
        P('PayPay', 'USD', 1, 17.98, 17.50, -0.48, -2.67, 17.50, 16.18),
        P('CME', 'USD', 0.2, 286.71, 275.51, -2.24, -3.91, 55.10, 258.04),
        P('Amgen', 'USD', 0.12, 434.99, 393.07, -5.03, -9.64, 47.17, 391.49),
        P('SpaceX', 'USD', 0.24, 171.10, 151.82, -4.63, -11.27, 36.44, 153.99),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 207.91, -3.84, -12.44, 27.04, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': ''}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-21')
