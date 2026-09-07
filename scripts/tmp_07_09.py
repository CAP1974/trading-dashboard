import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
usd_prev = d['2026-09-04']['usd']
d['2026-09-07'] = {
    'eur': {'saldo':86.21,'caixa':0.12,'lucro':-3.24,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':446.80,'lucro':0.72,'pct':1.64,'trust':'v','valor':44.68,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':295.80,'lucro':-0.67,'pct':-2.79,'trust':'r','valor':23.37,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':19.465,'lucro':-3.29,'pct':-15.42,'trust':'r','valor':18.04,'delta':None}]},
    'usd': usd_prev,
    'eventos':[{'tipo':'diario','nota':'Feriado nos EUA (mercado USD fechado, sem alteracoes). Sem trades EUR. ALERTA: BAE Systems -15.42%, 9o dia consecutivo em STOP DURO sem accao.'}],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-07 | EUR -3.24 caixa 0.12 | USD inalterado (feriado) | BAE -15.42% 9o dia')
