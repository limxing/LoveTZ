from apps.main.models import YouhengDuyao, DuyaoSchema
from flask import jsonify, g, request
from apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest, AuthRequest
import datetime
from sqlalchemy import desc


class YouhengApi(AuthRequest):
    def get(self):
        isM = request.values.get('isM')
        duYao = YouhengDuyao.query.filter_by(type=isM).order_by(YouhengDuyao.isSend, desc(YouhengDuyao.time_send),
                                                                desc(YouhengDuyao.time_creat)).limit(30)

        return jsonify(Result(200, '', json.loads(DuyaoSchema().dumps(duYao, many=True).data)).__dict__)

    def post(self):
        text = request.values.get('text').strip()
        if not text:
            return jsonify(Result(201, "填写内容不能为空", None).__dict__)

        else:
            type = request.values['type']
            duyao = YouhengDuyao()
            duyao.text = text
            duyao.type = type
            duyao.time_creat = datetime.datetime.now()
            duyao.isSend = False
            duyao.add()
            return jsonify(Result(200, "保存成功", None).__dict__)

    def delete(self):
        YouhengDuyao.query.get(request.values.get('uuid')).delete()
        return jsonify(Result(200, "删除成功", None).__dict__)

    def put(self):

        duyao = YouhengDuyao.query.get(request.values.get('uuid'))
        duyao.text = request.values['text']
        duyao.save()

        return jsonify(Result(200, "修改成功", None).__dict__)
