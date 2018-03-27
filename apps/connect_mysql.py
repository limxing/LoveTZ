import datetime
from apps.facotry import app
from .core import db

def connect():
    with app.app_context():
        print(datetime.datetime.now(),'定时任务，链接一下数据库',db.session.execute('select * from alembic_version'))
