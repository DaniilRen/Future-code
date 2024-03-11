from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/pong', methods=['POST'])
def index():
	print(request.form.get('data'))
	return 'pong'

app.run(host='0.0.0.0', port=4001, debug=True)