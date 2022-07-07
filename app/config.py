from dotenv import dotenv_values
from datetime import timedelta

env = dotenv_values('.env')
class Config:
    SECRET_KEY = env['SECRET_KEY']
    JWT_SECRET_KEY = env['SECRET_KEY']
    FLASK_ENV = env['FLASK_ENV']
    FLASK_DEBUG=env['FLASK_DEBUG']
    SQLALCHEMY_DATABASE_URI = env['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = env['SQLALCHEMY_TRACK_MODIFICATIONS']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=20)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    TOKEN_EXPIRE_HOURS= 0
    TOKEN_EXPIRE_MINUTES = 0
