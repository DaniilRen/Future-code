from flask import Flask, render_template, request
from peewee import *
import names

def fill_table(n=10):
    for _ in range(n):
        new_user = Users(name=names.get_full_name())
        new_user.save()


db = SqliteDatabase('task5.db')

class Users(Model):
	id = AutoField()
	name = TextField()

	class Meta:
			database = db

db.drop_tables([Users])
db.create_tables([Users])
fill_table()

app = Flask(__name__)
@app.route('/')
def index():
	id = request.args.get('id')
	if id:
		user_name = Users.select(Users.name).where(Users.id == id)[0].name
		return render_template('index5.html', id=id, name=user_name)
	return render_template('index5.html', id='empty', name='Error: Incorrect id')

app.run(host='0.0.0.0', port=4002, debug=True)