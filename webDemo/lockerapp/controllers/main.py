# coding:utf-8

from flask import (render_template,
                   current_app,
                   Blueprint,
                   redirect,
                   url_for,
                   request,
                   flash,
                    jsonify,
                   session)



from lockerapp.users.model import Users
from lockerapp import common
from lockerapp.auth.auths import Auth
from flask_jwt import jwt_required, current_identity
from lockerapp.util import push
from lockerapp.models.locker_common_log import LockerCommonLog
from lockerapp.models.locker_warning_log import LockerWarningLog
from lockerapp.models.locker_forget_log import LockerForgetLog
from lockerapp.models.locker import Locker
from lockerapp.models.bind_mapping import BindMapping
from lockerapp.util.time_format_util import time_to_chinese
import datetime
import json

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='./templates'
)


@main_blueprint.route('/forgetKey', methods=['GET', 'POST'])
@jwt_required()
def get_forget_log():
    user = Users.get(Users, current_identity.id)
    user_id = user.id
    bind_mapping = BindMapping.query.filter(BindMapping.user_id == user_id,BindMapping.del_flag == 0).first()
    if bind_mapping:
        locker_id = bind_mapping.locker_id
        flogs = LockerForgetLog.query.filter(LockerForgetLog.del_flag==0,LockerForgetLog.locker_id == locker_id).all()
        result = []
        for i in flogs:
            d = {}
            d['id'] = i.id
            d['locker_id'] = i.locker_id
            d['forget_log'] = i.forget_log
            d['create_time'] = time_to_chinese(i.create_time)
            result.append(d)
        return jsonify(common.trueReturn(result,msg="获取记遗忘钥匙记录成功"))
    else:
        return jsonify(common.falseReturn(None, msg="未获取到绑定的数据"))


@main_blueprint.route('/inOutDoor', methods=['GET', 'POST'])
@jwt_required()
def get_common_log():
    user = Users.get(Users, current_identity.id)
    user_id = user.id
    bind_mapping = BindMapping.query.filter(BindMapping.user_id == user_id,BindMapping.del_flag == 0).first()
    if bind_mapping:
        locker_id = bind_mapping.locker_id
        clogs = LockerCommonLog.query.filter(LockerCommonLog.del_flag==0,LockerCommonLog.locker_id==locker_id).all()
        result = []
        for i in clogs:
            d = {}
            d['id'] = i.id
            d['locker_id'] = i.locker_id
            d['common_log'] = i.common_log
            d['create_time'] = time_to_chinese(i.create_time)
            result.append(d)
        return jsonify(common.trueReturn(result,msg="获取出入门记录成功"))
    else:
        return jsonify(common.falseReturn(None, msg="未获取到绑定的数据"))

@main_blueprint.route('/getWarningLog', methods=['GET', 'POST'])
@jwt_required()
def get_warning_log():
    user = Users.get(Users, current_identity.id)
    user_id = user.id
    bind_mapping = BindMapping.query.filter(BindMapping.user_id == user_id,BindMapping.del_flag == 0).first()
    if bind_mapping:
        locker_id = bind_mapping.locker_id
        wlogs = LockerWarningLog.query.filter(LockerWarningLog.del_flag==0,LockerWarningLog.locker_id==locker_id).all()
        result = []
        for i in wlogs:
            d = {}
            d['id'] = i.id
            d['locker_id'] = i.locker_id
            d['warning_log'] = i.warning_log
            d['create_time'] = time_to_chinese(i.create_time)
            result.append(d)

        return jsonify(common.trueReturn(result,msg="获取告警记录成功"))
    else:
        return jsonify(common.falseReturn(None, msg="未获取到绑定的数据"))


@main_blueprint.route('/pushMsgAll', methods=['GET', 'POST'])
def push_msg_all():
    msg = '第一个msg ，测试..'
    # push.all(msg)
    # push.notification()
    push.audience_for_alias("smartLocker_74","warn")
    return jsonify(common.trueReturn(data={}, msg='发送成功'))



@main_blueprint.route('/')
def home():
    return 'hello world'


