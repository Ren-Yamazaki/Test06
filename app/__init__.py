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
from app.models.task import Post,Report

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from app.views.auth import auth
app.register_blueprint(auth)
from app.report_check import rcheck
app.register_blueprint(rcheck)
from app.reportgraph import graph
app.register_blueprint(graph)

@app.route('/',methods=['GET','POST'])
@login_required
def index():
    if request.method=='GET':
        posts=Post.query.order_by(Post.due).all()
        return render_template('index.html',posts=posts)
    else:
        title=request.form.get('title')
        detail=request.form.get('detail')
        due=request.form.get('due')
        name=request.form.get('name')

        due=datetime.strptime(due,'%Y-%m-%d')
        new_post=Post(title=title,detail=detail,due=due,name=name)

        db.session.add(new_post)
        db.session.commit()

        return redirect('/')


@app.route('/report/<int:id>',methods=['GET','POST'])
def report(id):
    post=Post.query.get(id)
    report=Report.query.get(id)
    if request.method=='GET':
        post=Post.query.get(id)
        return render_template('report.html',post=post)
    else:
        date=request.form.get('date')
        comment=request.form.get('comment')
        times=request.form.get('times')
        date=datetime.strptime(date,'%Y-%m-%d')
        name=request.form.get('name')
        pid=post.id

        new_report=Report(date=date,comment=comment,times=times,name=name,pid=pid)

        db.session.add(new_report)
        db.session.commit()
        return redirect('/')
    return render_template('detail.html',post=post)


@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/detail/<int:id>')
def read(id):
    post=Post.query.get(id)
    return render_template('detail.html',post=post)

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    post=Post.query.get(id)
    if request.method=='GET':
        return render_template('update.html',post=post)
    else:
        post.title=request.form.get('title')
        post.detail=request.form.get('detail')
        post.due=datetime.strptime(request.form.get('due'),'%Y-%m-%d')
        post.name=request.form.get('name')

        db.session.commit()
        return redirect('/')
    return render_template('detail.html',post=post)

@app.route('/delete/<int:id>')
def delete(id):
    post=Post.query.get(id)

    db.session.delete(post)
    db.session.commit()
    return redirect('/')

