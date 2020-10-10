from datetime import datetime

from core import models

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
db = SQLAlchemy()
class User(db.Model):
    __tablename__ = "user"
    username = db.Column(db.Integer,primary_key=True)
    pwd =  db.Column(db.String,default='')
    last_time = db.Column(db.TIMESTAMP,nullable=False,default=datetime.now())
    def __init__(self,name: str,pwd: str):
        self.username = name
        self.pwd = pwd
    def toDict(self):
        return { c.key: getattr(self, c.key)for c in inspect(self).mapper.column_attrs }


def adduser(username,pwd):
    user = User(name=username,pwd=pwd)
    db.session.add(user)
    db.session.commit()
    return True

def search_user_info(user_id):
    user = User.query.first()
    print("user",user.toDict())