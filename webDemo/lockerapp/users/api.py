from flask import jsonify, request
from lockerapp.users.model import Users
from flask_jwt import jwt_required, current_identity
from .. import common
import json


def init_api(app):
    @app.route('/register', methods=['POST'])
    def register():
        """
        用户注册
        :return: json
        """

        data = request.get_data().decode("utf-8")
        data_json = json.loads(data)

        phone = data_json["phone"]
        password = data_json["password"]

        user = Users(phone=phone, password=Users.set_password(Users, password))
        result = Users.add(Users, user)
        if user.id:
            returnUser = {
                'id': user.id,
                'phone': user.phone,
                'login_time': user.login_time
            }
            return jsonify(common.trueReturn(returnUser, "用户注册成功"))
        else:
            return jsonify(common.falseReturn('', '用户注册失败'))


    # 用户登录接口已由flask-jwt默认定义好，默认路由是"/auth"，可以在配置文件中配置:
    # JWT_AUTH_URL_RULE = '/login'
    # 修改登录接口路由为'/login'
    # 需要注意的是，登录接口的传值要使用 application/json 形式


    @app.route('/user')
    @jwt_required()
    def get():
        """
        获取用户信息
        :return: json
        """
        user = Users.get(Users, current_identity.id)
        returnUser = {
            'id': user.id,
            'phone': user.phone,
            'login_time': user.login_time
        }
        return jsonify(common.trueReturn(returnUser, "请求成功"))