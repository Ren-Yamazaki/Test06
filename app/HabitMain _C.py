'''
*  File Name		: HabitMain.py
*  Version		: V1.0
*  Designer		: 榎並龍大
*  Date			: 2021.06.02
*  Purpose       	: 新規登録画面から読み取ったデータをサーバへ出す。
'''
from flask import Flask, render_template, request,  redirect ,url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///r_info.db'
db_h = SQLAlchemy(app)

class Post(db_h.Model):
    id = db_h.Column(db_h.Integer,primary_key=True)
    student_id = db_h.Column(db_h.String(256), nullable=False)
    contents = db_h.Column(db_h.String(256), nullable=False)
    frequency = db_h.Column(db_h.String(256), nullable=False)
    period_s = db_h.Column(db_h.DateTime, nullable=False)
    period_e = db_h.Column(db_h.DateTime, nullable=False)
    distination = db_h.Column(db_h.String(256), nullable=False)
    difficulty = db_h.Column(db_h.String(256), nullable=False)
    field = db_h.Column(db_h.String(256), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def Habit_M():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('HabitMain.html',s_id='al19059',posts=posts) #s_idは暫定
    else:
        student_id = request.form.get('student_id') #学籍番号
        contents = request.form.get('contents') #内容
        frequency = request.form.get('frequency') #頻度
        period_s = request.form.get('period_s') #期間_start
        period_e = request.form.get('period_e') #期間_end
        distination = request.form.get('distination') #最終目標
        difficulty = request.form.get('difficulty') #難易度
        field = request.form.get('field') #分野

        period_s = datetime.strptime(period_s,'%Y-%m-%d')
        period_e = datetime.strptime(period_e,'%Y-%m-%d')
        new_post = Post(contents=contents,student_id=student_id,frequency=frequency,period_s=period_s,period_e=period_e,distination=distination,difficulty=difficulty,field=field)

        db_h.session.add(new_post)
        db_h.session.commit()

        return redirect('/')

@app.route('/check', methods=['GET', 'POST'])
def check():
    if request.method == 'GET':
        posts = Post.query.all()
        return render_template('check.html',posts=posts)
    else:
        student_id = request.form.get('student_id') #学籍番号
        contents = request.form.get('contents') #内容
        frequency = request.form.get('frequency') #頻度
        period_s = request.form.get('period_s') #期間_start
        period_e = request.form.get('period_e') #期間_end
        distination = request.form.get('distination') #最終目標
        difficulty = request.form.get('difficulty') #難易度
        field = request.form.get('field') #分野

        period_s = datetime.strptime(period_s,'%Y-%m-%d')
        period_e = datetime.strptime(period_e,'%Y-%m-%d')
        new_post = Post(contents=contents,student_id=student_id,frequency=frequency,period_s=period_s,period_e=period_e,distination=distination,difficulty=difficulty,field=field)

        db_h.session.add(new_post)
        db_h.session.commit()

        return redirect('/')

@app.route('/create_h')
def create_h():
    return render_template('create_h.html')

@app.route('/delete/<int:id>')
def delete(id):
    post = Post.query.get(id)

    db_h.session.delete(post)
    db_h.session.commit()
    return redirect('/')

    

if __name__ == '__main__':
    app.run(debug=True)
    