@main_blueprint.route('/sendLockerMsg', methods=['GET', 'POST'])
def send_locker_msg():

    request_a = request
    locker_id = dict(request_a.headers)["Lockerid"]  # 获取请求头中的lockerid
    data = request.get_data().decode("utf-8")
    locker = Locker.query.filter(Locker.del_flag == 0,Locker.mac==locker_id).first()  #根据locker_id  查库
    id = locker.id
    mapping = BindMapping.query.filter(BindMapping.locker_id == id,BindMapping.del_flag == 0).first()
    user_id = mapping.user_id
    tag = "smartLocker_"+str(user_id)
    if len(data) != 5:
        return "false"

    # 功能设置按钮触
    if data == "AZZZZ":
        locker = Locker.query.filter(Locker.del_flag == 0,Locker.mac==locker_id).first()  #根据locker_id  查库
        return "S"+locker.feature_id+locker.chu_ru+locker.tips+"Z"  #拼装出参

    # 盗贼假钥匙开锁
    if data == "ABZZZ":
        log = LockerWarningLog()
        log.locker_id = locker_id
        log.del_flag = 0
        log.locker_id = id
        log.warning_log = 1
        log.create_time = datetime.datetime.now()
        log.save()
        try:
            push.audience_for_alias(tag,"warn_1_1")
        except Exception as e:
            pass
        return "abzzz"

    # 盗贼拆锁芯
    if data == "ACZZZ":
        log = LockerWarningLog()
        log.locker_id = locker_id
        log.del_flag = 0
        log.locker_id = id
        log.warning_log = 2
        log.create_time = datetime.datetime.now()
        log.save()
        try:
            push.audience_for_alias(tag,"warn_1_2")
        except Exception as e:
            pass
        return "aczzz"

    # 盗贼撬门
    if data == "ADZZZ":
        log = LockerWarningLog()
        log.locker_id = locker_id
        log.del_flag = 0
        log.locker_id = id
        log.warning_log = 3
        log.create_time = datetime.datetime.now()
        log.save()
        try:
            push.audience_for_alias(tag,"warn_1_3")
        except Exception as e:
            pass
        return "adzzz"

    # 盗贼锡纸开锁
    if data == "AEZZZ":
        log = LockerWarningLog()
        log.locker_id = locker_id
        log.del_flag = 0
        log.locker_id = id
        log.warning_log = 4
        log.create_time = datetime.datetime.now()
        log.save()
        try:
            push.audience_for_alias(tag,"warn_4")
        except Exception as e:
            pass
        return "aezzz"

    # 有人出门
    if data == "AFZZZ":
        log = LockerCommonLog()
        log.locker_id = locker_id
        log.del_flag = 0
        log.locker_id = id
        log.common_log = 2
        log.create_time = datetime.datetime.now()
        log.save()
        try:
            push.audience_for_alias(tag,"prompt_2")
        except Exception as e:
            pass
        return "afzzz"

    # 有人入门
    if data == "AGZZZ":
        log = LockerCommonLog()
        log.locker_id = locker_id
        log.del_flag = 0
        log.locker_id = id
        log.common_log = 1
        log.create_time = datetime.datetime.now()
        log.save()
        try:
            push.audience_for_alias(tag,"prompt_1")
        except Exception as e:
            pass
        return "agzzz"

    return "false"

# 绑定锁 输入序列号 和 密码
@main_blueprint.route('/deviceBinding', methods=['GET', 'POST'])
@jwt_required()
def device_binding():
    user = Users.get(Users, current_identity.id)
    user_id = user.id
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)
    request_id = data_json['id']
    request_pwd = data_json['pwd']
    locker = Locker.query.filter(Locker.del_flag == 0,Locker.mac==request_id).first()
    if not locker:
        return jsonify(common.falseReturn(msg='输入的序列号或密码错误'))

    if locker.lock_password == request_pwd:
        mapping = BindMapping()
        mapping.locker_id = locker.id
        mapping.del_flag = 0
        mapping.user_id = user_id
        mapping.save()
        return jsonify(common.trueReturn(msg='绑定成功'))
    else:
        return jsonify(common.falseReturn(msg='输入的序列号或密码错误'))


@main_blueprint.route('/test', methods=['GET', 'POST'])
def test():
    data = None
    request_b = request
    print(str(request_b))
    request_a = request.data.decode("utf-8")
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

