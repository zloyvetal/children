from datetime import date

from peewee import *


db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

db.connect()
db.create_tables([Person, Pet])

uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
uncle_bob.save()
grandma = Person.create(name='Grandma L.', birthday=date(1935, 3, 1))
grandma.save()
herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
herb.save()

bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
bob_kitty.save()
herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
herb_fido.save()
herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
herb_mittens.save()
herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
herb_mittens_jr.save()


a = Person.select().where(Person.birthday == date(1950, 5, 5)).get()
print(a.birthday)