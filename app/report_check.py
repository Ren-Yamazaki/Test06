'''
*File Name :reportcheck.py
*Version   :V1.0
*Designer  :山﨑　蓮
*Date      :2021.6.21
*Purpose   :登録された記録情報を画面上に表示するhtmlファイルに登録情報と記録情報を渡す
'''

from flask import Blueprint,render_template,make_response
from app.models.task import Post,Report

rcheck=Blueprint('reportcheck',__name__)

#記録情報をhtmlファイルに渡す
@rcheck.route('/reportcheck/<int:id>')
def report_check(id):
    reports=Report.query.all()  #記録情報のリスト
    post=Post.query.get(id)     #登録情報のリスト

    #reportcheck.htmlを表示,その際記録情報のリストと登録情報のリストを渡す
    return render_template('reportcheck.html',reports=reports,post=post)
