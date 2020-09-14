import logging
import os

import redis


class Config(object):

    # session-自带的session数据存放到cookie
    SECRET_KEY = "28f8a6b7-1ac7-4c2c-b22d-263295fbeabd"  # session秘钥配置
    # PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=31),session有效期时间的设置
    # SESSION_COOKIE_NAME = "session_",  # cookies中存储的session字符串的键
    # JSONIFY_MIMETYPE = "application/json",  # 设置jsonify响应时返回的contentype类型
    # PERMANENT = True  # 开启记住我，默认时间是一个月

    # flask_session组件配置，将数据存放到redis
    SESSION_TYPE = 'redis'  # session类型为redis
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    SESSION_REDIS = redis.Redis(
        host='127.0.0.1',
        port='6379',
        db=5)  # 用于连接redis的配置

    # cache配置
    CACHE_KEY_PREFIX = 'cache_'  # 设置cache_key的前缀
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = '127.0.0.1'
    CACHE_REDIS_PORT = 6379
    CACHE_REDIS_DB = 6
    # CACHE_REDIS_PASSWORD = ''
    # 也可以一键配置
    # CACHE_REDIS_URL = "redis://localhost:6379/6"  #连接到Redis服务器的URL。
    # 示例redis: // user: password @ localhost:6379 / 2
    # 下面五个参数是所有的类型共有的
    CACHE_NO_NULL_WARNING = "warning"  # null类型时的警告消息
    # CACHE_ARGS = []  # 在缓存类实例化过程中解包和传递的可选列表，用来配置相关后端的额外的参数
    # CACHE_OPTIONS = {}  # 可选字典,在缓存类实例化期间传递，也是用来配置相关后端的额外的键值对参数
    # CACHE_DEFAULT_TIMEOUT  # 默认过期/超时时间，单位为秒
    # CACHE_THRESHOLD  # 缓存的最大条目数

    # 文件路径
    PROJECT_APP_DIR = os.path.dirname(os.path.realpath(__file__))  # 获取当前文件地址
    PROJECT_DIR = os.path.realpath(
        os.path.join(
            PROJECT_APP_DIR,
            ".."))  # 当前目录的上一级目录
    LOG_PATH = os.path.join(PROJECT_APP_DIR, "logs")  # 拼接logs路径

    # sqlalchemy 配置
    SQLALCHEMY_ECHO = False  # 这个是记录打印SQL语句用于调试的, 一般设置为False, 不然会在控制台输出一大堆的东西
    # 自动提交省去了每次 commit，添加数据对象后立马取 id 返回None 立马要取 id 的地方要先commit一下
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_POOL_SIZE = 5  # 连接池的大小
    SQLALCHEMY_POOL_TIMEOUT = 15  # 连接超时时间
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 使用flask-login匿名用户
    IS_MOCK_LOGIN = True


class DevConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG
    # 设置teardown_reques钩子函要在调试环境执行
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    # 连接的数据库
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/sample"
    )


class PropConfig(Config):
    TESTING = True
    LOG_LEVEL = logging.WARNING
    # 连接的数据库
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/sample"
    )
