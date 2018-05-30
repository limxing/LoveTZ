from werkzeug.datastructures import CombinedMultiDict

from apps.main.Result import Result
from apps.main.models import User,UserSchema
from apps.core import db
from datetime import datetime
import re
import copy
import json
import requests


appId = 2882303761517709315
appKey = "5301770927315"
appSecret = "7dFzuIqT0uyvtJKOm3OnXg=="
url = "https://mimc.chat.xiaomi.net/api/account/token"

appIdIOS = 2882303761517709315
appKeyIOS = "5301770927315"
appSecretIOS = "7dFzuIqT0uyvtJKOm3OnXg=="





class Users(object):

    @staticmethod
    def login(dic: CombinedMultiDict, isIOS = False):
        phone = dic.get('phone')
        if phone is None:
            return json.dumps(Result(201, '请输入手机号码再请求', None).json())
        if re.compile('^1[3,4,5,7,8]\d{9}$').match(phone) is None:
            return json.dumps(Result(201, '请输入正确手机号码再请求', None).json())

        user_db = db.session.query(User).filter_by(phone=phone).first()

        if not user_db:
            user_db = User()
            user_db.phone = phone
            user_db.time_creat = datetime.now()
            try:
                db.session.add(user_db)
                db.session.commit()
            except:
                db.session.rollback()
                return json.dumps(Result(501, '登录失败，重新登录', None))
        token = 'token '+user_db.generate_auth_token().decode('ascii')

        mi = json.loads("{\"appId\":" + str(
            appId) + ",\"appKey\":\"" + appKey + "\",\"appSecret\":\"" + appSecret + "\",\"url\":\"" + url + "\"}")
        if isIOS:
            mi = json.loads("{\"appId\":" + str(
                appIdIOS) + ",\"appKey\":\"" + appKeyIOS + "\",\"appSecret\":\"" + appSecretIOS + "\",\"url\":\"" + url + "\"}")
        else:
            mitoken = Users.getMiToken(user_db.uuid)
            if mitoken is None:
                return json.dumps(Result(201, '请重新登录', None))
            mi = json.loads("{\"token\":\"" + str(mitoken) + "\",\"appId\":"+str(appId)+"}")
        user = copy.deepcopy(user_db)
        user.mitoken = mi
        user.token = token
        base = Result(200, 'success', json.loads(UserSchema().dumps(user).data)).__dict__

        return base

    # 获取小米MIpush token
    @staticmethod
    def getMiToken(appAccount):
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





