import datetime
from apps.facotry import app
from .core import db

def connect():
    with app.app_context():
        db.session.rollback()
        print(datetime.datetime.now(),'定时任务，回滚链接一下数据库')
