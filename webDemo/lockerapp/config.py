__author__ = 'Guo'
from os import path
import datetime

class Config(object):
    #　JWT_AUTH_USERNAME_KEY='blank'
    SECRET_KEY = 'this is blank guo'
    JWT_AUTH_URL_RULE = '/login'
    JWT_EXPIRATION_DELTA = datetime.timedelta(weeks=4)
    # JWT_NOT_BEFORE_DELTA = datetime.timedelta(weeks=1)
    pass


class prodConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://blank:Guo1006575211@47.94.223.220:3306/smart_lock'
    #  JWT_AUTH_USERNAME_KEY='blank'
    #  JWT_AUTH_URL_RULE = '/login'
    # JWT_AUTH_USERNAME_KEY='blank'
