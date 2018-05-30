from flask import Blueprint, render_template, session, request, jsonify
from .Users import Users
from apps.core import auth
from flask import g

mod = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')


@mod.route('/')
def index():
    return '欢迎访问有恒数据库USER'


@mod.route('/login', methods=['POST', 'GET'])
def login():
    isIos = False
    try:
        isIos = request.headers['Apptype'] == 'IOS'
    except:
        pass
    return jsonify(Users.login(request.values, isIos))




