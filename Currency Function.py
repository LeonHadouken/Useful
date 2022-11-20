import sys


def show_currency(ti=1000, val=**, 'help'):
    '''ИНФО'''  # Здесь находится описание функции (show_curency.__doc__)
                # Вывести время (API запрос)
                # Получить данные по валютам
    if len(sys.argv) < 1:  # Если аргументов не было ведено через терминал
        val = ['USD', 'EUR']  # Вывести по умолчанию, курс доллара, курс евро и документацию
        for currency in val:
            # USD
            # EUR
        Print(show_curency.__doc__)
    else:
        for currency in sys.args:  # Начинаем итерацию по всем аргументам
            if currency.isdigit():  # Если аргумент числовой
             # Искать в базе валют по номеру
             # Собрать строку для вывода в формате (ВАЛЮТА, КОД ВАЛЮТЫ, КУРС)
            elif currency.isalpha() and arg != 'help':  # Если аргумент буквенный и это не help
                currency = currency.upper()
             # Искать в базе данных по наименованию валюты
             # Собрать строку для вывода в формате (ВАЛЮТА, КОД ВАЛЮТЫ, КУРС)
            else:
                Print(show_curency.__doc__)
