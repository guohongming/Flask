__author__ = 'Guo'
from os import path

class Config(object):
    SECRET_KEY = 'this is blank guo'
    pass


class prodConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database_user.db'
