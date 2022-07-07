from flask_restx import marshal
from flask import Flask, Response, jsonify
from app.database.db import db
from app.database.models.users import Users
import bcrypt
from .dto import UserDto
class Business:

    @staticmethod
    def get_users():
        try:
            users = Users.query.order_by(Users.id.asc()).all()
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
    def get_user_by_id(id):
        try:
            user = Users.query.filter_by(id =id).first()
            if user is not None:
                return marshal(user, UserDto.get_users), 200
            else:
                return Response ("Id user not found", 404)

        except Exception as e:
            return Response (f"ERROR: {e}", 500)

    @staticmethod
    def put_users(data:dict):
        try:
            user = Users.query.filter_by(id = data['id']).first()

            if user is not None:
                for key, value in data.items():
                    if (value is not None):
                        setattr(user, key, value)
            else:
                return Response ("User not found", 404)
            db.session.commit()

            updated_user = Users.query.filter_by(id = data['id']).first()

            return marshal(updated_user, UserDto.get_users), 200

        except Exception as e:
            return Response (f"ERROR: {e}", 500)

    @staticmethod
    def patch_user_deactivate(id):
        try:
            user = Users.query.filter_by(id = id).first()

            if user is not None:
                setattr(user, "active", 0)
            else:
                return Response ("User not found", 200)
            db.session.commit()

            return Response (f"User {user.email} has been succesfully deactivate.",200)

        except Exception as e:
            return Response (f"ERROR: {e}", 500)