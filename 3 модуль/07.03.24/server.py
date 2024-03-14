from flask import Flask
from flask import jsonify, abort
from peewee import *
from db_utils import *

init_table()
app = Flask(__name__)


@app.route('/login/<name>/<surname>/<password>')
def login(name, surname, password):
		print(name, surname, password)
		if not check_name(name, surname):
			return jsonify({'Status': 'USER NOT FOUND'})
		if not check_password(name, surname, password):
			return jsonify({'Status': 'WRONG PASSWORD'})
		return jsonify({'Status': 'Success'})

@app.route('/cars')
def home_page():
	abort(400)

@app.route('/cars/<model>', methods=['POST'])
def create(model):
	if len(model) == 0:
		abort(400)
	print('------------', model)
	create_el(model)
	return jsonify(
		{
			'Status': 'Success',
			'Info': 
			{
			'Id': f'{get_max_id()}',
			'Model': f'{model}'
			}
		})

@app.route('/cars/<int:id>', methods=['GET'])
def read(id):
	if not 0 < int(id) <= get_max_id() or not check_id(id):
		abort(404)
	return jsonify(
		{
			'Status': 'Success',
			'Info': 
			{
			'Id': f'{id}',
			'Model': f'{get_el(id)}'
			}
		})

@app.route('/cars/<int:id>/<model>', methods=['PUT'])
def update(id, model):
	if not 0 < int(id) <= get_max_id() or not check_id(id):
		abort(404)
	if len(model) == 0:
		abort(400)
	update_el(id, model)
	return jsonify(
		{
			'Status': 'Success',
			'Info': 
			{
			'Id': f'{id}',
			'Model': f'{model}'
			}
		})

@app.route('/cars/<int:id>', methods=['DELETE'])
def delete(id):
	if not 0 < int(id) <= get_max_id() or not check_id(id):
		abort(404)
	model = get_el(id)
	del_el(id)
	return jsonify(
		{
			'Status': 'Success',
			'Info': 
			{
			'Id': f'{id}',
			'Model': f'{model}'
			}
		})

@app.errorhandler(404)
def not_found(err):
	return jsonify(
		{
		'Status': 'Error',
		'Info':
		{
		'Id': 'Wrong id',
		'Model': 'Not found'
		}
		})

@app.errorhandler(400)
def not_found(err):
		return jsonify({
		'Status': 'Error',
		'Info':
		{
		'Id': 'Not specified',
		'Model': 'Bad request'
		}
		})


app.run(host='0.0.0.0', port=4001, debug=True)