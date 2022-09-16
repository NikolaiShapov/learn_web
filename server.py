from distutils.log import debug
from re import T
from flask import Flask, render_template
from weather import weather_by_city
from python_org_news import get_python_news
app = Flask(__name__)

@app.route('/')
def index():
    title = 'Новости Python'
    weather = weather_by_city('Калуга')
    news_list = get_python_news()
    return render_template('index.html',
                            page_title = title,
                            weather_text = weather,
                            news_list = news_list)

if __name__ == '__main__':
    app.run(debug = True) # Режим Дебагер
