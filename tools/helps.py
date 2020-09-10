
import functools

from flask import request, jsonify


# 将model的结果转为字典格式 filters是要过滤掉不返回的字段
def model_to_dict(result, filters=None):
    from collections import Iterable
    # 转换完成后，删除  '_sa_instance_state' 特殊属性
    try:
        if isinstance(result, Iterable):
            tmp = [dict(zip(res.__dict__.keys(), res.__dict__.values())) for res in result if res]
            for t in tmp:
                t.pop('_sa_instance_state')
                if filters:
                    [t.pop(key) for key in filters]
        else:
            tmp = dict(zip(result.__dict__.keys(), result.__dict__.values()))
            tmp.pop('_sa_instance_state')
            if filters:
                for key in filters:
                    tmp.pop(key)
        return tmp
    except BaseException as e:
        print(e.args)
        raise TypeError('Type error of parameter')


# 装饰器检测必填参数 -- 还没写好
def require_args(*args_list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(request.args.keys())
            if request.method == "GET":
                form_data = request.args
            else:
                if request.json:
                    form_data = request.json
                else:
                    form_data = request.form
            print(form_data)
            for arg in args_list:
                print(arg)
                if arg not in form_data:
                    return jsonify(code=400, message='缺少%s参数' % arg)
            return func(*args, **kwargs)
        return wrapper
    return decorator
