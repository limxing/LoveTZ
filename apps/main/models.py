from apps.core import db,ma
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


# class YouhengDuyaoType(db.Model):
#
#     __tablename__ = 'youheng_duyao_type'
#     uuid = db.Column(primary_key=True)
#     name = db.Column(db.String(64))
class Ask(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'youheng_ask'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    key = db.Column(db.Text)
    result = db.Column(db.Text)
    image = db.Column(db.String(128))


class Question(db.Model):
    # def gen_id(self):
    #     return uuid.uuid4().hex

    __tablename__ = 'youheng_question'
    uuid = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    result = db.Column(db.Text)
    image = db.Column(db.String(128))


class YouhengDuyao(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'youheng_duyao'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    text = db.Column(db.Text)
    isSend = db.Column(db.Boolean)
    type = db.Column(db.Integer)
    # type = db.relationship('YouhengDuyaoType')
    # type = db.Column(db.Integer, db.ForeignKey('YouhengDuyaoType.uuid'))


class DuyaoSchema(ma.ModelSchema):
    class Meta:
        model = YouhengDuyao
