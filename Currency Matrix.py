import requests
from datetime import datetime
import json
import sys

now = datetime.now()
currency = input('Введите валюту').upper()
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
print(f'Курс рубля на {now.strftime("%d.%m.%Y %H:%M:%S")}')
print('-' * 33)
print(currency, end=' ')
print(data['Valute'][currency]['NumCode'], end=' ')
print(float('{:.2f}'.format(data['Valute'][currency]['Value'])))
