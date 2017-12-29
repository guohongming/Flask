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
import json

device_blueprint = Blueprint(
    'device',
    __name__,
    template_folder='./templates'
)

# 现有锁具特征确认
@device_blueprint.route('/lockerFeatureConfirm', methods=['GET', 'POST'])
# @jwt_required()
def locker_feature_confirm():
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)
    feature_id = data_json["feature_id"]

    return common.trueReturn(msg="1")

# 出入门显示功能选择
@device_blueprint.route('/inOutDoorDisplay', methods=['GET', 'POST'])
# @jwt_required()
def in_out_door_display():
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)
    display = data_json['display']

    return common.trueReturn(msg="1")


# 附加提示音设置
@device_blueprint.route('/additionalBeepSettings', methods=['GET', 'POST'])
# @jwt_required()
def additional_beep_settings():
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)
    setting_id = data_json['setting_id']

    return common.trueReturn(msg="1")

# 让服务器启动网络监测
@device_blueprint.route('/networkDetection', methods=['GET', 'POST'])
# @jwt_required()
def network_detection():
    return common.trueReturn(msg="1")

