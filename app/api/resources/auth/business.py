from ....database.models.users import Users
import bcrypt
from flask import Response, jsonify, make_response
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended import get_jwt
from datetime import timedelta
from datetime import datetime
from ....database.models.revoked_tokens import RevokedTokens
from ....database.db import db

#Creating a decorator to check if the current token was revoked.
def token_is_revoked(func): 
    def wrapper(*args, **kwargs):
        jti = get_jwt()["jti"]

        token = RevokedTokens.query.filter_by(jti = jti).first()
        if token is not None:
            return Response("This token was revoked.", 401)
        else:
            return func(*args, **kwargs)
                
    return wrapper
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
                    return make_response(jsonify(access_token=access_token, refresh_token = refresh_token, user_id = user.id), 200)
            else:
                return Response("User not found", 406)
        except Exception as e:
            return Response(f"Error: {e}", 500)

    @staticmethod
    @jwt_required()
    def logout():
        try:
            jti = get_jwt()["jti"]
            today = datetime.now()

            new_token = RevokedTokens(jti, today)
            db.session.add(new_token)
            db.session.commit()

            return jsonify(msg="Access token revoked")

        except Exception as e:
            return Response(f"Error: {e}", 500)

    @staticmethod
    @jwt_required(refresh=True)
    def refresh():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token)
