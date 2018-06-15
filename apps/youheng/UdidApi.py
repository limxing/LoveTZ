from sqlalchemy import desc
from flask import jsonify,g,request,make_response,redirect,render_template
import logging
from apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest,AuthRequest
from xml.dom import minidom as dom
from apps.main.models import YouhengUdid,YouhengUdidSchema


class UdidApi(AuthRequest):

    def get(self):
        return jsonify(
            Result(200, '', json.loads(YouhengUdidSchema().dumps(YouhengUdid.query.order_by(desc('time_creat')).all(), many=True).data)).__dict__)

    def delete(self):

        uuid = request.args.get('uuid')
        if not uuid:
            return jsonify(Result(401, '不存在此记录', '').__dict__)
        yh = YouhengUdid.query.get(uuid)
        yh.delete()
        return jsonify(Result(200, '', '').__dict__)
