import json
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', encoding='utf-8') as f:
    d = json.load(f)
d['2026-09-14'] = {
    'eur': {'saldo':83.99,'caixa':0.12,'lucro':-5.46,'positions':[
        {'name':'Allianz','mkt':'EUR','vol':0.1,'abertura':439.60,'atual':444.00,'lucro':0.44,'pct':1.00,'trust':'v','valor':44.40,'delta':None},
        {'name':'Schneider','mkt':'EUR','vol':0.079,'abertura':304.39,'atual':271.20,'lucro':-2.62,'pct':-10.90,'trust':'r','valor':21.42,'delta':None},
        {'name':'BAE Systems','mkt':'EUR','vol':0.8,'abertura':22.650,'atual':19.400,'lucro':-3.28,'pct':-15.38,'trust':'r','valor':18.05,'delta':None}]},
    'usd': {'saldo':251.42,'caixa':60.21,'lucro':-19.65,'positions':[
        {'name':'Microsoft','mkt':'USD','vol':0.06,'abertura':489.51,'atual':505.67,'lucro':0.97,'pct':3.30,'trust':'v','valor':30.34,'delta':None},
        {'name':'CME','mkt':'USD','vol':0.2,'abertura':286.71,'atual':280.39,'lucro':-1.26,'pct':-2.20,'trust':'r','valor':56.08,'delta':None},
        {'name':'Amgen','mkt':'USD','vol':0.12,'abertura':434.99,'atual':381.61,'lucro':-6.41,'pct':-12.28,'trust':'r','valor':45.79,'delta':None},
        {'name':'SpaceX','mkt':'USD','vol':0.24,'abertura':171.10,'atual':148.06,'lucro':-5.54,'pct':-13.49,'trust':'r','valor':35.53,'delta':None},
        {'name':'Cerebras Systems','mkt':'USD','vol':0.13,'abertura':237.55,'atual':180.50,'lucro':-7.41,'pct':-24.00,'trust':'r','valor':23.47,'delta':None}]},
    'eventos':[
        {'tipo':'aporte','ticker':'SPCX','ativo':'SpaceX','mkt':'USD',
         'nota':'APORTE SPCX +0.08 @ 152.09 -- vol total 0.24 preco medio 171.10'},
        {'tipo':'diario','nota':'Aporte SpaceX para melhorar preco medio. Caixa USD confere: 72.38-12.17=60.21. ALERTA: BAE Systems -15.38%, 14o dia consecutivo em STOP DURO. Amgen -12.28%, 4o dia em violacao. NOVA VIOLACAO: Schneider atinge -10.90%, cruzando o STOP DURO. Ja sao tres posicoes em violacao activa (BAE, Amgen, Schneider), fora da excecao historica SpaceX/Cerebras.'}
    ],
    'posicoes_fechadas':[]
}
with open('C:/Users/Utilizador/trading-dashboard/data/trading_data.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)
print('OK 2026-09-14 | EUR -5.46 caixa 0.12 | USD -19.65 caixa 60.21 | APORTE SPCX | BAE 14o dia | Amgen 4o dia | Schneider NOVA violacao -10.90%')
