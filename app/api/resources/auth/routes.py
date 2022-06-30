import json
from flask import jsonify
from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from .dto import AuthDto

@ns.route("/")
class Login(Resource):
    @ns.expect(AuthDto.post_auth)
    def post(self):
        return Business.login(request)

@ns.route("/logout")
class Logout(Resource):

    def delete(self):
        return Business.logout()

@ns.doc(security=['jwt'])
@ns.route("/refresh")
class Refresh(Resource):

    def post(self):
        return Business.refresh()
