
from flask import jsonify,g,request
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest


class UdidApi(BaseRequest):

    def post(self):

        print(bytes.decode(request.data))

        return ''
