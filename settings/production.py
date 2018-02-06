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
