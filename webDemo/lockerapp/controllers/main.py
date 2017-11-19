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

