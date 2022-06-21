from ....database.models.users import Users
import bcrypt
from flask import Response, jsonify, make_response
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity, jwt_required


class Business():

    @staticmethod
    def login(data):

        try:
            email = data.json.get("email")
            password = data.json.get("password")
            user = Users.query.filter_by(email = email).first()

            if user:
                password = password.encode('utf-8')
                hash = user.password.encode('utf-8')
                if bcrypt.checkpw(password, hash):
                    access_token = create_access_token(identity=user.email)
                    refresh_token = create_refresh_token(identity=user.email)
                    return make_response(jsonify(access_token=access_token, refresh_token = refresh_token), 200)
            else:
                return Response("User not found", 406)
        except Exception as e:
            return Response(f"Error: {e}", 500)

    @staticmethod
    @jwt_required(refresh=True)
    def refresh():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token)

