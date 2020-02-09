#!/usr/bin/env python

from faker import Faker

from app import Thing, db

print("\n 🌱 seeding db... \n")
db.drop_all()
db.create_all()
fake = Faker()
things = []

for _ in range(1, 100):
    thing = Thing(name=fake.word(), description=fake.sentence())
    things.append(thing)

db.session.bulk_save_objects(things)
db.session.commit()
print("\n 🌿 done \n")
