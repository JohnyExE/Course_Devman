# Cотрудникам надо узнать погоду в Лондоне, Шереметьево и Череповце.

import requests

urls = ['https://wttr.in/London?nTqu&lang=en',
        'https://wttr.in/Шереметьево?nTqu&lang=en',
        'https://wttr.in/Череповец?nTqM&lang=ru']

if __name__ == '__main__':
    def request(weather_url: str) -> object:
        """Получаем ссылку на погоду. Возвращаем объект - погоду"""
        return requests.get(weather_url)

for city in urls:
    print(request(city).text)

