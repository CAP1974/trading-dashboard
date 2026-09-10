import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-10'] = {
    'eur': {'saldo':84.67,'caixa':0.12,'lucro':-4.78,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':440.20,'lucro':0.06,'pct':0.14,'trust':'v','valor':44.02,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':287.75,'lucro':-1.30,'pct':-5.41,'trust':'r','valor':22.74,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':19.205,'lucro':-3.54,'pct':-16.60,'trust':'r','valor':17.79,'delta':None}]},
    'usd': {'saldo':250.93,'caixa':72.17,'lucro':-19.93,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':492.51,'lucro':0.19,'pct':0.65,'trust':'v','valor':29.56,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':273.92,'lucro':-2.56,'pct':-4.46,'trust':'r','valor':54.78,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':382.31,'lucro':-6.32,'pct':-12.11,'trust':'r','valor':45.88,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.16,'abertura':180.60,'atual':148.25,'lucro':-5.18,'pct':-17.92,'trust':'r','valor':23.72,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.13,'abertura':237.55,'atual':190.83,'lucro':-6.06,'pct':-19.62,'trust':'r','valor':24.82,'delta':None}]},
    'eventos':[
        {'tipo':'aporte','ticker':'CRBS','ativo':'Cerebras Systems','mkt':'USD',
         'nota':'APORTE CRBS +0.02 @ 192.49 -- vol total 0.13 preco medio 237.55'},
        {'tipo':'diario','nota':'Aporte Cerebras para melhorar preco medio. Caixa USD confere: 76.00-3.85=72.15 vs 72.17 informado. ALERTA: BAE Systems -16.60%, 12o dia consecutivo em STOP DURO sem accao. Amgen -12.11%, 2o dia em violacao.'}
    ],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-10 | EUR -4.78 caixa 0.12 | USD -19.93 caixa 72.17 | APORTE CRBS 0.02@192.49 | BAE -16.60% 12o dia | Amgen -12.11% 2o dia')
