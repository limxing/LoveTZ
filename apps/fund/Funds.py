from werkzeug.datastructures import CombinedMultiDict

from apps.main.Result import Result
from apps.main.models import Fund
import json
from apps.core import db
from datetime import datetime
from apps.core import ma


class Funds:

    @staticmethod
    def getfund(dic: CombinedMultiDict):
        code = dic.get('code')
        fund_db = db.session.query(Fund).filter_by(fund_code=code).first()
        if fund_db is None:
            return json.dumps(Result(401, '不存在:' + code + '的记录', None).json())
        else:
            return json.dumps(Result(200, 'success', json.loads(FundSchema().dumps(fund_db).data)).json())

    @staticmethod
    def savefund(dic: CombinedMultiDict):
        code = dic.get('fund_code')
        fund_db = db.session.query(Fund).filter_by(fund_code=code).first()
        if fund_db is None:
            fund_db = Fund()
            fund_db.time_creat = datetime.now()
            fund_db.time_update = datetime.now()
            fund_db.fund_code = code
            fund_db.fund_name = dic.get('fund_name')
            fund_db.mixamt = dic.get('mixamt')
            fund_db.maxamt = dic.get('maxamt')
            fund_db.feeratio = dic.get('feeratio')
            db.session.add(fund_db)
            db.session.commit()
            return json.dumps(Result(200, 'success', json.loads(FundSchema().dumps(fund_db).data)).json())
        else:
            return json.dumps(Result(201, '已经存在:'+code+'的记录', None).json())


class FundSchema(ma.ModelSchema):
    class Meta:
        model = Fund