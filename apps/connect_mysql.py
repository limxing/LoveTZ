import datetime
from apps.facotry import app
from .core import db
import time
import logging

from apps.main.models import YouhengDuyao
from apps.youheng.wechat import bot

def connect():
    with app.app_context():
        print(datetime.datetime.now(),'定时任务，链接一下数据库', db.session.execute('select * from alembic_version'))

def morning():
    with app.app_context():
        duYao = db.session.query(YouhengDuyao).filter_by(isSend=False, type=0).first()
        quns = bot.groups().search('有恒')
        for qun in quns:
            try:
                qun.send(duYao.text + '\n各位早安/:sun')
                time.sleep(1)
            except Exception as e:
                logging.log(logging.ERROR, e)
                pass
        duYao.isSend = True
        duYao.time_send = datetime.datetime.now()
        db.session.commit()
    print("执行 早上任务")

def night():
    with app.app_context():

        duYao = db.session.query(YouhengDuyao).filter_by(isSend=False,type=1).first()
        quns = bot.groups().search('有恒')
        for qun in quns:
            try:
                qun.send(duYao.text + '\n各位晚安 /:moon')
                time.sleep(1)
            except Exception as e:
                logging.log(logging.ERROR, e)
                pass
        duYao.isSend = True
        duYao.time_send = datetime.datetime.now()
        db.session.commit()
    print("执行 晚上任务")