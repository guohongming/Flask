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



from lockerapp.users.model import Users
from lockerapp import common
from lockerapp.auth.auths import Auth
from flask_jwt import jwt_required, current_identity
from lockerapp.util import push
from lockerapp.models.locker_common_log import LockerCommonLog
from lockerapp.models.locker_warning_log import LockerWarningLog
from lockerapp.models.locker_forget_log import LockerForgetLog
from lockerapp.models.locker import Locker
import datetime

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='./templates'
)


@main_blueprint.route('/forgetKey', methods=['GET', 'POST'])
# @jwt_required()
def get_forget_log():
    # user = Users.get(Users, current_identity.id)
    # user_id = user.id
    flogs = LockerForgetLog.query.filter(LockerForgetLog.del_flag==0,LockerForgetLog.locker_id==1).all()
    result = []
    for i in flogs:
        d = {}
        d['id'] = i.id
        d['locker_id'] = i.locker_id
        d['forget_log'] = i.forget_log
        d['create_time'] = i.create_time
        result.append(d)

    return jsonify(common.trueReturn(result,msg="获取记遗忘钥匙记录成功"))



@main_blueprint.route('/inOutDoor', methods=['GET', 'POST'])
# @jwt_required()
def get_common_log():
    # user = Users.get(Users, current_identity.id)
    # user_id = user.id
    clogs = LockerCommonLog.query.filter(LockerCommonLog.del_flag==0,LockerCommonLog.locker_id==1).all()
    result = []
    for i in clogs:
        d = {}
        d['id'] = i.id
        d['locker_id'] = i.locker_id
        d['common_log'] = i.common_log
        d['create_time'] = i.create_time
        result.append(d)

    return jsonify(common.trueReturn(result,msg="获取出入门记录成功"))


@main_blueprint.route('/getWarningLog', methods=['GET', 'POST'])
# @jwt_required()
def get_warning_log():
    # user = Users.get(Users, current_identity.id)
    # user_id = user.id
    wlogs = LockerWarningLog.query.filter(LockerWarningLog.del_flag==0,LockerWarningLog.locker_id==1).all()
    result = []
    for i in wlogs:
        d = {}
        d['id'] = i.id
        d['locker_id'] = i.locker_id
        d['warning_log'] = i.warning_log
        d['create_time'] = i.create_time
        result.append(d)

    return jsonify(common.trueReturn(result,msg="获取告警记录成功"))

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
    locker_id = dict(request_a.headers)["Locker-Id"]  # 获取请求头中的lockerid
    data = request.get_data().decode("utf-8")
    if len(data) != 5:
        return "false"

    # 功能设置按钮触
    if data == "AZZZZ":
        locker = Locker.query.filter(Locker.del_flag == 0,Locker.mac==locker_id).all()[0]  #根据locker_id  查库
        return "S"+locker.feature_id+locker.chu_ru+locker.tips+"Z"  #拼装出参

    # 盗贼假钥匙开锁
    if data == "ABZZZ":
        return "abzzz"

    # 盗贼拆锁芯
    if data == "ACZZZ":
        return "aczzz"

    # 盗贼撬门
    if data == "ADZZZ":
        return "adzzz"

    # 盗贼锡纸开锁
    if data == "AEZZZ":
        return "aezzz"

    # 有人出门
    if data == "AFZZZ":
        return "afzzz"

    # 有人入门
    if data == "AGZZZ":
        return "agzzz"

    return "false"

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

