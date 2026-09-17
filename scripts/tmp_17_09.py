import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

d['2026-09-17'] = {
    'eur': {
        'saldo': 106.67, 'caixa': 8.23, 'lucro': -2.78,
        'positions': [
            {'ticker': 'ALV', 'nome': 'Allianz', 'vol': 0.1, 'entrada': 439.60, 'atual': 450.40, 'lucro': 1.08, 'pct': 2.46, 'stop': 395.64},
            {'ticker': 'SU', 'nome': 'Schneider', 'vol': 0.079, 'entrada': 304.39, 'atual': 287.60, 'lucro': -1.32, 'pct': -5.49, 'stop': 273.95},
            {'ticker': 'BA.', 'nome': 'Bae Systems', 'vol': 1.3, 'entrada': 21.738, 'atual': 20.410, 'lucro': -2.54, 'pct': -7.65, 'stop': 19.564},
        ]
    },
    'usd': {
        'saldo': 252.36, 'caixa': 33.03, 'lucro': -18.96,
        'positions': [
            {'ticker': 'ZS', 'nome': 'Zscaler', 'vol': 0.2, 'entrada': 194.2, 'atual': 197.33, 'lucro': 0.65, 'pct': 1.67, 'stop': 174.78},
            {'ticker': 'PAYP', 'nome': 'PayPay', 'vol': 1, 'entrada': 17.98, 'atual': 17.72, 'lucro': -0.26, 'pct': -1.45, 'stop': 16.18},
            {'ticker': 'CME', 'nome': 'CME', 'vol': 0.2, 'entrada': 286.71, 'atual': 271.10, 'lucro': -3.12, 'pct': -5.44, 'stop': 258.04},
            {'ticker': 'SPCX', 'nome': 'SpaceX', 'vol': 0.24, 'entrada': 171.10, 'atual': 154.71, 'lucro': -3.93, 'pct': -9.57, 'stop': 153.99},
            {'ticker': 'AMGN', 'nome': 'Amgen', 'vol': 0.12, 'entrada': 434.99, 'atual': 379.66, 'lucro': -6.64, 'pct': -12.72, 'stop': 391.49},
            {'ticker': 'CBRS', 'nome': 'Cerebras Systems', 'vol': 0.13, 'entrada': 237.55, 'atual': 194.01, 'lucro': -5.66, 'pct': -18.33, 'stop': 213.80},
        ]
    },
    'eventos': [
        {'tipo': 'entrada', 'conta': 'usd', 'ticker': 'ZS', 'nome': 'Zscaler', 'entrada': 194.2, 'vol': 0.2, 'setup': 'Stage 2 4/6', 'nota': ''},
        {'tipo': 'entrada', 'conta': 'usd', 'ticker': 'PAYP', 'nome': 'PayPay', 'entrada': 17.98, 'vol': 1, 'setup': '', 'nota': 'aposta IPO'},
        {'tipo': 'diario', 'nota': ''},
    ],
    'posicoes_fechadas': [],
}

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('OK 2026-09-17 | EUR -2.78 (BAE -7.65%, sem stop) | USD -18.96 (novo: ZS, PAYP) | Amgen 7o dia stop')
