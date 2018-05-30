from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_uploads import UploadSet
from flask_httpauth import HTTPTokenAuth
from flask import jsonify

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
photos = UploadSet('PHOTO')
auth = HTTPTokenAuth('token')
auth.error_handler(lambda: jsonify({
    "code": 40100,
    "data": None,
    "message": "认证失败"
}))



