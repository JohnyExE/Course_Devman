# Cотрудникам надо узнать погоду в Лондоне, Шереметьево и Череповце.

import requests

urls = ['https://wttr.in/London?nTqu&lang=en',
        'https://wttr.in/Шереметьево?nTqu&lang=en',
        'https://wttr.in/Череповец?nTqM&lang=ru']


def request(weather_url: str) -> object:
    """Получаем ссылку на погоду и город. Возвращаем объект - погоду в этом городе"""
    return requests.get(weather_url)


for city in urls:
    print(request(city).text)
