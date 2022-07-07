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