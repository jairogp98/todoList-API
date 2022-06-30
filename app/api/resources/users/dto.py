from flask_restx import Namespace, fields
from . import ns

class UserDto:

    post_users = ns.model('post_users', {
        'name': fields.String(description = "User name", required = True),
        'lastname': fields.String(description = "User lastname", required = True),
        'email': fields.String(description = "User email", required = True),
        'password': fields.String(description = "User password", required = True),
        'active': fields.Boolean(description = "User status", required = True)
    })

    get_users = ns.model('get_users', {
        'id': fields.Integer(description = "User id"),
        'name': fields.String(description = "User name", required = True),
        'lastname': fields.String(description = "User lastname", required = True),
        'email': fields.String(description = "User email", required = True),
        'active': fields.Boolean(description = "User status")
    })

    put_users = ns.model('put_users', {
        'id': fields.Integer(description = "User id", required = True),
        'name': fields.String(description = "User name"),
        'lastname': fields.String(description = "User lastname"),
        'email': fields.String(description = "User email")
    })
