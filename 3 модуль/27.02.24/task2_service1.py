import requests

def ping():
	url = 'http://127.0.0.1:4001/pong'
	json_ = {'data': 'ping'}
	req = requests.post(url, json_)
	print(req.text)

ping()