'''
*File Name :reportcheck.py
*Version   :V1.0
*Designer  :山﨑　蓮
*Date      :2021.6.19
*Purpose   :登録された記録情報を画面上に表示するhtmlファイルに登録情報と記録情報を渡す
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

#登録情報
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(30),nullable=False)
    detail=db.Column(db.String(100))
    due=db.Column(db.DateTime,nullable=False)
    name=db.Column(db.String(100),nullable=False)

#記録情報
class Report(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.DateTime,nullable=False)
    comment=db.Column(db.String(100))
    times=db.Column(db.Integer,nullable=False)
    name=db.Column(db.String(100),nullable=False)
    pid=db.Column(db.Integer)
