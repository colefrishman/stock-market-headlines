import string
from headlines import nyt_get_news
import requests
from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
	alphavantage_api_key = os.getenv('ALPHAVANTAGE_API_KEY')
	url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SPY&apikey={alphavantage_api_key}'
	r = requests.get(url)
	data = r.json()
	
	change_pct = float(data['Global Quote']['10. change percent'].strip('%'))

	out = ""

	if abs(change_pct) < 0.1:
		out = "Stocks stagnant"
	if change_pct > 1:
		out = "Stocks soar"
	if change_pct < -1:
		out = "Stocks plummet"
	if change_pct > 0:
		out = "Stocks rise"
	if change_pct < 0:
		out = "Stocks fall"

	out = string.capwords(f'{out} as {nyt_get_news()}')
	return out


@app.route('/stock-price')
def stock_price():
	alphavantage_api_key = os.getenv('ALPHAVANTAGE_API_KEY')
	url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=SPY&apikey={alphavantage_api_key}'
	r = requests.get(url)
	data = r.json()

	return data


@app.route('/random-headline')	
def headlines():
	return nyt_get_news()

if __name__ == "__main__":
	app.run()
