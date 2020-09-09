from flask import jsonify, session
import os
from io import BytesIO
from random import randrange, sample, choice

from PIL import ImageFont, Image, ImageDraw
from flask_login import login_user, logout_user, current_user

from apps.user.models import User
from exts import db, login_manager
from tools.helps import model_to_dict
from tools.timer import TimeManager


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class UserManager(object):

    @classmethod
    def verify_existence(self, user_name):
        user = User.query.filter_by(user_name=user_name, is_delete=0).first()
        return True if user else False

    @classmethod
    def register(cls, user_name, real_name, password, email, telephone, role_id, job):
        if UserManager.verify_existence(user_name):
            return jsonify({"code": 400, "message": "用户已存在，请更换用户名"})
        user = User()
        user.user_name = user_name
        user.real_name = real_name
        user.email = email
        user.telephone = telephone
        user.role_id = role_id
        user.job = job
        user.create_time = TimeManager.now()
        user.pwd = password
        db.session.add(user)
        user.save()
        return jsonify({"code": 200, "message": "注册成功"})

    @classmethod
    def login(cls, user_name, password, capcha):
        if not UserManager.check_capcha(capcha):
            return jsonify({"code": 500, "message": "验证码错误错误"})
        user = User.query.filter_by(user_name=user_name, is_delete=0).first()
        if not user:
            return jsonify({"code": 500, "message": "账号错误"})
        if not user.check_password(password):
            return jsonify({"code": 500, "message": "密码错误"})
        login_user(user)
        return jsonify({"code": 200, "message": "登陆成功"})

    @classmethod
    def logout(cls):
        logout_user()
        return jsonify({"code": 200, "message": "退出登陆成功"})

    @classmethod
    def get_user(cls):
        user = User.query.filter_by(id=current_user.id).first()
        data = model_to_dict(user, ['password'])
        return jsonify({"code": 200, "message": "成功", "data": data})

    @classmethod
    def get_user_list(cls, limit, offset):
        query = User.query.filter_by(is_delete=0).order_by(User.id.asc())
        total = query.count()
        users = query.limit(limit).offset(offset).all()
        filters = ['password', 'create_person']
        data = model_to_dict(users, filters)
        return jsonify({"code": 200, "message": "成功", "total": total, "data": data})

    # 验证码验证
    @classmethod
    def check_capcha(cls, code):
        session_code = session.pop("capcha", None)
        if not session_code or session_code != code.lower():
            return False
        return True


def gen_capcha():
    """生成验证码"""
    img_width = 58
    img_height = 30
    font_size = 16
    font_color = ["black", "darkblue", "darkred"]
    codes = "123456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"
    background = (randrange(230, 255), randrange(230, 255), randrange(230, 255))
    line_color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    sample_file = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "lib/LucidaSansDemiOblique.ttf"
    )
    font = ImageFont.truetype(sample_file, font_size)
    img = Image.new("RGB", (img_width, img_height), background)
    code = "".join(sample(codes, 4))
    draw = ImageDraw.Draw(img)
    for _i in range(randrange(3, 5)):
        xy = (
            randrange(0, img_width),
            randrange(0, img_height),
            randrange(0, img_width),
            randrange(0, img_height),
        )
        draw.line(xy, fill=line_color, width=1)
    x = 2
    for i in code:
        y = randrange(0, 10)
        draw.text((x, y), i, font=font, fill=choice(font_color))
        x += 14
    buf = BytesIO()
    img.save(buf, "gif")
    buf.seek(0)
    return code.lower(), buf.getvalue()
