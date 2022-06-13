import os

class Config:

    SECRET_KEY= os.environ.get("SECRET_KEY")
    FLASK_ENV = os.environ.get("FLASK_ENV")