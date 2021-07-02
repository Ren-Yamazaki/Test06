'''
*File Name :record.py
*Version   :V1.0
*Designer  :根岸　純平
*Date      :2021.6.28
*Purpose   :ホーム画面を表示する
'''

from flask import Flask, render_template, request, redirect


app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
    