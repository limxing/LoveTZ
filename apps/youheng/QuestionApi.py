from apps.main.models import Question, QuestionSchema
from flask import jsonify,g,request
from apps.main.Result import Result
import json
from apps.base.BaseRequest import BaseRequest,AuthRequest
import datetime
from sqlalchemy import desc


class QuestionApi(AuthRequest):

    def get(self):

        duYao = Question.query.order_by('uuid').all()

        return jsonify(Result(200, '', json.loads(QuestionSchema().dumps(duYao, many=True).data)).__dict__)

    def post(self):
        result = request.values['result'].strip()
        if not result:
            return jsonify(Result(201, "填写内容不能为空", None).__dict__)

        else:
            title = request.values['question']
            image = request.values['image']

            question = Question()
            question.result = result
            question.question = title
            question.image = image
            question.time_creat = datetime.datetime.now()
            question.time_update = datetime.datetime.now()

            question.add()
            return jsonify(Result(200, "保存成功", None).__dict__)

    def delete(self):
        Question.query.get(request.values['uuid']).delete()
        return jsonify(Result(200, "删除成功", None).__dict__)

    def put(self):

        question = Question.query.get(request.values['uuid'])
        question.result = request.values['result']
        question.question = request.values['question']
        question.image = request.values['image']
        question.time_update = datetime.datetime.now()
        question.save()

        return jsonify(Result(200, "修改成功", None).__dict__)

    def checkLogin(self):
        return False
