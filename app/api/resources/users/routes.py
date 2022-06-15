import json
from flask import jsonify
from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
import flask_jwt
from flask_jwt import jwt_required


@ns.route("/")
class Users(Resource):

    @jwt_required()
    def get(self):
        smth = flask_jwt.current_identity
        print (smth)
        return Business.get_users()

    def post(self):
        return Business.post_users(request)

@ns.route("/login")
class LoginUsers(Resource):
    
    def post(self):
        return Business.login_users(request)
