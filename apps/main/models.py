from apps.core import db,ma
import uuid
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature


class User(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'user'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    phone = db.Column(db.String(16))
    time_creat = db.Column(db.DateTime)
    password = db.Column(db.String(64))
    token = db.Column(db.String(64))
    mitoken = db.Column(db.JSON)

    def generate_auth_token(self, expiration=60*60*24):
        s = Serializer('leefeng', expires_in=expiration)
        return s.dumps({'id': self.uuid})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer('leefeng')
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


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
    time_creat = db.Column(db.DateTime)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.commit()


class App(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'youheng_app'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    size = db.Column(db.String(32))
    version = db.Column(db.String(32))
    build = db.Column(db.Integer)
    url = db.Column(db.String(128))
    name = db.Column(db.String(16))
    describe = db.Column(db.String(128))

    time_creat = db.Column(db.DateTime)
    time_update = db.Column(db.DateTime)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()
    def save(self):
        db.session.commit()


class Question(db.Model):
    # def gen_id(self):
    #     return uuid.uuid4().hex

    __tablename__ = 'youheng_question'
    uuid = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    result = db.Column(db.Text)
    image = db.Column(db.String(128))
    time_creat = db.Column(db.DateTime)
    time_update = db.Column(db.DateTime)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):

        db.session.delete(self)
        db.session.commit()

    def save(self):
        db.session.commit()


class YouhengDuyao(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'youheng_duyao'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    text = db.Column(db.Text)
    isSend = db.Column(db.Boolean)
    type = db.Column(db.Integer)
    time_creat = db.Column(db.DateTime)
    time_send = db.Column(db.DateTime)
    # type = db.relationship('YouhengDuyaoType')
    # type = db.Column(db.Integer, db.ForeignKey('YouhengDuyaoType.uuid'))

    def add(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):

        db.session.delete(self)
        db.session.commit()
    def save(self):
        db.session.commit()

class YouhengUdid(db.Model):
    def gen_id(self):
        return uuid.uuid4().hex

    __tablename__ = 'youheng_udid'
    uuid = db.Column(db.String(32), default=gen_id, primary_key=True)
    udid = db.Column(db.String(64))
    id = db.Column(db.Integer)
    time_creat = db.Column(db.DateTime)
    def add(self):
        db.session.add(self)
        db.session.commit()
    def delete(self):

        db.session.delete(self)
        db.session.commit()
    def save(self):
        db.session.commit()


class DuyaoSchema(ma.ModelSchema):
    class Meta:
        model = YouhengDuyao


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User


class QuestionSchema(ma.ModelSchema):
    class Meta:
        model = Question


class YouhengUdidSchema(ma.ModelSchema):
    class Meta:
        model = YouhengUdid


class AskSchema(ma.ModelSchema):
    class Meta:
        model = Ask


class AppSchema(ma.ModelSchema):
    class Meta:
        model = App
