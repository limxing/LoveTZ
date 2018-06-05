
from flask import jsonify,g,request
import json
from apps.base.BaseRequest import BaseRequest


class AppApi(BaseRequest):
    def post(self):
        phone = request.values.get('phone')
        msg = request.values.get('msg')
        print(phone,msg)
        pass
