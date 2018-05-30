from flask_restful import Api
from .YouhengApi import YouhengApi
from apps.core import auth,db
from flask import g
from apps.main.models import User
api = Api()

api.add_resource(YouhengApi, '/duyao')


@auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)
    if not user:
        return False
    else:
        g.user = user
        return True
