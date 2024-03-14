from peewee import *

DB = SqliteDatabase('cars.db')

class BaseModel(Model):
	id = AutoField()

	class Meta:
			database = DB

class Car(BaseModel):
	model = TextField()

class User(BaseModel):
	name = TextField()
	surname = TextField()
	password = TextField()


def create_el(model_):
	new_model = Car(model=model_)
	new_model.save()

def get_el(id_):
	return Car.select(Car.model).where(Car.id==id_)[0].model

def del_el(id_):
	Car.delete().where(Car.id==id_).execute()

def update_el(id_, new_model):
	qry=Car.update({Car.model:new_model}).where(Car.id==id_)
	print (qry.sql())
	qry.execute()

def get_max_id():
	return Car.select(fn.MAX(Car.id)).scalar()

def check_id(id, table=Car):
	return len(table.select(table).where(table.id==id)) != 0


def reg_user(name, sur, psw):
		new_user = User(name=name, surname=sur, password=psw)
		new_user.save()

def check_name(name_, sur_):
	return len(User.select(User).where((User.name==name_) & (User.surname==sur_))) != 0

def check_password(name_, sur_, psw_):
	return len(User.select(User).where((User.name==name_)
																		& (User.surname==sur_)
																		& (User.password==psw_))) != 0

def init_table():
	global Car
	DB.drop_tables([Car, User])
	DB.create_tables([Car, User])

	cars = ['Toyota', 'Mercedes', 'Nissan', 'Skoda',
				'Mitsubishi', 'Lexus', 'Reno']
	for model in cars:
			create_el(model)
	reg_user('admin', 'admin', 'admin')