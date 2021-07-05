from flask_login import login_user,logout_user
from sqlalchemy.exc import SQLAlchemyError
from app import db
from app.models.user import User
from flask import render_template,flash

#新規登録
def signup(data: {}) -> User:
    try:
        name=data.get('name')
        email=data.get('email')
        password=data.get('password')
        #ユーザ登録の確認
        user=User.query.filter_by(email=email).first()
        if user:
            return user
        new_user=User.from_args(name,email,password)
        db.session.add(new_user)
        db.session.commit()
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError

def login(data: {}) -> User:
    try:
        email=data.get('email')
        password=data.get('password')
        remember=True if data.get('remember') else False
        user=User.query.filter_by(email=email).first()

        if not user:
            raise SQLAlchemyError
        #ユーザとパスワードの確認
        if not user.check_password(password):
            raise SQLAlchemyError

        #ログイン,rememberにチェックを入れていればログインが維持される
        login_user(user,remember=remember)
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError

def logout():
    logout_user()
    return True
