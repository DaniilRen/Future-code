import hashlib
from peewee import *
import redis

db = SqliteDatabase('users.db')
r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def register():
    print('<--- Регистрация -->')
    name = input('Введите имя: ')
    if len(name) == 0:
        print('Введите непустое имя!')
    elif name in [u.name for u in Users.select(Users.name)]:
        print('Это имя уже используется!')

    password = hashlib.sha256(bytes("{}".format(
        input('Введите пароль: ')),'utf-8')).hexdigest()
    new_user = Users(name=name, password=password)
    new_user.save()
    print('Пользователь зарегистрирован')
    r.set('active_session', name)
    return True


def login(printing=True):
    if r.get('active_session') != '0':
        print('Вы уже вошли в систему')
        return

    if printing:
        print('<--- Авторизация -->')

    name = input('Введите имя: ')
    if len(name) == 0:
        print('Введите непустое имя!')
    elif name in [u.name for u in Users.select(Users.name)]:
        password = hashlib.sha256(bytes("{}".format(
            input('Введите пароль: ')), 'utf-8')).hexdigest()
        if password == [i.password for i in
            Users.select(Users.password).where(Users.name == name)][0]:
            print('Пользователь авторизован')
            r.set('active_session', name)
            return (True, name)
        else:
            print('Неверный пароль!')
    else:
        print('Пользователь не найден!')


def change():
    print('<--- Изменение данных --->')
    status = r.get('active_session')

    if status != '0':
        query = Users.select(Users).where(Users.name == status)
        data = input('Что вы хотите изменить? (<П>-пароль, <И>-имя): ').strip().capitalize()
        if data == 'П':
            for u in query:
                if u.name == status:
                    u.password = hashlib.sha256(bytes("{}".format(
                        input('Введите новый пароль: ')), 'utf-8')).hexdigest()
                    u.save()
        elif data == 'И':
            for u in query:
                if u.name == status:
                    u.name = input('Введите новое имя: ')
                    u.save()
        else:
            print('Введите корректный вариант ответа')
    else:
        print('Вы не вошли в систему!')


class Users(Model):
    id = AutoField()
    name = TextField(unique=True)
    password = TextField()

    class Meta:
        database = db


if __name__ == "__main__":
    r.set('active_session', 0)
    db.drop_tables([Users])
    db.create_tables([Users])

    register()
    login()
    change()
