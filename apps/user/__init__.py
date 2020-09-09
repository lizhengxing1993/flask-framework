from flask import Blueprint
b_user = Blueprint('b_user', __name__)
from apps.user.views import *


# 注册
b_user.add_url_rule('/user_manager/', view_func=UserView.as_view('user_manager'), methods=["GET", "POST"])
# 登陆
b_user.add_url_rule('/user_login/', view_func=UserLoginView.as_view('user_login'), methods=["GET", "POST", "DELETE"])
# 验证码
b_user.add_url_rule('/capcha/', view_func=CapchaMethodView.as_view('capcha'), methods=["GET"])
# 用户列表
b_user.add_url_rule('/user_list/', view_func=UserList.as_view('user_list'), methods=["GET"])
