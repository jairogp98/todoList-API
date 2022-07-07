from app.database.db import db
import jwt
from flask import current_app
from datetime import datetime, timedelta, timezone

class Users (db.Model):

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    active = db.Column(db.Boolean)

    def __init__(self, name, lastname, email, password, active):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
        self.active = active

    def encode_access_token(self):
        now = datetime.now(timezone.utc)
        token_age_h = current_app.config.get("TOKEN_EXPIRE_HOURS")
        token_age_m = current_app.config.get("TOKEN_EXPIRE_MINUTES")
        expire = now + timedelta(hours=token_age_h, minutes=token_age_m)
        self.session_code = int(str(datetime.timestamp(expire))[-4:])
        db.session.commit()
        payload = dict(exp=expire, iat=now, sub=str(self.id), code=self.session_code)
        key = current_app.config.get("SECRET_KEY")
        return jwt.encode(payload, key, algorithm="HS256")