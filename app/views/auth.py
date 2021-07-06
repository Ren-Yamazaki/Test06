from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import login_required,login_user,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.user import User
from app import db

auth=Blueprint('auth',__name__)

@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('auth/signup.html')
    else:
        email=request.form.get('email')
        name=request.form.get('name')
        password=request.form.get('password')

        if not name:
            flash('名前を入力してください。')
            return redirect(url_for('auth.signup'))

        if not email:
            flash('メールアドレスを入力してください。')
            return redirect(url_for('auth.signup'))

        if len(str(password)) < 8:
            flash('パスワードは８文字以上で入力してください。')
            return redirect(url_for('auth.signup'))

        user=User.query.filter_by(email=email).first()

        if user:
            flash('メールアドレスは既に登録されています。')
            return redirect(url_for('auth.signup'))

        new_user=User(email=email,name=name,password=generate_password_hash(password,method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        flash('新規登録に成功しました。')
        return redirect(url_for('index'))

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('auth/login.html')
    else:
        email=request.form.get('email')
        password=request.form.get('password')
        if request.form.get('remember'):
            remember=True
        else:
            remember=False

        user=User.query.filter_by(email=email).first()

        if not user or not check_password_hash(user.password,password):
            flash('メールアドレスもしくはパスワードに誤りがあります。')
            return render_template('auth/login.html')

        login_user(user,remember=remember)
        flash('ログインしました。')
        return redirect(url_for('index'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('ログアウトしました')
    return redirect(url_for('auth.login'))
