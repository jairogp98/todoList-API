import json
from flask import jsonify
from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from .dto import AuthDto

@ns.route("/")
class Login(Resource):
    @ns.doc(description = 'Login with valid credentials to get a JWT token')
    @ns.expect(AuthDto.post_auth)
    def post(self):
        return Business.login(request)

@ns.route("/logout")
class Logout(Resource):
    @ns.doc(security=['jwt'], description = 'Logout the user by destroying the current token')
    def post(self):
        return Business.logout()


@ns.route("/refresh")
class Refresh(Resource):
    @ns.doc(security=['jwt'], description = 'Refresh the current JWT token')
    def post(self):
        return Business.refresh()
