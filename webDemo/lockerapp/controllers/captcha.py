#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:wmc
@file: captcha.py 
@time: 2018/03/16

验证码的api
"""
import random

from lockerapp.util.rcscloudapi import RCSCLOUDAPI

__author__ = 'WMC'

import json

from flask import (Blueprint,
                   request,
                   jsonify)

from lockerapp import common


class PhoneCaptcha():
    phone_captcha_dict = {}


captcha_blueprint = Blueprint(
    'captcha',
    __name__,
    template_folder='./templates'
)


# 注册时发送短信验证码
@captcha_blueprint.route('/register', methods=['POST'])
def captcha4register():
    '''
    发送模板短信
    '''
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)

    phone = data_json["phone"]
    captcha = random.randint(1000, 9999)

    try:
        result = RCSCLOUDAPI.sendTplSms("76d68898d8624cbba44f8cc7626c830f", phone, "@1@=%s" % captcha)

        # print(result)
        # print("_______________-",PhoneCaptcha.phone_captcha_dict)
        # 记录发送短信的字典，手机号为key，验证码和时间戳为值
        import time
        startTime = int(time.time())
        PhoneCaptcha.phone_captcha_dict[phone] = (captcha, startTime)
        print("current list = %s" % PhoneCaptcha.phone_captcha_dict)

    except  Exception as ex:
        print("captcha for register Error = %s" % str(ex))
        return jsonify(common.falseReturn('', '发送短信失败'))
    else:
        return jsonify(common.trueReturn('', "发送短信成功"))


# 忘记密码时发送短信验证码
@captcha_blueprint.route('/forgetPwd', methods=['POST'])
def captcha4forgetPwd():
    '''
    发送模板短信
    '''
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)

    phone = data_json["phone"]
    captcha = random.randint(1000, 9999)

    try:
        result = RCSCLOUDAPI.sendTplSms("76d68898d8624cbba44f8cc7626c830f", phone, "@1@=%s" % captcha)

        # print(result)
        # print("_______________-",PhoneCaptcha.phone_captcha_dict)
        # 记录发送短信的字典，手机号为key，验证码和时间戳为值
        import time
        startTime = int(time.time())
        PhoneCaptcha.phone_captcha_dict[phone] = (captcha, startTime)
        print("current list = %s" % PhoneCaptcha.phone_captcha_dict)

    except  Exception as ex:
        print("captcha for register Error = %s" % str(ex))
        return jsonify(common.falseReturn('', '发送短信失败'))
    else:
        return jsonify(common.trueReturn('', "发送短信成功"))

