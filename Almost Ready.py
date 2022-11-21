import sys
import requests
from datetime import datetime
import subprocess, platform
# Парсим время и список курсов валют
now = datetime.now()
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
# Создаем список валют
currency_by_char = data['Valute']
# Создаем словарь с соответствующими данными по каждой из валют
currency_by_num = {
    currency_data['NumCode']: currency_data
    for _, currency_data in currency_by_char.items()
}
# Функция предназначена для вывода актуального курса валют
# Пока не понял, как прикрутить таймер для обновления строк
def show_currency(*args, ti=1000):
    # НАПИСАТЬ ИНФО
    '''ИНФО'''
    timer = ti
    values = []
    for arg in args:
        if arg.isalpha:
            arg = arg.upper()
            values.append(arg)
        elif arg.isdigit:
            values.append(arg)
    print(f'Курс рубля на {now.strftime("%d.%m.%Y %H:%M:%S")}')
    print('-' * 33)
    if len(args) < 1:       # Функция запускается в дефолтном режиме
        print(data['Valute']['USD']['CharCode'], end=' ')
        print(data['Valute']['USD']['NumCode'], end=' ')
        print(float('{:.2f}'.format(data['Valute']['USD']['Value'])), end='\r')
        print(data['Valute']['EUR']['CharCode'], end=' ')
        print(data['Valute']['EUR']['NumCode'], end=' ')
        print(float('{:.2f}'.format(data['Valute']['EUR']['Value'])), end='\r')
    elif len(sys.argv) > 0:
        for _ in sys.argv:
            for item in currency_by_char:
                if item in values:
                    print(currency_by_char[item]['CharCode'], end=' ')
                    print(data['Valute'][item]['NumCode'], end=' ')
                    print(float('{:.2f}'.format(data['Valute'][item]['Value'])))
                    values.remove(item)
            for item in currency_by_num:
                if item in values:
                    print(currency_by_num[item]['CharCode'], end=' ')
                    print(currency_by_num[item]['NumCode'], end=' ')
                    print(float('{:.2f}'.format(currency_by_num[item]['Value'])))
                    values.remove(item)
    print(show_currency.__doc__)
show_currency('eur','usd','036')
