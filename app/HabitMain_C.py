'''
*  File Name		: HabitMain.py
*  Version		: V1.0
*  Designer		: 榎並龍大
*  Date			: 2021.06.02
*  Purpose       	: 新規登録画面から読み取ったデータをサーバへ出す。
'''
from flask import Flask, render_template, request,  redirect ,url_for,Blueprint,flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app.models.post import Post
from app.models.record import Record
from app import db

hmain=Blueprint('habitmain',__name__)

@hmain.route('/create')
def create():
    return render_template('create_h.html')

@hmain.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')
