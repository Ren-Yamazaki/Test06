'''
*  File Name		: HabitMain.py
*  Version		: V1.1
*  Designer		: 榎並 龍大
*  Date			: 2021.07.12
*  Purpose       	: 新規登録画面から読み取ったデータをサーバへ出す。
'''
from flask import Flask, render_template, request,  redirect ,url_for,Blueprint,flash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from app.models.post import Post
from app.models.record import Record
from app import db

hmain=Blueprint('habitmain',__name__)

#習慣化登録
@hmain.route('/create')
def create():
    return render_template('create_h.html')

#データ削除
@hmain.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')
