
from flask import jsonify,g,request,make_response,redirect
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest
from xml.dom import minidom as dom


class UdidApi(BaseRequest):

    def post(self):
        f = request.files['file']

        # f.save(os.path.join('app/static',filename))
        f.save('app/static/data.xml')
        # print(bytes.decode(request.data))

        # dom.parseString()
        return redirect('/static/udid.html',code=301)
