import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

def P(name, mkt, vol, ab, at, lu, pct, valor, stop):
    return {'name': name, 'mkt': mkt, 'vol': vol, 'abertura': ab, 'atual': at, 'lucro': lu, 'pct': pct,
            'trust': 'v' if pct >= 0 else 'r', 'valor': valor, 'delta': None, 'stop': stop}

d['2026-09-25'] = {
    'eur': {'saldo': 103.15, 'caixa': 0.08, 'lucro': -6.30, 'positions': [
        P('Allianz', 'EUR', 0.119, 437.94, 423.80, -1.68, -3.22, 50.43, 395.64),
        P('Schneider', 'EUR', 0.079, 304.39, 290.80, -1.06, -4.41, 22.98, 273.95),
        P('BAE Systems', 'EUR', 1.3, 21.738, 19.725, -3.56, -10.72, 29.66, 19.564),
    ]},
    'usd': {'saldo': 252.56, 'caixa': 72.06, 'lucro': -18.97, 'positions': [
        P('Amgen', 'USD', 0.12, 434.99, 414.45, -2.47, -4.73, 49.73, 391.49),
        P('CME', 'USD', 0.2, 286.71, 264.37, -4.47, -7.80, 52.87, 258.04),
        P('Cerebras Systems', 'USD', 0.13, 237.55, 206.64, -4.03, -13.05, 26.85, 213.80),
        P('SpaceX', 'USD', 0.24, 171.10, 148.63, -5.40, -13.15, 35.67, 153.99),
        P('PayPay', 'USD', 1, 17.98, 15.38, -2.60, -14.46, 15.38, 16.18),
    ]},
    'eventos': [
        {'tipo': 'saida', 'ticker': 'ZS', 'ativo': 'Zscaler', 'mkt': 'USD',
         'nota': 'SAIDA ZS 0.2 @ 194.25 (entrada 194.12) +0.03$ -- evento risk'},
        {'tipo': 'diario', 'nota': ''},
    ],
    'posicoes_fechadas': [
        {'ticker': 'ZS', 'nome': 'Zscaler', 'mkt': 'USD', 'lucro': 0.03, 'lucro_pct': 0.08, 'tipo': 'lucro',
         'data_entrada': '2026-09-17', 'data_saida': '2026-09-25', 'preco_entrada': 194.12, 'preco_saida': 194.25,
         'volume': 0.2, 'dias_holding': 8, 'setup': 'Evento Risk', 'nota_entrada': 'Stage 2 4/6',
         'nota_saida': 'evento risk', 'imagem_setup': None},
    ],
}
m = d['meses']['2026-09']
m['realizado_usd'] = round(m.get('realizado_usd', 0) + 0.03, 2)
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-25 realizado_usd', m['realizado_usd'])
