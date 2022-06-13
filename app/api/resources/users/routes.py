import json
from flask import jsonify
from flask_restx import Resource
from flask import request
from . import ns

@ns.route('/')
class Users(Resource):

    def get(self):
        return "GET"

    def post(self):
        name = request.json['name']
        return name