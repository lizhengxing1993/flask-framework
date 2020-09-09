import json
import os

from flask import session, request, current_app

from apps import create_app
from exts import cache

app = create_app()

@app.route('/')
def hello_world():


    return 'Hello World!'


@app.route('/session', methods=['GET'])
def session_():
    """
    session操作
    :return:
    """
    # 增
    session['username'] = 'hubu'
    # 查
    print(session.get('username'))
    # 删
    # session.pop('username')
    print(session.get('username'))
    return 'session'


@app.route('/cache', methods=['GET'])
@cache.cached(timeout=30)  # 以装饰器方式缓存函数的返回值
def cache_():
    """
    cache缓存函数
    :return:
    """
    print('我是缓存')
    return '我被缓存了'


@app.route('/kwcache', methods=['GET'])
def del_cache_():
    """
    cache缓存值
    :return:
    """
    cache.set('name', 'xiaoming', timeout=30)
    cache.set('person', {'name': 'aaa', 'age': 20})
    x = cache.get('name')
    print(x)
    cache.set_many([('name1', 'hhh'), ('name2', 'jjj')])
    print(cache.get_many("name1", "name2"))
    print(cache.delete("name"))
    print(cache.delete_many("name1", "name2"))
    print(cache.get('person'))
    return 'ok'


@app.route('/log', methods=['GET'])
def log():
    app.logger.debug('This is debug message')
    app.logger.info('This is info message')
    app.logger.warning('This is warning message')
    return 'log'


def log_format(level, url, status_code, message):  # status_code为状态码，请求日志中为None
    process = os.getpid()
    method = request.method
    # 定义日志的格式 采用f‘’的方式格式化字符串
    strMessage = f'{process} {url} {method} {status_code} {message}'
    if level == "I":
        current_app.logger.info(strMessage)
    if level == "E":
        current_app.logger.error(strMessage)
    if level == "R":
        current_app.logger.info(strMessage)


@app.after_request
def after_app_request(response):
    print(response)
    api_name = request.url
    response_data = response.json
    if str(response.status_code).startswith('4') or str(response.status_code).startswith('5'):
         log_format('E', api_name, response.status_code, str(response_data))
    else:
         log_format('I', api_name, response.status_code,  str(response_data) or None)
    return response

@app.teardown_request
# def handle_teardown_request(response):
#     '''在每次请求之后被执行，不管视图函数是否执行正常都被执行，前提是在生产环境会显示，调试环境否则不会显示'''
#     print('teardown_reques被执行')
#     if isinstance(response, Exception):
#         print(response.errors)
#         # return make_response(jsonify(response.errors))
#         response.__setattr__()
#         return make_response(jsonify({"code":200}))
#     return response


@app.errorhandler(404)
def error_404(e):
    app.logger.debug(e)
    return '页面不存在'

@app.errorhandler(500)
def error_500(e):
    return '服务器出现了问题'


@app.before_request
def before_app_request():
    api_name = request.url
    try:
       #收到的前端数据
        request_data = json.loads(request.get_data())
    except Exception as e:
        request_data = request.form.to_dict()
    log_format('R', api_name, None, str(request_data))


if __name__ == '__main__':
    app.run()
