
from flask import jsonify,g,request,make_response,redirect
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest
from xml.dom import minidom as dom


class UdidApi(BaseRequest):

    def post(self):

        # f.save(os.path.join('app/static',filename))
        # print(bytes.decode(request.data))
        bys = request.data
        for b in bys:
            print(b)
        # print(request.headers)
        # dom.parseString()
        return redirect('/static/udid.html',code=301)
