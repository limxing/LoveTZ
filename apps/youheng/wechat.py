import json

import requests

from wxpy import *
import time
from apps.facotry import app
from apps.core import db
from apps.main.models import Question,Ask
import jieba.analyse
from sqlalchemy import or_, and_
import logging

# bot = Bot(console_qr=True)
bot = Bot(cache_path=True, console_qr=True)


# my_friend = bot.friends().search('妖怪哪里跑')[0]

quns = bot.groups().search('有恒')
# qun = bot.groups().search('微信机器人')[0]
# quns = bot.groups().search('微信机器人')


def talks_robot(info='北京天气'):
    api_url = 'http://www.tuling123.com/openapi/api'
    apikey = '2e313f2e75fd48d7b3356f73e579fdc9'
    data = {'key': apikey,
            'info': info}
    req = requests.post(api_url, data=data).text
    replys = json.loads(req)['text']
    # time.sleep(1)
    return replys


@bot.register()
def print_others(msg):
    if msg.member is None:

        print('msg.member.isNone', msg.text, msg.type, msg.id, msg.sender)
    else:
        # print('print_others', msg.text, msg.type, msg.id, msg.__dict__)
        # logging.log(logging.INFO, msg.raw)
        text = msg.text
        ActualNickName = msg.raw.get('ActualNickName')
        # if '邀请' in text and '加入群聊' in text:
        #     print(text)
        #     print(text.split('"'))
        #     msg.reply('欢迎')

        # if '@有恒' in text:
        if msg.raw.get('isAt'):
            # if '办卡政策' in text:
            #     msg.reply_image('./bankazhengce.jpeg')
            # if '会员政策' in text:
            #     msg.reply_image('./huiyuanzhengce.jpeg')
            # if '佣金结算' in text or '案例' in text:
            #     msg.reply_image('./anli.jpeg')
            with app.app_context():
                text = text.replace('@有恒', '').strip()
                logging.log(logging.INFO, '收到消息：' + text)
                if text.isdigit():
                    question = Question.query.filter(Question.uuid == int(text)).first()
                    if question:
                        if question.result:
                            msg.reply('@' + ActualNickName + ' \n' + str(question.uuid)+'、'+question.question+'\n'+question.result.replace('\\n', '\n'))
                        if question.image:
                            msg.reply_image('./images/'+question.image)
                        return
                # question = Question.query.filter(Question.question.like('%'+text+'%')).first()
                words = jieba.analyse.extract_tags(text)
                logging.log(logging.INFO, '分词：' + str(words))
                or_clause = []
                for w in words:
                    if '什么' in w or '怎么' in w or '如何' in w :
                        continue
                    or_clause.append(Question.question.like('%' + w + '%'))

                or_filter = or_(*or_clause)
                questions = Question.query.filter(or_filter).order_by('uuid').all()

                if len(questions) == 1:
                    question = questions[0]
                    # print(question.question, question.result)
                    if question.result:
                        msg.reply('@' + ActualNickName + ' \n'+question.question+'\n'+question.result.replace('\\n', '\n'))
                    if question.image:
                        msg.reply_image('./images/'+question.image)
                    return
                if len(questions) > 1:
                    s = '@' + ActualNickName + ' \n'
                    for q in questions:
                        s += str(q.uuid) + '、'+q.question +'\n'
                    s += '请选择问题序号。例如：@有恒 ' + str(questions[0].uuid)
                    msg.reply(s)
                    return
                if '天气' in text:
                    msg.reply(talks_robot(text))
                else:
                    logging.log(logging.INFO, '保存未识别的问题：' + text)
                    # msg.reply('抱歉，我还没有搜索到相关问题的答案')
                    a = Ask()
                    a.key = text
                    db.session.add(a)
                    db.session.commit()


                # db.session.query(Question).filter(Question.key.like('%'+text+'%')).first()
            # print("收到消息" + text)
            # first = 0
            # at = text.index('@')
            # if at == 0:
            #     first = text.index(' ') + 1
            #     print("@位置" + first)
            #     text = text[first:]
            # else:
            #     text = text[:at]
            #
            # # message = '{}'.format(msg.ActualNickName, text[first:])
            # message = '{}'.format(text)
            # print("收到消息" + message)
            # msg.reply(talks_robot(message))


# @bot.register(my_friend)
# def reply_my_friend(msg):
#     return 'received: {} ({})'.format(msg.text, msg.type.__dict__)


bot.start()
# bot.join()
