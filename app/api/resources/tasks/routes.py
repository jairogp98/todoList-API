from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from flask_jwt_extended import jwt_required
from ..auth.business import token_is_revoked
from .dto import TaskDto

@ns.doc(security=['jwt'])
@ns.route("/")
class Tasks(Resource):
    @ns.expect(TaskDto.post_task)
    @jwt_required()
    @token_is_revoked
    def post(self):
        return Business.post_task(ns.payload)