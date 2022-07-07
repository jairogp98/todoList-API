from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from flask_jwt_extended import jwt_required
from ..auth.business import token_is_revoked
from .dto import UserDto

@ns.doc(security=['jwt'])
@ns.route("/")
class Users(Resource):
    @ns.marshal_with(UserDto.get_users)
    @jwt_required()
    @token_is_revoked
    def get(self):
        return Business.get_users()

    @ns.expect(UserDto.post_users)
    def post(self):
        return Business.post_users(ns.payload)

    @ns.expect(UserDto.put_users)
    @jwt_required()
    @token_is_revoked
    def put(self):
        return Business.put_users(ns.payload)
        

@ns.doc(security=['jwt'])
@ns.route("/deactivate/<id>")
class DeactivateUser(Resource):
    @jwt_required()
    @token_is_revoked
    def patch(self, id):
        return Business.patch_user_deactivate(id)

@ns.doc(security=['jwt'])
@ns.route("/<id>")
class UserById(Resource):
    @jwt_required()
    @token_is_revoked
    def get(self, id):
        return Business.get_user_by_id(id)