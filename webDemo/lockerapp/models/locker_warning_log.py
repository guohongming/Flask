__author__ = 'Guo'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from lockerapp.users.model import db


class LockerWarningLog(db.Model):
    __tablename__ = 'locker_warning_log'
    id = db.Column(db.Integer, primary_key=True)
    locker_id = db.Column(db.INTEGER)
    warning_log = db.Column(db.INTEGER)
    del_flag = db.Column(db.INTEGER)
    create_time = db.Column(db.DATETIME)

    def __init__(self, locker_id = None , warning_log = None,del_flag  = None,create_time = None):
        self.locker_id = locker_id
        self.warning_log = warning_log
        self.del_flag = del_flag
        self.create_time = create_time

    def __repr__(self):
        return '<Post %r>' % self.warning_log

    def save(self):
        db.session.add(self)
        db.session.commit()

