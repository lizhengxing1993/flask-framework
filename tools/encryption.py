from werkzeug.security import generate_password_hash, check_password_hash


class EncryManager(object):

    @classmethod
    def jiami(cls, password):
        return generate_password_hash(password)
    @classmethod
    def verify_password(cls,password_hash, password):
        """密码验证"""
        if password is None:
            return False
        return check_password_hash(password_hash, password)


if __name__ == "__main__":
    encry = EncryManager()

    pwd = encry.jiami('123')
    print(pwd)
    pwd_hash = encry.verify_password('123', encry)
    print(pwd_hash)
    pwd_hash = encry.verify_password('000', encry)
    print(pwd_hash)
    """不能用"""