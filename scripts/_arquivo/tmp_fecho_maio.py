import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

# === FECHAR MAIO 2026 ===
d['meses']['2026-05'].update({
    'saldo_fim_eur': 73.10,
    'saldo_fim_usd': 294.09,
    'flutuante_fim_eur': 9.87,
    'flutuante_fim_usd': 20.34,
    'realizado_eur': 10.75,
    'realizado_usd': 12.77,
    'equity_eur': 20.62,
    'equity_usd': 33.11,
    'retorno_meta_eur_pct': 350.1,
    'retorno_meta_usd_pct': 121.6,
    'trades_total': 18,
    'trades_eur': 4,
    'trades_usd': 14,
    'win_rate_pct': 50.0,
    'profit_factor': 3.29,
    'status': 'FECHADO',
    'fim': '2026-05-29'
})

# === ABRIR JUNHO 2026 ===
d['meses']['2026-06'] = {
    'inicio': '2026-06-02',
    'status': 'EM CURSO',
    'base_eur': 73.10,
    'base_usd': 294.09,
    'base_ajustada_eur': 73.10,
    'base_ajustada_usd': 294.09,
    'meta_eur': 7.31,
    'meta_usd': 29.409,
    'ajustes_eur': 0,
    'ajustes_usd': 0,
    'realizado_eur': 0,
    'realizado_usd': 0,
    'flutuante_fim_eur': None,
    'flutuante_fim_usd': None,
    'saldo_fim_eur': None,
    'saldo_fim_usd': None
}

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('Maio fechado OK')
print('Junho criado OK')
print(f'  meta_eur: 7.31EUR | meta_usd: 29.41$')
