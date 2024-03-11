from peewee import *
import random

db = SqliteDatabase('shop.db')


def fill_table(n=10):
    models = ['Xiaomi', 'Samsung', 'Apple', 'Huawei']
    prices = [100*i for i in range(8)]
    for i in range(n):
        new_phone = Phone(model=random.choice(models),
                          price=random.choice(prices))
        new_phone.save()


def get_low_priced_phones():
    query = Phone.select(Phone.model, Phone.price).where(
        Phone.price <= 400)
    return [(p.model, p.price) for p in query]


def change_price_of_model(model='Samsung'):
    target = Phone.select().where(Phone.model == model)
    for p in target:
        p.price += 2000
        p.save()


def delete_phones(model='Xiaomi'):
    target = Phone.select().where(Phone.model == model)
    for p in target:
        p.delete_instance()


class Phone(Model):
    model = CharField()
    price = IntegerField()

    class Meta:
        database = db


if __name__ == "__main__":
    db.drop_tables([Phone])
    db.create_tables([Phone])

    fill_table()
    print(*get_low_priced_phones())
    change_price_of_model()
    delete_phones()


