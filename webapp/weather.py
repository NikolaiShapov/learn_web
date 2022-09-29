from flask import current_app #для работы app.config.from_pyfile('config.py') из __init__.py

import requests

#http://api.worldweatheronline.com/premium/v1/weather.ashx?key=c9af2cee1cb24c99987113909221209&q=Moscow,Russia&format=json&num_of_days=1&lang=ru
def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }
    try:
        result = requests.get(weather_url,params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except (IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print('Erro Ethernet.')
        return False


if __name__ == '__main__':
    w = weather_by_city('Kalyga')
    print(w)
