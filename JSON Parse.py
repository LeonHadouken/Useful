import requests
import json

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
input = input
cur_list = {}
val_list = []
for item in data['Valute']:
    cur_list.append(item)
for cur in cur_list:
    val_list.append(data['Valute'][cur]['NumCode'])
if  input in val_list:
    print(input)
if input in cur_list:
    print(input)