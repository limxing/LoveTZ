from flask import Blueprint, render_template, session, request, jsonify


mod = Blueprint('youheng', __name__, url_prefix='/youheng', template_folder='templates')

@mod.route('/')
def index():
    return '欢迎访问有恒微信自动回复'

@mod.route('/login',methods=['POST','GET'])
def login():
    isIos = False
    try:
        isIos = request.headers['Apptype'] == 'IOS'
    except:
        pass

    return 'haha'


import xlrd
from apps.main.models import YouhengDuyao,Question
from apps.core import db


@mod.route('/wechat')
def wechat():
    return '<html><body><img src=\"./QR.png\"/></body></html>'

@mod.route('/leefeng_question')
def question():
    data = xlrd.open_workbook('./有恒社区文案库.xlsx')
    table = data.sheets()[2]
    for i in range(table.nrows):
        print(table.row_values(i))
        key = table.row_values(i)[0]
        print(key)
        if key.strip():
            q = Question()
            q.key = key
            q.result = table.row_values(i)[1]
            if len(table.row_values(i)) > 2:
                q.image = table.row_values(i)[2]
            db.session.add(q)
    db.session.commit()
    return 'finish'


@mod.route('/leefeng_duyao', methods=['POST', 'GET'])
def start():
    data = xlrd.open_workbook('./鸡汤文案收集.xlsx')
    tables = data.sheets()
    for t in range(len(tables)):
        table = tables[t]  # 打开第一张表
        nrows = table.nrows  # 获取表的行数
        for i in range(nrows):  # 循环逐行打印

            text = table.row_values(i)[0].replace('\n', '')
            if text.strip():
                if text.find('【') != -1:
                    youheng = YouhengDuyao()
                    youheng.text = text[text.find('【'):]
                    youheng.isSend = False
                    youheng.type = t
                    db.session.add(youheng)
                    print(t, i, text)
        db.session.commit()
    return '<html><body><img src=\"./QR.png\"/></body></html>'
        # if bot.is_listening:
        #     return '已经登录'
        # else:
        #
        #     # bot.start()
        #     return '准备登录'


