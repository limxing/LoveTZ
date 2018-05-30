from flask import Blueprint, render_template, session, request, jsonify


mod = Blueprint('main', __name__, url_prefix='/main', template_folder='templates')

@mod.route('/')
def index():
    return '欢迎访问有恒数据库MAIN'

