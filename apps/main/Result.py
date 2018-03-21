class Result:
    def __init__(self, code, msg, data):
        self.code = code
        self.msg = msg
        self.data = data

    def json(self):
        return {"code": self.code, "msg": self.msg, "data": self.data}