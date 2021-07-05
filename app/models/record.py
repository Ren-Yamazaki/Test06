from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from .post import Post


#記録情報
class Record(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    comment = db.Column(db.String(100))
    time = db.Column(db.Integer, nullable=False)
    pid=db.Column(db.Integer,nullable=False)
