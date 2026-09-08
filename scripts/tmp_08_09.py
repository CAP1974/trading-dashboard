import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-08'] = {
    'eur': {'saldo':85.95,'caixa':0.12,'lucro':-3.50,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':442.10,'lucro':0.25,'pct':0.57,'trust':'v','valor':44.21,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':298.45,'lucro':-0.46,'pct':-1.91,'trust':'v','valor':23.58,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':19.455,'lucro':-3.29,'pct':-15.42,'trust':'r','valor':18.04,'delta':None}]},
    'usd': {'saldo':254.87,'caixa':76.00,'lucro':-15.97,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':493.76,'lucro':0.25,'pct':0.85,'trust':'v','valor':29.62,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':278.14,'lucro':-1.71,'pct':-2.98,'trust':'r','valor':55.63,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':393.18,'lucro':-5.02,'pct':-9.62,'trust':'r','valor':47.18,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.16,'abertura':180.60,'atual':153.45,'lucro':-4.35,'pct':-15.05,'trust':'r','valor':24.55,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.11,'abertura':245.75,'atual':199.06,'lucro':-5.14,'pct':-19.02,'trust':'r','valor':21.89,'delta':None}]},
    'eventos':[{'tipo':'diario','nota':'Sem trades. Caixa inalterada. ALERTA: BAE Systems -15.42%, 10o dia consecutivo em STOP DURO sem accao. Amgen aproxima-se do STOP DURO (-9.62%, ainda nao violado).'}],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-08 | EUR -3.50 caixa 0.12 | USD -15.97 caixa 76.00 | BAE -15.42% 10o dia | Amgen -9.62% (perto do stop)')
