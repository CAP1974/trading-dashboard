import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

# Carrega posições do último dia de Maio (carry-over fim de semana)
last_may = d['2026-05-29']

# Stub 2026-06-02 — posições inalteradas, sem eventos, sem fechados
entry = {
    'eur': {
        'saldo': last_may['eur']['saldo'],
        'caixa': last_may['eur']['caixa'],
        'lucro': last_may['eur']['lucro'],
        'positions': last_may['eur']['positions']
    },
    'usd': {
        'saldo': last_may['usd']['saldo'],
        'caixa': last_may['usd']['caixa'],
        'lucro': last_may['usd']['lucro'],
        'positions': last_may['usd']['positions']
    },
    'eventos': [
        {'tipo':'diario','nota':'Inicio Junho 2026 — posicoes carregadas do fim-de-semana. Base EUR 73.10EUR | Meta 7.31EUR. Base USD 294.09$ | Meta 29.41$.'}
    ],
    'posicoes_fechadas': []
}

d['2026-06-02'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('2026-06-02 stub criado OK')
print(f'EUR carry: saldo={entry["eur"]["saldo"]} lucro={entry["eur"]["lucro"]}')
print(f'USD carry: saldo={entry["usd"]["saldo"]} lucro={entry["usd"]["lucro"]}')
