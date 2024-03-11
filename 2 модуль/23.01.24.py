import requests
from bs4 import BeautifulSoup
import pandas as pd


## 1 Задание

def make_request():
	res = requests.get('https://www.boredapi.com/api/activity').json()
	return res['activity']

def activity_cycle():
	c = 0
	while c < 3:
		activity = make_request()
		print(f'Выбрать данную активность? : {activity}')
		if input('y (да) / n (нет)') == 'y':
			c += 1


## 2 Задание

def html_to_df():
	with open('index.html', 'r') as f:
		text = f.read()
		soup = BeautifulSoup(text, 'html.parser')
		data = soup.find_all('div', {'class': 'card'})
		res = []
		for i in range(len(data)):
			res.append([data[i].find('a', {'class': 'card__title'}).text.strip(), data[i].find('div', {'class': 'card__price'}).text])
		df = pd.DataFrame(res, columns=['Title', 'Price'])
		print(df)


activity_cycle()
html_to_df()