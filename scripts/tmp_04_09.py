import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-04'] = {
    'eur': {'saldo':85.98,'caixa':0.12,'lucro':-3.47,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':449.40,'lucro':0.98,'pct':2.23,'trust':'v','valor':44.94,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':288.80,'lucro':-1.22,'pct':-5.07,'trust':'r','valor':22.82,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':19.540,'lucro':-3.23,'pct':-15.14,'trust':'r','valor':18.10,'delta':None}]},
    'usd': {'saldo':261.40,'caixa':76.00,'lucro':-9.44,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':499.65,'lucro':0.61,'pct':2.08,'trust':'v','valor':29.98,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':437.09,'lucro':0.25,'pct':0.48,'trust':'v','valor':52.45,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':281.27,'lucro':-1.09,'pct':-1.90,'trust':'r','valor':56.25,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.11,'abertura':245.75,'atual':209.66,'lucro':-3.98,'pct':-14.72,'trust':'r','valor':23.05,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.16,'abertura':180.60,'atual':147.93,'lucro':-5.23,'pct':-18.10,'trust':'r','valor':23.67,'delta':None}]},
    'eventos':[{'tipo':'diario','nota':'Sem trades. Caixa inalterada. ALERTA: BAE Systems -15.14%, 8o dia consecutivo em STOP DURO sem accao.'}],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-04 | EUR -3.47 caixa 0.12 | USD -9.44 caixa 76.00 | BAE -15.14% 8o dia')
