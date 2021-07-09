'''
*File Name :user.py
*Version   :V1.1
*Designer  :山﨑　蓮
*Date      :2021.7.2
*Purpose   :データベースに追加するためのユーザモデルを定義する。
'''

from flask_login import UserMixin
from app import db

class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True) #ID,主キー
    email=db.Column(db.String(100),unique=True,nullable=False) #メールアドレス
    name=db.Column(db.String(1000),nullable=False) #名前
    password=db.Column(db.String(100),nullable=False) #パスワード
    #From.Added 山﨑　蓮　2021.7.2
    Num_Of_Registration = db.Column(db.Integer , default=0 ) #登録された習慣の数,初期値は0
    #To.Added 山﨑　蓮　2021.7.2
