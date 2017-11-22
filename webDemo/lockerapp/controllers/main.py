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
import datetime

main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder='./templates'
)


@main_blueprint.route('/getForgetLog', methods=['GET', 'POST'])
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



@main_blueprint.route('/getCommonLog', methods=['GET', 'POST'])
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
    b = request_a.stream
    a = str(request_a.stream)
    print(1)
    # try:
    #     request_a = request.data.decode("utf-8")
    # except:
    #     request_a = "err"

     # if request_a == "10H":
    #     pass
    # elif request_a=="11H":
    #     pass
    # elif request_a=="12H":
    #     pass
    # elif request_a=="13H":
    #     pass
    # elif request_a=="14H":
    #     pass
    # elif request_a=="15H":
    #     pass
    # elif request_a=="16H":
    #     pass


    push.audience_for_alias("smartLocker_75", "warn")
    return "1"

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

