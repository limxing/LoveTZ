# -*- coding: utf-8 -*-

from .base import BaseConfig


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    ASSETS_DEBUG = True
    EXPLAIN_TEMPLATE_LOADING = False
