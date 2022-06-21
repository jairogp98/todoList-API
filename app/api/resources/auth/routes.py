import json
from flask import jsonify
from flask_restx import Resource
from flask import request
from . import ns
from .business import Business


@ns.route("/")
class Auth(Resource):

    def post(self):
        return Business.login(request)

@ns.route("/refresh")
class Auth(Resource):

    def post(self):
        return Business.refresh()