from distutils.log import debug
from re import T
from flask import Flask
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    weather = weather_by_city('Калуга')
    if weather:
        return f"Погода: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        return 'Server weather no connect!'

if __name__ == '__main__':
    app.run(debug = True) # Режим Дебагер
