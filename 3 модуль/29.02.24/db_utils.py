from peewee import *

DB = SqliteDatabase('cars.db')

class Car(Model):
	id = AutoField()
	model = TextField()

	class Meta:
			database = DB


def create_el(model_):
	new_user = Car(model=model_)
	new_user.save()


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


def init_table():
	global Car
	DB.drop_tables([Car])
	DB.create_tables([Car])
	cars = ['Toyota', 'Mercedes', 'Nissan', 'Skoda',
				'Mitsubishi', 'Lexus', 'Reno']
	for model in cars:
			create_el(model)
