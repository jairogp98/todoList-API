from flask_restx import marshal
from flask import Flask, Response, jsonify
from app.api.resources.tasks.dto import TaskDto
from app.database.models.task import Task
from datetime import datetime
from ....database.db import db

class Business:

    @staticmethod
    def post_task(data: dict):
        try:
            created_at = datetime.now()
            new_task = Task(data['title'], data['description'], data['user_id'], data['expiration_date'], data['status'], data['priority'], created_at, data['active'])

            db.session.add(new_task)
            db.session.commit()

            return marshal(new_task, TaskDto.get_task), 200

        except Exception as e:
            return Response (f"ERROR: {e}", 500)

    @staticmethod
    def put_task(data: dict):
        try:
            task = Task.query.filter_by(id = data['id']).first()
            if task:
                for key, value in data.items():
                    if (value is not None):
                        setattr(task, key, value)
            else:
                return Response ("Task not found", 404)

            db.session.commit()

            updated_task = Task.query.filter_by(id = data['id']).first()

            return marshal(updated_task, TaskDto.get_task), 200

        except Exception as e:
            return Response (f"ERROR: {e}", 500)

    @staticmethod
    def get_tasks_by_user(user_id):
        """Getting tasks by user id"""
        try:
            tasks = Task.query.filter_by(user_id = user_id).filter(Task.active != False).all()
            if tasks:
                return marshal(tasks, TaskDto.get_task), 200
            else:
                return Response ("User doesn't have any tasks yet.", 200)

        except Exception as e:
            return Response (f"ERROR: {e}", 500)