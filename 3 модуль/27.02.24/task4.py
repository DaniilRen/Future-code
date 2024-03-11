from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
	n1, n2 = request.args.get('n1'), request.args.get('n2')
	if n1 and n2:
		return render_template('index4.html', n1=n1, n2=n2, n3=n1+n2)
	return render_template('index4.html', n1=1, n2=1, n3=2)

app.run(host='0.0.0.0', port=4001, debug=True)