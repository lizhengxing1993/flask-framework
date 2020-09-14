import logging
from logging.handlers import TimedRotatingFileHandler
from flask import Flask
from apps.user import b_user
from apps.user.models import Role, User, MyAnonymousUser
from config import DevConfig, Config
from exts import cache, db, login_manager, session
from tools.patch import db_to_dict
from tools.timer import TimeManager


def init_db(app):
    # 生成数据库表
    db.create_all()
    app.logger.debug('创建表')
    if Role.query.first():
        return
    role_admin = Role(role_name="管理员", role_desc="系统管理员")
    role_audit = Role(role_name="审计员", role_desc="审计员")
    role_ordinary = Role(role_name="普通用户", role_desc="普通管理员")
    db.session.add_all([role_admin, role_audit, role_ordinary])
    db.session.commit()
    app.logger.debug('初始化角色成功')
    admin = User(
        user_name="admin",
        role_id=1,
        create_time=TimeManager.now(),
        status=1,
        last_passwd_change_time=TimeManager.now())
    admin.pwd = 'admin'
    db.session.add(admin)
    db.session.commit()
    app.logger.debug('初始化用户成功')


# 注册蓝图
def register_blueprint(app):
    app.register_blueprint(b_user, url_prefix='/user')


def create_app():

    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(DevConfig)

        # 初始化flask_session
        session.init_app(app)
        # 初始化cache
        cache.init_app(app)

        # 注册蓝图
        register_blueprint(app)

        # 初始化日志-按天分隔
        handler = TimedRotatingFileHandler(
            Config.LOG_PATH + '/flask.log', when="D", interval=1,
            backupCount=15,
            encoding="UTF-8", delay=False, utc=True)
        formatter = logging.Formatter(
            "[%(asctime)s][%(filename)s:%(lineno)d]"
            "[%(levelname)s][%(thread)d] - %(message)s")
        # 为日志记录器设置记录格式
        handler.setFormatter(formatter)
        # 为全局的日志工具对象（flaks app使用的）加载日志记录器
        # logging.getLogger().addHandler(handler)
        app.logger.addHandler(handler)

        # 初始化db
        db.app = app
        db.init_app(app)
        db.engine.pool._use_threadlocal = True
        db.Model.to_dict = db_to_dict()

        # 初始化数据库
        init_db(app)

        # 初始化flask-login
        login_manager.init_app(app)  # 初始化应用
        login_manager.login_view = 'login'  # 设置用户登录视图函数 endpoint
        if app.config["IS_MOCK_LOGIN"]:
            login_manager.anonymous_user = MyAnonymousUser

    return app
