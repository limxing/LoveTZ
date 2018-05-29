from flask import Blueprint, render_template, session, request, jsonify,template_rendered
import jieba.analyse
from sqlalchemy import or_, and_
import requests
from apps.main.models import DuyaoSchema
import json

from apps.main.Result import Result

mod = Blueprint('youheng', __name__, url_prefix='/youheng', template_folder='templates')

@mod.route('/')
def index():
    # duYao = db.session.query(YouhengDuyao).all()
    return render_template('index.html')


@mod.route('/add',methods=['POST'])
def add():

    text = request.values['text']
    type = request.values['type']
    print(text, type)
    duyao = YouhengDuyao()
    duyao.text = text
    duyao.type = type
    duyao.isSend = False
    db.session.add(duyao)
    db.session.commit()

    return jsonify(Result(200, '', '').__dict__)


@mod.route('/delete')
def delete():
    uuid = request.values['uuid']
    duyao = db.session.query(YouhengDuyao).filter(YouhengDuyao.uuid == uuid).first()
    if duyao:
        db.session.delete(duyao)
        db.session.commit()
    return jsonify(Result(200, '', '').__dict__)


@mod.route('/questions')
def questions():
    isM = request.values['isM']
    duYao = db.session.query(YouhengDuyao).filter(YouhengDuyao.type==isM).order_by('isSend').all()
    return jsonify(Result(200, '', json.loads(DuyaoSchema().dumps(duYao, many=True).data)).__dict__)


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


@mod.route('/shorturl')
def shortUrl():
    url = request.values['url']
    if url is None:
        return '您没有查询到任何关键字'
    else:
        url = 'http://api.t.sina.com.cn/short_url/shorten.json?source=3271760578&url_long='+url
        json = requests.get(url).json()
        if len(json) > 0:
            return jsonify(json[0])
        return '错误'


@mod.route('/search')
def search():
    key = request.values['key']
    if key is None:
        return '您没有查询任何关键字'
    else:
        words = jieba.analyse.extract_tags(key)
        or_clause = []
        for w in words:
            or_clause.append(Question.question.like('%' + w + '%'))

        or_filter = and_(*or_clause)

        question = Question.query.filter(or_filter).first()

        return question.result, words


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
            q.question = table.row_values(i)[0]
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


