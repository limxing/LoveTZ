from apps.core import db
import uuid




class User(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'user'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    phone = db.Column(db.String(16))
    time_creat = db.Column(db.DateTime)
    password = db.Column(db.String(64))
    mitoken = db.Column(db.JSON)

class Fund(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'fund'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    time_creat = db.Column(db.DateTime)
    time_update = db.Column(db.DateTime)
    fund_name = db.Column(db.String(64))
    fund_code = db.Column(db.String(64))
    mixamt = db.Column(db.Float)#最低申购
    maxamt = db.Column(db.String(64))#最高申购额
    feeratio = db.Column(db.Float)#总费率


class YouhengDuyao(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'youheng_duyao'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    text = db.Column(db.Text)
    isSend = db.Column(db.Boolean)
