import json
F = 'C:/Users/Utilizador/trading-dashboard/data/trading_data.json'
with open(F, encoding='utf-8') as f:
    d = json.load(f)
s = d['meses']['2026-09']
s.update({'status': 'FECHADO', 'fim': '2026-09-30',
          'flutuante_fim_eur': -7.25, 'flutuante_fim_usd': -21.67,
          'saldo_fim_eur': 102.20, 'saldo_fim_usd': 249.86})
s['equity_eur'] = round(s['realizado_eur'] + s['flutuante_fim_eur'], 2)
s['equity_usd'] = round(s['realizado_usd'] + s['flutuante_fim_usd'], 2)
d['meses']['2026-10'] = {'inicio': '2026-10-01', 'status': 'EM CURSO',
    'base_eur': 102.20, 'base_usd': 249.86, 'base_ajustada_eur': 102.20, 'base_ajustada_usd': 249.86,
    'meta_eur': 10.22, 'meta_usd': 24.986, 'ajustes_eur': 0, 'ajustes_usd': 0,
    'realizado_eur': 0, 'realizado_usd': 0,
    'flutuante_fim_eur': None, 'flutuante_fim_usd': None, 'saldo_fim_eur': None, 'saldo_fim_usd': None}
with open(F, 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('SET', json.dumps(s)); print('OUT', json.dumps(d['meses']['2026-10']))
