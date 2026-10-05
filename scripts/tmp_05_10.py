import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-10-05'] = {
    'eur': {'saldo': 101.13, 'caixa': 0.08, 'lucro': -8.32, 'positions': [
        P('Allianz', 'EUR', 0.119, 437.94, 418.40, -2.32, -4.45, 49.79, 395.64),
        P('Schneider', 'EUR', 0.079, 304.39, 276.05, -2.24, -9.32, 21.80, 273.95),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.330, -3.76, -11.32, 29.46, 19.564),
    ]},
    'usd': {'saldo': 253.59, 'caixa': 7.77, 'lucro': -17.99, 'positions': [
        P('Zscaler', 'USD', 0.2, 198.14, 201.03, 0.58, 1.46, 40.21, 178.33),
        P('SpaceX', 'USD', 0.24, 171.10, 171.08, -0.01, -0.02, 41.06, 153.99),
        P('Intuitive', 'USD', 0.06, 411.76, 406.12, -0.34, -1.38, 24.37, 370.58),
        P('CME', 'USD', 0.2, 286.71, 269.93, -3.35, -5.84, 53.99, 258.04),
        P('Amgen', 'USD', 0.12, 434.99, 402.83, -3.86, -7.39, 48.34, 391.49),
        P('PayPay', 'USD', 1, 17.98, 14.26, -3.72, -20.69, 14.26, 16.18),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 181.42, -7.29, -23.61, 23.59, 213.80),
    ]},
    'eventos': [{'tipo': 'diario', 'nota': 'Caixa USD 7.77 no screenshot vs 7.72 no eventos.txt (+0.05, sem trades) -- usado o screenshot por confirmacao do utilizador; credito na caixa, nao e deposito.'}],
    'posicoes_fechadas': [],
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-10-05')
