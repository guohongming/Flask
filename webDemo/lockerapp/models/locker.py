__author__ = 'Guo'

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
from lockerapp.users.model import db


class Locker(db.Model):
    __tablename__ = 'locker'
    id = db.Column(db.Integer, primary_key=True)
    mac = db.Column(db.String(100))
    tips = db.Column(db.String(2))
    feature_id = db.Column(db.String(2))
    chu_ru = db.Column(db.String)
    net = db.Column(db.INTEGER)
    del_flag = db.Column(db.INTEGER)

    def __init__(self, mac, del_flag, feature_id, chu_ru, tips, net):
        self.mac = mac
        self.feature_id = feature_id
        self.chu_ru = chu_ru
        self.tips = tips
        self.net = net
        self.del_flag = del_flag

    def __repr__(self):
        return '<Post %r>' % self.mac

    def save(self):
        db.session.add(self)
        db.session.commit()
