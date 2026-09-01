import json

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)

# ── FECHO DE AGOSTO ──
ago = d['meses']['2026-08']
ago['status'] = 'FECHADO'
ago['saldo_fim_eur'] = 87.28
ago['saldo_fim_usd'] = 258.51
ago['flutuante_fim_eur'] = -2.17
ago['flutuante_fim_usd'] = -12.08
ago['equity_eur'] = round(ago['realizado_eur'] + ago['flutuante_fim_eur'], 2)
ago['equity_usd'] = round(ago['realizado_usd'] + ago['flutuante_fim_usd'], 2)

# ── INICIO DE SETEMBRO (juro composto sobre saldo_fim de agosto) ──
d['meses']['2026-09'] = {
    'inicio': '2026-09-01',
    'status': 'EM CURSO',
    'base_eur': 87.28,
    'base_usd': 258.51,
    'base_ajustada_eur': 87.28,
    'base_ajustada_usd': 258.51,
    'meta_eur': round(87.28 * 0.10, 3),
    'meta_usd': round(258.51 * 0.10, 3),
    'ajustes_eur': 0,
    'ajustes_usd': 0,
    'realizado_eur': 0,
    'realizado_usd': 0.19,
    'flutuante_fim_eur': None,
    'flutuante_fim_usd': None,
    'saldo_fim_eur': None,
    'saldo_fim_usd': None
}

# ── DIA 2026-09-01 ──
entry = {
    'eur': {
        'saldo': 86.64,
        'caixa': 0.12,
        'lucro': -2.81,
        'positions': [
            {'name':'Allianz',      'mkt':'EUR','vol':0.1,  'abertura':439.60,'atual':450.10,'lucro':1.05, 'pct':2.39, 'trust':'v','valor':45.01,'delta':None},
            {'name':'Schneider',    'mkt':'EUR','vol':0.079,'abertura':304.39,'atual':288.40,'lucro':-1.26,'pct':-5.24,'trust':'r','valor':22.78,'delta':None},
            {'name':'BAE Systems',  'mkt':'EUR','vol':0.8,  'abertura':22.650,'atual':20.180,'lucro':-2.60,'pct':-12.19,'trust':'r','valor':18.73,'delta':None}
        ]
    },
    'usd': {
        'saldo': 257.60,
        'caixa': 76.00,
        'lucro': -13.24,
        'positions': [
            {'name':'Microsoft',           'mkt':'USD','vol':0.06, 'abertura':489.51,'atual':500.98, 'lucro':0.69, 'pct':2.35, 'trust':'v','valor':30.06,'delta':None},
            {'name':'Amgen',                'mkt':'USD','vol':0.12, 'abertura':434.99,'atual':437.97, 'lucro':0.36, 'pct':0.69, 'trust':'v','valor':52.56,'delta':None},
            {'name':'CME',                  'mkt':'USD','vol':0.2,  'abertura':286.71,'atual':286.25, 'lucro':-0.09,'pct':-0.16,'trust':'v','valor':57.25,'delta':None},
            {'name':'SpaceX',              'mkt':'USD','vol':0.16, 'abertura':180.60,'atual':142.19, 'lucro':-6.15,'pct':-21.28,'trust':'r','valor':22.75,'delta':None},
            {'name':'Cerebras Systems',    'mkt':'USD','vol':0.11, 'abertura':245.75,'atual':172.52, 'lucro':-8.05,'pct':-29.78,'trust':'r','valor':18.98,'delta':None}
        ]
    },
    'eventos': [
        {'tipo':'saida','ticker':'BIO','ativo':'Bio-Rad','mkt':'USD',
         'nota':'SAIDA BIO +0.19$ -- saida:380.63 entrada:378.71 vol:0.1 -- Divergencia de Fluxo'},
        {'tipo':'diario','nota':'Fecho de Agosto (equity EUR -2.72 / -38.9% meta; equity USD -7.67 / -30.6% meta) e inicio de Setembro (base EUR 87.28 / base USD 258.51). Saida Bio-Rad com pequeno lucro (+0.19$, divergencia de fluxo). ALERTA: BAE Systems piora para -12.19%, 5o dia consecutivo a violar o STOP DURO sem accao.'}
    ],
    'posicoes_fechadas': [
        {'nome':'Bio-Rad','ticker':'BIO','mkt':'USD','lucro':0.19,'lucro_pct':0.51,
         'tipo':'lucro','data_entrada':'2026-08-21','data_saida':'2026-09-01','dias_holding':11,
         'preco_entrada':378.71,'preco_saida':380.63,'volume':0.1,'setup':'Divergencia de Fluxo',
         'nota_entrada':'VCP','nota_saida':'Divergencia de Fluxo'}
    ]
}

d['2026-09-01'] = entry

with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('Agosto FECHADO: saldo_fim EUR 87.28 / USD 258.51 | equity EUR', ago['equity_eur'], '/ USD', ago['equity_usd'])
print('Setembro EM CURSO: base EUR 87.28 (meta {:.3f}) / base USD 258.51 (meta {:.3f})'.format(d['meses']['2026-09']['meta_eur'], d['meses']['2026-09']['meta_usd']))
print('2026-09-01 criado OK')
print('EUR saldo:', entry['eur']['saldo'], 'caixa:', entry['eur']['caixa'], 'lucro:', entry['eur']['lucro'])
print('USD saldo:', entry['usd']['saldo'], 'caixa:', entry['usd']['caixa'], 'lucro:', entry['usd']['lucro'])
print('SAIDA BIO +0.19$ -- caixa USD: 37.88+38.06=75.94 vs 76.00 informado (diferenca minima, fee/rounding)')
print('ALERTA STOP DURO: BAE Systems -12.19% (5o dia consecutivo)')
print('REAL_EUR_SET: 0.00 | REAL_USD_SET: +0.19')
print('EUR equity: -2.81 (-32.2% meta) | USD equity: -13.05 (-50.5% meta)')
print('AUM correto: 86.64 + 257.60*0.92 = ~324')
