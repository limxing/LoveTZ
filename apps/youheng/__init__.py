from flask_restful import Api
from .YouhengApi import YouhengApi
from .QuestionApi import QuestionApi
from .AskApi import AskApi
from .UdidApi import UdidApi
from .AppApi import AppApi
from apps.core import auth,db
from flask import g
from apps.main.models import User
api = Api()

api.add_resource(YouhengApi, '/duyao')
api.add_resource(QuestionApi, '/question')
api.add_resource(AppApi, '/app')
api.add_resource(UdidApi, '/udidm')
api.add_resource(AskApi, '/ask')


@auth.verify_token
def verify_token(token):
    user = User.verify_auth_token(token)
    if not user:
        return False
    else:
        g.user = user
        return True
