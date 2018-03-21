from flask import Blueprint, render_template, session, request, jsonify
from .Users import Users

mod = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')

@mod.route('/')
def index():
    return '欢迎使用买卖不求人APP'

@mod.route('/login',methods=['POST','GET'])
def login():
    isIos = False
    try:
        isIos = request.headers['Apptype'] == 'IOS'
    except:
        pass

    return Users().login(request.values,isIos)


