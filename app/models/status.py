from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db

#キャラクター情報
class status(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000))
    Num_Of_Registration = db.Column(db.Integer,nullable=False)
