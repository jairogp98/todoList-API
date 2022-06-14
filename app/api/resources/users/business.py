from flask import Flask, Response, jsonify
from app.database.db import db
from app.database.models.users import Users
import json
class Business:

    @staticmethod
    def get_users():
        response = list()
        try:
            users = Users.query.all()
            
            for user in users:
                response.append({'id':user.id,'name':user.name, 'lastname':user.lastname})
        except Exception as e:
            return Response (f"ERROR: {e}", 500)

        return response
    @staticmethod
    def post_users(data):
        try:
            name = data.json['name']
            lastname = data.json['lastname']
            email = data.json['email']
            password = data.json['password']
            active = data.json['active']

            exists = Users.query.filter_by(email = email).first()

            if (exists):
                return Response('That email already exists', 406)

            new_user = Users(name, lastname, email, password, active)
            db.session.add(new_user)
            db.session.commit()

        except Exception as e:
            return Response (f"ERROR: {e}", 500)

        return Response('User created succesfully', 200)
