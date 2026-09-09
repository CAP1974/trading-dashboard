import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-09'] = {
    'eur': {'saldo':84.09,'caixa':0.12,'lucro':-5.36,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':435.20,'lucro':-0.44,'pct':-1.00,'trust':'r','valor':43.52,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':289.55,'lucro':-1.17,'pct':-4.87,'trust':'r','valor':22.87,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':18.970,'lucro':-3.75,'pct':-17.58,'trust':'r','valor':17.58,'delta':None}]},
    'usd': {'saldo':252.36,'caixa':76.00,'lucro':-18.48,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':491.39,'lucro':0.11,'pct':0.37,'trust':'v','valor':29.48,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':274.57,'lucro':-2.43,'pct':-4.24,'trust':'r','valor':54.91,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':390.81,'lucro':-5.30,'pct':-10.15,'trust':'r','valor':46.90,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.16,'abertura':180.60,'atual':147.56,'lucro':-5.28,'pct':-18.27,'trust':'r','valor':23.62,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.11,'abertura':245.75,'atual':195.06,'lucro':-5.58,'pct':-20.64,'trust':'r','valor':21.45,'delta':None}]},
    'eventos':[{'tipo':'diario','nota':'Sem trades. Caixa inalterada. ALERTA: BAE Systems piora para -17.58%, 11o dia consecutivo em STOP DURO sem accao. NOVA VIOLACAO: Amgen atinge -10.15%, cruzando o STOP DURO por primeira vez. Duas posicoes agora em violacao activa.'}],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-09 | EUR -5.36 caixa 0.12 | USD -18.48 caixa 76.00 | BAE -17.58% 11o dia | Amgen NOVA violacao -10.15%')
