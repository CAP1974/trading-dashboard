import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-11'] = {
    'eur': {'saldo':84.88,'caixa':0.12,'lucro':-4.57,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':441.50,'lucro':0.19,'pct':0.43,'trust':'v','valor':44.15,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':291.15,'lucro':-1.04,'pct':-4.33,'trust':'r','valor':23.00,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':18.970,'lucro':-3.72,'pct':-17.44,'trust':'r','valor':17.61,'delta':None}]},
    'usd': {'saldo':251.61,'caixa':72.38,'lucro':-19.46,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':495.99,'lucro':0.39,'pct':1.33,'trust':'v','valor':29.76,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':275.59,'lucro':-2.22,'pct':-3.87,'trust':'r','valor':55.12,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':377.14,'lucro':-6.94,'pct':-13.30,'trust':'r','valor':45.26,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.16,'abertura':180.60,'atual':151.22,'lucro':-4.71,'pct':-16.30,'trust':'r','valor':24.19,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.13,'abertura':237.55,'atual':191.51,'lucro':-5.98,'pct':-19.37,'trust':'r','valor':24.90,'delta':None}]},
    'eventos':[{'tipo':'diario','nota':'Sem trades. Dividendo AMGN +0.21$ (caixa 72.17->72.38, confere). ALERTA: BAE Systems piora para -17.44%, 13o dia consecutivo em STOP DURO sem accao. Amgen -13.30%, 3o dia em violacao, tambem a piorar.'}],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-11 | EUR -4.57 caixa 0.12 | USD -19.46 caixa 72.38 (div AMGN +0.21) | BAE -17.44% 13o dia | Amgen -13.30% 3o dia')
