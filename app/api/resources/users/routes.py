import json
from flask import jsonify
from flask_restx import Resource
from flask import request
from . import ns
from .business import Business


@ns.route("/")
class Users(Resource):

    def get(self):
        return Business.get_users()

    def post(self):
        return Business.post_users(request)
