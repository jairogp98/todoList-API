import json
from flask import jsonify
from flask_restx import Resource
from flask import request
from . import ns
from .business import Business


@ns.route("/")
class Login(Resource):

    def post(self):
        return Business.login(request)

@ns.route("/logout")
class Logout(Resource):

    def delete(self):
        return Business.logout()

@ns.route("/refresh")
class Refresh(Resource):

    def post(self):
        return Business.refresh()
