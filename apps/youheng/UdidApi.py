
from flask import jsonify,g,request,make_response,redirect
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest


class UdidApi(BaseRequest):

    def post(self):
        print(request.data)
        # print(bytes.decode(request.data,encoding=''))

        return redirect('/static/udid.html',code=301)
