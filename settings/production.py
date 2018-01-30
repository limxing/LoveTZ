# -*- coding: utf-8 -*-

from .base import BaseConfig


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = False
    ASSETS_DEBUG = False
