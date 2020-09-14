from flask_caching import Cache
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session


cache = Cache()
db = SQLAlchemy()
login_manager = LoginManager()
session = Session()
