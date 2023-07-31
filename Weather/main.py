# Cотрудникам надо узнать погоду в Лондоне, Шереметьево и Череповце.

import requests

urls = ['https://wttr.in/London?nTqu&lang=en',
        'https://wttr.in/Шереметьево?nTqu&lang=en',
        'https://wttr.in/Череповец?nTqM&lang=ru']


def request(url: str) -> object:
    """Получаем ссылку на погоду и город. Возвращаем объект - погоду в этом городе"""
    response = requests.get(url)
    return response if not response.raise_for_status() else print('Error connect')


for url in urls:
    print(request(url).text)
