from app.database.db import db

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