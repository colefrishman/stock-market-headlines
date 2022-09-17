import requests
from random import randint
import re
import os

def nyt_get_news():
	nyt_api_key = os.getenv('NYT_API_KEY')

	limit = 20
	url = f'https://api.nytimes.com/svc/topstories/v2/us.json?api-key={nyt_api_key}'
	r = requests.get(url)
	data = r.json()
	if 'error' in data:
		return "error"
	headline = data['results'][randint(0,limit)]['title']
	split_headline = re.split(',|;',headline)
	out = headline[0]
	for headline in split_headline:
		if ('say' not in headline.lower()) and (len(headline)>=len(out)):
			out = headline

	return out
