
from flask import jsonify,g,request,make_response,redirect,render_template
import logging
from  apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest
from xml.dom import minidom as dom


class UdidApi(BaseRequest):

    def get(self):
        udid = request.args.get('udid')
        return '您的UDID:'+udid

    def post(self):

        # f.save(os.path.join('app/static',filename))
        dataStr = request.data.decode('iso-8859-1')
        udid = dataStr[dataStr.find('<string>')+8:dataStr.find('</string>')]

        print(udid)
        # bys = request.data
        # for b in bys:
        #     print(b)
        # print(request.headers)
        # dom.parseString()

        return redirect('/udid?udid='+udid,code=301)
