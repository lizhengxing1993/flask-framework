
from flask import current_app, views, request, session, make_response
from flask_login import current_user

from apps.user import b_user
from apps.user.main import UserManager, gen_capcha


@b_user.route('/', methods=['GET'])
def user_():
    current_app.logger.debug('使用current_app写蓝图日志')
    # raise InvalidArgumentError({"field": "index", "message": "模拟抛出异常异常内容"})
    return '我是user蓝图'


class UserView(views.MethodView):

    def get(self):
        res = UserManager.get_user()
        return res

    def post(self):
        user_name = request.form.get('user_name')
        real_name = request.form.get('real_name')
        password = request.form.get('password')
        email = request.form.get('email')
        telephone = request.form.get('telephone')
        role_id = int(request.form.get('role_id'))
        job = request.form.get('job')
        res = UserManager.register(user_name, real_name, password,
                                   email, telephone, role_id, job)
        return res


class UserList(views.MethodView):
    def get(self):
        limit = int(request.form.get('limit', 10))
        offset = int(request.form.get('offset', 0))
        res = UserManager.get_user_list(limit, offset)
        return res


class UserLoginView(views.MethodView):

    def post(self):
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        capcha = request.form.get('capcha')
        res = UserManager.login(user_name, password, capcha)
        return res

    def delete(self):
        res = UserManager.logout()
        return res


class CapchaMethodView(views.MethodView):
    def get(self):
        print(current_user.is_anonymous)
        capcha, capcha_buf = gen_capcha()
        session["capcha"] = capcha.lower()
        session.modified = True
        response = make_response(capcha_buf)
        response.headers["Content-Type"] = "image/gif"
        return response
