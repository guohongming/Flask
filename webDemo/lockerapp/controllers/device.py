__author__ = 'Guo'

import json

from flask import (Blueprint,
                   request,
                   jsonify)

from lockerapp import common
from flask_jwt import jwt_required, current_identity
from lockerapp.users.model import Users
from ..models.bind_mapping import BindMapping
from ..models.locker import Locker

device_blueprint = Blueprint(
    'device',
    __name__,
    template_folder='./templates'
)

# 现有锁具特征确认
@device_blueprint.route('/lockerFeatureConfirm', methods=['GET', 'POST'])
@jwt_required()
def locker_feature_confirm():
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)
    feature_id = data_json["feature_id"]

    return jsonify(common.trueReturn(data="1", msg="1"))


# 出入门显示功能选择
@device_blueprint.route('/inOutDoorDisplay', methods=['GET', 'POST'])
@jwt_required()
def in_out_door_display():
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)
    display = data_json['display']

    return jsonify(common.trueReturn(data="1", msg="1"))


# 附加提示音设置
@device_blueprint.route('/additionalBeepSettings', methods=['GET', 'POST'])
@jwt_required()
def additional_beep_settings():
    data = request.get_data().decode("utf-8")
    data_json = json.loads(data)
    setting_id = data_json['setting_id']

    return jsonify(common.trueReturn(data="1", msg="1"))


# 让服务器启动网络监测
@device_blueprint.route('/networkDetection', methods=['GET', 'POST'])
@jwt_required()
def network_detection():
    user = Users.get(Users, current_identity.id)
    user_id = user.id
    bind_mapping = BindMapping.query.filter(BindMapping.user_id == user_id, BindMapping.del_flag == 0).first()
    if bind_mapping:
        locker_id = bind_mapping.locker_id
        locker = Locker.query.filter(Locker.id == locker_id, Locker.del_flag == 0).first()
        if locker:
            locker.net = 1
            locker.save()
            return jsonify(common.trueReturn(data="1", msg="1"))
        else:
            return jsonify(common.falseReturn(data="", msg=""))
    return jsonify(common.falseReturn(data="", msg=""))


# 查询网络结果
@device_blueprint.route('/networkQuery', methods=['GET', 'POST'])
@jwt_required()
def network_query():
    user = Users.get(Users, current_identity.id)
    user_id = user.id
    bind_mapping = BindMapping.query.filter(BindMapping.user_id == user_id, BindMapping.del_flag == 0).first()
    if bind_mapping:
        locker_id = bind_mapping.locker_id
        locker = Locker.query.filter(Locker.id == locker_id, Locker.del_flag == 0).first()
        if locker:
            if locker.net is 2:
                locker.net = 0
                locker.save()
                return jsonify(common.trueReturn(data="1", msg="网络通畅"))
            else:
                return jsonify(common.falseReturn(data="", msg=""))
    return jsonify(common.falseReturn(data="", msg=""))
