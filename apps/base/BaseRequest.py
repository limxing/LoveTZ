from flask import jsonify,g,request
from apps.core import auth
from flask_restful import Resource


class BaseRequest(Resource):

    def get_json(self):
        json = request.get_json()
        print('请求参数：', json)
        return json


class AuthRequest(BaseRequest):
    decorators = [auth.login_required]


