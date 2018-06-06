
from flask import jsonify,g,request,make_response,redirect
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest
from xml.dom import minidom as dom


class UdidApi(BaseRequest):

    def post(self):
        print(request.data.decode('ascii'))
        # print(bytes.decode(request.data))

        # dom.parseString()
        return redirect('/static/udid.html',code=301)
