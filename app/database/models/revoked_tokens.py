from app.database.db import db

class RevokedTokens (db.Model):

    id = db.Column(db.Integer, primary_key =True)
    jti = db.Column(db.String(200))
    created_at = db.Column(db.DateTime)

    def __init__(self, jti, created_at):
        self.jti = jti
        self.created_at = created_at
