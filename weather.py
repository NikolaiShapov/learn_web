import requests
import setting

#http://api.worldweatheronline.com/premium/v1/weather.ashx?key=c9af2cee1cb24c99987113909221209&q=Moscow,Russia&format=json&num_of_days=1&lang=ru
def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': setting.API_KEY,
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru'
    }
    result = requests.get(weather_url,params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except (IndexError, TypeError):
                return False
    return weather

if __name__ == '__main__':
    w = weather_by_city('Kalyga')
    print(w)
