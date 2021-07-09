'''
*File Name :auth.py
*Version   :V2.0
*Designer  :山﨑　蓮
*Date      :2021.7.9
*Purpose   :ログイン，新規登録，ログアウトの機能を実装する
'''
from flask import Blueprint,render_template,redirect,url_for,request,flash
from flask_login import login_required,login_user,logout_user
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.user import User
from app import db

auth=Blueprint('auth',__name__)

'''
関数名 :signup
作成者名: 山﨑　蓮
日付   :2021.7.6
機能要約 :GETの場合は新規登録画面に飛ばし，POSTの場合は登録されたユーザ情報をデータベースに追加する。
'''
@auth.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=='GET':
        return render_template('auth/signup.html')
    else:
        email=request.form.get('email') #メールアドレス
        name=request.form.get('name')   #名前
        password=request.form.get('password') #パスワード

        #From.Added 山﨑　蓮　2021.7.6
        #条件を判定する，条件を満たさない場合はエラーメッセージを出力して新規登録画面にリダイレクトする。
        if not name:
            flash('名前を入力してください。')
            return redirect(url_for('auth.signup'))

        if not email:
            flash('メールアドレスを入力してください。')
            return redirect(url_for('auth.signup'))

        if len(str(password)) < 8:
            flash('パスワードは８文字以上で入力してください。')
            return redirect(url_for('auth.signup'))
        #To.Added 山﨑　蓮　2021.7.6

        user=User.query.filter_by(email=email).first()

        if user:
            flash('メールアドレスは既に登録されています。')
            return redirect(url_for('auth.signup'))

        #ユーザを作成してデータベースに追加
        new_user=User(email=email,name=name,password=generate_password_hash(password,method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        flash('新規登録に成功しました。')
        return redirect(url_for('index'))

'''
関数名 :login
作成者名: 山﨑　蓮
日付   :2021.7.6
機能要約 :GETの場合はログイン画面に飛ばし，POSTの場合はログイン処理を行う。
'''
@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('auth/login.html')
    else:
        email=request.form.get('email') #メールアドレス
        password=request.form.get('password') #パスワード

        #From.Changed 山﨑　蓮　2021.7.6
        if request.form.get('remember'): 
            remember=True #次回サイトにアクセスした際にログイン状態を保持するかを決めるもの
        else:
            remember=False
        #To.Changed 山﨑　蓮　2021.7.6

        user=User.query.filter_by(email=email).first()

        #From.Changed 山﨑　蓮　2021.7.6
        #ログインの判定，入力されたメールアドレスが登録されていないかパスワードが一致しない場合はエラーメッセージを出力
        if not user or not check_password_hash(user.password,password):
            flash('メールアドレスもしくはパスワードに誤りがあります。')
            return render_template('auth/login.html')
        #To.Changed 山﨑　蓮　2021.7.6

        login_user(user,remember=remember)
        flash('ログインしました。')
        return redirect(url_for('index'))

'''
関数名 :logout
作成者 :山﨑　蓮
日付   :2021.6.20
'''
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('ログアウトしました')
    return redirect(url_for('auth.login'))
