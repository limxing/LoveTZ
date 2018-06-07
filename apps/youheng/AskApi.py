from apps.main.models import Ask,AskSchema
from flask import jsonify,g,request
from apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest,AuthRequest
import datetime
from sqlalchemy import desc


class AskApi(AuthRequest):

    def get(self):

        asks = Ask.query.order_by('uuid').all()
        return jsonify(Result(200, '', json.loads(AskSchema().dumps(asks, many=True).data)).__dict__)



    def delete(self):
        Ask.query.get(request.values.get('uuid')).delete()
        return jsonify(Result(200, "删除成功", None).__dict__)

    def put(self):

        question = Ask.query.get(request.values.get('uuid'))
        question.result = request.values.get('result')
        question.question = request.values.get('question')
        question.image = request.values.get('image')
        question.save()

        return jsonify(Result(200, "修改成功", None).__dict__)
