from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from flask_jwt_extended import jwt_required
from ..auth.business import token_is_revoked
from .dto import UserDto


@ns.route("/")
class Users(Resource):
    @ns.response(200, 'Success',UserDto.get_users)
    @ns.doc(security=['jwt'], description = 'Get all the users')
    @ns.marshal_with(UserDto.get_users)
    @jwt_required()
    @token_is_revoked
    def get(self):
        return Business.get_users()

    @ns.response(200, 'Success',UserDto.get_users)
    @ns.doc(security=['jwt'], description = 'Create a new user')
    @ns.expect(UserDto.post_users)
    def post(self):
        return Business.post_users(ns.payload)

    @ns.response(200, 'Success',UserDto.get_users)
    @ns.doc(security=['jwt'], description = 'Edit an existing user')
    @ns.expect(UserDto.put_users)
    @jwt_required()
    @token_is_revoked
    def put(self):
        return Business.put_users(ns.payload)
        


@ns.route("/deactivate/<id>")
class DeactivateUser(Resource):
    @ns.doc(security=['jwt'], description = 'Deactivate an user by the given ID')
    @jwt_required()
    @token_is_revoked
    def patch(self, id):
        return Business.patch_user_deactivate(id)


@ns.route("/<id>")
class UserById(Resource):
    @ns.response(200, 'Success',UserDto.get_users)
    @ns.doc(security=['jwt'],description = 'Get a user by the given ID')
    @jwt_required()
    @token_is_revoked
    def get(self, id):
        return Business.get_user_by_id(id)