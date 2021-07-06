'''
*File Name :reportcheck.py
*Version   :V1.0
*Designer  :山﨑　蓮
*Date      :2021.6.21
*Purpose   :登録された記録情報についてのグラフを作成し，表示する
'''
from flask import Blueprint,make_response
from app.models.post import Post
from app.models.record import Record
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

graph=Blueprint('recordcheck',__name__)


#グラフを作成し，画面上に表示する
@graph.route('/reportgraph/<int:id>')
def reportgraph(id):
    reports=Record.query.order_by(Record.date).all() #日付順に並べて，記録情報を取得
    post=Post.query.get(id)                          #引数で渡されたidについての登録情報を取得
    y=[]  #縦軸
    x=[]  #横軸

    #縦軸に登録情報の進歩，横軸に日付を追加
    for report in reports:
        if report.pid == post.id:
            y.append(report.time)
            d=report.date.strftime('%m-%d')
            x.append(d)

    #グラフを作成
    fig=plt.figure()
    ax=fig.add_subplot(111)
    plt.cla()
    ttl=post.contents
    plt.grid(which='both')
    plt.legend()
    plt.plot(x,y)

    #グラフを画像で出力
    canvas=FigureCanvasAgg(fig)
    png_output=BytesIO()
    canvas.print_png(png_output)
    data=png_output.getvalue()

    #出力した画像を画面上に表示
    response=make_response(data)
    response.headers['Content-Type']='image/png'
    response.headers['Content-Length']=len(data)
    return response
