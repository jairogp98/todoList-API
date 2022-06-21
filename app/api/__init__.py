from flask import Blueprint
from flask_restx import Api, Namespace
from .resources import namespaces

bp_api = Blueprint("api", "__name__", url_prefix="/api")

api = Api(bp_api)
for ns in namespaces:
    api.add_namespace(ns)
    