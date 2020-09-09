from flask import current_app
from apps.user import b_user
import logging

from tools.errors import InvalidArgumentError


@b_user.route('/', methods=['GET'])
def user_():
    current_app.logger.debug('使用current_app写蓝图日志')
    # raise InvalidArgumentError({"field": "index", "message": "模拟抛出异常异常内容"})
    return '我是user蓝图'

# class UserView()