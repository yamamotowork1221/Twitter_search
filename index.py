import os
#Flask インポート
from flask import Flask, render_template, request, session 
from datetime import timedelta
# .envファイル インポート
from dotenv import load_dotenv
# 検索API実行 インポート
from app import search_results
from app import usertweets

# .env 読み込み
load_dotenv()

# Flask起動
# Flaskクラスをインスタンス化して変数appに割り当てる
app = Flask(__name__)

# flask session 暗号化キー
app.secret_key = os.environ['SECRET_KEY']
#Flask session 保持時間
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/search", methods=['GET','POST'])
def search():
	if request.method == 'GET':
		return render_template('search.html')
	elif request.method == 'POST':
		session['input_keyword'] = request.form['input_keyword']
		search_results_raws = search_results.search_results()
		if search_results_raws is not None:
			return render_template('search.html' , search_results_raws_zip = zip(search_results_raws[0], search_results_raws[1]))
		else:
			return render_template('search.html' , search_results_raws_zip = None )

@app.route("/usertweet", methods=['GET','POST'])
def usertweet():
	if request.method == 'GET':
		return render_template('usertweet.html')
	elif request.method == 'POST':
		session['input_keyword'] = request.form['input_keyword']
		search_results_raws = usertweets.usertweets()
		if search_results_raws is not None:
			return render_template('usertweet.html' , search_results_raws = search_results_raws[0] , user_data_raws =  search_results_raws[1])
		else:
			return render_template('usertweet.html' , search_results_raws = None )

# ローカルサーバー起動
if __name__ == '__main__':
  app.run(host=os.getenv('APP_ADDRESS', 'localhost'), port=8000)