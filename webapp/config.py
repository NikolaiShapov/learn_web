import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__)) #получаем полный путь до файла __file__, который и есть config.py

WEATHER_DEFAULT_CITY = "Moscow,Russia"
WEATHER_API_KEY = "c9af2cee1cb24c99987113909221209"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
#print(SQLALCHEMY_DATABASE_URI)

SECRET_KEY = "hewlkh&*b3^bFLJWBHJKBE23"
REMEMBER_COOKIE_DURATION = timedelta(days=5)

SQLALCHEMY_TRACK_MODIFICATIONS = False
