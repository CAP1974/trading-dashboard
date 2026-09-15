import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-15'] = {
    'eur': {'saldo':84.74,'caixa':0.12,'lucro':-4.71,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':443.60,'lucro':0.40,'pct':0.91,'trust':'v','valor':44.36,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':275.25,'lucro':-2.29,'pct':-9.53,'trust':'r','valor':21.75,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':19.940,'lucro':-2.82,'pct':-13.22,'trust':'r','valor':18.51,'delta':None}]},
    'usd': {'saldo':248.35,'caixa':60.21,'lucro':-22.72,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':496.71,'lucro':0.43,'pct':1.46,'trust':'v','valor':29.80,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':275.07,'lucro':-2.33,'pct':-4.06,'trust':'r','valor':55.01,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':375.55,'lucro':-7.13,'pct':-13.66,'trust':'r','valor':45.07,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.24,'abertura':171.10,'atual':143.41,'lucro':-6.66,'pct':-16.22,'trust':'r','valor':34.41,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.13,'abertura':237.55,'atual':183.42,'lucro':-7.03,'pct':-22.77,'trust':'r','valor':23.85,'delta':None}]},
    'eventos':[{'tipo':'diario','nota':'Sem trades. Caixa inalterada. Schneider recupera para -9.53%, sai da violacao do STOP DURO. ALERTA: BAE Systems -13.22%, 15o dia consecutivo em STOP DURO. Amgen -13.66%, 5o dia em violacao.'}],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-15 | EUR -4.71 caixa 0.12 | USD -22.72 caixa 60.21 | Schneider recupera -9.53% | BAE 15o dia -13.22% | Amgen 5o dia -13.66%')
