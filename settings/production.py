# -*- coding: utf-8 -*-

from .base import BaseConfig


class ProductionConfig(BaseConfig):
    print("ProductionConfig")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/maimai?charset=utf8&autocommit=true'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
    ASSETS_DEBUG = False
    JOBS = [
        {
            'id': 'sqlconnect_hasgone',
            'func': 'apps.connect_mysql:connect',
            'args': None,
            'trigger': 'interval',
            # 'seconds': 5
            'hours': 5
        },
        {
            'id': 'youheng_night',
            'func': 'apps.connect_mysql:night',
            'args': None,
            'trigger': 'cron',
            'hour': 21,
            'minute': 30,
            'second': 0
        },
        {
            'id': 'youheng_morning',
            'func': 'apps.connect_mysql:morning',
            'args': None,
            'trigger': 'cron',
            'hour': 8,
            'minute': 30,
            'second': 0
        }
    ]
