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
from jwt import *

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='./templates'
)


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """
    用户登录
    :return: json
    """
    username = request.form.get('username')
    password = request.form.get('password')
    if (not username or not password):
        return jsonify(common.falseReturn('', '用户名和密码不能为空'))
    else:
        return Auth.authenticate(Auth, username, password)


@main_blueprint.route('/user', methods=['GET', 'POST'])
def get():
        """
        获取用户信息
        :return: json
        """
        result = Auth.identify(Auth, request)
        if (result['status'] and result['data']):
            user = Users.get(Users, result['data'])
            returnUser = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'login_time': user.login_time
            }
            result = common.trueReturn(returnUser, "请求成功")
        return jsonify(result)


@main_blueprint.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('movie.index'))


@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """
    用户注册
    :return: json
    """
    # return "1"
    print("email")
    print(request.form)
    email = request.form.get('email')
    # return "1"
    print(email)
    username = request.form.get('username')
    password = request.form.get('password')
    user = Users(email=email, username=username, password=Users.set_password(Users, password))
    result = Users.add(Users, user)
    if user.id:
        returnUser = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'login_time': user.login_time
        }
        return jsonify(common.trueReturn(returnUser, "用户注册成功"))
    else:
        return jsonify(common.falseReturn('', '用户注册失败'))


@main_blueprint.route('/')
def home():

    return render_template('index.html')

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


@main_blueprint.route('/testLogin', methods=['GET', 'POST'])
def test_login():
    data = None
    if request.method == "POST":
        data = request.form

    return jsonify(result=1)