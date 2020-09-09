from flask_login import UserMixin, AnonymousUserMixin, login_user
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship, backref

from exts import db


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(32), nullable=False, comment="用户")
    real_name = Column(String(32), nullable=True, comment="真实姓名")
    password = Column(String(128), nullable=False)
    email = Column(String(255), nullable=True)
    telephone = Column(String(32), nullable=True)
    role_id = Column(Integer, ForeignKey("role.id"), comment="角色id")
    role = relationship("Role", backref=backref("user", uselist=False))
    job = Column(String(50), nullable=True)
    create_time = Column(BigInteger, nullable=False)
    last_login_ip = Column(String(32), nullable=True)
    last_login_time = Column(BigInteger, nullable=True)
    last_passwd_change_time = Column(BigInteger, nullable=True)
    is_delete = Column(Integer, nullable=False, server_default="0")
    status = Column(
        Integer,
        nullable=False,
        server_default="2",
        comment="审核状态, 0:表示未通过审核，1表示通过审核, 2未审核",
    )
    create_person = Column(Integer, server_default="0", comment="创建人，用来区分是否第一次登录强制更换密码 0:注册 1:管理员创建")

    @staticmethod
    def save():
        db.session.commit()


class MyAnonymousUser(AnonymousUserMixin):
    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        user = User.query.filter_by(id=1).first()
        login_user(user)
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return User.query.filter_by(user_id=0).first()


class Role(db.Model):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(50))
    role_desc = Column(String(256))
    is_delete = Column(Integer, nullable=False, server_default="0")
