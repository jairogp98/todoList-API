from flask_restx import Resource
from flask import request
from . import ns
from .business import Business
from flask_jwt_extended import jwt_required
from ..auth.business import token_is_revoked
from .dto import TaskDto


@ns.route("/")
class Tasks(Resource):
    @ns.response(200, 'Success',TaskDto.get_task)
    @ns.doc(security=['jwt'], description = 'Create a new task')
    @ns.expect(TaskDto.post_task)
    @jwt_required()
    @token_is_revoked
    def post(self):
        """Create a new task"""
        return Business.post_task(ns.payload)

    @ns.response(200, 'Success',TaskDto.get_task)
    @ns.doc(security=['jwt'], description = 'Edit or update an existing task')
    @ns.expect(TaskDto.put_task)
    @jwt_required()
    @token_is_revoked
    def put(self):
        return Business.put_task(ns.payload)

@ns.route("/byUser/<user_id>")
class TasksByUser(Resource):
    @ns.response(200, 'Success',TaskDto.get_task)
    @ns.doc(security=['jwt'],description = 'Get tasks by user ID')
    @jwt_required()
    @token_is_revoked
    def get(self, user_id):
        return Business.get_tasks_by_user(user_id)

@ns.route("/byTask/<task_id>")
class TaskById(Resource):
    
    @ns.doc(security=['jwt'], description = 'Delete a task by the given ID')
    @jwt_required()
    @token_is_revoked
    def patch(self, task_id):
        return Business.delete_task(task_id)

    @ns.response(200, 'Success',TaskDto.get_task)
    @ns.doc(security=['jwt'], description = 'Get the data of an especific task by the given ID')
    @jwt_required()
    @token_is_revoked
    def get(self, task_id):
        return Business.get_task_by_id(task_id)

@ns.route("/validity/<user_id>")
class TaskById(Resource):
    @ns.response(200, 'Success',TaskDto.get_task)
    @ns.doc(security=['jwt'], description = 'Get the tasks that are expired or about to expire')
    @jwt_required()
    @token_is_revoked
    def get(self, user_id):
        return Business.get_expired_tasks(user_id)