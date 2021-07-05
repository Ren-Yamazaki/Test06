from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

#登録情報
class Post(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.String(256), nullable=False)
    contents = db.Column(db.String(256), nullable=False)
    frequency = db.Column(db.String(256), nullable=False)
    period_s = db.Column(db.DateTime, nullable=False)
    period_e = db.Column(db.DateTime, nullable=False)
    distination = db.Column(db.String(256), nullable=False)
    difficulty = db.Column(db.String(256), nullable=False)
    field = db.Column(db.String(256), nullable=False)
