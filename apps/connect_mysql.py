import datetime
from apps.facotry import app
from .core import db

from apps.youheng.wechat import bot,qun
from apps.main.models import YouhengDuyao


def connect():
    with app.app_context():
        print(datetime.datetime.now(),'定时任务，链接一下数据库', db.session.execute('select * from alembic_version'))

def morning():
    with app.app_context():
        duYao = db.session.query(YouhengDuyao).filter_by(isSend=False).first()

        qun.send(duYao.text+ '\n各位早安/:sun')
        duYao.isSend = True
        db.session.commit()
    print("执行 早上任务")

def night():
    with app.app_context():
        duYao = db.session.query(YouhengDuyao).filter_by(isSend=False).first()

        qun.send(duYao.text + '\n各位晚安 /:moon')
        duYao.isSend = True
        db.session.commit()
    print("执行 晚上任务")