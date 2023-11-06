import json
import requests
from config import keys

class ConvertionExeption(Exception):
    pass

class CryptoConverter():
    @staticmethod
    def converter(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeption('Вы указали одну валюту два раза')

        # проверка на правильность ввода. если не удаётся присвоить переменной значение
        # в виду того что введенный пользователем ключ отсутстсвует в списке вариантов, то ошибка

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionExeption('Вы неверно указали валюту 1')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConvertionExeption('Вы неверно указали валюту 2')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'третьим значением должно быть число {amount}')

        r = requests.get(f'http://apilayer.net/api/convert?access_key=438a9b40c3c6c24bbc6eb470a11d5d56&from={keys[quote]}&to={keys[base]}&amount={int(amount)}')
        anser = json.loads(r.content)['result']
        print(anser)
        return anser

    # {'success': True, 'terms': 'https://currencylayer.com/terms', 'privacy': 'https://currencylayer.com/privacy', 'query': {'from': 'EUR', 'to': 'GBP', 'amount': 100},
    # 'info': {'timestamp': 1699303983, 'quote': 0.868502}, 'result': 86.8502}