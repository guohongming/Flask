#!usr/bin/env python

from flask import jsonify, request
from lockerapp.users.model import Users
from flask_jwt import jwt_required, current_identity
from .. import common
import json
from ..controllers.captcha import PhoneCaptcha


def init_api(app):
    @app.route('/register', methods=['POST'])
    def register():
        """
        用户注册
        :return: json
        """
        # print("+++++++++++++++",PhoneCaptcha.phone_captcha_dict)
        data = request.get_data().decode("utf-8")
        data_json = json.loads(data)
        # print(data_json)
        phone = data_json["phone"]
        captcha4register = data_json["captcha"]
        password = data_json["password"]
        if PhoneCaptcha.phone_captcha_dict and phone in PhoneCaptcha.phone_captcha_dict:
            captcha, startTime = PhoneCaptcha.phone_captcha_dict[phone]
            # print(captcha, startTime)
            if captcha4register == str(captcha):
                user = Users(phone=phone, password=Users.set_password(Users, password))
                result = Users.add(Users, user)
                # print(result)
                if result:
                    return jsonify(common.falseReturn('', '该账号已经被注册'))
                if user.id:
                    returnUser = {
                        'id': user.id,
                        'phone': user.phone,
                        'login_time': user.login_time
                    }
                    return jsonify(common.trueReturn(returnUser, "用户注册成功"))
                else:
                    return jsonify(common.falseReturn('', '用户注册失败'))
            else:
                return jsonify(common.falseReturn('', '验证码错误'))
        else:
            return jsonify(common.falseReturn('', '你还没发验证码就注册了'))

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

    @app.route('/forgetPwd', methods=['POST'])
    def forgetPwd():
        """
        用户注册
        :return: json
        """
        # print("+++++++++++++++",PhoneCaptcha.phone_captcha_dict)
        data = request.get_data().decode("utf-8")
        data_json = json.loads(data)
        # print(data_json)
        phone = data_json["phone"]
        captcha4forgetPwd = data_json["captcha"]
        password = data_json["password"]
        if PhoneCaptcha.phone_captcha_dict and phone in PhoneCaptcha.phone_captcha_dict:
            captcha, startTime = PhoneCaptcha.phone_captcha_dict[phone]
            # print(captcha, startTime)
            if captcha4forgetPwd == str(captcha):
                userInfo = Users.query.filter_by(phone=phone).first()
                if (userInfo is None):
                    return jsonify(common.falseReturn('', '找不到用户'))
                else:
                    userInfo.password = Users.set_password(Users, password)
                    result = Users.update(Users)

                    if result:
                        return jsonify(common.falseReturn('', '用户重置密码失败'))
                    if userInfo.id:
                        returnUser = {
                            'id': userInfo.id,
                            'phone': userInfo.phone,
                            'login_time': userInfo.login_time
                        }
                        return jsonify(common.trueReturn(returnUser, "用户重置密码成功"))
                    else:
                        return jsonify(common.falseReturn('', '用户重置密码失败'))
            else:
                return jsonify(common.falseReturn('', '验证码错误'))
        else:
            return jsonify(common.falseReturn('', '你还没发验证码就想重置密码了'))

    @app.route('/changePwd', methods=['POST'])
    def changePwd():
        """
        用户注册
        :return: json
        """
        # print("+++++++++++++++",PhoneCaptcha.phone_captcha_dict)
        data = request.get_data().decode("utf-8")
        data_json = json.loads(data)
        # print(data_json)
        phone = data_json["phone"]
        old_password = data_json["old_password"]
        new_password = data_json["new_password"]
        print(phone, old_password, new_password)
        userInfo = Users.query.filter_by(phone=phone).first()
        if (userInfo is None):
            return jsonify(common.falseReturn('', '找不到用户'))
        else:
            if (Users.check_password(Users, userInfo.password, old_password)):
                userInfo.password = Users.set_password(Users, new_password)
                result = Users.update(Users)

                if result:
                    return jsonify(common.falseReturn('', '用户修改密码失败'))
                if userInfo.id:
                    returnUser = {
                        'id': userInfo.id,
                        'phone': userInfo.phone,
                        'login_time': userInfo.login_time
                    }
                    return jsonify(common.trueReturn(returnUser, "用户修改密码成功"))
                else:
                    return jsonify(common.falseReturn('', '用户修改密码失败'))
            else:
                return jsonify(common.falseReturn('', '旧密码错误'))