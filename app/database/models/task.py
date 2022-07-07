from app.database.db import db
from .users import Users

class Task (db.Model):

    id = db.Column(db.Integer, primary_key =True, nullable = False)
    title = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100))
    user_id = db.Column(db.Integer(), db.ForeignKey(Users.id, ondelete='CASCADE', onupdate='CASCADE'), nullable = False)
    expiration_date = db.Column(db.Date, nullable = False)
    status = db.Column(db.String(100), nullable = False)
    priority = db.Column(db.String(100), nullable = False)
    created_at = db.Column(db.DateTime, nullable = False)
    active = db.Column(db.Boolean, nullable = False)

    def __init__(self, title, description, user_id, expiration_date, status, priority, created_at, active):

        self.title = title
        self.description = description 
        self.user_id = user_id
        self.expiration_date = expiration_date
        self.status = status
        self.priority = priority
        self.created_at = created_at
        self.active = active