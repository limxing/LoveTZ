from werkzeug.datastructures import CombinedMultiDict
from apps.main.models import User
from apps.core import db
from datetime import datetime
from apps.core import ma
import re
import copy
import json
import requests
from  marshmallow.schema import MarshalResult

appId = 2882303761517709315
appKey = "5301770927315"
appSecret = "7dFzuIqT0uyvtJKOm3OnXg=="
url = "https://mimc.chat.xiaomi.net/api/account/token"

appIdIOS = 2882303761517709315
appKeyIOS = "5301770927315"
appSecretIOS = "7dFzuIqT0uyvtJKOm3OnXg=="


class Result:
    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    def json(self):
        return {"code": self.code, "msg": self.msg, "data": self.data}


class Users(object):
    def login(self, dic: CombinedMultiDict, isIOS=False):
        phone = dic.get('phone')
        if phone is None:
            return json.dumps(Result(201, '请输入手机号码再请求', None).json())
        if re.compile('^1[3,4,5,7,8]\d{9}$').match(phone) is None:
            return json.dumps(Result(201, '请输入正确手机号码再请求', None).json())
        # with db.session.no_autoflush:
        user_db = db.session.query(User).filter_by(phone=phone).first()
        # db.session.rollback()
        if user_db is None:
            user_db = User()
            user_db.phone = phone
            user_db.time_creat = datetime.now()
            db.session.add(user_db)
            db.session.commit()

        mi = json.loads("{\"appId\":" + str(
            appId) + ",\"appKey\":\"" + appKey + "\",\"appSecret\":\"" + appSecret + "\",\"url\":\"" + url + "\"}")
        if isIOS:
            mi = json.loads("{\"appId\":" + str(
                appIdIOS) + ",\"appKey\":\"" + appKeyIOS + "\",\"appSecret\":\"" + appSecretIOS + "\",\"url\":\"" + url + "\"}")
        else:
            token = self.getMiToken(user_db.uuid)
            print('获取token',token)
            if token is None:
                return json.dumps(Result(201, '请重新登录', None))
            mi = json.loads("{\"token\":\"" + str(token) + "\",\"appId\":"+str(appId)+"}")
        user = copy.deepcopy(user_db)
        user.mitoken = mi
        base = json.dumps(Result(200, 'success', json.loads(UserSchema().dumps(user).data)).json())

        return base

    # 获取小米MIpush token
    def getMiToken(self, appAccount):
        req_json = "{\"appId\":" + str(
            appId) + ",\"appKey\":\"" + appKey + "\",\"appSecret\":\"" + appSecret + "\",\"appAccount\":\"" + appAccount + "\"}"
        headers = {'content-type': 'application/json'}
        req = requests.post(url, data=req_json, headers=headers)
        result = json.loads(req.content.decode('utf-8'))
        if result['message'] == 'success':
            token = result['data']
            return token
        else:
            return None


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
