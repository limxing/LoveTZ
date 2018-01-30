# -*- coding: utf-8 -*-

import os

from flask import Config
from flask_uploads import IMAGES

class BaseConfig(Config):
    APP = "maimai"
    APP_NAME_CN = "maimai"
    SECRET_KEY = "65US7Cc8AF8dd4"
    BASEDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    DEBUG = False
    TESTING = False
    UPLOADED_PHOTO_DEST = os.path.join(BASEDIR,'upload')
    UPLOADED_PHOTO_ALLOW = IMAGES
    WTF_CSRF_ENABLED = False #全局禁用表单提交的防攻击验证

