
from flask import jsonify,g,request,make_response,redirect
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest
from xml.dom import minidom as dom


class UdidApi(BaseRequest):

    def post(self):

        # f.save(os.path.join('app/static',filename))
        dataStr = request.data.decode('iso-8859-1')
        print(dataStr[dataStr.find('<dict>'):dataStr.find('</dict>')])


        # bys = request.data
        # for b in bys:
        #     print(b)
        # print(request.headers)
        # dom.parseString()
        return redirect('/static/udid.html',code=301)
