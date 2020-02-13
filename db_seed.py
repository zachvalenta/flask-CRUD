#!/usr/bin/env python

from random import randint

from faker import Faker

from app import Thing, db

print("\n 🌱 seeding db... \n")
db.drop_all()
db.create_all()
fake = Faker()

names = []
for _ in range(0, 3):
    names.append(fake.word())

things = []
for _ in range(1, 100):
    thing = Thing(name=names[randint(0, 2)], description=fake.sentence())
    things.append(thing)

db.session.bulk_save_objects(things)
db.session.commit()
print("\n 🌿 done \n")
