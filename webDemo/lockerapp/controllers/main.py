__author__ = 'Guo'

from flask import (render_template,
                   current_app,
                   Blueprint,
                   redirect,
                   url_for,
                   request,
                   flash,
                    jsonify,
                   session)

from lockerapp.models.forms import LoginForm, RegisterForm
from lockerapp.models.models import User, db_user
from flask_login import login_user, logout_user, current_user, login_required
from lockerapp.users.model import Users
from lockerapp import common
from lockerapp.auth.auths import Auth
from flask_jwt import jwt_required, current_identity

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='./templates'
)




@main_blueprint.route('/getCommonLog', methods=['GET', 'POST'])
@jwt_required()
def get_common_log():
    user = Users.get(Users, current_identity.id)
    user_id = user.id

    return ""







@main_blueprint.route('/')
def home():
    return 'hello world'


@main_blueprint.route('/test', methods=['GET', 'POST'])
def test():
    data = None

    if request.method == "POST":
        data = request.form

    if request.method == "GET":
        data = request.args

    if data==None:
        data = {}
    else:
        data = data.to_dict()

    rep = 'i have got the request data:'+str(data)+',thank u !!!'
    return rep

