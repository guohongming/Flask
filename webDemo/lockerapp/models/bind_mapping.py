__author__ = 'Guo'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from lockerapp.users.model import db


class BindMapping(db.Model):
    __tablename__ = 'bind_mapping'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    locker_id = db.Column(db.Integer)
    del_flag = db.Column(db.Integer)

    def __init__(self, user_id = None, locker_id = None, del_flag = 0):
        self.user_id = user_id
        self.locker_id = locker_id
        self.del_flag = del_flag

    def __repr__(self):
        return '<Post %r>' % self.mac

    def save(self):
        db.session.add(self)
        db.session.commit()
