__author__ = 'Guo'


def trueReturn(data=None, msg=None):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(data=None, msg=None):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }
