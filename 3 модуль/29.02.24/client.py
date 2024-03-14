from flask import Flask
from flask import request, render_template
import requests
from json import dumps

app = Flask(__name__)

@app.route('/')
def cars():
	id_ = request.args.get('id')
	del_ = request.args.get('del')
	upd_ = request.args.get('upd')
	crt_ = request.args.get('crt')

	if id_ != None:
		resp = requests.get(f'http://127.0.0.1:4001/cars/{id_}')
		return render_template('client.html', 
													status=f"Search for {id_}: {resp.json()['Status']}",
													info=dumps(resp.json()['Info']))
	if crt_ != None:
		resp = requests.post(f"http://127.0.0.1:4001/cars/{crt_}")
		return render_template('client.html',
													status=f"Creating {crt_}: {resp.json()['Status']}",
													info=dumps(resp.json()['Info']))
	if del_ != None:
		resp = requests.delete(f'http://127.0.0.1:4001/cars/{del_}')
		return render_template('client.html', 
													status=f"Deleteting {del_}: {resp.json()['Status']}",
													info=dumps(resp.json()['Info']))
	if upd_ != None:
		id_, new_ = upd_.split(',')
		resp = requests.put(f'http://127.0.0.1:4001/cars/{id_}/{new_}')
		return render_template('client.html', 
													status=f"Updating {id_} to {new_}: {resp.json()['Status']}",
													info=dumps(resp.json()['Info']))

	return render_template('client.html')


app.run(host='0.0.0.0', port=4002, debug=True)