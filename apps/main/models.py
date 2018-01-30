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
