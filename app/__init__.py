from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
from app.config import Config
app.config.from_object(Config)
jwt = JWTManager(app)

def init():

    from app.api import bp_api

    app.register_blueprint(bp_api)
    return app
