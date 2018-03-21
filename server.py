from apps.facotry import create_app
from flask import request
from flask.wrappers import Response

app = create_app()
isAES = False

import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


@app.before_request
def before_request():
    # if request.method != 'POST' or 'me.leefeng.easymaimai' not in request.headers['User-Agent']:
    #     return '非法请求'
    # try:
    #     # request.headers['Apptype']
    #     print("接收请求：", request.headers['Apptype'])
    # except:
    #     return '非法请求'
    pass


@app.after_request
def after_request(response):
    if isAES:
        data = response.data
        base = bytes.decode(data)
        print('加密前：', base)
        base = base64.encodebytes(bytes(base, encoding="utf8"))
        base = bytes.decode(base)
        length = 16
        count = len(base)
        add = length - (count % length)
        base = base + ('\0' * add)
        data = b2a_hex(AES.new('leefengme1234567', AES.MODE_CBC, 'leefengme1234567').encrypt(base))
        response.data = data

        bys = a2b_hex(bytes.decode(data))
        s = AES.new('leefengme1234567', AES.MODE_CBC, 'leefengme1234567').decrypt(bys)
        s = base64.decodebytes(s)
        print('解密后：', bytes.decode(s))
    # data = response.data
    # base = bytes.decode(data)
    # print('加密前：', base)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=5001)
