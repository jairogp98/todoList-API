from flask_restx import Namespace, fields
from . import ns

class AuthDto:

    post_auth = ns.model('post_auth', {
        'email': fields.String(description = "User email", required = True),
        'password': fields.String(description = "User password", required = True),
    })
