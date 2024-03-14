from flask import Flask
from flask import jsonify, abort
from peewee import *
from db_utils import *

app = Flask(__name__)

@app.route('/cars')
def home_page():
	abort(400)


@app.route('/cars/<int:id>', methods=['GET'])
def get_car_model(id):
	if not 0 < int(id) <= get_max_id():
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


@app.route('/cars/<model>', methods=['POST'])
def create_car_model(model):
	if len(model) == 0:
		abort(400)
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


@app.route('/cars/<int:id>/<model>', methods=['PUT'])
def update_car_model(id, model):
	if not 0 < int(id) <= get_max_id():
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
def delete_car_model(id):
	if not 0 < int(id) <= get_max_id():
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