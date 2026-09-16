import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

d['2026-09-16'] = {
    'eur': {
        'saldo': 105.82, 'caixa': 8.23, 'lucro': -3.63,
        'positions': [
            {'ticker': 'ALV', 'nome': 'Allianz', 'vol': 0.1, 'entrada': 439.60, 'atual': 448.80, 'lucro': 0.92, 'pct': 2.09, 'stop': 395.64},
            {'ticker': 'BA.', 'nome': 'Bae Systems', 'vol': 1.3, 'entrada': 21.738, 'atual': 20.320, 'lucro': -2.59, 'pct': -7.80, 'stop': 19.564},
            {'ticker': 'SU', 'nome': 'Schneider', 'vol': 0.079, 'entrada': 304.39, 'atual': 279.45, 'lucro': -1.96, 'pct': -8.15, 'stop': 273.95},
        ]
    },
    'usd': {
        'saldo': 250.37, 'caixa': 89.83, 'lucro': -20.95,
        'positions': [
            {'ticker': 'CME', 'nome': 'CME', 'vol': 0.2, 'entrada': 286.71, 'atual': 272.43, 'lucro': -2.85, 'pct': -4.97, 'stop': 258.04},
            {'ticker': 'SPCX', 'nome': 'SpaceX', 'vol': 0.24, 'entrada': 171.10, 'atual': 150.79, 'lucro': -4.88, 'pct': -11.88, 'stop': 153.99},
            {'ticker': 'AMGN', 'nome': 'Amgen', 'vol': 0.12, 'entrada': 434.99, 'atual': 376.39, 'lucro': -7.03, 'pct': -13.47, 'stop': 391.49},
            {'ticker': 'CBRS', 'nome': 'Cerebras Systems', 'vol': 0.13, 'entrada': 237.55, 'atual': 189.84, 'lucro': -6.19, 'pct': -20.05, 'stop': 213.80},
        ]
    },
    'eventos': [
        {'tipo': 'aporte', 'conta': 'eur', 'ticker': 'BA.', 'nome': 'Bae Systems', 'preco': 20.28, 'vol': 0.5, 'nota': 'melhorar preço medio'},
        {'tipo': 'saida', 'conta': 'usd', 'ticker': 'MSFT', 'nome': 'Microsoft', 'lucro': 0.38, 'saida': 493.61, 'entrada': 481.05, 'vol': 0.03, 'setup': 'Lateralização', 'nota': ''},
        {'tipo': 'saida', 'conta': 'usd', 'ticker': 'MSFT', 'nome': 'Microsoft', 'lucro': -0.13, 'saida': 493.61, 'entrada': 497.97, 'vol': 0.03, 'setup': 'Lateralização', 'nota': ''},
        {'tipo': 'diario', 'nota': ''},
    ],
    'posicoes_fechadas': [
        {'ticker': 'MSFT', 'nome': 'Microsoft', 'conta': 'usd', 'lucro': 0.38, 'saida': 493.61, 'entrada': 481.05, 'vol': 0.03, 'setup': 'Lateralização', 'nota': '', 'data': '2026-09-16'},
        {'ticker': 'MSFT', 'nome': 'Microsoft', 'conta': 'usd', 'lucro': -0.13, 'saida': 493.61, 'entrada': 497.97, 'vol': 0.03, 'setup': 'Lateralização', 'nota': '', 'data': '2026-09-16'},
    ],
}

m = d['meses']['2026-09']
m['realizado_usd'] = round(m.get('realizado_usd', 0) + 0.38 - 0.13, 2)

fm = d['fund_metrics']
fm['eur'].setdefault('transferencias', []).append({'data': '2026-09-16', 'valor': 20.00, 'nota': 'deposito externo'})

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('OK 2026-09-16 | EUR -3.63 (BAE sai stop) | USD -20.95 (2x MSFT saida, net +0.25) | deposito EUR +20')
