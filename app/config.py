from dotenv import dotenv_values


class Config:

    env = dotenv_values('.env')
    
    SECRET_KEY = env['SECRET_KEY']
    FLASK_ENV = env['FLASK_ENV']
    FLASK_DEBUG=env['FLASK_DEBUG']
    SQLALCHEMY_DATABASE_URI = env['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS = env['SQLALCHEMY_TRACK_MODIFICATIONS']
