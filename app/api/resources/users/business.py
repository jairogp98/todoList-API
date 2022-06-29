from flask_restx import marshal
from flask import Flask, Response, jsonify
from app.database.db import db
from app.database.models.users import Users
import bcrypt
from .dto import UserDto
class Business:

    @staticmethod
    def get_users():
        response = list()
        try:
            users = Users.query.all()
        except Exception as e:
            return Response (f"ERROR: {e}", 500)

        return users

    @staticmethod
    def post_users(data: dict):
        try:
            name = data['name']
            lastname = data['lastname']
            email = data['email']
            password = data['password'].encode('utf-8')
            hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
            active = data['active']

            exists = Users.query.filter_by(email = email).first()

            if (exists):
                return Response('That email already exists', 406)

            new_user = Users(name, lastname, email, hashed_password.decode('utf-8'), active)
            db.session.add(new_user)
            db.session.commit()

            return marshal(new_user, UserDto.get_users), 200

        except Exception as e:
            return Response (f"ERROR: {e}", 500)


    @staticmethod
    def get_user_byId(id):
        try:
            user = Users.query.filter_by(id =id).first()
            if user is not None:
                return marshal(user, UserDto.get_users), 200
            else:
                return Response ("Id user not found", 204)

        except Exception as e:
            return Response (f"ERROR: {e}", 500)