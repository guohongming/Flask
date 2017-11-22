__author__ = 'Guo'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from lockerapp.users.model import db


class LockerForgetLog(db.Model):
    __tablename__ = 'locker_forget_log'
    id = db.Column(db.Integer, primary_key=True)
    locker_id = db.Column(db.INTEGER)
    forget_log = db.Column(db.INTEGER)
    del_flag = db.Column(db.INTEGER)
    create_time = db.Column(db.DATETIME)

    def __init__(self, locker_id, forget_log,del_flag,create_time):
        self.locker_id = locker_id
        self.forget_log = forget_log
        self.del_flag = del_flag
        self.create_time = create_time

    def __repr__(self):
        return '<Post %r>' % self.forget_log

    def save(self):
        db.session.add(self)
        db.session.commit()
