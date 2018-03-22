from flask import Blueprint, render_template, session, request, jsonify
from apps.fund.Funds import Funds

mod = Blueprint('fund', __name__, url_prefix='/fund', template_folder='templates')


@mod.route('/')
def index():
    return '欢迎使用有恒科技数据处理中心'


@mod.route('/get', methods=['POST', 'GET'])
def get():

    return jsonify(Funds.getfund(request.values))


@mod.route('/save', methods=['POST', 'GET'])
def save():

    return jsonify(Funds.savefund(request.values))


