'''
*File Name :__init__.py
*Version   :V1.1
*Designer  :山﨑　蓮
*Date      :2021.7.2
*Purpose   :アプリケーションの初期設定を行い，ログインやホームページについての設定も行う。
'''

from flask import Flask,render_template,url_for,request,redirect,make_response,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,login_required,current_user
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


'''
関数名 :index
作成者 :
日付   :2021.6.20
機能要約 :ホームページの設定をする。GETの場合はindex.htmlに飛ばし，POSTの場合は登録した情報をデータベースに追加する。
'''
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

        #From.Added 山﨑　蓮　2021.7.2
        users=User.query.all() #ユーザ情報
        for user in users:
            if user.name == student_id:
                user.Num_Of_Registration=user.Num_Of_Registration+1
        #To.Added 山﨑　蓮　2021.7.2

        db.session.add(new_post)
        db.session.commit()
        return redirect('/')


'''
関数名 :read
作成者 :山﨑　蓮
日付   :2021.6.20
機能要約 :進捗確認画面に飛ばす
'''
@app.route('/detail/<int:id>')
def read(id):
    post=Post.query.get(id)
    if current_user.name == post.student_id:
        return render_template('detail.html',post=post)
    else :
        flash('このページにはアクセスできません。')
        return redirect('/')
