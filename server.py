from flask import Flask, render_template, redirect, url_for
import requests, json
app = Flask(__name__)
app.config.from_pyfile('config.cfg')



@app.route('/')

def index():
	return redirect('/congnghe')
	

@app.route('/congnghe')

def congnghe():
	url_thethao = 'http://api.news.zing.vn/api/mobile/cong-nghe.json?p=1&c=50'
	a = requests.get(url_thethao)
	data_congnghe = a.json()
	congnghe = data_congnghe['data']

	return render_template('CN.html', congnghe = congnghe)


@app.route('/phapluat')

def phapluat():
	url_thethao = 'http://api.news.zing.vn/api/mobile/phap-luat.json?p=1&c=50'
	a = requests.get(url_thethao)
	data_phapluat = a.json()
	phapluat = data_phapluat['data']

	return render_template('PL.html', phapluat = phapluat)



@app.route('/newsbook')

def book():
	url_book = 'http://api.news.zing.vn/api/mobile/xuat-ban.json?p=1&c=50'
	a = requests.get(url_book)
	data_book = a.json()
	news_book = data_book['data']

	return render_template('book.html', book = news_book )


@app.route('/sport')

def sports():
	url_sport = 'http://api.news.zing.vn/api/mobile/the-thao.json?p=1&c=50'
	a = requests.get(url_sport)
	data_sport = a.json()
	sport = data_sport['data']
	return render_template('sports.html', sports = sport)


@app.route('/fashion')

def fashion():
    url_fashion = 'http://api.news.zing.vn/api/mobile/thoi-trang.json?p=1&c=50'
    a = requests.get(url_fashion)
    data_fashion = a.json()
    fashion = data_fashion['data']
    return render_template('fashion.html', fashion = fashion)



if __name__ == "__main__":
	app.run()
