from flask_login import login_manager

from apps.user.models import User
from flask import jsonify

from exts import db


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


class UserManager(object):

    def login(self, user_name, password):
        pass

    def register(self, user_name, real_name, password, email, telephone, role_id,job):
        user = User(user_name=user_name,
                    real_name=real_name,
                    password=password,
                    email=email,
                    telephone=telephone,
                    role_id=role_id,
                    job=job)
        db.session.add(user)
        user.save()