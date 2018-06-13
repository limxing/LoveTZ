
from flask import jsonify,g,request
from sqlalchemy import desc
import logging
from  apps.main.Result import Result
from apps.main.models import App,AppSchema
import json,datetime
from apps.base.BaseRequest import BaseRequest,AuthRequest


class AppApi(AuthRequest):

    def get(self):
        return jsonify(Result(200, 'success', json.loads(AppSchema().dumps(App.query.order_by(desc('time_creat')).all(),many=True).data)).__dict__)

    def post(self):
        dictApp = request.get_json(cache=False)
        name = dictApp['name']
        if name:
            app = App()
            app.name = name
            app.size = dictApp['size']
            app.version = dictApp['version']
            app.url = dictApp['url']
            app.build = dictApp['build']
            app.describe = dictApp['describe']
            app.time_update = datetime.datetime.now()
            app.time_creat = datetime.datetime.now()
            app.add()
            return jsonify(Result(200, 'success', '').__dict__)
        return jsonify(Result(201, '失败', '').__dict__)

    def put(self):
        dictApp = request.get_json(cache=False)
        app = App.query.get(dictApp['uuid'])
        if app:
            app.name = dictApp['name']
            app.size = dictApp['size']
            app.version = dictApp['version']
            app.url = dictApp['url']
            app.build = dictApp['build']
            app.describe = dictApp['describe']
            app.time_update = datetime.datetime.now()
            app.save()
            return jsonify(Result(200, 'success', '').__dict__)
        return jsonify(Result(201, '失败', '').__dict__)

    def delete(self):
        App.query.get(request.values.get('uuid')).delete()
        return jsonify(Result(200, "删除成功", None).__dict__)
