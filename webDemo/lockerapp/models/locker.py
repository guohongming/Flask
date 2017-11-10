__author__ = 'Guo'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from lockerapp.users.model import db


class Locker(db.Model):
    __tablename__ = 'locker'
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(100))
    del_flag = db.Column(db.INTEGER)

    def __init__(self, mac, del_flag):
        self.mac = mac
        self.del_flag = del_flag

    def __repr__(self):
        return '<Post %r>' % self.mac

    def save(self):
        db.session.add(self)
        db.session.commit()
