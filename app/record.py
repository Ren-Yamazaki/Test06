'''
*File Name :record.py
*Version   :V1.0
*Designer  :根岸　純平
*Date      :2021.6.28
*Purpose   :取り組んだ内容を記録する
'''

from datetime import datetime

from flask import Flask, render_template, request, redirect,Blueprint
from flask_sqlalchemy import SQLAlchemy
from app.models.record import Record
from app.models.post import Post
from app import db

record=Blueprint("records",__name__)

'''
*module name :M9  記録リスト受け渡し処理
*Designer    :根岸　純平
*Date        :2021.6.28
*Purpose     :日付、コメント、時間をDBに記録する
'''
@record.route('/record/<int:id>', methods=['GET', 'POST'])
def newrecord(id):
    post=Post.query.get(id)
    if request.method == 'GET':
        post = Post.query.get(id)
        return render_template('record.html', post=post)
    else:
        date = request.form.get('date')
        comment = request.form.get('comment')
        time = request.form.get('time')
        pid=post.id

        date = datetime.strptime(date, '%Y-%m-%d')
        new_record = Record(date=date, comment=comment, time=time,pid=pid)

        db.session.add(new_record)
        db.session.commit()
        return redirect('/')

    return render_template('index.html',post=post)
