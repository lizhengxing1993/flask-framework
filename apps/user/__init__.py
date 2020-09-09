from flask import Blueprint
b_user = Blueprint('b_user', __name__)
from apps.user.views import *