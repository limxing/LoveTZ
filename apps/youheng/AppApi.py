
from flask import jsonify,g,request
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest


class AppApi(BaseRequest):

    def post(self):
        phone = request.values.get('phone')
        msg = request.values.get('msg')
        logging.log(logging.WARNING, phone+'==' + msg)

        return jsonify(Result(200, '', phone+'==' + msg).__dict__)
