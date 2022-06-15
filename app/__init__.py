from flask import Flask
from flask_jwt import JWT


app = Flask(__name__)
from app.config import Config

app.config.from_object(Config)

from .api.resources.auth.business import authenticate, identity
jwt = JWT(app, authenticate, identity)

def init():
    from app.api import bp_api

    app.register_blueprint(bp_api)
    return app
