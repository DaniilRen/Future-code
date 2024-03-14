import requests
import flet as ft
from re import fullmatch

def main(page: ft.Page):

	def create(e):
		id = cr_field.value
		if len(id) > 29:
			cr_field.value = 'Model should be contain less then 30 characters'
			page.update()
			return
		print(id)
		resp = requests.post(f'http://127.0.0.1:4001/cars/{id}')
		print(resp)
		output = f"Status: {resp.json()['Status']}. \
			Id: {resp.json()['Info']['Id']}, Model: {resp.json()['Info']['Model']}"
		console.value = output
		page.update()

	def read(e):
		id = read_field.value
		print(id)
		if not id.isdigit():
			read_field.value = 'Id should content only numbers'
			page.update()
			return
		resp = requests.get(f'http://127.0.0.1:4001/cars/{id}')
		output = f"Status: {resp.json()['Status']}. \
			Id: {resp.json()['Info']['Id']}, Model: {resp.json()['Info']['Model']}"
		console.value = output
		page.update()

	def update(e):
		id_and_model = upd_field.value
		print(id_and_model)
		if fullmatch(r'\d+ \w+', id_and_model) == None:
			upd_field.value = 'Warning: Id should content only numbers!'
			page.update()
			return
		id, model = id_and_model.split(' ')
		resp = requests.put(f'http://127.0.0.1:4001/cars/{id}/{model}')
		output = f"Status: {resp.json()['Status']}. \
			Id: {resp.json()['Info']['Id']}, Model: {resp.json()['Info']['Model']}"
		console.value = output
		page.update()
	
	def delete(e):
		id = del_field.value
		if not id.isdigit():
			del_field.value = 'Id should content only numbers'
			page.update()
			return
		resp = requests.delete(f'http://127.0.0.1:4001/cars/{id}')
		output = f"Status: {resp.json()['Status']}. \
			Id: {resp.json()['Info']['Id']}, Model: {resp.json()['Info']['Model']}"
		console.value = output
		page.update()

	page.title = "Car database remote control"
	info = ft.Text('This program performs CRUD operations with database (creates, reads, updates or deletes car models)\nTo use it type your queries into following fields abd press enter:',
								size=18)
	cr_field = ft.TextField(label='Create car model', on_submit=create)
	read_field = ft.TextField(label='Search for model by id', on_submit=read)
	upd_field = ft.TextField(label='Update model by id', on_submit=update)
	del_field = ft.TextField(label='Delete model by id', on_submit=delete)
	console = ft.Text('-- Output --', text_align=ft.TextAlign.CENTER, width=100,
									  size=16, weight=ft.FontWeight.W_800,)

	page.add(info)
	page.add(cr_field, read_field, upd_field, del_field)
	page.add(console)


ft.app(target=main)