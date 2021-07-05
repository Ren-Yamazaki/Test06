from flask import Flask,render_template,url_for,request,redirect,make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_required
from datetime import datetime


app=Flask(__name__)

app.secret_key="super secret key"
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Syukanmanage.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

login_manager=LoginManager()
login_manager.login_view='auth.login'
login_manager.init_app(app)

from app.models.user import User
from app.models.post import Post

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.views.auth import auth
app.register_blueprint(auth)
from app.report_check import rcheck
app.register_blueprint(rcheck)
from app.reportgraph import graph
app.register_blueprint(graph)
from app.M5_main import cmain
app.register_blueprint(cmain)
from app.HabitMain_C import hmain
app.register_blueprint(hmain)
from app.record import record
app.register_blueprint(record)


@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        posts = Post.query.order_by(Post.period_s).all()
        return render_template('index.html',posts=posts)
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

        users=User.query.all()
        for user in users:
            if user.name == student_id:
                user.Num_Of_Registration=user.Num_Of_Registration+1

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')

@app.route('/detail/<int:id>')
def read(id):
    post=Post.query.get(id)
    return render_template('detail.html',post=post)
