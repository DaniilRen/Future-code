from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
	return render_template('index3.html', num1=24, num2=3, num3=27)

app.run(host='0.0.0.0', port=4001, debug=True)