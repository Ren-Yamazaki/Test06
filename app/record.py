'''
*File Name :record.py
*Version   :V1.0
*Designer  :根岸　純平
*Date      :2021.6.28
*Purpose   :取り組んだ内容を記録する
'''

from datetime import datetime

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

record = Flask(__name__)
record.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(record)

class Record(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    comment = db.Column(db.String(100))
    time = db.Column(db.Integer, nullable=False)

#データベースに記録する
@record.route('/record', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        posts = Record.query.all()
        return render_template('record.html', posts=posts)
    else:
        date = request.form.get('date')
        comment = request.form.get('comment')
        time = request.form.get('time')

        date = datetime.strptime(date, '%Y-%m-%d')
        new_post = Record(date=date, comment=comment, time=time)

        db.session.add(new_post)
        db.session.commit()

        return redirect('/record.html')



if __name__ == '__main__':
    record.run(debug=True)
    