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
        """Create a new task"""
        return Business.post_task(ns.payload)

    @ns.expect(TaskDto.put_task)
    @jwt_required()
    @token_is_revoked
    def put(self):
        return Business.put_task(ns.payload)



@ns.doc(security=['jwt'])
@ns.route("/<user_id>")
class TasksByUser(Resource):

    @jwt_required()
    @token_is_revoked
    def get(self, user_id):
        """Getting tasks by user id"""
        return Business.get_tasks_by_user(user_id)
