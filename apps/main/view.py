from flask import Blueprint, render_template, session, request, jsonify


mod = Blueprint('main', __name__, url_prefix='', template_folder='templates')

@mod.route('/')
def index():
    return '欢迎使用买卖不求人APP'

