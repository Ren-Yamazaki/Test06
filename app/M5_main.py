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
from flask import Flask, render_template, request, redirect,session,url_for,Blueprint # 追加で2つimportする
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import numpy as np
import cgi
from app import db


cmain=Blueprint('charactermain',__name__)

#M5で必要なデータベースの記録(内部設計書より)
"""
id(Integer)→id，主キー
name(String)→名前，1000文字
Num_Of_Registration→登録した習慣化数
level(Integer)→使用可能アイテム数  ※Num_Of_Registrationに応じて増加
"""
ItemALL = ['レベルを上げて称号をゲットしよう!','初めての称号！！','2個目の称号！！','3個目の称号！！','4個目の称号！！','5個目の称号！！']
#ここでアイテムの名前と順番を設定

from app.models.user import User
@cmain.route('/status/<int:id>',methods=['GET','POST'])
def M5_main(id):
    user=User.query.get(id) # .all()は必要ないかも？
    new_level=int(user.Num_Of_Registration/4)
    user.level=new_level
    #db.session.commit()  #levelはその都度計算するからDBにおいておく必要ないかも

    if new_level == 0:
        show_item_names=ItemALL[0:1]
    else:
        show_item_names=ItemALL[1:new_level+1] #ItemALLのリストからnew_levelの数だけ1番目から取り出す
    #status画面に表示する基礎情報とアイテム名を渡す
    return render_template('M5_main.html',posts=user,show_item_names=show_item_names)
