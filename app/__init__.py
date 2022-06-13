from flask import Flask

app = Flask(__name__)
from app.config import Config
app.config.from_object(Config)

def init():
    from app.api import bp_api
    app.register_blueprint(bp_api)
    return app