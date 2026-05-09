import json

with open('data/trading_data.json', encoding='utf-8') as f:
    data = json.load(f)

dates = sorted([k for k in data.keys() if len(k)==10 and k[4]=='-'])
latest = dates[-1]

js = 'const TRADING_DATA = ' + json.dumps(data, indent=2, ensure_ascii=False) + ';\n'
js += 'const DATA_DATES = ' + json.dumps(dates) + ';\n'
js += 'const LATEST_DATE = "' + latest + '";\n'

with open('data.js', 'w', encoding='utf-8') as f:
    f.write(js)

print('OK -', len(dates), 'dias:', dates)