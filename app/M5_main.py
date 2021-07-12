''' 
*  File Name		: M5_main.py 
*  Version		: V1.1
*  Designer		: 落合 祐介 
*  Date			: 2021.07.02 
*  Purpose       	: ステータス一覧画面を表示する 
''' 

from operator import and_, methodcaller
from flask import Flask, render_template, request, redirect,session,url_for,Blueprint 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
import numpy as np
import cgi
from app import db

cmain=Blueprint('charactermain',__name__)

#M5_main.pyで使用した変数の説明
"""
* id(Integer)→id，主キー
* name(String)→名前，1000文字
* Num_Of_Registration→登録した習慣化数
* level(Integer)→使用可能アイテム数  ※Num_Of_Registrationに応じて増加
"""
#称号と順番を設定
ItemALL = ['レベルを上げて称号をゲットしよう!','物事をうまく始められたなら、半分できたも同然だ。　　アリストテレス',
           '勝者と敗者の違いはたいていの場合、、、やめないことである。　　ウォルト・ディズニー',
           '私たちの最大の弱点は諦めることにある。成功するのに最も確実な方法は、常にもう一回だけ試してみることだ。　　トーマス・エジソン',
           '挑戦を続ける限りあなたにできないことはないのだ。　　アレクサンドロス大王',
           '自分に打ち勝つことが、最も偉大な勝利である。　　プラトン']

from app.models.user import User
@cmain.route('/status/<int:id>',methods=['GET','POST'])
def M5_main(id):
    user=User.query.get(id)
    #From. Added 落合祐介 2021.07.12
    new_level=int(user.Num_Of_Registration/4)
    user.level=new_level

    if new_level == 0:
        show_item_names=ItemALL[0:1]
    else:
        #表示する称号のリストを作成
        show_item_names=ItemALL[1:new_level+1] 
    #To. Added 落合祐介　2021.07.12
    #ステータス一覧画面に表示するステータス情報と称号リストを渡す
    return render_template('M5_main.html',posts=user,show_item_names=show_item_names)
