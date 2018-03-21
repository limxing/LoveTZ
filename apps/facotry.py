from flask import Flask
from flask_uploads import configure_uploads

from settings import load_config
from .core import db, migrate, ma, photos

from flask_wtf.csrf import CSRFProtect

def create_app():
    # app配置
    app = Flask(__name__, instance_relative_config=True)
    config = load_config()
    app.config.from_object(config)

    # 数据库
    db.init_app(app)
    app.app_context().push()
    # with app.app_context():
    #     db.create_all()

    migrate.init_app(app, db=db)
    from apps.main.view import mod as main_mod
    app.register_blueprint(main_mod)
    from apps.user.view import mod as user_mod
    app.register_blueprint(user_mod)
    from apps.fund.view import mod as fund_mod
    app.register_blueprint(fund_mod)

    #解析json
    ma.init_app(app)
    #上传图片配置
    configure_uploads(app, photos)
    # flask内置的保护机制,每次请求需要带上密钥，因此关闭它，
    # CSRFProtect(app)
    return app
