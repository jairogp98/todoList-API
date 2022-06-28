from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from flask_jwt_extended import get_jwt_identity, jwt_required
from ..auth.business import token_is_revoked


@ns.route("/")
class Users(Resource):
    @jwt_required()
    @token_is_revoked
    def get(self):
        return Business.get_users()

    @jwt_required()
    @token_is_revoked
    def post(self):
        return Business.post_users(request)

@ns.route("/<id>")
class UserById(Resource):

    @jwt_required()
    @token_is_revoked
    def get(self, id):
        return Business.get_user_byId(id)