import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-03'] = {
    'eur': {'saldo':86.31,'caixa':0.12,'lucro':-3.14,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':452.30,'lucro':1.27,'pct':2.89,'trust':'v','valor':45.23,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':286.75,'lucro':-1.38,'pct':-5.74,'trust':'r','valor':22.66,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':19.765,'lucro':-3.03,'pct':-14.21,'trust':'r','valor':18.30,'delta':None}]},
    'usd': {'saldo':261.07,'caixa':76.00,'lucro':-9.77,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':509.53,'lucro':1.21,'pct':4.12,'trust':'v','valor':30.58,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':443.86,'lucro':1.06,'pct':2.03,'trust':'v','valor':53.26,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':281.86,'lucro':-0.97,'pct':-1.69,'trust':'r','valor':56.37,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.16,'abertura':180.60,'atual':149.68,'lucro':-4.95,'pct':-17.13,'trust':'r','valor':23.95,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.11,'abertura':245.75,'atual':190.20,'lucro':-6.12,'pct':-22.64,'trust':'r','valor':20.91,'delta':None}]},
    'eventos':[{'tipo':'diario','nota':'Sem trades. Caixa inalterada. ALERTA: BAE Systems -14.21%, 7o dia consecutivo em STOP DURO sem accao.'}],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-03 | EUR -3.14 caixa 0.12 | USD -9.77 caixa 76.00 | BAE -14.21% 7o dia')
