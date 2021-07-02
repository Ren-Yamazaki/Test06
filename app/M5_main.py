''' 
*  File Name		: M5_main.py 
*  Version		: V1.0
*  Designer		: 落合 祐介 
*  Date			: 2021.07.02 
*  Purpose       	: ステータス一覧画面を表示する 
''' 
''' 
* Revision : 
* V1.0 : 作成者名, yyyy.mm.dd 
* V1.1 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く 
* V1.2 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く 
* V1.3 : 修正者名, yyyy.mm.dd 改訂モジュール名を書く 
''' 

from operator import and_, methodcaller
from flask import Flask, render_template, request, redirect,session,url_for # 追加で2つimportする
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import numpy as np
import cgi

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///F4.db'
db = SQLAlchemy(app)

#M5で必要なデータベースの記録(内部設計書より)
"""
id(Integer)→id，主キー
name(String)→名前，1000文字
Num_Of_Registration→登録した習慣化数
level(Integer)→使用可能アイテム数  ※Num_Of_Registrationに応じて増加
"""
class status(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(1000))
    Num_Of_Registration = db.Column(db.Integer,nullable=False)

ItemALL = ['レベルを上げて称号をゲットしよう!','初めての称号！！','2個目の称号！！','3個目の称号！！','4個目の称号！！','5個目の称号！！']
#ここでアイテムの名前と順番を設定


@app.route('/status/<int:id>',methods=['GET','POST'])
def M5_main(id):
    post=status.query.get(id) # .all()は必要ないかも？
    new_level=int(post.Num_Of_Registration/4)
    post.level=new_level
    #db.session.commit()  #levelはその都度計算するからDBにおいておく必要ないかも
    
    #posts=status.query.all()
    #posts=db.session.execute("SELECT * FROM status WHERE name=name")
    '''
    g = open('posts.txt', 'w') 
    for a in posts:
        g.write(str(a) + "\n")
    g.close()
    '''
    #(xがstatus.amount_useableに依存するようにする)

    #t=text("SELECT * FROM status WHERE status.name == '%s' " % (name))    #謎のエラーによりやむなくSQL文を直接使用
    #確認用
    
    '''
    g = open('list.txt', 'w') 
    for list in db.session.execute(t):
        g.write(str(list)+"\n")
    g.close()     
    '''
    #x=list[3]   #xにamount_useable(文字列)を代入
    ''''
    h = open('list.txt','a')
    h.write(str(x))    
    h.close()
    '''
    #x=int(x)    #xを文字列から数値に変換

    if new_level == 0:
        show_item_names=ItemALL[0:1]
    else:
        show_item_names=ItemALL[1:new_level+1] #ItemALLのリストからnew_levelの数だけ1番目から取り出す

    #確認用 
    '''
    g = open('ItemALL.txt', 'w') 
    for a in show_item_names:
        g.write(str(a) + "\n")
    g.close()   
    '''
    #status画面に表示する基礎情報とアイテム名を渡す
    return render_template('M5_main.html',posts=post,show_item_names=show_item_names)

@app.route('/regist_db')    #dbに登録(テスト・確認用)
def touroku():
    if request.method =='GET':
        return render_template('/regist_db.html')
    else:
        name = request.form.get('name')
        #item_use_id = request.form.get('item_use_id')
        #level = request.form.get('level')
        Num_Of_Registration = request.form.get('Num_Of_Registration')
        #amount_useable = request.form.get('amount_useable')
        #change_item_id = request.form.get('change_item_id')

        new_post = status(name=name, Num_Of_Registration=Num_Of_Registration)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    post = status.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/db_all')

@app.route('/db_all',methods=['GET','POST'])
def registed():
    if request.method == 'GET':
        #posts=db.session.execute("SELECT * FROM status")
        posts=status.query.all()
        return render_template('db_all.html',posts=posts)
    else:
        name = request.form.get('name')
        #item_use_id = request.form.get('item_use_id')
        #level = request.form.get('level')
        Num_Of_Registration = request.form.get('Num_Of_Registration')
        #amount_useable = request.form.get('amount_useable')
        #change_item_id = request.form.get('change_item_id')

        new_post = status(name=name, Num_Of_Registration=Num_Of_Registration)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/db_all')


if __name__ == "__main__":
    app.run(debug=True)
