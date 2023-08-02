# Cотрудникам надо узнать погоду в Лондоне, Шереметьево и Череповце.

import requests

urls = ['https://wttr.in/London?nTqu&lang=en',
        'https://wttr.in/Шереметьево?nTqu&lang=en',
        'https://wttr.in/Череповец?nTqM&lang=ru']


def request_weather(weather_url: str) -> object:
    """Получаем ссылку на погоду. Возвращаем объект - погоду"""
    return requests.get(weather_url)


if __name__ == '__main__':
    for city in urls:
        print(request_weather(city).text)

