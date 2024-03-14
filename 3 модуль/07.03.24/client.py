import requests
import flet as ft
from re import fullmatch

def main(page: ft.Page):
	page.title = "Cars database remote control"

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

	def close_dlg(e):
		alert.open = False
		page.update()

	def open_dlg(e):
		page.dialog = alert
		alert.open = True
		page.update()

	def login(e):
		resp = requests.get(f'http://127.0.0.1:4001/login/{name.value}/{surname.value}/{password.value}')
		status = resp.json()['Status']
		print(resp.json())
		if status == 'Success':
			page.go("/cars")
		else:
			alert.content = ft.Text(f"{status}")
			open_dlg(1)

	name = ft.TextField(label='Name')
	surname = ft.TextField(label='Surname')
	password = ft.TextField(label='Password', password=True, can_reveal_password=False)
	alert = ft.AlertDialog(
		title=ft.Text('Something went wrong!'),
		content=ft.Text(''),
		actions=[ft.TextButton('OK', on_click=close_dlg)]
	)

	page.title = "Car database remote control"
	login_info = ft.Text('By default: admin admin admin')
	info = ft.Text('This program performs CRUD operations with database (creates, reads, updates or deletes car models)\nTo use it type your queries into following fields abd press enter:',
								size=18)
	cr_field = ft.TextField(label='Create car model', on_submit=create)
	read_field = ft.TextField(label='Search for model by id', on_submit=read)
	upd_field = ft.TextField(label='Update model by id', on_submit=update)
	del_field = ft.TextField(label='Delete model by id', on_submit=delete)
	console = ft.Text('-- Output --', text_align=ft.TextAlign.CENTER,
									  size=18, weight=ft.FontWeight.W_400,)

	def route_change(route):
			page.views.clear()
			page.views.append(
					ft.View(
							"/",
							[
								login_info,
								name, surname, password,
								ft.AppBar(title=ft.Text("Login"), bgcolor=ft.colors.SURFACE_VARIANT),
								ft.ElevatedButton("Login", on_click=login),
							],
					)
			)
			if page.route == "/cars":
					page.views.append(
							ft.View(
									"/cars",
									[
										ft.AppBar(title=ft.Text("Remote control"), bgcolor=ft.colors.SURFACE_VARIANT),
										info,
										cr_field, read_field, upd_field, del_field,
										console,
									],
							)
					)
			page.update()

	def view_pop(view):
			page.views.pop()
			top_view = page.views[-1]
			page.go(top_view.route)

	page.on_route_change = route_change
	page.on_view_pop = view_pop
	page.go(page.route)


def cars(page: ft.Page):

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


ft.app(target=main, view=ft.AppView.WEB_BROWSER)